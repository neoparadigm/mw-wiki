---
conflicts:
- '[CONFLICT: Jannik Reinhard does not provide new information on configuration]'
- '[CONFLICT: Jannik Reinhard does not provide new information on common pitfalls]'
- '[CONFLICT: Jannik Reinhard does not provide new related topics]'
- '[CONFLICT: Jeffrey emphasizes the importance of proper configuration to avoid mistakes
  during deployment]'
- '[CONFLICT: Jeffrey does not provide new information on common pitfalls related
  to ASR]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2022-06-15'
  title: Attack Surface Reduction Dashboard for Microsoft Sentinel
  url: https://danielchronlund.com/2022/06/15/attack-surface-reduction-dashboard-for-microsoft-sentinel
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2023-12-07'
  title: 'Microsoft Defender for Endpoint: Key Configurations and Best Practices (2/2)'
  url: https://jannikreinhard.com/2023/12/07/microsoft-defender-for-endpoint-key-configurations-and-best-practices-2-2
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-02-12'
  title: Common mistakes during Microsoft Defender for Endpoint deployments
  url: https://jeffreyappel.nl/common-mistakes-during-microsoft-defender-for-endpoint-deployments
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2023-08-08'
  title: Onboard and configure Defender for Endpoint for non-persistent VDI environments
  url: https://jeffreyappel.nl/onboard-and-configure-defender-for-endpoint-for-non-persistent-vdi-environments
stale_after: '2026-06-13'
title: Attack Surface Reduction Rules
topic: intune/security/asr-rules
---

# Attack Surface Reduction Rules

## Attack Surface Reduction Rules

### Overview
Attack Surface Reduction (ASR) rules are a set of security configurations in Windows Defender that help reduce the attack surface by blocking potential threats and vulnerabilities. This topic is crucial for securing Microsoft environments against cyber attacks. [(Source: Existing entry)]

### Key Concepts
- ASR rules: A collection of predefined rules designed to block specific types of potentially malicious activities, such as executable file downloads, script execution, and email attachments. [(Source: Existing entry)]
- Audit mode vs Block mode: ASR rules can be configured to operate in either audit mode (logging events without blocking them) or block mode (blocking the action and logging an event). [(Source: Existing entry)]
- 16 different ASR rules: As of June 2022, there are 16 different ASR rules available in Windows. More information on these rules can be found [here](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide). [(Source: Existing entry)]

### Configuration
To implement the ASR rules and monitor them over time, you can use the Attack Surface Reduction Dashboard for Microsoft Sentinel. The dashboard allows filtering on rules in audit mode and block mode, selecting a specific time range, and filtering by rules, devices, or users. To install the dashboard, follow the instructions provided in [Daniel Chronlund's blog post](https://danielchronlund.com/2022/06/15/attack-surface-reduction-dashboard-for-microsoft-sentinel).

[New Information: Common mistakes during Microsoft Defender for Endpoint deployments by Jeffrey (February 12, 2025) highlights the importance of properly configuring ASR rules to avoid false positives or blocking legitimate activities.]

### Common Pitfalls
- Misconfiguring ASR rules can lead to false positives or blocking of legitimate activities. It is essential to test and refine the rules before deploying them in a production environment. [(Source: Existing entry)]
  * [CONFLICT: Jeffrey emphasizes the importance of proper configuration to avoid mistakes during deployment]
- Failing to monitor the ASR events can result in missed security incidents or ineffective threat detection. Regularly reviewing the event logs and adjusting the rules as needed is crucial for maintaining an effective security posture. [(Source: Existing entry)]
  * [CONFLICT: Jeffrey does not provide new information on common pitfalls related to ASR]

### KQL / PowerShell
[No specific queries or scripts provided in the article]

### Related Topics
- ASR
- attack surface reduction
- block mode
- audit mode
- ASR rules
* [New Information: Jeffrey's blog post discusses common mistakes during Microsoft Defender for Endpoint deployments, which includes ASR configuration]

[New Source Article: Onboard and configure Defender for Endpoint for non-persistent VDI environments]

## Onboarding and Configuring Defender for Endpoint in Non-Persistent VDI Environments

Jeffrey's blog post discusses the challenges of onboarding and configuring Defender for Endpoint in non-persistent VDI environments, providing solutions to ensure efficient operation. [(Source: New Source)]

### Key Concepts
- Non-persistent VDI: A type of virtual desktop infrastructure where each user session is temporary and does not retain data between sessions. [(Source: New Source)]
- Signature update process/ AV configuration: The process by which Defender for Endpoint updates its antivirus signatures and configurations in non-persistent VDI environments. [(Source: New Source)]

### Configuration
The blog post provides detailed steps to onboard and configure Defender for Endpoint in non-persistent VDI environments, addressing the challenges associated with signature updates and AV configuration. [(Source: New Source)]