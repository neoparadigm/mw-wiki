---
conflict_topics:
- intune/apps/powershell-scripts
- intune/compliance/compliance-policy-design
conflicts:
- '[CONFLICT: Oliver Kieselbach provides an example of a specific application being
  available via winget, while the existing entry does not mention this method.]'
- '[CONFLICT: Oliver Kieselbach provides specific instructions for SyncML Viewer installation
  and usage via winget, while the existing entry does not mention this method.]'
- '[CONFLICT: Anoop C Nair provides more detailed information about the integration
  between Microsoft Intune and the Microsoft Store, while Oliver Kieselbach''s example
  of SyncML Viewer installation and usage via winget is not mentioned in the new source.]'
context_note: Winget Intune is part of the intune domain. Synthesised from 5 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-12-11'
  title: Deploy Windows Store Apps via Intune
  url: https://jannikreinhard.com/2022/12/11/deploy-windows-store-apps-via-intune
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2024-03-04'
  title: SyncML Viewer via Winget
  url: https://oliverkieselbach.com/2024/03/04/syncml-viewer-via-winget
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2022-11-30'
  title: Simon does The new Microsoft Store Experience
  url: https://skotheimsvik.no/the-new-microsoft-store-experience
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2024-08-07'
  title: Windows Package Manager Now Supports Downloading Packaged Apps From Microsoft
    Store And Install Using WCD HTMD Blog
  url: https://www.anoopcnair.com/windows-package-manager-supports-download-apps
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2024-09-16'
  title: 'Simon does WinTuner: The Ultimate Fix For Microsoft Store App Problem!'
  url: https://skotheimsvik.no/wintuner-the-ultimate-fix-for-microsoft-store-app-problem
stale_after: '2026-06-02'
title: WinGet and Microsoft Store Integration
topic: intune/apps/winget-intune
---

# WinGet and Microsoft Store Integration

## Overview
This topic discusses how to deploy Windows Store Apps via Intune using WinGet and the new Microsoft Store integration. This feature simplifies the process of deploying apps by providing a large software catalog in Intune, eliminating the need for cumbersome app packaging. Additionally, it has been noted that some applications can now be installed directly through the Windows Package Manager Community Repository (winget) using simple commands, such as SyncML Viewer with `winget install SyncMLViewer`. [CONFLICT: Oliver Kieselbach provides an example of a specific application being available via winget, while the existing entry does not mention this method.]

## Key Concepts
- WinGet: A command-line package manager for Windows that allows users to discover, install, upgrade, and remove applications on their Windows devices.
- Microsoft Store integration in Intune: A feature that enables the deployment of apps directly from the Microsoft Store within the Intune console.
- winget: An open-source package manager for Windows that provides a community repository for various applications. [New]
- WinTuner: A tool developed by MVP Stephan van Rooij to package any app from Winget to Intune, particularly useful when dealing with apps like Adobe Creative Cloud that may have missing version information in the Microsoft Store. [New: Simon Skotheimsvik]

## Configuration
[...] (Existing configuration steps)

## Common Pitfalls
- Ensuring that the selected app is compatible with Windows Store integration in Intune.
- Properly configuring the app assignment to meet your organization's requirements (required vs available).
- Ensuring compatibility and proper installation of applications installed via winget. [New]
- Understanding that while Microsoft has confirmed discussions about deploying Win32 apps from winget source via Intune, it is not currently part of their roadmap or plan. [New: Anoop C Nair]
- Addressing issues with missing latest package versions in the Microsoft Store for certain applications, such as Adobe Creative Cloud. In such cases, WinTuner can be used to package and prepare the application. [New: Simon Skotheimsvik]

## KQL / PowerShell
The article does not provide any specific queries or scripts related to KQL or PowerShell, but it is important to note that some applications installed via winget may require additional PowerShell scripts for management and configuration. [New]

## Related Topics
- WinGet
- Microsoft Store
- UWP (Universal Windows Platform)
- winget (Open-source package manager for Windows) [New]
- WinTuner (A tool to package apps from Winget to Intune) [New: Simon Skotheimsvik]

## Additional Information from New Sources
The new sources provide more detailed information about the integration between Microsoft Store, Intune, and winget, as well as a practical workaround for addressing issues with missing latest package versions in the Microsoft Store using WinTuner.

New source article: "Simon does WinTuner: The Ultimate Fix For Microsoft Store App Problem!"
Author: Simon Skotheimsvik