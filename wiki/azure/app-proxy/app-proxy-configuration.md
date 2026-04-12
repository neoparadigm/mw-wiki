---
conflicts:
- '[CONFLICT: The new source mentions integration with Intune app protection policy,
  but the existing entry does not.]'
- '[CONFLICT: The new source does not specify whether this step is necessary for the
  integration with Intune Managed Browser and Conditional Access.]'
- '[CONFLICT: The new source does not provide specific steps for this step.]'
domain: azure
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access
stale_after: '2026-07-11'
title: Azure App Proxy Configuration
topic: azure/app-proxy/app-proxy-configuration
---

# Azure App Proxy Configuration and Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional Access

## Overview
The Azure App Proxy Configuration allows organizations to publish their internal websites externally with minimal effort, ensuring secure access to these resources on mobile devices through the Intune Managed Browser (MAM) and app-based Conditional Access (CA). This solution supports various authentication scenarios inclusive Single Sign-On (SSO), and does not require opening up any inbound firewall ports. [CONFLICT: The new source mentions integration with Intune app protection policy, but the existing entry does not.]

## Key Concepts
- Intune Managed Browser (MAM)
- App-based Conditional Access (CA)
- Azure AD Application Proxy
- Internal websites publishing
- Single Sign-On (SSO)
- On-premises application access

## Configuration
1. Disable the IE Enhanced Security Configuration on the Windows Server. [CONFLICT: The new source does not specify whether this step is necessary for the integration with Intune Managed Browser and Conditional Access.]
2. Download and install the Azure AD Application Proxy on the demo IIS server using the msi installer, providing Global Administrator credentials during setup.
3. Enable the installed connector by clicking "Enable application proxy".
4. Configure the internal websites to be published through the Azure AD Application Proxy. [CONFLICT: The new source does not provide specific steps for this step.]

## Common Pitfalls
- Failing to disable IE Enhanced Security Configuration before setting up the Azure AD Application Proxy.
- Installing the connector on the IIS server instead of a dedicated Windows Server 2016.

## KQL / PowerShell
[No specific queries or scripts provided in the article]

## Related Topics
- App Proxy
- application proxy
- connector
- on-prem app
- pre-auth
- Intune Managed Browser (MAM)
- Intune app protection policy
- Conditional Access