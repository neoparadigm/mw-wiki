---
conflict_topics:
- azure/monitoring/azure-monitor-log-analytics
conflicts:
- '[CONFLICT: Oliver Kieselbach does not mention this, but the existing entry includes
  it]'
- '[CONFLICT: The new source does not provide specific steps for configuring Conditional
  Access policies, but it is mentioned in the existing entry]'
context_note: App Proxy Configuration is part of the azure domain. Synthesised from
  2 community sources.
domain: azure
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access
stale_after: '2026-07-17'
title: Azure App Proxy Configuration
topic: azure/app-proxy/app-proxy-configuration
---

# Azure App Proxy Configuration

## Overview
The Azure App Proxy is a service that allows internal applications to be published and accessed securely from outside the corporate network, enhancing the Modern Workplace experience by enabling Bring Your Own Device (BYOD) solutions. The new source article discusses the integration of Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional Access, which allows for publishing internal websites externally with minimal effort and secure access from mobile devices using the Intune Managed Browser protected by an Intune app protection policy.

## Key Concepts
- Mobile Application Management (MAM)
- Intune Managed Browser (MAM)
- App-based Conditional Access (CA)
- Azure AD Application Proxy
- Intune app protection policy
- Single Sign-On (SSO)
- Inbound and outbound firewall connections
[CONFLICT: Oliver Kieselbach does not mention this, but the existing entry includes it]
- Disable IE Enhanced Security Configuration on the Windows Server

## Configuration
1. Disable IE Enhanced Security Configuration on the Windows Server.
2. Download and install the Azure AD Application Proxy on the server hosting the internal websites.
3. Enable the installed connector.
4. Configure Conditional Access policies to approve access only through the Intune Managed Browser.
[CONFLICT: The new source does not provide specific steps for configuring Conditional Access policies, but it is mentioned in the existing entry]

## Common Pitfalls
- Failing to disable IE Enhanced Security Configuration can prevent the Azure AD Application Proxy from functioning correctly during setup.
- Not configuring Conditional Access policies properly may allow unauthorized access to internal resources.

## KQL / PowerShell
[No specific queries or scripts provided in the article]

## Related Topics
- App Proxy
- application proxy
- connector
- on-prem app
- pre-auth
- Intune Managed Browser (MAM)
- Azure AD Application Proxy
- Conditional Access policies
- Single Sign-On (SSO)