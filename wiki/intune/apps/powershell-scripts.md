---
conflicts:
- '[CONFLICT: Oliver Kieselbach mentions the ability to deploy basic MSI packages
  via MDM OMA-DM channel, but this is not explicitly mentioned in the existing entry]'
- '[CONFLICT: Oliver Kieselbach mentions that the device must be AAD joined and the
  automatic MDM enrollment must be enabled, but this is not explicitly mentioned in
  the existing entry]'
- '[CONFLICT: Oliver Kieselbach does not mention specific pitfalls in his article]'
- '[CONFLICT: Oliver Kieselbach adds MSI packages via MDM OMA-DM channel as a related
  topic, but this is not explicitly mentioned in the existing entry]'
- '[CONFLICT: Oliver Kieselbach mentions this, but it was not explicitly mentioned
  in the existing entry]'
- '[CONFLICT: Oliver Kieselbach adds this as a related topic, but it was not explicitly
  mentioned in the existing entry]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-29'
  title: November 2017 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2017/11
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-28'
  title: Deep dive Microsoft Intune Management Extension &#8211; PowerShell Scripts
  url: https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-28'
  title: Deep dive Microsoft Intune Management Extension &#8211; PowerShell Scripts
  url: https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-02-12'
  title: Part 2, Deep dive Microsoft Intune Management Extension &#8211; PowerShell
    Scripts
  url: https://oliverkieselbach.com/2018/02/12/part-2-deep-dive-microsoft-intune-management-extension-powershell-scripts/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-02-12'
  title: Part 2, Deep dive Microsoft Intune Management Extension &#8211; PowerShell
    Scripts
  url: https://oliverkieselbach.com/2018/02/12/part-2-deep-dive-microsoft-intune-management-extension-powershell-scripts
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-02-25'
  title: Process automation for Intune and Azure AD with Azure Automation
  url: https://oliverkieselbach.com/2018/02/25/process-automation-for-intune-and-azure-ad-with-azure-automation
stale_after: '2026-06-13'
title: PowerShell Scripts in Intune
topic: intune/apps/powershell-scripts
---

# PowerShell Scripts in Intune

## Overview
PowerShell Scripts in Intune is a modern IT strategy that allows for the management and execution of PowerShell scripts on Windows 10 devices using Microsoft's Intune Management Extension (IME). This approach addresses limitations like custom configurations or Win32 App installs, making it an essential tool for streamlining IT operations.

Microsoft made a big step forward in the Modern Management field. Limitations like custom configurations or even Win32 App installs can be addressed now. Microsoft developed an EMS agent (aka SideCar) and released it as a new Intune feature called [Intune Management Extension](https://docs.microsoft.com/en-us/intune/intune-management-extension). This agent is able to [manage and execute PowerShell scripts](https://docs.microsoft.com/en-us/intune/intune-management-extension) on Windows 10 devices and it does this quite well.

## Key Concepts
- Intune Management Extension (IME)
- PowerShell scripts execution on Windows 10 devices
- Microsoft EMS agent (SideCar)
- Configuring and managing policies via OMA-URIs in Intune
- Deploying basic MSI packages via MDM OMA-DM channel [CONFLICT: Oliver Kieselbach mentions this, but it was not explicitly mentioned in the existing entry]
- Details of the MSI deployment of the Intune Management Extension agent? (see below)
- Azure Automation for process automation with Intune and Azure AD [NEW: from Oliver Kieselbach's article]

## Configuration
1. Install the Intune Management Extension on your Windows 10 device.
2. Configure PowerShell scripts as Intune Win32 apps.
3. Assign the script to a group of devices or users within the Intune console.
4. Monitor the execution status and results of the PowerShell scripts in the Intune console.
5. The device must be AAD joined and the automatic MDM enrollment must be enabled [CONFLICT: Oliver Kieselbach mentions this, but it was not explicitly mentioned in the existing entry]
6. For process automation with Azure Automation, set up the Azure environment and create a Runbook to perform tasks like deleting old devices from Intune and Azure AD [NEW: from Oliver Kieselbach's article]

## Common Pitfalls
- Ensuring that the PowerShell scripts are properly formatted and secure before deployment.
- Verifying that the scripts have been assigned to the correct group of devices or users.
- Troubleshooting any issues related to script execution, such as permissions or dependencies.
- [CONFLICT: Oliver Kieselbach does not mention specific pitfalls in his article]

## KQL / PowerShell
[The article does not provide specific queries or scripts.]

## Related Topics
- PowerShell script
- Intune management extension (IME)
- Script execution
- 32-bit applications (as the article mentions that Win32 Apps can be installed using this approach)
- MSI packages via MDM OMA-DM channel [CONFLICT: Oliver Kieselbach adds this as a related topic, but it was not explicitly mentioned in the existing entry]
- Details of the MSI deployment of the Intune Management Extension agent? (see below)
- Azure Automation for process automation with Intune and Azure AD [NEW: from Oliver Kieselbach's article]

## Details of the MSI deployment of the Intune Management Extension agent? (from Part 2)
The EnterpriseDesktopAppManagement CSP takes care of the MSI install job and delivers the MSI to the device and starts the execution. The CSP provides some helpers for the installation process, such as [InstallApplication](https://docs.microsoft.com/en-us/intune/deploy-use-powershell-scripts#installapplication) and [UninstallApplication](https://docs.microsoft.com/en-us/intune/deploy-use-powershell-scripts#uninstallapplication).

## Additional Information (from Oliver Kieselbach's article)
For process automation with Azure Automation, you can set up the Azure environment and create a Runbook to perform tasks like deleting old devices from Intune and Azure AD. This workflow can be used by the service desk to quickly delete a device in both involved services Intune and AAD. The established cloud workflow can be used to build other workflows which are worthwhile in your environment.

To authenticate as an user (service account) for the Intune API via Microsoft Graph, you need to set up an Azure application to support this scenario: [How to use Azure AD to access Intune](https://docs.microsoft.com/en-us/intune/how-to-use-azuread-access-intune).