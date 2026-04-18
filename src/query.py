"""
MW-Wiki Query Engine
--------------------
Four-stage pipeline:
  1. ROUTING   — keyword match against _index.yaml → topic file paths
  2. RETRIEVAL — load topic files, check staleness, check conflicts
  3. SYNTHESIS — single Claude API call, grounded answer with citations
  4. VALIDATION — verify citations present, flag uncited claims

Usage:
    python src/query.py "How do I block device code flow?"
    python src/query.py --interactive
"""

import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import anthropic
import yaml

# ── CONFIG ────────────────────────────────────────────────────────────────────

BASE_DIR  = Path(__file__).parent.parent
WIKI_DIR  = BASE_DIR / "wiki"
RAW_DIR   = BASE_DIR / "raw"
INDEX_PATH = WIKI_DIR / "_index.yaml"

# Claude model for synthesis — one call per query
CLAUDE_MODEL      = "claude-sonnet-4-20250514"
MAX_TOKENS        = 1000
MAX_CONTEXT_CHARS = 12000  # ~3000 tokens of context
MAX_TOPICS        = 2      # max topic files to load per query
MAX_RAW_FALLBACK  = 3      # max raw articles to include as fallback

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("query")


# ── DATA TYPES ────────────────────────────────────────────────────────────────

@dataclass
class TopicContext:
    path:               str
    title:              str
    body:               str
    sources:            list[dict]
    has_conflicts:      bool
    is_stale:           bool
    stale_days:         int = 0
    related_topics:     list[str] = None
    prerequisite_topics: list[str] = None


@dataclass
class QueryResult:
    question:      str
    answer:        str
    topics_used:   list[str]
    sources:       list[dict]
    warnings:      list[str] = field(default_factory=list)
    citations_ok:  bool = True


# ── STAGE 1: ROUTING ─────────────────────────────────────────────────────────

def load_index() -> list[dict]:
    """Load _index.yaml. Returns list of topic entries."""
    if not INDEX_PATH.exists():
        log.error(f"_index.yaml not found at {INDEX_PATH}")
        log.error("Run: python src/librarian.py --rebuild-index")
        return []
    with open(INDEX_PATH) as f:
        data = yaml.safe_load(f)
    return data.get("topics", [])


def route_question(question: str, index: list[dict]) -> list[str]:
    """
    Match question against topic keywords.
    Returns ordered list of topic paths — best matches first.
    Simple and transparent — no ML, no embeddings.
    """
    question_lower = question.lower()
    question_words = set(re.findall(r'\b\w+\b', question_lower))

    scores = []
    for topic in index:
        keywords = [kw.lower() for kw in topic.get("keywords", [])]
        title_words = set(re.findall(r'\b\w+\b', topic.get("title", "").lower()))

        # Score: keyword matches weighted higher than title matches
        kw_matches    = sum(1 for kw in keywords if kw in question_lower)
        title_matches = len(question_words & title_words)
        score         = (kw_matches * 3) + title_matches

        if score > 0:
            scores.append((score, topic["id"]))

    scores.sort(reverse=True)
    # Only include second topic if score is within 60% of top score
    top = scores[:1]
    if len(scores) > 1 and scores[0][0] > 0:
        if scores[1][0] >= scores[0][0] * 0.6:
            top.append(scores[1])
    top_paths = [path for _, path in top]

    log.info(f"Routing: '{question[:50]}...' → {top_paths}")
    return top_paths


# ── STAGE 2: RETRIEVAL ────────────────────────────────────────────────────────

