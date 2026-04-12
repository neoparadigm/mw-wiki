---
conflicts:
- '[CONFLICT: Jeffrey''s article does not mention Endpoint Manager as a requirement]'
- '[CONFLICT: Jeffrey says X, existing entry says Y]'
- '[CONFLICT: Jeffrey''s new source does not provide any information about Enrollment
  Status Page Configuration]'
- '[CONFLICT: Jeffrey''s new source provides information about Defender for Endpoint
  Advanced Hunting and custom detections, which is not present in the existing entry]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-01-20'
  title: 'How To: Optimize Office 365 Network Performance'
  url: https://danielchronlund.com/2021/01/20/how-to-optimize-office-365-network-performance
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2025-03-31'
  title: How to enable and configure Quick Machine Recovery with Intune - Ugur Koc
  url: https://ugurkoc.de/how-to-enable-and-configure-quick-machine-recovery-with-intune
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2024-08-25'
  title: 'Azure AI Search: Deploying a Powerful AI-Powered Search Engine'
  url: https://jannikreinhard.com/2024/08/25/azure-ai-search-deploying-a-powerful-ai-powered-search-engine
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-11-10'
  title: Manage Device control with Microsoft Defender for Endpoint and Endpoint Manager
  url: https://jeffreyappel.nl/manage-device-control-with-microsoft-defender-for-endpoint-and-endpoint-manager-part-1
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2023-01-23'
  title: Defender for Endpoint Advanced Hunting and custom detections
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-advanced-hunting-and-custom-detections-part8
stale_after: '2026-06-11'
title: Enrollment Status Page Configuration
topic: intune/deployment/enrollment-status-page
---

# Enrollment Status Page Configuration and Quick Machine Recovery with Intune

## Enrollment Status Page Configuration

### Overview
The Enrollment Status Page (ESP) is a crucial component in Microsoft Endpoint Manager (MEM) for providing users with real-time information about their device enrollment status. Proper configuration ensures seamless and efficient device management.

### Key Concepts
- Enrollment Status Page (ESP)
- Device enrollment status
- Real-time user feedback
- MEM Configuration Manager
- Conditional Access policies

### Configuration
1. In the MEM admin center, navigate to Tenant administration > Connectors and tokens > Enrollment status page.
2. Select Edit and customize the text as needed for your organization.
3. Save changes and assign the ESP URL to users through Conditional Access policies or other deployment methods.

### Common Pitfalls
- Incorrectly configured ESP may lead to user confusion and frustration during device enrollment.
- Failing to update the ESP with relevant information can result in outdated or misleading feedback for users.

### KQL / PowerShell (New addition)
N/A (The source article does not provide any queries or scripts related to ESP configuration.)

[CONFLICT: Jeffrey's new source does not provide any information about Enrollment Status Page Configuration]

## Quick Machine Recovery with Intune

**Quick Machine Recovery (QMR)** is a powerful new feature introduced in Windows 11 (24H2 Insider Preview) that automatically detects, diagnoses, and repairs critical boot issues leveraging Microsoft’s cloud diagnostics. This detailed guide explains Quick Machine Recovery in-depth and provides clear steps for IT administrators to configure it using Microsoft Intune.

### How to Configure Quick Machine Recovery with Microsoft Intune

Follow this detailed step-by-step guide to configure Quick Machine Recovery:

#### Prerequisites
- You can test this feature today with the Windows 11 24H2 Insider Preview Beta Channel.
- Devices must be enrolled in Intune and capable of network connectivity (Ethernet or Wi-Fi).

#### Creating an Intune Custom Configuration Profile

1. Navigate to **Microsoft Endpoint Manager Admin Center > Devices > Configuration Profiles > Create Profile**.
2. Select **Windows 10 and later** and the **Custom** profile type.

#### Configuring OMA-URI Settings

**Enable Cloud Remediation:**

- **OMA-URI:** `./Device/Vendor/MSFT/RemoteRemediation/CloudRemediationSettings/EnableCloudRemediation`
- **Data type:** Boolean
- **Value:** `True`

**Enable Automatic Remediation (optional but strongly recommended):**

- **OMA-URI:** `./Device/Vendor/MSFT/RemoteRemediation/CloudRemediationSettings/AutoRemediationSettings/EnableAutoRemediation`
- **Data type:** Boolean
- **Value:** `True`

**Set Retry Interval:**

- **OMA-URI:** `./Device/Vendor/MSFT/RemoteRemediation/CloudRemediationSettings/AutoRemediationSettings/SetRetryInterval`
- **Data type:** Integer
- **Value:** (Optional) Set the retry interval in seconds. Default is 600 seconds (10 minutes).

### Common Pitfalls
- Incorrectly configured QMR settings may lead to issue

## Defender for Endpoint Advanced Hunting and custom detections (New addition)

Defender for Endpoint Advanced Hunting and custom detections

[March 30, 2026](https://jeffreyappel.nl/automatic-migration-from-defender-for-identity-sensor-v2-to-v3-x-and-gmsa-changes/)

9 min read

[March 23, 2026](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/)

7 min read

[February 12, 2026](https://jeffreyappel.nl/how-to-secure-microsoft-copilot-studio-agents-with-real-time-protection/)

13 min read

[February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)

9 min read

[February 2, 2026](https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x/)

5 min read

[January 20, 2026](https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years/)

10 min read

[January 6, 2026](https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage/)

4 min read


## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Microsoft Defender for Endpoint series – Advanced hunting and custom detections – Part8

[Security](https://jeffreyappel.nl/category/security/)

# Microsoft Defender for Endpoint series – Advanced hunting and custom detections – Part8

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[January 23, 2023](https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-advanced-hunting-and-custom-detections-part8/)
1


12 min read

It is time for part 8 of the Microsoft Defender for Endpoint (MDE) series. Part 8 is focused on the hunting experience in Microsoft 365 Defender. The advanced hunting feature and custom detection feature are part of the security.microsoft.com portal. Advanced hunting is based on the **K**usto **Q**uery **L**anguage (KQL).

NOTE: The blog series focuses on features in **Microsoft Defender for Endpoint P2** all **Microsoft Defender for Endpoint P1** features are available in P2.

**Specific question or content idea part of Defender for Endpoint? Use the [contact submission](https://jeffreyappel.nl/contact-form-content-request/) form and share the post ideas.**

## Introduction

Defender for Endpoint is part of Microsoft 365 Defender. The portal contains different sections and data. Advanced hunting is a query-based tool that lets you explore all raw data. Each configured sensor sends telemetry and events directly to the Defender instance. Device events and alertinfo / alert evidence data is a directory available.

This part of the series is focussing on hunting with advanced hunting in Microsoft 365 Defender and the creation of custom detections.

Custom detections are powerful and can be used for improving the security response with automated device/ user actions and designing/creating more alerts for specific situations/ performed actions based on customer behavior or known blind spots based on MDE

[CONFLICT: Jeffrey's new source provides information about Defender for Endpoint Advanced Hunting and custom detections, which is not present in the existing entry]