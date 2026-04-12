# MW·Wiki

A synthesised knowledge base for Modern Workplace practitioners, built from the best Microsoft MVP blogs and Microsoft documentation.

## Quick Start — Just Want Answers?
```bash
git clone https://github.com/neoparadigm/mw-wiki.git
cd mw-wiki
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python3 wiki.py serve
```

Open `http://localhost:8000` — the wiki is ready. No crawling. No setup. The knowledge base comes pre-built.

To ask from the command line:
```bash
python3 wiki.py ask "How do I block device code flow in Conditional Access?"
```

## What It Is

MW·Wiki crawls a curated set of Microsoft MVP blogs, distils each article into structured topic files using a local LLM, and answers questions with cited responses — every claim traced back to the original author and URL.

It does not replace the original blogs. It makes them findable.

## What It Is Not

- A replacement for reading the original authors
- Always current — check `wiki/_stale.md` for topics needing refresh
- Complete — check `wiki/_gaps.md` for missing topics
- A substitute for professional judgement

## Contributing a Source

Found a great blog post that should be in the wiki? Submit a PR adding the URL to `config/seed_list.yaml`. The maintainer will process it and commit the updated topic files.

You never need to run the crawler yourself.

## Commands

| Command | Who uses it | What it does |
|---|---|---|
| `python3 wiki.py serve` | Everyone | Start web UI at localhost:8000 |
| `python3 wiki.py ask "..."` | Everyone | Query from CLI |
| `python3 wiki.py status` | Everyone | Show corpus statistics |
| `python3 wiki.py test` | Everyone | Run test suite |
| `python3 wiki.py build` | Maintainer only | Crawl sources + process |
| `python3 wiki.py crawl` | Maintainer only | Crawl only |
| `python3 wiki.py process` | Maintainer only | Process raw files |
| `python3 wiki.py reindex` | Maintainer only | Rebuild index |

## Sources

Built from the work of the Modern Workplace community. Every topic file credits its sources. See `wiki/_sources.md` for the complete attribution list.

This project synthesises ideas into new structured entries and always links back to the original authors. It does not reproduce article content verbatim.

## Limitations

- Topic files may be stale — Microsoft ships changes frequently. Verify configuration guidance against current documentation before implementing in production.
- Corpus is incomplete — see `wiki/_gaps.md`
- Synthesis quality depends on source quality — always follow citations back to the original

## License

Code: MIT  
Wiki content: CC-BY — reuse with attribution to original sources
