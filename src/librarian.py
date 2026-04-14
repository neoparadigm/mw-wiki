"""
MW-Wiki Librarian
-----------------
Reads raw crawled articles from /raw/
Classifies each into a canonical topic from topic_taxonomy.yaml
Creates or merges topic files in /wiki/
Updates _index.yaml, _gaps.md, _sources.md

Uses Ollama (local, zero API cost) for classification and synthesis.
Claude is NOT used here — cost reserved for query time.

Usage:
    python src/librarian.py --process-all    # process all unprocessed raw files
    python src/librarian.py --file raw/x.md  # process one file
    python src/librarian.py --rebuild-index  # rebuild _index.yaml from existing topic files
"""

import json
import logging
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import ollama
import yaml

# ── CONFIG ────────────────────────────────────────────────────────────────────

BASE_DIR    = Path(__file__).parent.parent
CONFIG_DIR  = BASE_DIR / "config"
RAW_DIR     = BASE_DIR / "raw"
WIKI_DIR    = BASE_DIR / "wiki"
PROCESSED_LOG = RAW_DIR / ".processed.txt"  # tracks which raw files are done

# Ollama model — mistral is good balance of quality vs speed on Mac Mini
# Change to "phi4-mini" if memory constrained
OLLAMA_MODEL = "mistral"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("librarian")


# ── TAXONOMY LOADER ───────────────────────────────────────────────────────────

def load_taxonomy() -> dict:
    """Load topic taxonomy. Returns dict keyed by path."""
    with open(CONFIG_DIR / "topic_taxonomy.yaml") as f:
        raw = yaml.safe_load(f)
    return {t["path"]: t for t in raw["topics"]}


def taxonomy_as_list_str(taxonomy: dict) -> str:
    """Format taxonomy as a compact string for prompts."""
    lines = []
    for path, topic in taxonomy.items():
        keywords = ", ".join(topic["keywords"][:5])
        lines.append(f"  {path} — {topic['title']} [{keywords}]")
    return "\n".join(lines)


# ── PROCESSED TRACKING ────────────────────────────────────────────────────────

def get_processed() -> set[str]:
    if not PROCESSED_LOG.exists():
        return set()
    return set(PROCESSED_LOG.read_text().strip().splitlines())


def mark_processed(filename: str) -> None:
    with open(PROCESSED_LOG, "a") as f:
        f.write(filename + "\n")


# ── OLLAMA HELPERS ────────────────────────────────────────────────────────────

def ollama_call(prompt: str, max_tokens: int = 1500) -> str:
    """Single Ollama call. Returns text or empty string on failure."""
    try:
        response = ollama.generate(
            model=OLLAMA_MODEL,
            prompt=prompt,
            options={"num_predict": max_tokens, "temperature": 0.1}
        )
        return response["response"].strip()
    except Exception as e:
        log.error(f"Ollama error: {e}")
        return ""


# ── CLASSIFICATION ────────────────────────────────────────────────────────────

def classify_article(
    title: str,
    content: str,
    taxonomy_str: str
) -> str | None:
    """Simple keyword-based classification. Fast and reliable."""
    taxonomy = load_taxonomy()
    text = (title + " " + content).lower()

    best_path = None
    best_score = 0
    title_lower = title.lower()
    # First 300 words for lead paragraph check
    lead = ' '.join(content.split()[:300]).lower()

    for path, info in taxonomy.items():
        score = 0
        for kw in info.get("keywords", []):
            kw_lower = kw.lower()
            # Title match = 5x weight — article is specifically about this topic
            if kw_lower in title_lower:
                score += 5
            # Lead paragraph match = 3x weight — topic is primary subject
            elif kw_lower in lead:
                score += 3
            # Body match = 1x weight — topic mentioned in passing
            elif kw_lower in text:
                score += 1
        if score > best_score:
            best_score = score
            best_path = path

    # Require score of 5+ meaning at least one title match
    # This ensures the article is specifically about the topic
    if best_score < 5:
        log.info(f"  Score too low ({best_score}) — no title match, skipping")
        return None

    log.info(f"  Classified as: {best_path} (score {best_score})")
    return best_path


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown file. Returns (metadata, body)."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2].strip()


