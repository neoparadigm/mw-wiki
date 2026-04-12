---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-02-09'
  title: Microsoft 365 Data Exfiltration &#8211; Attack and Defend
  url: https://danielchronlund.com/2023/02/09/microsoft-365-data-exfiltration-attack-and-defend
stale_after: '2026-06-11'
title: Service Principal and App Registration Governance
topic: identity/entra-id/service-principal-governance
---

# Service Principal and App Registration Governance

## Service Principal and App Registration Governance

Service principal and app registration governance is crucial for securing Microsoft 365 tenants by managing access to sensitive data through properly configured Azure AD applications and Microsoft Graph permissions.

## Key Concepts
- Insecure app registrations with privileged API permissions assigned
- Possible privilege escalation paths
- Possible data exfiltration
- Risky API permissions such as Files.Read.All, Files.ReadWrite.All, Sites.Read.All, Sites.ReadWrite.All, GroupMember.Read.All, Group.Read.All, Directory.Read.All, Group.ReadWrite.All, and Directory.ReadWrite.All
- The use of client secrets instead of certificates for highly privileged app registrations

## Configuration
1. Review all app registrations in Azure AD to identify any with risky API permissions or insecure configurations.
2. Implement Multi-Factor Authentication (MFA) for all application administrators and service principals.
3. Use certificates instead of client secrets for highly privileged app registrations.
4. Regularly audit and revoke unused or unnecessary app registrations.
5. Limit the number of Application Administrators in the tenant to only those who require access.

## Common Pitfalls
- Failing to regularly review and manage app registrations, leading to insecure configurations and potential data exfiltration.
- Granting too many permissions to an application, increasing the risk of privilege escalation and data exposure.
- Using client secrets instead of certificates for highly privileged app registrations, making them more vulnerable to credential theft.

## KQL / PowerShell
```powershell
Invoke-DCM365DataExfiltration -ClientID '' -ClientSecret '' -TenantName 'COMPANY.onmicrosoft.com' -WhatIf
```

## Related Topics
- [Service Principal](service_principal)
- [App Registration](app_registration)
- [Client Secret](client_secret)
- [Certificate Auth](certificate_auth)
- [SP Governance](sp_governance)