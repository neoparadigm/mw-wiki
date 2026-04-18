---
conflicts: []
context_note: Cost Optimization is part of the sentinel domain. Synthesised from 1
  community source.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2026-01-06'
  title: 'Microsoft Sentinel Cost Management: How to get insights in data lake usage'
  url: https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage
stale_after: '2026-06-02'
title: Microsoft Sentinel Cost Optimization
topic: sentinel/architecture/cost-optimization
---

# Microsoft Sentinel Cost Optimization

## Microsoft Sentinel Cost Optimization

### Overview
Microsoft Sentinel Cost Management is a feature that provides in-depth cost visibility into the usage of Sentinel and Sentinel Data Lake. This topic matters as it helps organizations manage and monitor costs associated with their use of the data lake tier, which is essential with the release of Microsoft Sentinel Data Lake.

### Key Concepts
- Microsoft Sentinel Cost Management: A new cost management experience for managing and monitoring costs associated with data lake usage in Microsoft Sentinel.
- Data Lake Tier: The tier in Microsoft Sentinel that stores large amounts of data for extended periods, which is the focus of the cost management feature.
- Usage View: A view within Microsoft Sentinel Cost Management that provides details about data lake usage.
- Notification View: A view within Microsoft Sentinel Cost Management for configuring notification and service alerts related to ingested costs.
- Permissions: The Security Administrator role and the Billing Administrator role in Entra are required to access Microsoft Sentinel cost management.

### Configuration
To access Microsoft Sentinel Cost Management, navigate to **Microsoft Defender** -> **Cost management**. The feature is currently in preview and can be found under **Microsoft Sentinel**.

### Common Pitfalls
- Not understanding the difference between data lake tier costs and Log Analytics workspace costs.
- Failing to configure notifications and service alerts related to ingested costs, leading to unexpected expenses.

### KQL / PowerShell
This article does not provide any relevant queries or scripts.

### Related Topics
- Sentinel cost
- Ingestion cost
- Log retention
- Basic logs
- Auxiliary logs