# MW·Wiki

A synthesised knowledge base for Modern Workplace practitioners, built from the best Microsoft MVP blogs and Microsoft documentation.

## Get Started
```bash
git clone https://github.com/neoparadigm/mw-wiki.git
cd mw-wiki
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python3 wiki.py serve
```

Open `http://localhost:8000` in your browser. The wiki is ready.

No crawling. No setup. The knowledge base comes pre-built.

## What It Is

MW·Wiki is a community knowledge base for the Modern Workplace — Intune, Entra ID, Conditional Access, Sentinel, Defender, Exchange, and Teams.

Ask a question in the browser. Get a cited answer traced back to the original MVP blog post or Microsoft documentation that covers it.

It does not replace the original authors. It makes their work findable in one place.

## What It Is Not

- A replacement for reading the original blogs — every answer links back to them
- Always current — Microsoft ships changes frequently, check `wiki/_stale.md`
- Complete — see `wiki/_gaps.md` for topics not yet covered
- A substitute for professional judgement — always verify before implementing in production

## Contributing

Found a blog post that should be in the wiki? Open a PR adding the URL to `config/seed_list.yaml`. The maintainer processes it and commits the updated topic files. You never need to run the crawler.

## Sources

Built on the work of the Modern Workplace community. See `wiki/_sources.md` for full attribution. Every answer cites the original author and URL.

## License

Code: MIT — Wiki content: CC-BY with attribution to original sources
