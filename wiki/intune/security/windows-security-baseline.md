---
conflict_topics:
- sentinel/architecture/cost-optimization
- intune/security/wdac-app-control
conflicts:
- '[CONFLICT: Anoop C Nair does not mention Policy and Profile Manager, but it is
  a built-in role required for managing baselines in Intune.]'
- '[CONFLICT: Anoop C Nair mentions that older profiles become read-only but can be
  updated to the latest version for editing, while existing entry does not mention
  this.]'
- '[CONFLICT: Anoop C Nair does not mention deploying the created security baseline,
  but it is an essential step.]'
- '[CONFLICT: Anoop C Nair does not mention incorrect configuration of settings, but
  it is an important point to consider.]'
context_note: Windows Security Baseline is part of the intune domain. It connects
  closely to Defender For Endpoint Intune. Synthesised from 2 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
prerequisite_topics:
- intune/security/defender-for-endpoint-intune
related_topics:
- intune/security/defender-for-endpoint-intune
sources:
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2022-07-26'
  title: Intune Security Baselines Policies For Windows 10 Or Windows 11 Deployment
    Guide HTMD Blog
  url: https://www.anoopcnair.com/intune-security-baselines-policies-windows10-11
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2026-04-07'
  title: New Windows 11 25H2 Security Baseline Released In Microsoft Intune HTMD Blog
  url: https://www.anoopcnair.com/windows-11-25h2-security-baseline-in-intune
stale_after: '2026-06-17'
title: Windows Security Baseline in Intune
topic: intune/security/windows-security-baseline
---

# Windows Security Baseline in Intune

## Overview
The Windows Security Baseline in Intune is a set of pre-configured security settings for Windows 10 and Windows 11 devices managed through Microsoft Endpoint Manager (MEM). These baselines help secure and protect an organization's resources and data by enforcing granular security settings recommended by relevant security teams.

## Key Concepts
- Intune Security Baselines: Groups of pre-configured Windows settings that can be deployed to devices managed through the Intune MEM Portal. [CONFLICT: Anoop C Nair does not mention Policy and Profile Manager, but it is a built-in role required for managing baselines in Intune.]
- Baseline versions: Versions of security baselines provided by Microsoft Endpoint Manager, which may change based on the evolving needs of a typical organization. [CONFLICT: Anoop C Nair mentions that older profiles become read-only but can be updated to the latest version for editing, while existing entry does not mention this.]

## Configuration
1. Sign in to the Microsoft Endpoint Manager Admin Center (<https://endpoint.microsoft.com>).
2. Navigate to the **Endpoint Security** node and click on the **Security Baselines** node.
3. Select the **Security Baseline for Windows 10 and later** set, then click on **+ Create Profile** to create a new security baseline.
4. Enter the name, description, platform (Windows 10 and Later), and baseline version (e.g., November 2021).
5. Review the default values of the Windows 10 or Windows 11 security baseline categories.
6. Deploy the created security baseline to groups of users or devices in Intune. [CONFLICT: Anoop C Nair does not mention deploying the created security baseline, but it is an essential step.]

## Common Pitfalls
- Using outdated versions of security baselines: Ensure that all policies and profiles are updated to the latest version to maintain security.
- Incorrect configuration of settings: Review the default values provided by Microsoft and customize only the required settings and values for your organization's needs. [CONFLICT: Anoop C Nair does not mention incorrect configuration of settings, but it is an important point to consider.]

## New Windows 11 25H2 Security Baseline
Microsoft released the **Windows 11 25H2** security baseline in Intune, providing preconfigured, recommended security settings for Windows devices. Organizations can customize the baseline based on their needs. This release is part of Microsoft’s effort to keep enterprise environments secure from cybersecurity threats. [New information]

## Related Topics
- Security baseline
- Windows baseline
- CIS benchmark
- Intune baseline
- Hardening baseline
- New Windows 11 25H2 Security Baseline (added from new source)