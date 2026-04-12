---
conflicts:
- '[CONFLICT: Jannik Reinhard''s article goes into greater detail about the functionality
  of Microsoft Defender for Endpoint, while the existing entry does not.]'
- '[CONFLICT: These topics are not covered in the existing entry.]'
- '[CONFLICT: This topic is not covered in the existing entry.]'
- '[CONFLICT: The existing entry does not cover these topics in detail.]'
- '[CONFLICT: This information is not present in the existing entry.]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-06-15'
  title: Attack Surface Reduction Dashboard for Microsoft Sentinel
  url: https://danielchronlund.com/2022/06/15/attack-surface-reduction-dashboard-for-microsoft-sentinel
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2023-12-07'
  title: 'Microsoft Defender for Endpoint: Key Configurations and Best Practices (2/2)'
  url: https://jannikreinhard.com/2023/12/07/microsoft-defender-for-endpoint-key-configurations-and-best-practices-2-2
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-11-03'
  title: 2025 Microsoft Defender Optimization &amp; Configuration Cheat Sheet
  url: https://jeffreyappel.nl/2025-microsoft-defender-optimization-configuration-cheat-sheet
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-07-11'
  title: Block internet macros in Office, and don&#039;t wait for Microsoft
  url: https://jeffreyappel.nl/blocking-internet-macros-in-office-and-dont-wait-for-microsoft
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-02-12'
  title: Common mistakes during Microsoft Defender for Endpoint deployments
  url: https://jeffreyappel.nl/common-mistakes-during-microsoft-defender-for-endpoint-deployments
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-05-24'
  title: Managing Microsoft Defender for Endpoint with the new Security Management
    feature in MEM/Intune
  url: https://jeffreyappel.nl/managing-microsoft-defender-for-endpoint-with-the-new-security-management-feature-in-mem
stale_after: '2026-06-11'
title: Attack Surface Reduction Rules
topic: intune/security/asr-rules
---

# Attack Surface Reduction Rules

## Attack Surface Reduction Rules

### Overview
Attack Surface Reduction (ASR) rules are a set of security configurations in Windows Defender that help protect against potential threats by blocking or auditing specific actions. Understanding and monitoring these rules is crucial for maintaining a secure environment. [(Source: Existing entry)]

### Key Concepts
- **Windows Defender**: The built-in antivirus and threat protection system in Windows operating systems.
- **ASR Rules**: Specific configurations within Windows Defender that can be set to audit or block certain actions based on predefined conditions.
- **Audit Mode**: A setting for ASR rules where events are logged but not blocked, allowing for monitoring and analysis.
- **Block Mode**: A setting for ASR rules where the specified action is prevented from occurring.
- **ASR Events**: Occurrences when an action subject to an ASR rule takes place, either audited or blocked. [(Source: Existing entry)]

### Configuration
1. Download the latest version of the Attack Surface Reduction Dashboard JSON file from [Daniel Chronlund's GitHub](https://github.com/DanielChronlund/DCSecurityOperations/blob/main/Sentinel%20Workbooks/Attack-Surface-Reduction-Dashboard.json).
2. In your Microsoft Sentinel workspace, click on **Workbooks** and add a new workbook.
3. Replace the JSON content in the new workbook with the downloaded file.
4. Save the workbook with the same Azure resource group as your Sentinel workspace and set the Title to "Attack Surface Reduction Dashboard". [(Source: Existing entry)]

### Common Pitfalls
- Failing to properly configure ASR rules can lead to either overly restrictive or insufficient security measures.
- Not monitoring ASR events can result in missed opportunities for threat detection and incident investigation. [(Source: Existing entry)]

### New Information from "Microsoft Defender for Endpoint: Key Configurations and Best Practices (2/2)"
- The new source provides a detailed explanation of how Microsoft Defender for Endpoint works, including its main components such as Endpoint Behavioral Sensors, Cloud Security Analytics, Threat Intelligence, and more. [CONFLICT: Jannik Reinhard's article goes into greater detail about the functionality of Microsoft Defender for Endpoint, while the existing entry does not.]
- The new source also discusses the onboarding and setup process for Microsoft Defender for Endpoint, as well as continuous monitoring and response, threat and vulnerability management, and creating RBAC roles. [CONFLICT: These topics are not covered in the existing entry.]

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to ASR Rules.]

### Related Topics
- [ASR](asr)
- [attack surface reduction](attack-surface-reduction)
- [block mode](block-mode)
- [audit mode](audit-mode)
- [ASR rules](asr-rules)
- [Microsoft Defender for Endpoint](microsoft-defender-for-endpoint)
- [Endpoint Behavioral Sensors](endpoint-behavioral-sensors)
- [Cloud Security Analytics](cloud-security-analytics)
- [Threat Intelligence](threat-intelligence)
- [Microsoft Defender for Identity](microsoft-defender-for-identity)
- [Security Management in MEM/Intune](security-management-in-mem-intune)

### New Information from "Managing Microsoft Defender for Endpoint with the new Security Management feature in MEM/Intune"
- The new source discusses the general availability of the new Security Settings Management in Microsoft Defender for Endpoint, which allows managing security settings for devices and servers that are not enrolled yet in Microsoft Endpoint Manager/ Intune from one single portal. [CONFLICT: This information is not present in the existing entry.]
- The source also mentions a new blog post that explains the new solution for managing Defender for Endpoint for Windows, macOS, and Linux via Security settings management. [CONFLICT: This information is not present in the existing entry.]

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to ASR Rules.]

### Related Topics
- [ASR](asr)
- [attack surface reduction](attack-surface-reduction)
- [block mode](block-mode)
- [audit mode](audit-mode)
- [ASR rules](asr-rules)
- [Microsoft Defender for Endpoint](microsoft-defender-for-endpoint)
- [Endpoint Behavioral Sensors](endpoint-behavioral-sensors)
- [Cloud Security Analytics](cloud-security-analytics)
- [Threat Intelligence](threat-intelligence)
- [Microsoft Defender for Identity](microsoft-defender-for-identity)
- [Security Management in MEM/Intune](security-management-in-mem-intune)