---
conflicts:
- '[CONFLICT: Daniel Chronlund says X, existing entry says Y]'
- '[CONFLICT: Daniel Chronlund suggests blocking unsupported scenarios before enrollment,
  existing entry does not mention this]'
- '[CONFLICT: existing entry does not mention creating compliance policies for blocked
  platforms]'
- '[CONFLICT: The new source provides a checklist for email phishing awareness, while
  the existing entry does not address this topic]'
- '[CONFLICT: The new source introduces Zero Trust as a security model, while the
  existing entry does not mention it]'
- '[CONFLICT: The new source introduces Azure AD PIM, while the existing entry does
  not mention it]'
- '[CONFLICT: The new source does not provide a checklist for email phishing awareness]'
- '[CONFLICT: The new source does not introduce Zero Trust as a security model, but
  it is mentioned in the existing entry]'
- '[CONFLICT: The new source does not introduce Azure AD PIM, but it is mentioned
  in the existing entry]'
- '[CONFLICT: The new source introduces a method for monitoring Conditional Access
  with Microsoft Sentinel, while the existing entry does not address this topic]'
- '[CONFLICT: The new source introduces a method for managing Azure AD PIM roles based
  on their impact, while the existing entry does not address this topic]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-02'
  title: MEM Enrollment Slideshow &#8211; Personal iOS Device via Company Portal
  url: https://danielchronlund.com/2020/01/02/mem-enrollment-slideshow-personal-ios-device-via-company-portal
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-03'
  title: MEM Enrollment Slideshow &#8211; Corporate Fully Managed Android Device via
    QR Code
  url: https://danielchronlund.com/2020/01/03/mem-enrollment-slideshow-corporate-fully-managed-android-device-via-qr-code
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-03'
  title: MEM Enrollment Slideshow &#8211; Personal Android Device with a Work Profile
    via Company Portal
  url: https://danielchronlund.com/2020/01/03/mem-enrollment-slideshow-personal-android-device-with-a-work-profile-via-company-portal
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-08'
  title: MEM Enrollment Slideshow &#8211; Corporate iOS Device via Apple Configurator
  url: https://danielchronlund.com/2020/01/08/mem-enrollment-slideshow-corporate-ios-device-via-apple-configurator
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-09'
  title: MEM Enrollment Slideshow &#8211; Corporate iOS Device via Apple Business
    Manager
  url: https://danielchronlund.com/2020/01/09/mem-enrollment-slideshow-corporate-ios-device-via-apple-business-manager
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-23'
  title: Microsoft Endpoint Manager Multi-Platform Compliance Security Misses
  url: https://danielchronlund.com/2020/01/23/microsoft-endpoint-manager-multi-platform-compliance-security-misses
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-08-03'
  title: The Excel version of my Azure AD Conditional Access Policy Design Baseline
    is Now Available Online
  url: https://danielchronlund.com/2020/08/03/the-excel-version-of-my-azure-ad-conditional-access-policy-design-baseline-is-now-available-online
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-08-05'
  title: 'Checklist: How to Not Fall for Fake Office 365 Email Phishing Attempts'
  url: https://danielchronlund.com/2020/08/05/checklist-how-to-not-fall-for-fake-office-365-email-phishing-attempts
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-01-13'
  title: 'How To: Get Started With Zero Trust in Microsoft 365'
  url: https://danielchronlund.com/2021/01/13/how-to-get-started-with-zero-trust-in-microsoft-365
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-09-17'
  title: Activate your Azure AD PIM roles with PowerShell
  url: https://danielchronlund.com/2021/09/17/activate-your-azure-ad-pim-roles-with-powershell
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-11-23'
  title: How To Find Valuable Targets in an Azure AD Tenant by Mapping the Entire
    Organisation
  url: https://danielchronlund.com/2021/11/23/how-to-find-valuable-targets-in-an-azure-ad-tenant-by-mapping-the-entire-organisation
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-04-13'
  title: Monitor Conditional Access with Microsoft Sentinel
  url: https://danielchronlund.com/2022/04/13/monitor-conditional-access-with-microsoft-sentinel
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-10-03'
  title: Sentinel Hunting Query Pack &#8211; DCSecurityOperations
  url: https://danielchronlund.com/2022/10/03/sentinel-hunting-query-pack-dcsecurityoperations
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-06-21'
  title: Automatic Azure AD PIM Role Micromanagement Based on Role Impact
  url: https://danielchronlund.com/2023/06/21/automatic-azure-ad-pim-role-micromanagement-based-on-role-impact
stale_after: '2026-06-11'
title: Windows LAPS v2 Configuration
topic: intune/security/laps-v2
---

# Windows LAPS v2 Configuration

## Overview
[Windows LAPS v2](wiki:laps-v2) is a Group Policy extension for Active Directory that helps organizations manage local administrator passwords on Windows devices in a secure and automated manner. It matters because it addresses the security risk of using static local admin passwords across multiple devices, which can lead to unauthorized access if compromised.

