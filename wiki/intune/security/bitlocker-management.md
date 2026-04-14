---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests this is a requirement, while the existing
  entry does not explicitly state it.]'
- '[CONFLICT: Oliver Kieselbach suggests that enabling Pre-Boot BitLocker startup
  PIN might require setting "Warning for other disk encryption" to Block, while the
  existing entry does not explicitly state it.]'
- '[CONFLICT: Oliver Kieselbach suggests setting "Warning for other disk encryption"
  to Block when using the AllowStandardUserEncryption setting.]'
- '[CONFLICT: Oliver Kieselbach suggests this might be necessary for Pre-Boot BitLocker
  startup PIN]'
- '[CONFLICT: Jannik Reinhard suggests setting "Disable prompt at sign out" to Enable
  and "Number of times allowed to bypass" to a value other than Not configured.]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-10-23'
  title: Enabling BitLocker on non-HSTI devices with Intune
  url: https://oliverkieselbach.com/2018/10/23/enabling-bitlocker-on-non-hsti-devices-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-08-02'
  title: How to enable Pre-Boot BitLocker startup PIN on Windows with Intune
  url: https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/comment-page-3
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2022-08-17'
  title: Activate Mac FileVault using Intune
  url: https://jannikreinhard.com/2022/08/17/activate-mac-filevault-using-intune
stale_after: '2026-07-13'
title: BitLocker Management via Intune
topic: intune/security/bitlocker-management
---

# BitLocker Management via Intune and Mac FileVault using Intune

This topic discusses the process of enabling BitLocker on non-HSTI devices using Microsoft Intune and Windows 10 version 1809, allowing standard user permissions for encryption, as well as activating Mac FileVault using Intune. The enhancement with Windows 10 version 1809 is that we are able to activate BitLocker with a MDM policy (Intune), even for non-HSTI devices and on Windows 10 Pro Edition. This was not working with Windows 10 version 1803 or lower, and the community came up with custom solutions to handle this like custom PowerShell scripts deployed via Intune Management Extension.

### Key Concepts
- HSTI (Hardware Security Testability Interface)
- MDM policy (Intune)
- BitLocker CSP (BitLocker Configuration Service Provider)
- Enrollment Status Page (ESP)
- Endpoint protection profile
- Custom OMA-URI configuration
- Pre-Boot BitLocker startup PIN (introduced from the new source)
- FileVault (MacOS disk encryption)

### Configuration
1. Ensure the following prerequisites are met:
   - Windows 10 version 1809 Enterprise or Pro
   - Azure Active Directory joined devices
   - Microsoft Intune
   - Enabled Enrollment Status Page (ESP)
   - non-HSTI device

2. Create two configuration policies:
   - An endpoint protection profile that configures silent BitLocker enforcement and other parameters like encryption strength.
   - A custom profile that enforces the BitLocker encryption even when standard users are logging in, and enables Pre-Boot BitLocker startup PIN for pre-boot authentication (introduced from the new source). [CONFLICT: Oliver Kieselbach suggests setting "Warning for other disk encryption" to Block when using the AllowStandardUserEncryption setting.]

3. Set the following settings for the endpoint protection profile:
   - Encrypt devices to Require
   - Warning for other disk encryption to Block ([CONFLICT: Oliver Kieselbach suggests this might be necessary for Pre-Boot BitLocker startup PIN])

4. Configure the custom OMA-URI configuration as follows:
   ```
   OMA-URI: ./Vendor/MSFT/BitLocker/AllowStandardUserEncryption
   Data type: integer
   Value: 1
   ```

### Activate Mac FileVault using Intune

Activating Mac FileVault using Intune involves creating a configuration profile and assigning it to a group in which your MacOS devices are in. The user will receive a popup with the information that the FileVault should be activated, depending on what you have selected as the value for the setting “*Number of times allowed to bypass*“, the encryption is then forced.

[CONFLICT: Jannik Reinhard suggests setting "Disable prompt at sign out" to Enable and "Number of times allowed to bypass" to a value other than Not configured.]

### Common Pitfalls
- Ensuring that the "Warning for other disk encryption" is set to Block when using the AllowStandardUserEncryption setting ([CONFLICT: Oliver Kieselbach suggests this might be necessary for Pre-Boot BitLocker startup PIN])
- When “Disable prompt at sign out” is set to Enable, the “Number of times allowed to bypass” must be set to a value other than Not configured ([Post](https://techcommunity.microsoft.com/t5/intune-customer-success/resolved-known-issue-for-filevault-configuration-profiles-on/ba-p/788542))

### Additional Information (from new source)
The guide will demonstrate how to enable the BitLocker startup PIN for pre-boot authentication on Windows 10 with Microsoft Intune. The key material security is based mainly on the trusted computing platform concepts, including the Endorsement Key and the Sealed Storage concept. In a widely used standard configuration of Microsoft Windows 10, BitLocker is used with a TPM only key protection to protect the operating system and data.

The new source article also explains how to activate Mac FileVault using Intune. Encrypting the disk of a workspace is one of the basic settings that every managed device should have. Everyone who manages Windows PCs knows BitLocker. The solution that is integrated in MacOS to encrypt disks is called FileVault. In this blog, Jannik Reinhard explains how to configure this for MacOs devices.

New source article: "Activate Mac FileVault using Intune"
Author: Jannik Reinhard
New source content: [Content added above]