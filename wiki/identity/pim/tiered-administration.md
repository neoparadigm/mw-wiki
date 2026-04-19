---
conflicts: []
context_note: Tiered Administration is part of the identity domain. Synthesised from
  2 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2022-01-13'
  title: Using Windows 365 for Cloud Based Privileged Access Workstations (PAW)
  url: https://danielchronlund.com/2022/01/13/using-windows-365-for-cloud-based-privileged-access-workstations-paw
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2019-10-31'
  title: Improve security and usability of privileged access in Microsoft Azure
  url: https://www.cloud-architekt.net/improve-security-and-usability-privileged-access-azure
stale_after: '2026-07-17'
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
- [Improve security and usability of privileged access in Azure](improve-security-and-usability-of-privileged-access-in-microsoft-azure) recommends using a PAW to separate privileged and productivity workloads, and applying sufficient security baseline for privileged tasks on Device-/OS-level.

### Configuration
- Important: Careful scoping of PAW management and the Windows 365 service in Intune.
- Strict Windows 11 policy hardening using Microsoft security baselines and a custom policy.
- Enable all Defender Attack Surface Reduction rules with Intune.
- Enable Application Control for Windows (WDAC or AppLocker) and block any unwanted applications.
- Use strict Defender SmartScreen blocking to allow required management portal and API URLs and endpoints.
- Ensure admins use separate cloud-only admin accounts, each with their own Windows 365 license and cloud PC.
- Optional: Require these admin accounts to sign in to the Windows 365 portal with FIDO2 security keys.
- [Improve security and usability of privileged access in Azure](improve-security-and-usability-of-privileged-access-in-microsoft-azure) suggests ensuring that all admins have a privileged account for Azure Management which is separated from “productivity” accounts (e.g. internet and mail access) or (high-privileged) on-premises admin accounts.

### Common Pitfalls
- Insufficient hardening of Windows 11 policies and lack of enforcement of Defender rules can lead to increased attack surface.
- Allowing unwanted applications or URLs through Defender SmartScreen can compromise the security of the PAW.
- Sharing admin accounts or using on-prem resources with non-PAW workstations can bypass the intended security measures.
- [Improve security and usability of privileged access in Azure](improve-security-and-usability-of-privileged-access-in-microsoft-azure) warns against using a browser on a productivity (standard) workstation to manage Azure or Microsoft 365 workloads.

### KQL / PowerShell
[This topic does not cover any queries or scripts.]

### Related Topics
- [Tiered Administration](tiered-administration)
- [Privileged Access Workstation (PAW)](paw)
- [Windows 365](windows-365)
- [Microsoft Security Baselines](microsoft-security-baselines)
- [Improve security and usability of privileged access in Azure](improve-security-and-usability-of-privileged-access-in-microsoft-azure)