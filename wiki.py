"""
MW-Wiki — Main Entry Point
--------------------------
python wiki.py build      — crawl all sources + run librarian
python wiki.py crawl      — crawl only (no librarian)
python wiki.py process    — run librarian on existing raw files
python wiki.py ask "..."  — query the wiki
python wiki.py serve      — start web server at localhost:8000
python wiki.py test       — run test suite
python wiki.py status     — show corpus status
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SRC_DIR  = BASE_DIR / "src"
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR  = BASE_DIR / "raw"


def cmd(args: list[str]) -> int:
    return subprocess.run([sys.executable] + args).returncode


def status():
    wiki_files  = list(WIKI_DIR.rglob("*.md"))
    topic_files = [f for f in wiki_files if not f.name.startswith("_")]
    raw_files   = list(RAW_DIR.glob("*.md"))

    processed_log = RAW_DIR / ".processed.txt"
    processed = set()
    if processed_log.exists():
        processed = set(processed_log.read_text().strip().splitlines())

    print("\n" + "=" * 50)
    print("MW-WIKI STATUS")
    print("=" * 50)
    print(f"  Raw articles crawled:  {len(raw_files)}")
    print(f"  Raw articles processed:{len(processed)}")
    print(f"  Topic files:           {len(topic_files)}")
    print(f"  Unprocessed raw:       {len(raw_files) - len(processed)}")

    gaps_file = WIKI_DIR / "_gaps.md"
    if gaps_file.exists():
        gap_lines = [l for l in gaps_file.read_text().splitlines() if l.startswith("|") and "topic" not in l.lower()]
        print(f"  Known gaps:            {len(gap_lines)}")

    conflicts_file = WIKI_DIR / "_conflicts.md"
    if conflicts_file.exists():
        conflict_count = conflicts_file.read_text().count("## ")
        print(f"  Conflicts detected:    {conflict_count}")

    stale_file = WIKI_DIR / "_stale.md"
    if stale_file.exists():
        stale_lines = [l for l in stale_file.read_text().splitlines() if l.startswith("|") and "topic" not in l.lower()]
        print(f"  Stale topics:          {len(stale_lines)}")

    print("=" * 50)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == "build":
        print("Step 1/2: Crawling sources...")
        rc = cmd([str(SRC_DIR / "crawler.py"), "--all"])
        if rc != 0:
            print("Crawl failed.")
            sys.exit(rc)
        print("\nStep 2/2: Running librarian...")
        rc = cmd([str(SRC_DIR / "librarian.py"), "--process-all"])
        sys.exit(rc)

    elif command == "crawl":
        if len(sys.argv) > 2:
            sys.exit(cmd([str(SRC_DIR / "crawler.py"), "--source", sys.argv[2]]))
        sys.exit(cmd([str(SRC_DIR / "crawler.py"), "--all"]))

    elif command == "process":
        sys.exit(cmd([str(SRC_DIR / "librarian.py"), "--process-all"]))

    elif command == "ask":
        if len(sys.argv) < 3:
            print("Usage: python wiki.py ask \"your question\"")
            sys.exit(1)
        question = " ".join(sys.argv[2:])
        sys.exit(cmd([str(SRC_DIR / "query.py"), question]))

    elif command == "serve":
        sys.exit(cmd([str(SRC_DIR / "server.py")]))

    elif command == "test":
        test_arg = sys.argv[2] if len(sys.argv) > 2 else "all"
        sys.exit(cmd([str(BASE_DIR / "tests" / "test_wiki.py"), "--test", test_arg]))

    elif command == "status":
        status()

    elif command == "reindex":
        sys.exit(cmd([str(SRC_DIR / "librarian.py"), "--rebuild-index"]))

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
