---
conflicts: []
context_note: Macos Security is part of the intune domain. Synthesised from 1 community
  source.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-08-17'
  title: Activate Mac FileVault using Intune
  url: https://jannikreinhard.com/2022/08/17/activate-mac-filevault-using-intune
stale_after: '2026-06-17'
title: macOS Security and Compliance with Intune
topic: intune/security/macos-security
---

# macOS Security and Compliance with Intune

## Overview
This topic discusses how to activate macOS FileVault using Intune for enhanced security and compliance of managed devices. Encrypting the disk is a basic setting that every managed device should have, and this blog explains how to configure it for MacOS devices.

## Key Concepts
- MEM Portal: Microsoft Endpoint Manager portal used to create configuration profiles.
- Configuration Profile: A set of policies and settings applied to manage devices.
- FileVault: macOS built-in disk encryption solution.
- Personal Recovery Key: A key required to decrypt the encrypted disk in case of data loss or device theft.
- Escrow location description of personal recovery key: The method for retrieving the personal recovery key for your macOS device from Microsoft Intune, Company Portal website, or Company Portal apps for Android and iOS/iPadOS.
- Number of times allowed to bypass: The number of times a user can bypass the FileVault prompt before it is forced.

## Configuration
1. Open the MEM Portal (<https://endpoint.microsoft.com/>).
2. Navigate to **Devices** -> **Configuration profiles**.
3. Click **+ Create profile**.
4. Select **macOS** as *Platform* and **Templates** as *Profile type*.
5. Select Endpoint protection.
6. Enter a Name and configure FileVault settings as desired or specified by the security department.
7. Assign the Configuration profile to a group containing your MacOS devices.
8. Click **Next** > **Create**.

## Common Pitfalls
- When Disable prompt at sign out is set to Enable, the Number of times allowed to bypass must be set to a value other than Not configured.

## KQL / PowerShell
Not applicable in this article.

## Related Topics
- macOS security
- Mac compliance
- macOS LAPS (if discussing device management and password policies)
- FileVault
- Gatekeeper (if discussing app security and permissions)