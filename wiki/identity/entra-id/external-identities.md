---
conflict_topics:
- identity/entra-id/graph-api-permissions
- identity/entra-id/entra-id-protection
conflicts:
- '[CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue,
  while the existing entry does not mention it.]'
- '[CONFLICT: Michael Morten Sonne says X, existing entry says Y]'
- '[CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue,
  while the existing entry does not mention it. Michael Morten Sonne''s blog post
  confirms this feature.]'
- '[CONFLICT: Thomas Naunheim suggests the need for investigation into missing sign-in
  (failure) events and enforcement of Conditional Access and risk-based policies for
  invited users, while the existing entry mentions it as a solution.]'
context_note: External Identities is part of the identity domain. Synthesised from
  6 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- identity/hybrid/entra-connect-hardening
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2021-11-18'
  title: Scary Azure AD Tenant Enumeration&#8230; Using Regular B2B Guest Accounts
  url: https://danielchronlund.com/2021/11/18/scary-azure-ad-tenant-enumeration-using-regular-b2b-guest-accounts
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-01-19'
  title: Enable automatic Access Reviews for Guest users in Teams and Microsoft 365
    Groups
  url: https://jeffreyappel.nl/enable-automatic-access-reviews-for-guest-users
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-12-06'
  title: Global Secure Access – Guest Access support with the Windows Client (B2B
    Guest) – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/global-secure-access-guest-access-support-with-the-windows-clientb2b-guest
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: ''
  title: Azure AD/Entra ID
  url: https://blog.sonnes.cloud/topics/azure-ad-entra-id
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: ''
  title: Identity
  url: https://blog.sonnes.cloud/topics/identity
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2020-07-16'
  title: 'Azure AD B2B: Security considerations to protect external (privileged) identities'
  url: https://www.cloud-architekt.net/azuread-b2b-security-considerations
stale_after: '2026-06-17'
title: External Identities and B2B Collaboration
topic: identity/entra-id/external-identities
---

# External Identities and B2B Collaboration

## External Identities and B2B Collaboration

This topic discusses the security risks associated with Azure AD's default guest permissions in a hybrid work environment using Microsoft Teams and Azure AD B2B guest access. It also introduces new features for enabling automatic Access Reviews for Guest users in Teams and Microsoft 365 Groups, as well as Global Secure Access (GSA) support for Guest Access on Windows clients.

## Key Concepts
- Default guest permissions in Azure AD
- Guest user access restrictions
- PowerShell connectivity to Azure AD tenants by guests
- User enumeration, group memberships, and potential GDPR issues
- `Get-DCAzureADUsersAndGroupsAsGuest` script for enumerating users and security groups/teams as a guest user
- Automatic Access Reviews for Guest users in Teams and Microsoft 365 Groups [CONFLICT: Thomas Naunheim suggests the need for investigation into missing sign-in (failure) events and enforcement of Conditional Access and risk-based policies for invited users, while the existing entry mentions it as a solution.]
- External user access with Global Secure Access (GSA)
- New addition: Blog posts by Michael Morten Sonne on Azure AD/Entra ID, including topics like Global Secure Access – Guest Access support with the Windows Client (B2B Guest), and Global Secure Access – Intelligent Local Access for Private Access.
- [Security considerations to protect external (privileged) identities](https://jeffreya.blogspot.com/2020/07/azure-ad-b2b-security-considerations-to.html) by Thomas Naunheim, discussing identity security in Azure AD B2B scenarios, including known but also undocumented limitations or concerns of identity protection in Azure AD B2B.

## Configuration
The article does not provide specific configuration guidance for Azure AD. It is recommended to assess and potentially fix the default guest security configuration in Azure AD, especially if guests are allowed to connect to an Azure AD tenant with PowerShell. Enabling automatic Access Reviews for Guest users in Teams and Microsoft 365 Groups requires Azure AD Premium P2 license. For Global Secure Access (GSA), prerequisites include licensing and enabling B2B Guest Access with GSA.

## Common Pitfalls
- Not securing guest access properly can lead to unauthorized enumeration of users, groups, and teams within a tenant, which could potentially be a GDPR issue. [CONFLICT: Thomas Naunheim suggests the need for investigation into missing sign-in (failure) events and enforcement of Conditional Access and risk-based policies for invited users, while the existing entry mentions it as a solution.]
- Insufficient security configurations in Global Secure Access (GSA) may lead to SSO/tenant change bugs and Entra ID UI bugs.

## KQL / PowerShell
The article includes a `Get-DCAzureADUsersAndGroupsAsGuest` script for enumerating users and security groups/teams as a guest user. This script is available in DCToolbox version 1.0.24 and later. Additionally, Jeffrey's blog post mentions the use of Azure AD Access reviews for checking guest users in Teams and Microsoft 365 Groups. Global Secure Access (GSA) allows secure access for guests, partners, and contractors to corporate resources.

## Related Topics
- external identity
- B2B collaboration
- guest access
- cross-tenant
- external user
- automatic access reviews
- Global Secure Access (GSA)
- Azure AD/Entra ID
- Security considerations to protect external (privileged) identities [New addition]