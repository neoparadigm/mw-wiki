---
conflict_topics:
- intune/reporting/intune-reporting-log-analytics
- intune/security/bitlocker-management
conflicts:
- '[CONFLICT: Jeffrey''s source mentions additional protection layers in Defender,
  but the existing entry does not explicitly mention this term.]'
context_note: Attack Surface Reduction is part of the intune domain. It connects closely
  to Azure Monitor Log Analytics. Synthesised from 3 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- azure/monitoring/azure-monitor-log-analytics
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-11-10'
  title: Manage Device control with Microsoft Defender for Endpoint and Endpoint Manager
  url: https://jeffreyappel.nl/manage-device-control-with-microsoft-defender-for-endpoint-and-endpoint-manager-part-1
- author: limwainstein
  crawled: '2026-04-18'
  date: '2025-10-20'
  title: Understand and use attack surface reduction - Microsoft Defender for Endpoint
  url: https://learn.microsoft.com/en-us/defender-endpoint/overview-attack-surface-reduction
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-11-08'
  title: Configure Attack Surface reduction and additional protection in Defender
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-attack-surface-reduction-and-additional-protection-part4b
stale_after: '2026-06-17'
title: Attack Surface Reduction Policies
topic: intune/security/attack-surface-reduction
---

# Attack Surface Reduction Policies

## Attack Surface Reduction Policies

Attack Surface Reduction (ASR) policies are a set of rules in Microsoft Defender for Endpoint designed to help protect against known and unknown threats by reducing the attack surface available to attackers. These policies are crucial for securing Windows devices from various types of attacks, including those that exploit common vulnerabilities or use malicious software.

## Key Concepts
- Attack Surface Reduction (ASR)
- ASR rules
- Controlled folder access
- Network protection
- EDR (Endpoint Detection and Response)
- ASR policies configuration
- Hardware-based isolation for Microsoft Edge
- Application control
- Device control
- Web protection
- Exploit protection
- Windows Firewall with advanced security

## Configuration
1. Navigate to the Microsoft Endpoint Manager admin center portal.
2. Go to **Endpoint Security > Attack Surface Reduction**.
3. Click on **Create Policy**.
4. Configure the platform with the value; **Windows 10 and later**. For the profile select **Device control**.
5. Fill in the required name and optional description.
6. Configure the setting **Block removable storage** with the value **Yes.**
7. To enable hardware-based isolation for Microsoft Edge, follow [this guide](/en-us/windows/security/threat-protection/microsoft-defender-application-guard/install-md-app-guard).
8. For application control, review base policies in Windows, see [Example Base Policies](/en-us/windows/security/threat-protection/windows-defender-application-control/example-wdac-base-policies). Refer to the [Windows Defender Application Control design guide](/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide) and [Deploying Windows Defender Application Control (WDAC) policies](/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).
9. To enable controlled folder access, follow [this guide](enable-controlled-folders).
10. Enable device control by following the [overview](device-control-overview).
11. Turn on network protection using [this guide](enable-network-protection).
12. Enable web protection using [this overview](web-protection-overview).
13. Enable exploit protection using [this guide](enable-exploit-protection).
14. Set up your network firewall by getting an overview of [Windows Firewall with advanced security](/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security) and using the [Windows Firewall design guide](/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security-design-guide) to decide how you want to design your firewall policies. Use the [Windows Firewall deployment guide](/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-wit)

## Common Pitfalls
- Not configuring ASR policies properly can leave devices vulnerable to attacks.

## Additional Protection Layers in Defender (New Information from the new source)
- Configure Attack Surface reduction and additional protection in Defender: [March 30, 2026](https://jeffreyappel.nl/automatic-migration-from-defender-for-identity-sensor-v2-to-v3-x-and-gmsa-changes/)
- Defending with Microsoft: A deep dive into the Microsoft Defender suite blog series intro: [March 23, 2026](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/)
- How to secure Microsoft Copilot Studio agents with real-time protection: [February 12, 2026](https://jeffreyappel.nl/how-to-secure-microsoft-copilot-studio-agents-with-real-time-protection/)
- How to protect Microsoft Teams with Microsoft 365 Defender: [February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)
- Automatic Windows Event Auditing Configuration for Defender for Identity v3 x: [February 2, 2026](https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x/)
- How to archive Defender logs natively in Defender XDR up to 12 years: [January 20, 2026](https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years/)
- Microsoft Sentinel cost management: How to get insights in data lake usage: [January 6, 2026](https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage/)

[CONFLICT: Jeffrey's source mentions additional protection layers in Defender, but the existing entry does not explicitly mention this term.]