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
context_note: Entra Connect Hardening is part of the identity domain. Synthesised
  from 5 community sources.
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
- author: Brandon Colley
  crawled: '2026-04-18'
  date: '2025-12-03'
  title: 'Lifeline or Liability: Managing Emergency Accounts in Hybrid Environments'
  url: https://practical365.com/lifeline-or-liability-managing-emergency-accounts-in-hybrid-environments
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
- [Lifeline or Liability: Managing Emergency Accounts in Hybrid Environments](#lifeline-or-liability-managing-emergency-accounts-in-hybrid-environments) (New Source)

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
   2. [What is Entra ID Connect?](#what-is-entra-id-connect) (New Concept from new source)
   3. [Prerequisites](#prerequisites)
   4. [What is added](#what-is-added)
      1. [New detections](#new-detections)
      2. [Additional Improvements and Capabilities](#additional-improvements-and-capabilities)
      3. [New Posture Recommendations](#new-posture-recommendations)
2. [How to install the new sensor](#how-to-install-the-new-sensor

## Lifeline or Liability: Managing Emergency Accounts in Hybrid Environments (New Source)

Lifeline or Liability: Managing Emergency Accounts in Hybrid Environments | Practical365

If you manage Active Directory (AD) or Entra ID, you’ve probably encountered break-glass or emergency access accounts—special accounts held in reserve for worst-case scenarios. These accounts serve as your administrative lifeline when your normal identity systems fail. But, just like a fire extinguisher, an emergency account is only valuable if it’s charged, reachable, and tested.

### The Purpose of Emergency Accounts

Emergency accounts exist for one simple goal: to ensure administrative access to critical systems in the event of catastrophic failure. Commonly referred to as “break-glass” accounts, these emergency accounts must be outage resistant, fully isolated, and disaster ready.

An emergency account must be able to authenticate without dependency on external identity providers. This means the accounts must originate from the system they protect. In the case of AD, an emergency account must reside locally to the domain. For Entra ID, emergency accounts must be cloud-only and not federated or synchronized with another identity provider.

Administrators should carefully evaluate any reliance on external sources or security protections that could also fail during an outage. This includes Conditional Access policies, MFA providers, and network connectivity. Successful implementation of an emergency account maximizes outage resilience by ensuring usability under degraded conditions.

Emergency accounts have a long history in the hybrid identity space. As the threat landscape has changed over the years, so have the best practices that surround the proper implementation of emergency accounts. Migrating from a legacy practice to a more modern approach is not only an important security control; it improves the resiliency of an organization during an emergency.

### From Legacy AD Habits to Modern Hygiene (New Source)

Historically, protecting the built-in AD Administrator account was about obscurity and rotation — renaming the account and resetting the password. More security-minded organizations might even disable the Administrator account, but others may still allow this account to log in anywhere in the domain.

New [Microsoft guidance](https://learn.microsoft.com/en-us/windows) (New Source Content)