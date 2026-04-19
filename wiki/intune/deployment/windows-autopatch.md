---
conflict_topics:
- intune/deployment/co-management
- intune/reporting/intune-reporting-log-analytics
conflicts:
- '[CONFLICT: Simon Skotheimsvik says this is a common silent setting blocking communication
  with Windows update services, existing entry does not mention this]'
- '[CONFLICT: Simon Skotheimsvik mentions a specific issue called "Silent Windows
  Autopatch Killer" that may cause this]'
- '[CONFLICT: The existing entry mentions "Expedite polices" but does not provide
  further details. The new source explains that it refers to a feature allowing administrators
  to prioritize the installation of specific quality updates on devices.]'
context_note: Windows Autopatch is part of the intune domain. Synthesised from 5 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2024-10-02'
  title: Simon does How To Use Autopatch Groups For A Smooth Windows 11 Upgrade
  url: https://skotheimsvik.no/how-to-use-autopatch-groups-for-a-smooth-windows-11-upgrade
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-12-15'
  title: 'New Intune/Autopatch Feature: CVE and KB reporting – Better visibility,
    smarter patching – General Availability – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/new-intune-autopatch-feature-cve-and-kb-reporting-better-visibility-smarter-patching-general-availability
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2025-08-14'
  title: Simon does The Silent Windows Autopatch Killer
  url: https://skotheimsvik.no/the-silent-windows-autopatch-killer
- author: paolomatarazzo
  crawled: '2026-04-18'
  date: '2026-04-01'
  title: Windows Update Management Overview - Microsoft Intune
  url: https://learn.microsoft.com/en-us/mem/device-updates/windows
- author: tiaraquan
  crawled: '2026-04-18'
  date: '2025-03-31'
  title: What is Windows Autopatch?
  url: https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-overview
stale_after: '2026-06-02'
title: Windows Autopatch Configuration
topic: intune/deployment/windows-autopatch
---

# Windows Autopatch Configuration

## Windows Autopatch Configuration

Windows Autopatch is a Microsoft service that automates the process of updating and patching Windows devices to ensure they are always running the latest secure versions. This topic matters because it simplifies the upgrade process from Windows 10 to Windows 11, making it more efficient and less prone to errors.

## Key Concepts
- Tenant Enrollment
- Windows Autopatch Device Configurations
- Autopatch Release Management
- Autopatch Device Onboarding
- Autopatch Reporting
- AutoPatch Troubleshooting
- [CVE/KB Reporting](#new-intuneautopatch-feature-cve-and-kb-reporting-better-visibility-smarter-patching-general-availability) (New from the new source)
- [Silent Windows Autopatch Killer](#simon-does-the-silent-windows-autopatch-killer) (New from the new source)
- Windows Update Management Overview - Microsoft Intune (New from the new source)
- **[What is Windows Autopatch?](#what-is-windows-autopatch)** (New from the new source)

## Configuration
The article provides a detailed guide on how to set up and configure Windows Autopatch for a smooth Windows 11 upgrade. This includes steps for tenant enrollment, creating device configurations, managing autopatch release schedules, onboarding devices, troubleshooting issues, CVE/KB Reporting, addressing the Silent Windows Autopatch Killer ([CONFLICT: Simon Skotheimsvik mentions a specific issue called "Silent Windows Autopatch Killer" that may cause this]), and introducing the concept of Windows Update Management Overview provided by Microsoft Intune.

The new source also introduces the goal of Windows Autopatch, which is to minimize the involvement of IT resources in the planning and deployment of updates for Windows, Microsoft 365 Apps, Microsoft Edge, or Teams. It explains how Windows Autopatch uses careful rollout sequences and communicates with IT Admins throughout the release so that they can focus on other activities and tasks.

## Common Pitfalls
- Conflicting existing policies with new autopatch configurations
- Incorrectly assigning devices to autopatch groups
- Insufficient understanding of the various new Entra ID security groups
- Registry settings blocking Windows Auto Update ([CONFLICT: Simon Skotheimsvik mentions a specific issue called "Silent Windows Autopatch Killer" that may cause this])
- Overlooking CVE/KB Reporting (New from the new source)
- Misconfigurations related to Windows Update Management Overview provided by Microsoft Intune (New from the new source)

## KQL / PowerShell
The article includes a PowerShell script that can be used in an Azure runbook for automating device assignment to the correct Autopatch group. The new source also mentions the use of Windows Update Management policies through the Settings Catalog and update rings.

## Related Topics
- autopatch
- windows autopatch
- update rings
- quality update
- feature update
- [CVE/KB Reporting](#new-intuneautopatch-feature-cve-and-kb-reporting-better-visibility-smarter-patching-general-availability) (New from the new source)
- [Silent Windows Autopatch Killer](#simon-does-the-silent-windows-autopatch-killer) (New from the new source)
- Windows Update Management Overview - Microsoft Intune (New from the new source)
- **[What is Windows Autopatch?](#what-is-windows-autopatch)** (New from the new source)

## New

New source article: "What is Windows Autopatch?"
Author: tiaraquan
New source content:

### What is Windows Autopatch?

Feedback

Summarize this article for me

Important

In April 2025, Windows Autopatch removed feature activation and made Windows Autopatch features available to Business Premium and A3+ licenses. These changes are rolling out over the next several weeks. If your experience looks different from the documentation, you didn’t receive the changes yet. Review [Prerequisites](../prepare/windows-autopatch-prerequisites) and [Features and capabilities](#features-and-capabilities) to understand licensing and feature entitlement.

Windows Autopatch is a cloud service that automates Windows, Microsoft 365 Apps for enterprise, Microsoft Edge, and Microsoft Teams updates to improve security and productivity across your organization.

## Unique to Windows Autopatch

Rather than maintaining complex digital infrastructure, businesses want to focus on what makes them unique and successful. Windows Autopatch offers a solution to some of the challenges facing businesses and their people today:

- **Close the security gap**: Windows Autopatch keeps Microsoft Windows current, there are fewer vulnerabilities and threats to your devices.
- **Close the productivity gap**: Windows Autopatch adopts features as they're made available. End users get the latest tools to amplify their collaboration and work.
- **Optimize your IT admin resources**: Windows Autopatch automates routine endpoint updates. IT pros have more time to create value.
- **On-premises infrastructure**: Transitioning to the world of software as a service (SaaS) allows you to minimize your investment in on-premises hardware since updates are delivered from the cloud.
- **Onboard new services**: Windows Autopatch makes it easy to enroll and minimizes the time required from your IT Admins to get started.
- **Minimize end user disruption**: Windows Autopatch releases updates in sequential deployment rings, and responding to reliability and compatibility signals, user disruptions due to updates are minimized.

Windows Autopatch helps you minimize the involvement of your scarce IT resources in the planning and deployment of updates for Windows, Microsoft 365 Apps, Microsoft Edge, or Teams. Windows Autopatch uses careful rollout sequences and communicates with you throughout the release so that IT Admins can focus on other activities and tasks.

## Features and capabilities

The goal of Windows Autopatch

[Exit editor mode]