---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2025-04-14'
  title: Windows Hotpatch for Intune Admins - Ugur Koc
  url: https://ugurkoc.de/windows-hotpatch-for-intune-admins
stale_after: '2026-07-11'
title: Credential Guard and VBS
topic: intune/security/credential-guard
---

# Credential Guard and VBS

## Overview
Credential Guard and Virtualization-Based Security (VBS) are security features in Windows 10 and Windows Server 2016 designed to protect credentials and sensitive data from credential theft attacks, such as Pass-the-Hash and Pass-the-Ticket. These features are crucial for maintaining the integrity of enterprise environments.

## Key Concepts
- Credential Guard: A security feature that isolates the Local Security Authority Subsystem Service (LSASS) process in a secure virtual environment, protecting credentials from credential theft attacks.
- Virtualization-Based Security (VBS): An umbrella term for several Windows security features, including Credential Guard, Device Guard, and Secure Boot, that utilize virtualization to enhance system security.
- LSASS Protection: The process of isolating the LSASS process in a secure virtual environment to protect it from credential theft attacks.
- Pass-the-Hash (PtH): A type of attack where an attacker extracts hashed passwords from memory and uses them to gain unauthorized access to systems or resources.
- Pass-the-Ticket (PtT): A type of attack where an attacker steals Kerberos Tickets from the LSASS process memory and uses them for unauthorized access.

## Configuration
To configure Credential Guard and VBS, follow these steps:

1. Enable Secure Boot in UEFI settings.
2. Enable Virtualization in BIOS/UEFI settings.
3. Install the latest Windows updates.
4. Configure Group Policy or Local Security Policy to enable Credential Guard and Device Guard.
5. Restart the system for changes to take effect.

## Common Pitfalls
- Incorrectly configuring Secure Boot, Virtualization, or other prerequisites can prevent Credential Guard from functioning correctly.
- Failing to install the latest Windows updates may result in compatibility issues with Credential Guard and VBS.
- Improper configuration of Group Policy or Local Security Policy can lead to errors or unexpected behavior.

## KQL / PowerShell
[This article does not provide any specific queries or scripts related to Credential Guard and VBS configuration.]

## Related Topics
- [Credential Guard](wiki:Credential_Guard)
- [VBS](wiki:Virtualization-Based_Security)
- [virtualisation-based security](wiki:Virtualization-Based_Security)
- [LSASS protection](wiki:LSASS_Protection)
- [Pass-the-Hash](wiki:Pass-the-Hash)