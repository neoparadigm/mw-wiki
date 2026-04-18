---
conflict_topics:
- intune/compliance/custom-compliance
- intune/apps/winget-intune
conflicts:
- '[CONFLICT: Misstep: IT departments enrolling devices on behalf of users, introducing
  a hidden compliance risk. This contradicts the existing entry''s common pitfall
  about requiring Bitlocker causing delays.]'
context_note: Compliance Policy Design is part of the intune domain. Synthesised from
  3 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2021-11-15'
  title: Managing Windows Bitlocker Compliance Policy Using Intune | MS Graph | Grace
    Period HTMD Blog
  url: https://www.anoopcnair.com/bitlocker-compliance-policy-using-intune
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2025-09-01'
  title: Simon does The Hidden Intune Enrolled User Exists Check You’re Missing
  url: https://skotheimsvik.no/the-hidden-intune-enrolled-user-exists-check-youre-missing
- author: lenewsad
  crawled: '2026-04-18'
  date: '2026-04-15'
  title: Device compliance policies in Microsoft Intune - Microsoft Intune
  url: https://learn.microsoft.com/en-us/mem/device-security/compliance/overview
stale_after: '2026-06-17'
title: Compliance Policy Design and CA Integration
topic: intune/compliance/compliance-policy-design
---

# Compliance Policy Design and CA Integration

## Compliance Policy Design and CA Integration

### Overview
This topic discusses managing Windows Bitlocker compliance policy using Intune and MS Graph, focusing on the enforcement of Bitlocker encryption via Intune compliance policy and the associated challenges with Intune compliance settings for Bitlocker. The article also explores a method to implement Bitlocker without requiring a reboot and allowing users to access corporate resources immediately after AutoPilot enrollment.

### Key Concepts
- Bitlocker Compliance Policy Settings in Intune (MEM)
  - "Require Bitlocker" under Device Health
  - "Require encryption of data storage on device" under System Security
- Intune Actions For Noncompliance and Grace period
- [**New Information: Critical Intune Enrolled User Exists Compliance Check**]
- [**New Information: Intune-CheckDeviceEnrolledBy.ps1 script for identifying devices with mismatched enrollment**]

### Configuration
The article does not provide step-by-step configuration guidance. It is assumed that the reader already has Bitlocker deployed and working, and the focus is on managing compliance policy settings in Intune.

### Common Pitfalls
- Both "Require Bitlocker" and "Require encryption of data storage on device" settings have drawbacks:
  - "Require Bitlocker" requires a reboot after AutoPilot enrollment, causing delays for users.
  - "Require encryption of data storage on device" can cause significant delays in user productivity when combined with conditional access.
- [**New Information: Misstep: IT departments enrolling devices on behalf of users, introducing a hidden compliance risk.**]
- [CONFLICT: Misstep: IT departments enrolling devices on behalf of users, introducing a hidden compliance risk. This contradicts the existing entry's common pitfall about requiring Bitlocker causing delays.]

### KQL / PowerShell
No specific queries or scripts are provided in the article.

### Related Topics
- compliance policy
- compliant device
- grace period
- non-compliant
- compliance CA
- Enrolled User Exists Compliance Check
- [**New Information: Intune-CheckDeviceEnrolledBy.ps1 script for identifying devices with mismatched enrollment**]