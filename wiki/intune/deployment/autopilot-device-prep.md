---
conflicts: []
context_note: Autopilot Device Prep is part of the intune domain. Synthesised from
  1 community source.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-07-14'
  title: A default set on assignment Filter
  url: https://jannikreinhard.com/2022/07/14/a-default-set-on-assignment-filter
stale_after: '2026-06-02'
title: Autopilot Device Preparation v2
topic: intune/deployment/autopilot-device-prep
---

# Autopilot Device Preparation v2

## Autopilot Device Preparation v2

### Overview
This topic discusses a script created by Jannik Reinhard to simplify the process of creating a default set of filters for device preparation in Microsoft Intune, specifically for Autopilot v2. The filters allow for more targeted assignment of group configurations, such as applying a configuration profile only on Windows 11 devices within the group.

### Key Concepts
- Default set of filters for device ownership, enrollment profiles, operating system, SKU, and device category in Intune
- Script to create and deploy these default filters
- Filters can be used to refine the assignment of group configurations in Autopilot v2

### Configuration
1. Download the script from Jannik Reinhard's GitHub repository or copy the code provided in the article.
2. Run the script to create the default set of filters.
3. Apply these filters when creating device configuration profiles in Intune.

### Common Pitfalls
- Ensuring that all necessary filters are created and applied correctly to achieve the desired targeting for device configurations.
- Understanding the impact of each filter on the assignment of group configurations.

### KQL / PowerShell
```powershell
<#
Version: 1.0
Author: Jannik Reinhard (jannikreinhard.com)
Script: Deploy-DefaultFilter
Description:
Default set on intune filteer
Release notes:
Version 1.0: Init
#>

[...]
```
### Related Topics
- Device preparation
- Autopilot v2
- APv2
- Device prep policy
- DAP