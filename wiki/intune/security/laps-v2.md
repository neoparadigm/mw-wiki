---
conflicts:
- '[CONFLICT: Simon Skotheimsvik provides an alternative approach for migration]'
- '[CONFLICT: This section is new content not present in the existing entry]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2023-04-29'
  title: How to use Windows LAPS – PowerShell – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/how-to-use-windows-laps-powershell
- author: Simon Skotheimsvik
  crawled: '2026-04-14'
  date: '2023-06-12'
  title: Simon does Migrating Cloud LAPS to the New Windows LAPS
  url: https://skotheimsvik.no/migrating-cloud-laps-to-the-new-windows-laps
- author: Simon Skotheimsvik
  crawled: '2026-04-14'
  date: '2025-05-20'
  title: Simon does Migrating To The New 24H2 LAPS Settings
  url: https://skotheimsvik.no/migrating-to-the-new-24h2-laps-settings
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2023-04-23'
  title: Windows LAPS and management through Microsoft Intune – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/windows-laps-and-management-through-microsoft-intune
stale_after: '2026-06-13'
title: Windows LAPS v2 Configuration
topic: intune/security/laps-v2
---

# Windows LAPS v2 Configuration

## Windows LAPS v2 Configuration

### Overview
This topic discusses the configuration of Windows LAPS v2, a solution for managing local admin passwords on domain-joined computers in a secure and scalable manner. The importance lies in enhancing security by enforcing regular password rotation and restricting access to sensitive systems. [Simon Skotheimsvik](https://skotheimsvik.no/author/ss-ga-wordpress) provides an alternative approach for migrating from Cloud LAPS to the New Windows LAPS, as well as a guide on Migrating To The New 24H2 LAPS Settings.

[Michael Morten Sonne](https://sonnes.cloud) also discusses managing Windows LAPS through Microsoft Intune in his blog post "Windows LAPS and management through Microsoft Intune" (<https://blog.sonnes.cloud/posts/windows-laps-and-management-through-microsoft-intune/>).

### Key Concepts
- Windows LAPS v2
- Local admin password management
- Password rotation
- LAPS policy configuration
- Migrating Cloud LAPS to the New Windows LAPS ([Simon Skotheimsvik](https://skotheimsvik.no/author/ss-ga-wordpress))
- Migrating To The New 24H2 LAPS Settings ([Simon Skotheimsvik](https://skotheimsvik.no/author/ss-ga-wordpress))
- Windows LAPS management through Microsoft Intune ([Michael Morten Sonne](https://sonnes.cloud))

### Configuration
1. Install the latest version of Windows LAPS from the Microsoft Intune portal or using PowerShell. [CONFLICT: Simon Skotheimsvik provides an alternative approach for migration]
2. Register the LAPS PowerShell module in your environment by running `Register-LapsProvider -Force`.
3. Configure Group Policy to enable LAPS and set the required settings, such as password length, expiration time, and password history.
4. Deploy the LAPS Group Policy Object (GPO) to the appropriate organizational units (OUs).
5. Ensure that the computers in the targeted OUs have the LAPS client installed and are joined to a domain with Active Directory Rights Management Services (AD RMS) enabled.
6. Verify successful deployment by checking the event logs for Event ID 102 (LAPS Client Installed) and Event ID 103 (LAPS Client Registered).

### Common Pitfalls
- Failing to configure the LAPS GPO correctly, resulting in passwords not being rotated or stored securely.
- Not deploying the LAPS client to all domain-joined computers, leaving some systems vulnerable to unsecured local admin passwords.
- Incorrectly configuring the LAPS policy settings, such as setting a short password expiration time or allowing weak passwords.

### KQL / PowerShell
```powershell
# Get LAPS-managed computers with expired passwords
Get-ADComputer -Filter {ms-Mcs-Admx-Laps-PasswordSettings-LocalAdminPasswordPolicy-ExpirationTimeStamp -lt (Get-Date).AddDays(-7)} | Select Name, ms-Mcs-Admx-Laps-PasswordSettings-LocalAdminPasswordPolicy-ExpirationTimeStamp
```

### Migrating Cloud LAPS to the New Windows LAPS ([Simon Skotheimsvik](https://skotheimsvik.no/author/ss-ga-wordpress))
- The Background
- Different Approaches Migration Cloud LAPS to Windows LAPS
  - Dedicated Admin Account, or not?
    - Rename Existing Administrator [New]
    - Create a Dedicated Administrator [New]
  - Reuse Cloud LAPS Admin, or not?
    - Reuse Cloud LAPS Admin [New]
    - Create New Windows LAPS Admin [New]
- The Migration from Cloud LAPS to the New Windows LAPS
  - Remove Cloud LAPS

### Windows LAPS and management through Microsoft Intune ([Michael Morten Sonne](https://sonnes.cloud))
This section provides additional information on managing Windows LAPS through Microsoft Intune, including technical requirements, how it works, audit logs, troubleshooting, and conclusion. For more details, please refer to the original source: <https://blog.sonnes.cloud/posts/windows-laps-and-management-through-microsoft-intune/>

[CONFLICT: This section is new content not present in the existing entry]