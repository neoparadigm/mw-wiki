---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests that in future the hardware information will
  be synced into our tenant from the OEM vendor.]'
- '[CONFLICT: Oliver Kieselbach says X, existing entry says Y]'
- '[CONFLICT: The existing entry does not mention telemetry levels for Device Health]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-15'
  title: Gather Windows 10 Autopilot info in Azure Blob Storage during wipe and reload
  url: https://oliverkieselbach.com/2017/11/16/gather-windows-10-autopilot-info-in-azure-blob-storage-during-wipe-and-reload
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-15'
  title: Gather Windows 10 Autopilot info in Azure Blob Storage during wipe and reload
  url: https://oliverkieselbach.com/2017/11/16/gather-windows-10-autopilot-info-in-azure-blob-storage-during-wipe-and-reload/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-07-17'
  title: Automation of gathering and importing Windows Autopilot information
  url: https://oliverkieselbach.com/2018/07/17/automation-of-gathering-and-importing-windows-autopilot-information
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-07-17'
  title: Automation of gathering and importing Windows Autopilot information
  url: https://oliverkieselbach.com/2018/07/17/automation-of-gathering-and-importing-windows-autopilot-information/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-03-28'
  title: Windows Analytics onboarding with Intune
  url: https://oliverkieselbach.com/2019/03/28/windows-analytics-onboarding-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-03-28'
  title: Windows Analytics onboarding with Intune
  url: https://oliverkieselbach.com/2019/03/28/windows-analytics-onboarding-with-intune
stale_after: '2026-06-13'
title: Autopilot User-Driven Mode
topic: intune/deployment/autopilot-user-driven
---

# Autopilot User-Driven Mode

## Autopilot User-Driven Mode

Autopilot User-Driven Mode is a feature in Windows 10 that allows for user-driven enrollment of devices during the Out-of-Box Experience (OOBE). This mode provides a managed way of provisioning with near zero touch, enabling IT to control the end-user experience during the enrollment process.

## Key Concepts
- Autopilot User-Driven Mode
- Device Serial Number
- Windows Product ID
- Hardware Hash
- Azure AD Join
- Windows as a Service (WaaS)
- OEM vendor
- MDT (Microsoft Deployment Toolkit)
- [Azure Blob Storage](#Gather-Windows-10-Autopilot-info-in-Azure-Blob-Storage-during-wipe-and-reload)
- [Automation of gathering and importing Windows Autopilot information](#Automation-of-gathering-and-importing-Windows-Autopilot-information)
- **[Windows Analytics](#Windows-Analytics-onboarding-with-Intune)** (New Source)

## Configuration
1. Gather the necessary device information: Device Serial Number, Windows Product ID, and Hardware Hash.
2. Upload this information to the Autopilot service. [CONFLICT: Oliver Kieselbach suggests that in future the hardware information will be synced into our tenant from the OEM vendor.]
3. During OOBE, the device will be recognized as an Autopilot device and show a customized enrollment experience.
4. To deploy this on existing Windows 7 devices, create a Deployment USB media using MDT and build a Standard Task Sequence to deploy Windows 10.
5. For automation of gathering and importing Windows Autopilot information:
   - Gather hardware information via PowerShell Script `Get-WindowsAutoPilotInfo` during wipe and reload
   - Upload .csv file via AzCopy to an Azure Blob Storage
   - Gather .csv files from Azure Blob Storage and combine them into a single combined.csv file
   - Upload combined .csv file to Autopilot and assign Deployment Profiles

## Common Pitfalls
- Incorrect or incomplete device information may cause issues with device recognition during the Autopilot process.
- Ensuring that all necessary drivers are installed before enrollment is crucial for a smooth deployment process.

## Gather Windows 10 Autopilot info in Azure Blob Storage during wipe and reload (New)
[Gather Windows 10 Autopilot info in Azure Blob Storage during wipe a

New source article: "Windows Analytics onboarding with Intune"
Author: Oliver Kieselbach
New source content:

## Windows Analytics onboarding with Intune

Windows Analytics provides a key component in a modern managed environment. If we use [Windows Update for Business](https://docs.microsoft.com/en-us/windows/deployment/update/waas-manage-updates-wufbhttps://docs.microsoft.com/en-us/windows/deployment/update/windows-analytics-overview?WT.mc_id=EM-MVP-5003177) we have no way of monitoring key performance metrics of our environment without Windows Analytics.

Windows Analytics – Update Compliance Overview

Windows Analytics is based on an [Azure Monitor Log Analytics](https://docs.microsoft.com/en-us/azure/azure-monitor/log-query/get-started-portalhttps://docs.microsoft.com/en-us/windows/deployment/update/windows-analytics-overview?WT.mc_id=EM-MVP-5003177) instance which provides three key solutions.

[Update Compliance](https://docs.microsoft.com/en-us/windows/deployment/update/update-compliance-get-startedhttps://docs.microsoft.com/en-us/windows/deployment/update/windows-analytics-overview?WT.mc_id=EM-MVP-5003177) to monitor Quality Updates, Features Updates and Delivery Optimization performance.

Update Compliance

**Upgrade Readiness** is used to get insights into your app environment and to plan a mitigation strategy for successful feature upgrades.

Upgrade Readiness

**Device Health** is used to gather crash data to get proactive and resolve app and drivers issues in your environment.

Device Health

**UPDATE**: [Retirement of Windows Analytics in favor of Desktop Analytics on January 31st, 2020](https://techcommunity.microsoft.com/t5/Desktop-Analytics-Blog/Migrate-user-input-data-from-Windows-Analytics-Upgrade-Readiness/ba-p/841744) – **Update Compliance will stay**!!!

To get the client data into the Log Analytics instance to let the Windows Analytics solutions provide you the insights, we need to onboard our corporate clients. To setup Log Analytics with the Windows Analytics solutions follow this Microsoft article [Windows Analytics in the Azure Portal](https://docs.microsoft.com/en-us/windows/deployment/update/windows-analytics-azure-portal). In this guide I will walk through the MDM settings set by Microsoft Intune. Keep in mind that these settings can also be controlled with GPOs which we will not show here. We will look at every setting and the pitfalls they may have and how to overcome these. This is a guide for corporate devices, for personal devices you might want different settings and more control for the user. In a corporate device scenario you take control over the settings.

The first and most important setting is the telemetry level which needs to be set to Basic to enable Windows Update for Business and to get Update Compliance and Upgrade Readiness to work. For the Device Health we need more data to support this solution (e.g. crash data of apps) and this requires telemetry level  [CONFLICT: The existing entry does not mention telemetry levels for Device Health]

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: Oliver Kieselbach says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.