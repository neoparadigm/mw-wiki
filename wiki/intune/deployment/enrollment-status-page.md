---
conflicts: []
context_note: Enrollment Status Page is part of the intune domain. Synthesised from
  1 community source.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-10-02'
  title: How to skip the ESP for a single app installation
  url: https://jannikreinhard.com/2022/10/02/how-to-skip-the-esp-for-a-single-app-installation
stale_after: '2026-06-17'
title: Enrollment Status Page Configuration
topic: intune/deployment/enrollment-status-page
---

# Enrollment Status Page Configuration

## Enrollment Status Page Configuration

This topic discusses how to skip the ESP (Enrollment Status Page) for a single app installation in Intune, a scenario where it may be necessary to install an app after the ESP due to installation requirements that necessitate user interaction.

## Key Concepts
- ESP (Enrollment Status Page)
- App installation during ESP or white glove phase
- Detecting if in ESP
- Requirement script for skipping ESP

## Configuration
1. Write a requirement script to detect if in ESP:
   - Option 1: Check the user running the explorer process (`Get-EspDetection` script provided)
   - Option 2: Check registry keys in "Computer\HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Provisioning\AutopilotSettings" (`Get-EspDetection` script provided)

2. Upload the requirement script to the MEM portal, navigate to the app you want to skip the ESP, click **Edit** and **Requirements**, then add a new requirement rule with the uploaded script.
   - Select **Script**
   - Upload the **Requirement script**
   - Select **Boolean** as “*Select output data type*“
   - Operator: **Equals**
   - Value: **No**

## Common Pitfalls
- Failing to properly detect if in ESP can lead to apps being installed during ESP, potentially causing issues or delays.

## KQL / PowerShell
```powershell
# Option 1 (Get-EspDetection script)
<#
Version: 1.0
Author: Jannik Reinhard (jannikreinhard.com)
Script: Get-EspDetection
Description:
Skip the ESP for app installation
Release notes:
Version 1.0: Init
#>

... (script provided in the source article)

# Option 2 (Get-EspDetection script)
<#
Version: 1.0
Author: Jannik Reinhard (jannikreinhard.com)
Script: Get-EspDetection
Description:
Skip the ESP for app installation
Release notes:
Version 1.0: Init
#>

... (script provided in the source article)
```

## Related Topics
- ESP
- Enrollment status page
- Blocking apps
- Timeout
- ESP error