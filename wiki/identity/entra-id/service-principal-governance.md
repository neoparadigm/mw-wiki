---
conflict_topics:
- identity/entra-id/passwordless-authentication
- identity/hybrid/entra-connect-hardening
conflicts:
- '[CONFLICT: Michael Morten Sonne does not provide a definition for Service Principal]'
- '[CONFLICT: Michael Morten Sonne does not mention Client Secret]'
- '[CONFLICT: Michael Morten Sonne does not provide specific instructions for registering
  an app]'
- '[CONFLICT: Michael Morten Sonne does not provide specific instructions for configuring
  permissions]'
- '[CONFLICT: Michael Morten Sonne does not mention setting up a client secret]'
- '[CONFLICT: Michael Morten Sonne does not mention any specific pitfalls]'
context_note: Service Principal Governance is part of the identity domain. Synthesised
  from 6 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-08-18'
  title: 'Entra ID – Managed Identity Permission Manager: A Community-Driven Recap
    – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/entra-id-managed-identity-permission-manager-a-community-driven-recap
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-05-13'
  title: Entra ID – Managed Identity Permissions Manager – Performance Stats and Community
    Insights – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-managed-identity-permissions-manager-performance-stats-and-community-insights
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-11-01'
  title: Managed Identity Permission Manager – v. 1.0.0.2 is out! – Blog - Sonne´s
    Cloud
  url: https://blog.sonnes.cloud/managed-identity-permission-manager-v-1-0-0-2-is-out
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-01-24'
  title: Managed Identity Permission Manager – v. 1.0.0.4 is out! – Blog - Sonne´s
    Cloud
  url: https://blog.sonnes.cloud/managed-identity-permission-manager-v-1-0-0-4-is-out
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-02-06'
  title: 🚀 Managed Identity Permission Manager v1.1.0.0 is here! 🚀 – Blog - Sonne´s
    Cloud
  url: https://blog.sonnes.cloud/managed-identity-permission-manager-v1-1-0-0-is-here
- author: Jan Bakker
  crawled: '2026-04-18'
  date: '2025-10-20'
  title: A public bug report for Entra ID application policies
  url: https://janbakker.tech/a-public-bug-report-for-entra-id-application-policies
stale_after: '2026-06-17'
title: Service Principal and App Registration Governance
topic: identity/entra-id/service-principal-governance
---

# Service Principal and App Registration Governance

## Service Principal and App Registration Governance

### Overview
Service Principal and App Registration Governance is an essential aspect of managing Azure AD identities, particularly in the context of Managed Identities. This topic matters because it helps administrators maintain control over the lifecycle, security, and permissions of service principals and app registrations.

### Key Concepts
- Service Principal: A security identity representing a service or application that can authenticate and access resources in Azure AD. [CONFLICT: Michael Morten Sonne does not provide a definition for Service Principal]
- App Registration: The registration of an application in Azure AD, which includes details like the application's name, redirect URI, and supported account types.
- Client Secret: A secret value used for authentication by confidential clients (e.g., daemons or web applications) when they cannot use certificates. [CONFLICT: Michael Morten Sonne does not mention Client Secret]
- Certificate Auth: Authentication method using digital certificates to establish the identity of a service principal.
- SP Governance: Policies and practices aimed at managing the lifecycle, security, and permissions of service principals in Azure AD.
- Application Exception (New): A temporary exception granted to an automated process or user account that creates or modifies applications, bypassing certain security policies due to compatibility issues with existing processes. [Source: Jan Bakker]

### Configuration
- Register an app in Azure AD by navigating to the App Registrations section and following the prompts. [CONFLICT: Michael Morten Sonne does not provide specific instructions for registering an app]
- Configure required permissions for the app registration by adding appropriate API permissions. [CONFLICT: Michael Morten Sonne does not provide specific instructions for configuring permissions]
- Set up a client secret or certificate for authentication, depending on the client type. [CONFLICT: Michael Morten Sonne does not mention setting up a client secret]
- Assign roles to the service principal to control its access to resources in Azure AD.
- Grant Application Exceptions (New) to specific users or automated processes that require bypassing certain security policies due to compatibility issues with existing processes. [Source: Jan Bakker]

### Common Pitfalls
- Neglecting to rotate client secrets regularly, increasing the risk of unauthorized access.
- Granting excessive permissions to service principals, leading to potential security vulnerabilities.
- Failing to monitor and manage service principals effectively, resulting in orphaned or unused identities. [CONFLICT: Michael Morten Sonne does not mention any specific pitfalls]
- Incorrectly defining security attribute sets for Application Exceptions, causing them to be of type boolean instead of string. [Source: Jan Bakker]

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to Service Principal and App Registration Governance.]

### Related Topics
- [Service Principal](https://blog.sonnes.cloud/topics/identity/)
- [App Registration](https://blog.sonnes.cloud/topics/general/software/cool-tools/)
- [Certificate Auth](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
- [SP Governance](https://docs.microsoft.com/en-us/azure/active-directory/governance/entitlement-management-overview)
- [Entra ID – Managed Identity Permissions Manager – Performance Stats]
- [Jan Bakker's Blog Post on Application Exceptions](https://janbakker.tech/a-closer-look-at-entra-application-policies-to-govern-secrets-and-certificates/)