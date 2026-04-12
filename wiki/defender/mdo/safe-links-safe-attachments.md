---
conflicts:
- '[CONFLICT: Daniel Chronlund suggests that backup might not be necessary in most
  cases, while this section mentions potential issues with misconfigurations.]'
- '[CONFLICT: Daniel Chronlund says X, existing entry says Y]'
domain: defender
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-07'
  title: Configure Office 365 ATP Like a Pro with ORCA
  url: https://danielchronlund.com/2020/01/07/configure-office-365-atp-like-a-pro-with-orca
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-09-16'
  title: Is it necessary to back up your data in Office 365 externally?
  url: https://danielchronlund.com/2020/09/16/is-it-necessary-to-back-up-your-data-in-office-365-externally
stale_after: '2026-06-11'
title: Safe Links and Safe Attachments
topic: defender/mdo/safe-links-safe-attachments
---

# Safe Links and Safe Attachments

## Safe Links and Safe Attachments

### Overview

This topic discusses the configuration of Safe Links and Safe Attachments in Office 365 Advanced Threat Protection (ATP) using ORCA, a tool provided by Microsoft to ensure proper configuration following best practices. These features help protect against malicious links and attachments in emails.

### Key Concepts

- **ORCA (Office 365 ATP Recommended Configuration Analyzer)**: A PowerShell module that checks the configuration of EOP and Office 365 ATP to ensure it follows Microsoft's best practices.
- **SafeLinks**: A feature that helps protect against malicious links in emails by rewriting URLs to a temporary Microsoft server, where they are scanned for threats before being delivered to the recipient.
- **SafeAttachments**: A feature that scans email attachments for viruses and other malware before they are delivered to the recipient's mailbox.

### Configuration

1. Install the ORCA PowerShell Module: `Install-Module -Name ORCA`
2. Connect to Exchange Online with PowerShell as usual.
3. Generate the ORCA report: `Get-ORCAReport`
4. Follow the recommendations in the generated report to configure SafeLinks and SafeAttachments.

### Common Pitfalls

- Misconfiguration of SafeLinks and SafeAttachments policies can lead to false positives or negatives, affecting user experience and email delivery. [CONFLICT: Daniel Chronlund suggests that backup might not be necessary in most cases, while this section mentions potential issues with misconfigurations.]
- Failure to enable Zero Hour Autopurge can result in the persistence of malicious emails in the mailbox.

### KQL / PowerShell

```powershell
# Generate ORCA report
Get-ORCAReport
```

### Related Topics

- [Safe Links](wiki:safe_links)
- [Safe Attachments](wiki:safe_attachments)
- [MDO](wiki:mdo)
- [Detonation](wiki:detonation)
- [Zero-hour purge](wiki:zero-hour_purge)
- [Office 365 Backup](wiki:office_365_backup) [New addition from the new source]

### Office 365 Backup

Is it necessary to back up your data in Office 365 externally? – Daniel Chronlund Cloud Security Blog

Office 365 backup is a hot topic and there are a lot of opinions out there. My opinion and short answer is No, most organisations probably don’t need an extra backup solution for Office 365 data, or there are more important security investments to prioritise before cloud backup. However, there might be exceptions for compliance reasons and such, so here is my long answer.

It may be helpful to know that it is relatively rare that organisations make external backups of Office 365 data today. It is not a good enough reason to do backups, just because that is how it has always been. I would argue that in most cases it works just fine with the features included in the service. Backup is something you already pay for!

First, Microsoft always keeps multiple copies of your data in different [fault domains](https://docs.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-data-resiliency-overview?view=o365-worldwide#microsoft-365-data-resiliency-principles) (geographically separated datacenters).

Second, Office 365 features such as [Versioning](https://support.microsoft.com/en-us/office/restore-a-previous-version-of-a-file-stored-in-onedrive-159cad6d-d76e-4981-88ef-de6e96c93893) in OneDrive and SharePoint, [Archiving](https://docs.microsoft.com/en-us/microsoft-365/compliance/enable-archive-mailboxes?view=o365-worldwide), [Retention policies](https://docs.microsoft.com/en-us/microsoft-365/compliance/retention?view=o365-worldwide), [In-Place hold and Litigation hold](https://docs.microsoft.com/en-us/exchange/security-and-compliance/in-place-and-litigation-holds), holds in SharePoint, self-service [“restore deleted files”](https://support.microsoft.com/en-us/office/restore-items-in-the-recycle-bin-that-were-deleted-from-sharepoint-or-teams-6df466b6-55f2-4898-8d6e-c0dff851a0be), [eDiscovery](https://docs.microsoft.com/en-us/microsoft-365/compliance/ediscovery?view=o365-worldwide), and [Content search](https://docs.microsoft.com/en-us/microsoft-365/compliance/content-search?view=o365-worldwide), help customers protect and restore lost data. These, if configured correctly, protects your data from human errors and ransomware in the cloud.

All the above are **Office 365 E3** functionality.

You can even lock your data to keep it forever by turning on [Preservation Lock](https://docs.microsoft.com/en-us/microsoft-365/compliance/retention?view=o365-worldwide#use-preservation-lock-to-comply-with-regulatory-requirements) which

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: Daniel Chronlund says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.