def render_frontmatter(meta: dict) -> str:
    """Render metadata dict back to YAML frontmatter block."""
    return "---\n" + yaml.dump(meta, default_flow_style=False, allow_unicode=True) + "---\n\n"


def topic_file_path(topic_path: str) -> Path:
    """Convert topic path string to filesystem path."""
    return WIKI_DIR / (topic_path + ".md")


def create_topic_file(
    topic_path:    str,
    topic_info:    dict,
    article_title: str,
    article_url:   str,
    article_author:str,
    article_date:  str,
    article_body:  str,
) -> None:
    """Create a new topic file from scratch using Ollama synthesis."""
    log.info(f"  CREATE topic: {topic_path}")

    prompt = f"""You are creating a structured knowledge base entry for a Modern Workplace wiki.

Source article: "{article_title}"
Source URL: {article_url}
Author: {article_author}

Article content:
{article_body[:4000]}

Create a wiki entry for the topic: "{topic_info['title']}"

Format exactly as follows:

## Overview
[2-3 sentences explaining what this topic is and why it matters]

## Key Concepts
[Bullet points covering the core concepts]

## Configuration
[Step-by-step configuration guidance where applicable]

## Common Pitfalls
[What goes wrong most often and why]

## KQL / PowerShell
[Include any relevant queries or scripts from the article, properly formatted]

## Related Topics
[List 2-4 related topic paths from this list: {', '.join(topic_info.get('keywords', [])[:5])}]

Rules:
- Be specific and technical. This is for practitioners, not beginners.
- Do not pad with generic content. Only include what the source article actually covers.
- If the article does not cover a section, omit that section entirely.
- Do not reproduce large verbatim passages from the article."""

    synthesised = ollama_call(prompt, max_tokens=1500)

    if not synthesised:
        log.warning(f"  Ollama returned empty for {topic_path} — writing stub")
        synthesised = f"## Overview\nStub — synthesis failed for this topic.\n"

    today = datetime.now().strftime("%Y-%m-%d")
    stale_date = (
        datetime.now() + timedelta(days=topic_info.get("stale_days", 90))
    ).strftime("%Y-%m-%d")

    meta = {
        "topic":          topic_path,
        "title":          topic_info["title"],
        "domain":         topic_path.split("/")[0],
        "last_synthesised": today,
        "stale_after":    stale_date,
        "sources": [{
            "url":     article_url,
            "author":  article_author,
            "title":   article_title,
            "crawled": today,
            "date":    article_date,
        }],
        "conflicts": [],
        "gaps":      [],
    }

    filepath = topic_file_path(topic_path)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(
        render_frontmatter(meta) + f"# {topic_info['title']}\n\n" + synthesised,
        encoding="utf-8"
    )
    log.info(f"  CREATED: {filepath.relative_to(BASE_DIR)}")


