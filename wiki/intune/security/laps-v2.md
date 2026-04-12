---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-10-15'
  title: Recap Ignite 2022 &#8211; New Intune related announcements
  url: https://jannikreinhard.com/2022/10/15/recap-ignite-2022-new-intune-related-announcements
stale_after: '2026-06-11'
title: Windows LAPS v2 Configuration
topic: intune/security/laps-v2
---

# Windows LAPS v2 Configuration

## Overview
Windows LAPS v2 Configuration is an update to the Local Administrator Password Solution (LAPS) that allows for more efficient and secure management of local administrator passwords on Windows devices. This update matters because it enhances security by rotating local admin passwords, reducing the risk of unauthorized access.

## Key Concepts
- Windows LAPS v2: The updated version of Local Administrator Password Solution that supports password rotation and cloud management.
- Local Administrator Password: The password used for local administrators on Windows devices, which should be regularly rotated to maintain security.
- Password Rotation: The process of changing a password at regular intervals to prevent unauthorized access.
- LAPS Policy: A policy that defines the settings and rules for managing local administrator passwords using LAPS.

## Configuration
1. Install the latest version of LAPS from the Microsoft Download Center.
2. Configure Group Policy Object (GPO) to enable LAPS for the desired organizational units (OUs).
3. Create a LAPS policy and link it to the appropriate GPO.
4. Configure the password rotation settings in the LAPS policy, such as the frequency of password changes and the length of the new passwords.
5. Deploy the GPO to the desired devices.
6. Verify that the LAPS agent is installed on the devices and that they are reporting passwords to Active Directory.

## Common Pitfalls
- Failing to update to the latest version of LAPS, which may not support all features or have known security vulnerabilities.
- Not configuring the GPO correctly, resulting in incorrect settings or devices not receiving the policy.
- Incorrectly setting password rotation frequencies, which could lead to either too frequent changes (impacting productivity) or insufficient changes (reducing security).

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to Windows LAPS v2 Configuration.]

## Related Topics
- LAPS
- Local admin password
- LAPS v2
- Password rotation
- LAPS policy