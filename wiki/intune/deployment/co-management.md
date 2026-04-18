---
conflict_topics:
- intune/deployment/windows-autopatch
- intune/deployment/autopilot-user-driven
conflicts:
- '[CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed
  from the Intune cloud console, while the existing entry states that devices can
  switch between being managed by ConfigMgr and Intune.]'
- '[CONFLICT: Anoop C Nair does not mention this term specifically, but the concept
  is implied in his discussion of moving to a fully cloud-native Intune setup.]'
- '[CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed
  from the Intune cloud console, while the existing entry states that this can be
  done using workload policies.]'
- '[CONFLICT: Jeffrey suggests that co-management allows for migration from SCCM to
  Intune, while the existing entry does not mention this explicitly.]'
context_note: Co Management is part of the intune domain. Synthesised from 6 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2025-08-20'
  title: 'One Toolkit, Three Outcomes: Meet the New Right Click Tools for SCCM/Intune
    Teams'
  url: https://jannikreinhard.com/2025/08/20/one-toolkit-three-outcomes-meet-the-new-right-click-tools-for-sccm-intune-teams
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-11-04'
  title: How To Move From Co-Management To Full Intune With Modern Identity Modern
    Policies And No On-Prem HTMD Blog
  url: https://www.anoopcnair.com/how-to-move-from-co-management-to-full-intune
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-11-14'
  title: What Is Intune And MOF Relationship? SCCM MOF File Tech Is Still Used In
    Modern Management? HTMD Blog
  url: https://www.anoopcnair.com/is-intune-and-mof-relationship-sccm-mof-file
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-10-30'
  title: Top 4 Pillars Of SCCM To Intune Migration Workloads Identity Applications
    Policies HTMD Blog
  url: https://www.anoopcnair.com/top-4-pillars-of-sccm-to-intune-migration
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-11-03'
  title: Top Scenarios And Core Tools For SCCM To Intune Migration HTMD Blog
  url: https://www.anoopcnair.com/top-scenarios-and-core-sccm-to-intune-migration
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-05-20'
  title: 'Windows 10 co-management: Flexibel naar de cloud'
  url: https://jeffreyappel.nl/windows-10-co-management-flexibel-naar-de-cloud
stale_after: '2026-07-17'
title: Co-management with ConfigMgr and Intune
topic: intune/deployment/co-management
---

# Co-management with ConfigMgr and Intune

## Overview
Co-management is a feature in Microsoft Endpoint Manager (MEM) that allows for the management of Windows 10 devices using both Configuration Manager (ConfigMgr) and Intune. This approach combines the strengths of ConfigMgr, such as its ability to handle large numbers of devices and its support for legacy applications, with the cloud-based capabilities of Intune, such as mobile device management and app deployment.

## Key Concepts
- Co-management: The process of managing Windows 10 devices using both Configuration Manager (ConfigMgr) and Intune. [CONFLICT: Jeffrey suggests that co-management allows for migration from SCCM to Intune, while the existing entry does not mention this explicitly.]
- Workload switching: The ability for a device to switch between being managed by ConfigMgr and Intune based on the specific workload. [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that devices can switch between being managed by ConfigMgr and Intune.]
- Cloud attach: A feature that allows ConfigMgr to leverage cloud services, such as Microsoft Intune, to manage devices. [CONFLICT: Anoop C Nair does not mention this term specifically, but the concept is implied in his discussion of moving to a fully cloud-native Intune setup.]

## What Is Intune and MOF Relationship? SCCM MOF File Tech Is Still Used In Modern Management? (New Information)
Intune also uses MOF files, but for a very different purpose. Intune sends a desired state to the device, and the WinDC agent reads that state using a **MOF-based** format. This helps Windows understand exactly how it should configure and maintain the device. [From Anoop C Nair's article]

## Introduction to SCCM to Intune Migration (New Information from Jeffrey)
Jeffrey discusses co-management as a solution for businesses making the transition towards the cloud, particularly in situations where system setups like SCCM are still necessary or where the business is not yet ready for a full cloud migration. He notes that with co-management, traditional capabilities applied via SCCM and Active Directory can still be used, while also taking advantage of modern features provided by Intune. [From Jeffrey's article]

## Configuration
1. Enroll devices in Intune: Devices must be enrolled in Intune before they can be managed using co-management.
2. Enable co-management for the ConfigMgr tenant: In the ConfigMgr console, navigate to Administration > Cloud Services > Co-Management and enable co-management for the tenant.
3. Configure workload switching: Determine which workloads will be managed by ConfigMgr and which will be managed by Intune. This can be done using workload policies in the MEM admin center. [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that this can be done using workload policies.]
4. Deploy the co-management client: The co-management client must be deployed to devices for them to start being managed using co-management.
5. Migrate Workloads, Identity, Applications, and Policies (New Information from Jeffrey) [Details on this process can be found in Jeffrey's article]

## Additional Information (from Jeffrey's Article)
Jeffrey's article emphasizes the flexibility of co-management as a solution for businesses transitioning to the cloud. He notes that with co-management, it is possible to migrate workloads from SCCM to Intune in a secure manner. [From Jeffrey's article]