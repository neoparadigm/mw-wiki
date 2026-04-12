---
conflicts: []
domain: defender
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-07-16'
  title: Defender for Office 365 Auto-Remediation of Malicious Messages (AIR)
  url: https://jeffreyappel.nl/defender-for-office-365-auto-remediation-of-malicious-messages-air
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-01-04'
  title: Deploying Defender for Endpoint on iOS with zero-touch onboarding
  url: https://jeffreyappel.nl/deploying-defender-for-endpoint-on-ios-with-zero-touch-onboarding
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-07-10'
  title: Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/downloads-blokkeren-via-conditional-access-app-control
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2024-08-05'
  title: How to check for a healthy Defender for Endpoint environment?
  url: https://jeffreyappel.nl/how-to-check-for-a-healthy-defender-for-endpoint-environment
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-08-17'
  title: Inzage in malware via Cloud App Security en acties via de Microsoft threat
    intelligence engine
  url: https://jeffreyappel.nl/inzage-in-malware-via-cloud-app-security-en-acties-via-de-microsoft-threat-intelligence-engine
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-09-12'
  title: How to onboard Defender for Endpoint using Defender for Cloud
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-onboard-using-defender-for-cloud-part3b
stale_after: '2026-06-11'
title: MDE Tamper Protection
topic: defender/mde/tamper-protection
---

# MDE Tamper Protection and Deploying Defender for Endpoint on iOS with zero-touch onboarding

## MDE Tamper Protection

### Overview
MDE (Microsoft Defender for Endpoint) Tamper Protection is a feature designed to prevent unauthorized changes to the MDE agent configuration and settings, ensuring the integrity of the endpoint security solution.

### Key Concepts
- MDE Agent
- Configuration settings
- Unauthorized changes
- Integrity protection
- Tampering attempts

### Configuration
To enable MDE Tamper Protection:
1. Navigate to the MDE portal.
2. Go to Settings > Endpoint security > Advanced rules.
3. Search for "Tamper Protection" and enable it.
4. Configure the desired settings, such as allowed IP addresses and exclusions.

### Common Pitfalls
- Misconfiguring Tamper Protection settings can lead to false positives or legitimate changes being blocked.
- Failing to update Tamper Protection rules can leave the system vulnerable to tampering attempts.

### KQL / PowerShell
N/A (The article does not provide any relevant queries or scripts.)

### Related Topics
- [Tamper protection](tamper_protection)
- [MDE](mde)
- [Disable Defender](disable_defender)
- [Sensor](sensor)
- [MsSense](ms_sense)

## Deploying Defender for Endpoint on iOS with zero-touch onboarding

### Overview
This section has been updated with new information from the source "Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint Manager" by Jeffrey. The article explains how to block downloads on iOS devices using Conditional Access App Control (CAAC) within Microsoft Endpoint Manager (MEM). This method allows for zero-touch onboarding of Defender for Endpoint on iOS devices.

### Key Concepts
- Conditional Access App Control (CAAC)
- Zero-touch onboarding
- Download blocking
- MEM (Microsoft Endpoint Manager)

### Configuration
To block downloads on iOS devices using CAAC:
1. Navigate to the MEM admin center.
2. Go to Tenant administration > Conditional Access > App Control policies.
3. Create a new policy or edit an existing one, and configure the following settings:
   - Platform: iOS/iPadOS
   - Apps: All apps
   - Conditions: User and device compliance
   - Controls: Block downloads
4. Assign the policy to the appropriate group of users or devices.

### Common Pitfalls
- Failing to properly configure CAAC policies can result in unintended blocking of legitimate downloads.
- Not testing the policy before deployment can lead to unexpected issues.

### KQL / PowerShell
N/A (The article does not provide any relevant queries or scripts.)

### Related Topics
- [Conditional Access App Control](conditional_access_app_control)
- [Microsoft Endpoint Manager](microsoft_endpoint_manager)
- [Zero-touch onboarding](zero_touch_onboarding)
- [Download blocking](download_blocking)

## How to onboard Defender for Endpoint using Defender for Cloud (New Source)

### Overview
This new section provides information from the source "Microsoft Defender for Endpoint series – Onboard using Defender for Cloud – Part3B" by Jeffrey. The article explains how to onboard Defender for Endpoint using Defender for Cloud, focusing on Windows Servers.

### Key Concepts
- Defender for Cloud
- Defender for Servers
- Microsoft Defender for Endpoint Plan 2

### Configuration
To onboard Defender for Endpoint using Defender for Cloud:
1. Navigate to the Azure portal.
2. Go to Security > Defender for Cloud.
3. Click Onboard servers and follow the instructions provided.

### Common Pitfalls
- Failing to properly configure Defender for Cloud can result in issues with onboarding or functionality.
- Not understanding the differences between Defender for Cloud plans may lead to incorrect onboarding or insufficient protection.

### KQL / PowerShell
N/A (The article does not provide any relevant queries or scripts.)

### Related Topics
- [Defender for Cloud](defender_for_cloud)
- [Defender for Servers](defender_for_servers)
- [Microsoft Defender for Endpoint Plan 2](microsoft_defender_for_endpoint_plan_2)