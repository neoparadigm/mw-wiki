---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-06-15'
  title: Attack Surface Reduction Dashboard for Microsoft Sentinel
  url: https://danielchronlund.com/2022/06/15/attack-surface-reduction-dashboard-for-microsoft-sentinel
stale_after: '2026-06-11'
title: Attack Surface Reduction Rules
topic: intune/security/asr-rules
---

# Attack Surface Reduction Rules

## Attack Surface Reduction Rules

### Overview
Attack Surface Reduction (ASR) rules are a set of security configurations in Windows Defender that help reduce the attack surface by blocking potential threats and vulnerabilities. This topic is crucial for securing an organization's digital environment against cyber attacks.

### Key Concepts
- ASR rules: Specific security configurations designed to block potential threats and vulnerabilities.
- Audit mode: A mode in which ASR rules are logged but do not block the actions they are designed to prevent.
- Block mode: A mode in which ASR rules actively block the actions they are designed to prevent.
- Windows Defender: The built-in antivirus and threat protection system in Windows operating systems.

### Configuration
1. Navigate to the Windows Security settings.
2. Go to "Virus & Threat Protection" > "Manage settings".
3. Scroll down to "Attack Surface Reduction" and click on it.
4. Enable or disable rules as needed, choosing between audit mode and block mode.

### Common Pitfalls
- Overly restrictive ASR rules can cause legitimate applications to be blocked.
- Incorrect configuration of ASR rules can lead to increased attack surface.
- Failing to monitor ASR rule events can result in missed security incidents.

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to ASR rules.]

### Related Topics
- [ASR](/wiki/ASR)
- [Attack surface reduction](/wiki/Attack_surface_reduction)
- [Block mode](/wiki/Block_mode)
- [Audit mode](/wiki/Audit_mode)
- [ASR rules reference](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide)