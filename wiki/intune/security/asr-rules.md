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
Attack Surface Reduction (ASR) rules are a set of security configurations in Windows Defender that help protect against potential threats by blocking or auditing specific actions. Understanding and monitoring these rules is crucial for maintaining a secure environment.

### Key Concepts
- **Windows Defender**: The built-in antivirus and threat protection system in Windows operating systems.
- **ASR Rules**: Specific configurations within Windows Defender that can be set to audit or block certain actions based on predefined conditions.
- **Audit Mode**: A setting for ASR rules where events are logged but not blocked, allowing for monitoring and analysis.
- **Block Mode**: A setting for ASR rules where the specified action is prevented from occurring.
- **ASR Events**: Occurrences when an action subject to an ASR rule takes place, either audited or blocked.

### Configuration
1. Download the latest version of the Attack Surface Reduction Dashboard JSON file from [Daniel Chronlund's GitHub](https://github.com/DanielChronlund/DCSecurityOperations/blob/main/Sentinel%20Workbooks/Attack-Surface-Reduction-Dashboard.json).
2. In your Microsoft Sentinel workspace, click on **Workbooks** and add a new workbook.
3. Replace the JSON content in the new workbook with the downloaded file.
4. Save the workbook with the same Azure resource group as your Sentinel workspace and set the Title to "Attack Surface Reduction Dashboard".

### Common Pitfalls
- Failing to properly configure ASR rules can lead to either overly restrictive or insufficient security measures.
- Not monitoring ASR events can result in missed opportunities for threat detection and incident investigation.

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to ASR Rules.]

### Related Topics
- [ASR](asr)
- [attack surface reduction](attack-surface-reduction)
- [block mode](block-mode)
- [audit mode](audit-mode)
- [ASR rules](asr-rules)