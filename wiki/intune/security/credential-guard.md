---
conflict_topics:
- intune/security/bitlocker-management
- intune/security/defender-for-endpoint-intune
conflicts:
- '[CONFLICT: Anoop C Nair provides additional details on the OMA-URI values, but
  the existing entry does not conflict with this information.]'
context_note: Credential Guard is part of the intune domain. Synthesised from 5 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-01-11'
  title: Configuring Windows Defender Credential Guard with Intune
  url: https://oliverkieselbach.com/2018/01/11/configuring-windows-defender-credential-guard-with-intune/
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-01-16'
  title: Best Method To Enable Virtualization Based Security Using Microsoft Intune
    HTMD Blog
  url: https://www.anoopcnair.com/enable-virtualization-based-security-intune
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-01-27'
  title: January 2018 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2018/01
- author: officedocspr5
  crawled: '2026-04-18'
  date: '2026-03-29'
  title: Credential Guard overview
  url: https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard
stale_after: '2026-07-17'
title: Credential Guard and VBS
topic: intune/security/credential-guard
---

# Credential Guard and VBS

## Overview
Windows Defender Credential Guard is a feature in Windows 10 Enterprise designed to protect NTLM, Kerberos, and Sign-on credentials by isolating certain Operating System (OS) pieces using virtualization-based security (VBS). This protection is crucial as it prevents malicious tools like Mimikatz from extracting credentials from the Local Security Authority (LSA).

The new sources provide additional details about the configuration of Credential Guard using Modern Management in Intune and offer an overview of Credential Guard.

### From "January 2018 - Modern IT - Cloud - Workplace" by Oliver Kieselbach
- Credential Guard prevents credential theft attacks by protecting NTLM password hashes, Kerberos Ticket Granting Tickets (TGTs), and credentials stored by applications as domain credentials.
- When enabled, Credential Guard provides the following benefits:
  - Hardware security: NTLM, Kerberos, and Credential Manager take advantage of platform security features, including Secure Boot and virtualization, to protect credentials.
  - Virtualization-based security: NTLM, Kerberos derived credentials, and other secrets run in a protected environment that is isolated from the running operating system.
  - Protection against advanced persistent threats: when credentials are protected using VBS, the credential theft attack techniques and tools used in many targeted attacks are blocked. Malware running in the operating system with administrative privileges can't extract secrets that are protected by VBS.

### From "Credential Guard overview" by officedocspr5
- Credential Guard uses [Virtualization-based security (VBS)](/en-us/windows-hardware/design/device-experiences/oem-vbs) to isolate secrets so that only privileged system software can access them. Unauthorized access to these secrets can lead to credential theft attacks like *pass the hash* and *pass the ticket*.
- While Credential Guard is a powerful mitigation, persistent threat attacks will likely shift to new attack techniques, and you should also incorporate other security strategies and architectures.

## Key Concepts
- Virtualization-based security (VBS): A technology that isolates certain OS components to protect them from malicious tools. [New: This section is expanded with more details.] VBS leverages hardware virtualization features to create an isolated, secure memory region within the system, protecting critical system processes from common vulnerabilities and attacks.
- LSASS: The Local Security Authority Subsystem process, which stores NTLM and Kerberos credentials.
- LSAiso: An isolated process created by VBS that can only be accessed by the LSASS process, protecting credentials from malicious tools.
- Credential Guard: A feature that protects an attack vector used by bad actors to steal sensitive information.

## Configuration
To configure Windows Defender Credential Guard via Modern Management in Intune:

1. Create a custom device profile.
2. Choose Profile type: custom.
3. Add the following OMA-URIs to configure Credential Guard with default settings and additional DMA Protection:
   - `DeviceGuard/EnableVirtualizationBasedSecurity` (enable virtualization based security)
   - `DeviceGuard/LsaCfgFlags` (Enabled with UEFI lock) [CONFLICT: Anoop C Nair provides additional details on the OMA-URI values, but the existing entry does not conflict with this information.]
   - `DeviceGuard/RequirePlatformSecurityFeatures` (Turns on VBS with Secure Boot and direct memory access (DMA). DMA requires hardware support.)
4. Assign the new device configuration profile to the desired user group.
   - **NOTE:** It is now possible to configure Credential Guard using the built-in “Endpoint protection” configuration profile, as mentioned in the new source.

## Common Pitfalls
- Ensuring the device was restarted after successful configuration, as Credential Guard relies on Hyper-V technology for virtualization-based security.

## KQL / PowerShell
Not applicable in this article.

## Related Topics
- Credential Guard
- VBS (Virtualization-based Security)
- LSASS Protection
- Pass-the-Hash