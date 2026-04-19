---
conflict_topics:
- identity/conditional-access/token-protection
- identity/entra-id/entra-id-protection
conflicts:
- '[CONFLICT: Jeffrey mentions consent phishing attacks specifically]'
- '[CONFLICT: Jeffrey mentions the need for regular audits and reviews]'
- '[CONFLICT: Jeffrey says X, existing entry says Y]'
- '[CONFLICT: Jeffrey mentions consent phishing attacks specifically, Thomas Naunheim
  mentions illicit consent attacks]'
- '[CONFLICT: Jeffrey mentions the need for regular audits and reviews, Thomas Naunheim
  provides a PowerShell cmdlet for monitoring the desired state of the “UsersPermissionToUserConsentToAppEnabled”
  setting]'
context_note: Admin Consent Workflow is part of the identity domain. Synthesised from
  4 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
prerequisite_topics:
- identity/hybrid/entra-connect-hardening
related_topics:
- identity/hybrid/entra-connect-hardening
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-06-07'
  title: Controle op Azure AD machtigingen met de Admin consent workflow; zo werkt
    het
  url: https://jeffreyappel.nl/controle-op-azure-ad-machtigingen-met-de-admin-consent-workflow-zo-werkt-het
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-02-02'
  title: Protect against AzureAD OAuth Consent phishing attempts (Illicit consent
    attack)
  url: https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2020-01-21'
  title: Detection and Mitigation of Illicit Consent Grant Attacks in Azure AD
  url: https://www.cloud-architekt.net/detection-and-mitigation-consent-grant-attacks-azuread
- author: Mezba Uddin
  crawled: '2026-04-18'
  date: '2025-08-26'
  title: Investigating OAuth App Abuse with the Graph Activity Log
  url: https://practical365.com/investigating-oauth-app-abuse-with-the-graph-activity-log
stale_after: '2026-06-17'
title: Admin Consent Workflow and OAuth App Control
topic: identity/entra-id/admin-consent-workflow
---

# Admin Consent Workflow and OAuth App Control

## Overview
The Admin Consent Workflow and OAuth App Control is a crucial aspect of securing Azure Active Directory (Azure AD) permissions by preventing unwanted permissions before they become problematic. This topic matters because as more applications are connected via the cloud, it's essential to ensure that the single identity associated with these apps is securely managed.

## Key Concepts
- Admin Consent Workflow
- OAuth App Control
- Preventing unauthorized access and data breaches
- Phishing attacks targeting app permissions [CONFLICT: Jeffrey mentions consent phishing attacks specifically, Thomas Naunheim mentions illicit consent attacks]
- Illicit consent attacks [New information from the new source]

## Configuration
1. Understand the Admin Consent Workflow and its role in managing app permissions.
2. Implement proper controls to manage and monitor OAuth apps connected to Azure AD.
3. Configure Conditional Access policies to ensure that only authorized users can access sensitive data.
4. Use Multi-Factor Authentication (MFA) to add an additional layer of security for user accounts.
5. Regularly review and audit app permissions to identify any potential security risks. [CONFLICT: Jeffrey mentions the need for regular audits and reviews, Thomas Naunheim provides a PowerShell cmdlet for monitoring the desired state of the “UsersPermissionToUserConsentToAppEnabled” setting]
6. Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack) [New information from the new source]
7. Review and manage user settings to ensure that end-users do not register applications or set consent permission on their behalf without compliance or risk checks [New information from the new source]
8. Investigate OAuth app abuse with the Graph Activity Log (Mezba Uddin) [New information from the new source]

## Common Pitfalls
- Failing to monitor and control OAuth apps, leading to unauthorized access or data breaches.
- Granting excessive permissions to apps without proper evaluation and justification.
- Ignoring the need for regular audits and reviews of app permissions. [CONFLICT: Jeffrey mentions the need for regular audits and reviews]
- Not reviewing user settings to ensure that end-users do not register applications or set consent permission on their behalf without compliance or risk checks [New information from the new source]
- Overlooking illicit consent attacks as a potential threat vector. [New information from the new source]

## KQL / PowerShell
- Microsoft Cloud App Security (for detection)
- Azure Sentinel (for detection)
- PowerShell cmdlet for monitoring the desired state of the “UsersPermissionToUserConsentToAppEnabled” setting in your tenant. [New information from the new source]
- Graph Activity Log for investigating OAuth app abuse. [New information from the new source]

## Related Topics
- Admin Consent
- User Consent
- OAuth App
- Consent Phishing
- Illicit consent attack
- App Permissions
- Investigating OAuth app abuse with Graph Activity Log (Mezba Uddin) [New information from the new source]