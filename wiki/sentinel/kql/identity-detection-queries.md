---
conflicts:
- '[CONFLICT: Bert-Jan Pals says the Microsoft 365 Defender Connector allows additional
  tables to be ingested into Microsoft Sentinel, but this is not mentioned in the
  existing entry.]'
- '[CONFLICT: Bert-Jan Pals discusses this in more detail, but the existing entry
  already provides a brief overview.]'
- '[CONFLICT: Bert-Jan Pals says the Microsoft 365 Defender Connector is relevant
  to ingesting additional data into Azure Sentinel, while the existing entry does
  not mention it.]'
- '[CONFLICT: Bert-Jan Pals mentions filtering the ProductCodeCpe column within the
  DeviceTvmSoftwareInventory table to also identify software for which there is not
  a CPE, while the existing entry does not mention this.]'
- '[CONFLICT: Bert-Jan Pals mentions the Microsoft 365 Defender Connector as a way
  to ingest additional data into Azure Sentinel, which is not mentioned in the existing
  entry.]'
- '[CONFLICT: Bert-Jan Pals says the Microsoft 365 Defender Connector is relevant
  to ingesting additional data into Azure Sentinel, while the existing entry does
  not mention it]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-08-04'
  title: Protecting against password spray attacks with Azure Sentinel and Azure AD
  url: https://jeffreyappel.nl/protecting-against-password-spray-attacks-with-azure-sentinel-and-azure-ad
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Detections - Time
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20April%202022
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Cafe August 2022
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20August%202022
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: Hello from Down Under
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20February%202022
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Workbooks
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20March%202022
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: Hello KQL
  url: https://kqlcafe.com/shownotes/2022/KQL%20Cafe%20-%20%20January%202022
stale_after: '2026-05-27'
title: KQL — Identity and Sign-in Detection
topic: sentinel/kql/identity-detection-queries
---

# KQL — Identity and Sign-in Detection

## Overview
KQL (Kusto Query Language) is used for identity and sign-in detection in Azure Sentinel to identify potential password spray attacks. This topic matters as it helps organizations protect against brute force attacks where a malicious actor attempts the same password on many accounts.

The new source article "Hello KQL" by Bert-Jan Pals provides additional insights into learning and using KQL.

## Key Concepts
- Password Spray Attacks: A type of brute force attack where a hacker tries the same password on multiple accounts before moving on to another one.
- Azure AD Password Protection: A feature that helps protect against password spray attacks by blocking users from using commonly used, easily guessable, or compromised passwords.
- Azure AD Identity Protection: A feature that provides real-time detection and mitigation of suspicious sign-ins based on risky user behavior and account compromise.
- Azure Sentinel Insights: Provides security analysts with prebuilt analytics and threat intelligence to help detect and respond to threats more effectively.

[CONFLICT: Bert-Jan Pals mentions the Microsoft 365 Defender Connector as a way to ingest additional data into Azure Sentinel, which is not mentioned in the existing entry.]

## Configuration
1. Enable Azure AD Password Protection in the Azure portal.
2. Configure Azure AD Identity Protection to monitor for risky sign-ins.
3. Create a custom Azure Sentinel rule to detect password spray attacks using KQL queries.
4. Ingest additional data into Microsoft Sentinel from Microsoft 365 Defender using the Microsoft 365 Defender Connector (see [What's new in KQL](#whats-new-in-kql)).
5. Learn about the parse-kv operator for parsing JSON data more efficiently (see [Learning KQL](#learning-kql)).
6. Utilize the DeviceTvmSoftwareEvidenceBeta table for advanced hunting related to software evidence (see [What's new in KQL](#whats-new-in-kql)).
7. Use the AADSignInEventsBeta table for information about Azure Active Directory interactive and non-interactive sign-ins (see [What's new in KQL](#whats-new-in-kql)).
8. Configure large watchlists with up to 500 MB file size by storing the files in an Azure Blob Storage account (see "KQL Workbooks").
9. Filter the ProductCodeCpe column within the [DeviceTvmSoftwareInventory](https://docs.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-devicetvmsoftwareinventory-table?view=o365-worldwide) table to also identify software for which there is not a CPE (see "KQL Workbooks").
10. [CONFLICT: Bert-Jan Pals mentions the Microsoft 365 Defender Connector as a way to ingest additional data into Azure Sentinel, which is not mentioned in the existing entry.]

## Common Pitfalls
- Not configuring Azure AD Password Protection and Azure AD Identity Protection

## Related Topics
- KQL Detections - Time (new)
- KQL Workbooks (new)
- [KQL Cafe](https://github.com/KQLCafe/website/blob/gh-pages/Presentations/KQL%20Cafe%20-%20January%202022.pdf) (new from "Learning KQL")

## Learning KQL
- parse-kv operator: [Learning KQL](#learning-kql)

## What's new in KQL
- Creating large watchlists
- DeviceTvmSoftwareInventory table
- AADSignInEventsBeta table (new from "KQL Workbooks")
- Microsoft 365 Defender Connector (new from [CONFLICT: Bert-Jan Pals says the Microsoft 365 Defender Connector is relevant to ingesting additional data into Azure Sentinel, while the existing entry does not mention it])
- Filtering the ProductCodeCpe column within the DeviceTvmSoftwareInventory table to also identify software for which there is not a CPE (new from "KQL Workbooks")