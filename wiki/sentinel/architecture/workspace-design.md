---
conflicts:
- '[CONFLICT: Daniel Chronlund mentions a separate RBAC structure for Azure Resource
  Manager when exporting logs]'
- '[CONFLICT: New source article suggests that daily tasks in SOC involve updating
  rules and workbooks, while existing entry does not mention this.]'
- '[CONFLICT: New source article suggests using Power BI for advanced analytics, while
  existing entry does not mention this.]'
- '[CONFLICT: Jeffrey suggests that Microsoft Sentinel Cost Management is available
  for users with the Security Administrator role and the Billing Administrator role
  in Entra, while existing entry does not mention this.]'
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
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2023-05-21'
  title: Mastering Intune Reporting and Analytics
  url: https://jannikreinhard.com/2023/05/21/mastering-intune-reporting-and-analytics
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2026-01-06'
  title: 'Microsoft Sentinel Cost Management: How to get insights in data lake usage'
  url: https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage
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
- **Rules**: Logic used to detect potential threats based on predefined patterns or conditions within the collected data. [New source article suggests updating rules daily.]
- **Playbooks**: Automated responses or actions triggered by specific rule events to streamline threat investigation and remediation processes.
- **Azure Role-Based Access Control (RBAC)**: Used to manage access to the workspace and its resources. [CONFLICT: New source article suggests that daily tasks in SOC involve updating rules and workbooks, while existing entry does not mention this.]
- **Intune Reporting and Analytics**: A comprehensive guide on leveraging reporting and analytics capabilities offered by Microsoft Intune for managing devices and the environment. [New source content added from "Mastering Intune Reporting and Analytics" article]
- **Microsoft Sentinel Cost Management**: A new feature that provides cost visibility into the usage of Sentinel and Sentinel Data Lake, currently in preview under **Microsoft Sentinel** > **Cost management** in the Microsoft Defender portal. [New source content added from "Microsoft Sentinel Cost Management: How to get insights in data lake usage" article]

## Configuration
1. Create a new Log Analytics workspace in the Azure portal.
2. Configure data connectors for relevant services and systems to populate the workspace with security-related data.
3. Define rules within the workspace to detect potential threats based on the collected data. [New source article suggests updating rules daily.]
4. Create playbooks to automate responses to rule events, improving threat response times.
5. Assign appropriate roles and permissions using Azure Role-Based Access Control (RBAC) to manage access to the workspace and its resources. [CONFLICT: Daniel Chronlund mentions a separate RBAC structure for Azure Resource Manager when exporting logs]
6. Understand the importance of reporting and analytics, explore Intune reporting capabilities, leverage Intune data in Azure Monitor, use Power BI for advanced analytics, start with Endpoint Analytics, and learn about Graph API for powerful analytics. [New source content added from "Mastering Intune Reporting and Analytics" article]
6. (New) Configure Microsoft Sentinel Cost Management to gain visibility into pricing and the new key cost drivers that are now available in the data lake tier. Accessible via **Microsoft Defender** -> **Cost management**.

## Common Pitfalls
- Inadequate planning and design can lead to inefficient data collection, poor threat detection, and slow response times.
- Overcomplicating rules and playbooks may result in false positives or misconfigurations.
- [CONFLICT: Jeffrey suggests that Microsoft Sentinel Cost Management is available for users with the Security Administrator role and the Billing Administrator role in Entra, while existing entry does not mention this.]

New source article: "Microsoft Sentinel Cost Management: How to get insights in data lake usage"
Author: Jeffrey
New source content:
[...] (The rest of the article is already included in the Usage section)