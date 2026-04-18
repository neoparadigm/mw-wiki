---
conflicts:
- '[CONFLICT: Oliver Kieselbach mentions .intunewin files but does not provide specific
  details on common pitfalls related to them]'
- '[CONFLICT: Oliver Kieselbach says X, existing entry says Y]'
context_note: Win32 App Deployment is part of the intune domain. Synthesised from
  6 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-09-29'
  title: Ignite 2018 &#8211; My wrap up
  url: https://oliverkieselbach.com/2018/09/29/ignite-2018-my-wrap-up
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-09-29'
  title: Ignite 2018 &#8211; My wrap up
  url: https://oliverkieselbach.com/2018/09/29/ignite-2018-my-wrap-up/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-10-02'
  title: Part 3, Deep dive Microsoft Intune Management Extension – Win32 Apps
  url: https://oliverkieselbach.com/2018/10/02/part-3-deep-dive-microsoft-intune-management-extension-win32-apps
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-10-02'
  title: Part 3, Deep dive Microsoft Intune Management Extension – Win32 Apps
  url: https://oliverkieselbach.com/2018/10/02/part-3-deep-dive-microsoft-intune-management-extension-win32-apps/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-12-15'
  title: Deploying Win32 app BGInfo with Intune
  url: https://oliverkieselbach.com/2018/12/15/deploying-win32-app-bginfo-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-12-15'
  title: Deploying Win32 app BGInfo with Intune
  url: https://oliverkieselbach.com/2018/12/15/deploying-win32-app-bginfo-with-intune
stale_after: '2026-06-17'
title: Win32 App Deployment and Packaging
topic: intune/apps/win32-app-deployment
---

# Win32 App Deployment and Packaging

## Win32 App Deployment and Packaging

Win32 app deployment and packaging refers to the process of preparing and distributing traditional Windows desktop applications for management in a modern workplace environment using Microsoft Intune. This topic matters because it enables organizations to modernize their application management approach by leveraging cloud-based solutions, reducing complexity, and improving security.

## Key Concepts

* Win32 app support in Microsoft Intune [New: Confirmed at Ignite 2018]
* App containerization (zip format)
* Microsoft Management Extension (MME)
* Hybrid Azure AD join for Windows Autopilot
* Intune Security Baselines
* Desktop Analytics
* [Intune Win32 app packages (.intunewin)](#packagedapps-new)
* Deployment of Win32 apps using BGInfo with Intune [New Source: Oliver Kieselbach, Confirmed method at Ignite 2018]
* Local Administrator identification through vbs script [New Source: Oliver Kieselbach]

## Configuration

1. Wrap your Win32 apps using the MME to create a containerized package, including .intunewin files.
    - [Part 3, Deep dive Microsoft Intune Management Extension – Win32 Apps](#newsourcecontent) provides details on how to create packaged apps using the MME.
2. Distribute the package via Microsoft Intune.
3. For Windows Autopilot, configure Hybrid Azure AD join and harvest Autopilot data.
4. Utilize Intune Security Baselines to fill configuration gaps during transition from local AD and Group Policy environment to Azure AD/MDM environment.
5. Leverage Administrative Templates for Office and Windows configurations in Intune.
6. Use the Intune PowerShell SDK for automation tasks.
7. Deploy Win32 apps like BGInfo using Intune [New Source: Oliver Kieselbach]
    - [Deploying Win32 app BGInfo with Intune](#newsourcecontent) provides a detailed walkthrough of deploying BGInfo using Intune.
8. Identify local administrators through vbs script [New Source: Oliver Kieselbach]
    - The provided vbs script can be used to identify local administrators in the context of BGInfo deployment.

## Common Pitfalls

* Misconfigurations leading to security vulnerabilities or application compatibility issues.
* Incorrectly packaging apps, resulting in deployment failures or unexpected behavior.
    - [CONFLICT: Oliver Kieselbach mentions .intunewin files but does not provide specific details on common pitfalls related to them]
* Overlooking the need for administrative templates when transitioning from a local AD and Group Policy environment to Azure AD/MDM environment.

## KQL / PowerShell

The article does not provide specific queries or scripts related to Win32 app deployment and packaging. However, relevant information can be found in the following links:

* [Microsoft Intune Management Extension (Part 1)](https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts/)
* [Microsoft Intune Management Extension (Part 2)](https://oliverkieselbach.com/2018/02/12/part-2-deep-dive-microsoft-intune-management-extension-powershell-scripts/)
* [Intune PowerShell SDK](https://github.com/Microsoft/Intune-PowerShell-SDK)
* [New: Deep dive Microsoft Intune Management Extension – Win32 Apps (Oliver Kieselbach)](#newsou)
* [Deploying Win32 app BGInfo with Intune (Oliver Kieselbach)](#newsourcecontent)
* Local Administrator identification through vbs script [New Source: Oliver Kieselbach]