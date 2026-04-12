---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests monitoring policy changes for a certain set
  of policies, while the existing entry does not mention this specifically for PAW
  policies.]'
- '[CONFLICT: Jannik Reinhard''s article suggests using a PowerShell script to generate
  a weekly report for all newly enrolled devices via email, while the existing entry
  does not mention this.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-01-13'
  title: Using Windows 365 for Cloud Based Privileged Access Workstations (PAW)
  url: https://danielchronlund.com/2022/01/13/using-windows-365-for-cloud-based-privileged-access-workstations-paw
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2019-04-23'
  title: On-demand Windows Diagnostic Logs via Intune
  url: https://oliverkieselbach.com/2019/04/23/on-demand-windows-diagnostic-logs-via-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2019-04-23'
  title: On-demand Windows Diagnostic Logs via Intune
  url: https://oliverkieselbach.com/2019/04/23/on-demand-windows-diagnostic-logs-via-intune
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2022-07-19'
  title: Monitoring Intune policy configuration changes
  url: https://oliverkieselbach.com/2022/07/19/monitoring-intune-policy-configuration-changes
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-08-01'
  title: Introduction of the Intune App Creator with help of Chocolatey
  url: https://jannikreinhard.com/2022/08/01/introduction-of-the-chocolatey-intune-app-creator
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2023-03-19'
  title: How to get an report with all new enrolled devices
  url: https://jannikreinhard.com/2023/03/19/how-to-get-an-report-with-all-new-enrolled-devices
stale_after: '2026-07-11'
title: Tiered Administration Model T0 T1 T2
topic: identity/pim/tiered-administration
---

# Tiered Administration Model T0 T1 T2

## Tiered Administration Model T0 T1 T2

### Overview
The Enterprise Access model is Microsoft's new approach to security, focusing on cloud and hybrid scenarios for modern IT security. This model is used to create a privileged access plane where Windows 365 cloud PCs act as jump servers for both cloud management and on-prem management, specifically in the context of Privileged Access Workstations (PAW).

### Key Concepts
- Windows 365 PAWs acting as jump servers for various management tools and portals.
- Strict policy hardening using Microsoft security baselines, Defender Attack Surface Reduction rules, Application Control, Defender SmartScreen, and separate cloud-only admin accounts with their own Windows 365 licenses and cloud PCs.
- [On-demand Windows Diagnostic Logs via Intune](#on-demand-windows-diagnostic-logs-via-intune) for troubleshooting devices in a modern managed environment (Prerequisites: Windows Insider or Windows 10 Version 1903 which includes the DiagnosticLog CSP in Version 1.4).
- [On-demand Windows Diagnostic Logs via Intune](#on-demand-windows-diagnostic-logs-via-intune-new) (New source content) - In a modern managed environment, it is possible to gather on-demand diagnostic log files from Windows 10 devices via the MDM channel.
- [On-demand Windows Diagnostic Logs via Intune](#on-demand-windows-diagnostic-logs-via-intune-new-procedure) (New procedure source content) - The procedure involves specifying a data collection XML structure, providing cloud storage and SAS URI for upload, and MDM server sends the data collection and upload URI to the device.
- [Monitoring Intune policy configuration changes](#monitoring-intune-policy-configuration-changes) (New source article by Oliver Kieselbach) - In a lot of Microsoft Intune environments, there is often the requirement to monitor configuration changes and take action based on changes. This section provides guidance on using Log Analytics and Azure Monitor to monitor policy changes for a certain set of policies.
- [Introduction of the Intune App Creator with help of Chocolatey](#introduction-of-the-intune-app-creator-with-help-of-chocolatey) (New source article by Jannik Reinhard) - This tool simplifies the process of creating and deploying apps in Microsoft Intune. It allows you to search within the >9,000 Chocolatey packages and automatically add this app to your Intune app portfolio with just one click.
- [How to get an report with all new enrolled devices](#how-to-get-an-report-with-all-new-enrolled-devices) (New source article by Jannik Reinhard) - This PowerShell script retrieves all devices enrolled in the last 7 day and create a csv out of it and attached this csv to a Email.

### Configuration
- Important: Careful scoping of PAW management and the Windows 365 service in Intune.
- Strict Windows 11 policy hardening using Microsoft security baselines and a custom policy.
- Enable all Defender Attack Surface Reduction rules with Intune.
- Enable Application Control for Windows (WDAC or AppLocker) and block any unwanted applications.
- Use strict Defender SmartScreen blocking to allow required management portal and API URLs and endpoints.
- Ensure admins use separate cloud-only admin accounts, each with their own Windows 365 licenses and cloud PCs. [CONFLICT: Jannik Reinhard's article suggests using a PowerShell script to generate a weekly report for all newly enrolled devices via email, while the existing entry does not mention this.]

[On-demand Windows Diagnostic Logs via Intune]: #on-demand-windows-diagnostic-logs-via-intune
[On-demand Windows Diagnostic Logs via Intune (New source content)]: #on-demand-windows-diagnostic-logs-via-intune-new
[On-demand Windows Diagnostic Logs via Intune (New procedure source content)]: #on-demand-windows-diagnostic-logs-via-intune-new-procedure
[Monitoring Intune policy configuration changes]: #monitoring-intune-policy-configuration-changes
[Introduction of the Intune App Creator with help of Chocolatey]: #introduction-of-the-intune-app-creator-with-help-of-chocolatey
[How to get an report with all new enrolled devices]: #how-to-get-an-report-with-all-new-enrolled-devices