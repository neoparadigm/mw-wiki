---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-01-13'
  title: Using Windows 365 for Cloud Based Privileged Access Workstations (PAW)
  url: https://danielchronlund.com/2022/01/13/using-windows-365-for-cloud-based-privileged-access-workstations-paw
stale_after: '2026-07-11'
title: Tiered Administration Model T0 T1 T2
topic: identity/pim/tiered-administration
---

# Tiered Administration Model T0 T1 T2

## Tiered Administration Model T0 T1 T2

### Overview
The Enterprise Access model is Microsoft's new approach to security, focusing on cloud and hybrid scenarios for modern IT security. This model is used to create a privileged access plane where Windows 365 cloud PCs act as jump servers for both cloud management and on-prem management, specifically in the context of Privileged Access Workstations (PAW).

### Key Concepts
- Windows 365 PAWs acting as jump servers for various management tools and portals.
- Strict policy hardening using Microsoft security baselines, Defender Attack Surface Reduction rules, Application Control, Defender SmartScreen, and separate cloud-only admin accounts with their own Windows 365 licenses and cloud PCs.

### Configuration
- Important: Careful scoping of PAW management and the Windows 365 service in Intune.
- Strict Windows 11 policy hardening using Microsoft security baselines and a custom policy.
- Enable all Defender Attack Surface Reduction rules with Intune.
- Enable Application Control for Windows (WDAC or AppLocker) and block any unwanted applications.
- Use strict Defender SmartScreen blocking to allow required management portal and API URLs and endpoints.
- Ensure admins use separate cloud-only admin accounts, each with their own Windows 365 license and cloud PC.
- Optional: Require these admin accounts to sign in to the Windows 365 portal with FIDO2 security keys.

### Common Pitfalls
- Inadequate hardening of Windows 11 policies and lack of enforcement of Defender rules can leave the system vulnerable to attacks.
- Allowing unwanted applications or not blocking them properly using Application Control can create potential security risks.
- Failing to use strict Defender SmartScreen blocking can allow unauthorized access to management portals and APIs.
- Using shared admin accounts instead of separate ones for each administrator can compromise the system's security.

### KQL / PowerShell
[Not applicable as the article does not provide any relevant queries or scripts.]

### Related Topics
- [Tiered Administration](tiered-administration)
- [Privileged Access Workstations (PAW)](paw)
- [Windows 365](windows-365)
- [Microsoft Security Baselines](microsoft-security-baselines)