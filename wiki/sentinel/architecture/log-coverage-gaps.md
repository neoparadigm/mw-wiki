---
conflicts:
- '[CONFLICT: Jeffrey mentions Azure Data Explorer, but it''s not explicitly listed
  as a key concept in the existing entry]'
- '[CONFLICT: Jeffrey mentions streaming data directly to Log Analytics and Storage
  account/event hub, but these methods are not explicitly listed as configuration
  options in the existing entry]'
- '[CONFLICT: Add Azure Data Explorer]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2026-01-20'
  title: How to natively archive Defender XDR logs for up to 12 years
  url: https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-08-04'
  title: How to store Defender XDR data for years in Sentinel data lake without expensive
    ingestion cost
  url: https://jeffreyappel.nl/how-to-store-defender-xdr-data-for-years-in-sentinel-data-lake-without-expensive-ingestion-cost
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-07-30'
  title: 'Microsoft Sentinel data lake: How to use/enable and set-up the unified data
    lake'
  url: https://jeffreyappel.nl/microsoft-sentinel-data-lake-how-to-use-enable-and-set-up-the-unified-datalake
stale_after: '2026-05-27'
title: Sentinel Log Coverage and Ingestion Gaps
topic: sentinel/architecture/log-coverage-gaps
---

# Sentinel Log Coverage and Ingestion Gaps

## Sentinel Log Coverage and Ingestion Gaps

### Overview
This topic discusses the limitations and gaps in log coverage and ingestion within Microsoft Sentinel, particularly with regards to Defender XDR logs. Understanding these gaps is crucial for effective security operations and compliance. The entry has been updated with new information from a blog post by Jeffrey Appel.

### Key Concepts
- Log coverage: The extent to which various security events are captured by Sentinel.
- Ingestion: The process of collecting and sending data from various sources into Sentinel.
- Data lake tier ingestion: A feature that allows Microsoft XDR Advanced Hunting tables to be directly ingested into the Microsoft Sentinel data lake.
- Workspace transformation rules: Rules used to transform data before it is ingested into Sentinel.
- Custom table: A user-created table in Sentinel for storing specific types of data.
- Azure Data Explorer: A data management system that allows users to run complex queries against large amounts of data. [New]

### Configuration
- To enable data lake tier ingestion for Microsoft XDR Advanced Hunting tables, follow the steps outlined in [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/sentinel/data-lake-ingestion).
- For the workaround mentioned in Jeffrey Appel's blog post, refer to [Jeffrey's blog post](https://jeffreyappel.nl/how-to-store-defender-xdr-data-for-years-in-sentinel-data-lake-without-expensive-ingestion-cost/).
- Jeffrey mentions streaming data directly to Log Analytics and Storage account/event hub, but these methods are not explicitly listed as configuration options in the existing entry. [CONFLICT]

### Common Pitfalls
- Failing to properly configure data lake tier ingestion can result in high ingestion costs.
- The workaround mentioned by Jeffrey, while functional, is complex and harder to maintain compared to native solutions.

### KQL / PowerShell
[This section is not applicable as it does not cover any specific queries or scripts.]

### Related Topics
- Log coverage
- Data connector
- Ingestion
- Diagnostic settings
- Log gap
- Azure Data Explorer [New]

### Blog Post
> [Security](https://jeffreyappel.nl/category/security/) > How to store Defender XDR data for years in Sentinel data lake without expensive ingestion cost

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[August 4, 2025](https://jeffreyappel.nl/how-to-store-defender-xdr-data-for-years-in-sentinel-data-lake-without-expensive-ingestion-cost/)
6


12 min read

In recent years, an increasing number of customers have requested options to extend retention in Microsoft Defender XDR beyond the default 30 days at a low cost, all with the requirement of having the KQL experience available.

|  |
| --- |
| **Blog information:**Feature is currently in General Available  Blog update: 27 october 2025 |

With security log volumes growing fast, teams are forced into making painful tradeoffs: reduce logging by risking blind spots, shorten retention by compromising forensic depth, or absorb unsustainable costs when aiming to manage all their security data within a SIEM.

With the new Sentinel data lake Microsoft released a new foundation for agentic defense and brings all security data together from Microsoft sources and third-party sources. One of the biggest benefits is to simplify security data management without having to manage complex infrastructures with Azure Data Explorer/ Storage blobs and other data management systems. Of course, there is a balance where Azure Data Explorer is useful and the new Sentinel data lake Microsoft released, both products are different in terms of the use-case, cost, features, and storage – all more on this later in the blog.

## In the p