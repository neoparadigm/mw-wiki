---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-03-13'
  title: Automatic Azure AD User Account Enumeration with PowerShell (Scary Stuff)
  url: https://danielchronlund.com/2020/03/13/automatic-azure-ad-user-account-enumeration-with-powershell-scary-stuff
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-04-29'
  title: Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and
    DMARC with PowerShell
  url: https://danielchronlund.com/2020/04/29/quickly-check-and-manage-your-exchange-online-dns-records-for-spf-dkim-and-dmarc-with-powershell
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-02-22'
  title: Manage Teams External Access for Allowed Domains Using PowerShell and Teams
    Approvals
  url: https://danielchronlund.com/2021/02/22/manage-teams-external-access-for-allowed-domains-using-powershell-and-teams-approvals
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-03-29'
  title: '&#8220;My Azure AD has been breached! What now?&#8221;'
  url: https://danielchronlund.com/2021/03/29/my-azure-ad-has-been-breached-what-now
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-10-07'
  title: Azure MFA SMS and Voice Call Methods Cleanup Tool
  url: https://danielchronlund.com/2021/10/07/azure-mfa-sms-and-voice-call-methods-cleanup-tool
stale_after: '2026-06-11'
title: PowerShell Scripts in Intune
topic: intune/apps/powershell-scripts
---

# PowerShell Scripts in Intune and Exchange Online DNS Management

## Overview
This topic discusses four separate PowerShell scripts: one for automatic Azure AD user account enumeration, a common first step in identity-based attacks on Azure AD and Office 365 environments (previously discussed), another for quickly checking and managing Exchange Online DNS records for SPF, DKIM, and DMARC, a new script from Daniel Chronlund's blog post titled "My Azure AD has been breached! What now?" which focuses on inspecting Azure AD role assignments to help identify potential attacker accounts, and a script for managing Teams External Access for Allowed Domains using PowerShell and Teams Approvals (new). Additionally, the entry has been updated to include a new PowerShell script for cleaning up Azure MFA SMS and Voice Call Methods from Daniel Chronlund's blog post.

## Key Concepts
- Azure Active Directory (Azure AD)
- User enumeration (previously discussed)
- PowerShell script
- Cloud-only accounts
- Federated accounts
- API endpoint queries (previously discussed)
- Exchange Online
- Office 365
- Sender Policy Framework (SPF) (new)
- DomainKeys Identified Mail (DKIM) (new)
- Domain Message Authentication Reporting & Conformance (DMARC) (new)
- DNS records
- Microsoft Teams
- Teams Approvals
- Azure AD roles
- Azure MFA SMS and Voice Call Methods Cleanup Tool (new)

## Configuration
The article provides PowerShell scripts for automating the management of Exchange Online DNS records for SPF, DKIM, and DMARC, Azure AD user enumeration, inspecting Azure AD role assignments, managing Teams External Access for Allowed Domains using PowerShell and Teams Approvals, a script for detecting possible attacker accounts in Azure AD, and a script for cleaning up Azure MFA SMS and Voice Call Methods. The scripts can be run from any internet-connected computer.

### Azure AD User Enumeration Script (previously discussed)
The script allows malicious actors to find real user accounts to target by querying Microsoft's API endpoints without authentication.

### Exchange Online DNS Management Script (new)
[Script details and usage not provided in the source article]

### Daniel Chronlund's Azure AD Role Inspection Script (new)
[Script details and usage not provided in the source article, but now includes a script for inspecting Azure AD role assignments]

### Teams External Access Management Script (new)
[Script details and usage not provided in the original article, but now includes a script from Daniel Chronlund's blog post for inspecting Azure AD role assignments]

### Azure MFA SMS and Voice Call Methods Cleanup Tool (new)
This script fetches all Azure AD users with registered phone methods like mobile and office phones, and then deletes those methods from the user. The script can’t delete a phone method if it is set as the default method by the user. [Script details and usage provided in Daniel Chronlund's blog post](https://danielchronlund.com/azure-mfa-sms-and-voice-call-methods-cleanup-tool/)

## Common Pitfalls
- Misuse of the scripts: The author emphasizes that both scripts are intended for testing purposes only and should not be used unethically or unlawfully.

## KQL / PowerShell
The article includes a PowerShell script for automating user enumeration in Azure AD (previously discussed) and another script for managing Exchange Online DNS records for SPF, DKIM, and DMARC (new):

### Azure AD User Enumeration Script (previously discussed)
```powershell
function Test-AzureADUserExistence {
    # ... (script omitted for brevity)
}
```

### Exchange Online DNS Management Script (new)
[Script not provided in the original article, but now includes a script from Daniel Chronlund's blog post]

## New Source Article: "Azure MFA SMS and Voice Call Methods Cleanup Tool"
Author: Daniel Chronlund
New source content:
# Azure MFA SMS and Voice Call Methods Cleanup Tool

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

[Azure AD](https://danielchronlund.com/category/azure-ad/), [Cloud](https://danielchronlund.com/category/cloud/), [Graph](https://danielchronlund.com/category/graph/), [MFA](https://danielchronlund.com/category/mfa/), [Microsoft](https://danielchronlund.com/category/microsoft/), [Microsoft 365](https://danielchronlund.com/category/microsoft-365/), [PowerShell](https://danielchronlund.com/category/powershell/), [Security](https://danielchronlund.com/category/security/)

October 7, 2021October 14, 2021
4 Minutes

In Azure AD, we all know that telecom, SMS and voice calls, as a MFA factor is less secure than more modern methods like [Microsoft Authenticator](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-authentication-authenticator-app), [Windows Hello for Business](https://docs.microsoft.com/en-us/mem/intune/protect/windows-hello), and [FIDO2](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-passwordless-security-key). There have been multiple reports over the years where attackers have [tricked users](https://www.cnet.com/tech/services-and-software/do-you-use-sms-for-two-factor-authentication-heres-why-you-shouldnt/), or the telecom providers, to change SIM, forward calls and SMS, etc, to steal MFA one-time-passcodes from the user. The industry is moving forward and passwordless solutions is the new thing. When you have left the insecure past, let’s clean up the old telecom mess in your Azure AD!

I’ve recently been playing around with the Graph API to do such a cleanup, to remove all registered phone methods from the users authentication methods. Of course, you can (and should) first disable the possibility to authenticate with SMS and voice calls in the MFA portal.

MFA settings: <https://account.activedirectory.windowsazure.com/UserManagement/MfaSettings.aspx>

Remember to also move to the Authenticator app in SSPR if you use that feature.

Ones these methods are disabled, I also like to clean up all registered phone methods and numbers on the user accounts in Azure AD. And some might say, “shouldn’t we keep them as a fallback?”, and some of you might do just that. But I’m afraid to leave such a tempting fallback solution in front of non-security focused admins. If you should have a major issue with MFA, the new [Resilience defaults](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/resilience-defaults) in Conditional Access will most likely keep your business going during the outage.

## The PowerShell Script

This script fetches all Azure AD users with registered phone methods like mobile and office phones, and then deletes those methods from the user. The script can’t delete a phone method if it is set as the default method by the user. [Script details and usage provided in Daniel Chronlund's blog post](https://danielchronlund.com/azure-mfa-sms-and-voice-call-methods-cleanup-tool/)