---
conflicts:
- '[CONFLICT: The new source mentions a blog post from Sarah about documenting KQL
  queries, but it is not included in the existing entry.]'
- '[CONFLICT: The new source mentions Thomas Naunheim has developed a KQL function
  that generates a summarized overview of all directory role assignments, enriched
  with details from his #EntraOps classification and role definitions. This function
  is available from his GitHub repo.]'
- '[CONFLICT: The new source mentions a function that generates a summarized overview
  of all directory role assignments, but it is not included in the existing entry.]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Cafe - June 2025
  url: https://kqlcafe.com/shownotes/2025/KQL%20Cafe%20-%20June%202025
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Cafe - March 2025
  url: https://kqlcafe.com/shownotes/2025/KQL%20Cafe%20-%20March%202025
stale_after: '2026-05-27'
title: KQL — Privilege Escalation Detection
topic: sentinel/kql/privilege-escalation-queries
---

# KQL — Privilege Escalation Detection

## KQL — Privilege Escalation Detection

### Overview
This topic focuses on using KQL (Kusto Query Language) for detecting privilege escalation in Microsoft Office 365, a crucial aspect of securing digital workspaces. The ability to identify and prevent unauthorized access or elevated privileges is essential for maintaining the integrity and security of an organization's data.

### Key Concepts
- KQL Queries: Utilizing KQL queries to detect potential privilege escalation cases, such as DLL hijacking, communication over insecure channels, and sensitive Microsoft Graph delegated permission access. [CONFLICT: The new source mentions a blog post from Sarah about documenting KQL queries, but it is not included in the existing entry.]
- Azure Sentinel: A cloud-native security information and event management (SIEM) solution that enables organizations to collect, analyze, and act on security data across their entire digital estate.
- EntraOps Classification Files: Open-source scripts for classifying files in Azure Active Directory (AAD) based on their sensitivity and access levels. [CONFLICT: The new source mentions Thomas Naunheim has developed a KQL function that generates a summarized overview of all directory role assignments, enriched with details from his #EntraOps classification and role definitions. This function is available from his GitHub repo.]

### Configuration
1. Install Azure Sentinel and connect it to your Microsoft 365 environment.
2. Import the provided KQL queries into Azure Sentinel's Hunting Queries section.
3. Set up alerts for specific events, such as suspicious SSH connections or devices with external RDP connections.
4. Configure EntraOps Classification Files to classify sensitive files in AAD based on their permissions and access levels. [CONFLICT: The new source mentions a function that generates a summarized overview of all directory role assignments, but it is not included in the existing entry.]

### Common Pitfalls
- Incorrectly configured queries may generate false positives or miss genuine threats, leading to alert fatigue or missed opportunities for remediation.
- Failing to regularly update and refine KQL queries can result in outdated detection rules that do not account for new attack vectors or techniques. [CONFLICT: The new source mentions a function that generates a summarized overview of all directory role assignments, but it is not included in the existing entry.]

### KQL / PowerShell
```kql
// Example KQL query for detecting potential DLL hijacking cases
AzureActivity
| where OperationName == "FileDownload"
| where FileName contains ".dll"
| where ClientIpAddress != "127.0.0.1"
| summarize CountBy(ClientIpAddress, OperationName) by bin(TimeGenerated, 5m), InitiatorId
```

### Related Topics
- KQL Benchmark Dashboard
- PIM activation
- Role assignment
- Group membership change
- Privilege KQL Queries (this topic)
- [Documenting KQL Queries](https://www.techielass.com/documenting-your-kql-queries/) (new source content)
- [Kusto Detective Agency S03](https://detective.kusto.io/inbox?season=Fabric) (new source content)
- [IdentityInfo Table – Entra ID – eligible Roles](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-identityinfo-table) (new source content)
- [New Cybersecurity Functions](https://learn.microsoft.com/en-us/kusto/functions-library/) (new source content)