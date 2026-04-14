---
conflicts:
- '[CONFLICT: Ugur Koc mentions the initial learning curve of KQL being difficult,
  while the existing entry does not explicitly state this]'
- '[CONFLICT: Daniel Chronlund emphasizes the importance of threat hunting in Microsoft
  Sentinel, while the existing entry does not explicitly discuss it]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Ugur Koc
  crawled: '2026-04-14'
  date: '2025-07-14'
  title: Ugur Koc - Microsoft MVP for Intune and Security Copilot
  url: https://ugurkoc.de/2021/11
- author: Ugur Koc
  crawled: '2026-04-14'
  date: '2025-07-14'
  title: Ugur Koc - Microsoft MVP for Intune and Security Copilot
  url: https://ugurkoc.de/2022/01
- author: Ugur Koc
  crawled: '2026-04-14'
  date: '2025-07-14'
  title: Ugur Koc - Microsoft MVP for Intune and Security Copilot
  url: https://ugurkoc.de/2022/06
- author: Ugur Koc
  crawled: '2026-04-14'
  date: '2025-07-14'
  title: Ugur Koc - Microsoft MVP for Intune and Security Copilot
  url: https://ugurkoc.de/2022/07
- author: Ugur Koc
  crawled: '2026-04-14'
  date: '2025-07-14'
  title: Ugur Koc - Microsoft MVP for Intune and Security Copilot
  url: https://ugurkoc.de/2022/08
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2022-10-03'
  title: Sentinel Hunting Query Pack &#8211; DCSecurityOperations
  url: https://danielchronlund.com/2022/10/03/sentinel-hunting-query-pack-dcsecurityoperations
stale_after: '2026-05-29'
title: KQL — Identity and Sign-in Detection
topic: sentinel/kql/identity-detection-queries
---

# KQL — Identity and Sign-in Detection

## KQL — Identity and Sign-in Detection

### Overview
KQL (Kusto Query Language) is a powerful tool used for querying data in Microsoft's Log Analytics service, which includes diagnostic logs from Intune. This topic matters as it enables IT administrators to gain insights into identity and sign-in activities within their organization.

### Key Concepts
- KQL syntax and functions
- SignInLogs table for storing sign-in data
- Identity detection through user and device properties
- Risky sign-ins and legacy authentication
- Ugur Koc's insights on learning KQL (New source content)
- [Ugur Koc - Microsoft MVP for Intune and Security Copilot](# Ugur Koc - Microsoft MVP for Intune and Security Copilot) (New source content)
- Daniel Chronlund's insights on threat hunting in Microsoft Sentinel (New source content)
- [Sentinel Hunting Query Pack — DCSecurityOperations](https://github.com/DanielChronlund/DCSecurityOperations) (New source content)

### Configuration
To configure KQL for identity and sign-in detection, follow these steps:

1. Connect to your Log Analytics workspace in Azure.
2. Query the SignInLogs table using KQL syntax to filter for specific users, devices, or sign-in events.
3. Configure alerts based on risky sign-ins or other criteria to receive notifications of potential security issues.
4. [Ugur Koc's approach to writing KQL queries](https://ugurkoc.de/kql-queries-made-easy-my-intune-admin-journey-with-copilot/) (New source content)
5. [Daniel Chronlund's guide on deploying Sentinel hunting queries from DCSecurityOperations](https://danielchronlund.com/sentinel-hunting-query-pack-dcssecurityoperations/) (New source content)
6. [Ugur Koc mentions the initial learning curve of KQL being difficult, while the existing entry does not explicitly state this]
7. [CONFLICT: Daniel Chronlund emphasizes the importance of threat hunting in Microsoft Sentinel, while the existing entry does not explicitly discuss it]

### Common Pitfalls
- Misunderstanding KQL syntax and functions can lead to incorrect queries and inaccurate results.
- Failing to properly filter queries can result in large amounts of irrelevant data, making it difficult to identify important information.
- [CONFLICT: Ugur Koc mentions the initial learning curve of KQL being difficult, while the existing entry does not explicitly state this]
- [CONFLICT: Daniel Chronlund emphasizes the importance of threat hunting in Microsoft Sentinel, while the existing entry does not explicitly discuss it]

### KQL / PowerShell
Here's an example KQL query for detecting risky sign-ins:
```kql
SignInLogs
| where AuthenticationMethod == "Interactive"
| where RiskLevel > 3
| summarize Count = count() by ClientIP, UserName, AuthenticationSuccess
```
### Related Topics
- [KQL](wiki:KQL)
- [SigninLogs](wiki:SigninLogs)
- [identity detection](wiki:Identity_Detection)
- [risky sign-in](wiki:Risky_Sign-In)
- [legacy auth KQL](wiki:Legacy_Auth_KQL)
- [Ugur Koc's insights on learning KQL](https://ugurkoc.de/kql-queries-made-easy-my-intune-admin-journey-with-copilot/) (New source content)
- # Ugur Koc - Microsoft MVP for Intune and Security Copilot (New source content)
- [Sentinel Hunting Query Pack — DCSecurityOperations](https://github.com/DanielChronlund/DCSecurityOperations) (New source content)