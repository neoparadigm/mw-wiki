---
conflicts:
- '[CONFLICT: Daniel Chronlund''s entry provides additional deployment methods and
  automation tools, while the existing entry does not.]'
- '[CONFLICT: Daniel Chronlund''s entry provides additional information about the
  importance of understanding the Conditional Access policy evaluation process and
  how to find and exploit flaws in a policy design, while the existing entry does
  not.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
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
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-01-07'
  title: The Attackers Guide to Azure AD Conditional Access
  url: https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access
stale_after: '2026-06-11'
title: Blocking Legacy Authentication Protocols
topic: identity/conditional-access/legacy-auth-blocking
---

Blocking Legacy Authentication Protocols
=========================================

This topic discusses the importance of blocking legacy authentication protocols in Azure Active Directory (Azure AD) to prevent password spray attacks using PowerShell. These attacks can bypass Multi-Factor Authentication (MFA) if legacy authentication is allowed, potentially compromising an organization's security.

## Key Concepts
- Legacy authentication vs Modern authentication
- Office 365 reporting API
- Basic authentication
- Password spray attack
- Smart Lockout in Azure AD
- [Attacker's Guide to Azure AD Conditional Access](https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access/) (New)

## Configuration
1. Enable Conditional Access to protect your organization from password spray attacks by blocking legacy authentication.
2. Review and adjust the Conditional Access policies to ensure they are appropriate for your organization's needs, understanding that everything is allowed by default in Azure AD and it's important to focus on what should be blocked rather than what use cases to allow. (New information from "The Attackers Guide to Azure AD Conditional Access")

## Common Pitfalls
- Failing to enable Conditional Access, leaving the organization vulnerable to password spray attacks.
- Allowing too many password attempts in a short period, potentially triggering Smart Lockout and locking out users unnecessarily.
- Designing Conditional Access policies backwards, focusing on what use cases to allow rather than what should be blocked, which can leave the tenant vulnerable to attacks. (New information from "The Attackers Guide to Azure AD Conditional Access")

## KQL / PowerShell
The article includes a PowerShell script for demonstration purposes only. It is not recommended to use this script in a production environment without proper security measures in place.

```powershell
function Invoke-AzureAdPasswordSprayAttack {
    # ... (omitted for brevity)
}
```

## Related Topics
- [Legacy auth](legacy_auth)
- [Basic auth](basic_auth)
- [SMTP AUTH](smtp_auth)
- [POP3](pop3)
- [IMAP](imap)
- [Attacker's Guide to Azure AD Conditional Access](https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access/) (New)

## Additional Information (from "Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support")
- The Entra ID Conditional Access Policy Design Baseline is updated at least twice every year, always containing lessons learned from the field. It is based on recommendations of how Conditional Access should be deployed to create a strong zero trust security posture.
- There are two methods of deployment: Manual Deployment and Automatic Deployment. The automatic deployment method uses the [Conditional Access Gallery](https://danielchronlund.com/2024/11/21/conditional-access-gallery-point-select-and-deploy-in-minutes/) for easy and efficient policy creation.
- For details on Conditional Access automation with DCToolbox, see [How to Manage Conditional Access as Code – The Ultimate Guide](https://danielchronlund.com/2020/11/25/how-to-manage-conditional-access-as-code-the-ultimate-guide/)

[CONFLICT: Daniel Chronlund's entry provides additional information about the importance of understanding the Conditional Access policy evaluation process and how to find and exploit flaws in a policy design, while the existing entry does not.]