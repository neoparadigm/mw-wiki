---
conflicts:
- '[CONFLICT: Oliver Kieselbach does not mention inbound and outbound firewall connections,
  existing entry includes them]'
- '[CONFLICT: Oliver Kieselbach suggests a different order of steps, first enabling
  the Azure AD Application Proxy and then configuring Conditional Access policies]'
- '[CONFLICT: No specific pitfalls mentioned by Oliver Kieselbach]'
- '[CONFLICT: Oliver Kieselbach suggests enabling the Azure AD Application Proxy before
  disabling IE Enhanced Security Configuration]'
- '[CONFLICT: New source does not provide specific configuration steps related to
  this topic]'
domain: azure
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-03-17'
  title: Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional
    Access
  url: https://oliverkieselbach.com/2018/03/17/intune-managed-browser-mam-with-azure-ad-application-proxy-and-conditional-access
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune/comment-page-2
stale_after: '2026-07-13'
title: Azure App Proxy Configuration
topic: azure/app-proxy/app-proxy-configuration
---

# Azure App Proxy Configuration and Intune Managed Browser (MAM) with Azure AD Application Proxy and Conditional Access

## Overview
The Azure App Proxy is a service that allows internal applications to be published and accessed securely from outside the corporate network, enhancing the Modern Workplace experience by enabling Bring Your Own Device (BYOD) solutions. Recently, Microsoft enhanced the Intune Managed Browser (MAM) experience with app-based Conditional Access (CA) integration, allowing for a solution to publish internal websites externally with minimal effort and secure access from mobile devices using the Intune Managed Browser.

[CONFLICT: Oliver Kieselbach does not mention inbound and outbound firewall connections, existing entry includes them]

## Key Concepts
- Mobile Application Management (MAM)
- Intune Managed Browser (MAM)
- App-based Conditional Access (CA)
- Azure AD Application Proxy
- Internal websites publishing
- Single Sign-On (SSO)

## Configuration
1. Disable IE Enhanced Security Configuration on the Windows Server.
2. Enable the Azure AD Application Proxy. [CONFLICT: Oliver Kieselbach suggests enabling the Azure AD Application Proxy before disabling IE Enhanced Security Configuration]
3. Download and install the Azure AD Application Proxy on the server hosting the internal websites.
4. Configure Conditional Access policies to approve the Intune Managed Browser for accessing the published applications. [CONFLICT: New source does not provide specific configuration steps related to this topic]

[CONFLICT: No specific pitfalls mentioned by Oliver Kieselbach]

## The easy way to deploy device certificates with Intune (New Source)
In this guide, we will have a look at an easy way to deploy device certificates to modern cloud managed clients using SCEPman | Intune SCEP-as-a-Service. This solution does not require an on-premises PKI and is available in the Azure Marketplace.

A typical setup would involve:

1. An active Azure Subscription
2. The SCEPman service from [Glück & Kanja Consulting AG](https://glueckkanja.com) available in the [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/gluckkanja.scepman?tab=Overview)

## Related Topics
- App Proxy
- application proxy
- connector
- on-prem app
- pre-auth
- Intune Managed Browser (MAM)
- Conditional Access (CA)
- Device Certificates (New Source)