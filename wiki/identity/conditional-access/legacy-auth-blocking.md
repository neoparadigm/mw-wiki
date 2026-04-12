---
conflicts:
- '[CONFLICT: Daniel Chronlund''s entry provides additional deployment methods and
  automation tools, while the existing entry does not.]'
- '[CONFLICT: Daniel Chronlund''s entry provides additional information about the
  importance of understanding the Conditional Access policy evaluation process and
  how to find and exploit flaws in a policy design, while the existing entry does
  not.]'
- '[CONFLICT: Jeffrey says to block legacy auth immediately, existing entry suggests
  enabling Conditional Access to block it]'
- '[CONFLICT: Jeffrey suggests implementing MFA as a way to protect against password
  threats, existing entry does not mention this]'
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
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-03-15'
  title: Block Legacy Authentication now, and don&#039;t wait for Microsoft
  url: https://jeffreyappel.nl/block-legacy-authentication-now-and-dont-wait-for-microsoft
stale_after: '2026-06-11'
title: Blocking Legacy Authentication Protocols
topic: identity/conditional-access/legacy-auth-blocking
---

Blocking Legacy Authentication Protocols
=========================================

This topic discusses the importance of blocking legacy authentication in Azure Active Directory (Azure AD) to prevent password spray attacks using PowerShell. These attacks can bypass Multi-Factor Authentication (MFA) if legacy authentication is allowed, potentially compromising an organization's security.

## Key Concepts
- Legacy authentication vs Modern authentication
- Office 365 reporting API
- Basic authentication
- Password spray attack
- Smart Lockout in Azure AD
- [Attacker's Guide to Azure AD Conditional Access](https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access/) (New)
- Block Legacy Authentication now, and don't wait for Microsoft (New from Jeffrey) [CONFLICT: Jeffrey says to block legacy auth immediately, existing entry suggests enabling Conditional Access to block it]

## Configuration
1. Enable Conditional Access to protect your organization from password spray attacks by blocking legacy authentication. (New information from "The Attackers Guide to Azure AD Conditional Access" and "Block Legacy Authentication now, and don't wait for Microsoft")
2. Review and adjust the Conditional Access policies to ensure they are appropriate for your organization's needs, understanding that everything is allowed by default in Azure AD and it's important to focus on what should be blocked rather than what use cases to allow. (New information from "The Attackers Guide to Azure AD Conditional Access")
3. Implement Multi-Factor Authentication (MFA) to add an additional layer of security. [CONFLICT: Jeffrey suggests implementing MFA as a way to protect against password threats, existing entry does not mention this]
4. Disable legacy authentication as soon as possible and switch users to the latest modern authentication protocol. (New from "Block Legacy Authentication now, and don't wait for Microsoft")

## Common Pitfalls
- Failing to enable Conditional Access, leaving the organization vulnerable to password spray attacks.
- Allowing too many password attempts in a short period, potentially triggering Smart Lockout and locking out users unnecessarily.
- Designing Conditional Access policies backwards, focusing on what use cases to allow rather than what should be blocked, which can leave the tenant vulnerable to attacks. (New information from "The Attackers Guide to Azure AD Conditional Access")
- Failing to disable legacy authentication in a timely manner, leaving the organization vulnerable to password threats. (New from "Block Legacy Authentication now, and don't wait for Microsoft")

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
- Block Legacy Authentication now, and don't wait for Microsoft (New)

## Additional Information (from "Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support")
- The Entra ID Conditional Access Policy Design Baseline is updated at least twice every year, always containing lessons learned from the field. It is based on recommendations of how Conditional Access should be deployed to create a strong zero trust security posture.
- There are two methods of deployment: Manual Deployment and Automatic Deployment. The automatic deployment method uses the [Conditional Access Gallery](https://danielchronlund.com/2024/11/21/conditional-access-gallery-point-select-and-deploy-in-minutes/) for easy and efficient policy creation.
- For details on Conditional Access policies, refer to the [Attacker's Guide to Azure AD Conditional Access](https://danielchronlund.com/2022/01/07/the-attackers-guide-to-azure-ad-conditional-access/) and "Block Legacy Authentication now, and don't wait for Microsoft".

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Block Legacy Authentication now, and don’t wait for Microsoft

[Modern Workplace](https://jeffreyappel.nl/category/modern-workplace/), [Security](https://jeffreyappel.nl/category/security/)

# Block Legacy Authentication now, and don’t wait for Microsoft

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[March 15, 2021](https://jeffreyappel.nl/block-legacy-authentication-now-and-dont-wait-for-microsoft/)
0


6 min read

**Legacy authentication is the most compromising sign-in.  Microsoft is going to disable basic/ legacy authentication. It is recommended to implement Legacy Authentication as soon as possible and switch users to the latest modern authentication protocol. In this blog post, we take a look at legacy authentication and how to block it on your tenant.**

Since 2019 Microsoft announced that Microsoft will be turning off legacy authentication. Microsoft announced the following information during the current pandemic:

> We previously [announced](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-and-exchange-online-july-update/ba-p/1530163) we would begin to disable Basic Auth for five Exchange Online protocols in the second half of 2021. Due to the pandemic and the effect it has on priorities and work patterns, we are announcing some important changes to our plan to disable Basic Auth in Exchange Online.

It is a good point to disable legacy authentication and track the usage and don’t wait for Microsoft. Single-factor authentication is not enough these days to remain secure. One of the easiest things that can be done to protect against password threats is implementing multi-factor authentication (MFA).

## What is legacy auth?

The usual meaning for legacy auth in the context of Microsoft cloud services includes all those older protocols one could use to access email and other services, such as Basic Authentication. These protocols are less secure than modern authentication methods and can be easily exploited by attackers.

## Why is it important to block legacy auth?

Legacy authentication is a common target for cyber attacks due to its vulnerability. Attackers can use password spraying, brute force attacks, or other techniques to gain unauthorized access to an organization's resources. By blocking legacy authentication, organizations can significantly reduce the risk of these types of attacks.

## How to block legacy auth in Azure AD?

To block legacy authentication in Azure Active Directory (Azure AD), you can use Conditional Access policies. These policies allow you to control access to your organization's resources based on various conditions, such as the sign-in location, device platform, and application. To block legacy authentication specifically, you can create a policy that requires modern authentication for all users or specific groups of users.

Here are the steps to create a Conditional Access policy in Azure AD:

1. Go to the Azure portal (<https://portal.azure.com/>) and sign in with your administrator account.
2. Search for "Conditional Access" in the search bar and select it from the results.
3. Click on "New policy" to create a new policy.
4. Give your policy a name and description, then select the users or groups that the policy will apply to.
5. Under "Cloud apps or actions", select "Select apps" and choose the applications for which you want to block legacy authentication.
6. Under "Conditions", select "Client app" and choose "Any client application".
7. Under "Access controls", select "Grant" and choose "Block access".
8. Click on "Create" to save your policy.

After creating the policy, Azure AD will enforce it for the selected users or groups, requiring modern authentication for the specified applications. You can also adjust the policy settings as needed to meet your organization's specific requirements.

## Conclusion

Blocking legacy authentication is an important step in securing your organization's resources against cyber attacks. By implementing Conditional Access policies in Azure Active Directory, you can easily block