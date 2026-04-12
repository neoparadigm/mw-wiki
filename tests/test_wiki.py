"""
MW-Wiki Test Suite
------------------
Run before any public launch.
All tests must pass — not most, all.

Usage:
    python tests/test_wiki.py
    python tests/test_wiki.py --test routing
    python tests/test_wiki.py --test citations
"""

import re
import sys
import logging
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

import yaml
from query import route_question, load_index, load_topic, validate_answer

logging.basicConfig(level=logging.WARNING)  # Suppress info during tests

PASS = "✓"
FAIL = "✗"
results = []


def test(name: str, condition: bool, detail: str = "") -> None:
    status = PASS if condition else FAIL
    results.append((status, name, detail))
    print(f"  {status}  {name}" + (f" — {detail}" if detail else ""))


# ── TEST: ROUTING ─────────────────────────────────────────────────────────────

def test_routing():
    print("\n[ ROUTING TESTS ]")
    index = load_index()
    if not index:
        test("Index loads", False, "_index.yaml missing — run librarian --rebuild-index")
        return

    test("Index loads", True, f"{len(index)} topics")

    # Known question → expected topic path (partial match acceptable)
    routing_cases = [
        (
            "How do I block device code flow in Conditional Access?",
            "identity/conditional-access/device-code-flow-blocking"
        ),
        (
            "What is AiTM proxy attack and how do I defend against it?",
            "identity/conditional-access/aitm-defence"
        ),
        (
            "How do I configure PIM for Groups?",
            "identity/pim/pim-for-groups"
        ),
        (
            "What are the Autopilot deployment modes?",
            "intune/deployment/autopilot-user-driven"
        ),
        (
            "How do I configure LAPS v2 in Intune?",
            "intune/security/laps-v2"
        ),
        (
            "Write a KQL query to detect legacy auth sign-ins",
            "sentinel/kql/identity-detection-queries"
        ),
        (
            "How do I enable Credential Guard?",
            "intune/security/credential-guard"
        ),
        (
            "What are ASR rules and how do I put them in block mode?",
            "intune/security/asr-rules"
        ),
        (
            "How do I disable SMTP AUTH?",
            "exchange/security/smtp-auth-disable"
        ),
        (
            "What is WDAC and how do I enforce it?",
            "intune/security/wdac-app-control"
        ),
    ]

    passed = 0
    for question, expected_path in routing_cases:
        paths = route_question(question, index)
        matched = any(expected_path in p or p in expected_path for p in paths)
        test(
            f"Routes: '{question[:45]}...'",
            matched,
            f"Expected: {expected_path}, Got: {paths[:2]}"
        )
        if matched:
            passed += 1

    test(
        "Routing accuracy ≥ 70%",
        passed / len(routing_cases) >= 0.7,
        f"{passed}/{len(routing_cases)} correct"
    )


# ── TEST: TOPIC FILE INTEGRITY ────────────────────────────────────────────────

def test_topic_files():
    print("\n[ TOPIC FILE INTEGRITY TESTS ]")
    wiki_dir = BASE_DIR / "wiki"

    topic_files = [f for f in wiki_dir.rglob("*.md") if not f.name.startswith("_")]
    test("Topic files exist", len(topic_files) > 0, f"{len(topic_files)} files found")

    if not topic_files:
        return

    # Check each topic file has required frontmatter
    missing_frontmatter = []
    missing_sources     = []
    missing_title       = []

    for tf in topic_files:
        content = tf.read_text(encoding="utf-8")
        if not content.startswith("---"):
            missing_frontmatter.append(tf.name)
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            missing_frontmatter.append(tf.name)
            continue

        try:
            meta = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            missing_frontmatter.append(tf.name)
            continue

        if not meta.get("sources"):
            missing_sources.append(tf.name)
        if not meta.get("title"):
            missing_title.append(tf.name)

    test(
        "All topic files have frontmatter",
        len(missing_frontmatter) == 0,
        f"Missing: {missing_frontmatter[:3]}" if missing_frontmatter else ""
    )
    test(
        "All topic files have sources",
        len(missing_sources) == 0,
        f"Missing: {missing_sources[:3]}" if missing_sources else ""
    )
    test(
        "All topic files have titles",
        len(missing_title) == 0,
        f"Missing: {missing_title[:3]}" if missing_title else ""
    )


# ── TEST: META FILES ──────────────────────────────────────────────────────────

def test_meta_files():
    print("\n[ META FILE TESTS ]")
    wiki_dir = BASE_DIR / "wiki"

    required_meta = ["_index.yaml", "_gaps.md", "_sources.md", "_conflicts.md", "_stale.md"]
    for filename in required_meta:
        filepath = wiki_dir / filename
        test(f"{filename} exists", filepath.exists())
        if filepath.exists():
            size = filepath.stat().st_size
            test(f"{filename} non-empty", size > 0, f"{size} bytes")


