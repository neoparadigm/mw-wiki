---
conflict_topics:
- intune/security/bitlocker-management
- intune/deployment/windows-autopatch
conflicts:
- '[CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention
  it]'
context_note: Intune Reporting Log Analytics is part of the intune domain. Synthesised
  from 2 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2023-05-21'
  title: Mastering Intune Reporting and Analytics
  url: https://jannikreinhard.com/2023/05/21/mastering-intune-reporting-and-analytics
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2026-04-08'
  title: Create Custom Dashboards Alerts And 30-Day Compliance Trends Using MS Intune
    And Azure Log Analytics HTMD Blog
  url: https://www.anoopcnair.com/compliance-ms-intune-and-azure-log-analytics
stale_after: '2026-06-17'
title: Intune Reporting with Log Analytics
topic: intune/reporting/intune-reporting-log-analytics
---

# Intune Reporting with Log Analytics

## Overview
Intune Reporting with Log Analytics provides a method to leverage Microsoft Intune data in Azure Monitor for advanced analytics and reporting capabilities. This approach is crucial for IT administrators seeking to gain insights into the state of their managed devices, security vulnerabilities, policy compliance, and device issues.

The new source article introduces that Microsoft Intune now supports advanced reporting with **Azure Log Analytics**, allowing organizations to track device compliance trends over longer periods and create custom queries for deeper data analysis. Visual dashboards make it easier to understand and share insights.

## Key Concepts
- Integration of Intune with Azure Monitor
- Utilization of Log Analytics workspace
- Diagnostic settings configuration for sending Intune logs to Log Analytics
- Querying Intune data using KQL (Kusto Query Language)
- Creating custom dashboards and alerts [CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention it]

## Configuration
1. Create an Azure Log Analytics workspace if not already available.
2. Configure diagnostic settings in the Intune tenant to send logs to the created Log Analytics workspace.
3. Verify that logs are being received by the workspace.
4. Create custom dashboards and alerts using KQL queries [CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention it]

## Common Pitfalls
- Misconfiguration of diagnostic settings, leading to missing or incomplete data in Log Analytics.
- Incorrect KQL queries resulting in improper data retrieval or interpretation.

## KQL / PowerShell
[The article does not provide specific KQL queries or PowerShell scripts related to Intune Reporting with Log Analytics.]

## Related Topics
- [Intune reporting](/wiki/Intune_reporting)
- [Log Analytics](/wiki/Log_Analytics)
- [Diagnostic settings](/wiki/Azure_Monitor_diagnostic_settings)
- [Device compliance report](/wiki/Device_compliance_report)
- [Intune logs](/wiki/Intune_logs)
- [Custom dashboards and alerts](#custom-dashboards-and-alerts)