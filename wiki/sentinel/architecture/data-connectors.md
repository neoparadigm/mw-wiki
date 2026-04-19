---
conflicts: []
context_note: Data Connectors is part of the sentinel domain. Synthesised from 1 community
  source.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-01-27'
  title: Monitor Microsoft Sentinel Data Connectors using Health Monitoring and Logic
    App
  url: https://jeffreyappel.nl/monitor-microsoft-sentinel-data-connectors-using-health-monitoring-and-logic-app
stale_after: '2026-06-02'
title: Sentinel Data Connectors Configuration
topic: sentinel/architecture/data-connectors
---

# Sentinel Data Connectors Configuration

## Sentinel Data Connectors Configuration

### Overview
This topic discusses how to monitor Microsoft Sentinel Data Connectors using Health Monitoring and Logic App. The new feature allows for checking the health of Microsoft Sentinel instances, particularly data connectors like Amazon Web Services (CloudTrail), Dynamics 365, Office 365, Office ATP, Threat Intelligence – TAXII, and Threat Intelligence Platforms.

### Key Concepts
- Microsoft Sentinel Health Monitoring feature
- SentinelHealth data table
- Enabling health monitoring in the Microsoft Sentinel console
- Configuring diagnostic settings for Microsoft Sentinel's health monitoring feature

### Configuration
1. Open **Microsoft Sentinel** and the correct **Sentinel workspace**.
2. Go to **Settings(1)** in the left menu, then access the **settings tab at the top(2)**.
3. Open the **Health Monitoring section (3)** on the settings page and click **Configure Diagnostic settings (4)**.
4. To turn on Microsoft Sentinel’s health monitoring feature, select **Configure diagnostic settings (4)** and configure the correct destination details.
5. Click on **Add diagnostic settings (5)**.
6. Fill in the name – select either **allLogs** or only **DataConnectors logs**. Configure the correct destination. For using the Sentinel workspace, select **Send to Log Analytics workspace**.

### Common Pitfalls
- Ensuring that the selected data connectors are supported by the SentinelHealth data table.
- Properly configuring the diagnostic settings for Microsoft Sentinel's health monitoring feature.

### KQL / PowerShell
N/A (The article does not provide any relevant queries or scripts.)

### Related Topics
- [Data Connector](data_connector)
- [Sentinel connector](sentinel_connector)
- [MDE connector](mde_connector)
- [M365 connector](m365_connector)
- [CEF connector](cef_connector)