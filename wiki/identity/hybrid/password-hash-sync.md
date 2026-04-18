---
conflicts: []
context_note: Password Hash Sync is part of the identity domain. Synthesised from
  1 community source.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: omondiatieno
  crawled: '2026-04-18'
  date: '2025-04-09'
  title: What is Microsoft Entra Connect and Connect Health. - Microsoft Entra ID
  url: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect
stale_after: '2026-07-17'
title: Password Hash Sync and Leaked Credential Detection
topic: identity/hybrid/password-hash-sync
---

# Password Hash Sync and Leaked Credential Detection

## Overview
Password Hash Sync (PHS) is a sign-in method in Microsoft Entra Connect that synchronizes a hash of a user's on-premises Active Directory (AD) password with Microsoft Entra ID. This feature ensures users can sign in to cloud services using the same credentials as their on-premises accounts, while maintaining security and reducing the need for password resets.

## Key Concepts
- Password Hash Sync (PHS): A method that synchronizes a hash of a user's on-premises AD password with Microsoft Entra ID.
- Leaked Credential Detection: A feature in Microsoft Entra Connect Health that identifies potential security risks by checking hashed passwords against known compromised credentials databases.

## Configuration
1. Install and configure Microsoft Entra Connect on your on-premises environment.
2. Configure Password Hash Sync during the setup process or using the Azure AD Connect wizard.
3. Ensure that the same user principal name (UPN) is used for both on-premises AD and Azure AD.
4. Enable Leaked Credential Detection in Microsoft Entra Connect Health.

## Common Pitfalls
- Using different UPNs for on-premises AD and Azure AD can cause authentication issues.
- Incorrectly configuring Password Hash Sync or Leaked Credential Detection may lead to authentication failures or security vulnerabilities.

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to Password Hash Sync and Leaked Credential Detection.]

## Related Topics
- [Password Hash Sync](whatis-phs)
- PHS
- [Leaked credentials](https://learn.microsoft.com/en-us/security/leaked-credentials/)
- Smart Lockout
- [Entra Connect sync](how-to-connect-sync-whatis)