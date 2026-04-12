---
conflicts:
- '[CONFLICT: Daniel Chronlund mentions the importance of blocking legacy authentication
  to prevent password spray attacks, while the existing entry does not explicitly
  mention this.]'
- '[CONFLICT: Daniel Chronlund suggests adding a condition for specific client apps
  to block legacy authentication, while the existing entry does not mention this.]'
- '[CONFLICT: Daniel Chronlund specifically mentions this as a vulnerability]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-01-07'
  title: The Attackers Guide to Azure AD Conditional Access
  url: https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-03-17'
  title: Azure AD Password Spray Attacks with PowerShell and How to Defend your Tenant
  url: https://danielchronlund.com/2020/03/17/azure-ad-password-spray-attacks-with-powershell-and-how-to-defend-your-tenant
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-11-26'
  title: Entra ID Conditional Access Policy Design Baseline with Automatic Deployment
    Support
  url: https://danielchronlund.com/2020/11/26/azure-ad-conditional-access-policy-design-baseline-with-automatic-deployment-support
stale_after: '2026-06-11'
title: Blocking Legacy Authentication Protocols
topic: identity/conditional-access/legacy-auth-blocking
---

# Blocking Legacy Authentication Protocols

## Blocking Legacy Authentication Protocols

### Overview
Blocking legacy authentication protocols is crucial for securing Azure AD Conditional Access by preventing unsecure connections and reducing attack surface. [CONFLICT: Daniel Chronlund mentions the importance of blocking legacy authentication to prevent password spray attacks, while the existing entry does not explicitly mention this.] This practice helps mitigate various threats such as man-in-the-middle and brute force attacks.

### Key Concepts
- Legacy authentication protocols: Outdated methods like Basic Auth, SMTP AUTH, POP3, IMAP that are vulnerable to attacks such as man-in-the-middle and brute force attacks.
- Conditional Access policies: Azure AD feature used to control access to resources based on conditions like device compliance, location, client app, and sign-in risk level.
- Secure authentication protocols: Modern methods like OAuth 2.0 and OpenID Connect that provide stronger security through encryption and multi-factor authentication.
- Password Spray Attacks [New addition based on the new source]

### Configuration
1. Navigate to Azure AD > Security > Conditional Access > New policy.
2. Select Users and Cloud apps or actions, then select "Select an app" and choose the target application.
3. Under Conditions, add a condition for Client Apps > Browser > Client App > All clients. [CONFLICT: Daniel Chronlund suggests adding a condition for specific client apps to block legacy authentication, while the existing entry does not mention this.]
4. Under Access controls, under Cloud App or Action restrictions, select Block legacy authentication.
5. Configure other conditions and access controls as needed, then set the policy to On.

### Common Pitfalls
- Failing to block all legacy protocols: Ensure that all vulnerable protocols are blocked to minimize attack surface.
- Not testing policies thoroughly: Test policies in a controlled environment before deploying them to production to avoid unintended disruptions.
- Allowing legacy authentication in Office 365, which bypasses MFA and can be exploited in password spray attacks [CONFLICT: Daniel Chronlund specifically mentions this as a vulnerability].
- Not considering the need for exceptions or specific use cases that may require legacy protocols. [New addition based on the new source]

### KQL / PowerShell
[The article does not provide any relevant queries or scripts for this topic.]

### Related Topics
- Legacy auth
- Basic Auth
- SMTP AUTH
- POP3
- IMAP
- Password Spray Attacks [New addition based on the new source]

## Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support

Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support – Daniel Chronlund Cloud Security Blog

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

[Azure AD](https://danielchronlund.com/category/azure-ad/), [Cloud](https://danielchronlund.com/category/cloud/), [Conditional Access](https://danielchronlund.com/category/conditional-access/), [Microsoft](https://danielchronlund.com/category/microsoft/), [Security](https://danielchronlund.com/category/security/)

November 26, 2020November 26, 2024
14 Minutes

My Entra ID Conditional Access Policy Design Baseline is updated at least twice every year, always containing lessons learned from the field. It is based on my recommendations of how Conditional Access should be deployed to create a strong zero trust security posture.

Note that all organisations are different and you might need to adjust the baseline to fit your specific needs. My goal is to provide inspiration and a great starting point for your own Conditional Access design.

|  |  |
| --- | --- |
| **Current baseline version**: | **1**5 |
| **Release date**: | **2024-11-2**6 |

There are two methods of deployment:

## Option 1: Manual Deployment

Download the Excel version of the baseline and manually create each Conditional Access policy in the Azure portal.

[conditional-access-design-version-15-poc](https://danielchronlund.com/wp-content/uploads/2020/11/conditional-access-design-version-15-poc.xlsx)[Ladda ner](https://danielchronlund.com/wp-content/uploads/2020/11/conditional-access-design-version-15-poc.xlsx)

## Option 2: Automatic Deployment

**Version 7** of this baseline was the first version with [DCToolbox](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/) automation support, and **version 15** was the first to change deployment model to use the [Conditional Access Gallery](https://danielchronlund.com/2024/11/21/conditional-access-gallery-point-select-and-deploy-in-minutes/). This means that you can now automatically deploy this baseline with [DCToolbox](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/) (or create your own JSON templates).

Please see this article for details of Conditional Access automation with **DCToolbox**: [How to Manage Conditional Access as Code – The Ultimate Guide](https://danielchronlund.com/2020/11/25/how-to-manage-conditional-access-as-code-the-ultimate-guide/)

To automatically install the baseline, run this in **PowerShell 7**:

```
# Install DCToolboc from the PowerShell Gallery:
Install-Module -Name DCToolbox -Force

# Deploy the baseline as a complete Conditional Access PoC in report-only mode, add a PILOT prefix, AND create documentation in Markdown format.
Deploy-DCConditionalAccessBaselinePoC 

```