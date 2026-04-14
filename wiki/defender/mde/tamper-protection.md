---
conflicts:
- '[CONFLICT: Jeffrey provides specific event IDs, but they are not mentioned in the
  existing entry]'
- '[CONFLICT: The existing entry does not mention Microsoft Threat Protection (MTP)
  Dynamic Signatures]'
domain: defender
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-11-03'
  title: 2025 Microsoft Defender Optimization &amp; Configuration Cheat Sheet
  url: https://jeffreyappel.nl/2025-microsoft-defender-optimization-configuration-cheat-sheet
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2026-02-02'
  title: Automatic Windows event auditing configuration for Defender for Identity
    V3.x sensor
  url: https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2023-04-05'
  title: Block &quot;vulnerable/unwanted&quot; applications with Defender for Endpoint
    and Vulnerability Management
  url: https://jeffreyappel.nl/block-vulnerable-unwanted-applications-with-defender-for-endpoint-and-vulnerability-management
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2024-08-05'
  title: How to check for a healthy Defender for Endpoint environment?
  url: https://jeffreyappel.nl/how-to-check-for-a-healthy-defender-for-endpoint-environment
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2022-06-28'
  title: How to upgrade from MMA-based Defender for Endpoint to MDE unified solution
    in Defender for Cloud?
  url: https://jeffreyappel.nl/how-to-upgrade-from-mma-based-defender-for-endpoint-to-mde-unified-solution-in-defender-for-cloud
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-01-04'
  title: How to use Microsoft Security Exposure Management (XSPM)
  url: https://jeffreyappel.nl/how-to-use-microsoft-security-exposure-management-xspm
stale_after: '2026-06-13'
title: MDE Tamper Protection
topic: defender/mde/tamper-protection
---

# MDE Tamper Protection and Automatic Windows event auditing configuration for Defender for Identity V3.x sensor

## MDE Tamper Protection
### Overview
MDE Tamper Protection is a feature in Microsoft Defender designed to prevent unauthorized changes to the security settings and configurations of the Defender service. This feature is crucial for maintaining the integrity and effectiveness of the Defender solution.

### Key Concepts
- Tamper protection
- MDE (Microsoft Defender for Endpoint)
- Unauthorized changes
- Security configuration
- Integrity maintenance

### Configuration
1. Navigate to the Microsoft Endpoint Manager admin center.
2. Go to Tenant administration > Connected apps > Microsoft Defender for Endpoint.
3. Click on Configure and select Tamper Protection.
4. Enable Tamper Protection and configure the settings according to your organization's requirements.

### Common Pitfalls
- Failing to enable Tamper Protection, leaving the Defender configuration vulnerable to unauthorized changes.
- Overly restrictive or overly permissive configurations that may compromise security or hinder legitimate administrative tasks.

## Automatic Windows event auditing configuration for Defender for Identity V3.x sensor

Automatic Windows event auditing configuration for Defender for Identity V3.x sensor is crucial for capturing events, alerting on MDI threats, and collecting information from on-premises systems through the installed sensor.

### Why event auditing for MDI?
Event auditing plays a vital role in effective threat detection, as Microsoft Defender for Identity depends on specific Windows security events to identify identity-based attacks. Audit settings are frequently overlooked. Administrators either forget to configure them or assume the default settings are enough.

To reliably capture high-value security signals, Defender for Identity requires the following audit policies and subcategories to be enabled:

| Audit Category | Audit Policy / Subcategory | Event ID(s) |
| --- | --- | --- |
| Account Logon | Audit Credential  | N/A (The original article does not provide specific event IDs for this category) [CONFLICT: Jeffrey provides specific event IDs, but they are not mentioned in the existing entry] |

### Configuration
N/A (The original article does not provide a configuration section for this topic)

### Common Pitfalls
- Failing to enable the correct Windows Event audit policies, leading to reduced visibility and potential missed threats.

## Block "vulnerable/unwanted" applications with Defender for Endpoint and Vulnerability Management (New information from Jeffrey's article)
Microsoft Defender Vulnerability Management (MDVM) is part of Microsoft Defender for Endpoint P2. When using Defender for Endpoint, there are multiple ways to block vulnerable and unwanted applications. Ideally, there is a dynamic source where all application/ CVEs and vulnerability information is located. In terms of Defender for Endpoint, this part of the product is called Microsoft Security Exposure Management (XSPM).

### Configuration
1. Navigate to the Microsoft Endpoint Manager admin center.
2. Go to Tenant administration > Connected apps > Microsoft Defender for Endpoint.
3. Click on Configure and select App Control.
4. Enable App Control and configure the policies according to your organization's requirements, focusing on blocking vulnerable or unwanted applications.
5. To use Microsoft Security Exposure Management (XSPM), follow the steps outlined in Jeffrey's article: "How to use Microsoft Security Exposure Management (XSPM)"

### Common Pitfalls
- Failing to configure App Control, leaving the Defender configuration vulnerable to unwanted or vulnerable applications.
- Overly restrictive or overly permissive configurations that may compromise security or hinder legitimate application usage.