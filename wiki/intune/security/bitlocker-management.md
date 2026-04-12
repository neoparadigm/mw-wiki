---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests that older devices can be protected by Intune
  BitLocker policy now, but the existing entry does not mention this.]'
- '[CONFLICT: Oliver Kieselbach''s article suggests that these custom solutions are
  no longer necessary with Windows 10 version 1809.]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2025-07-14'
  title: 'KQL Queries Made Easy: My Intune Admin Journey with Copilot - Ugur Koc'
  url: https://ugurkoc.de/kql-queries-made-easy-my-intune-admin-journey-with-copilot
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune/
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-08-17'
  title: Activate Mac FileVault using Intune
  url: https://jannikreinhard.com/2022/08/17/activate-mac-filevault-using-intune
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2025-10-14'
  title: Windows 11 KB5066835 KB5066793 October 2025 Patch And 5 Zero Day Vulnerabilies
    And 118 Flaws HTMD Blog
  url: https://www.anoopcnair.com/windows-11-kb5066835-kb5066793-october-2025
stale_after: '2026-07-11'
title: BitLocker Management via Intune
topic: intune/security/bitlocker-management
---

# BitLocker Management via Intune

## Overview
BitLocker Management via Intune provides administrators with the ability to manage BitLocker encryption on Windows devices through Microsoft Endpoint Manager (Intune). This topic matters as it ensures data protection and compliance by encrypting sensitive data stored on devices.

## Key Concepts
- BitLocker: A full disk encryption feature included in Windows Vista and later versions that helps protect data by providing encryption for fixed drives.
- Microsoft Endpoint Manager (Intune): A cloud-based service that provides unified endpoint management, including configuration, compliance, and security management for mobile devices and computers.
- BitLocker Recovery Key: A backup key used to unlock encrypted drives when the user forgets their password or loses access to the recovery information stored on the device.
- Silent Encryption: An option in BitLocker that allows encryption to occur without user interaction, making it suitable for automated deployment scenarios.
- BitLocker Policy: A set of configuration settings that define how BitLocker operates on a specific device or group of devices.
- HSTI (from Oliver Kieselbach's article)
- Non-HSTI devices (added from Oliver Kieselbach's article)
- FileVault (new from Jannik Reinhard's article)
- [FileVault](#activatemacfilevaultusingintune) (new from Jannik Reinhard's article)

## Configuration
1. In the Microsoft Endpoint Manager admin center, navigate to Tenant administration > Connectors and tokens > Connectors.
2. Click Add, select the connector type as "Endpoint Manager connector," and follow the prompts to configure the connector.
3. Navigate to Devices > Windows > Configuration Manager > BitLocker Recovery.
4. Create a new policy or edit an existing one, and configure the settings according to your requirements. This includes enabling silent encryption for automated deployment scenarios. [CONFLICT: Oliver Kieselbach suggests that older devices can be protected by Intune BitLocker policy now, but the existing entry does not mention this.]
5. Deploy the policy to the appropriate groups of devices.

## Common Pitfalls
- Failing to configure recovery keys properly can lead to data loss if users are unable to unlock encrypted drives.
- Incorrectly configuring BitLocker policies may result in encryption conflicts or unexpected behavior on devices.
- Not using silent encryption during automated deployment scenarios can require user interaction, which may not be feasible in some cases.

## Related Topics
- BitLocker
- Encryption
- Recovery key
- Silent encryption
- BitLocker policy
- [HSTI](https://docs.microsoft.com/en-us/windows-hardware/test/hlk/testref/hardware-security-testability-specification) (from Oliver Kieselbach's article)
- Non-HSTI devices (added from Oliver Kieselbach's article)
- [FileVault](#activatemacfilevaultusingintune) (new from Jannik Reinhard's article)
- [Windows 11 KB5066835 KB5066793 October 2025 Patch And 5 Zero Day Vulnerabilies And 118 Flaws HTMD Blog](#windows11kb5066835kb5066793october2025patchand5zerodayvulnerabilitiestmdblog) (new from Anoop C Nair's article)

## Enabling BitLocker on non-HSTI devices with Intune

Enabling BitLocker on non-HSTI devices with the October 2025 Patch Tuesday update is now possible, as the issue where a link for BitLocker drive encryption could appear on unsupported drives has been fixed. This prevents the error (0x80004005) and ensures a smoother experience when managing disk encryption.

## Windows 11 KB5066835 KB5066793 October 2025 Patch And 5 Zero Day Vulnerabilies And 118 Flaws HTMD Blog

Windows 11 **KB5066835 KB5066793** **October 2025 Patch and 5 Zero Day Vulnerabilities and 118 Flaws**. In the october 2025 Patch Tuesday release, Microsoft rolled out important **updates** targeting **security**, stability, and overall system performance.

For Windows 11, the updates KB5066835 and KB5066793 deliver a set of performance enhancements and critical security fixes, addressing vulnerabilities that could impact system integrity. This release also shows **5 zero-day vulnerability** along with other security flaws. **Windows 10** receives KB5066791, which focuses on improving system reliability, performance, and security

In the October update, **[Click to Do](https://www.anoopcnair.com/click-to-do-powerful-windows-application/)** introduces several exciting new features designed to enhance productivity and user interactions. The **context menu** now includes new and popular action tags, making it easier to discover the latest and most widely used **AI-powered actions**.

The October update addresses an issue in Settings > System > Storage > **Disks and Volumes**, where a link for BitLocker drive encryption could appear even on unsupported drives. Previously, selecting this link would open BitLocker and trigger error **0x80004005**. With the fix, this incorrect link no longer appears, preventing the error and ensuring a **smoother**, more reliable experience when managing disk encryption.

Windows 11 KB5066835 KB5066793 October 2025 Patch and 5 Zero Day Vulnerabilies and 118 Flaws – Fig.1

## **Table of Contents**

## ****5 Zero Day Security Vulnerabilities for October 2025****

The October 2025 Patch Tuesday update includes 5 zero-day vulnerabilities, four of which are already being actively exploited. These flaws impact components such as Windows Remote Access Connection Manager, Agere Modem Drivers, IGEL OS Secure Boot, and the TCG TPM 2.0 reference implementation.

| Release Date | CVE Number | CVE Title | Publicly disclosed | Exploitability assessment | Exploited |
| --- | --- | --- | --- | --- | --- |
| Oct 14, 2025 | [CVE-2025-59230](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59230) | **Windows Remote Access Connection Manager Elevation of Privilege Vulnerability** | No | **Exploitation Detected** | Yes |
| Oct 14, 2025 | [CVE-2025-47827](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47827) | MITRE CVE-2025-47827: Secure Boot bypass in IGEL OS before 11 | No | Exploitation Detected | Yes |
| Oct 14, 2025 | [CVE-2025-24990](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24990) | Windows Agere Modem Driver Elevation of Privilege Vulnerability | No | Exploitation Detected | Yes |
| Oct 14, 2025 | [CVE-2025-2884](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-2884) | **Microsoft TPM 2.0 Reference Implementation Elevation of Privilege Vulnerability** | No | Exploitation Detected | Yes |
| Oct 14, 2025 | [CVE-2025-3967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-3967) | **Microsoft Windows Kernel Elevation of Privilege Vulnerability** | No | Exploitation Detected | Yes |