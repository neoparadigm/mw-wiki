---
conflicts: []
context_note: Edr Block Mode is part of the defender domain. Synthesised from 1 community
  source.
domain: defender
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: limwainstein
  crawled: '2026-04-18'
  date: '2025-10-20'
  title: Endpoint detection and response in block mode - Microsoft Defender for Endpoint
  url: https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode
stale_after: '2026-07-17'
title: EDR in Block Mode
topic: defender/mde/edr-block-mode
---

# EDR in Block Mode

## EDR in Block Mode

Endpoint detection and response (EDR) in block mode is a feature of Microsoft Defender for Endpoint that provides additional protection when a non-Microsoft antivirus solution is used as the primary antivirus product, with Microsoft Defender Antivirus running in passive mode. This setup is particularly useful for organizations that require multiple antivirus solutions.

## Key Concepts

- EDR in block mode works behind the scenes to remediate malicious artifacts that may have been missed by the primary, non-Microsoft antivirus product.
- Some capabilities like real-time protection and network protection are only available when Microsoft Defender Antivirus is running in active mode.
- EDR in block mode is integrated with threat & vulnerability management capabilities.
- To get the best protection, deploy Microsoft Defender for Endpoint baselines.

## Configuration

1. Ensure that your operating system is supported (Windows).
2. Turn on EDR in block mode, and a malicious artifact detected will be remediated by Defender for Endpoint.

## Common Pitfalls

- Not meeting the requirements before turning on EDR in block mode.
- Relying solely on EDR in block mode for all protection capabilities; some features require Microsoft Defender Antivirus to be the active antivirus solution.

## KQL / PowerShell

Not applicable, as this article does not cover any specific queries or scripts.

## Related Topics

- EDR block mode
- Passive mode
- Third-party AV
- MDE coexistence
- EDR