def merge_into_topic_file(
    topic_path:     str,
    topic_info:     dict,
    article_title:  str,
    article_url:    str,
    article_author: str,
    article_date:   str,
    article_body:   str,
) -> None:
    """Merge a new source into an existing topic file."""
    log.info(f"  MERGE into topic: {topic_path}")

    filepath = topic_file_path(topic_path)
    existing_content = filepath.read_text(encoding="utf-8")
    meta, existing_body = parse_frontmatter(existing_content)

    # Check if this URL already indexed
    existing_urls = [s.get("url") for s in meta.get("sources", [])]
    if article_url in existing_urls:
        log.info(f"  ALREADY INDEXED: {article_url}")
        return

    # Cap sources per topic file at 6
    if len(meta.get("sources", [])) >= 6:
        log.info(f"  TOPIC FULL (6 sources max): {topic_path}")
        return

    prompt = f"""You are updating a structured knowledge base entry for a Modern Workplace wiki.

Existing wiki entry:
{existing_body[:3000]}

New source article: "{article_title}"
Author: {article_author}
New source content:
{article_body[:3000]}

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: {article_author} says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged."""

    updated_body = ollama_call(prompt, max_tokens=2000)

    if not updated_body:
        log.warning(f"  Ollama returned empty for merge — keeping existing")
        return

    # Detect conflicts in the updated body
    conflicts_found = re.findall(r'\[CONFLICT:[^\]]+\]', updated_body)

    # Update metadata
    today = datetime.now().strftime("%Y-%m-%d")
    stale_date = (
        datetime.now() + timedelta(days=topic_info.get("stale_days", 90))
    ).strftime("%Y-%m-%d")

    sources = meta.get("sources", [])
    sources.append({
        "url":     article_url,
        "author":  article_author,
        "title":   article_title,
        "crawled": today,
        "date":    article_date,
    })

    conflicts = meta.get("conflicts", [])
    for c in conflicts_found:
        if c not in conflicts:
            conflicts.append(c)

    meta.update({
        "last_synthesised": today,
        "stale_after":      stale_date,
        "sources":          sources,
        "conflicts":        conflicts,
    })

    filepath.write_text(
        render_frontmatter(meta) + updated_body,
        encoding="utf-8"
    )
    log.info(f"  MERGED: {len(sources)} sources now in {filepath.relative_to(BASE_DIR)}")


# ── INDEX AND GAP MANAGEMENT ─────────────────────────────────────────────────

def rebuild_index() -> None:
    """
    Rebuild _index.yaml from all existing topic files.
    Run after bulk processing or to repair a corrupted index.
    """
    log.info("Rebuilding _index.yaml...")
    taxonomy = load_taxonomy()
    index_entries = []

    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        # Skip meta files
        if md_file.name.startswith("_"):
            continue
        content = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        if not meta:
            continue

        topic_path = meta.get("topic")
        if not topic_path or topic_path not in taxonomy:
            continue

        topic_info = taxonomy[topic_path]
        entry = {
            "id":           topic_path,
            "title":        meta.get("title", topic_info["title"]),
            "domain":       topic_path.split("/")[0],
            "subdomain":    topic_path.split("/")[1] if "/" in topic_path else "",
            "keywords":     topic_info["keywords"],
            "sources":      len(meta.get("sources", [])),
            "last_updated": meta.get("last_synthesised", ""),
            "stale_after":  meta.get("stale_after", ""),
            "has_conflicts": bool(meta.get("conflicts")),
            "related":      [],  # TODO: derive from Related Topics section
        }
        index_entries.append(entry)

    index = {"topics": index_entries, "generated": datetime.now().strftime("%Y-%m-%d %H:%M")}
    index_path = WIKI_DIR / "_index.yaml"
    with open(index_path, "w") as f:
        yaml.dump(index, f, default_flow_style=False, allow_unicode=True)

    log.info(f"_index.yaml rebuilt: {len(index_entries)} topics")


def update_gaps() -> None:
    """
    Write _gaps.md — topics in taxonomy with no wiki file yet.
    """
    taxonomy   = load_taxonomy()
    gap_topics = []

    for path, info in taxonomy.items():
        filepath = topic_file_path(path)
        if not filepath.exists():
            gap_topics.append((path, info["title"]))

    lines = [
        "# MW-Wiki — Known Gaps\n",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
        f"Topics with no sources yet: {len(gap_topics)}\n\n",
        "These are topics the wiki knows should exist but has no articles for yet.\n",
        "Submit a PR to `config/seed_list.yaml` with a source URL to fill a gap.\n\n",
        "| Topic Path | Title |\n",
        "|---|---|\n",
    ]
    for path, title in sorted(gap_topics):
        lines.append(f"| `{path}` | {title} |\n")

    (WIKI_DIR / "_gaps.md").write_text("".join(lines), encoding="utf-8")
    log.info(f"_gaps.md updated: {len(gap_topics)} gaps")


