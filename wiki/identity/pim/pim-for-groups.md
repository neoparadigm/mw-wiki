---
conflicts: []
context_note: Pim For Groups is part of the identity domain. It connects closely to
  Avd Security Baseline and Mfa Registration Policy. Synthesised from 2 community
  sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- azure/avd/avd-security-baseline
- identity/entra-id/mfa-registration-policy
sources:
- author: kenwith
  crawled: '2026-04-18'
  date: '2026-03-23'
  title: Privileged Identity Management (PIM) for Groups - Microsoft Entra ID Governance
  url: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2020-08-11'
  title: 'Privileged Access Groups: Manage privileged access outside of Azure AD admin
    roles with Azure PIM'
  url: https://www.cloud-architekt.net/azurepim-pag-rbac
stale_after: '2026-06-17'
title: PIM for Groups Configuration
topic: identity/pim/pim-for-groups
---

# PIM for Groups Configuration and Privileged Access Groups

## Overview
PIM for Groups Configuration allows administrators to manage and configure the Privileged Identity Management (PIM) feature for Microsoft Entra ID Governance, focusing on groups. This configuration is crucial for just-in-time membership and ownership of security and Microsoft 365 groups, which can control access to various scenarios such as Microsoft Entra roles, Azure roles, Azure SQL, Azure Key Vault, Intune, other application roles, and third-party applications.

Privileged Access Groups (PAG) is a new feature introduced by Microsoft that allows managing privileged access outside of Azure AD admin roles in services like Azure DevOps, Intune, or MDATP RBAC. PAG enables just-in-time access to the Owner or Member role of groups, providing enhanced security for owners with delegated administrative tasks.

## Key Concepts
- PIM for Groups policies: Approval requirements, multifactor authentication (MFA), justification, maximum activation time, etc.
- Eligible membership and ownership activation in groups.
- Role-assignable groups and non-role-assignable groups.
- Active owners and eligible owners in a group.
- Privileged Access Groups: Just-in-time access to Owner or Member role of groups with approval workflow, MFA challenge, etc.

## Configuration
1. Create or manage PIM for Groups policies:
   - Navigate to the Microsoft Entra admin center.
   - Go to Azure AD > Privileged Identity Management > Policies.
   - Choose "New policy" and select either "Activation of membership" or "Activation of ownership".
   - Configure the policy settings according to your organization's requirements.
2. Assign policies to groups:
   - Navigate to the Microsoft Entra admin center.
   - Go to Azure AD > Groups.
   - Select a group and go to the "Privileged Identity Management" tab.
   - Choose the desired policy for activation of membership or ownership.
3. Enable eligible membership for groups:
   - Navigate to the Microsoft Entra admin center.
   - Go to Azure AD > Groups.
   - Select a group and go to the "Members" tab.
   - Add users as eligible members.
4. Manage Privileged Access Groups:
   - Navigate to the service where PAG is applicable (Azure DevOps, Intune, etc.).
   - Create or manage Privileged Access Groups and assign eligible members.

## Common Pitfalls
- Failing to require approval for membership or ownership activation, leaving the organization vulnerable to security risks from less-privileged administrators.
- Not understanding the difference between role-assignable and non-role-assignable groups, leading to insufficient protections for sensitive resources.
- Ignoring the 30-day deactivation period for user B's ownership when the last active owner A is removed from the group or tenant.
- Failing to implement just-in-time access controls for Privileged Access Groups, potentially exposing sensitive resources to unauthorized access.

## KQL / PowerShell
The article does not provide any specific queries or scripts related to PIM for Groups Configuration or Privileged Access Groups.

## Related Topics
- [PIM for groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)
- [Role-assignable group](https://learn.microsoft.com/en-us/azure/active-directory/users-groups-roles/roles-groups-concept?WT.mc_id=M365-MVP-5003945)
- [Eligible membership](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups#what-is-pim-for-groups)
- [PIM activation](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups#pim-for-groups-and-ownership-deactivation)
- [Group PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)
- [Privileged Access Groups](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/groups-features?WT.mc_id=M365-MVP-5003945)