def load_topic(topic_path: str) -> TopicContext | None:
    """Load a topic file and parse its contents."""
    filepath = WIKI_DIR / (topic_path + ".md")
    if not filepath.exists():
        log.warning(f"Topic file not found: {filepath}")
        return None

    content = filepath.read_text(encoding="utf-8")

    # Parse frontmatter
    meta, body = {}, content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except yaml.YAMLError:
                pass

    # Check staleness
    is_stale   = False
    stale_days = 0
    stale_after = meta.get("stale_after")
    if stale_after:
        try:
            stale_date = datetime.strptime(stale_after, "%Y-%m-%d").date()
            today      = datetime.now().date()
            if stale_date < today:
                is_stale   = True
                stale_days = (today - stale_date).days
        except ValueError:
            pass

    return TopicContext(
        path                = topic_path,
        title               = meta.get("title", topic_path),
        body                = body[:MAX_CONTEXT_CHARS // MAX_TOPICS],
        sources             = meta.get("sources", []),
        has_conflicts       = bool(meta.get("conflicts")),
        is_stale            = is_stale,
        stale_days          = stale_days,
        related_topics      = meta.get("related_topics", []),
        prerequisite_topics = meta.get("prerequisite_topics", []),
    )


def retrieve_context(topic_paths: list[str]) -> list[TopicContext]:
    """Load all matched topic files."""
    contexts = []
    for path in topic_paths:
        ctx = load_topic(path)
        if ctx:
            contexts.append(ctx)
    return contexts


# ── STAGE 2b: FALLBACK CORPUS SEARCH ─────────────────────────────────────────

@dataclass
class RawArticleContext:
    title:   str
    author:  str
    url:     str
    date:    str
    body:    str
    score:   int


def search_raw_corpus(question: str, already_loaded_urls: set[str]) -> list[RawArticleContext]:
    """
    Search raw articles for question keywords.
    Returns top matching articles not already covered by topic files.
    This ensures no article is ever lost — even if it wasn't classified
    into a topic file, it can still be found at query time.
    """
    if not RAW_DIR.exists():
        return []

    question_words = set(re.findall(r'\b\w{4,}\b', question.lower()))
    if not question_words:
        return []

    scored = []

    for raw_file in RAW_DIR.glob("*.md"):
        try:
            content = raw_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        # Parse frontmatter
        meta = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    meta = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except Exception:
                    pass

        url = meta.get("source_url", "")

        # Skip articles already covered by loaded topic files
        if url in already_loaded_urls:
            continue

        title  = meta.get("title", "").lower()
        author = meta.get("author", "Unknown")
        lead   = " ".join(body.split()[:200]).lower()

        # Score: title matches worth more than body matches
        score = 0
        for word in question_words:
            if word in title:
                score += 5
            elif word in lead:
                score += 2
            elif word in body.lower():
                score += 1

        if score >= 3:
            scored.append(RawArticleContext(
                title  = meta.get("title", raw_file.stem),
                author = author,
                url    = url,
                date   = meta.get("published", ""),
                body   = body[:2000],
                score  = score,
            ))

    # Return top matches sorted by score
    scored.sort(key=lambda x: x.score, reverse=True)
    return scored[:MAX_RAW_FALLBACK]


# ── STAGE 3: SYNTHESIS ────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are the Modern Workplace Wiki — a synthesised knowledge base built from the best Microsoft MVP blogs, Microsoft documentation, and community resources.

You answer questions about Microsoft 365, Azure, Intune, Entra ID, Microsoft Sentinel, Microsoft Defender, Exchange Online, and Teams.

RULES — follow these exactly:
1. Prefer wiki context above all else. Cite every factual claim: [Source: Author Name]
2. If the wiki context covers the question fully — answer from it exclusively.
3. If the wiki context covers the topic partially — answer what the wiki knows, then extend with your own Microsoft product knowledge for the gaps. Label extended knowledge as [Source: Microsoft Documentation] and add: "⚠ This detail is not yet in the wiki corpus."
4. If the wiki has no context at all — answer fully from your Microsoft product knowledge, label every claim [Source: Microsoft Documentation], and add: "⚠ This topic is not yet in the wiki. The answer is based on Microsoft documentation knowledge."
5. NEVER say you cannot answer a Modern Workplace question. Always provide value.
6. Do not pad answers. Be precise and technical.
7. Include PowerShell or KQL code blocks when relevant.
8. When sources conflict, state both positions explicitly rather than blending them.
9. End every answer with a ## Sources section and a ## Wiki Coverage note stating whether this answer came fully, partially, or not from the wiki corpus.

CITATION FORMAT: Every factual sentence must end with [Source: Author Name] before the period.
Example: "Block device code flow by setting the Authentication flows condition to Block [Source: Daniel Chronlund]."
"""


def synthesise(
    question:     str,
    contexts:     list[TopicContext],
    raw_fallback: list[RawArticleContext] | None = None
) -> str:
    """Single Claude API call. Returns raw answer text."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Build context from topic files (synthesised, high quality)
    context_parts = []
    for ctx in contexts:
        sources_str = "\n".join(
            f"  - {s.get('author', 'Unknown')}: {s.get('url', '')}"
            for s in ctx.sources[:5]
        )
        context_parts.append(
            f"=== SYNTHESISED TOPIC: {ctx.title} ===\n"
            f"Sources:\n{sources_str}\n\n"
            f"{ctx.body}\n"
        )

    # Add raw fallback articles (unsynthesised but directly relevant)
    if raw_fallback:
        for raw in raw_fallback:
            context_parts.append(
                f"=== COMMUNITY ARTICLE: {raw.title} ===\n"
                f"Author: {raw.author}\n"
                f"URL: {raw.url}\n"
                f"Date: {raw.date}\n\n"
                f"{raw.body}\n"
            )

    context_block = "\n\n".join(context_parts)

    # CONTEXT ENGINEERING
    seen_paths = {ctx.path for ctx in contexts}
    context_extras = []
    for ctx in contexts:
        for rp in (getattr(ctx, "related_topics", None) or [])[:3]:
            if rp in seen_paths: continue
            rf = WIKI_DIR / (rp + ".md")
            if rf.exists():
                rt = rf.read_text(encoding="utf-8")
                parts = rt.split("---", 2)
                rb = parts[2].strip() if len(parts) >= 3 else rt
                sm = " ".join(rb.split()[:200])
                lb = rp.split("/")[-1].replace("-", " ").title()
                context_extras.append("=== RELATED: " + lb + " ===\n" + sm + "\n")
                seen_paths.add(rp)
    if context_extras:
        context_parts.extend(context_extras)
        context_block = "\n\n".join(context_parts)
    also_know = []
    for ctx in contexts:
        for r in (getattr(ctx, "related_topics", None) or [])[:2]:
            lb = r.split("/")[-1].replace("-", " ").title()
            if lb not in also_know: also_know.append(lb)
    also_str = ("\n\nSee Also: " + ", ".join(also_know)) if also_know else ""
    user_message = ("Knowledge base context:\n\n" + context_block + "\n\nQuestion: " + question + also_str)


    response = client.messages.create(
        model      = CLAUDE_MODEL,
        max_tokens = MAX_TOKENS,
        system     = SYSTEM_PROMPT,
        messages   = [{"role": "user", "content": user_message}]
    )

    return response.content[0].text


# ── STAGE 4: VALIDATION ───────────────────────────────────────────────────────

def validate_answer(answer: str, contexts: list[TopicContext]) -> tuple[bool, list[str]]:
    """
    Check that:
    1. Answer contains at least one [Source: ...] citation
    2. Cited author names actually exist in the loaded contexts
    3. Answer does not contain made-up URLs
    Returns (citations_ok, list_of_warnings)
    """
    warnings = []

    # Check citations present
    citations = re.findall(r'\[Source:\s*([^\]]+)\]', answer)
    if not citations:
        warnings.append(
            "VALIDATION: No citations found in answer. "
            "Answer may not be grounded in wiki corpus."
        )
        return False, warnings

    # Check cited authors exist in loaded contexts
    all_authors = set()
    for ctx in contexts:
        for source in ctx.sources:
            author = source.get("author", "")
            if author:
                all_authors.add(author.lower())

    for citation in citations:
        cited_author = citation.strip().lower()
        # Always accept Microsoft Documentation citations
        if "microsoft" in cited_author:
            continue
        # Fuzzy check — cited name should partially match a real author
        if not any(cited_author in auth or auth in cited_author for auth in all_authors):
            warnings.append(
                f"VALIDATION: Cited author '{citation}' not found in loaded sources. "
                f"Verify this claim manually."
            )

    citations_ok = len(warnings) == 0
    return citations_ok, warnings


# ── FULL PIPELINE ─────────────────────────────────────────────────────────────

def query(question: str) -> QueryResult:
    """
    Run the full four-stage query pipeline.
    Returns QueryResult with answer, sources, and any warnings.
    """
    warnings = []

    # Stage 1: Route
    index    = load_index()
    if not index:
        return QueryResult(
            question    = question,
            answer      = "Wiki index not found. Run: python src/librarian.py --rebuild-index",
            topics_used = [],
            sources     = [],
            warnings    = ["INDEX_MISSING"],
            citations_ok= False
        )

    topic_paths = route_question(question, index)

    # Stage 2: Retrieve topic files (may be empty if no index match)
    contexts = retrieve_context(topic_paths) if topic_paths else []

    # Stage 2b: Fallback corpus search — find relevant raw articles
    # not already covered by topic files
    already_loaded_urls = set()
    for ctx in contexts:
        for source in ctx.sources:
            url = source.get("url", "")
            if url:
                already_loaded_urls.add(url)

    raw_fallback = search_raw_corpus(question, already_loaded_urls)
    if raw_fallback:
        log.info(f"Fallback: {len(raw_fallback)} raw articles found")

    if not contexts and not raw_fallback:
        return QueryResult(
            question    = question,
            answer      = "Topic files not found. The index may be out of sync — run rebuild-index.",
            topics_used = topic_paths,
            sources     = [],
            warnings    = ["TOPIC_FILES_MISSING"],
            citations_ok= False
        )

    # Collect staleness warnings before synthesis
    for ctx in contexts:
        if ctx.is_stale:
            warnings.append(
                f"STALE: '{ctx.title}' was last updated {ctx.stale_days} days ago. "
                f"Verify against current Microsoft documentation before implementing."
            )
        if ctx.has_conflicts:
            warnings.append(
                f"CONFLICT: '{ctx.title}' has source disagreements. "
                f"Review _conflicts.md for details."
            )

    # Stage 3: Synthesise
    try:
        answer = synthesise(question, contexts, raw_fallback)
    except anthropic.APIError as e:
        log.error(f"Claude API error: {e}")
        return QueryResult(
            question    = question,
            answer      = f"API error during synthesis: {e}",
            topics_used = [ctx.path for ctx in contexts],
            sources     = [],
            warnings    = [f"API_ERROR: {e}"],
            citations_ok= False
        )

    # Stage 4: Validate
    citations_ok, validation_warnings = validate_answer(answer, contexts)
    warnings.extend(validation_warnings)

    # Collect all sources — topic files + raw fallback, deduplicated by URL
    seen_urls = set()
    all_sources = []

    def normalise_url(u):
        return u.rstrip("/").lower()

    for ctx in contexts:
        for source in ctx.sources:
            u = normalise_url(source.get("url", ""))
            if u and u not in seen_urls:
                seen_urls.add(u)
                all_sources.append(source)

    for raw in (raw_fallback or []):
        u = normalise_url(raw.url)
        if u and u not in seen_urls:
            seen_urls.add(u)
            all_sources.append({
                "author": raw.author,
                "title":  raw.title,
                "url":    raw.url,
                "date":   raw.date,
            })

    # Auto-capture gaps — if answer used no wiki context, log the question
    if not contexts and not raw_fallback:
        gaps_file = WIKI_DIR / "_gaps.md"
        if gaps_file.exists():
            gaps_text = gaps_file.read_text(encoding="utf-8")
            if question[:40] not in gaps_text:
                gaps_file.write_text(gaps_text.rstrip() + "\n" + gap_entry + "\n")
                log.info(f"  Gap captured: {question[:60]}")
                log.info(f"  Gap captured: {question[:60]}")

    return QueryResult(
        question    = question,
        answer      = answer,
        topics_used = [ctx.path for ctx in contexts],
        sources     = all_sources,
        warnings    = warnings,
        citations_ok= citations_ok
    )


# ── CLI OUTPUT ────────────────────────────────────────────────────────────────

def print_result(result: QueryResult) -> None:
    """Print query result to terminal with clear formatting."""
    print("\n" + "=" * 70)
    print(f"QUESTION: {result.question}")
    print("=" * 70)

    if result.warnings:
        print("\n⚠ WARNINGS:")
        for w in result.warnings:
            print(f"  {w}")

    print(f"\nTOPICS USED: {', '.join(result.topics_used) or 'none'}")
    print(f"CITATIONS OK: {'✓' if result.citations_ok else '✗'}")
    print("\nANSWER:")
    print("-" * 70)
    print(result.answer)
    print("-" * 70)

    if result.sources:
        print(f"\nSOURCES ({len(result.sources)}):")
        for s in result.sources:
            print(f"  [{s.get('author', 'Unknown')}] {s.get('title', '')} — {s.get('url', '')}")


def interactive_mode() -> None:
    """Simple interactive query loop."""
    print("\nMW-Wiki Query Engine")
    print("Type your question. Ctrl+C to exit.\n")
    while True:
        try:
            question = input("Question: ").strip()
            if not question:
                continue
            result = query(question)
            print_result(result)
        except KeyboardInterrupt:
            print("\nExiting.")
            break


# ── ENTRY POINT ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MW-Wiki Query Engine")
    group  = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("question",      nargs="?", help="Question to ask the wiki")
    group.add_argument("--interactive", action="store_true", help="Interactive query mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.question:
        result = query(args.question)
        print_result(result)
    else:
        parser.print_help()
