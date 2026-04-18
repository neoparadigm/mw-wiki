---
conflict_topics:
- intune/security/windows-security-baseline
- windows/updates/windows-update-for-business
conflicts:
- '[CONFLICT: Bert-Jan Pals says the new content adds Zeek and Azure Resource Graph,
  existing entry does not mention these topics.]'
context_note: Identity Detection Queries is part of the sentinel domain. Synthesised
  from 6 community sources.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2022-10-03'
  title: Sentinel Hunting Query Pack &#8211; DCSecurityOperations
  url: https://danielchronlund.com/2022/10/03/sentinel-hunting-query-pack-dcsecurityoperations
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe August 2022
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20August%202022
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe September 2022
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20September%202022
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe - February 2023
  url: https://kqlcafe.com/shownotes/2023/KQL%20Cafe%20-%20February%202023
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe October 2023
  url: https://kqlcafe.com/shownotes/2023/KQL%20Cafe%20-%20October%202023
- author: Bert-Jan Pals
  crawled: '2026-04-18'
  date: ''
  title: KQL Cafe September 2023
  url: https://kqlcafe.com/shownotes/2023/KQL%20Cafe%20-%20September%202023
stale_after: '2026-06-02'
title: KQL — Identity and Sign-in Detection
topic: sentinel/kql/identity-detection-queries
---

# KQL — Identity and Sign-in Detection

## Overview
The "Sentinel Hunting Query Pack - DCSecurityOperations" by Daniel Chronlund provides a collection of KQL (Kusto Query Language) queries for identity and sign-in detection in Microsoft Sentinel. These queries are designed to help proactively detect anomalies and suspicious behaviors related to user identities and sign-ins, enhancing the threat hunting capabilities of Microsoft Sentinel.

The "KQL Cafe August 2022", "KQL Cafe September 2022", and "KQL Cafe February 2023" articles discuss various topics related to KQL, including new features in Sentinel Data Retention, Archive, and Restore, Guided Hunting in Microsoft 365 Defender, working with IOCs (Indicators of Compromise), learning KQL through parse-kv operator, Microsoft Learn resources, tampering events detection, parsing command lines, Go HUNT - ABC of threat hunting, and more.

The "KQL Cafe October 2023" article by Bert-Jan Pals focuses on analyzing MicrosoftGraphActivityLogs, App Governance - Entra ID Consented Apps Cleanup, Client Inspector, Hunting for Curl, and Zeek SMTP.

The new "KQL Cafe September 2023" article by Bert-Jan Pals adds content related to Zeek and Azure Resource Graph.

## Key Concepts
- KQL: Kusto Query Language is a powerful query language used in Azure Monitor and Microsoft Sentinel for analyzing large volumes of data.
- Threat Hunting: A proactive approach to cybersecurity that involves searching for potential threats within an IT environment.
- Microsoft Sentinel: A cloud-native SIEM solution that provides threat detection, security analytics, and automated response capabilities.
- GitHub Repo: A repository on GitHub where the hunting queries are stored and managed centrally.

## Configuration
To automatically deploy all Sentinel hunting queries from the DCSecurityOperations GitHub repo, ensure you have PowerShell 7.2 or later, git, AZSentinel PowerShell module, and powershell-yaml PowerShell module installed. Then, run the provided PowerShell script to download and deploy the queries.

## Common Pitfalls
Ensure that existing queries are updated on import, as long as the name of the query is the same.

## KQL / PowerShell
The DCSecurityOperations GitHub repo includes a set of hunting queries for identity and sign-in detection. To download and deploy these queries using PowerShell, run the following script:

```
# Clone the DCSecurityOperations GitHub repo.
git clone https://github.com/DanielChronlund/DCSecurityOperations

# Connect to Azure AD (requires at least the Sentinel Contributor role on the Sentinel resource group).
Connect-AzAccount

# Import/update all hunting queries from DCSecurityOperations.
Get-Item ".\DCSecurityOperations\Sentinel Hunting Queries\*.yaml" | Import-AzSentinelHuntingRule -WorkspaceName "NAME OF YOUR SENTINEL WORKSPACE"
```

