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
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2017-11-29'
  title: November 2017 &#8211; Modern IT &#8211; Cloud &#8211; Workplace
  url: https://oliverkieselbach.com/2017/11
stale_after: '2026-06-11'
title: PowerShell Scripts in Intune
topic: intune/apps/powershell-scripts
---

# PowerShell Scripts in Intune and Modern Workplace DNS Management

## Overview
This topic discusses various PowerShell scripts related to modern workplace management, including updates based on the "November 2017 - Modern IT - Cloud - Workplace" article by Oliver Kieselbach. The updated discussion includes:

- Automatic Azure AD user account enumeration ([PowerShell Script for Automatic User Enumeration](#key-concepts))
- Cloud-only accounts vs Federated accounts
- Public endpoints in Azure AD
- Exchange Online
- Sender Policy Framework (SPF)
- DomainKeys Identified Mail (DKIM)
- Domain Message Authentication Reporting & Conformance (DMARC)
- Teams External Access
- Teams Approvals
- Azure AD Role Assignments [New: Daniel Chronlund says inspecting roles is important, CONFLICT: Oliver Kieselbach does not mention this]
- MFA SMS and Voice Call Methods
- Intune Management Extension ([Deep Dive: Microsoft Intune Management Extension - PowerShell Scripts](#intune-management-extension))
- ADMX ingestion for policy settings in Intune ([Deep Dive: ADMX Ingestion to Configure SilentAccountConfig with OneDrive](#admx-ingestion))

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
- Intune Management Extension
- ADMX ingestion for policy settings in Intune

## Configuration
The article provides PowerShell scripts for the following:
1. Automatic Azure AD user account enumeration ([PowerShell Script for Automatic User Enumeration](#configuration))
2. Managing Exchange Online DNS records for SPF, DKIM, and DMARC (Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and DMARC with PowerShell)
3. Enabling Teams federation for allowed domains only using PowerShell ([Manage Teams External Access for Allowed Domains Using PowerShell and Teams Approvals](#manage-teams-external-access-for-allowed-domains-using-powershell-and-teams-approvals))
4. Inspecting Azure AD Role Assignments [New: Daniel Chronlund says inspecting roles is important]
5. Cleaning up Azure MFA SMS and Voice Call Methods ([Azure MFA SMS and Voice Call Methods Cleanup Tool](#azure-mfa-sms-and-voice-call-methods-cleanup-tool))
6. Intune Management Extension ([Deep Dive: Microsoft Intune Management Extension - PowerShell Scripts](#intune-management-extension))
7. ADMX ingestion for policy settings in Intune ([Deep Dive: ADMX Ingestion to Configure SilentAccountConfig with OneDrive](#admx-ingestion))

## Common Pitfalls
The author warns that the user enumeration script is intended for testing purposes only and should not be used in an unethical or unlawful manner. The script may not work for federated domains, as they are managed by the organization's federation infrastructure (AD FS). For Exchange Online DNS management, it's important to ensure that SPF, DKIM, and DMARC records are correctly configured to improve email reputation [Quickly Check and Manage your Exchange Online DNS Records for SPF, DKIM and DMARC with PowerShell].

## Intune Management Extension
[Deep Dive: Microsoft Intune Management Extension - PowerShell Scripts](https://oliverkieselbach.com/2017/11/29/deep-dive-microsoft-intune-management-extension-powershell-scripts/)

Microsoft made a big step forward in the Modern Management field with the Intune Management Extension (aka SideCar). This agent is able to manage and execute PowerShell scripts on Windows 10.

## ADMX ingestion
[Deep Dive: ADMX Ingestion to Configure SilentAccountConfig with OneDrive](https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive/)

Since Windows 10 1703, you can use ADMX ingestion to extend policy settings in Intune. What it basically does is to parse an ADMX file and build a MDM policy of it. In the end, you can configure the ADMX settings via OMA-URIs in Intune. More details about ADMX ingestion can be found [here](https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive/).