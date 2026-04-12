---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-02-26'
  title: How to Automate Renewal of Android Dedicated Devices Enrollment Tokens and
    QR Codes in MEM (Solve the 90 Day Limit Issue)
  url: https://danielchronlund.com/2020/02/26/how-to-automate-renewal-of-android-dedicated-devices-enrollment-tokens-and-qr-codes-in-mem-solve-the-90-day-limit-issue
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-02-09'
  title: Microsoft 365 Data Exfiltration &#8211; Attack and Defend
  url: https://danielchronlund.com/2023/02/09/microsoft-365-data-exfiltration-attack-and-defend
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-02-14'
  title: The Threat of Microsoft 365 Wiper Malware
  url: https://danielchronlund.com/2023/02/14/the-threat-of-microsoft-365-wiper-malware
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-03-07'
  title: Get All Assignments in Intune for a User, Group or Device - Ugur Koc
  url: https://ugurkoc.de/get-all-assignments-in-intune-for-a-user-group-or-device
stale_after: '2026-06-11'
title: Service Principal and App Registration Governance
topic: identity/entra-id/service-principal-governance
---

# Service Principal and App Registration Governance

## Service Principal and App Registration Governance
This topic discusses the automation of renewing Android Dedicated Devices enrollment tokens and QR codes in Microsoft Endpoint Manager (MEM) to overcome the 90-day limit issue using Microsoft Graph and PowerShell. It also includes a new section on Microsoft 365 Data Exfiltration, based on the articles "Microsoft 365 Data Exfiltration - Attack and Defend" and "The Threat of Microsoft 365 Wiper Malware" by Daniel Chronlund.

The new source article, "Get All Assignments in Intune for a User, Group or Device - Ugur Koc", adds information about a tool that helps get an overview of all assignments in Intune based on search criteria for users, groups, or devices. This section will be incorporated into the existing Microsoft 365 Data Exfiltration and Wiper Malware section as it pertains to the potential risks of insecure app registrations with privileged API permissions assigned.

## Key Concepts
- Android Enterprise corporate-owned dedicated devices enrollment tokens
- 90-day lifetime of Android enrollment tokens
- Automatic renewal of Android enrollment tokens via Microsoft Graph and PowerShell
- Microsoft Graph endpoint documentation for Intune Android enrollment token creation
- Azure AD application permissions and delegated permissions for renewing tokens
- Connecting to Microsoft Graph as an Intune Admin in PowerShell
- Microsoft 365 Data Exfiltration, potential risks of insecure app registrations with privileged API permissions assigned, including the threat of wiper malware
- Tools like Intune Assignment Checker for getting an overview of all assignments in Intune based on search criteria

## Configuration
1. Connect to Microsoft Graph as an Intune Admin using PowerShell functions.
2. Authenticate to Microsoft Graph with the Intune admin account.
3. List all Android enrollment profiles and get the profile ID of a specific Android enrollment profile.
4. Use the Microsoft Graph endpoint to renew the Android enrollment token for the specified profile.

## Common Pitfalls
- Using application permissions instead of delegated permissions when renewing tokens.
- Not signing in with an Intune admin account when using delegated permissions.
- Insecure app registrations with privileged API permissions assigned, leading to potential data exfiltration and wiper malware risks.
- Lack of visibility into the assignments of a user or an entire Entra ID group in the Intune Portal without tools like Intune Assignment Checker.

## KQL / PowerShell
[Not applicable as this article does not provide any queries or scripts.]

## Microsoft 365 Data Exfiltration and Wiper Malware
This section is based on the articles "Microsoft 365 Data Exfiltration - Attack and Defend" by Daniel Chronlund, "The Threat of Microsoft 365 Wiper Malware" by Daniel Chronlund, and "Get All Assignments in Intune for a User, Group or Device - Ugur Koc". It discusses the risks of insecure app registrations with privileged API permissions assigned, leading to potential data exfiltration and wiper malware. The script **Invoke-DCM365DataExfiltration** can be used as a proof of concept to showcase how an attacker can perform data exfiltration with Microsoft Graph, while **Invoke-DCM365DataWiper** is a tool that demonstrates the potential threat of wiper malware in Microsoft 365 environments. The Intune Assignment Checker tool helps get an overview of all assignments in Intune based on search criteria to mitigate these risks.

**This script is a proof of concept and for testing purposes only. Do not use these scripts in an unethical or unlawful way. Don’t be stupid!**

## Related Topics
- [Se

The updated wiki entry includes new information from the Ugur Koc article about the Intune Assignment Checker tool, which helps get an overview of all assignments in Intune based on search criteria for users, groups, or devices. This information has been incorporated into the Microsoft 365 Data Exfiltration and Wiper Malware section as it pertains to the potential risks of insecure app registrations with privileged API permissions assigned. The existing entry remains unchanged in other sections.