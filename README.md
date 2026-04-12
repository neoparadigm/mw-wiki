<div align="center">

<img src="https://img.shields.io/badge/Modern%20Workplace-Knowledge%20Graph-c0392b?style=for-the-badge&labelColor=1a1612" alt="MW·Wiki"/>

# MW·Wiki

**A living knowledge graph of Modern Workplace community intelligence.**

Built from years of bookmarks, saved articles, and late-night troubleshooting sessions —
the blogs that actually taught practitioners this craft, synthesised into a single
queryable knowledge graph. Every answer cites a real author, a real URL, a real date.

[![License: MIT](https://img.shields.io/badge/Code-MIT-1a5c3a?style=flat-square)](LICENSE)
[![Wiki: CC-BY](https://img.shields.io/badge/Wiki-CC--BY-1a3a5c?style=flat-square)](#license)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-c0392b?style=flat-square)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-7a6f65?style=flat-square)](https://ollama.com)
[![Inspired by](https://img.shields.io/badge/Inspired%20by-Karpathy%20LLM%20Wiki-474747?style=flat-square)](https://github.com/karpathy)

</div>

---

## The Problem

Every Modern Workplace practitioner has a private list of blogs they trust. The ones bookmarked at 11pm when something is broken. The ones forwarded to colleagues when words fail. That knowledge exists — but it is scattered, unsynthesised, and invisible to anyone who has not been doing this for years.

Claude and ChatGPT will answer your Conditional Access question confidently. They will not tell you it was last accurate in 2023, that Daniel Chronlund and Jeffrey Appel disagree on a specific edge case, or that nobody in the community has written a definitive article on that particular topic yet.

MW·Wiki is the answer to both problems.

---

## What It Is

MW·Wiki is an open-source knowledge graph for the Modern Workplace community — Intune, Entra ID, Conditional Access, Sentinel, Defender, Exchange, and Teams.

It crawls a curated set of community blogs, distils each article into structured topic nodes using a local LLM, and connects them into a graph of community knowledge. Ask a question and get a cited answer — every claim traced back to the specific blog post and author that covers it.

> *"Most AI tools retrieve context on demand by searching documents. MW·Wiki maintains long-lived knowledge instead — relationships are explicit, topics accumulate over time, and the graph compounds rather than starting cold every session."*

**This is not RAG.** Articles are not chunked into fragments and retrieved by similarity. They are distilled into owned, structured topic nodes — plain Markdown files you can read, edit, and contribute to directly. The knowledge graph is the product.

---

## Get Started in 3 Steps

```bash
# 1. Clone — the knowledge graph ships pre-built
git clone https://github.com/neoparadigm/mw-wiki.git
cd mw-wiki

# 2. Install
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Serve
python3 wiki.py serve
```

Open **http://localhost:8000** — ask your first question.

No crawling. No database. No Docker. No API key required.

The knowledge graph is pre-built and ships with the repo. Ollama runs locally — your queries stay on your machine.

### With Claude (higher quality answers)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 wiki.py serve
```

The server auto-detects your API key. With it — Claude synthesises answers. Without it — Ollama runs locally, free and private.

---

## How It Works

Built on a single architectural insight from Karpathy's LLM Wiki: **distil, don't chunk.**

```
Community blogs → Crawler → Librarian (Ollama) → Knowledge graph nodes
                                    ↓
                          Not RAG. Not vectors.
                          Owned structured knowledge —
                          one Markdown file per topic,
                          cross-linked, cited, dated.
                                    ↓
                    Question → Route → Retrieve nodes
                             → Synthesise (one LLM call)
                             → Validate citations
                             → Cited answer
```

Every topic node in the graph carries:
- Synthesised knowledge from every source that covers it
- Full attribution — author, URL, crawl date
- Cross-links to related nodes
- A `stale_after` date — so you always know when to verify
- Conflict flags — where sources disagree

**The graph knows what it does not know.** `_gaps.md` lists every topic the community has not written a definitive article on yet. That is the editorial roadmap — open to contribution.

---

## What Is in the Graph

| Domain | Topics Covered |
|---|---|
| **Identity & Access** | Conditional Access, AiTM defence, Device Code Flow, Legacy Auth, Token Protection, PIM |
| **Privileged Access** | PIM for Groups, Break Glass, Tiered Administration, Service Principal Governance |
| **Intune & Endpoints** | Autopilot, WDAC, LAPS v2, ASR Rules, Credential Guard, BitLocker, Compliance Policy |
| **Sentinel & KQL** | Identity detection, Privilege escalation, Lateral movement queries, Log coverage |
| **Defender** | MDE Tamper Protection, EDR Block Mode, Safe Links & Attachments |
| **Exchange & Teams** | SMTP AUTH, Inbox rule exfiltration, External access federation |
| **Azure** | Key Vault RBAC, App Proxy, AVD security |

See [`wiki/_gaps.md`](wiki/_gaps.md) for topics not yet covered.
See [`wiki/_conflicts.md`](wiki/_conflicts.md) for where sources disagree.
See [`wiki/_stale.md`](wiki/_stale.md) for topics needing a refresh.

---

## The Community That Built This

MW·Wiki exists because of practitioners who chose to share what they learned. This project is an attempt to give back — by making their collective knowledge permanently findable, permanently attributed, and permanently honest about what it does not know.

Every answer links back to the original. Every author is credited. The graph never claims to know more than its sources.

| Author | Focus |
|---|---|
| [Michael Niehaus](https://oofhours.com) | Autopilot, Windows Deployment |
| [Anoop C Nair / HTMD](https://anoopcnair.com) | Intune, Windows, Cloud PC |
| [MSEndpointMgr](https://msendpointmgr.com) | Intune, Autopilot, Identity |
| [Daniel Chronlund](https://danielchronlund.com) | Entra ID, Conditional Access, PIM |
| [Ugur Koc](https://ugurkoc.de) | Intune Automation, Graph API, KQL |
| [Jannik Reinhard](https://jannikreinhard.com) | Intune, Modern Management |
| [Rudy Ooms / Call4Cloud](https://call4cloud.nl) | Intune, Troubleshooting |
| [Jan Bakker](https://janbakker.tech) | Conditional Access, Entra ID |
| [Jeffrey Appel](https://jeffreyappel.nl) | Security, Identity |
| [Bert-Jan Pals](https://kqlcafe.com) | KQL, Sentinel |
| [Alex Verboon](https://alexverboon.com) | Sentinel, Defender |

Full attribution in [`wiki/_sources.md`](wiki/_sources.md).

---

## Contributing to the Graph

Found a blog post that belongs here?

1. Fork the repo
2. Add the URL to `config/seed_list.yaml`
3. Open a PR with a one-line note on what it covers

The maintainer processes it and commits the updated topic nodes. You never need to run the crawler. The graph grows through PRs, not forks.

---

## Commands

| Command | What it does |
|---|---|
| `python3 wiki.py serve` | Start web UI at localhost:8000 |
| `python3 wiki.py serve --local` | Force Ollama mode, no API key |
| `python3 wiki.py ask "..."` | Query from CLI |
| `python3 wiki.py status` | Show graph statistics |
| `python3 wiki.py test` | Run test suite |

---

## Honest Limitations

- **Not always current** — Microsoft ships changes every three weeks. Every topic node has a `stale_after` date. Check `wiki/_stale.md` before implementing anything in production.
- **Not complete** — see `wiki/_gaps.md`. The graph knows what it does not know.
- **Not a substitute for professional judgement** — always follow citations back to the original source before acting on any guidance.
- **Synthesis quality improves with sources** — topic nodes get more accurate and complete as more community articles are added.

---

## Why This Matters

Claude will give you a confident answer about Conditional Access. MW·Wiki will give you the answer the community actually verified — with a date, a name, and a link to go read the original.

The goal is not to replace the community blogs. It is to make them permanently findable, permanently attributed, and permanently honest about what they do not cover.

*This wiki empowers practitioners. It does not replace the community that built it.*

---

## License

**Code:** MIT  
**Wiki content:** [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse with attribution to the original source authors listed in `wiki/_sources.md`

---

<div align="center">

Built by [neoparadigm](https://github.com/neoparadigm) · Inspired by [Karpathy's LLM Wiki](https://github.com/karpathy) and [Rowboat's knowledge graph philosophy](https://github.com/rowboatlabs/rowboat) · Powered by the Modern Workplace community

</div>
