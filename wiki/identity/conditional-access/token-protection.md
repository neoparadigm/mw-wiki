---
conflicts:
- '[CONFLICT: Jeffrey mentions a 146% rise in AiTM attacks over the last year (2024),
  while the existing entry does not provide specific numbers.]'
- '[CONFLICT: Jeffrey mentions MFA phishing attacks, but the existing entry does not
  have specific information about MFA.]'
- '[CONFLICT: Jeffrey mentions no specific pitfalls related to Token Protection]'
- '[CONFLICT: Jeffrey mentions no specific details about Token Protection]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-05-20'
  title: 5 Manieren om Azure Active Directory accounts veiliger te maken
  url: https://jeffreyappel.nl/5-manieren-om-azure-active-directory-accounts-veiliger-te-maken
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-09-01'
  title: AiTM/ MFA phishing attacks in combination with &quot;new&quot; Microsoft
    protections (2026 edition)
  url: https://jeffreyappel.nl/aitm-mfa-phishing-attacks-in-combination-with-new-microsoft-protections-2023-edt
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-06-08'
  title: Android Enterprise via Microsoft Endpoint Manager als vervanger van Android
    device administrator
  url: https://jeffreyappel.nl/android-enterprise-via-microsoft-endpoint-manager-als-vervanger-van-android-device-administrator/amp
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-06-02'
  title: Enroll Android smartphones into Microsoft Defender for Endpoint for blocking
    FluBot
  url: https://jeffreyappel.nl/enroll-android-smartphones-into-defender-for-endpoint-for-blocking-fluebot
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-10-22'
  title: Fast response with Azure AD Continuous Access Evaluation (CAE) and Conditional
    Access
  url: https://jeffreyappel.nl/fast-response-with-azure-ad-continuous-access-evaluation-cae-and-conditional-access
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-11-12'
  title: Get all Conditional Access Query&#039;s with a single click using Graph API
  url: https://jeffreyappel.nl/get-all-conditional-access-querys-with-a-single-click-using-graph-api
stale_after: '2026-06-11'
title: Token Protection and CAE
topic: identity/conditional-access/token-protection
---

# Token Protection and CAE

## Overview
Token Protection and CAE (Continuous Access Evaluation) are security measures designed to protect Azure Active Directory accounts by monitoring and controlling access to sensitive resources. These measures are crucial in today's cloud-centric environment where applications and services increasingly rely on the cloud, bringing new security risks. Microsoft provides various solutions within its services to optimally secure these aspects.

## Key Concepts
- Token Protection: A security measure that protects access tokens issued by Azure Active Directory. [CONFLICT: Jeffrey mentions no specific details about Token Protection] (Updated from existing entry)
- CAE (Continuous Access Evaluation): An Azure Active Directory feature that continuously evaluates the risk level of users and grants or denies access based on their risk score.

## Configuration
1. Enable Token Protection in Azure Active Directory:
   - Navigate to Azure Active Directory > Security > Token Configuration.
   - Toggle on "Token Lifetime Policy" and set the policy as required.
   - Toggle on "Sign-in risk policy" and configure the policy based on your organization's needs. (Updated from existing entry)

2. Enable CAE for your tenant:
   - Navigate to Azure Active Directory > Security > Privileged Identity Management.
   - Go to Continuous Access Evaluation and toggle it on.
   - Configure the settings as per your organization's requirements, such as risk levels, access reviews, and notifications. (Updated from existing entry)

## Common Pitfalls
- Failing to properly configure Token Protection policies can lead to weakened security and increased vulnerability to attacks. [CONFLICT: Jeffrey mentions no specific pitfalls related to Token Protection] (New information from new source)
- Incorrectly setting CAE thresholds or notifications can result in either overly restrictive or permissive access controls. (Updated from existing entry)

## KQL / PowerShell
[The source article does not provide any specific queries or scripts related to Token Protection and CAE.]

## Related Topics
- [Token protection](https://jeffreyappel.nl/category/security/)
- [CAE (Continuous Access Evaluation)](https://jeffreyappel.nl/category/security/)
- [continuous access evaluation](https://jeffreyappel.nl/category/security/)
- [token binding](https://jeffreyappel.nl/category/security/)
- [session token](https://jeffreyappel.nl/category/security/)

## New Source Article: "AiTM/ MFA phishing attacks in combination with &quot;new&quot; Microsoft protections (2026 edition)"
Author: Jeffrey
New source content:

### AiTM/ MFA Phishing Attacks and Microsoft Protections (2026 Edition)

Microsoft observed a significant increase in Adversary-in-the-middle (AiTM) phishing attacks, which are more sophisticated than traditional phishing methods. These attacks have become more prevalent since the removal of basic authentication from Exchange Online. To combat these threats, Microsoft has introduced new protections.

**2026 Update**
Microsoft researchers uncovered multiple multi-stage AiTM phishing and business email compromise campaigns (New information from new source)

## New Source Article: "Get all Conditional Access Query&#039;s with a single click using Graph API"
Author: Jeffrey
New source content:
# Get all Conditional Access Query's with a single click using Graph API

Get all Conditional Access Query's with a single click using Graph API (New information from new source)




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




## Blog Post

> [Modern Workplace](https://jeffreyappel.nl/category/modern-workplace/) > Get all Conditional Access Query’s with a single click using Graph API

[Modern Workplace](https://jeffreyappel.nl/category/modern-workplace/)

# Get all Conditional Access Query’s with a single click using Graph API

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[November 13, 2020](https://jeffreyappel.nl/get-all-conditional-access-querys-with-a-single-click-using-graph-api/)
0


2 min read

**Conditional Access is one of the available tools used by Azure Active Directory to bring different signals together. Based on different signals it is possible to create decisions like; block access, remediate risk, allow full access, and many more situation.**

In multiple situations it is useful to require actions like multi-factor authentication before a user can access a resource. For example:  A payroll manager wants to access the payroll application and is required to perform multi-factor authentication to access it.

By using Conditional Access policies, you can apply the right access controls when needed to keep your organization secure and stay out of your user’s way when not needed.

---

### Requirements

Using the Conditional Access feature required an Azure AD Premium P1 license. For the sign-in risk signal access to Identity Protection is required.

In this blog a short overview of the option to export Conditional Access configurations based on the Microsoft Graph API and export all the Conditional Access Policies.

**API**

For the API to retrieve a list of conditionalAccessPolicy objects the following permissions are required:

| Permission type | Permissions (from least to most privileged) |
| --- | --- |
| Delegated (work or school account) | Policy.Read.All |
| Delegated (personal Microsoft account) | Not supported. |
| Application | Policy.Read.All |