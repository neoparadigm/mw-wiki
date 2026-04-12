---
conflicts:
- '[CONFLICT: Daniel Chronlund suggests that MFA should be implemented but only for
  non-break glass accounts]'
- '[CONFLICT: Daniel Chronlund suggests that Multi-Factor Authentication (MFA) should
  be implemented but only for non-break glass accounts.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2019-04-08'
  title: Break Glass Account Best Practices in Azure AD
  url: https://danielchronlund.com/2019/04/08/break-glass-account-best-practices-in-azure-ad
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2019-09-30'
  title: An Azure AD Break Glass Routine Template for your Organization
  url: https://danielchronlund.com/2019/09/30/an-azure-ad-break-glass-routine-template-for-your-organization
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-10-06'
  title: Easy Bulk Management of Entra ID Conditional Access Policies
  url: https://danielchronlund.com/2023/10/06/easy-bulk-management-of-entra-id-conditional-access-policies
stale_after: '2026-07-11'
title: Break Glass Emergency Access Accounts
topic: identity/pim/break-glass-accounts
---

# Break Glass Emergency Access Accounts

## Overview
Break Glass Emergency Access Accounts are highly privileged accounts used in Azure Active Directory (Azure AD) to provide emergency access when normal admin accounts cannot be used due to various reasons such as lockouts or service outages. Proper implementation and management of these accounts are crucial for an organization's disaster recovery plan.

[New] The article "An Azure AD Break Glass Routine Template for your Organization" by Daniel Chronlund provides a template for a break glass routine, emphasizing the importance of having such a plan in place before implementing security features like Conditional Access and MFA. [CONFLICT: Daniel Chronlund suggests that Multi-Factor Authentication (MFA) should be implemented but only for non-break glass accounts.]

## Key Concepts
- Complex, hard-to-guess username and password
- Allowed admins list
- Global Administrator role assignment
- Password never expires
- MFA not configured ([CONFLICT: Daniel Chronlund suggests that MFA should be implemented but only for non-break glass accounts])
- Exclusion from Conditional Access policies
- Cloud-only account
- Use of tenants `*.onmicrosoft.com` domain
- No federation or synchronization with on-prem AD
- No connection with employee-supplied mobile phones or hardware tokens
- Documentation and validation
- Regular practice of the emergency routine ([New] Daniel Chronlund emphasizes the importance of practicing the break glass routine every 90 days)

## Configuration
1. Create a complex username and password, split into two parts, stored in secure locations.
2. Assign the Global Administrator role permanently to the account.
3. Set the password to never expire.
4. Configure the account to not have MFA ([CONFLICT: Daniel Chronlund suggests that MFA should be implemented but only for non-break glass accounts])
5. Exclude the account from all Conditional Access policies.
6. Ensure the account is a cloud-only account and uses the tenants `*.onmicrosoft.com` domain.
7. Do not federate or synchronize the account with on-prem AD.
8. Do not connect the account with any employee-supplied mobile phones or hardware tokens.
9. Document the emergency routine and verify and practice it every 90 days ([New] Emphasized by Daniel Chronlund)

## Common Pitfalls
- Weak username or password security
- Incorrect configuration of MFA or Conditional Access policies ([CONFLICT: Daniel Chronlund suggests that MFA should be implemented but only for non-break glass accounts])
- Lack of documentation and validation
- Exposure to unauthorized individuals

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to Break Glass Emergency Access Accounts.]

## Related Topics
- [Break Glass](break-glass)
- [Emergency access](emergency-access)
- [Excluded from CA](excluded-from-ca)
- [Offline credentials](offline-credentials)
- [Recovery account](recovery-account)

New source article: "Easy Bulk Management of Entra ID Conditional Access Policies"
Author: Daniel Chronlund
New source content:
# Easy Bulk Management of Entra ID Conditional Access Policies

Easy Bulk Management of Entra ID Conditional Access Policies – Daniel Chronlund Cloud Security Blog

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

[Cloud](https://danielchronlund.com/category/cloud/), [Conditional Access](https://danielchronlund.com/category/conditional-access/), [Entra ID](https://danielchronlund.com/category/entra-id/), [Microsoft](https://danielchronlund.com/category/microsoft/), [PowerShell](https://danielchronlund.com/category/powershell/), [Security](https://danielchronlund.com/category/security/)

October 6, 2023October 6, 2023
3 Minutes