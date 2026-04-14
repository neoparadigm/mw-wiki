---
conflicts: []
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Bert-Jan Pals
  crawled: '2026-04-14'
  date: ''
  title: KQL Cafe - March 2025
  url: https://kqlcafe.com/shownotes/2025/KQL%20Cafe%20-%20March%202025
stale_after: '2026-05-29'
title: KQL — Privilege Escalation Detection
topic: sentinel/kql/privilege-escalation-queries
---

# KQL — Privilege Escalation Detection

## Overview
This topic discusses the use of KQL (Kusto Query Language) for Privilege Escalation Detection in Microsoft Defender XDR and Azure Sentinel. The expansion of the IdentityInfo table to include eligible roles from Microsoft Entra managed by Privileged Identity Management (PIM) is a significant development, enabling more comprehensive threat detection.

## Key Concepts
- IdentityInfo Table
- Microsoft Defender XDR
- Microsoft Entra
- Privileged Identity Management (PIM)
- KQL Functions for Anomaly Detection and Graph Analysis

## Configuration
1. Ensure you have the necessary permissions to access and query the IdentityInfo table in Microsoft Defender XDR.
2. Implement the provided KQL functions for anomaly detection and graph analysis in your queries.
3. Utilize Thomas Naunheim's KQL function for generating a summarized overview of all directory role assignments, enriched with details from his #EntraOps classification and role definitions.

## Common Pitfalls
- Incorrectly configuring permissions or missing necessary permissions to access the IdentityInfo table.
- Failing to implement the provided KQL functions for anomaly detection and graph analysis in queries.
- Not utilizing Thomas Naunheim's KQL function for generating a summarized overview of all directory role assignments.

## KQL / PowerShell
[The article does not provide any specific KQL or PowerShell queries related to this topic.]

## Related Topics
- KQL
- PIM activation
- Role assignment
- Group membership change
- Privilege escalation detection in Azure Sentinel and Microsoft Defender XDR