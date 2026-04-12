<div align="center">

<img src="https://img.shields.io/badge/Modern%20Workplace-Knowledge%20Base-c0392b?style=for-the-badge&labelColor=1a1612" alt="MW·Wiki"/>

# MW·Wiki

**The answer Claude can't give you — current, cited, and community-verified.**

A synthesised knowledge base for Modern Workplace practitioners, built from the best Microsoft MVP blogs and Microsoft documentation. Every answer traces back to a named author, a real URL, and a date.

[![License: MIT](https://img.shields.io/badge/Code-MIT-1a5c3a?style=flat-square)](LICENSE)
[![Wiki: CC-BY](https://img.shields.io/badge/Wiki-CC--BY-1a3a5c?style=flat-square)](#license)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-c0392b?style=flat-square)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-7a6f65?style=flat-square)](https://ollama.com)
[![Inspired by](https://img.shields.io/badge/Inspired%20by-Karpathy%20LLM%20Wiki-474747?style=flat-square)](https://github.com/karpathy)

</div>

---

## Get Started in 5 Minutes

```bash
# 1. Clone — the knowledge base comes pre-built
git clone https://github.com/neoparadigm/mw-wiki.git
cd mw-wiki

# 2. Install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-...

# 4. Serve
python3 wiki.py serve
```

Open **http://localhost:8000** — ask your first question.

No crawling. No database. No Docker. The knowledge base is pre-built and ships with the repo.

---

## What It Does

You ask a question about Modern Workplace. MW·Wiki finds the most relevant topic files from the corpus, makes a single API call to Claude, and returns a cited answer — every claim attributed to the specific blog post and author that covers it.

```
You ask: "How do I block device code flow in Conditional Access?"

MW·Wiki returns:

  To block device code flow, create a CA policy targeting the
  Authentication flows condition [Daniel Chronlund — CA Policy
  Design Baseline, 2024]. Set the condition to Block for all
  users, excluding break-glass accounts [Jan Bakker — Device
  Code Flow Restriction, 2025].

  SOURCES
  ★★★ Daniel Chronlund — CA Policy Design Baseline (2024)
  ★★  Jan Bakker — How to restrict Device Code Flow (2025)
  ★★  Jeffrey Appel — Storm-2372 Attack Defence (2025)
```

---

## How It Works

Inspired by [Andrej Karpathy's LLM Wiki](https://github.com/karpathy) concept — structured knowledge maintained by an LLM librarian, not chunks retrieved from a vector database.

```mermaid
flowchart TD
    A[seed_list.yaml\n18 curated sources] --> B[Crawler\nrobots.txt aware\nhttpx + markdownify]
    B --> C[/raw/\nmarkdown articles]
    C --> D[Librarian\nOllama local · zero API cost]
    D --> E{Topic file exists?}
    E -->|No| F[Create topic file\nsynthesised + cited]
    E -->|Yes| G[Merge · flag conflicts\nupdate sources]
    F --> H[/wiki/ topic files]
    G --> H
    H --> I[_index.yaml]
    H --> J[_gaps.md]
    H --> K[_conflicts.md]
    H --> L[_stale.md]
    M[Your question] --> N[Query Engine]
    I --> N
    N --> O[Route · keyword match]
    O --> P[Retrieve · load topic files]
    P --> Q[Synthesise · Claude API\none call · ~$0.006]
    Q --> R[Validate · citations present?]
    R --> S[Cited answer\n+ staleness warnings]
```

**Build cost:** ~$0 — Ollama runs locally, no API calls during corpus build  
**Query cost:** ~$0.006 per question — one Claude Sonnet call  
**No vector database. No embeddings. No FAISS.** The index is a human-readable YAML file.

---

## What's Covered

| Domain | Topics |
|---|---|
| **Identity & Access** | Conditional Access, AiTM defence, Device Code Flow, Legacy Auth, Token Protection |
| **Privileged Access** | PIM for Groups, Break Glass, Tiered Administration, JIT Access |
| **Intune & Endpoints** | Autopilot, WDAC, LAPS v2, ASR Rules, Credential Guard, BitLocker |
| **Sentinel & KQL** | Identity detection, Privilege escalation, Lateral movement queries |
| **Defender** | MDE Tamper Protection, EDR Block Mode, Safe Links |
| **Exchange & Teams** | SMTP AUTH, Inbox rule exfiltration, External access |
| **Azure** | Key Vault RBAC, App Proxy, AVD security |

See [`wiki/_gaps.md`](wiki/_gaps.md) for topics not yet covered.  
See [`wiki/_conflicts.md`](wiki/_conflicts.md) for where sources disagree.

---

## Built On Community Knowledge

MW·Wiki exists because of the practitioners who chose to share what they learned. Every topic file credits its sources. Every answer links back to the original.

| Author | Focus | Authority |
|---|---|---|
| [Michael Niehaus](https://oofhours.com) | Autopilot, Windows Deployment | ★★★ |
| [Anoop C Nair / HTMD](https://anoopcnair.com) | Intune, Windows, Cloud PC | ★★★ |
| [MSEndpointMgr](https://msendpointmgr.com) | Intune, Autopilot, Identity | ★★★ |
| [Daniel Chronlund](https://danielchronlund.com) | Entra ID, Conditional Access, PIM | ★★★ |
| [Ugur Koc](https://ugurkoc.de) | Intune Automation, Graph API, KQL | ★★★ |
| [Jannik Reinhard](https://jannikreinhard.com) | Intune, Modern Management | ★★★ |
| [Rudy Ooms / Call4Cloud](https://call4cloud.nl) | Intune Edge Cases | ★★ |
| [Jan Bakker](https://janbakker.tech) | Conditional Access, Entra ID | ★★ |
| [Jeffrey Appel](https://jeffreyappel.nl) | Security, Identity | ★★ |
| [Bert-Jan Pals](https://kqlcafe.com) | KQL, Sentinel | ★★ |
| [Alex Verboon](https://alexverboon.com) | Sentinel, Defender | ★★ |

Full attribution in [`wiki/_sources.md`](wiki/_sources.md).

---

## Contributing a Source

Found a great post that belongs in the wiki?

1. Fork the repo
2. Add the URL to `config/seed_list.yaml`
3. Open a PR

The maintainer processes it and commits the updated topic files. You never need to run the crawler.

---

## Honest Limitations

- **Not always current** — Microsoft ships changes every 3 weeks. Check `wiki/_stale.md` before implementing anything in production.
- **Not complete** — see `wiki/_gaps.md`. The wiki knows what it doesn't know.
- **Not a substitute for professional judgement** — always follow citations back to the original source before acting on any guidance.
- **Synthesis quality** — topic files are synthesised by Ollama/Mistral locally. Quality improves as more sources are added per topic.

---

## License

**Code:** MIT  
**Wiki content:** [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse with attribution to the original source authors listed in `wiki/_sources.md`

---

<div align="center">

Built by [neoparadigm](https://github.com/neoparadigm) · Inspired by [Andrej Karpathy](https://github.com/karpathy) · Powered by the Modern Workplace community

*This wiki empowers practitioners. It does not replace the community that built it.*

</div>
