---
conflicts: []
context_note: Asr Rules is part of the intune domain. Synthesised from 1 community
  source.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2022-06-15'
  title: Attack Surface Reduction Dashboard for Microsoft Sentinel
  url: https://danielchronlund.com/2022/06/15/attack-surface-reduction-dashboard-for-microsoft-sentinel
stale_after: '2026-06-17'
title: Attack Surface Reduction Rules
topic: intune/security/asr-rules
---

# Attack Surface Reduction Rules

## Attack Surface Reduction Rules

### Overview
Attack Surface Reduction (ASR) rules are a set of security configurations in Windows Defender designed to help protect against potential threats by blocking or auditing specific actions that could lead to vulnerabilities. Understanding and implementing these rules is crucial for maintaining the security posture of an organization.

### Key Concepts
- **ASR Rules**: Specific configurations within Windows Defender that can be set to audit or block certain actions based on predefined conditions.
- **Audit Mode**: A setting for ASR rules where events are logged but not blocked, allowing for monitoring and analysis of potential threats.
- **Block Mode**: A setting for ASR rules where the specified actions are prevented from occurring, providing an additional layer of security.
- **ASR Events**: Occurrences triggered by ASR rules when a monitored action takes place.

### Configuration
1. Download or copy the latest version of the Attack Surface Reduction Dashboard JSON file from [Daniel Chronlund's GitHub](https://github.com/DanielChronlund/DCSecurityOperations/blob/main/Sentinel%20Workbooks/Attack-Surface-Reduction-Dashboard.json).
2. In your Microsoft Sentinel workspace, click on **Workbooks** and add a new workbook.
3. Replace the JSON content in the new workbook with the one from the downloaded file.
4. Click on Apply to save the changes.
5. To permanently save the workbook in Sentinel, click on the save icon at the top and set the Title to **Attack Surface Reduction Dashboard**.

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
- [ASR rules](attack-surface-reduction-rules)