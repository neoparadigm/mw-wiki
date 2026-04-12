---
conflicts: []
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

### KQL / PowerShell
N/A (The source article does not provide any queries or scripts related to ESP configuration.)

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
- Incorrectly configured QMR settings may lead to issues with device recovery.
- Failing to update QMR settings can result in outdated or ineffective recovery for devices.

### KQL / PowerShell
N/A (The source article does not provide any queries or scripts related to QMR configuration.)

### Related Topics
- ESP
- Enrollment status page
- Blocking apps
- Timeout
- ESP error
- Quick Machine Recovery
- Windows 11
- Intune
- Cloud diagnostics