def update_sources() -> None:
    """
    Write _sources.md — all crawled sources and what they contributed.
    """
    all_sources = []

    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        content = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        for source in meta.get("sources", []):
            all_sources.append({
                "topic": meta.get("topic", ""),
                **source
            })

    # Deduplicate by URL
    seen = set()
    unique = []
    for s in all_sources:
        if s["url"] not in seen:
            seen.add(s["url"])
            unique.append(s)

    # Group by author
    by_author: dict[str, list] = {}
    for s in sorted(unique, key=lambda x: x.get("author", "")):
        author = s.get("author", "Unknown")
        by_author.setdefault(author, []).append(s)

    lines = [
        "# MW-Wiki — Source Attribution\n\n",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
        f"Total unique sources indexed: {len(unique)}\n\n",
        "Every source that has contributed knowledge to this wiki.\n\n",
    ]
    for author, sources in sorted(by_author.items()):
        lines.append(f"## {author} ({len(sources)} articles)\n\n")
        for s in sources:
            title   = s.get("title", "Untitled")
            url     = s.get("url", "")
            crawled = s.get("crawled", "")
            topic   = s.get("topic", "")
            lines.append(f"- [{title}]({url}) → `{topic}` _(crawled {crawled})_\n")
        lines.append("\n")

    (WIKI_DIR / "_sources.md").write_text("".join(lines), encoding="utf-8")
    log.info(f"_sources.md updated: {len(unique)} unique sources")


def update_conflicts() -> None:
    """
    Write _conflicts.md — topics where sources disagree.
    """
    conflicts = []

    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        content = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(content)
        file_conflicts = meta.get("conflicts", [])
        inline_conflicts = re.findall(r'\[CONFLICT:[^\]]+\]', body)
        all_conflicts = file_conflicts + inline_conflicts
        if all_conflicts:
            conflicts.append({
                "topic": meta.get("topic", ""),
                "title": meta.get("title", ""),
                "conflicts": all_conflicts
            })

    lines = [
        "# MW-Wiki — Source Conflicts\n\n",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n",
        "Topics where indexed sources disagree. "
        "Review the topic file and the original sources before relying on this guidance.\n\n",
    ]
    if not conflicts:
        lines.append("_No conflicts detected in current corpus._\n")
    else:
        for c in conflicts:
            lines.append(f"## {c['title']}\n")
            lines.append(f"Topic: `{c['topic']}`\n\n")
            for conflict in c["conflicts"]:
                lines.append(f"- {conflict}\n")
            lines.append("\n")

    (WIKI_DIR / "_conflicts.md").write_text("".join(lines), encoding="utf-8")
    log.info(f"_conflicts.md updated: {len(conflicts)} topics with conflicts")


def update_stale() -> None:
    """
    Write _stale.md — topic files past their stale_after date.
    """
    today  = datetime.now().date()
    stale  = []

    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        content = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        stale_after = meta.get("stale_after")
        if stale_after:
            try:
                stale_date = datetime.strptime(stale_after, "%Y-%m-%d").date()
                if stale_date < today:
                    days_stale = (today - stale_date).days
                    stale.append({
                        "topic": meta.get("topic", ""),
                        "title": meta.get("title", ""),
                        "stale_after": stale_after,
                        "days_stale": days_stale,
                    })
            except ValueError:
                pass

    lines = [
        "# MW-Wiki — Stale Topics\n\n",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n",
        "Topics that have not been refreshed within their stale window.\n",
        "Microsoft ships changes frequently. Verify against current docs before implementing.\n\n",
    ]
    if not stale:
        lines.append("_All topics are within their freshness window._\n")
    else:
        lines.append("| Topic | Title | Stale Since | Days Overdue |\n")
        lines.append("|---|---|---|---|\n")
        for s in sorted(stale, key=lambda x: x["days_stale"], reverse=True):
            lines.append(
                f"| `{s['topic']}` | {s['title']} | {s['stale_after']} | {s['days_stale']} |\n"
            )

    (WIKI_DIR / "_stale.md").write_text("".join(lines), encoding="utf-8")
    log.info(f"_stale.md updated: {len(stale)} stale topics")


