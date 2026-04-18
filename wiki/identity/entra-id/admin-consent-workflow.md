---
conflict_topics:
- identity/conditional-access/legacy-auth-blocking
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
context_note: Admin Consent Workflow is part of the identity domain. It connects closely
  to Entra Connect Hardening. Synthesised from 2 community sources.
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

## Configuration
1. Understand the Admin Consent Workflow and its role in managing app permissions.
2. Implement proper controls to manage and monitor OAuth apps connected to Azure AD.
3. Configure Conditional Access policies to ensure that only authorized users can access sensitive data.
4. Use Multi-Factor Authentication (MFA) to add an additional layer of security for user accounts.
5. Regularly review and audit app permissions to identify any potential security risks. [CONFLICT: Jeffrey mentions the need for regular audits and reviews, Thomas Naunheim provides a PowerShell cmdlet for monitoring the desired state of the “UsersPermissionToUserConsentToAppEnabled” setting]
6. Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack) [New information from the new source]
7. Review and manage user settings to ensure that end-users do not register applications or set consent permission on their behalf without compliance or risk checks [New information from the new source]

## Common Pitfalls
- Failing to monitor and control OAuth apps, leading to unauthorized access or data breaches.
- Granting excessive permissions to apps without proper evaluation and justification.
- Ignoring the need for regular audits and reviews of app permissions. [CONFLICT: Jeffrey mentions the need for regular audits and reviews]
- Not reviewing user settings to ensure that end-users do not register applications or set consent permission on their behalf without compliance or risk checks [New information from the new source]

## KQL / PowerShell
- Microsoft Cloud App Security (for detection)
- Azure Sentinel (for detection)
- PowerShell cmdlet for monitoring the desired state of the “UsersPermissionToUserConsentToAppEnabled” setting in your tenant. [New information from the new source]

## Related Topics
- Admin Consent
- User Consent
- OAuth App
- Consent Phishing
- Illicit consent attack
- App Permissions

## Blog Post
> [Security](https://jeffreyappel.nl/category/security/) > Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)
>
> [Thomas Naunheim](https://thomasnaunheim.com/) > Detection and Mitigation of Illicit Consent Grant Attacks in Azure AD

[Security](https://jeffreyappel.nl/category/security/)

# Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 2, 2022](https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack/)
1

10 min read

**In the last couple of months, there is a large increase visible in consent phishing emails ([illicit consent attacks](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/detect-and-remediate-illicit-consent-grants?view=o365-worldwide)). Microsoft threat analysts are tracking a continued increase in consent phishing attempts/mails. This blog described some of the Microsoft prevention/detection capabilities against OAuth Consent phishing.**

## What is consent phishing?

Consent phishing attacks (Illicit consent attacks) abuse legitimate cloud service providers' permissions to gain company or user data. In this article, we will cover the detection (with Microsoft Cloud App Security and Azure Sentinel) and mitigation with the latest feature of Azure AD.

## Consent Framework and Default (Tenant) Settings

In the first step, it’s very helpful to know the permission and consent framework in the Microsoft Identity platform. You need to understand the delegation process and potential attack surface.
Microsoft has already documented this in details:
[Microsoft identity platform scopes, permissions, and consent | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)

By default, all users in Azure AD can register applications and set consent permission on their behalf. This represents a risk and should be reviewed by IT compliance, risk, and governance management of your company.
So regardless of phishing attacks, this default setting should be reviewed by IT compliance, risk, and governance management of your company.

The user settings are split into **"User can register applications"**…

…and **"Users can consent to apps accessing company data on their behalf"**:

Follow Microsoft’s step-by-step guide to find out which setting is configured in your tenant:
[Configure how end-users consent to applications using Azure AD | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent)

*Tip: Use the PowerShell cmdlet for monitoring your desired state of the “UsersPermissionToUserConsentToAppEnabled” setting in your tenant.*

This default settings makes it easy for users to enable access or onboard any SaaS applications.
Nevertheless, it is [recommended by Microsoft to disable user consent operations](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#restrict-user-consent-operations).
This is also part of the identity secure score:

In the last month, we are seeing increased numbers of consent grant attacks by phishing mails but also Microsoft introduced new (public preview) features to detect/manage consent request.
By now every organization should review their settings and methods to detect, remediate, and mitigate these attacks.

## Attack methods and scenarios

Many popular phishing attacks and campaigns try to take over accounts by user consent requests from apps that look like Office 365 services.
Attackers sending mails with subjects like “storage upgrade” or “shared OneDrive files” to fool the victims that permission to Office 365 is required.

In my opinion, it’s unrealistic to prevent this attacks or minimize their impact without proper monitoring and control of OAuth apps connected to Azure AD.

## Mitigation

To mitigate illicit consent attacks, Microsoft recommends the following steps:
1. Review and manage user settings to ensure that end-users do not register applications or set consent permission on their behalf without compliance or risk checks.
2. Implement proper controls to manage and monitor OAuth apps connected to Azure AD.
3. Configure Conditional Access policies to ensure that only authorized users can access sensitive data.
4. Use Multi-Factor Authentication (MFA) to add an additional layer of security for user accounts.
5. Regularly review and audit app permissions to identify any potential security risks.
6. Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack).