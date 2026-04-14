---
conflicts:
- '[CONFLICT: Daniel Chronlund says the tool Enable-DCAzureADPIMRole is included in
  DCToolbox PowerShell module, existing entry does not mention this.]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: unknown
  crawled: '2026-04-14'
  date: '2021-09-17'
  title: Activate your Azure AD PIM roles with PowerShell
  url: https://danielchronlund.com/2021/09/17/activate-your-azure-ad-pim-roles-with-powershell/
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2021-09-17'
  title: Activate your Azure AD PIM roles with PowerShell
  url: https://danielchronlund.com/2021/09/17/activate-your-azure-ad-pim-roles-with-powershell
- author: kenwith
  crawled: '2026-04-14'
  date: '2026-03-23'
  title: Privileged Identity Management (PIM) for Groups - Microsoft Entra ID Governance
  url: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups
stale_after: '2026-06-13'
title: PIM for Groups Configuration
topic: identity/pim/pim-for-groups
---

# PIM for Groups Configuration

## PIM for Groups Configuration
This topic covers the configuration of Azure AD Privileged Identity Management (PIM) for groups, which is a crucial aspect of Microsoft 365's Zero Trust strategy. PIM for groups helps implement Just-In-Time/Just-Enough Access (JIT/JEA) for admin roles within an organization.

## Key Concepts
- Azure AD Privileged Identity Management (PIM)
- JIT/JEA for admin roles
- Role-assignable groups in PIM
- Eligible membership in PIM
- PIM activation
- Group PIM
- [Privileged Access Groups](#privileged-access-groups) - Microsoft Entra ID Governance (New Source)

## Configuration
1. Install the `DCToolbox` PowerShell module from the PowerShell Gallery by running `Install-Module -Name DCToolbox -Force`.
2. Install two dependencies for `Enable-DCAzureADPIMRole`: `AzureADPreview` and `msal.ps`. You can run the following installation snippets:

```
# For local admin users:
Install-Module -Name DCToolbox -Force
Install-Module -Name AzureADPreview -Force
Install-Package msal.ps -AcceptLicense -Force

# For non-admin users:
Install-Module -Name DCToolbox -Scope CurrentUser -Force
Install-Module -Name AzureADPreview -Scope CurrentUser -Force
Install-Package msal.ps -AcceptLicense -Force
```

3. Run the command to activate your Azure AD PIM roles with PowerShell:

```
# Enable one of your Azure AD PIM roles.
Enable-DCAzureADPIMRole
```

4. To activate multiple roles at once, use the `-RolesToActivate` parameter:

```
# Enable multiple Azure AD PIM roles.
Enable-DCAzureADPIMRole -RolesToActivate @("role1", "role2")
```

## Common Pitfalls
- In highly locked-down environments, the `msal.ps` package may fail due to dependencies. If you encounter any error messages, connect with `Connect-AzureAD` before running `Enable-DCAzureADPIMRole`.
- This method is not the same as using Privileged Access groups in PIM. Privileged Access groups are managed by PIM administrators and group multiple Azure AD roles to specific work roles within the organization. (CONFLICT: kenwith mentions "Privileged Access Groups" as a feature, while existing entry only mentions "Privileged Access groups" in the related topics section)

## KQL / PowerShell
[The article includes a PowerShell script for activating Azure AD PIM roles with PowerShell, formatted as follows:]

```powershell
# Enable one of your Azure AD PIM roles.
Enable-DCAzureADPIMRole

# Enable multiple Azure AD PIM roles.
Enable-DCAzureADPIMRole -RolesToActivate @("role1", "role2")
```

## Related Topics
- [PIM for groups](wiki:pim_for_groups)
- [role-assignable group](wiki:role-assignable_group)
- [eligible membership](wiki:eligible_membership)
- [PIM activation](wiki:pim_activation)
- [group PIM](wiki:group_pim)
- [Privileged Access Groups](#privileged-access-groups) - Microsoft Entra ID Governance (New Source)

## Privileged Access Groups (New Source)
Microsoft Entra ID allows you to grant users just-in-time membership and ownership of groups through Privileged Identity Management (PIM) for Groups. Groups can be used to control access to a variety of scenarios, including Microsoft Entra roles, Azure roles, Azure SQL, Azure Key Vault, Intune, other application roles, and third-party applications.

### What is PIM for Groups?
PIM for Groups is part of Microsoft Entra Privileged Identity Management – alongside PIM for Microsoft Entra roles and PIM for Azure Resources, PIM for Groups enables users to activate the ownership or membership of a Microsoft Entra security group or Microsoft 365 group. Groups can be used to govern access to various scenarios that include Microsoft Entra roles, Azure roles, Azure SQL, Azure Key Vault, Intune, other application roles, and third-party applications.

With PIM for Groups you can use policies similar to ones you use in PIM for Microsoft Entra roles and PIM for Azure Resources: you can require approval for membership or ownership activation, enforce multifactor authentication (MFA), require justification, limit maximum activation time, and more. Each group in PIM for Groups has two policies: one for activation of membership and another for activation of ownership in the group. Up until January 2023, the PIM for Groups feature was called “Privileged Access Groups”.

Note
For groups used for elevating into Microsoft Entra roles, we recommend that you require an approval process for eligible member assignments. Assignments that can be activated without approval can leave you vulnerable to a security risk from less-privileged administrators. For example, the Helpdesk Administrator has permission to reset an eligible user's passwords.

### PIM for Groups and ownership deactivation
Microsoft Entra ID doesn't allow you to remove the last (active) owner of a group. For example, consider a group that has active owner A and eligible owner B. If user B activates their ownership with PIM and then later user A is removed from the group or from the tenant, deactivation of user B's ownership won't succeed.

PIM will try to deactivate user B's ownership for up to 30 days. If another active owner C is added to the group, the deactivation will succeed.