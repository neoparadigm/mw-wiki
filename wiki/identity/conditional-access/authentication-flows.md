---
conflict_topics:
- identity/conditional-access/device-code-flow-blocking
- identity/conditional-access/aitm-defence
conflicts:
- '[CONFLICT: Daniel Chronlund says Conditions and Access Controls are distinct, existing
  entry does not make this distinction]'
- '[CONFLICT: Daniel Chronlund says X, existing entry does not make this distinction]'
context_note: Authentication Flows is part of the identity domain. Synthesised from
  6 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2018-11-21'
  title: Azure AD Conditional Access Policy Design Baseline
  url: https://danielchronlund.com/2018/11/21/azure-ad-conditional-access-policy-design-baseline
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2018-11-23'
  title: How Multiple Conditional Access Policies Are Applied
  url: https://danielchronlund.com/2018/11/23/how-multiple-conditional-access-policies-are-applied
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2018-12-12'
  title: Conditional Access Logs in Azure AD
  url: https://danielchronlund.com/2018/12/12/conditional-access-logs-in-azure-ad
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2020-10-20'
  title: Export your Conditional Access Policy Assignments to Excel
  url: https://danielchronlund.com/2020/10/20/export-your-conditional-access-policy-assignments-to-excel
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2020-11-26'
  title: Entra ID Conditional Access Policy Design Baseline with Automatic Deployment
    Support
  url: https://danielchronlund.com/2020/11/26/azure-ad-conditional-access-policy-design-baseline-with-automatic-deployment-support
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2021-09-21'
  title: Conditional Access Ring Based Deployment with DCToolbox
  url: https://danielchronlund.com/2021/09/21/conditional-access-ring-based-deployment-with-dctoolbox
stale_after: '2026-06-17'
title: Conditional Access — Authentication Flows
topic: identity/conditional-access/authentication-flows
---

# Conditional Access — Authentication Flows

## Conditional Access — Authentication Flows

### Overview
This topic discusses the various authentication flows available in Azure AD Conditional Access (CA), explaining their purpose and when to use them for secure access to cloud applications. [New: How Multiple Conditional Access Policies Are Applied](#how-multiple-conditional-access-policies-are-applied)

### Key Concepts
- Modern Authentication
- Multi-Factor Authentication (MFA)
- Passwordless Authentication
- Device Registration
- Device Trust
- Just-In-Time Registration
- Seamless SSO
- Work Accounts
- [CONFLICT: Daniel Chronlund says Conditions and Access Controls are distinct, existing entry does not make this distinction]

### Configuration
1. Navigate to Azure Active Directory > Security > Conditional Access > New Policy
2. Select the applicable cloud app and users or groups
3. Under "Access controls", choose the desired authentication flow (e.g., Modern Authentication, MFA, Passwordless)
4. Configure additional conditions as needed (device platform, location, client app, etc.)
5. Set session control options (sign-in frequency, persistent browser sessions)
6. Review policy settings and assign the policy
7. [New: Understanding Conditions vs Access Controls](#conditions-vs-access-controls)
8. [New: Troubleshooting CA issues using Azure AD Sign-In logs (Daniel Chronlund)](#troubleshooting-ca-issues-using-azure-ad-sign-in-logs)
9. [New: Export your Conditional Access Policy Assignments to Excel (Daniel Chronlund)](#export-your-conditional-access-policy-assignments-to-excel)
10. [New: Entra ID Conditional Access Policy Design Baseline with Automatic Deployment Support](#entra-id-conditional-access-policy-design-baseline-with-automatic-deployment-support)
11. [New: Conditional Access Ring Based Deployment with DCToolbox (Daniel Chronlund)](#conditional-access-ring-based-deployment-with-dctoolbox)

### Common Pitfalls
- Misconfiguring authentication flows can lead to user frustration or security vulnerabilities
- Failing to test policies thoroughly before deployment
- Neglecting to exclude Global Admin accounts from CA policies
- [New: Misunderstanding the order of policy application and potential conflicts between multiple policies](#in-what-order-are-conditional-access-policies-applied)

### How Multiple Conditional Access Policies Are Applied
[New content]
CA policies aren't applied in any particular order. All matching policies apply and the resulting access controls required by the policies will be merged! If both grant and block policies match, block will always win. No exceptions!

When multiple policies match and they have different Access Controls like Require MFA, Require Compliant Device or Require Azure AD Joined, the requirements will actually be merged and all the access controls from all matching policies have to be fulfilled. The same is true for Session Controls from different policies.

### Conditional Access Ring Based Deployment with DCToolbox (Daniel Chronlund)
[New content]
It’s time to take our Conditional Access management skills to the next level! A ring based deployment model makes it easy to test policy changes in a small scale at first, and then successively roll it out throughout the organisation. We can detect issues early on without affecting all users, and we can increase our deployment speed and improve test effectiveness.

I recently read a great whitepaper by [Claus Jespersen](https://twitter.com/claus_jespersen), called [Microsoft Azure AD Conditional Access principles and guidance](https://www.linkedin.com/feed/update/urn:li:activity:6843561417782689795/). I highly recommend you to check out his work! Claus, among many other things, talks about how you can ring manage Conditional Access policies and this got me thinking. My conditional access export/import tools have been included in [DCToolbox](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/) for some time now and I thought to myself that it should be possible to use them as part of a ring deployment model. The only thing I actually needed to add was a prefix filter parameter so that it would be possible to distinguish different ring policy sets from each other through prefixes. I’ve included this change in version **1.0.22** and this article is a proof on concept of what you can do with it.

I give you ‘Conditional Access Ring Based Deployment with DCToolbox’. Enjoy!

*Note: I highly recommend that you also read my previous articles on [DCToolbox](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/) and [Conditional Access automation](https://danielchronlund.com/2020/11/25/how-to-manage-conditional-access-as-code-the-ultimate-guide/) before trying this.*

## Our Goal

By creating multiple copies, called rings, of the same Conditional Access policy design, and by using Azure AD groups to deploy them to different sets of users, we can accomplish a ring based deployment model in Conditional Access.

In my example I will use three rings but you could build a solution with as many as you would need.

**RING1** is for test/IT users who can test, understand and troubleshoot the policy change. **RING2** is for a subset of the organisations users, like managers or high-risk employees, to test the policy before rolling it out to the entire organisation. **RING3** is for the rest of the organisation.

Each ring will have the same Conditional Access policies but with different settings, such as different access controls, session control options, and conditions. This way, we can test the policies in a controlled manner and gradually roll them out to more users as we gain confidence in their effectiveness and stability.

New source article: "Conditional Access Ring Based Deployment with DCToolbox"
Author: Daniel Chronlund
New source content:
... (the rest of the article is already included in the updated wiki entry)