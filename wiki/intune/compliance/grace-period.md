---
conflicts: []
context_note: Grace Period is part of the intune domain. Synthesised from 1 community
  source.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2026-03-26'
  title: How To Set Alert For Windows 365 Cloud PCs In Grace Period Using Intune HTMD
    Blog
  url: https://www.anoopcnair.com/alert-for-windows-365-cloud-pcs-in-grace-intune
stale_after: '2026-06-17'
title: Compliance Grace Period and Actions for Noncompliance
topic: intune/compliance/grace-period
---

# Compliance Grace Period and Actions for Noncompliance

## Overview
This topic discusses how to set up alerts for Windows 365 Cloud PCs during their grace period using Microsoft Intune, which helps administrators proactively monitor Cloud PC health and status, and take timely action before automatic deprovisioning occurs due to license issues.

## Key Concepts
- Alerts for Cloud PCs in grace period
- Timely notifications for potential deprovisioning
- Customizable thresholds and conditions
- Improved visibility into provisioning, connectivity, and service-related failures

## Configuration
1. Log in to the Microsoft Intune Admin Center using your administrator credentials.
2. Navigate to > Tenant administration > Alerts > Create policy
3. Select Windows 10 and later as the platform
4. Choose Cloud PCs in grace period from the list of available alerts
5. Configure alert rules, including customizable thresholds and conditions
6. Save and assign the policy to relevant groups

## Common Pitfalls
- Failing to configure alerts for devices nearing deprovisioning can lead to unexpected Cloud PC deactivation
- Incorrectly setting thresholds or conditions may result in excessive notifications or missed warnings

## KQL / PowerShell
Not applicable as the article does not provide any queries or scripts.

## Related Topics
- Grace period
- Noncompliance action
- Retire noncompliant Cloud PCs
- Compliance notification
- Action noncompliance for Cloud PCs