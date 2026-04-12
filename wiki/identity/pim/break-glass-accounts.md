---
conflicts:
- '[CONFLICT: Daniel Chronlund suggests that MFA should be used]'
- '[CONFLICT: The existing entry does not mention Conditional Access policies.]'
- '[CONFLICT: Daniel Chronlund''s blog post introduces the use of Conditional Access
  policies to require admin access only from specific, managed devices.]'
- '[CONFLICT: The existing entry does not mention Conditional Access policies]'
- '[CONFLICT: The existing entry does not mention this risk]'
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
  date: '2021-11-02'
  title: Require Privileged Workstation for Admin Access with Conditional Access
  url: https://danielchronlund.com/2021/11/02/require-privileged-workstation-for-admin-access-with-conditional-access
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-11-18'
  title: Scary Azure AD Tenant Enumeration&#8230; Using Regular B2B Guest Accounts
  url: https://danielchronlund.com/2021/11/18/scary-azure-ad-tenant-enumeration-using-regular-b2b-guest-accounts
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
Break Glass Emergency Access Accounts are highly privileged accounts used in Azure Active Directory (Azure AD) to provide emergency access when normal admin accounts cannot be used due to various reasons such as lockouts or service outages. These accounts should be kept secret and only known by a limited number of approved admins.

- An Azure AD Break Glass Routine Template for your Organization (Daniel Chronlund, September 30, 2019) suggests that every organization should have a break glass routine in place for their Azure AD and Office 365 tenant.
- "Require Privileged Workstation for Admin Access with Conditional Access" by Daniel Chronlund (November 2, 2021) introduces the concept of using Conditional Access policies to require admin access only from specific, managed devices [CONFLICT: The existing entry does not mention Conditional Access policies].
- "Scary Azure AD Tenant Enumeration... Using Regular B2B Guest Accounts" by Daniel Chronlund (November 18, 2021) highlights a potential security risk with default guest access settings in Azure AD, allowing guests to enumerate users, groups, and teams [CONFLICT: The existing entry does not mention this risk].
- "Easy Bulk Management of Entra ID Conditional Access Policies" by Daniel Chronlund (October 6, 2023) introduces a PowerShell module for automating bulk management tasks in Conditional Access policies [NEW CONTENT].

## Key Concepts
- Complex, hard-to-guess username
- Complex password stored in secure locations
- List of allowed admins who can use the break glass accounts
- Monitoring break glass accounts in Azure AD sign-in logs and audit logs
- Global Administrator role assigned permanently
- Password never expires [CONFLICT: Daniel Chronlund suggests that MFA should be used]
- Excluded from all Conditional Access policies [CONFLICT: Daniel Chronlund's blog post introduces the use of Conditional Access policies to require admin access only from specific, managed devices.]
- Cloud-only account using the tenants `*.onmicrosoft.com` domain
- Not federated or synchronized with on-prem AD
- Not connected with employee-supplied mobile phones or hardware tokens
- Documentation and validation of emergency routine [New Content: Regular practice of the break glass routine]
- Requiring admin access only from specific, managed devices (Daniel Chronlund's blog post)
- Potential security risk of enumerating users, groups, and teams with default guest permissions (Daniel Chronlund's blog post)
- Bulk management of Conditional Access policies using PowerShell (Daniel Chronlund's new blog post)

## Configuration
1. Create a complex username and store it securely.
2. Generate a complex password and split it into two parts, storing each part in separate fireproof safes at different locations.
3. Assign the Global Administrator role permanently to the break glass account.
4. Set the password to never expire [CONFLICT: Daniel Chronlund suggests that MFA should be used]
5. Configure the account to use MFA (Daniel Chronlund's suggestion)
6. Exclude the account from all Conditional Access policies [CONFLICT: Daniel Chronlund's blog post introduces the use of Conditional Access policies to require admin access only from specific, managed devices.]
7. Ensure the account is not federated or synchronized with on-prem AD
8. Not connected with employee-supplied mobile phones or hardware tokens
9. Documentation and validation of emergency routine [New Content: Regular practice of the break glass routine]
10. Requiring admin access only from specific, managed devices (Daniel Chronlund's blog post)
11. Potential security risk of enumerating users, groups, and teams with default guest permissions (Daniel Chronlund's blog post)
12. Bulk management of Conditional Access policies using PowerShell (Daniel Chronlund's new blog post)