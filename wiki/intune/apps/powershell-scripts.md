---
conflicts:
- '[CONFLICT: Daniel Chronlund says Exchange Online DNS Management, existing entry
  does not mention it]'
- '[CONFLICT: Daniel Chronlund says Teams External Access Management, existing entry
  does not mention it]'
- '[CONFLICT: Daniel Chronlund says inspecting roles is important, existing entry
  does not mention this]'
- '[CONFLICT: Daniel Chronlund says inspecting roles is important]'
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

# PowerShell Scripts in Intune and Modern Workplace DNS Management

## Overview
This topic discusses various PowerShell scripts related to modern workplace management: one for automatic Azure AD user account enumeration, which can be used by malicious actors to find real user accounts to target in an identity-based attack on Azure AD and Office 365 environments ([PowerShell Script for Automatic User Enumeration](#key-concepts)), another for quickly checking and managing Exchange Online DNS records for SPF, DKIM, and DMARC (Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and DMARC with PowerShell), a third one for managing Teams External Access for allowed domains using PowerShell and Teams Approvals by Daniel Chronlund, a script for inspecting Azure AD Role Assignments [CONFLICT: Daniel Chronlund says inspecting roles is important], and a new addition "My Azure AD has been breached! What now?" by Daniel Chronlund. Additionally, there's a new PowerShell script for cleaning up Azure MFA SMS and Voice Call Methods ([Azure MFA SMS and Voice Call Methods Cleanup Tool](#azure-mfa-sms-and-voice-call-methods-cleanup-tool)).

## Key Concepts
- Azure AD User Account Enumeration
- PowerShell Script for Automatic User Enumeration
- Cloud-only accounts vs Federated accounts
- Public endpoints in Azure AD
- Exchange Online
- Sender Policy Framework (SPF)
- DomainKeys Identified Mail (DKIM)
- Domain Message Authentication Reporting & Conformance (DMARC)
- Teams External Access
- Teams Approvals
- Azure AD Role Assignments [New: Daniel Chronlund says inspecting roles is important]
- MFA SMS and Voice Call Methods

## Configuration
The article provides PowerShell scripts for the following:
1. Automatic Azure AD user account enumeration ([PowerShell Script for Automatic User Enumeration](#configuration))
2. Managing Exchange Online DNS records for SPF, DKIM, and DMARC (Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and DMARC with PowerShell)
3. Enabling Teams federation for allowed domains only using PowerShell ([Manage Teams External Access for Allowed Domains Using PowerShell and Teams Approvals](#manage-teams-external-access-for-allowed-domains-using-powershell-and-teams-approvals))
4. Inspecting Azure AD Role Assignments [New: Daniel Chronlund says inspecting roles is important]
5. Cleaning up Azure MFA SMS and Voice Call Methods ([Azure MFA SMS and Voice Call Methods Cleanup Tool](#azure-mfa-sms-and-voice-call-methods-cleanup-tool))

## Common Pitfalls
The author warns that the user enumeration script is intended for testing purposes only and should not be used in an unethical or unlawful manner. The script may not work for federated domains, as they are managed by the organization's federation infrastructure (AD FS). For Exchange Online DNS management, it's important to ensure that SPF, DKIM, and DMARC records are correctly configured to improve email reputation [Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and DMARC with PowerShell].

Regarding the Teams federation script, it's important to ensure that only trusted domains are added to the list of allowed domains for federation. The script includes a switch called **-RemoveExistingDomains** which resets the list before adding new domains.

In case of Azure AD breach, Daniel Chronlund suggests inspecting important roles and using PowerShell scripts to understand Azure AD role assignments, detections, and cleanup ([My Azure AD has been breached! What now?](#my-azure-ad-has-been-breached-what-now)).

Regarding MFA, it's recommended to disable SMS and voice calls as a MFA factor due to security concerns and move towards more modern methods like Microsoft Authenticator, Windows Hello for Business, and FIDO2. The new script ([Azure MFA SMS and Voice Call Methods Cleanup Tool](#azure-mfa-sms-and-voice-call-methods-cleanup-tool)) helps in cleaning up all registered phone methods and numbers on the user accounts in Azure AD.

## Azure MFA SMS and Voice Call Methods Cleanup Tool

Azure MFA SMS and Voice Call Methods Cleanup Tool – Daniel Chronlund Cloud Security Blog

[Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/)

[Azure AD](https://danielchronlund.com/category/azure-ad/), [Cloud](https://danielchronlund.com/category/cloud/), [Graph](https://danielchronlund.com/category/graph/), [MFA](https://danielchronlund.com/category/mfa/), [Microsoft](https://danielchronlund.com/category/microsoft/), [Microsoft 365](https://danielchronlund.com/category/microsoft-365/), [PowerShell](https://danielchronlund.com/category/powershell/), [Security](https://danielchronlund.com/category/security/)

October 7, 2021October 14, 2021
4 Minutes