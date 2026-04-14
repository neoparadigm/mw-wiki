---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests that inadequate monitoring of Intune policy
  configuration changes can lead to unintended or accidental modifications, while
  the existing entry does not mention this specifically.]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2022-01-13'
  title: Using Windows 365 for Cloud Based Privileged Access Workstations (PAW)
  url: https://danielchronlund.com/2022/01/13/using-windows-365-for-cloud-based-privileged-access-workstations-paw
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2022-07-19'
  title: Monitoring Intune policy configuration changes
  url: https://oliverkieselbach.com/2022/07/19/monitoring-intune-policy-configuration-changes
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2023-02-14'
  title: Microsoft Defender for Endpoint series – Tips and tricks/ common mistakes
    – Part10
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-tips-and-tricks-common-mistakes-part10
stale_after: '2026-07-13'
title: Tiered Administration Model T0 T1 T2
topic: identity/pim/tiered-administration
---

# Tiered Administration Model T0 T1 T2

## Tiered Administration Model T0 T1 T2

### Overview
The Enterprise Access model is Microsoft's new approach to security, focusing on cloud and hybrid scenarios for modern IT security. This model is used to create a privileged access plane where Windows 365 cloud PCs act as jump servers for both cloud management and on-prem management, specifically in the context of Privileged Access Workstations (PAW).

### Key Concepts
- Windows 365 PAWs acting as jump servers for various management tools and portals.
- Hardening Windows 11 policies using Microsoft security baselines and custom policies.
- Enabling Defender Attack Surface Reduction rules, Application Control (WDAC or AppLocker), Defender SmartScreen, and strict URL blocking.
- Using separate cloud-only admin accounts with their own Windows 365 licenses and cloud PCs.
- Optional: Requiring admin accounts to sign in to the Windows 365 portal with FIDO2 security keys.
- [Monitoring Intune policy configuration changes](#monitoring-intune-policy-configuration-changes) for a certain set of policies, specifically those starting with "Win – PAW" following a naming scheme.
- [CONFLICT: Oliver Kieselbach suggests that inadequate monitoring of Intune policy configuration changes can lead to unintended or accidental modifications, while the existing entry does not mention this specifically.]
- [New] Tips and tricks for Defender for Endpoint from Jeffrey's blog series (Part 10)

### Configuration
- Important: Careful scoping of PAW management and the Windows 365 service in Intune.
- Strict Windows 11 policy hardening using Microsoft security baselines and a custom policy.
- Enable all Defender Attack Surface Reduction rules with Intune.
- Enable Application Control for Windows (WDAC or AppLocker) and block any unwanted applications.
- Use strict Defender SmartScreen blocking to allow required management portal and API URLs and endpoints.
- Ensure all admins use separate cloud-only admin accounts, each with their own Windows 365 license and cloud PC.
- Optional: Require these admin accounts to sign in to the Windows 365 portal with FIDO2 security keys.
- Configure Intune Diagnostic settings to ship AuditLogs to a Log Analytics workspace for monitoring policy changes, specifically those starting with "Win – PAW".
- [New] Tips and tricks from Jeffrey's blog series (Part 10) for Defender for Endpoint configuration.

### Common Pitfalls
- Inadequate hardening of Windows 11 policies can leave attack surfaces open.
- Failure to block unwanted applications using Application Control (WDAC or AppLocker) can lead to potential security risks.
- Lax Defender SmartScreen blocking can allow unauthorized access to management portals and APIs.
- Sharing admin accounts can compromise security and accountability.
- [CONFLICT: Oliver Kieselbach suggests that inadequate monitoring of Intune policy configuration changes can lead to unintended or accidental modifications, while the existing entry does not mention this specifically.]
- [New] Common mistakes during Defender for Endpoint deployments on the Windows platform from Jeffrey's blog series (Part 10).

### KQL / PowerShell
N/A - The article does not provide any relevant queries or scripts in this context.

### Related Topics
- [Tiered Administration](tiered_administration)
- [Privileged Access Workstations (PAW)](paw)
- [Windows 365](windows_365)
- [Microsoft Security Baselines](microsoft_security_baselines)
- [Monitoring Intune policy configuration changes](#monitoring-intune-policy-configuration-changes)
- [Jeffrey's Microsoft Defender for Endpoint series – Tips and tricks/ common mistakes](jeffreys_mde_tips_tricks)