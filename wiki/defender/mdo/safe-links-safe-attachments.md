---
conflicts: []
context_note: Safe Links Safe Attachments is part of the defender domain. Synthesised
  from 1 community source.
domain: defender
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2026-02-03'
  title: How to protect Microsoft Teams with Microsoft Defender
  url: https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender
stale_after: '2026-06-17'
title: Safe Links and Safe Attachments
topic: defender/mdo/safe-links-safe-attachments
---

# Safe Links and Safe Attachments

## Safe Links and Safe Attachments

### Overview
Safe Links and Safe Attachments are security features provided by Microsoft Defender for Office to protect against malicious URLs and files shared via Microsoft Teams, SharePoint, and OneDrive. These features help prevent phishing attacks and data breaches.

### Key Concepts
- Safe Links: Time-of-click URL protection that scans URLs in real time for known threats before they are clicked.
- Safe Attachments: Time-of-click file protection that scans files in real time for known threats before they are downloaded.
- Time-of-click: Scanning occurs when the user clicks on a link or attempts to download a file, not during the initial delivery of the message.

### Configuration
To enable Safe Links and Safe Attachments, follow these steps:

1. Navigate to the Microsoft 365 Defender portal (<https://security.microsoft.com/>)
2. Go to Policies > Threat policies > Create a new policy
3. Select Office apps > Teams, SharePoint, and OneDrive > Set policies
4. Enable Safe Links and Safe Attachments
5. Configure settings as needed (e.g., URL blocking, file types to scan)
6. Save the policy

### Common Pitfalls
- Not enabling Safe Links and Safe Attachments for all relevant users and apps
- Using overly restrictive policies that block legitimate links or files
- Failing to update policies as new threats emerge

### KQL / PowerShell
These features do not require specific queries or scripts. Configuration can be managed through the Microsoft 365 Defender portal or PowerShell using the Set-MDATPThreatPolicy cmdlet.

### Related Topics
- Safe links
- Safe attachments
- MDO (Microsoft Defender for Office)
- Detonation
- Zero-hour purge