---
conflict_topics:
- intune/configuration/settings-catalog
- intune/deployment/co-management
conflicts:
- '[CONFLICT: Oliver Kieselbach''s article does not mention custom Azure Automation
  Runbook, which is still part of the existing entry.]'
- '[CONFLICT: Oliver Kieselbach''s article automates this step manually]'
- '[CONFLICT: Oliver Kieselbach''s article still mentions this step manually]'
- '[CONFLICT: Oliver Kieselbach''s article introduces Autopilot Manager, while the
  existing entry does not.]'
- '[CONFLICT: The existing entry does not mention custom Azure Automation Runbook,
  which is still part of the existing entry.]'
- '[CONFLICT: Oliver Kieselbach''s article automates this step using Autopilot Manager]'
context_note: Autopilot User Driven is part of the intune domain. Synthesised from
  6 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-07-17'
  title: Automation of gathering and importing Windows Autopilot information
  url: https://oliverkieselbach.com/2018/07/17/automation-of-gathering-and-importing-windows-autopilot-information
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-07-17'
  title: Automation of gathering and importing Windows Autopilot information
  url: https://oliverkieselbach.com/2018/07/17/automation-of-gathering-and-importing-windows-autopilot-information/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2020-12-08'
  title: Introducing Autopilot Manager
  url: https://oliverkieselbach.com/2020/12/08/autopilot-manager
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2021-12-21'
  title: Evolving Autopilot Manager
  url: https://oliverkieselbach.com/2021/12/21/evolving-autopilot-manager
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-08-24'
  title: Check Autopilot enrollment prerequisite
  url: https://jannikreinhard.com/2022/08/24/check-autopilot-enrollment-prerequisite
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2022-10-14'
  title: Post ESP Intune Win32 apps installations
  url: https://oliverkieselbach.com/2022/10/14/post-esp-intune-win32-apps-installations
stale_after: '2026-06-17'
title: Autopilot User-Driven Mode
topic: intune/deployment/autopilot-user-driven
---

# Autopilot User-Driven Mode

## Autopilot User-Driven Mode
This topic discusses the automation of gathering and importing Windows Autopilot information for devices during a wipe and reload scenario, focusing on user-driven mode. This process is crucial in managing devices that are already running Windows 7 and need to be upgraded to Windows 10 while leveraging Autopilot deployment profiles.

The new source article by Oliver Kieselbach provides additional details about the automation of gathering and importing Windows Autopilot information during a wipe and reload scenario. The process involves using PowerShell Script Get-WindowsAutoPilotInfo, AzCopy, Azure Blob Storage, and now introduces Autopilot Manager as a simplified tool for managing imports ([New Information]).

The existing entry does not mention Autopilot Manager. [CONFLICT: Oliver Kieselbach's article introduces Autopilot Manager, while the existing entry does not.]

## Key Concepts
- Windows Autopilot: A cloud service provided by Microsoft that streamlines the device setup process, making it easier to deploy new devices or reimage existing ones.
- User-Driven Mode: A method of Autopilot deployment where users complete the Out-of-Box Experience (OOBE) to enroll their devices in Intune.
- PowerShell Script Get-WindowsAutoPilotInfo: A script used for gathering hardware information during a wipe and reload scenario.
- AzCopy: A command-line utility for copying blobs, files, and file shares between Azure storage and local or remote filesystems.
- Azure Blob Storage: A service in Microsoft Azure that provides an object store for storing large amounts of unstructured data.
- Autopilot Manager: A simplified tool for managing Windows Autopilot imports using a small client program and an Azure app service ([New Information]).
- [CONFLICT: The existing entry does not mention custom Azure Automation Runbook, which is still part of the existing entry.]

## Configuration
1. Install the PowerShell Script Get-WindowsAutoPilotInfo on devices running Windows 7.
2. Run the script during a wipe and reload scenario to gather hardware information.
3. Use AzCopy to upload the generated .csv file to an Azure Blob Storage container.
4. Write a custom Azure Automation Runbook to combine multiple .csv files from Azure Blob Storage into a single combined.csv file ([CONFLICT: Oliver Kieselbach's article automates this step using Autopilot Manager]). **OR** [New Information] Use Autopilot Manager for simplified imports and combining multiple .csv files.
5. Upload the combined .csv file to Autopilot and assign Deployment Profiles.
6. Deliver the devices to end users for user-driven enrollment in Intune.
7. Optionally, use Autopilot Manager for simplified imports ([New Information]).

## Customizable Timeout (New Information)
Autopilot Manager allows you to configure the caching timeout value, which can be customized to meet your organization's needs. The default is 60 minutes but can be adjusted as needed.

To conf

## Post ESP Intune Win32 apps installations (New Information)
In enterprise environments, we have to deal with a lot of requirements when it comes to app management. One of the common challenges is to control the installation moment during enrollment. We already have some basic controls in place. If the [Enrollment Status Page (ESP)](https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enrollment-status?WT.mc_id=EM-MVP-5003177) is configured during the enrollment all device targeted apps are installed in the “Device Setup” phase and all the user targeted apps are installed in the “Account Setup” phase. These are simple moments in time already. But what if you would like to schedule the installation after ESP when the Desktop is fully available and displayed?

The goal is to let a required Win32 app deployed via Intune install only if the ESP is not running anymore. Why? Maybe because we want to display a dialog for user interaction and this is only possible when the Desktop is fully loaded, otherwise the dialog will be hidden behind the ESP and can’t be interacted with. Resulting in an ESP waiting infinitely for an app which is hidden in the background :-(.

In fact, I needed this for my BitLocker PIN solution ([How to enable Pre-Boot BitLocker startup PIN on Windows with Intune](https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/)) already in the past but didn’t come up with a good idea how to solve it in a reliable way.

Now I gave it another try and solved it by doing the following.

**UPDATE 10/20/202:**

*The following approach worked well in my test environment, but not during the final implementation! The initial idea is used somewhere else where it is working successfully with a different precondition, but in the Autopilot requirement script, there is one caveat I found after releasing the blog. The following paragraphs still describe the way I approached the problem and finally also the issue discovered later with it. If you want to jump to the final solution, [click here](#changedapproach).*

Similar to the [Win32 App Requirement Script](https://docs.microsoft.com/en-us/mem/intune/apps/apps-win32-add#step-3-requirements?WT.mc_id=EM-MVP-5003177) for Primary User Detection ([Deploy an Intune application with user device affinity](https://oliverkieselbach.com/2022/08/30/deploy-an-intune-application-with-user-device-affinity/)) I wrote a Win32 App Requirement Script to detect the running ESP. The script is looking for the **WWAHost** process which is responsible for UWP apps to run JavaScript code. The ESP is based on a UWP app implementation using JavaScript. To accomplish this task, the **WWAHost** has to load the **CloudExperienceHost** Module for this to actually display the ESP to the user. So, if the **WWAHost** is running and has the 

This new section provides information about scheduling Win32 app installations after the Enrollment Status Page (ESP) is no longer running. It discusses a method of controlling the installation moment during enrollment and solving issues related to user interaction with dialogs hidden behind the ESP.