---
conflict_topics:
- azure/app-proxy/app-proxy-configuration
- azure/network/global-secure-access
conflicts:
- '[CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure
  Monitor Agent setup]'
- '[CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure
  Monitor Agent setup, but Bert-Jan Pals mentions no specific pitfalls in his article]'
context_note: Azure Monitor Log Analytics is part of the azure domain. Synthesised
  from 5 community sources.
domain: azure
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2022-07-19'
  title: Monitoring Intune policy configuration changes
  url: https://oliverkieselbach.com/2022/07/19/monitoring-intune-policy-configuration-changes
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2023-07-30'
  title: Azure Monitor Agent to monitor Windows devices (1/2) &#8211; Setup
  url: https://jannikreinhard.com/2023/07/30/azure-monitor-agent-to-monitor-windows-devices-1-2-setup
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe 28. November 2023
  url: https://kqlcafe.com/shownotes/2023/KQL%20Cafe%20-%20November%202023
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-08-04'
  title: How to store Defender XDR data for years in Sentinel data lake without expensive
    ingestion cost
  url: https://jeffreyappel.nl/how-to-store-defender-xdr-data-for-years-in-sentinel-data-lake-without-expensive-ingestion-cost
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-09-21'
  title: Stream Azure AD Identity Protection events to Microsoft Sentinel/ Log Analytics
  url: https://jeffreyappel.nl/stream-azure-ad-identity-protection-events-to-azure-sentinel-log-analytics
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2023-01-26'
  title: Deploy Sysmon and collect additional data with Sentinel and the AMA agent
  url: https://jeffreyappel.nl/deploy-sysmon-and-collect-data-with-sentinel-and-the-ama-agent
stale_after: '2026-06-17'
title: Azure Monitor and Log Analytics Workspaces
topic: azure/monitoring/azure-monitor-log-analytics
---

# Azure Monitor and Log Analytics Workspaces

## Overview
This topic discusses monitoring changes to Intune policy configurations using Azure Monitor and Log Analytics Workspaces, as well as setting up alerts for specific policy sets such as those for Privileged Access Workstations (PAW), to ensure intended changes and prevent unintended modifications. Additionally, it covers the setup of Azure Monitor Agent to monitor Windows devices.

The KQL Cafe 28. November 2023 provides additional resources and tools for learning Kusto Query Language (KQL) which is used in Log Analytics.

## Key Concepts
- Microsoft Intune
- Log Analytics
- Azure Monitor
- AuditLogs
- Diagnostic settings
- Kusto Query Language (KQL)
- Alert rules
- Azure Monitor Agent
- [AS operator](https://kqlsearch.com/blog/as-operator/) (New from KQL Cafe 28. November 2023)
- Sysmon (New from Jeffrey's blog post)

## Configuration
1. Organize your Intune policy configurations using a common naming scheme, such as the one provided in the article.
2. Configure Intune Diagnostic settings to ship AuditLogs to a Log Analytics workspace.
3. Create an Azure Monitor Alert rule using KQL queries to monitor for specific policy changes.
4. Follow the steps outlined in "Azure Monitor Agent to monitor Windows devices (1/2) – Setup" by Jannik Reinhard to set up Azure Monitor Agent on Windows devices and collect data from them.
5. Utilize tools like [KQL Query Helper](https://chat.openai.com/g/g-bE8NlTPzO-kql-query-helper) for assisting with KQL queries.
6. Explore the AS operator to run queries at specific points in your data (New from KQL Cafe 28. November 2023).
7. [NEW] Stream Azure AD Identity Protection events to Microsoft Sentinel/ Log Analytics (Jeffrey, September 21, 2021)
8. Deploy Sysmon for additional data collection (New from Jeffrey's blog post)

## Common Pitfalls
- Not following a consistent naming scheme for policies can make it difficult to manage and monitor them effectively.
- Failing to configure Intune Diagnostic settings properly may result in AuditLogs not being shipped to the Log Analytics workspace.
- [CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure Monitor Agent setup, but Bert-Jan Pals mentions no specific pitfalls in his article]

## KQL / PowerShell
```
In
```
(KQL query from the article)

## Related Topics
- [Azure Monitor](wiki:azure_monitor)
- [Log Analytics](wiki:log_analytics)
- [workspace](wiki:workspace)
- [DCR](wiki:dcr)
- [DCE](wiki:dce)
- [Azure Monitor Agent](wiki:azure_monitor_agent)
- [AS operator](https://kqlsearch.com/blog/as-operator/) (New from KQL Cafe 28. November 2023)
- [Stream Azure AD Identity Protection events to Microsoft Sentinel/ Log Analytics](wiki:stream_azure_ad_identity_protection_events) (New source article by Jeffrey)
- [Sysmon](https://jeffreyappel.nl/category/security/) (New from Jeffrey's blog post)

## New Source Article: "How to store Defender XDR data for years in Sentinel data lake without expensive ingestion cost"
Author: Jeffrey

## New Source Content:
[Not included as it is not related to the topic of this wiki entry]

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Stream A

New source article: "Deploy Sysmon and collect additional data with Sentinel and the AMA agent"
Author: Jeffrey
New source content:
# Deploy Sysmon and collect additional data with Sentinel and the AMA agent

Deploy Sysmon and collect additional data with Sentinel and the AMA agent




[March 30, 2026](https://jeffreyappel.nl/automatic-migration-from-defender-for-identity-sensor-v2-to-v3-x-and-gmsa-changes/)


9 min read


[March 23, 2026](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/)


7 min read


[February 12, 2026](https://jeffreyappel.nl/how-to-secure-microsoft-copilot-studio-agents-with-real-time-protection/)


13 min read


[February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)


9 min read


[February 2, 2026](https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x/)


5 min read


[January 20, 2026](https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years/)


10 min read


[January 6, 2026](https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage/)


4 min read




## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Deploy Sysmon and collect additional data with Sentinel and the AMA agent

[Security](https://jeffreyappel.nl/category/security/)

# Deploy Sysmon and collect additional data with Sentinel and the AMA agent

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[January 26, 2023](https://jeffreyappel.nl/deploy-sysmon-and-collect-data-with-sentinel-and-the-ama-agent/)
2


10 min read

**System Monitor (Sysmon) is one of the most common add-ons for Windows logging. With Sysmon, you can detect malicious activity by tracking code behavior and network traffic. Sysmon is part of the Sysinternals package and is owned by Microsoft.** **Sysmon can be used for collecting more logs**.

|  |
| --- |
| ****Blog information:**** Blog published: October 10, 2022 Blog latest updated: January 26, 2023 |