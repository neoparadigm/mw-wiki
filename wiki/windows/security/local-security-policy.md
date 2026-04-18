---
conflicts: []
context_note: Local Security Policy is part of the windows domain. Synthesised from
  1 community source.
domain: windows
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-06-02'
  title: How To Configure Audit Policy For Registry Object Access In Windows Using
    Intune HTMD Blog
  url: https://www.anoopcnair.com/audit-policy-for-registry-object-access-intune
stale_after: '2026-07-17'
title: Local Security Policy and CIS Hardening
topic: windows/security/local-security-policy
---

# Local Security Policy and CIS Hardening

## Overview
The Local Security Policy and CIS Hardening is a crucial aspect of Windows system security, focusing on configuring settings to enhance system protection against threats and meet compliance requirements.

## Key Concepts
- Local Security Policy: A Microsoft Management Console (MMC) snap-in that allows administrators to configure security settings for a local or domain computer.
- CIS Hardening: A set of guidelines and best practices for securing Windows systems, developed by the Center for Internet Security (CIS).
- Security benchmark: A standardized set of requirements for system security, used to evaluate and improve the security posture of a system.
- AppLocker: A Microsoft application control technology that helps prevent unauthorized applications from running on a system.
- Windows hardening: The process of securing a Windows operating system by reducing its attack surface and increasing its resistance to threats.

## Configuration
To configure the Local Security Policy for CIS Hardening, follow these steps:

1. Open Local Group Policy Editor: Run `gpedit.msc` in the Start menu search bar.
2. Navigate to Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options.
3. Apply the recommended settings from the CIS Microsoft Windows Server 2016 Benchmark (Level 1) or other applicable benchmarks.

## Common Pitfalls
- Incorrectly configuring security settings can lead to system instability, reduced functionality, or increased vulnerability. Always test changes in a controlled environment before deploying them to production systems.
- Failing to regularly review and update security policies can leave systems vulnerable to new threats.

## KQL / PowerShell
This article does not provide any specific queries or scripts related to KQL (Kusto Query Language) or PowerShell.

## Related Topics
- Local Security Policy
- CIS Hardening
- Security benchmark
- AppLocker
- Windows hardening