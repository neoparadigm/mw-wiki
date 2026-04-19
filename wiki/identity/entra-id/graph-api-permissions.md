---
conflict_topics:
- identity/entra-id/external-identities
- identity/entra-id/identity-governance
conflicts:
- '[CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges]'
- '[CONFLICT: Michael Morten Sonne mentions inconsistencies across tools]'
- '[CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent
  API coverage, and support for app-only access]'
- '[CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges,
  Jeffrey adds Conditional Access as a tool]'
- '[CONFLICT: Jeffrey does not mention this specifically]'
- '[CONFLICT: Jeffrey adds the ability to export Conditional Access configurations]'
- '[CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges,
  Jeffrey adds Conditional Access as a tool; CONFLICT: Jan Bakker emphasizes the importance
  of Graph API in Microsoft 365]'
- '[CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; CONFLICT:
  Jan Bakker does not specifically mention data exfiltration or privilege escalation
  risks]'
- '[CONFLICT: Jeffrey adds the ability to export Conditional Access configurations;
  Jan Bakker demonstrates how to use browser developer tools and Postman to interact
  with the Graph API]'
- '[CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent
  API coverage, and support for app-only access; Jan Bakker does not specifically
  mention these points]'
- '[CONFLICT: This point is shared by all sources]'
- '[CONFLICT: Michael Morten Sonne mentions the need for regular reviews; Jan Bakker
  emphasizes the importance of regularly reviewing API calls from the Entra admin
  center or Microsoft Admin portal]'
- '[CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; Jan Bakker
  does not specifically mention this]'
context_note: Graph Api Permissions is part of the identity domain. Synthesised from
  6 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2023-02-09'
  title: Microsoft 365 Data Exfiltration &#8211; Attack and Defend
  url: https://danielchronlund.com/2023/02/09/microsoft-365-data-exfiltration-attack-and-defend
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2025-09-02'
  title: 'Closing Microsoft Graph Gaps: My Feedback Portal Request Gains Top 3 in
    Just 4 Days – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/closing-microsoft-graph-gaps-my-feedback-portal-request-gains-top-3-in-just-4-days
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-11-12'
  title: Get all Conditional Access Query&#039;s with a single click using Graph API
  url: https://jeffreyappel.nl/get-all-conditional-access-querys-with-a-single-click-using-graph-api
- author: Jan Bakker
  crawled: '2026-04-18'
  date: '2026-03-06'
  title: How to get better with Graph API - Part one
  url: https://janbakker.tech/how-to-get-better-with-graph-api-part-one
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-02-09'
  title: How to check for OAuth apps with specific Graph permissions assigned
  url: https://jeffreyappel.nl/how-to-check-for-oauth-apps-with-specific-graph-permissions-assigned
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2023-08-03'
  title: Microsoft Entra Workload ID - Introduction and Delegated Permissions
  url: https://www.cloud-architekt.net/entra-workload-id-introduction-and-delegation
stale_after: '2026-06-17'
title: Microsoft Graph API Permissions and Governance
topic: identity/entra-id/graph-api-permissions
---

# Microsoft Graph API Permissions and Governance

## Microsoft Graph API Permissions and Governance

Microsoft Graph API provides a unified programmability model that allows developers to access data across multiple Microsoft services, including Office 365, Windows, and Enterprise Mobility + Security. Proper management of Graph API permissions is crucial for maintaining security and preventing data exfiltration in a Microsoft 365 environment.

## Key Concepts
- Understanding the risks associated with insecure app registrations and privileged API permissions [CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges, Jeffrey adds Conditional Access as a tool; CONFLICT: Jan Bakker emphasizes the importance of Graph API in Microsoft 365]
- Identifying common problems such as missing Multi-Factor Authentication (MFA), excessive Application Administrators, use of client secrets instead of certificates, and insecure Conditional Access configurations [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; CONFLICT: Jan Bakker does not specifically mention data exfiltration or privilege escalation risks]
- Recognizing the potential for privilege escalation and data exfiltration due to risky API permissions [CONFLICT: Jeffrey does not mention this specifically]
- Utilizing tools like `Invoke-DCM365DataExfiltration` and Microsoft Graph API to demonstrate the impact of poor permission management on a Microsoft 365 tenant, and exporting Conditional Access configurations using Microsoft Graph API [CONFLICT: Jeffrey adds the ability to export Conditional Access configurations; Jan Bakker demonstrates how to use browser developer tools and Postman to interact with the Graph API]
- Implementing strict access controls for app registrations, including MFA and limiting Application Administrators [CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent API coverage, and support for app-only access; Jan Bakker does not specifically mention these points]
- Using certificates instead of client secrets to secure app registrations [CONFLICT: This point is shared by all sources]
- Regularly reviewing and auditing app registrations for any insecure configurations [CONFLICT: Michael Morten Sonne mentions the need for regular reviews; Jan Bakker emphasizes the importance of regularly reviewing API calls from the Entra admin center or Microsoft Admin portal]
- Limit the scope of API permissions assigned to apps based on their intended functionality [CONFLICT: This point is shared by all sources]
- New: **Checking for OAuth apps with specific Graph permissions assigned** (Jeffrey)
  * Importance of checking OAuth permissions due to potential attacks like 'OAuth consent grant' and the Midnight Blizzard actor
  * Simulation of a Midnight Blizzard attack scenario
- New: **Introduction and Delegated Permissions for Microsoft Entra Workload ID** (Thomas Naunheim)
  * Overview of Workload Identities and their use in Microsoft Entra
  * Importance of managing Workload IDs at scale, especially in DevOps environments
  * Avoiding assigning 'owner' to service principals or application objects

## New source article: "Microsoft Entra Workload ID - Introduction and Delegated Permissions"
Author: Thomas Naunheim
New source content:

... (The existing entry remains unchanged, as the new source does not add any new information that is not already present in the existing entry.)