---
conflicts:
- '[CONFLICT: Daniel Chronlund suggests that MFA should be configured for Break Glass
  Accounts]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2019-04-08'
  title: Break Glass Account Best Practices in Azure AD
  url: https://danielchronlund.com/2019/04/08/break-glass-account-best-practices-in-azure-ad
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2019-09-30'
  title: An Azure AD Break Glass Routine Template for your Organization
  url: https://danielchronlund.com/2019/09/30/an-azure-ad-break-glass-routine-template-for-your-organization
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2020-01-22'
  title: Monitor your Azure AD Break Glass Accounts with Azure Monitor
  url: https://danielchronlund.com/2020/01/22/monitor-your-azure-ad-break-glass-accounts-with-azure-monitor
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2021-06-14'
  title: Monitor Azure AD break-glass accounts with Microsoft Sentinel
  url: https://jeffreyappel.nl/monitor-azure-ad-break-glass-accounts-with-azure-sentinel
stale_after: '2026-07-13'
title: Break Glass Emergency Access Accounts
topic: identity/pim/break-glass-accounts
---

# Break Glass Emergency Access Accounts

## Overview
Break Glass Emergency Access Accounts are highly privileged accounts used in Azure Active Directory (Azure AD) to provide emergency access when normal admin accounts cannot be used due to various reasons such as lockouts or service outages. Proper implementation and management of these accounts are crucial for an organization's disaster recovery plan.

[New] The article "An Azure AD Break Glass Routine Template for your Organization" by Daniel Chronlund emphasizes the importance of having a break glass routine in place for Azure AD and Office 365 tenants, especially before implementing security features like MFA and Conditional Access policies. [CONFLICT: Daniel Chronlund suggests that MFA should be configured for Break Glass Accounts]

## Key Concepts
- Complex, hard-to-guess username and password
- Allowed admins who can use the break glass accounts
- Exclusion from all Conditional Access (CA) policies [CONFLICT: Daniel Chronlund suggests that MFA should be configured for Break Glass Accounts]
- Cloud-only account using the tenants `*.onmicrosoft.com` domain
- No synchronization with on-prem AD or connection to employee-supplied devices
- Regular documentation, validation, and practice of emergency routines
- [New] MFA configuration for Break Glass Accounts (according to Daniel Chronlund)
- [New] Monitoring break glass accounts using Azure Monitor (according to Daniel Chronlund)
- [New] Monitoring break glass accounts with Microsoft Sentinel (according to Jeffrey)

## Configuration
1. Create a username that is hard to guess.
2. Assign the Global Administrator role permanently.
3. Set the password to never expire.
4. Disable MFA for the account [CONFLICT: Daniel Chronlund suggests that MFA should be configured for Break Glass Accounts]
5. Exclude the account from all CA policies
6. Ensure the account is a cloud-only account using the tenants `*.onmicrosoft.com` domain.
7. Do not federate the account.
8. Avoid synchronization with on-prem AD and connection to employee-supplied devices.
9. Document, validate, and practice emergency routines regularly.
10. [New] Configure MFA for Break Glass Accounts (according to Daniel Chronlund)
11. [New] Monitor Azure AD Break Glass Accounts with Azure Monitor (according to Daniel Chronlund)
12. [New] Monitor Azure AD break-glass accounts with Microsoft Sentinel (according to Jeffrey)

## Common Pitfalls
- Weak or easily guessable usernames and passwords
- Incorrect configuration of MFA or CA policies [New: MFA misconfiguration is now a pitfall]
- Lack of documentation and regular validation of emergency routines
- Failure to keep break glass accounts secret and secure
- [New] Insufficient monitoring of break glass account usage (according to Jeffrey)

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to Break Glass Emergency Access Accounts.]

## Related Topics
- [Break Glass](break-glass)
- [Emergency access](emergency-access)
- [Excluded from CA](excluded-from-ca)
- [Offline credentials](offline-credentials)
- [Recovery account](recovery-account)
- [Monitor Azure AD Break Glass Accounts with Azure Monitor](monitor-azure-ad-break-glass-accounts-with-azure-monitor)
- [Monitor Azure AD break-glass accounts with Microsoft Sentinel](monitor-azure-ad-break-glass-accounts-with-microsoft-sentinel)