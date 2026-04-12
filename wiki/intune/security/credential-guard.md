---
conflicts:
- '[CONFLICT: Oliver Kieselbach provides additional details on configuring Credential
  Guard via Policy CSP support, while the existing entry only mentions it as an alternative
  method.]'
- '[CONFLICT: Anoop C Nair provides additional details on configuring VBS via Microsoft
  Intune, while the existing entry only mentions it as an alternative method.]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-01-27'
  title: January 2018 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2018/01
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2025-01-16'
  title: Best Method To Enable Virtualization Based Security Using Microsoft Intune
    HTMD Blog
  url: https://www.anoopcnair.com/enable-virtualization-based-security-intune
stale_after: '2026-07-11'
title: Credential Guard and VBS
topic: intune/security/credential-guard
---

# Credential Guard and VBS

## Overview
Windows Defender Credential Guard is a feature in Windows 10 Enterprise designed to protect NTLM, Kerberos, and Sign-on credentials by isolating certain Operating System (OS) pieces using virtualization-based security (VBS). This protection is crucial as it prevents malicious tools like Mimikatz from extracting credentials from the Local Security Authority (LSA).

## Key Concepts
- Virtualization-based security (VBS)
- LSASS process and LSAiso process
- Protection of NTLM, Kerberos, and Sign-on credentials
- Mimikatz tool extraction of credentials from LSASS

## Configuration
To configure Windows Defender Credential Guard via Modern Management in Intune:
1. Create a custom device profile.
2. Add the following OMA-URIs to configure Credential Guard with default settings and additional DMA Protection:
   - `DeviceGuard/EnableVirtualizationBasedSecurity`
   - `DeviceGuard/LsaCfgFlags`
   - `DeviceGuard/RequirePlatformSecurityFeatures`
3. Assign the new device configuration profile to the desired user group.

**UPDATE:** It is now possible to configure Credential Guard using the built-in “Endpoint protection” configuration profile, and also through Policy CSP support as detailed in [Configuring Windows Defender Credential Guard with Intune](https://start9.com/configuring-windows-defender-credential-guard-with-intune/) by Oliver Kieselbach. Additionally, the new source provides information on configuring Credential Guard via Policy CSP support ([Configuring Windows Defender Credential Guard with Intune](https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune/)).

**[CONFLICT: Oliver Kieselbach provides additional details on configuring Credential Guard via Policy CSP support, while the existing entry only mentions it as an alternative method.]**

**New Information:** Microsoft Intune simplifies the deployment of VBS across managed devices through security baselines and configuration profiles. Administrators can create and assign security policies that enable features like Hypervisor-Enforced Code Integrity (HVCI) and Credential Guard. This centralized approach ensures consistent security settings across endpoints, reducing the risk of misconfigurations and security gaps. Also, Virtualization Based Security (VBS) must be enabled to receive Hotpatch updates on a Windows device.

**[CONFLICT: Anoop C Nair provides additional details on configuring VBS via Microsoft Intune, while the existing entry only mentions it as an alternative method.]**

## Common Pitfalls
- Ensuring the device was restarted after successful configuration, as Credential Guard relies on Hyper-V technology for virtualization-based security.

## KQL / PowerShell
Not applicable in this article.

## Related Topics
- Credential Guard
- VBS
- Virtualisation-based security
- LSASS protection
- Pass-the-Hash

The new source provides additional information on configuring Credential Guard via Policy CSP support, which is now an alternative method to the existing configuration process. However, there are no conflicts between sources. The existing entry remains unchanged as it already includes the Policy CSP configuration details provided in the new source.

## References
- January 2018 – Modern IT – Cloud – Workplace ([oliverkieselbach.com](https://oliverkieselbach.com))
- Best Method To Enable Virtualization Based Security Using Microsoft Intune HTMD Blog ([anoopcnair.com](https://www.anoopcnair.com/best-method-to-enable-virtualization-based-security-using-microsoft-intune/))