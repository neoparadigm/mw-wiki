---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-07-24'
  title: From Intune to EntraID - Add custom data to the Extension Attributes - Ugur
    Koc
  url: https://ugurkoc.de/from-intune-to-entraid-add-custom-data-to-the-extension-attributes
stale_after: '2026-06-11'
title: Autopilot User-Driven Mode
topic: intune/deployment/autopilot-user-driven
---

# Autopilot User-Driven Mode

## Autopilot User-Driven Mode

Autopilot User-Driven Mode is a feature in Microsoft Endpoint Manager (MEM) that allows users to enroll their devices into Intune during the Out-of-Box Experience (OOBE). This mode provides a self-service option for users to join their devices to Azure Active Directory (AAD) and configure them according to organizational policies.

## Key Concepts
- Autopilot User-Driven Mode
- Self-service device enrollment
- Out-of-Box Experience (OOBE)
- Azure Active Directory (AAD) join
- Hybrid AAD join

## Configuration
1. Enable Autopilot User-Driven Mode in the MEM admin center.
2. Configure Autopilot deployment profiles to include user-driven settings.
3. Assign the profile to a device collection or user group.
4. Users can then enroll their devices during OOBE by following the on-screen instructions.

## Common Pitfalls
- Ensuring that the device is compatible with Autopilot User-Driven Mode.
- Properly configuring the Autopilot deployment profile to include user-driven settings.
- Assigning the profile to an incorrect device collection or user group.

## KQL / PowerShell
[This topic does not provide any relevant queries or scripts]

## Related Topics
- [Autopilot](autopilot)
- [User-Driven](user-driven)
- [OOBE](oobe)
- [Entra join](entra-join)
- [Hybrid join](hybrid-join)