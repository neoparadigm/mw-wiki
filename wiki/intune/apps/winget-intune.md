---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests using SyncML Viewer via Winget, while the
  existing entry does not mention this method.]'
- '[CONFLICT: Anoop C Nair says X, existing entry says Y]'
- '[CONFLICT: Anoop C Nair provides a new method for installing Speech Packs using
  Microsoft Intune, while the existing entry does not mention this method.]'
- '[CONFLICT: Anoop C Nair introduces Natural Voice Packs as standalone apps in the
  Microsoft Store, while the existing entry does not mention this concept.]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2022-12-11'
  title: Deploy Windows Store Apps via Intune
  url: https://jannikreinhard.com/2022/12/11/deploy-windows-store-apps-via-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2024-03-04'
  title: SyncML Viewer via Winget
  url: https://oliverkieselbach.com/2024/03/04/syncml-viewer-via-winget
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2025-06-06'
  title: How To Configure App Data Sharing Using SharedLocal Folder In Windows 10
    With Intune Policy HTMD Blog
  url: https://www.anoopcnair.com/app-data-sharing-folder-in-windows-10-intune
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2025-03-11'
  title: Easy Method To Install Speech Pack Using Microsoft Intune HTMD Blog
  url: https://www.anoopcnair.com/install-speech-pack-using-microsoft-intune
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2026-03-11'
  title: Microsoft Intune Expands Windows Settings Catalog With Silent Printing Geolocation
    And Windows Restore Settings HTMD Blog
  url: https://www.anoopcnair.com/intune-expands-windows-settings-catalog
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2025-05-08'
  title: Simple Method To Deploy Natural Voice Pack To Windows 11 Using Intune HTMD
    Blog
  url: https://www.anoopcnair.com/natural-voice-pack-to-windows-11-using-intune
stale_after: '2026-05-29'
title: WinGet and Microsoft Store Integration
topic: intune/apps/winget-intune
---

# WinGet and Microsoft Store Integration

## Overview
This topic discusses deploying Windows Store Apps via Intune using WinGet and Microsoft Store integration, making it easier to manage app deployment on Windows devices. Additionally, it now includes information about installing SyncML Viewer via the Windows Package Manager (Winget), configuring App Data Sharing Using SharedLocal Folder In Windows 10 With Intune Policy, a new method for installing Speech Packs using Microsoft Intune, updates to the Windows Settings Catalog, and a simple method for deploying Natural Voice Packs to Windows 11 using Intune.

## Key Concepts
- WinGet: A command-line package manager for Windows that allows users to discover, install, upgrade, and remove applications.
- Microsoft Store Integration in Intune: Allows the installation of apps directly from the Microsoft Store within the Intune console.
- Winget: An open-source package manager for Windows that simplifies the installation of various applications.
- Shared Local Folder: A folder available through the `Windows.Storage` API used for sharing app data between users on the same device.
- Speech Packs: Add-ons that enhance speech recognition and text-to-speech capabilities for different languages, available in multiple languages such as English (US, UK, Canada, Australia), French, Spanish, German, Italian, Chinese (Simplified & Traditional), Japanese, Korean, Arabic, Hindi, Portuguese, etc.
- Silent Printing: A feature in Microsoft Edge that allows administrators to control automatic printing on managed devices.
- Geolocation: The ability for websites to access location data on managed devices.
- Windows Restore Policy: Allows users to restore their Windows settings and Microsoft Store apps from the cloud when setting up a new or reset device.
- Natural Voice Packs: Standalone apps in the Microsoft Store that provide human-like, expressive, and intelligible text-to-speech (TTS) experiences for Windows 11 devices. [New information from Anoop C Nair]

## Configuration
1. Open the Intune Console (<https://endpoint.microsoft.com/#home>)
2. Navigate to Apps -> Windows
3. Select **+ Add**
4. Select **Microsoft Store app (new)** -> **Select**
5. Click **Search the Microsoft Store app (new)**
6. Search for the desired app and click **Select**
7. Adapt the app information (optional)
8. Create a required or available assignment
9. Click create
10. To install SyncML Viewer via Winget, open a command prompt and type: `winget install SyncMLViewer`
11. To configure App Data Sharing Using SharedLocal Folder In Windows 10 With Intune Policy, follow the steps outlined in [How To Configure App Data Sharing Using SharedLocal Folder In Windows 10 With Intune Policy HTMD Blog](https://www.anoopcnair.com/2024/03/04/configure-app-data-sharing-using-sharedlocal-folder-in-windows-10-with-intune-policy-htmd-blog/)
12. To install Speech Packs using Microsoft Intune, follow the steps outlined in "Easy Method To Install Speech Pack Using Microsoft Intune HTMD Blog" by Anoop C Nair. [New information from Anoop C Nair]
13. To enable Silent Printing in Edge, follow the steps outlined in "[Enable Silent Printing in Edge Browser using Microsoft 365 Admin Center Policy](https://www.anoopcnair.com/silent-printing-in-edge-policy-)"
14. To deploy Natural Voice Packs to Windows 11, follow the steps outlined in "Simple Method To Deploy Natural Voice Pack To Windows 11 Using Intune HTMD Blog" by Anoop C Nair. [New information from Anoop C Nair]

[CONFLICT: Anoop C Nair provides a new method for installing Speech Packs using Microsoft Intune, while the existing entry does not mention this method.]
[CONFLICT: Anoop C Nair introduces Natural Voice Packs as standalone apps in the Microsoft Store, while the existing entry does not mention this concept.]