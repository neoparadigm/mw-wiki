---
conflicts:
- '[CONFLICT: Daniel Chronlund mentions a separate RBAC structure for Azure Resource
  Manager when exporting logs]'
- '[CONFLICT: New source article suggests that daily tasks in SOC involve updating
  rules and workbooks, while existing entry does not mention this.]'
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
Sentinel Workspace Architecture refers to the design and organization of Azure Sentinel workspaces, which are essential components for security operations in Microsoft's cloud platform. Properly configuring workspaces ensures efficient threat detection and response.

[Azure AD Log Export Security Considerations](wiki:Azure_AD_Log_Export_Security_Considerations) (New source content added)

## Key Concepts
- **Workspace**: A logical container that holds data sources, rules, playbooks, and other artifacts required for Azure Sentinel to function effectively.
- **Data Connectors**: Integrations with various services and systems to collect security-related data into the workspace.
- **Log Analytics Workspace**: The underlying infrastructure that supports Azure Sentinel workspaces, providing storage, processing, and querying capabilities for log data.
- **Rules**: Logic used to detect potential threats based on predefined patterns or conditions within the collected data.
- **Playbooks**: Automated responses or actions triggered by specific rule events to streamline threat investigation and remediation processes.
- [CONFLICT: Daniel Chronlund mentions a separate RBAC structure for Azure Resource Manager when exporting logs] **Azure Role-Based Access Control (RBAC)**: Used to manage access to the workspace and its resources. [CONFLICT: New source article suggests that daily tasks in SOC involve updating rules and workbooks, while existing entry does not mention this.]

## Configuration
1. Create a new Log Analytics workspace in the Azure portal.
2. Configure data connectors for relevant services and systems to populate the workspace with security-related data.
3. Define rules within the workspace to detect potential threats based on the collected data. [New source article suggests updating rules daily.]
4. Create playbooks to automate responses to rule events, improving threat response times.
5. Assign appropriate roles and permissions using Azure Role-Based Access Control (RBAC) to manage access to the workspace and its resources. [CONFLICT: Daniel Chronlund mentions a separate RBAC structure for Azure Resource Manager when exporting logs]

## Common Pitfalls
- Inadequate planning and design can lead to inefficient data collection, poor threat detection, and slow response times.
- Overcomplicating rules and playbooks may result in false positives or missed threats due to overly restrictive conditions.
- Insufficient RBAC configuration can lead to unauthorized access to sensitive data or resources within the workspace.

## KQL / PowerShell
The article does not provide any specific queries or scripts for Sentinel Workspace Architecture. However, Azure Sentinel primarily uses Kusto Query Language (KQL) for querying log data and defining rules, while PowerShell can be used for automating various tasks within the workspace. [New source content added: Azure Log Analytics integration is preferred by Daniel Chronlund]

## Related Topics
- [Workspace](wiki:Azure_Sentinel/Workspace)
- [Log Analytics](wiki:Azure_Monitor/Log_Analytics)
- [Sentinel Design](wiki:Azure_Sentinel/Design)
- [Microsoft Sentinel SOC Activities](wiki:Microsoft_Sentinel_SOC_Activities) (New source content added)
- [Multi

The new source article, "Microsoft Sentinel SOC Activities," provides additional information about daily tasks in a SOC using Microsoft Sentinel. It suggests that daily tasks involve investigating and responding to incidents, hunting results, and anomalies, as well as updating rules and workbooks within the workspace. The article also emphasizes the importance of weekly tasks for maintaining the detect capabilities of Sentinel, such as ensuring connectors are working and agents are running, and keeping rules and workbooks up-to-date.