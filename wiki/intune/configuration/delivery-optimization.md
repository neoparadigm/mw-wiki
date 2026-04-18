---
conflict_topics:
- intune/configuration/settings-catalog
- intune/compliance/custom-compliance
conflicts:
- '[CONFLICT: Oliver Kieselbach''s source does not provide information about the MCC
  acting as a transparent proxy to cache content or the complete list of content supported
  by DO.]'
- '[CONFLICT: Oliver Kieselbach says X, existing entry says Y]'
- '[CONFLICT: Jannik Reinhard''s article refers to DO as a cloud managed peer-to-peer
  technology, while the existing entry does not specify this.]'
- '[CONFLICT: Michael Niehaus'' article mentions a standalone version of MCC, but
  the existing entry does not mention this.]'
context_note: Delivery Optimization is part of the intune domain. Synthesised from
  6 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-02-23'
  title: Use Delivery Optimization with DHCP Option on Pre-Windows 10 version 1803
  url: https://oliverkieselbach.com/2018/02/24/use-delivery-optimization-with-dhcp-option-on-pre-windows-10-version-1803
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2018-02-23'
  title: Use Delivery Optimization with DHCP Option on Pre-Windows 10 version 1803
  url: https://oliverkieselbach.com/2018/02/24/use-delivery-optimization-with-dhcp-option-on-pre-windows-10-version-1803/
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2020-03-07'
  title: Delivery Optimization with Intune and Microsoft Connected Cache (MCC)
  url: https://oliverkieselbach.com/2020/03/07/delivery-optimization-with-intune-and-microsoft-connected-cache-mcc
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2020-03-07'
  title: Delivery Optimization with Intune and Microsoft Connected Cache (MCC)
  url: https://oliverkieselbach.com/2020/03/07/delivery-optimization-with-intune-and-microsoft-connected-cache-mcc/
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-10-09'
  title: Deep Dive into delivery optimization
  url: https://jannikreinhard.com/2022/10/09/deep-dive-into-delivery-optimization
- author: Michael Niehaus
  crawled: '2026-04-18'
  date: '2024-10-31'
  title: Finally, a standalone version of Connected Cache for Delivery Optimization
  url: https://oofhours.com/2024/10/30/finally-a-standalone-version-of-connected-cache-for-delivery-optimization
stale_after: '2026-07-17'
title: Delivery Optimization for Windows Updates
topic: intune/configuration/delivery-optimization
---

# Delivery Optimization for Windows Updates

## Overview
Delivery Optimization for Windows Updates is a feature in Windows 10 that allows devices to download updates more efficiently by using peer-to-peer networking and content delivery optimization techniques. This topic matters because it can significantly reduce bandwidth usage and improve update deployment times, especially in enterprise environments with multiple devices.

## Key Concepts
- Delivery Optimization: A feature in Windows 10 that allows devices to download updates more efficiently by using peer-to-peer networking and content delivery optimization techniques. [CONFLICT: Jannik Reinhard's article refers to DO as a cloud managed peer-to-peer technology, while the existing entry does not specify this.]
- DHCP Option ID 234: A Dynamic Host Configuration Protocol (DHCP) option used to deliver a Group ID for Delivery Optimization.
- Intune Management Extension: A PowerShell script that can be used to manage Windows 10 devices in an enterprise environment.
- Scheduled Task: A task that is scheduled to run at specific times or events, such as logon or unlock of the workstation.
- Microsoft Connected Cache (MCC): A distributed cache solution using peer to peer transfers for content downloads, formerly known as DOINC (Delivery Optimization In-Network Cache). [CONFLICT: Michael Niehaus' article mentions a standalone version of MCC, but the existing entry does not mention this.]
- Delivery Optimization Service: A web service that manages peers in Delivery Optimization.
- Microsoft Connected Cache (MCC) (Standalone): A standalone version of the distributed cache solution for content downloads, available without SCCM and running on Windows 11, Windows Server 2022, or Linux. [New]

## Configuration
For pre-Windows 10 version 1803:
1. Configure the DHCP server to provide Option ID 234 with the Group ID for Delivery Optimization.
2. Download and compile the C++ program `DhcpOption.exe` from [GitHub](https://github.com/okieselbach/Intune/tree/master/ManagementExtension-Samples/DOScript).
3. Use the Intune Management Extension to create a PowerShell script that queries the DHCP server for Option ID 234, writes the result (Group ID) to the registry, and schedules the script as a scheduled task to run at logon and on every unlock of the workstation.
4. Make sure the device queries the DHCP server from time to time to get the group ID belonging to the current DHCP scope the client is using.
5. Disable the scheduled task and remove the registry key as soon as Windows 10 version 1803, a build greater than 16299 is found.

For post-Windows 10 version 1803:
[The native implementation starting with 1803 bypasses the need for the scheduled task and registry key.]

## Prerequisites [New]
- Min Windows Os Version from 1511 (With each later version more features were added)
- Open port TCP 7680 on clients and local firewalls for requests from other peers
- Internet connection with access to the delivery optimisation service:

For communication between clients and the Delivery Optimization cloud service:

```
*.do.dsp.mp.microsoft.com
```

For Delivery Optimization metadata:

```
*.dl.delivery.mp.microsoft.com
*.emdl.ws.microsoft.com
```

For the payloads (optional):

```
*.download.windowsupdate.com
*.windowsupdate.com
```

For the standalone Microsoft Connected Cache:
- You must be licensed for Windows 10/11 E3/E5/F3/A3/A5 (or Microsoft 365 E3/E5/F3/A3/A5) in order to use it.
- You need an Azure subscription (and someone who has access to it) to register your MCC hosts.
- You can run it on Windows 11 or Windows Server 2022 (or higher), or on Linux. On Windows, it will use the Windows Subsystem for Linux (WSL), running inside an Ubuntu container. If you haven't used WSL yet, no big deal, because you don't have to interact with that container yourself. If using Windows on Hyper-V, you'll need to enable nested virtualization for WSL to work.
- Port 80 must not be in use on the machines this is installed on — so don't put it on an SCCM server or anything else running with a web server on port 80.