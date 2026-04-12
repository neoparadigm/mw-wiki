<div align="center">

<img src="https://img.shields.io/badge/Modern%20Workplace-Knowledge%20Base-c0392b?style=for-the-badge&labelColor=1a1612" alt="MW·Wiki"/>

# MW·Wiki

**The answer LLMs can't give you - current, cited, and community-verified.**

A living knowledge graph of Modern Workplace community intelligence.

Built from years of bookmarks, saved articles, and late-night troubleshooting sessions -the blogs that actually taught practitioners this craft, synthesised into a single queryable knowledge graph. Every answer cites a real author, a real URL, a real date.

A synthesised knowledge base for Modern Workplace practitioners, built from the best Microsoft MVP blogs and Microsoft documentation. Every answer traces back to a named author, a real URL, and a date.

[![License: MIT](https://img.shields.io/badge/Code-MIT-1a5c3a?style=flat-square)](LICENSE)
[![Wiki: CC-BY](https://img.shields.io/badge/Wiki-CC--BY-1a3a5c?style=flat-square)](#license)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-c0392b?style=flat-square)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-7a6f65?style=flat-square)](https://ollama.com)
[![Inspired by](https://img.shields.io/badge/Inspired%20by-Karpathy%20LLM%20Wiki-474747?style=flat-square)](https://github.com/karpathy)

</div>

## **The Problem**

Every Modern Workplace practitioner has a private list of blogs they trust. The ones bookmarked at 11pm when something is broken. The ones forwarded to colleagues when words fail. That knowledge exists - but it is scattered, unsynthesised, and invisible to anyone who has not been doing this for years.

Claude and ChatGPT will answer your Conditional Access question confidently. They will not tell you it was last accurate in 2023, that Daniel Chronlund and Jeffrey Appel disagree on a specific edge case, or that nobody in the community has written a definitive article on that particular topic yet.

MW·Wiki is the answer to both problems.

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

## What It Is

MW·Wiki is an open-source knowledge graph for the Modern Workplace community - Intune, Entra ID, Conditional Access, Sentinel, Defender, Exchange, and Teams.

It crawls a curated set of community blogs, distils each article into structured topic nodes using a local LLM, and connects them into a graph of community knowledge. Ask a question and get a cited answer - every claim traced back to the specific blog post and author that covers it.

> *"Most AI tools retrieve context on demand by searching documents. MW·Wiki maintains long-lived knowledge instead - relationships are explicit, topics accumulate over time, and the graph compounds rather than starting cold every session."*

**This is not RAG.** Articles are not chunked into fragments and retrieved by similarity. They are distilled into owned, structured topic nodes — plain Markdown files you can read, edit, and contribute to directly. The knowledge graph is the product.


## What It Does

You ask a question about Modern Workplace. MW·Wiki finds the most relevant topic files from the corpus, makes a single API call to Claude, and returns a cited answer - every claim attributed to the specific blog post and author that covers it.

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

<img width="1440" height="1736" alt="image" src="https://github.com/user-attachments/assets/7c1af603-0d9d-4710-bfa4-91c61299a168" />



**No vector database. No embeddings. No FAISS.** The index is a human-readable YAML file.

The end result

<img width="1903" height="682" alt="image" src="https://github.com/user-attachments/assets/b5091351-4e53-4214-b2a8-3748cecdba8a" />


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

*This wiki empowers practitioners, subject matter experts, engineers. It does not replace the community that built it.*

</div>
