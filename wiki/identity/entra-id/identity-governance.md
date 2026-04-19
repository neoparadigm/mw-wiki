---
conflict_topics:
- identity/entra-id/passwordless-authentication
- identity/entra-id/graph-api-permissions
conflicts:
- '[CONFLICT: Thomas Naunheim suggests that Conditional Access and Entitlement Management
  are essential for applying Zero Trust principles to Privileged Identity and Access.
  The existing entry does not mention this.]'
- '[CONFLICT: Thomas Naunheim also mentions the importance of Conditional Access Policies
  for securing access to privileged interfaces.]'
- '[CONFLICT: Thomas Naunheim also suggests implementing Conditional Access Policies
  to secure access to privileged interfaces.]'
context_note: Identity Governance is part of the identity domain. Synthesised from
  2 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2022-11-15'
  title: Automated Lifecycle Workflows for Privileged Identities with Azure AD Identity
    Governance
  url: https://www.cloud-architekt.net/manage-privileged-identities-with-azuread-identity-governance
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2022-12-20'
  title: Securing privileged user access with Azure AD Conditional Access and Identity
    Governance
  url: https://www.cloud-architekt.net/securing-privileged-access-conditionalaccess-governance
stale_after: '2026-06-17'
title: Identity Governance and Access Reviews
topic: identity/entra-id/identity-governance
---

# Identity Governance and Access Reviews

## Overview
Automated Lifecycle Workflows for Privileged Identities with Azure AD Identity Governance is a feature that automates onboarding and offboarding tasks for privileged accounts in Azure Active Directory (Azure AD). This approach enhances security by isolating privileged accounts from work accounts, enforcing strong access policies, and reducing the risk of identity compromise.

[CONFLICT: Thomas Naunheim suggests that Conditional Access and Entitlement Management are essential for applying Zero Trust principles to Privileged Identity and Access. The existing entry does not mention this.]

## Key Concepts
- Cloud-only and dedicated user accounts for privileged access
- Isolation of privileged accounts in Azure AD to protect against on-premises compromises
- Built-in workflow templates and custom extensions using Logic Apps
- HR-driven user provisioning for supported systems like WorkDay or SAP SuccessFactor
- Separation between work account (for productivity tasks) and privileged accounts (for managing infrastructure or workloads)
- Privileged Admin Workstations (PAW) and Conditional Access Policies [CONFLICT: Thomas Naunheim also mentions the importance of Conditional Access Policies for securing access to privileged interfaces.]
- Enterprise Access Model

## Configuration
1. Create cloud-only accounts for privileged identities, separate from "work accounts"
2. Assign required licenses (Azure AD P2) to privileged accounts
3. Configure built-in workflow templates or integrate custom extensions using Logic Apps
4. Set up HR-driven user provisioning for supported systems like WorkDay or SAP SuccessFactor
5. Implement Conditional Access Policies for Privileged Admin Workstations (PAW) [CONFLICT: Thomas Naunheim also suggests implementing Conditional Access Policies to secure access to privileged interfaces.]

## Common Pitfalls
- Failing to separate work and privileged accounts, leading to increased attack surface and compromised security
- Assigning licenses/access to productive workloads to privileged accounts
- Not enforcing usage of Privileged Admin Workstations (PAW) by Conditional Access Policies

## Provisioning of Privileged Identity [New content from Thomas Naunheim]
In the [previous blog post](https://www.cloud-architekt.net/manage-privileged-identities-with-azuread-identity-governance/), I’ve described how to onboard a new privileged user account by using “Lifecycle Workflows” in Azure Active Directory. As a result of the provisioning process, a dedicated privileged account has been created which the following configurations and properties:

- Cloud-only account without any privileges by default
  - Relation between work/privileged account and scope of access level (Control-/Management Plane) are stored in custom security attributes
  - Privileged user account has no assigned RBAC roles in Azure AD, Azure or any other platform per default (at this time, only unprivileged and [default member user permissions](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/users-default-permissions?WT.mc_id=AZ-MVP-5003945#compare-member-and-guest-default-permissions) are available for this dedicated account)
- Assignment to Administrative Unit (AU) for Privileged Accounts (by using dynamic membership filter)
- Assignment to Group which contains all Privileged Accounts that has been provisioned for the targeted Enterprise Access/Tier level (in this case: dug\_AAD.Tier1.PrivilegedAccounts)
- Optional: Employee owns Verified Credential as employee of company’s IT department
- Employee has received Temporary Access Pass for passwordless onboarding

*Overview of work and privileged account provisioning. In this article, I will describe the implementation that governs the process for privileged access assignments and enforcing access controls in context of privileged access with Conditional Access Policies.*

## Principles of Tiered Administration Model [New content from Thomas Naunheim]
The goal is to provide an approach which supports the principles of Zero Trust, namely "Verify explicitly" and "Use least-privilege access" for Privileged Identity and Access. This model consists of the following components:

1. Tiered Access Model: Defines different levels of access based on the role and responsibilities of the user. Each tier corresponds to a specific set of permissions, applications, and resources.
2. Just-In-Time (JIT) Access: Provides temporary access to users only when it's necessary, reducing the attack surface and minimizing the risk of unauthorized access.
3. Least Privilege Principle: Assigns the minimum set of permissions required for a user to perform their job functions, limiting potential damage in case of a security breach.
4. Conditional Access Policies: Enforces access controls based on various conditions such as device compliance, location, and risk level.
5. Privileged Identity Management (PIM): Allows administrators to elevate their access levels temporarily when needed, ensuring that they have the appropriate permissions only during specific tasks.
6. Multi-Factor Authentication (MFA): Requires users to authenticate using multiple verification methods, adding an extra layer of security to privileged accounts.
7. Privileged Access Workstations (PAW): Provides a secure and isolated environment for administrators to perform their duties, reducing the risk of lateral movement in case of a breach.
8. Monitoring and Auditing: Continuously monitors and logs activities related to privileged accounts, enabling organizations to detect and respond to potential threats promptly.
9. Automated Remediation: Automates the process of revoking access or resetting passwords when suspicious activities are detected, minimizing the impact of a security incident.

## Related Topics
- Identity Governance
- Access Review
- Entitlement Management
- Access Package
- Lifecycle Workflow
- Conditional Access Policies
- Privileged Identity Management (PIM)
- Multi-Factor Authentication (MFA)
- Privileged Admin Workstations (PAW)
- Zero Trust Architecture