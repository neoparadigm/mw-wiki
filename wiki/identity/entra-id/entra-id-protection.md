---
conflict_topics:
- identity/entra-id/admin-consent-workflow
- identity/entra-id/external-identities
conflicts:
- '[CONFLICT: Michael Morten Sonne does not mention Azure AD Identity Protection]'
- '[CONFLICT: Michael Morten Sonne''s new source does not discuss configuration]'
- '[CONFLICT: Jeffrey states that Sign-In Risk Policy requires a separate policy]'
context_note: Entra Id Protection is part of the identity domain. Synthesised from
  5 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-07-12'
  title: 'Azure AD Identity Protection: User Risk and Sign-in Risk protection with
    automation'
  url: https://jeffreyappel.nl/azure-ad-identity-protection-user-risk-and-sign-in-risk-protection-with-automation
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2026-03-24'
  title: Microsoft Defender’s New Password Protection Experience – Blog - Sonne´s
    Cloud
  url: https://blog.sonnes.cloud/microsoft-defenders-new-password-protection-experience
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-05-20'
  title: 'Azure AD Sign-In Risk Policy: Zo werkt deze functionaliteit'
  url: https://jeffreyappel.nl/azure-ad-sign-in-risk-policy-zo-werkt-deze-functionaliteit
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-11-22'
  title: 'Identity Protection Risk Analysis workbook: Get more Azure AD Identity Protection
    insights'
  url: https://jeffreyappel.nl/identity-protection-risk-analysis-workbook-get-more-azure-ad-identity-protection-insights
- author: shlipsey3
  crawled: '2026-04-18'
  date: '2025-05-27'
  title: Microsoft Entra activity log integration options - Microsoft Entra ID
  url: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations
stale_after: '2026-06-17'
title: Entra ID Protection Risk Policies
topic: identity/entra-id/entra-id-protection
---

# Entra ID Protection Risk Policies

## Azure AD Identity Protection: User Risk and Sign-in Risk protection with automation

### Overview
Azure AD Identity Protection is a security tool available in the Microsoft E5 license that allows organizations to protect users based on Microsoft signals. The blog post provides an overview of Azure AD Identity Protection, its components, and how it works. [CONFLICT: Michael Morten Sonne does not mention Azure AD Identity Protection]

### Key Concepts
- Azure AD Identity Protection
- User Risk
- Sign-in Risk
- Leaked credentials
- Azure AD threat intelligence
- Anonymous IP address
- Atypical travel
- Malware linked IP address
- Unfamiliar sign-in properties
- Password spray

### Configuration
The blog post does not provide specific configuration guidance. However, it mentions that an Azure AD Premium P2 license is necessary for all the Identity Protection features and that multiple policies should be enabled to use the full capabilities of Identity Protection. [CONFLICT: Jeffrey states that Sign-In Risk Policy requires a separate policy]

### Common Pitfalls
Not mentioned in the article.

### KQL / PowerShell
Not applicable as the article does not provide any queries or scripts.

### Azure AD Sign-In Risk Policy
Azure AD Sign-In Risk Policy is a feature of Azure AD Identity Protection that helps organizations protect against risky sign-ins by automatically enforcing multi-factor authentication (MFA) or blocking users based on risk levels. [New information]

### Azure AD Identity Protection Risk Analysis Workbook
The new Identity Protection Risk Analysis workbook provides more in-depth insights based on Azure AD Identity Protection data. It is useful for organizations seeking additional insights beyond the standard Azure AD Identity Protection dashboard. [New information from Jeffrey's blog post]

### Microsoft Entra activity log integration options - Microsoft Entra ID
With these integrations, you can enable rich visualizations, monitoring, and alerting on the connected data. This article describes the recommended uses for each integration type or access method. Cost considerations for sending Microsoft Entra activity logs to various endpoints are also covered. [New information from shlipsey3's article]

#### Supported reports
- The audit logs gives you access to the history of every task performed in your tenant.
- With the sign-in logs, you can see when users attempt to sign in to your applications or troubleshoot sign-in errors.
- With the provisioning logs, you can monitor which users were, updated, and deleted in all your non-Microsoft applications.
- The risky users report helps you monitor changes in user risk level and remediation activity.
- With the risk detections report, you can monitor user's risk detections and analyze trends in risk activity detected in your organization.

## Related Topics
- ID protection
- User risk
- Sign-in risk
- Risk policy
- Leaked credentials
- Azure AD Identity Protection
- Azure AD Identity Protection Risk Analysis Workbook
- Microsoft Entra activity log integration options - Microsoft Entra ID