# ── TEST: CITATION VALIDATION ─────────────────────────────────────────────────

def test_citation_validation():
    print("\n[ CITATION VALIDATION TESTS ]")

    # Mock context for testing
    from query import TopicContext

    mock_context = TopicContext(
        path          = "identity/conditional-access/device-code-flow-blocking",
        title         = "Blocking Device Code Flow",
        body          = "Test content",
        sources       = [
            {"author": "Daniel Chronlund", "url": "https://danielchronlund.com/test"},
            {"author": "MSEndpointMgr",    "url": "https://msendpointmgr.com/test"},
        ],
        has_conflicts = False,
        is_stale      = False,
    )

    # Good answer — has citations matching real authors
    good_answer = (
        "Block device code flow via the Authentication flows condition "
        "in Conditional Access [Source: Daniel Chronlund]. "
        "Set the condition to Block for all users [Source: MSEndpointMgr]."
    )
    ok, warnings = validate_answer(good_answer, [mock_context])
    test("Valid answer passes validation", ok, f"Warnings: {warnings}")

    # Bad answer — no citations
    bad_answer_no_cite = (
        "Block device code flow via the Authentication flows condition."
    )
    ok, warnings = validate_answer(bad_answer_no_cite, [mock_context])
    test("Answer without citations fails validation", not ok, f"Correctly flagged: {warnings[:1]}")

    # Bad answer — invented author
    bad_answer_fake_author = (
        "Block device code flow [Source: Fake Person Who Does Not Exist]."
    )
    ok, warnings = validate_answer(bad_answer_fake_author, [mock_context])
    test("Answer with unknown citation author flagged", len(warnings) > 0, f"Warnings: {warnings[:1]}")


# ── TEST: SEED LIST ───────────────────────────────────────────────────────────

def test_seed_list():
    print("\n[ SEED LIST TESTS ]")
    seed_path = BASE_DIR / "config" / "seed_list.yaml"
    test("seed_list.yaml exists", seed_path.exists())

    if not seed_path.exists():
        return

    with open(seed_path) as f:
        config = yaml.safe_load(f)

    sources = config.get("sources", [])
    test("Sources defined", len(sources) > 0, f"{len(sources)} sources")

    required_fields = ["name", "author", "base_url", "robots_url", "focus"]
    for source in sources:
        for field in required_fields:
            test(
                f"'{source.get('name', '?')}' has '{field}'",
                field in source,
            )
        # Verify robots_url is distinct from base_url (common mistake)
        test(
            f"'{source.get('name', '?')}' robots_url set",
            "robots_url" in source and source["robots_url"] != source.get("base_url"),
        )


# ── TEST: TAXONOMY ────────────────────────────────────────────────────────────

def test_taxonomy():
    print("\n[ TAXONOMY TESTS ]")
    tax_path = BASE_DIR / "config" / "topic_taxonomy.yaml"
    test("topic_taxonomy.yaml exists", tax_path.exists())

    if not tax_path.exists():
        return

    with open(tax_path) as f:
        config = yaml.safe_load(f)

    topics = config.get("topics", [])
    test("Topics defined", len(topics) > 0, f"{len(topics)} topics")

    required_fields = ["path", "title", "keywords", "stale_days"]
    for topic in topics:
        for field in required_fields:
            if field not in topic:
                test(f"Topic '{topic.get('path', '?')}' has '{field}'", False)

    # Check for duplicate paths
    paths = [t["path"] for t in topics]
    unique_paths = set(paths)
    test(
        "No duplicate topic paths",
        len(paths) == len(unique_paths),
        f"Duplicates: {[p for p in paths if paths.count(p) > 1]}"
    )


# ── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="MW-Wiki Test Suite")
    parser.add_argument("--test", choices=["routing","files","meta","citations","seed","taxonomy","all"],
                        default="all")
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("MW-WIKI TEST SUITE")
    print("=" * 60)

    t = args.test
    if t in ("taxonomy", "all"): test_taxonomy()
    if t in ("seed",     "all"): test_seed_list()
    if t in ("files",    "all"): test_topic_files()
    if t in ("meta",     "all"): test_meta_files()
    if t in ("citations","all"): test_citation_validation()
    if t in ("routing",  "all"): test_routing()

    print("\n" + "=" * 60)
    passed = sum(1 for r in results if r[0] == PASS)
    failed = sum(1 for r in results if r[0] == FAIL)
    print(f"RESULTS: {passed} passed, {failed} failed")

    if failed > 0:
        print("\nFAILED TESTS:")
        for status, name, detail in results:
            if status == FAIL:
                print(f"  ✗ {name}" + (f" — {detail}" if detail else ""))
        print("\nFix all failures before launching.")
        sys.exit(1)
    else:
        print("All tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
