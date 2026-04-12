---
conflicts:
- '[CONFLICT: Ugur Koc does not mention any common pitfalls related to Quick Machine
  Recovery configuration]'
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

The Enrollment Status Page (ESP) is a crucial component in Microsoft Endpoint Manager (MEM) for providing users with real-time information about their device enrollment status. Proper configuration of ESP ensures seamless and efficient device management.

Quick Machine Recovery (QMR) is a powerful new feature introduced in Windows 11 (24H2 Insider Preview) that automatically detects, diagnoses, and repairs critical boot issues leveraging Microsoft’s cloud diagnostics. This detailed guide explains Quick Machine Recovery in-depth and provides clear steps for IT administrators to configure it using Microsoft Intune.

## Key Concepts
- Enrollment Status Page (ESP)
- Microsoft Endpoint Manager (MEM)
- Device enrollment status
- User experience
- Real-time information
- Quick Machine Recovery (QMR)
- Windows 11
- Windows Recovery Environment (WinRE)

## Configuration
1. Navigate to the MEM admin center.
2. Go to Tenant administration > Enrollment > Enrollment settings.
3. Under Enrollment Status Page, select Enable Enrollment Status Page and customize the text and branding as desired.
4. Save changes.

### To configure Quick Machine Recovery with Intune:
#### Prerequisites
- You can test this feature today with the Windows 11 24H2 Insider Preview Beta Channel.
- Devices must be enrolled in Intune and capable of network connectivity (Ethernet or Wi-Fi).

#### Step 1: Create an Intune Custom Configuration Profile
- Navigate to **Microsoft Endpoint Manager Admin Center > Devices > Configuration Profiles > Create Profile**.
- Select **Windows 10 and later** and the **Custom** profile type.

#### Step 2: Configure OMA-URI Settings
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
- **Value:** [Refer to the original source for recommended values]

## Common Pitfalls
- Incorrectly configuring ESP settings may lead to confusion for users regarding their device enrollment status.
- Failing to customize ESP may result in a generic, unbranded page that does not align with the organization's identity.
- [CONFLICT: Ugur Koc does not mention any common pitfalls related to Quick Machine Recovery configuration]

## KQL / PowerShell
[This article does not provide any relevant queries or scripts for Quick Machine Recovery]

## Related Topics
- ESP
- Enrollment status page
- Blocking apps
- Timeout
- ESP error
- Quick Machine Recovery (QMR)