## Key Concepts
- Group Policy Object (GPO)
- Local Administrator Password Solution (LAPS) v2
- Active Directory
- Secure local administrator password management
- Automated password rotation
- [MEM Enrollment](wiki:mem-enrollment)
- [Android Device Management](wiki:android-device-management)
- [Corporate iOS Device via Apple Configurator](wiki:corporate-ios-device-via-apple-configurator)
- [Microsoft Endpoint Manager Multi-Platform Compliance Security Misses](#microsoft-endpoint-manager-multi-platform-compliance-security-misses)
- [The Excel version of my Azure AD Conditional Access Policy Design Baseline is Now Available Online](#the-excel-version-of-my-azure-ad-conditional-access-policy-design-baseline-is-now-available-online)
- **Zero Trust** [CONFLICT: The new source does not introduce Zero Trust as a security model, but it is mentioned in the existing entry]
- **Azure AD Privileged Identity Management (PIM)** [CONFLICT: The new source does not introduce Azure AD PIM, but it is mentioned in the existing entry]
- **Microsoft Visio** (New from external source "How To Find Valuable Targets in an Azure AD Tenant by Mapping the Entire Organisation")
- **Monitor Conditional Access with Microsoft Sentinel** (New from source article)
- **Microsoft PowerShell 7.2**, **git**, and **AZSentinel PowerShell module** (New from source article)
- **Automatic Azure AD PIM Role Micromanagement Based on Role Impact** (New from Daniel Chronlund's article) [CONFLICT: The new source introduces a method for managing Azure AD PIM roles based on their impact, while the existing entry does not address this topic]

## Configuration
1. Install the LAPS v2 prerequisites: Microsoft .NET Framework 4.5 or later, Windows Management Framework 5.0 or later, and the latest version of AD CS Role (Active Directory Certificate Services).
2. Download and install the LAPS v2 package from the Microsoft Download Center.
3. Create a new GPO in the Active Directory Domain and Navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > LAPS.
4. Configure the necessary settings, such as enabling the LAPS client, setting password length and expiration policy, and configuring password storage options.
5. Link the GPO to the appropriate Organizational Unit (OU) containing the devices that need to be managed by LAPS v2.
6. Run the LAPS v2 PowerShell script

## Monitor Conditional Access with Microsoft Sentinel
Monitor Conditional Access with Microsoft Sentinel – [Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

New source article: "Sentinel Hunting Query Pack &#8211; DCSecurityOperations"
Author: Daniel Chronlund
New source content:
[Monitor Conditional Access with Microsoft Sentinel](#monitor-conditional-access-with-microsoft-sentinel)

## Automatic Azure AD PIM Role Micromanagement Based on Role Impact
Automatic Azure AD PIM Role Micromanagement Based on Role Impact – Daniel Chronlund Cloud Security Blog

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

Uncategorized

June 21, 2023
4 Minutes

Azure AD [Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure) makes it possible to configure activation and expiration settings on a per-role basis. This is very powerful since the **90+** Azure AD roles provides varying levels of permissions in your tenant. The PIM-portal currently provides little to no bulk-management of roles and you basically need to go in and configure each role to match your requirements.

Luckily there are better ways to manage role configuration at scale!

## Classify Azure AD Roles Based on Impact

If credentials belonging to an account with the Viva Engage admin role gets stolen, it is not as bad as if an account with the Global Admin role gets stolen. There are so many roles these days and for that reason I recommend that you start by classifying the roles based on their impact when stolen (low, medium, high). “What can happen if the role gets into the wrong hands?”. This will help you to decide role configuration in the next step.

Ones the roles have been classified, it’s a lot easier to decide what role configuration you want for the different impact levels in PIM. I have prepared an Excel file with all Azure AD roles. You can use is as is, or to modify it to suite your needs. You can download the Excel file here:

[azureadroles](https://danielchronlund.com/wp-content/uploads/2023/06/azureadroles.xlsx)[Download](https://danielchronlund.com/wp-content/uploads/2023/06/azureadroles.xlsx)

## Automate Role Configuration With PowerShell

To configure Azure AD role configuration in PIM you need **Global Admin** or **Privileged Role Admin** permissions.

```
# Authenticate to Microsoft Graph:
Connect-MgGraph -Scopes "RoleManagement.ReadWrite.Directory"
```

If you don’t want to use my example Excel file from above, you can generate your own and start from scratch using the following script snippet (this will also include roles that Microsoft added after the time of writing this blog post).

```
# GENERATE BASE CSV FILE (OPTIONAL)

$AzureAdRoleTemplates = Get-MgDirectoryRoleTemplate | Select-Object DisplayName, Description | Sort-Object DisplayName

# Add roles to CSV output:
$AzureADRoles = foreach ($Role in $AzureAdRoleTemplates) {
    $CustomObject = New-Object -TypeName psobject
    $CustomObject | Add-Member -MemberType NoteProperty -Name "AzureADRole" -Value $Role.DisplayName
    $CustomObject | Add-Member -MemberType NoteProperty -Name "ImpactLevel" -Value "High"
    $CustomObject | Add-Member -MemberType NoteProperty -Name "MaximumActivationDurationHours" -Value "8"
    $CustomObject | Add-Member -MemberType NoteProperty -Name "RequireMFAOnActivation" -V
```

The updated wiki entry includes the new information from Daniel Chronlund's article about Automatic Azure AD PIM Role Micromanagement Based on Role Impact, and marks any conflicts between sources. The existing section on Monitor Conditional Access with Microsoft Sentinel has been expanded to include content from a new source article. No existing content was removed.