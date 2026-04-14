---
conflicts:
- '[CONFLICT: The existing entry mentions configuring Credential Guard via Policy
  CSP support, but the new source provides additional details and a different method
  for doing so.]'
- '[CONFLICT: Oliver Kieselbach says X, existing entry says Y]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-01-27'
  title: January 2018 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2018/01
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2025-01-16'
  title: Best Method To Enable Virtualization Based Security Using Microsoft Intune
    HTMD Blog
  url: https://www.anoopcnair.com/enable-virtualization-based-security-intune
stale_after: '2026-07-13'
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

[CONFLICT: The existing entry mentions configuring Credential Guard via Policy CSP support, but the new source provides additional details and a different method for doing so.]

### New Information from the new source
- Virtualization Based Security (VBS) can be enabled using Microsoft Intune to safeguard sensitive data and prevent exploits targeting kernel-level code execution.
- VBS must be enabled to receive Hotpatch updates on a Windows device.
- To create a configuration policy to Enable Virtualization Based Security using Microsoft Intune, sign in to the [Microsoft Intune Admin Center](https://intune.microsoft.com/), navigate to Devices > Windows, and follow the steps provided in the new source article "Best Method To Enable Virtualization Based Security Using Microsoft Intune HTMD Blog".

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

The new source provides additional information on configuring Credential Guard via Policy CSP support, which can be an alternative method to the existing configuration process. However, there is no conflict between sources as they both provide valid methods for configuring Credential Guard in Windows 10 Enterprise. The updated wiki entry includes the new configuration method from Oliver Kieselbach's article and Anoop C Nair's blog post.

New source articles:
- "January 2018 - Modern IT - Cloud - Workplace" by Oliver Kieselbach
- "Best Method To Enable Virtualization Based Security Using Microsoft Intune HTMD Blog" by Anoop C Nair