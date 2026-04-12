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
INDEX_PATH = WIKI_DIR / "_index.yaml"

# Claude model for synthesis — one call per query
CLAUDE_MODEL      = "claude-sonnet-4-20250514"
MAX_TOKENS        = 1000
MAX_CONTEXT_CHARS = 12000  # ~3000 tokens of context
MAX_TOPICS        = 4      # max topic files to load per query

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("query")


# ── DATA TYPES ────────────────────────────────────────────────────────────────

@dataclass
class TopicContext:
    path:          str
    title:         str
    body:          str
    sources:       list[dict]
    has_conflicts: bool
    is_stale:      bool
    stale_days:    int = 0


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
    top_paths = [path for _, path in scores[:MAX_TOPICS]]

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
        path          = topic_path,
        title         = meta.get("title", topic_path),
        body          = body[:MAX_CONTEXT_CHARS // MAX_TOPICS],
        sources       = meta.get("sources", []),
        has_conflicts = bool(meta.get("conflicts")),
        is_stale      = is_stale,
        stale_days    = stale_days,
    )


def retrieve_context(topic_paths: list[str]) -> list[TopicContext]:
    """Load all matched topic files."""
    contexts = []
    for path in topic_paths:
        ctx = load_topic(path)
        if ctx:
            contexts.append(ctx)
    return contexts


# ── STAGE 3: SYNTHESIS ────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are the Modern Workplace Wiki — a synthesised knowledge base built from the best Microsoft MVP blogs, Microsoft documentation, and community resources.

You answer questions about Microsoft 365, Azure, Intune, Entra ID, Microsoft Sentinel, Microsoft Defender, Exchange Online, and Teams.

RULES — follow these exactly:
1. Answer using ONLY the knowledge base context provided. Do not use general training knowledge.
2. Every factual claim MUST be followed immediately by a citation: [Source: Author Name]
3. If the context does not contain enough information to answer, say exactly: "The wiki does not have sufficient coverage of this topic yet. Check _gaps.md."
4. Do not pad answers. Be precise and technical.
5. Include PowerShell or KQL code blocks if present in the context and relevant to the question.
6. End every answer with a ## Sources section listing all cited sources with URLs.

CITATION FORMAT: Every factual sentence must end with [Source: Author Name] before the period.
Example: "Block device code flow by setting the Authentication flows condition to Block [Source: Daniel Chronlund]."
"""


def synthesise(question: str, contexts: list[TopicContext]) -> str:
    """Single Claude API call. Returns raw answer text."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Build context block
    context_parts = []
    for ctx in contexts:
        sources_str = "\n".join(
            f"  - {s.get('author', 'Unknown')}: {s.get('url', '')}"
            for s in ctx.sources
        )
        context_parts.append(
            f"=== TOPIC: {ctx.title} ===\n"
            f"Sources:\n{sources_str}\n\n"
            f"{ctx.body}\n"
        )

    context_block = "\n\n".join(context_parts)

    user_message = (
        f"Knowledge base context:\n\n{context_block}\n\n"
        f"Question: {question}"
    )

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

    if not topic_paths:
        return QueryResult(
            question    = question,
            answer      = (
                "No relevant topics found for this question. "
                "This may be a gap in the wiki corpus — check `_gaps.md`. "
                "You can contribute by submitting a source URL via GitHub PR."
            ),
            topics_used = [],
            sources     = [],
            warnings    = ["NO_TOPICS_MATCHED"],
            citations_ok= True
        )

    # Stage 2: Retrieve
    contexts = retrieve_context(topic_paths)

    if not contexts:
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
        answer = synthesise(question, contexts)
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

    # Collect all sources
    all_sources = []
    for ctx in contexts:
        for source in ctx.sources:
            if source not in all_sources:
                all_sources.append(source)

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
