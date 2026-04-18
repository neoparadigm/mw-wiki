---
conflict_topics:
- intune/apps/microsoft-store-apps
- identity/hybrid/entra-connect-hardening
conflicts:
- '[CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is
  not configured for Break Glass accounts according to the existing entry]'
- '[CONFLICT: The existing entry does not configure MFA for Break Glass accounts]'
context_note: Break Glass Accounts is part of the identity domain. Synthesised from
  5 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2019-04-08'
  title: Break Glass Account Best Practices in Azure AD
  url: https://danielchronlund.com/2019/04/08/break-glass-account-best-practices-in-azure-ad
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2019-09-30'
  title: An Azure AD Break Glass Routine Template for your Organization
  url: https://danielchronlund.com/2019/09/30/an-azure-ad-break-glass-routine-template-for-your-organization
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2020-01-22'
  title: Monitor your Azure AD Break Glass Accounts with Azure Monitor
  url: https://danielchronlund.com/2020/01/22/monitor-your-azure-ad-break-glass-accounts-with-azure-monitor
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2023-01-25'
  title: A Security MVP&#8217;s Take on Cloud Security in 2023
  url: https://danielchronlund.com/2023/01/25/a-security-mvps-take-on-cloud-security-in-2023
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-06-14'
  title: Monitor Azure AD break-glass accounts with Microsoft Sentinel
  url: https://jeffreyappel.nl/monitor-azure-ad-break-glass-accounts-with-azure-sentinel
- author: Julian Stephan
  crawled: '2026-04-18'
  date: '2023-09-28'
  title: 'Heard at TEC: The Current State of Microsoft Identity Security: Common Security
    Issues and Misconfigurations'
  url: https://practical365.com/heard-at-tec-the-current-state-of-microsoft-identity-security-common-security-issues-and-misconfigurations
stale_after: '2026-07-17'
title: Break Glass Emergency Access Accounts
topic: identity/pim/break-glass-accounts
---

# Break Glass Emergency Access Accounts

## Overview
Break Glass Emergency Access Accounts are highly privileged accounts used in Azure Active Directory (Azure AD) to regain access when normal admin accounts cannot sign in due to various disasters such as lockouts, service outages, or failed federation services. These accounts should be kept secret and only known by a select group of admins.

## Key Concepts
- Complex username and password
- Allowed admins list
- Global Administrator role
- Password never expires [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
- MFA configured (according to Daniel Chronlund's suggestions) [CONFLICT: The existing entry does not configure MFA for Break Glass accounts]
- Excluded from Conditional Access policies
- Cloud-only account
- Uses the tenants `*.onmicrosoft.com` domain
- Not federated or synchronized with on-prem AD
- No employee-supplied mobile phones or hardware tokens
- Emergency routine documentation and validation
- Possibly less obvious naming for break glass accounts to avoid attracting attackers (Daniel Chronlund)
- Monitoring Azure AD Break Glass Accounts with Microsoft Sentinel (Jeffrey Appel)
- [New Content] Privileged and service accounts with old passwords should be changed annually (Julian Stephan)
- [New Content] Implement a password filter to reduce non-secure password patterns (Julian Stephan)
- [New Content] Fine-grained password policies allow flexibility to set different password policy settings for different types of accounts (Julian Stephan)
- [New Content] Leverage Group Managed Service Accounts (GMSAs) where possible that automatically rotate passwords within Windows Server for applications (Julian Stephan)
- [New Content] Disable the Print Spooler Service on Domain Controllers (Julian Stephan)

## Configuration
1. Create a complex username and password, split into two parts, stored in secure locations.
2. Assign the Global Administrator role permanently to the account.
3. Set the password to never expire [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
4. Configure MFA for the account [CONFLICT: The existing entry does not configure MFA for Break Glass accounts]
5. Configure the account to not use MFA during sign-in (if needed for emergency access) [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
6. Exclude the account from all Conditional Access policies
7. Ensure the account is a cloud-only account and uses the tenants `*.onmicrosoft.com` domain
8. Do not federate or synchronize the account with on-prem AD
9. Do not connect the account with any employee-supplied mobile phones or hardware tokens
10. Document and validate the emergency routine regularly
11. [New Content] Change privileged and service accounts passwords annually (Julian Stephan)
12. [New Content] Implement a password filter to reduce non-secure password patterns (Julian Stephan)
13. [New Content] Use fine-grained password policies for flexibility in setting different password policy settings for different types of accounts (Julian Stephan)
14. [New Content] Leverage Group Managed Service Accounts (GMSAs) where possible that automatically rotate passwords within Windows Server for applications (Julian Stephan)
15. [New Content] Disable the Print Spooler Service on Domain Controllers (Julian Stephan)