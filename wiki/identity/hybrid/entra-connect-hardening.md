---
conflict_topics:
- identity/entra-id/service-principal-governance
- identity/pim/break-glass-accounts
conflicts:
- '[CONFLICT: Michael Morten Sonne''s new source provides additional details on Microsoft
  Defender for Identity expanding support to servers with Microsoft Entra Connect
  and new posture recommendations focusing on Active Directory, but the existing entry
  does not include this information.]'
- '[CONFLICT: Michael Morten Sonne says X, existing entry says Y]'
context_note: Entra Connect Hardening is part of the identity domain. It connects
  closely to External Identities and Admin Consent Workflow. Synthesised from 4 community
  sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
prerequisite_topics:
- identity/entra-id/external-identities
related_topics:
- identity/entra-id/external-identities
- identity/entra-id/admin-consent-workflow
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-01-28'
  title: Entra ID – New build-in audit feature in Entra Connect is finally here! –
    Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-new-build-in-audit-feature-in-entra-connect-is-finally-here
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-08-28'
  title: Microsoft Defender for Identity – Expands support to servers with Microsoft
    Entra Connect – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/microsoft-defender-for-identity-expands-support-to-servers-with-microsoft-entra-connect
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-10-07'
  title: Microsoft Defender for Identity – New posture recommendations focusing on
    Active Directory – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/microsoft-defender-for-identity-new-posture-recommendations-focusing-on-active-directory
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: ''
  title: Entra ID Connect
  url: https://blog.sonnes.cloud/topics/entra-id-connect
stale_after: '2026-06-17'
title: Entra Connect Server Hardening
topic: identity/hybrid/entra-connect-hardening
---

# Entra Connect Server Hardening and Microsoft Defender for Identity Expansion

## Entra Connect Server Hardening

### Overview
This topic discusses the hardening of the Entra Connect server to improve security and protect against potential threats. The importance lies in ensuring a secure identity management system for both cloud and on-premises resources.

### Key Concepts
- Hybrid Identity
- Secure Access
- Conditional Access
- Microsoft Entra Connect Sync
- PowerShell scripts
- [Microsoft Defender for Identity](#microsoft-defender-for-identity) (New)
- [Entra ID Connect](#entra-id-connect) (New)

### Configuration
1. Update Entra Connect Sync to version 2.4.129.0 or later, which includes the new auditing capabilities for administrator events. (New source does not specify an update related to this step.)
2. Enable auditing of administrator events via PowerShell script:
   ```powershell
   Set-EntraConnectSyncAuditPolicy -Enable $true
   ```
3. Manually enable/disable default auditing of administrator events through the user interface.

### Common Pitfalls
- Neglecting to update Entra Connect Sync to the latest version, which may not include essential security features or bug fixes. (New source does not specify an update related to this step.)
- Failing to properly configure auditing settings, leading to incomplete or inaccurate logs.

### KQL / PowerShell
The article provides two PowerShell scripts for enabling and disabling auditing of administrator events via PowerShell:

1. Enable auditing:
   ```powershell
   Set-EntraConnectSyncAuditPolicy -Enable $true
   ```
2. Disable auditing:
   ```powershell
   Set-EntraConnectSyncAuditPolicy -Enable $false
   ```

### Microsoft Defender for Identity (New)
- [Attacks/compromise](https://blog.sonnes.cloud/topics/attacks/)
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Entra ID Connect](#entra-id-connect) (New)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Microsoft Defender for Identity](#microsoft-defender-for-identity) (New)
- [Security](https://blog.sonnes.cloud/topics/security/)

### Microsoft Defender for Identity – Expands support to servers with Microsoft Entra Connect (New)
[by Michael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

August 28, 2024

9 minute read

Last Updated on June 2, 2025 by [Michael Morten Sonne](https://sonnes.cloud)

##### Table of Contents

1. [Intoduction](#intoduction)
   1. [What is Microsoft Defender for Identity](#what-is-microsoft-defender-for-identity)
   2. [What is Entra ID Connect?](#what-is-entra-id-connect)
   3. [Prerequisites](#prerequisites)
   4. [What is added](#what-is-added)
      1. [New detections](#new-detections)
      2. [Additional Improvements and Capabilities](#additional-improvements-and-capabilities)
      3. [New Posture Recommendations](#new-posture-recommendations)
2. [How to install the new sensor](#how-to-install-the-new-sensor)
   1. [Get the in

### Entra ID Connect (New)
- [Active Directory](https://blog.sonnes.cloud/topics/active-directory/)
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Entra ID Connect](https://blog.sonnes.cloud/topics/entra-id-connect/)
- [GitHub](https://blog.sonnes.cloud/topics/github/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Microsoft](https://blog.sonnes.cloud/topics/microsoft/)
- [Microsoft 365](https://blog.sonnes.cloud/topics/microsoft-365-cloud/)
- [Passwordless](https://blog.sonnes.cloud/topics/passwordless-microsoft/)
- [PowerShell](https://blog.sonnes.cloud/topics/general/software/powershell/)
- [Security](https://blog.sonnes.cloud/topics/security/)
- [Windows](https://blog.sonnes.cloud/topics/windows/)

## [Entra ID – Entra Connect – Secure App & Certificate-Based Authentication is here! Plus: I built you a better way to manage it](https://blog.sonnes.cloud/entra-id-entra-connect-secure-app-certificate-based-authentication-is-here-plus-i-built-you-a-better-way-to-manage-it/)

Introduction Yes finally, it’s here! No more need for an old-school, classic service account in your Entra ID…

[byMichael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

May 29, 2025

Read More

9 minute read

- [Active Directory](https://blog.sonnes.cloud/topics/active-directory/)
- [Attacks/compromise](https://blog.sonnes.cloud/topics/attacks/)
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Entra ID Connect](#entra-id-connect) (New)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Microsoft Defender for Identity](https://blog.sonnes.cloud/topics/microsoft-defender-for-identity/)
- [Security](https://blog.sonnes.cloud/topics/security/)

## [Microsoft Defender for Identity – Expands support to servers with Microsoft Entra Connect](https://blog.sonnes.cloud/microsoft-defender-for-identity-expands-support-to-servers-with-microsoft-entra-connect/)

Intoduction What is Microsoft Defender for Identity Microsoft Defender for Identity is a comprehensive security solution provided by…

[byMichael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

August 28, 2024

Read More

14 minute read

- [Active Directory](https://blog.sonnes.cloud/topics/active-directory/)
- [Attacks/compromise](https://blog.sonnes.cloud/topics/attacks/)
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Entra ID Connect](#entra-id-connect) (New)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Security](https://blog.sonnes.cloud/topics/security/)

## [Azure AD – Why use Cloud-Only Administrative/normal accounts and how to protect them in Azure AD from on-premises attacks](https://blog.sonnes.cloud/why-use-cloud-only-account)

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: Michael Morten Sonne says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.