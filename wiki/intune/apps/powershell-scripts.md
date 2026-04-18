---
conflict_topics:
- intune/apps/winget-intune
- intune/apps/microsoft-store-apps
conflicts:
- '[CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI
  packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method
  is not mentioned in the existing entry.]'
context_note: Powershell Scripts is part of the intune domain. Synthesised from 6
  community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2017-11-29'
  title: November 2017 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2017/11
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2017-11-28'
  title: Deep dive Microsoft Intune Management Extension &#8211; PowerShell Scripts
  url: https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2017-11-28'
  title: Deep dive Microsoft Intune Management Extension &#8211; PowerShell Scripts
  url: https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-02-12'
  title: Part 2, Deep dive Microsoft Intune Management Extension &#8211; PowerShell
    Scripts
  url: https://oliverkieselbach.com/2018/02/12/part-2-deep-dive-microsoft-intune-management-extension-powershell-scripts/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-02-12'
  title: Part 2, Deep dive Microsoft Intune Management Extension &#8211; PowerShell
    Scripts
  url: https://oliverkieselbach.com/2018/02/12/part-2-deep-dive-microsoft-intune-management-extension-powershell-scripts
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-02-25'
  title: Process automation for Intune and Azure AD with Azure Automation
  url: https://oliverkieselbach.com/2018/02/25/process-automation-for-intune-and-azure-ad-with-azure-automation
stale_after: '2026-06-17'
title: PowerShell Scripts in Intune
topic: intune/apps/powershell-scripts
---

# PowerShell Scripts in Intune and Azure Automation for Process Automation

## Overview
PowerShell Scripts in Intune is a modern management strategy introduced by Microsoft to address limitations like custom configurations and Win32 App installs. This approach allows for managing and executing PowerShell scripts on Windows 10 devices using the Intune Management Extension (IME).

Microsoft made a big step forward in the Modern Management field. Limitations like custom configurations or even Win32 App installs can be addressed now. Microsoft developed an EMS agent (aka SideCar) and released it as a new Intune feature called [Intune Management Extension](https://docs.microsoft.com/en-us/intune/intune-management-extension). This agent is able to manage and execute PowerShell scripts on Windows 10 devices and it does this quite well.

[CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method is not mentioned in the existing entry.]

## Key Concepts
- Intune Management Extension (IME)
- PowerShell script execution on Windows 10 devices
- ADMX ingestion to extend policy settings in Intune
- Azure Automation for process automation

## Configuration
To configure PowerShell scripts in Intune, follow these steps:

1. Create a PowerShell script and save it as .ps1 file.
2. Upload the script to a network share or Azure Blob Storage that is accessible by your Intune tenant.
3. In the Intune console, navigate to "Templates" > "Configuration profiles" > "Create profile".
4. Select "Windows 10 and later" as the platform and "PowerShell" as the profile type.
5. Configure settings such as script name, script parameters, and execution frequency.
6. Under "Script content", select "Script in Azure storage" or "Script from a network share".
7. Provide the necessary details for the chosen option and save the configuration profile.
8. Assign the profile to the appropriate group of devices.

### Common Pitfalls
- Ensuring that the PowerShell script is properly formatted and has execution permissions set.
- Verifying that the network share or Azure Blob Storage used for storing the scripts is accessible by the Intune tenant.
- Making sure that the configuration profile is assigned to the correct group of devices.
- [CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method is not mentioned in the existing entry.]

## Azure Automation for Process Automation
[New content]

Process automation for Intune and Azure AD with Azure Automation – Modern IT – Cloud – Workplace

Start typing and press Enter to search

open search form

close search form

Cloud managed environments benefit from the idea of software as a service, you don’t have to think about upgrading or maintenance of the infrastructure itself. But often we need to automate the tools itself. A very good example here is when an employee quits his job, than we need to trigger a lot of processes like disabling the account, retire of the device(s), wiping of the devices, sending some notes to various people and so on. Another example might be the cleanup of devices within Intune and Azure AD as they get stale over time and they are not used by users anymore.

### Introduction

In the following blog post I like to show how to automate the process to delete old devices from Intune and Azure AD without the help of services from on-premises like servers running scheduled scripts. The established cloud workflow can be used by the service desk to quickly delete a device in both involved services Intune and AAD. After seeing a lot of environments where devices are being cleaned up in Intune and left in AAD, I thought its beneficial to show how to easily automate this with the Microsoft cloud solution [Azure Automation](https://azure.microsoft.com/en-us/services/automation/). If the basics are built it’s just a matter of combining new tasks within a Runbook to build other workflows which are worthwhile in your environment.

I will show how to setup the Azure environment and create the first Runbook. A Runbook is the actual workflow which runs the PowerShell script. The Runbook will do an unattended authentication against the Inunte API via Microsoft Graph to manage Intune. We do not have a PowerShell module for Intune at the time of writing therefore we use the Intune API in Microsoft Graph. For the AAD operations we use the AzureAD module to perform the management tasks.

### How to do unattended authentication with the Intune API?

The problem with the Intune API and Microsoft Graph is, that we can’t authenticate as an application as this is not supported at the time of writing. (**UPDATE 22 July 2019**: [Intune PowerShell SDK](https://www.powershellgallery.com/packages/Microsoft.Graph.Intune) – [works with Azure Automation now and supports app-only auth read operations!](https://docs.microsoft.com/en-us/intune/whats-new#intune-powershell-sdk)) See section here Intune Device Management permissions > *Application permissions: None.* <https://developer.microsoft.com/en-us/graph/docs/concepts/permissions_reference#intune-device-management-permissions>.

We need to authenticate as an user (service account). This requires additional credentials and a secure storage of them to automate. Microsoft has a good guide how to set up an Azure application to support this scenario: [How to use Azure AD to access 

## KQL / PowerShell
[The article does not provide any specific queries or scripts.]

## Related Topics
- PowerShell script
- Intune management extension (IME)
- Script execution in Intune
- 32-bit application deployment with Intune
- [Deep dive Microsoft Intune Management Extension – PowerShell Scripts](https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts/) (Oliver Kieselbach)
- [Deep dive Microsoft Intune Management Extension – Win32 Apps](https://oliverkieselbach.com/2018/10/02/part-

[New content]
- Azure Automation for process automation in Intune and Azure AD
- Unattended authentication with the Intune API via Microsoft Graph
- [How to use Azure AD to access Microsoft Graph](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-authenticate-app-service-application) (Microsoft documentation)