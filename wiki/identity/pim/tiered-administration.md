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
The Enterprise Access model is Microsoft's new approach to security, focusing on cloud and hybrid scenarios for modern IT security. This model introduces a tiered administration structure (T0, T1, T2) that helps organizations manage access to sensitive resources based on the level of trust and risk associated with each user or group.

### Key Concepts
- Tiered Administration Model: A three-tier system for managing access to sensitive resources in a cloud and hybrid environment.
- T0, T1, T2: The three tiers in the Enterprise Access model, representing different levels of trust and risk.
- Privileged Access Workstations (PAW): Dedicated workstations used by administrators for performing administrative tasks in the cloud and on-premises.

### Configuration
The article does not provide specific configuration guidance for the tiered administration model. However, it suggests using Windows 365 for cloud-based PAWs as a part of the privileged access plane.

### Common Pitfalls
- Insufficient hardening of Windows 365 PAWs can lead to security vulnerabilities.
- Misconfigurations in Intune or other management tools can result in unwanted applications being allowed on the PAWs.
- Lack of strict Defender SmartScreen blocking can expose administrators to phishing attacks and malicious URLs.

### KQL / PowerShell
The article does not include any relevant queries or scripts for the tiered administration model.

### Related Topics
- [Tiered Administration](tiered-administration)
- [T0](t0)
- [T1](t1)
- [T2](t2)
- [Privileged Access Workstations (PAW)](paw)