## Related Topics
- KQL
- SigninLogs
- identity detection
- risky sign-in
- legacy auth KQL
- Sentinel Data Retention, Archive, and Restore
- Guided Hunting in Microsoft 365 Defender
- Working with IOCs (Indicators of Compromise)
- parse-kv operat
- MicrosoftGraphActivityLogs
- Azure Resource Graph
- Zeek

## New Source Article: "KQL Cafe September 2023"
Author: Bert-Jan Pals
New source content:
# KQL Cafe September 2023

KQL Cafe September 2023 - KQL Cafe

[Skip to content](#kql-cafe-september-2023)

## Zeek

- [Enrich your advanced hunting experience using network layer signals from Zeek](https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/enrich-your-advanced-hunting-experience-using-network-layer/ba-p/3794693)

### InboundInternetScanInspected

```
DeviceNetworkEvents
| where ActionType == "InboundInternetScanInspected"
| project TimeGenerated, DeviceName, LocalIP, LocalPort, RemoteIP, RemotePort, RemoteIPType
| extend geoinfo = geo_info_from_ip_address(LocalIP)
| extend country = tostring(geoinfo.country)
| extend city = tostring(geoinfo.city)
| extend state = tostring(geoinfo.state)
| project-away geoinfo
```

### FTP

```
DeviceNetworkEvents
| where ActionType == "FtpConnectionInspected"
| extend json = todynamic(AdditionalFields)
| extend command = tostring(json.command)
| extend reply_code = tostring(json.reply_code)
| extend reply_msg = tostring(json.reply_msg)
| extend direction = tostring(json.direction)
| extend user = tostring(json.user)
| extend arg = tostring(json.arg)
| extend cwd = tostring(json.cwd)
```

## Azure Resource Graph

- [Query Azure Resource Graph from Azure Monitor](https://techcommunity.microsoft.com/t5/azure-observability-blog/query-azure-resource-graph-from-azure-monitor/ba-p/3918298)
- [Query data in Azure Data Explorer and Azure Resource Graph from Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/azure-monitor-data-explorer-proxy)
- [Azure Resource Graph table and resource type reference](https://learn.microsoft.com/en-us/azure/governance/resource-graph/reference/supported-tables-resources)

### Show all Resource Types

```
arg("").Resources
| distinct type
```

### Log Analytics Workspace Info

```
arg("").Resources
| where type == "microsoft.operationalinsights/workspaces"
| extend SKUName = tostring(parse_json(tostring(properties.sku)).name)
| extend dailyQuotaGb = tostring(parse_json(tostring(properties.workspaceCapping)).dailyQuotaGb)
| extend quotaNextResetTime = todatetime(tostring(parse_json(tostring(properties.workspaceCapping)).quotaNextResetTime))
| extend retentionInDays = tostring(properties.retentionInDays)
| project name, location, resourceGroup, retentionInDays,SKUName, dailyQuotaGb, quotaNextResetTime
```

### Identify Azure Subscriptions that are not monitored by the Azure Activity Data Connector in Sentinel

```
// Identify Azure Subscriptions that are not monitored by the Azure Activity Data Connector in Sentinel
let allsubscriptions =
arg("").resourcecontainers
| where type == "microsoft.resources/subscriptions"
| distinct subscriptionId, name;
allsubscriptions
| join kind=leftouter  (AzureActivity
| extend AzureActivitySyubscriptionId = SubscriptionId
| distinct AzureActivitySyubscriptionId)
on $left. subscriptionId == $right.AzureActivitySyubscriptionId
| extend IsMonitored = iff(isempty(AzureActivitySyubscr
```
[CONFLICT: Bert-Jan Pals says the new content adds Zeek and Azure Resource Graph, existing entry does not mention these topics.]

[Task complete]