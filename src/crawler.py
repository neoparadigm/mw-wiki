"""
MW-Wiki Crawler
---------------
Fetches articles from seed_list.yaml sources.
Respects robots.txt — refuses to crawl disallowed URLs.
Converts HTML to clean markdown, strips nav/ads/footer.
Saves one .md file per article to /raw/ with frontmatter.

Usage:
    python src/crawler.py --source "Daniel Chronlund"  # one source
    python src/crawler.py --all                         # all sources
    python src/crawler.py --url https://...             # single URL
"""

import asyncio
import hashlib
import logging
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import httpx
import yaml
from markdownify import markdownify as md

# ── CONFIG ────────────────────────────────────────────────────────────────────

BASE_DIR    = Path(__file__).parent.parent
CONFIG_DIR  = BASE_DIR / "config"
RAW_DIR     = BASE_DIR / "raw"
RAW_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "MW-Wiki-Bot/1.0 (community knowledge synthesis; "
                  "respects robots.txt; "
                  "contact: github.com/neoparadigm/mw-wiki)"
}

# Conservative — we are a guest on these sites
CRAWL_DELAY       = 2.0   # seconds between requests per domain
MAX_ARTICLES      = 200   # safety cap per source
REQUEST_TIMEOUT   = 20    # seconds
MAX_CONTENT_BYTES = 500_000  # 500KB — skip giant pages

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("crawler")


# ── ROBOTS ────────────────────────────────────────────────────────────────────

_robots_cache: dict[str, RobotFileParser] = {}

def can_fetch(url: str, robots_url: str) -> bool:
    """Check robots.txt. Defaults to DISALLOW on any error — we never assume permission."""
    if robots_url not in _robots_cache:
        rp = RobotFileParser()
        rp.set_url(robots_url)
        try:
            rp.read()
            _robots_cache[robots_url] = rp
            log.info(f"robots.txt loaded: {robots_url}")
        except Exception as e:
            log.warning(f"Could not read robots.txt at {robots_url}: {e} — treating as DISALLOW")
            return False
    return _robots_cache[robots_url].can_fetch(HEADERS["User-Agent"], url)


# ── URL DISCOVERY ─────────────────────────────────────────────────────────────

def is_article_url(url: str, base_url: str) -> bool:
    """
    Heuristic: is this URL likely a blog article rather than a category/tag/page?
    Conservative — we prefer to miss articles than crawl noise.
    """
    parsed   = urlparse(url)
    base     = urlparse(base_url)

    # Must be same domain
    if parsed.netloc and parsed.netloc != base.netloc:
        return False

    path = parsed.path.rstrip("/")

    # Skip obvious non-articles
    skip_patterns = [
        r"^/$",
        r"/page/\d+",
        r"/tag/",
        r"/category/",
        r"/author/",
        r"/feed",
        r"\.xml$",
        r"\.pdf$",
        r"\.zip$",
        r"/wp-content/",
        r"/wp-admin/",
        r"#",
        r"\?",
    ]
    for pattern in skip_patterns:
        if re.search(pattern, url):
            return False

    # Must have meaningful path depth (not just homepage)
    segments = [s for s in path.split("/") if s]
    if len(segments) < 1:
        return False

    return True


async def discover_article_urls(
    client: httpx.AsyncClient,
    base_url: str,
    robots_url: str,
    depth: int = 2,
) -> list[str]:
    """
    Crawls the base URL and discovers article links up to `depth` levels.
    Returns deduplicated list of article URLs.
    """
    visited  = set()
    articles = []
    queue    = [base_url]

    for level in range(depth):
        next_queue = []
        for url in queue:
            if url in visited:
                continue
            visited.add(url)

            if not can_fetch(url, robots_url):
                log.info(f"  robots.txt DISALLOW: {url}")
                continue

            try:
                await asyncio.sleep(CRAWL_DELAY)
                resp = await client.get(url, follow_redirects=True, timeout=REQUEST_TIMEOUT)
                if resp.status_code != 200:
                    continue

                # Find all links
                links = re.findall(r'href=["\']([^"\']+)["\']', resp.text)
                for link in links:
                    full_url = urljoin(url, link).split("#")[0].rstrip("/")
                    if full_url not in visited and is_article_url(full_url, base_url):
                        if level == depth - 1:
                            # Last level — these are articles, not further crawl targets
                            if full_url not in articles:
                                articles.append(full_url)
                        else:
                            next_queue.append(full_url)

            except Exception as e:
                log.warning(f"  Discovery error {url}: {e}")
                continue

        queue = next_queue

    # Also treat base-level discovered URLs as articles
    for url in queue:
        if url not in articles and is_article_url(url, base_url):
            articles.append(url)

    log.info(f"  Discovered {len(articles)} candidate URLs at {base_url}")
    return articles[:MAX_ARTICLES]


