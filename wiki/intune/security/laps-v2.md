---
conflicts:
- '[CONFLICT: Simon Skotheimsvik provides alternative approaches for migration and
  configuration]'
- '[CONFLICT: Simon Skotheimsvik provides additional options for setting password
  policies]'
- '[CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune]'
- '[CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which
  might not require this step]'
- '[CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which
  might have different configuration options]'
- '[CONFLICT: Michael Morten Sonne''s article does not mention this step in the context
  of managing through Microsoft Intune]'
- '[CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which
  might have different methods for setting password policies]'
context_note: Laps V2 is part of the intune domain. Synthesised from 5 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2023-04-29'
  title: How to use Windows LAPS – PowerShell – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/how-to-use-windows-laps-powershell
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2023-06-12'
  title: Simon does Migrating Cloud LAPS to the New Windows LAPS
  url: https://skotheimsvik.no/migrating-cloud-laps-to-the-new-windows-laps
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2025-05-20'
  title: Simon does Migrating To The New 24H2 LAPS Settings
  url: https://skotheimsvik.no/migrating-to-the-new-24h2-laps-settings
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2023-04-23'
  title: Windows LAPS and management through Microsoft Intune – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/windows-laps-and-management-through-microsoft-intune
- author: James Yip
  crawled: '2026-04-18'
  date: '2024-04-18'
  title: 'Practical Endpoint: Deploy Cloud-Based Windows LAPS to Windows Endpoints'
  url: https://practical365.com/deploy-cloud-based-windows-laps-to-windows-endpoints
stale_after: '2026-06-17'
title: Windows LAPS v2 Configuration
topic: intune/security/laps-v2
---

# Windows LAPS v2 Configuration and Migrating Cloud LAPS to the New Windows LAPS

## Windows LAPS v2 Configuration

### Overview
This topic discusses the configuration of Windows LAPS v2, a solution for managing local administrator passwords on domain-joined computers in a secure and scalable manner. It also includes information about migrating from Cloud LAPS to the New Windows LAPS. [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune]

### Key Concepts
- Windows LAPS v2
- Local Administrator Password Solution (LAPS)
- Group Policy Object (GPO)
- PowerShell scripts
- Azure AD/Entra ID (from the new source)
- Identity, Intune, Security, Windows 10, Windows 11, and Windows Server (from the new source)
- Configuration Service Provider (CSP) (new from James Yip)

### Configuration
1. Install the LAPS client on target computers. [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might not require this step]
2. Create a new GPO or modify an existing one to include the LAPS ADMX templates.
3. Link the GPO to the appropriate Organizational Unit (OU) containing the target computers.
4. Configure the GPO settings, such as password length and expiration policy. [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different configuration options]
5. Run the `Install-LapsClient` PowerShell script on each target computer to register it with Active Directory. [CONFLICT: Michael Morten Sonne's article does not mention this step in the context of managing through Microsoft Intune]
6. Use the `Set-LapsPasswordPolicy` PowerShell cmdlet to set the password policy for the entire domain or specific OUs. [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different methods for setting password policies]
7. To work with cloud-managed endpoints, ensure a supported version of Windows is used (Windows 10 or 11 with Apr 2023 update, or Windows Server 2019 or 2022 with Apr 2023 update) and leverage the Configuration Service Provider (CSP) provided by Microsoft. (new from James Yip)

### Common Pitfalls
- Forgetting to install the LAPS client on target computers.
- Not linking the GPO containing the LAPS ADMX templates to the appropriate OU.
- Misconfiguring the GPO settings, such as setting a too short or too frequent password expiration policy.

### KQL / PowerShell
```powershell
# Set password policy for the entire domain
Set-LapsPasswordPolicy -DomainName contoso.com -PasswordLength 30 -PasswordExpiryDays 90

# Set password policy for a specific OU
$ou = Get-ADOrganizationalUnit -Filter "Name -eq 'Sales'"
Set-LapsPasswordPolicy -Ou $ou -PasswordLength 20 -PasswordExpiryDays 60
```

### Migrating Cloud LAPS to the New Windows LAPS
[Simon Skotheimsvik provides detailed steps for migrating from Cloud LAPS to the New Windows LAPS, including alternative approaches not present in the existing entry]

#### The Background
[Existing entry provides a brief background on Microsoft LAPS, expanded upon by Simon Skotheimsvik's article]

#### Different Approaches Migration Cloud LAPS to Windows LAPS
[Simon Skotheimsvik outlines alternative approaches for migration not present in the existing entry, including options for automating local admin account creation and using passphrases]

#### New Source Article: Practical Endpoint: Deploy Cloud-Based Windows LAPS to Windows Endpoints
Author: James Yip
New source content:
To address the problem of using classic LAPS with cloud-managed endpoints, Microsoft has released a revamped version of LAPS that can store the local admin password in Entra ID. This new version is called Windows LAPS and does not require agents to be installed on Windows endpoints. Instead, it leverages Configuration Service Provider (CSP) available in supported versions of Windows 10, 11, Server 2019, and Server 2022 with the Apr 2023 update.

For more details about deploying LAPS and enhancing the security of Windows endpoints, refer to [Practical Endpoint: Deploy Cloud-Based Windows LAPS to Windows Endpoints](https://practical365.com/deploy-cloud-based-windows-laps-to-windows-endpoints/) by James Yip.