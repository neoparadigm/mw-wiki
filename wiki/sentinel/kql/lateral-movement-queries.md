---
conflicts:
- '[CONFLICT: Jeffrey''s source provides additional information about Automatic Attack
  Disruption in Microsoft Defender XDR and User Containment during Human-operated
  attacks, which is not present in the existing entry.]'
- '[CONFLICT: Michael Morten Sonne suggests switching from SMB to NFS for Veeam Backup
  issues with Synology SMB Share, existing entry does not mention this]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-01-23'
  title: How to disable SMBv1 with Intune [deep dive analysis]
  url: https://oliverkieselbach.com/2018/01/23/how-to-disable-smbv1-with-intune-deep-dive-analysis/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-01-23'
  title: How to disable SMBv1 with Intune [deep dive analysis]
  url: https://oliverkieselbach.com/2018/01/23/how-to-disable-smbv1-with-intune-deep-dive-analysis
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2024-02-20'
  title: Automatic attack disruption in Microsoft Defender XDR and containing users
    during Human-operated Attacks
  url: https://jeffreyappel.nl/automatic-attack-disruption-in-microsoft-365-xdr-and-containing-users-during-human-operated-attacks
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-12-28'
  title: 'KB: Veeam Backup Fails to Synology SMB Share – “An unexpected network error
    occurred – Asynchronous request operation has failed” – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/kb-veeam-backup-fails-to-synology-smb-share-an-unexpected-network-error-occurred-asynchronous-request-operation-has-failed
stale_after: '2026-05-29'
title: KQL — Lateral Movement Detection
topic: sentinel/kql/lateral-movement-queries
---

# KQL — Lateral Movement Detection and Automatic attack disruption in Microsoft Defender XDR, and Veeam Backup Fails to Synology SMB Share

## Overview
This entry provides a deep dive analysis on how to disable SMBv1 with Intune, a crucial step in modern workplace security as SMBv1 is vulnerable to various attacks and should be disabled where possible. The article also demonstrates how to find new available settings, configure them without technical documentation, and understand their inner workings. It focuses on the SMBv1 settings in the latest Windows 10 Insider build (17074) derived from MSSecurityGuide.

The entry has been updated with additional information from two sources: "Automatic attack disruption in Microsoft Defender XDR and containing users during Human-operated Attacks" by Jeffrey, and "KB: Veeam Backup Fails to Synology SMB Share – “An unexpected network error occurred – Asynchronous request operation has failed” – Blog - Sonne´s Cloud" by Michael Morten Sonne.

## Key Concepts
- MDM settings in Windows 10 Insider Build (17074)
- ADMX-backed policy configuration in Windows 10 via Intune OMA-URIs
- SMB 1.0/CIFS File Sharing Support and the related settings: ConfigureSMBV1ClientDriver and ConfigureSMBV1Server
- Registry keys for MDM Policy CSP settings and ADMX-backed policies
- Automatic Attack Disruption in Microsoft Defender XDR and User Containment during Human-operated attacks
- Veeam Backup issues with Synology SMB Share

## Configuration
The article demonstrates how to get the right pieces of information to configure an ADMX-backed policy setting in Windows 10 via Intune OMA-URIs with no technical documentation for it. The goal is to show some of the inner workings how parts of the MDM policies are implemented and how we can get a deeper understanding of them.

The two settings controlled by the article are:
- **ConfigureSMBV1ClientDriver**
- **ConfigureSMBV1Server**

These settings control the SMB 1.0/CIFS File Sharing Support.

### **How do we get to know this new available settings?**
First, we have a look at the registry. There is a new place where you can find MDM Policy CSP settings. Group Policy settings are stored in the Policies registry key and MDM Policy CSP settings can be found in the **PolicyManager** key here:

```
HKLM\SOFTWARE\Mircosoft\PolicyManager
```

Within the **current** key we find all settings configured for this device by MDM like Intune. Within the **default** key we find all available settings for the particular Windows 10 release.

As mentioned, the latest Windows 10 version (at time of writing build version 17074) has a sub key for **MSSecurityGuide** with additional sub keys for **ConfigureSMBV1ClientDriver** and **ConfigureSMBV1Server**.

If we have a look at the details, for example of **ConfigureSMBV1ClientDriver** we see the value name **admxMetadataDevice**. This gives us a hint that this particular policy is an ADMX-backed policy.

### **How do we configure it if we don’t know the input values for it?**
The way Microsoft implemented the feature ADMX-backed policies, you can find the corresponding ADMX file in the following location:

```
C:\Windows\PolicyDefinitions
```

Open the ADMX file with a tool like PowerShell or a third-party tool to view the possible values.

[CONFLICT: Michael Morten Sonne suggests switching from SMB to NFS for Veeam Backup issues with Synology SMB Share, existing entry does not mention this]

## New Source Article: "KB: Veeam Backup Fails to Synology SMB Share – “An unexpected network error occurred – Asynchronous request operation has failed” – Blog - Sonne´s Cloud"

- [KB](https://blog.sonnes.cloud/topics/general/kb/)
- [Veeam](https://blog.sonnes.cloud/topics/general/software/veeam/)

# KB: Veeam Backup Fails to Synology SMB Share – “An unexpected network error occurred – Asynchronous request operation has failed”

[byMichael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

December 28, 2025

5 minute read





Last Updated on December 28, 2025 by [Michael Morten Sonne](https://sonnes.cloud)

##### Table of Contents

1. [Introduction](#introduction)
2. [My setup](#my-setup)
3. [The symptoms](#the-symptoms)
   1. [Random and inconsistent backup failures](#random-and-inconsistent-backup-failures)
   2. [Why this was tricky](#why-this-was-tricky)
   3. [Digging deeper](#digging-deeper)
4. [The fix: Switching from SMB to NFS](#the-fix-switching-from-smb-to-nfs)
   1. [Why NFS helps](#why-nfs-helps)
5. [Takeaways](#takeaways)
6. [Conclusion](#conclusion)
7. [References](#references)

# Introduction

Recently, I ran into a frustrating Veeam Backup issue in my home lab/home setup that took far longer to troubleshoot than I’d like to admit. What made it especially annoying was the fact that this setup had been **rock solid since February 2023**, and only started failing towards the **end of November 2025** – with no obvious configuration changes on my side.

Of course, who knows what may have changed *under the hood* over time 😆

And yes – this wasn’t business-critical. Luckily, I had time to dig into it properly during my Christmas vacation 👌🎄

# My setup

- **History:** Stable for almost 3 years
- **Backup software:** Veeam Backup & Replication
- **Target:** Synology NAS
- **Protocol:** SMB / CIFS
- **Network:** UniFi (switches + gateway)
  - Previously: pfSense + UniFi switches
- **Workload:** VM backups (VHDX)
- **Hypervisor:** Hyper-V

# The symptoms

Backups would start normally and run for several minutes with good throughput. Then – **completely at random** – the job would fail with network-related errors. Performance graphs looked fine right up until the failure.

A typical Veeam error looked like this:


**The error in full format:**

*26-12-2025 11:46:18 :: Error: An unexpected network error occurred.
Asynchronous request operation has failed. [requestsize = 1052672] [offset = 70989729792]
An unexpected network error occurred.
Asynchronous request operation has failed. [requestsize = 118784] [offset = 70990970880]
An unexpected network error occurred.
Asynchronous request operation has failed. [requestsize = 16384] [offset = 70991183872]
An unexpected network error occurred.
Asynchronous request operation has failed. [requestsize = 204

[CONFLICT: Michael Morten Sonne suggests switching from SMB to NFS for Veeam Backup issues with Synology SMB Share, existing entry does not mention this]