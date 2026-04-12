---
conflicts:
- '[CONFLICT: Daniel Chronlund says that most organizations may not need an extra
  backup solution, existing entry does not mention this.]'
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

Safe Links and Safe Attachments are security features in Office 365 Advanced Threat Protection (ATP) designed to protect users from malicious links and attachments in emails. These features help prevent phishing attacks, ransomware, and other forms of cyber threats.

### Key Concepts

- Safe Links: A feature that scans URLs in emails for potential threats and replaces them with temporary, safe links.
- Safe Attachments: A feature that scans email attachments for malicious content before they are downloaded or opened by the user.
- Zero-hour auto-purge: A setting that automatically removes suspicious emails from the inbox to prevent potential threats from spreading.

### Configuration

1. Enable Safe Links and Safe Attachments in the Office 365 Security & Compliance Center.
2. Configure policies for Safe Links and Safe Attachments, including settings for URL detonation, attachment scanning, and user notifications.
3. Test the configuration to ensure that it is working correctly.

### Common Pitfalls

- Not enabling or properly configuring Safe Links and Safe Attachments can leave users vulnerable to phishing attacks and other forms of cyber threats.
- Overly restrictive policies can result in legitimate emails being blocked or delayed, causing frustration for users.

### KQL / PowerShell

```powershell
# Get SafeLinks policy
Get-SafeLinksPolicy -Identity "Default"

# Set SafeAttachments policy
Set-OrganizationConfig -SafeAttachmentPolicies @{Add="Custom Policy Name"; ExcludedFileTypes="*.exe"}
```

### Is it necessary to back up your data in Office 365 externally?

Office 365 includes several built-in features for protecting and restoring lost data, such as Versioning in OneDrive and SharePoint, Archiving, Retention policies, In-Place hold and Litigation hold, holds in SharePoint, self-service "restore deleted files", eDiscovery, and Content search. These features help protect against human errors and ransomware in the cloud.

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/) suggests that most organizations may not need an extra backup solution for Office 365 data, as these features are already included in the service. However, there might be exceptions for compliance reasons and such.

[CONFLICT: Daniel Chronlund says that most organizations may not need an extra backup solution, existing entry does not mention this.]

### Related Topics

- [Safe Links](wiki:safe_links)
- [Safe Attachments](wiki:safe_attachments)
- [MDO](wiki:mdo)
- [Detonation](wiki:detonation)
- [Zero-hour purge](wiki:zero-hour_purge)
- [Office 365 data protection and recovery](wiki:office_365_data_protection_and_recovery)