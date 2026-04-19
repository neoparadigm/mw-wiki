---
conflicts: []
context_note: Log Coverage Gaps is part of the sentinel domain. Synthesised from 1
  community source.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Thijs Lecomte
  crawled: '2026-04-18'
  date: '2024-07-15'
  title: 'Practical Sentinel: Adding Networking Data to Microsoft Sentinel'
  url: https://practical365.com/adding-networking-data-to-microsoft-sentinel
stale_after: '2026-06-02'
title: Sentinel Log Coverage and Ingestion Gaps
topic: sentinel/architecture/log-coverage-gaps
---

# Sentinel Log Coverage and Ingestion Gaps

## Sentinel Log Coverage and Ingestion Gaps

This topic discusses the importance of understanding and addressing gaps in log coverage and ingestion within Microsoft Sentinel, focusing on networking data sources such as firewalls, proxies, switches, and access points.

## Key Concepts
- Prioritizing data connectors in Sentinel
- Firewall, proxy, switch, and access point functionalities
- Layer 7 information and its significance for Microsoft Defender for Endpoint (MDE)
- TLS inspection and Intrusion Prevention Systems (IPS)
- Data sources with limited details or intelligence

## Configuration
- Prioritize data connectors based on the use case, as discussed in [Prioritizing Data Connectors in Microsoft Sentinel](https://practical365.com/prioritizing-data-connectors-in-microsoft-sentinel/)
- Configure networking devices to export logs to Azure Monitor Logs and connect them to Microsoft Sentinel

## Common Pitfalls
- Overlooking the importance of networking data sources in Sentinel, leading to blind spots in threat detection
- Failing to prioritize data connectors appropriately, resulting in suboptimal threat detection and response
- Neglecting to configure proxies on Defender for Endpoint supported devices, limiting their effectiveness

## KQL / PowerShell
[No specific queries or scripts provided in the source article]

## Related Topics
- [Log Coverage](log_coverage)
- [Data Connector](data_connector)
- [Ingestion](ingestion)
- [Diagnostic Settings](diagnostic_settings)
- [Log Gap](log_gap)