---
conflict_topics:
- intune/reporting/intune-reporting-log-analytics
- intune/security/credential-guard
conflicts:
- '[CONFLICT: Oliver Kieselbach emphasizes this point more strongly]'
- '[CONFLICT: The existing entry does not provide this level of detail]'
- '[CONFLICT: The new source provides a detailed explanation of HSTI and its purpose
  for high assurance validation of proper security configuration]'
- '[CONFLICT: The new source provides more information on the Pre-Boot BitLocker startup
  PIN]'
context_note: Bitlocker Management is part of the intune domain. Synthesised from
  6 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/comment-page-3
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2024-07-25'
  title: BitLocker Recovery Boot Issue After July 2024 Security Update HTMD Blog
  url: https://www.anoopcnair.com/bitlocker-recovery-boot-issue-after-july-2024
stale_after: '2026-07-17'
title: BitLocker Management via Intune
topic: intune/security/bitlocker-management
---

# BitLocker Management via Intune

This topic discusses the process of enabling BitLocker on non-HSTI devices using Microsoft Intune and Windows 10 version 1809, allowing standard user permissions for encryption.

## Key Concepts
- HSTI (Hardware Security Testability Interface) [CONFLICT: The new source provides a detailed explanation of HSTI and its purpose for high assurance validation of proper security configuration]
- MDM policy (Intune)
- BitLocker CSP (BitLocker Configuration Service Provider)
- Enrollment Status Page (ESP)
- Endpoint protection profile
- Custom OMA-URI configuration
- Pre-Boot BitLocker startup PIN (optional, see related topics) [CONFLICT: The new source provides more information on the Pre-Boot BitLocker startup PIN]
- Trusted Computing Group, Endorsement Key, Sealed Storage concept, TPM (Trusted Platform Module), platform configuration registers (PCRs) [New Information from the new source]

## Configuration
1. Ensure the following prerequisites are met:
   - Windows 10 version 1809 Enterprise or Pro
   - Azure Active Directory joined devices
   - Microsoft Intune
   - Enabled Enrollment Status Page (ESP)
   - non-HSTI device

2. Create two configuration policies:
   - Endpoint protection profile for silent BitLocker enforcement and other parameters like encryption strength.
   - A custom profile to enforce BitLocker encryption even when standard users are logging in.

3. Configure the endpoint protection profile:
   - Go to Microsoft Intune > Device configuration – Profiles > **yourpolicyname** – Properties > Endpoint protection > Windows Encryption
     - Set **Encrypt devices** to **Require**
     - Set **Warning for other disk encryption** to **Block**

4. Configure the custom profile:
   - The custom OMA-URI configuration must be configured like this:
     ```
     OMA-URI: ./Vendor/MSFT/BitLocker/AllowStandardUserEncryption
     Data type: integer
     Value: 1
     ```
   - To enable Pre-Boot BitLocker startup PIN, follow the steps outlined in [How to enable Pre-Boot BitLocker startup PIN on Windows with Intune](#how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune) (see related topics).

## How does BitLocker key protection work?

First, we need to understand the general procedure of how BitLocker will get access to the encryption key. The [Trusted Computing Group](https://en.wikipedia.org/wiki/Trusted_Computing_Group) introduced the trusted computing platform. In short, this board defined measures for [trusted computing](https://en.wikipedia.org/wiki/Trusted_Computing). From interest here is the Endorsement Key and the Sealed Storage concept. The underlying idea is to bind private information to the platform configuration to generate the Sealed Storage. This process ensures that the encryption key can only be accessed when the device boots with the correct firmware, BIOS, and operating system.

New source article: "BitLocker Recovery Boot Issue After July 2024 Security Update HTMD Blog"
Author: Anoop C Nair
New source content:
# BitLocker Recovery Boot Issue After July 2024 Security Update HTMD Blog

BitLocker Recovery Boot Issue After July 2024 Security Update HTMD Blog

News Alert! **[BitLocker](https://www.anoopcnair.com/intune-bitlocker-drive-encryption-part4/)** Recovery Boot Issue After **July 2024** Security Update**.** Microsoft Identified a crucial security update that caused some devices to boot into BitLocker recovery. Recently, users faced a problem after installing the July 2024 Windows update (KB5040437).

As you know, Windows update **[KB5040437](https://www.anoopcnair.com/july-2024-windows-11-kb5040442-kb5040431-patche/)** (OS Build 22621.3880) is a recent update that aims to **improve** your system and fix issues. With the latest Windows security updates, some users have faced problems. Microsoft reports the issue **officially** in their document.

Microsoft recently **announced** the Known issue of Devices that Might **Boot** Into BitLocker Recovery, but Microsoft does not currently have any **[fixes](https://www.anoopcnair.com/fix-intune-error-code-80192ee7-the-device/)** for this. This issue is more likely to impact devices with the **Device Encryption** option.

If you recently updated your Windows system with the **July 2024** security update, you may need a Bitlockery recovery screen. As you know, the Bitlockery recovery screen plays a **critical** role in **data [protection](https://www.anoopcnair.com/potentially-unwanted-app-protection-edge/)** and **system security.** So, in this post, we can look at an **overview** of this known issue: ”Devices Might Boot Into BitLocker Recovery”.

- **[Intune Bitlocker Drive Encryption A Deeper Dive To Explore](https://www.anoopcnair.com/intune-bitlocker-drive-encryption-part4/)**
- [**Managing Windows Bitlocker Compliance Policy Using Intune | MS Graph | Grace Period**](https://www.anoopcnair.com/bitlocker-compliance-policy-using-intune/)
- [**Block Hide BitLocker Recovery Key From Users Using MS Graph And PowerShell**](https://www.anoopcnair.com/block-hide-bitlocker-recovery-key-users-graph/)
- **[Intune Bitlocker Drive Encryption A Deeper Dive To Explore](https://www.anoopcnair.com/intune-bitlocker-drive-encryption-part4/)**
- [**Device Encryption – Bitlocker made Effortless**](https://www.anoopcnair.com/exploring-bitlocker-device-encryption/)
- [**Deciphering Intune’s Scope w.r.t Bitlocker Drive Encryption**](https://www.anoopcnair.com/exploring-bitlocker-drive-encryption/)
- **[Bitlocker Recovery key Screen Prompt Issues | Error 0x800f0922 after installing August Patch KB5012170](https://www.anoopcnair.com/bitlocker-recovery-key-screen-prompt-issues/)**

| Index |
| --- |
| [Troubleshooting BitLocker Boot Failures After July 2024 Update](https://www.anoopcnair.com/bitlocker-recovery-boot-issue-after-july-2024/#BitLocker-Recovery-Boot-Issue-After-July-2024-Security-Update) |
| [Solution for this Known Issue](https://www.anoopcnair.com/bitlocker-recovery-boot-issue-after-july-2024/#Solution-for-this-Known)