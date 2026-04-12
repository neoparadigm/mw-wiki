---
conflicts:
- '[CONFLICT: Anoop C Nair mentions new event logs for enhanced NTLM auditing, but
  no specific guidance on how it relates to XSPM configuration]'
- '[CONFLICT: Anoop C Nair does not mention this point]'
- '[CONFLICT: Anoop C Nair does not mention KQL or PowerShell in relation to XSPM]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2024-02-20'
  title: Automatic attack disruption in Microsoft Defender XDR and containing users
    during Human-operated Attacks
  url: https://jeffreyappel.nl/automatic-attack-disruption-in-microsoft-365-xdr-and-containing-users-during-human-operated-attacks
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-01-04'
  title: How to use Microsoft Security Exposure Management (XSPM)
  url: https://jeffreyappel.nl/how-to-use-microsoft-security-exposure-management-xspm
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-03-09'
  title: Microsoft Introduces Enhanced NTLM Auditing To Improve Windows Authentication
    Security HTMD Blog
  url: https://www.anoopcnair.com/microsoft-introduces-enhanced-ntlm-auditing
stale_after: '2026-05-27'
title: KQL — Lateral Movement Detection
topic: sentinel/kql/lateral-movement-queries
---

# KQL — Lateral Movement Detection & Microsoft Security Exposure Management (XSPM)

## Overview
KQL (Kusto Query Language) is a powerful tool used for data exploration and analysis in Microsoft Defender XDR, focusing on lateral movement detection as well as providing insights into the full exposure of organizations with Microsoft Security Exposure Management (XSPM). This topic is significant as it allows security analysts to detect lateral movement, a common technique used by attackers during human-operated attacks to move within a network after initial access.

## Key Concepts
- Lateral Movement: The process of an attacker moving from the initial compromised system to other systems within the network.
- KQL: Kusto Query Language, a powerful tool for data exploration and analysis in Microsoft Defender XDR.
- Data Analysis: Analyzing logs and events to identify patterns and indicators of compromise (IOCs).
- Microsoft Security Exposure Management (XSPM): A new product/feature in the Defender XDR suite that provides a unified view of an organization's attack surfaces, reducing security risk exposures.

## Configuration
The article does not provide specific configuration guidance for lateral movement detection using KQL or Microsoft Security Exposure Management (XSPM). It is recommended to consult Microsoft documentation or seek professional assistance for proper setup and configuration. [CONFLICT: Anoop C Nair mentions new event logs for enhanced NTLM auditing, but no specific guidance on how it relates to XSPM configuration]

## Common Pitfalls
- Overlooking relevant data sources: Ensuring all necessary data sources are included in the analysis is crucial for effective lateral movement detection.
- Incorrect query syntax: Proper understanding of KQL syntax is essential to avoid errors and ensure accurate results.
- Lack of context: Analyzing events in isolation can lead to false positives or missed detections. It's important to consider the overall context of the network and attack scenario, as well as understanding the differences between Vulnerability Management/ Secure Score and XSPM. [CONFLICT: Anoop C Nair does not mention this point]

## KQL / PowerShell
The article does not provide specific KQL queries or PowerShell scripts for lateral movement detection. However, Microsoft provides a variety of pre-built queries and scripts in their documentation that can be used as a starting point. For Microsoft Security Exposure Management (XSPM), the blog post explains more about its use and differences with Vulnerability Management/ Secure Score. [CONFLICT: Anoop C Nair does not mention KQL or PowerShell in relation to XSPM]

## Related Topics
- [KQL](https://github.com/microsoft/O365-ATP-KQL)
- Lateral Movement
- SMB
- Pass-the-Hash
- DCSync
- Microsoft Security Exposure Management (XSPM)
- Enhanced NTLM Auditing [New]

## Blog Post
> [Security](https://jeffreyappel.nl/category/security/) > How to use Microsoft Security Exposure Management (XSPM)

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[January 4, 2025](https://jeffreyappel.nl/how-to-use-microsoft-security-exposure-management-xspm/)
0

11 min read

Microsoft Security Exposure Management is a new product/feature in the Defender XDR suite. This blog will explain more about it and the diffe

New source article: "Microsoft Introduces Enhanced NTLM Auditing To Improve Windows Authentication Security HTMD Blog"
Author: Anoop C Nair
New source content:
# Microsoft Introduces Enhanced NTLM Auditing To Improve Windows Authentication Security HTMD Blog

Microsoft Introduces Enhanced NTLM Auditing To Improve Windows Authentication Security HTMD Blog

## **Key Takeaways**

- Microsoft is working to **reduce** the use of the legacy **authentication** protocol NTLM.
- Enhanced **NTLM** auditing is now available in **Windows 11 version 24H2** and Windows Server 2025.
- New event logs help **administrators** identify where and why **NTLM authentication** is used.
- The long-term goal is to move organizations toward stronger **authentication** methods such as **Kerberos.**

In this post we are discussing Microsoft Introduces Enhanced NTLM Auditing to Improve Windows Authentication Security. Microsoft is taking new steps to improve **Windows authentication** security by introducing enhanced auditing features to track the use of the legacy authentication protocol NTLM. During a security session, Maryam **Gawita** explained the company’s strategy to reduce **[NTLM](http://Supporting Secure Login Practices Through NTLM Auditing using Intune Policy)** usage while encouraging organizations to adopt more **secure authentication** methods such as **Kerberos**.

**Table of Contents**

## Table of Contents

## **Microsoft Introduces Enhanced NTLM Auditing to Improve Windows Authentication Security**

NTLM has long been part of **Windows authentication**, but security experts consider it **outdated** and vulnerable to several attacks. Microsoft’s latest improvements aim to help **administrators** better understand where NTLM is still being used in their environments.

- **[New SCCM Hotfix KB15498768 NTLM Connection Fallback Update](https://www.anoopcnair.com/sccm-hotfix-kb15498768-ntlm-fallback-update/)**
- **[Windows 11 Security Feature Blocking NTLM over SMB for Advanced Threat Protection](https://www.anoopcnair.com/windows-11-security-blocking-ntlm-over-smb/)**
- **[Microsoft Announces Deprecation of NTLM Authentication Protocols](https://www.anoopcnair.com/deprecation-of-ntlm-authentication-protocols/)**

## **How NTLM Authentication Works**

NTLM **authentication** works using a simple challenge response process between a **client and a server.** When a client tries to access a resource, it sends a request to the server. The server then sends back a challenge asking the client to prove its **identity**. The client creates a response using a **password-based hash** generated with **MD4** and a calculation using **HMAC-MD5.** This response is sent back to the server, and if the information matches, the server allows the client to access the resource.

- However, this process has some security problems. NTLM does not **properly verify** the server’s **identity**, so an attacker could pretend to be a server and **capture authentication** data.
- It also uses older **encryption methods**, which makes it easier for attackers to perform relay or **pass-the-hash attacks.**

Microsoft Introduces Enhanced NTLM Auditing 

[The rest of the content remains the same as before]