# ── PROCESS A SINGLE RAW FILE ────────────────────────────────────────────────

def process_raw_file(raw_file: Path, taxonomy: dict) -> bool:
    """
    Process one raw markdown file through the librarian pipeline.
    Returns True if successfully processed.
    """
    log.info(f"\nProcessing: {raw_file.name}")

    content = raw_file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    if not meta:
        log.warning(f"  No frontmatter — skipping {raw_file.name}")
        return False

    title   = meta.get("title", "Untitled")
    url     = meta.get("source_url", "")
    author  = meta.get("author", "Unknown")
    date    = meta.get("published", "")

    if not url:
        log.warning(f"  No source URL — skipping")
        return False

    # Step 1: Classify
    taxonomy_str = taxonomy_as_list_str(taxonomy)
    topic_path   = classify_article(title, body, taxonomy_str)

    if not topic_path:
        log.info(f"  NO_MATCH for classification: {title}")
        return False

    log.info(f"  Classified as: {topic_path}")
    topic_info = taxonomy[topic_path]

    # Step 2: Create or merge
    filepath = topic_file_path(topic_path)
    if filepath.exists():
        merge_into_topic_file(topic_path, topic_info, title, url, author, date, body)
    else:
        create_topic_file(topic_path, topic_info, title, url, author, date, body)

    return True


# ── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(description="MW-Wiki Librarian")
    group  = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--process-all",   action="store_true", help="Process all unprocessed raw files")
    group.add_argument("--file",          type=str,            help="Process a single raw file")
    group.add_argument("--rebuild-index", action="store_true", help="Rebuild index and meta files only")
    args = parser.parse_args()

    # Verify Ollama is running (unless just rebuilding index)
    if not args.rebuild_index:
        try:
            ollama.list()
            log.info(f"Ollama connected — model: {OLLAMA_MODEL}")
        except Exception:
            log.error("Ollama is not running. Start it with: ollama serve")
            sys.exit(1)

    taxonomy  = load_taxonomy()
    processed = get_processed()

    if args.rebuild_index:
        rebuild_index()
        update_gaps()
        update_sources()
        update_conflicts()
        update_stale()
        return

    if args.file:
        raw_file = Path(args.file)
        if not raw_file.exists():
            log.error(f"File not found: {args.file}")
            sys.exit(1)
        success = process_raw_file(raw_file, taxonomy)
        if success:
            mark_processed(raw_file.name)
            rebuild_index()
            update_gaps()
            update_sources()
            update_conflicts()
            update_stale()
        return

    if args.process_all:
        raw_files = [
            f for f in sorted(RAW_DIR.glob("*.md"))
            if f.name not in processed and not f.name.startswith(".")
        ]
        log.info(f"Files to process: {len(raw_files)}")

        success_count = 0
        fail_count    = 0

        for i, raw_file in enumerate(raw_files, 1):
            log.info(f"\n[{i}/{len(raw_files)}]")
            try:
                success = process_raw_file(raw_file, taxonomy)
                if success:
                    mark_processed(raw_file.name)
                    success_count += 1
                else:
                    fail_count += 1
            except Exception as e:
                log.error(f"  Unhandled error on {raw_file.name}: {e}")
                fail_count += 1

            # Rebuild meta files every 10 articles
            if i % 10 == 0:
                log.info("\n--- Updating meta files ---")
                rebuild_index()
                update_gaps()
                update_sources()

        # Final rebuild
        log.info("\n=== Final meta rebuild ===")
        rebuild_index()
        update_gaps()
        update_sources()
        update_conflicts()
        update_stale()

        log.info(f"\n{'='*60}")
        log.info(f"LIBRARIAN COMPLETE")
        log.info(f"  Processed: {success_count}")
        log.info(f"  Failed:    {fail_count}")
        log.info(f"  See: {WIKI_DIR / '_gaps.md'}")
        log.info(f"{'='*60}")


if __name__ == "__main__":
    main()
