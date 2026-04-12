---
conflicts:
- '[CONFLICT: Oliver Kieselbach does not mention this]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-12-11'
  title: Deploy Windows Store Apps via Intune
  url: https://jannikreinhard.com/2022/12/11/deploy-windows-store-apps-via-intune
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2024-03-04'
  title: SyncML Viewer via Winget
  url: https://oliverkieselbach.com/2024/03/04/syncml-viewer-via-winget
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2025-06-06'
  title: How To Configure App Data Sharing Using SharedLocal Folder In Windows 10
    With Intune Policy HTMD Blog
  url: https://www.anoopcnair.com/app-data-sharing-folder-in-windows-10-intune
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-03-12'
  title: Microsoft Introduces Windows Backup For Organizations With Secure Backup
    And Quick Restore HTMD Blog
  url: https://www.anoopcnair.com/introduces-windows-backup-for-organizations
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-03-11'
  title: Microsoft Intune Expands Windows Settings Catalog With Silent Printing Geolocation
    And Windows Restore Settings HTMD Blog
  url: https://www.anoopcnair.com/intune-expands-windows-settings-catalog
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2025-06-09'
  title: How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune
    Policy HTMD Blog
  url: https://www.anoopcnair.com/lock-option-in-user-tile-menu-on-windows-intune
stale_after: '2026-05-27'
title: WinGet and Microsoft Store Integration
topic: intune/apps/winget-intune
---

# WinGet and Microsoft Store Integration

## Overview
This topic discusses the deployment of Windows Store Apps via Intune, utilizing the WinGet command-line package manager for Windows and the new Microsoft Store integration in Intune. This method simplifies the process of deploying apps via Intune by providing access to all apps available in the winget repository through a large software catalog in Intune.

Additionally, it has been noted that SyncML Viewer is now available through the official [Windows Package Manager Community Repository](https://github.com/microsoft/winget-pkgs/tree/master) (winget). The installation command is `winget install SyncMLViewer`.

## Key Concepts
- WinGet: A command-line package manager for Windows that allows users to discover, install, upgrade, and remove applications on their Windows devices. [CONFLICT: Oliver Kieselbach does not mention this]
- Microsoft Store integration in Intune: A feature that enables the deployment of apps from the Microsoft Store directly through Intune.
- Shared Local Folder (New addition): A shared folder available through the `Windows.Storage` API, used for app data sharing between users on the same device. [Source: Anoop C Nair]
- Windows Backup for Organizations (New addition, from Anoop C Nair): A feature that helps restore user settings on new devices, supporting both Windows 10 and Windows 11 devices. User settings like personalization, accessibility, and Start menu layout can be backed up. Backups are encrypted and stored securely in the user’s Entra ID cloud profile.
- Silent Printing (New addition, from Microsoft Intune Expands Windows Settings Catalog): A policy that allows administrators to control automatic printing in Microsoft Edge.
- Geolocation Policies (New addition, from Microsoft Intune Expands Windows Settings Catalog): A policy that enables or blocks location data access for specific websites on managed devices.
- Windows Restore Policy (New addition, from Microsoft Intune Expands Windows Settings Catalog): A policy that allows users to restore their Windows settings and Microsoft Store apps from the cloud when setting up a new or reset device.
- Show/Hide Lock Option in User Tile Menu (New addition, from How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune Policy HTMD Blog): A policy that allows administrators to control whether the lock option appears in the user tile menu on Windows devices. If enabled, it’s shown; if disabled, it’s hidden; if not configured, users can choose via the Power Options Control Panel.

## Configuration
1. Open the Intune Console.
2. Navigate to Apps -> Windows.
3. Select **+ Add**.
4. Choose **Microsoft Store app (new)** and click **Select**.
5. Click **Search the Microsoft Store app (new)**, search for the desired app, select it, adapt the app information if necessary, create a required or available assignment, and then click **Create**.

## Common Pitfalls
- Ensuring that the selected app is compatible with the target devices and their configurations.
- Properly configuring the app assignment (required or available) to ensure it is deployed effectively.
- Ensuring that Shared Local Folder policy is configured correctly for app data sharing between users on the same device. [Source: Anoop C Nair]
- Ensuring that Windows Backup for Organizations is properly configured and used for backing up and restorin
- Ensuring that Show/Hide Lock Option in User Tile Menu policy is configured correctly to control whether the lock option appears in the user tile menu. [Source: How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune Policy HTMD Blog]

New source article: "How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune Policy HTMD Blog"
Author: Anoop C Nair
New source content:
[...]
# How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune Policy HTMD Blog

[...]
- Show/Hide Lock Option in User Tile Menu (New addition, from How To Show Or Hide Lock Option In User Tile Menu On Windows Using Intune Policy HTMD Blog): A policy that allows administrators to control whether the lock option appears in the user tile menu on Windows devices. If enabled, it’s shown; if disabled, it’s hidden; if not configured, users can choose via the Power Options Control Panel.
[...]