---
conflicts:
- '[CONFLICT: Jeffrey says this is a method, existing entry does not mention it]'
- '[CONFLICT: New source mentions this, existing entry does not]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-03-11'
  title: 6 Core Security Pillars Of Windows 11 Chip-to-Cloud Protection HTMD Blog
  url: https://www.anoopcnair.com/6-core-security-pillars-of-windows-11
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2023-04-05'
  title: Block &quot;vulnerable/unwanted&quot; applications with Defender for Endpoint
    and Vulnerability Management
  url: https://jeffreyappel.nl/block-vulnerable-unwanted-applications-with-defender-for-endpoint-and-vulnerability-management
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Cafe - June 2024
  url: https://kqlcafe.com/shownotes/2024/KQL%20Cafe%20-%20June%202024
stale_after: '2026-06-11'
title: WDAC and App Control for Business
topic: intune/security/wdac-app-control
---

# WDAC and App Control for Business

## WDAC and App Control for Business

### Overview
WDAC (Windows Defender Application Control) and App Control for Business are security features in Windows 11 designed to enhance application control, improve code integrity, and reduce the attack surface by allowing only trusted applications to run on a device. These features matter because they help protect against malware, unauthorized access, and other cyber threats.

### Key Concepts
- WDAC: A security feature that allows administrators to create application permission policies, specifying which applications are allowed to run on devices.
- App Control for Business: An extension of WDAC that provides additional features for enterprise environments, such as the ability to allow list specific applications and enforce code integrity rules.
- Code Integrity: The process of ensuring that only trusted code is executed on a device, reducing the risk of malware infections and unauthorized access.
- Allow List: A list of approved applications that are allowed to run on a device, helping to reduce the attack surface and improve security.

### Configuration
1. Enable WDAC:
   - Open Group Policy Editor (gpedit.msc)
   - Navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Defender Application Control > Turn on Code Integrity Policies
   - Set the policy to Enabled and configure settings as needed

2. Create an application permission policy:
   - Open MDM (Mobile Device Management) or Group Policy Editor
   - Create a new rule allowing specific applications or groups of applications to run
   - Assign the policy to devices as needed

### Common Pitfalls
- Failing to properly configure WDAC policies can result in legitimate applications being blocked, causing disruptions to workflows.
- Incorrectly configuring allow lists can lead to unintended security risks if untrusted applications are accidentally included.

### Microsoft Defender for Endpoint and Vulnerability Management [CONFLICT: Jeffrey says this is a method, existing entry does not mention it]
Microsoft Defender for Endpoint (P2) contains the vulnerability management solution for getting visibility based on the installed MDE sensor. When using Defender for Endpoint, there are multiple ways to block vulnerable and unwanted applications. Ideally, there is a dynamic source where all application/ CVEs and vulnerability information is located. In terms of Defender for Endpoint, this part of the product is included in Defender for Endpoint P2. An add-on is available with more features – including a feature for blocking applications based on the vulnerable version.

### Related Topics
- [WDAC](/wiki/WDAC)
- [App Control](/wiki/App_Control)
- [Application control](/wiki/Application_control)
- [Code integrity](/wiki/Code_integrity)
- [Allow list](/wiki/Allow_list)
- [Defender for Endpoint and Vulnerability Management](/wiki/Defender_for_Endpoin)

New source article: "KQL Cafe - June 2024"
Author: Bert-Jan Pals
New source content:

### Microsoft Defender for Endpoint Advanced Hunting and Application Control for Business – WDACConfig [CONFLICT: New source mentions this, existing entry does not]
A presentation from KQL Cafe discusses Microsoft Defender for Endpoint (MDE) and its advanced hunting capabilities, including the use of Application Control for Business (WDAC) configurations. The presentation covers various use cases such as monitoring suspicious processes running on hidden desktops, auditing Defender XDR activities, and detecting changes to evade detection. It also provides examples of KQL queries that can be used for these purposes.

### Our Guest Michalis Michalos [CONFLICT: New source mentions this, existing entry does not]
The June 2024 edition of KQL Cafe featured a guest presentation by Michalis Michalos, who spoke about Defender for Endpoint and WSL (Windows Subsystem for Linux). The presentation covered various topics related to using MDE for security monitoring and threat hunting in Windows environments.