# ── CONTENT EXTRACTION ────────────────────────────────────────────────────────

def extract_title(html: str) -> str:
    """Extract article title from HTML."""
    # Try OG title first
    m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
    if m:
        return m.group(1).strip()
    # Fall back to h1
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', html, re.I)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    # Fall back to title tag
    m = re.search(r'<title>([^<]+)</title>', html, re.I)
    if m:
        return m.group(1).strip()
    return "Untitled"


def extract_author(html: str, default_author: str) -> str:
    """Extract author from meta tags or return default."""
    m = re.search(r'<meta[^>]+name=["\']author["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
    if m:
        return m.group(1).strip()
    return default_author


def extract_date(html: str) -> str:
    """Extract publish date from meta tags or structured data."""
    patterns = [
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\']([^"\']+)["\']',
        r'datetime=["\'](\d{4}-\d{2}-\d{2})',
    ]
    for pattern in patterns:
        m = re.search(pattern, html, re.I)
        if m:
            return m.group(1)[:10]  # Return YYYY-MM-DD only
    return ""


def html_to_clean_markdown(html: str) -> str:
    """
    Convert HTML to clean markdown.
    Aggressively strips navigation, headers, footers, sidebars, ads.
    Preserves: headings, paragraphs, lists, code blocks, links.
    """
    # Remove script, style, nav, header, footer, sidebar, comments
    remove_tags = [
        r'<script[^>]*>[\s\S]*?</script>',
        r'<style[^>]*>[\s\S]*?</style>',
        r'<nav[^>]*>[\s\S]*?</nav>',
        r'<header[^>]*>[\s\S]*?</header>',
        r'<footer[^>]*>[\s\S]*?</footer>',
        r'<aside[^>]*>[\s\S]*?</aside>',
        r'<!--[\s\S]*?-->',
        r'<form[^>]*>[\s\S]*?</form>',
        r'<noscript[^>]*>[\s\S]*?</noscript>',
    ]
    for pattern in remove_tags:
        html = re.sub(pattern, '', html, flags=re.I | re.S)

    # Remove elements by common class/id patterns for navigation/ads
    html = re.sub(
        r'<[^>]+(?:class|id)=["\'][^"\']*(?:nav|menu|sidebar|footer|header|'
        r'banner|advertisement|subscribe|newsletter|comment|social|share|'
        r'related|widget|breadcrumb)[^"\']*["\'][^>]*>[\s\S]*?</\w+>',
        '', html, flags=re.I | re.S
    )

    # Convert to markdown
    content = md(html, heading_style="ATX", bullets="-", strip=["img"])

    # Clean up excessive whitespace
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    content = re.sub(r'[ \t]+\n', '\n', content)
    content = content.strip()

    return content


def url_to_filename(url: str) -> str:
    """Convert URL to a safe filesystem filename."""
    parsed = urlparse(url)
    path   = parsed.path.strip("/").replace("/", "_")
    if not path:
        path  = "index"
    # Truncate and add hash suffix for uniqueness
    h     = hashlib.md5(url.encode()).hexdigest()[:8]
    clean = re.sub(r'[^\w\-]', '_', path)[:80]
    return f"{clean}_{h}.md"


# ── ARTICLE FETCHER ───────────────────────────────────────────────────────────

async def fetch_article(
    client:         httpx.AsyncClient,
    url:            str,
    source_name:    str,
    author:         str,
    robots_url:     str,
    focus_domains:  list[str],
) -> bool:
    """
    Fetch a single article URL, convert to markdown, save to /raw/.
    Returns True if saved, False if skipped.
    """
    if not can_fetch(url, robots_url):
        log.info(f"  SKIP (robots): {url}")
        return False

    filename = RAW_DIR / url_to_filename(url)
    if filename.exists():
        log.info(f"  CACHED: {url}")
        return False  # Already fetched

    try:
        await asyncio.sleep(CRAWL_DELAY)
        resp = await client.get(url, follow_redirects=True, timeout=REQUEST_TIMEOUT)

        if resp.status_code != 200:
            log.warning(f"  HTTP {resp.status_code}: {url}")
            return False

        if len(resp.content) > MAX_CONTENT_BYTES:
            log.info(f"  SKIP (too large {len(resp.content)/1000:.0f}KB): {url}")
            return False

        content_type = resp.headers.get("content-type", "")
        if "html" not in content_type:
            log.info(f"  SKIP (not HTML): {url}")
            return False

        html         = resp.text
        title        = extract_title(html)
        article_auth = extract_author(html, author)
        pub_date     = extract_date(html)
        body_md      = html_to_clean_markdown(html)

        # Skip very short content — likely a page, not an article
        word_count = len(body_md.split())
        if word_count < 200:
            log.info(f"  SKIP (too short {word_count} words): {url}")
            return False

        # Build the raw file with frontmatter
        frontmatter = f"""---
source_url: {url}
source_name: {source_name}
author: {article_auth}
title: "{title.replace('"', "'")}"
published: "{pub_date}"
crawled: "{datetime.now().strftime('%Y-%m-%d')}"
focus_domains: {focus_domains}
word_count: {word_count}
---

# {title}

"""
        full_content = frontmatter + body_md

        filename.write_text(full_content, encoding="utf-8")
        log.info(f"  SAVED ({word_count}w): {title[:60]} — {url}")
        return True

    except httpx.TimeoutException:
        log.warning(f"  TIMEOUT: {url}")
        return False
    except Exception as e:
        log.warning(f"  ERROR {url}: {e}")
        return False


# ── MAIN CRAWL LOGIC ─────────────────────────────────────────────────────────

async def crawl_source(source: dict) -> dict[str, int]:
    """Crawl one source. Returns stats."""
    name        = source["name"]
    base_url    = source["base_url"]
    robots_url  = source["robots_url"]
    author      = source["author"]
    focus       = source["focus"]
    depth       = source.get("crawl_depth", 2)

    log.info(f"\n{'='*60}")
    log.info(f"SOURCE: {name}")
    log.info(f"BASE:   {base_url}")
    log.info(f"{'='*60}")

    stats = {"discovered": 0, "saved": 0, "skipped": 0}

    async with httpx.AsyncClient(headers=HEADERS) as client:
        # Discover article URLs
        urls = await discover_article_urls(client, base_url, robots_url, depth)
        stats["discovered"] = len(urls)

        # Fetch each article
        for url in urls:
            saved = await fetch_article(
                client, url, name, author, robots_url, focus
            )
            if saved:
                stats["saved"] += 1
            else:
                stats["skipped"] += 1

    log.info(f"\n{name}: {stats['saved']} saved, {stats['skipped']} skipped")
    return stats


async def crawl_all() -> None:
    """Crawl all sources in seed_list.yaml."""
    seed_path = CONFIG_DIR / "seed_list.yaml"
    with open(seed_path) as f:
        config = yaml.safe_load(f)

    sources = config["sources"]
    log.info(f"Starting crawl: {len(sources)} sources")

    total_saved = 0
    for source in sources:
        stats       = await crawl_source(source)
        total_saved += stats["saved"]

    log.info(f"\n{'='*60}")
    log.info(f"CRAWL COMPLETE: {total_saved} articles saved to {RAW_DIR}")
    log.info(f"{'='*60}")


async def crawl_single_url(url: str) -> None:
    """Crawl a single URL — for testing."""
    async with httpx.AsyncClient(headers=HEADERS) as client:
        saved = await fetch_article(
            client, url, "manual", "unknown",
            f"{urlparse(url).scheme}://{urlparse(url).netloc}/robots.txt",
            ["manual"]
        )
    if saved:
        log.info("Saved successfully")
    else:
        log.info("Not saved — check logs above")


# ── ENTRY POINT ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MW-Wiki Crawler")
    group  = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all",    action="store_true", help="Crawl all sources")
    group.add_argument("--source", type=str,            help="Crawl one source by name")
    group.add_argument("--url",    type=str,            help="Crawl a single URL")
    args = parser.parse_args()

    if args.all:
        asyncio.run(crawl_all())

    elif args.source:
        seed_path = CONFIG_DIR / "seed_list.yaml"
        with open(seed_path) as f:
            config = yaml.safe_load(f)
        matches = [s for s in config["sources"] if args.source.lower() in s["name"].lower()]
        if not matches:
            log.error(f"Source not found: {args.source}")
            sys.exit(1)
        for source in matches:
            asyncio.run(crawl_source(source))

    elif args.url:
        asyncio.run(crawl_single_url(args.url))
