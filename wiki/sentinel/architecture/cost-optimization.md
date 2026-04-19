---
conflict_topics:
- intune/security/windows-security-baseline
- sentinel/automation/playbooks-logic-apps
conflicts:
- '[CONFLICT: Thijs Lecomte does not mention this concept, but it is already present
  in the existing entry]'
- '[CONFLICT: Thijs Lecomte does not mention permissions, but they are already present
  in the existing entry]'
- '[CONFLICT: Thijs Lecomte does not provide configuration details, but they are already
  present in the existing entry]'
- '[CONFLICT: Thijs Lecomte does not mention this pitfall, but it is already present
  in the existing entry]'
context_note: Cost Optimization is part of the sentinel domain. Synthesised from 2
  community sources.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2026-01-06'
  title: 'Microsoft Sentinel Cost Management: How to get insights in data lake usage'
  url: https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage
- author: Thijs Lecomte
  crawled: '2026-04-18'
  date: '2025-05-22'
  title: 'Practical Sentinel: Reviewing and Optimizing costs'
  url: https://practical365.com/practical-sentinel-reviewing-and-optimizing-costs
stale_after: '2026-06-02'
title: Microsoft Sentinel Cost Optimization
topic: sentinel/architecture/cost-optimization
---

# Microsoft Sentinel Cost Optimization

## Microsoft Sentinel Cost Optimization

### Overview
Microsoft Sentinel Cost Management is a feature that provides in-depth cost visibility into the usage of Sentinel and Sentinel Data Lake. This topic matters as it helps organizations manage and monitor costs associated with their use of the data lake tier, which is essential with the release of Microsoft Sentinel Data Lake.

### Key Concepts
- Microsoft Sentinel Cost Management: A new cost management experience for managing and monitoring costs associated with data lake usage in Microsoft Sentinel. [CONFLICT: Thijs Lecomte does not mention this concept, but it is already present in the existing entry]
- Data Lake Tier: The tier in Microsoft Sentinel that stores large amounts of data for extended periods, which is the focus of the cost management feature.
- Usage View: A view within Microsoft Sentinel Cost Management that provides details about data lake usage. [CONFLICT: Thijs Lecomte does not mention this concept, but it is already present in the existing entry]
- Notification View: A view within Microsoft Sentinel Cost Management for configuring notification and service alerts related to ingested costs. [CONFLICT: Thijs Lecomte does not mention this concept, but it is already present in the existing entry]
- Permissions: The Security Administrator role and the Billing Administrator role in Entra are required to access Microsoft Sentinel cost management. [CONFLICT: Thijs Lecomte does not mention permissions, but they are already present in the existing entry]

### Configuration
To access Microsoft Sentinel Cost Management, navigate to **Microsoft Defender** -> **Cost management**. The feature is currently in preview and can be found under **Microsoft Sentinel**. [CONFLICT: Thijs Lecomte does not provide configuration details, but they are already present in the existing entry]

### Common Pitfalls
- Not understanding the difference between data lake tier costs and Log Analytics workspace costs.
- Failing to configure notifications and service alerts related to ingested costs, leading to unexpected expenses. [CONFLICT: Thijs Lecomte does not mention this pitfall, but it is already present in the existing entry]

### Practical Sentinel: Reviewing and Optimizing costs
Thijs Lecomte provides additional information on gaining insights into Microsoft Sentinel costs:
- The Azure Cost Analysis view is the only way to get correct details on your actual spend, as this is where the bill is based upon. Navigate to the **resource group** where Microsoft Sentinel is located and select **cost analysis**. Afterwards, select ‘**Cost by resource’** at the top of the page. Within this list, search for the resource type ‘**Log Analytics workspace’**. If this resource is expanded, the Microsoft Sentinel cost will be visible as seen in Figure 1.
- This method does not provide a means to identify which data connector is contributing the most to the overall cost. For this, we need to retrieve the information from Microsoft Sentinel itself. The best way to do this is using the *Sentinel workbooks*. [New Information]

### KQL / PowerShell
This article does not provide any relevant queries or scripts.

### Related Topics
- Sentinel cost
- Ingestion cost
- Log retention
- Basic logs
- Auxiliary logs
- Azure Cost Analysis
- Sentinel workbooks [New Information]