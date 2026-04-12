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
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2026-02-03'
  title: How to protect Microsoft Teams with Microsoft Defender
  url: https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender
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

[Daniel Chronlund says that most organizations may not need an extra backup solution, existing entry does not mention this.] [CONFLICT: Daniel Chronlund says that most organizations may not need an extra backup solution, existing entry does not mention this.]

### Related Topics

- [Safe Links](wiki:safe_links)
- [Safe Attachments](wiki:safe_attachments)
- [MDO](wiki:mdo)
- [Detonation](wiki:detonation)
- [Zero-hour purge](wiki:zero-hour_purge)
- [Office 365 data protection and recovery](wiki:office_365_data_protection_and_recovery)

## How to protect Microsoft Teams with Microsoft Defender

How to protect Microsoft Teams with Microsoft Defender

[March 30, 2026](https://jeffreyappel.nl/automatic-migration-from-defender-for-identity-sensor-v2-to-v3-x-and-gmsa-changes/)

9 min read

[March 23, 2026](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/)

7 min read

[February 12, 2026](https://jeffreyappel.nl/how-to-secure-microsoft-copilot-studio-agents-with-real-time-protection/)

13 min read

[February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)

9 min read

[February 2, 2026](https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x/)

5 min read

[January 20, 2026](https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years/)

10 min read

[January 6, 2026](https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage/)

4 min read

### Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > How to protect Microsoft Teams with Microsoft Defender

[Security](https://jeffreyappel.nl/category/security/)

# How to protect Microsoft Teams with Microsoft Defender

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)
0

9 min read

Microsoft released additional protections for Microsoft Teams. The new Office protection is part of the Defender for Office product and protects against more modern phishing methods via chat messages.

In the past years, phishing was mainly based on email entities. There has been a huge increase in phishing via messaging apps like Microsoft Teams. Microsoft improved the detections, releasing new prevention methods against malicious attempts/ messages via Microsoft Teams, and released new insights.

## **Why are collaboration tools more attacked?**

Since the past years, more and more companies have been using collaboration tools and working remotely. Since more customers are using Microsoft Teams, it is a good threat factor to send malicious messages. In the past months, multiple attacks were discovered by Microsoft Security researchers. Attackers are always evaluating new methods to abuse and send malicious messages. Since MFA is more and more enabled, attackers are switching to [AiTM](https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor/)/ Teams messages to bypass current protections.

In the past months, Microsoft released a couple of new capabilities to detect and prevent malicious attacks via Microsoft Teams. Some features are moved from Plan 2 to Plan 1. A good example is ZAP.

## **Which protection is available in which plan**?

The available security feature depends on the availability of which license. The following breakdown informs the ava