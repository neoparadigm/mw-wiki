---
conflicts:
- '[CONFLICT: Jeffrey does not mention this point]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2023-07-30'
  title: Azure Monitor Agent to monitor Windows devices (1/2) &#8211; Setup
  url: https://jannikreinhard.com/2023/07/30/azure-monitor-agent-to-monitor-windows-devices-1-2-setup
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2026-01-06'
  title: 'Microsoft Sentinel Cost Management: How to get insights in data lake usage'
  url: https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage
stale_after: '2026-07-13'
title: Sentinel Workspace Architecture
topic: sentinel/architecture/workspace-design
---

# Sentinel Workspace Architecture

## Sentinel Workspace Architecture

This topic discusses the architecture of Azure Sentinel workspaces, a cloud-native security information and event management (SIEM) solution that helps organizations detect, investigate, and respond to cybersecurity threats. Understanding the workspace architecture is crucial for effective threat hunting and security operations.

## Key Concepts

- **Azure Sentinel Workspace**: A logical container in Azure Monitor where data from various sources is collected, processed, and stored for analysis.
- **Data Connectors**: Prebuilt integrations that allow data from various security solutions to be ingested into the workspace.
- **Log Analytics**: The underlying technology used by Azure Sentinel to collect, store, and process log data.
- **Kusto Query Language (KQL)**: A powerful query language used in Log Analytics for searching, filtering, and analyzing data.
- **Azure Monitor**: The Microsoft solution that provides unified monitoring services across various Azure resources.

## Configuration

1. Create an Azure Sentinel workspace within your existing Log Analytics workspace.
2. Configure data connectors to ingest data from various security solutions into the workspace.
3. Set up alert rules and hunting queries to proactively detect threats and investigate incidents.
4. Customize the workspace by creating custom dashboards, playbooks, and analytics rules.

## Common Pitfalls

- Misconfigured data connectors can lead to incomplete or incorrect data being ingested into the workspace. [CONFLICT: Jeffrey does not mention this point]
- Inefficient queries can result in slow performance and increased costs.
- Lack of proper RBAC roles and permissions can lead to unauthorized access to sensitive data.

## KQL / PowerShell

This article does not provide specific KQL or PowerShell examples, as it focuses on the setup and configuration of Azure Sentinel workspaces rather than querying or scripting.

However, a new source provides insights into Microsoft Sentinel Cost Management, which includes cost management for data lake usage:

## Microsoft Sentinel Cost Management: How to get insights in data lake usage

Microsoft announced the public preview of Microsoft Sentinel Cost Management at Microsoft Ignite 2025. The new feature brings more in-depth cost visibility into the usage of Sentinel and Sentinel Data Lake. With the release of Microsoft Sentinel data lake, it is essential to gain visibility into pricing and the new key cost drivers that are now available.

### Permissions

Good to know, Microsoft Sentinel cost management is available for users with the Security Administrator role and the Billing Administrator role in Entra. Good to know; this is the Billing Administrator role in Microsoft Entra and not the Azure subscription Billing Administrator role.

Task: Update the wiki entry by adding the new information about Microsoft Sentinel Cost Management, marking any conflicts between sources, and expanding the Common Pitfalls section if necessary.

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.

---

# Sentinel Workspace Architecture

## Sentinel Workspace Architecture

This topic discusses the architecture of Azure Sentinel workspaces, a cloud-native security information and event management (SIEM) solution that helps organizations detect, investigate, and respond to cybersecurity threats. Understanding the workspace architecture is crucial for effective threat hunting and security operations.

## Key Concepts

- **Azure Sentinel Workspace**: A logical container in Azure Monitor where data from various sources is collected, processed, and stored for analysis.
- **Data Connectors**: Prebuilt integrations that allow data from various security solutions to be ingested into the workspace.
- **Log Analytics**: The underlying technology used by Azure Sentinel to collect, store, and process log data.
- **Kusto Query Language (KQL)**: A powerful query language used in Log Analytics for searching, filtering, and analyzing data.
- **Azure Monitor**: The Microsoft solution that provides unified monitoring services across various Azure resources.

## Configuration

1. Create an Azure Sentinel workspace within your existing Log Analytics workspace.
2. Configure data connectors to ingest data from various security solutions into the workspace.
3. Set up alert rules and hunting queries to proactively detect threats and investigate incidents.
4. Customize the workspace by creating custom dashboards, playbooks, and analytics rules.

## Common Pitfalls

- Misconfigured data connectors can lead to incomplete or incorrect data being ingested into the workspace. [CONFLICT: Jeffrey does not mention this point]
  - It is essential to ensure that data connectors are correctly configured to avoid missing important data and potential misinterpretations of the collected data.
- Inefficient queries can result in slow performance and increased costs.
- Lack of proper RBAC roles and permissions can lead to unauthorized access to sensitive data.
  - Implementing appropriate Role-Based Access Control (RBAC) is crucial for maintaining security and privacy within the workspace by granting users the necessary permissions while limiting their access to sensitive data.

## KQL / PowerShell

This article does not provide specific KQL or PowerShell examples, as it focuses on the setup and configuration of Azure Sentinel workspaces rather than querying or scripting.

However, a new source provides insights into Microsoft Sentinel Cost Management, which includes cost management for data lake usage:

## Microsoft Sentinel Cost Management: How to get insights in data lake usage

Microsoft announced the public preview of Microsoft Sentinel Cost Management at Microsoft Ignite 2025. The new feature brings more in-depth cost visibility into the usage of Sentinel and Sentinel Data Lake. With the release of Microsoft Sentinel data lake, it is essential to gain visibility into pricing and the new key cost drivers that are now available.

### Permissions

Good to know, Microsoft Sentinel cost management is available for users with the Security Administrator role and the Billing Administrator role in Entra. Good to know; this is the Billing Administrator role in Microsoft Entra and not the Azure subscription Billing Administrator role.

Task: Update the wiki entry by adding the new information about Microsoft Sentinel Cost Management, marking any conflicts between sources, and expanding the Common Pitfalls section if necessary.

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.