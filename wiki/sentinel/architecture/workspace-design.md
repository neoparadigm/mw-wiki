---
conflicts:
- '[CONFLICT: Daniel Chronlund suggests using Azure Log Analytics integration for
  easier access to Azure AD insight workbooks]'
- '[CONFLICT: Daniel Chronlund suggests using Azure AD log export for compliance reasons,
  SIEM integration, internal policies, monitoring and alerts, automation, etc.]'
- '[CONFLICT: Not present in existing entry]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-01-22'
  title: Monitor your Azure AD Break Glass Accounts with Azure Monitor
  url: https://danielchronlund.com/2020/01/22/monitor-your-azure-ad-break-glass-accounts-with-azure-monitor
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-04-27'
  title: Azure AD Log Export Security Considerations
  url: https://danielchronlund.com/2020/04/27/azure-ad-log-export-security-considerations
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-04-21'
  title: A Powerful Conditional Access Change Dashboard for Microsoft Sentinel
  url: https://danielchronlund.com/2022/04/21/a-powerfull-conditional-access-change-dashboard-for-microsoft-sentinel
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2022-09-21'
  title: Microsoft Sentinel SOC Activities
  url: https://danielchronlund.com/2022/09/21/microsoft-sentinel-soc-activities
stale_after: '2026-07-11'
title: Sentinel Workspace Architecture
topic: sentinel/architecture/workspace-design
---

# Sentinel Workspace Architecture

## Sentinel Workspace Architecture
Sentinel Workspace Architecture outlines the design and structure of Azure Sentinel, a cloud-native Security Information and Event Management (SIEM) solution for threat detection and response in Microsoft Azure. Understanding the architecture is crucial for effective implementation and management of security operations within an organization's Azure environment.

## Key Concepts
- **Azure Sentinel**: A cloud-native SIEM solution that provides threat detection and response capabilities in Azure.
- **Log Analytics Workspace**: The underlying component where data is collected, stored, and analyzed by Azure Sentinel. [CONFLICT: Daniel Chronlund suggests using Azure Log Analytics integration for easier access to Azure AD insight workbooks]
- **Connectors**: Data sources that collect logs and events from various services within an organization's Azure environment for analysis by Azure Sentinel. [CONFLICT: Daniel Chronlund suggests using Azure AD log export for compliance reasons, SIEM integration, internal policies, monitoring and alerts, automation, etc.]
- **Analytic rules**: Custom rules created to detect specific patterns or anomalies in the data collected by Azure Sentinel, triggering alerts when a threat is detected.
- **Incident response**: The process of investigating and responding to security incidents identified by Azure Sentinel, including containment, eradication, and recovery actions.
- **Conditional Access Change Dashboard**: A dashboard created by Daniel Chronlund for monitoring Conditional Access changes in Microsoft Sentinel, providing a visual representation of recent changes and detailed policy comparisons (new). [CONFLICT: Not present in existing entry]
- **Microsoft Sentinel SOC Activities**: Daily, weekly, and monthly tasks expected in a Security Operations Center (SOC) using Microsoft Sentinel for threat detection and response. [New information from Daniel Chronlund's article]

## Configuration
1. Create a Log Analytics Workspace in the Azure portal.
2. Configure connectors to collect data from various services within your Azure environment. [CONFLICT: Daniel Chronlund suggests using Azure AD log export for compliance reasons, SIEM integration, internal policies, monitoring and alerts, automation, etc.]
3. Define analytic rules based on your organization's specific security requirements.
4. Set up automation and playbooks for incident response actions.
5. Customize dashboards and views to monitor the security posture of your Azure environment, including the Conditional Access Change Dashboard (new).
6. Manage access to Azure AD logs as needed for compliance and security purposes (new information from Daniel Chronlund's article).
7. Implement Microsoft Sentinel SOC Activities for daily, weekly, and monthly tasks in your SOC (new information from Daniel Chronlund's article).

## Common Pitfalls
- Inadequate configuration of connectors, leading to incomplete or inconsistent data collection.
- Overly complex analytic rules that generate false positives or miss genuine threats due to overcomplication.
- Insufficient incident response processes, resulting in slow or ineffective threat containment and remediation.
- Neglecting weekly and monthly tasks for maintaining detect capabilities of Sentinel (new information from Daniel Chronlund's article).

## KQL / PowerShell
Azure Sentinel primarily uses Kusto Query Language (KQL) for querying data within Log Analytics Workspaces. PowerShell scripts may also be used for automating various tasks within the Azure Sentinel environment. [CONFLICT: Daniel Chronlund suggests using Azure Log Analytics integration for easier access to Azure AD insight workbooks]