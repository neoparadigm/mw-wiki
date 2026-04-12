# MW-Wiki

A synthesised knowledge base for Modern Workplace practitioners, built from community blogs and Microsoft documentation.

## What it is

MW-Wiki crawls a curated set of Microsoft MVP blogs and documentation, processes each article through a local LLM, and builds structured topic files — one per subject. At query time, your question is matched to relevant topic files and a single Claude API call produces a cited answer.

It is not a chatbot. Every answer must cite a real source or it is flagged.

## What it is not

- A replacement for reading the original blogs
- A substitute for professional judgement
- Complete — check `_gaps.md` to see what is missing
- Always current — every topic file has a `stale_after` date; check `_stale.md`

## Quick start

```bash
# Prerequisites
brew install ollama
ollama pull mistral          # one-time, ~4GB
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key

# Build the corpus (crawl + process, takes several hours)
python wiki.py build

# Ask a question
python wiki.py ask "How do I block device code flow in Conditional Access?"

# Start the web UI
python wiki.py serve         # opens at localhost:8000

# Check status
python wiki.py status

# Run tests
python wiki.py test
```

## Commands

| Command | What it does |
|---|---|
| `python wiki.py build` | Crawl all sources + run librarian |
| `python wiki.py crawl` | Crawl only, save to /raw/ |
| `python wiki.py process` | Run librarian on existing /raw/ files |
| `python wiki.py ask "..."` | Query the wiki from CLI |
| `python wiki.py serve` | Start web server at localhost:8000 |
| `python wiki.py test` | Run test suite |
| `python wiki.py status` | Show corpus statistics |
| `python wiki.py reindex` | Rebuild _index.yaml and meta files |

## Architecture

```
seed_list.yaml → crawler.py → /raw/ → librarian.py → /wiki/
                                                         ↓
                                                    query.py
                                                         ↓
                                                   Claude API (one call)
                                                         ↓
                                                   cited answer
```

- **Crawler**: Respects robots.txt. Converts HTML to markdown. Saves with frontmatter.
- **Librarian**: Ollama (local, zero cost). Classifies articles into canonical topics. Creates or merges topic files.
- **Query engine**: Four stages — route, retrieve, synthesise, validate. One Claude API call per query (~$0.006).
- **Validation**: Every answer checked for citations. Uncited answers are flagged.

## Contributing

Submit a PR adding a source URL to `config/seed_list.yaml`. The librarian will process it in the next build.

All submissions must be:
- Publicly accessible
- Not disallowed by robots.txt
- Relevant to Modern Workplace (M365, Azure, Intune, Entra ID, Sentinel, Defender)

## Sources

All knowledge in this wiki is synthesised from community blogs and documentation. Every topic file credits its sources. See `wiki/_sources.md` for the complete list.

This project does not reproduce article content verbatim. It synthesises ideas into new structured entries and always links back to the original authors.

## Limitations

- Corpus is incomplete — see `_gaps.md`
- Topic files may be stale — see `_stale.md`  
- Synthesis quality depends on Ollama/Mistral — review topic files before relying on them
- Always verify configuration guidance against current Microsoft documentation before implementing in production

## License

Code: MIT  
Wiki content: CC-BY — reuse with attribution
