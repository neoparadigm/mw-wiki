---
conflicts:
- '[CONFLICT: officedocspr5 provides additional information about managing external
  meetings and chat, while the existing entry focuses solely on Teams External Access
  and Federation Control.]'
- '[CONFLICT: Michael Morten Sonne provides additional details on how to enable this
  feature]'
domain: teams
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2021-02-22'
  title: Manage Teams External Access for Allowed Domains Using PowerShell and Teams
    Approvals
  url: https://danielchronlund.com/2021/02/22/manage-teams-external-access-for-allowed-domains-using-powershell-and-teams-approvals
- author: officedocspr5
  crawled: '2026-04-14'
  date: '2025-11-19'
  title: IT Admins - Manage external meetings and chat with people and organizations
    using Microsoft identities - Microsoft Teams
  url: https://learn.microsoft.com/en-us/microsoftteams/manage-external-access
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-12-06'
  title: Global Secure Access – Guest Access support with the Windows Client (B2B
    Guest) – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/global-secure-access-guest-access-support-with-the-windows-clientb2b-guest
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: ''
  title: Azure AD/Entra ID
  url: https://blog.sonnes.cloud/topics/azure-ad-entra-id
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: ''
  title: Global Secure Access
  url: https://blog.sonnes.cloud/topics/global-secure-access
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: ''
  title: Identity
  url: https://blog.sonnes.cloud/topics/identity
stale_after: '2026-06-13'
title: Teams External Access and Federation Control
topic: teams/security/external-access-federation
---

# Teams External Access and Federation Control

## Overview
This topic discusses managing Teams external access for allowed domains using PowerShell and Teams Approvals, a crucial aspect of Microsoft Teams governance in highly regulated industries. The process enables organizations to control chat and call functionality with external Teams and Skype for Business users based on a list of trusted domains.

The new source article provides additional information about managing external meetings and chat with people and organizations using Microsoft identities in Microsoft Teams, as well as introducing the Global Secure Access (GSA) feature for Guest Access support with the Windows Client (B2B Guest).

## Key Concepts
- Teams External Access
- Federation (External access in the Teams admin center)
- Allowed Domains
- PowerShell scripting for Microsoft Teams
- Teams Approvals
- Microsoft Accounts
- Skype Users
- Global Secure Access (GSA)
- Azure AD/Entra ID [NEW]

## Configuration
1. Install the Microsoft Teams PowerShell module, if not already installed: `Install-Module MicrosoftTeams`
2. Connect to Microsoft Teams using PowerShell: `New-CsOnlineSession | Import-PSSession`
3. Run the provided PowerShell script (Enable-TeamsFederationForAllowedDomainsOnly) to enable federation for allowed domains only, with an optional switch to remove existing domains before adding new ones. [CONFLICT: Michael Morten Sonne provides additional details on how to enable this feature]
4. Implement Teams Approvals to make this process available throughout your organization.
5. Configure external access for other Microsoft 365 organizations (chat and meetings), Teams users not managed by an organization (those users with a [Microsoft account](https://account.microsoft.com)) (chat only), and Skype users (chat only). Users in your organization can accept or block incoming chats from people outside the organization.
6. Follow the steps outlined in the Global Secure Access (GSA) article to enable Guest Access support with the Windows Client (B2B Guest). [CONFLICT: Michael Morten Sonne provides additional details on how to enable this feature]
7. To manage external meetings and chat using Azure AD/Entra ID, follow the instructions provided in the [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/) blog by Michael Morten Sonne.

## Common Pitfalls
- Neglecting to properly configure Teams federation settings can lead to unintended communication with external users not on the allowed list.
- Manual configuration of Teams federation for multiple domains can be time-consuming and prone to errors.

New source article: "Global Secure Access" and "Identity" by Michael Morten Sonne

8 posts in Global Secure Access
9 minute read

- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Global Secure Access](https://blog.sonnes.cloud/topics/global-secure-access/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)

52 posts in Identity
3 minute read

- [Active Directory](https://blog.sonnes.cloud/topics/active-directory/)
- [Analyzer](https://blog.sonnes.cloud/topics/analyzer/)
- [Attacks/compromise](https://blog.sonnes.cloud/topics/attacks/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Microsoft](https://blog.sonnes.cloud/topics/microsoft/)
- [Microsoft Defender for Identity](https://blog.sonnes.cloud/topics/microsoft-defender-for-identity/)
- [Security](https://blog.sonnes.cloud/topics/security/)