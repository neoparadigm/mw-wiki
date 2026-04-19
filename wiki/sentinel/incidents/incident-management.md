---
conflicts: []
context_note: Incident Management is part of the sentinel domain. Synthesised from
  1 community source.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Thomas Naunheim
  crawled: '2026-04-18'
  date: '2024-01-12'
  title: Microsoft Entra Workload ID - Incident Response with Microsoft Sentinel Playbooks
    and Conditional Access
  url: https://www.cloud-architekt.net/entra-workload-id-incident-response
stale_after: '2026-06-17'
title: Sentinel Incident Management and Triage
topic: sentinel/incidents/incident-management
---

# Sentinel Incident Management and Triage

## Sentinel Incident Management and Triage

Incident management and triage is a crucial aspect of Microsoft Entra Workload ID's incident response process, focusing on automating responses to malicious activities and threats using Conditional Access and Microsoft Sentinel Playbooks. This process helps in blocking compromised service principals for further malicious activity.

## Key Concepts
- Incident Response Playbook templates
- Service Principal compromise confirmation
- Continuous access evaluation (CAE) for workload identities
- Disable service principal and confirm service principal compromise events
- Entity mapping in Microsoft Sentinel Analytics Rules

## Configuration
1. Ensure the `ObjectId` of the Service Principal is available by using the trigger of Microsoft Sentinel Incidents.
2. Configure a Microsoft Sentinel Playbook with the least privileges for incident response scenarios.
3. Utilize Conditional Access for Workload ID to stop further sign-in activity when needed.

## Common Pitfalls
- The incident playbook trigger in Microsoft Sentinel may not provide the `Application Id` required for Graph API calls, making it necessary to establish a clean entity mapping in Analytics Rules.

## KQL / PowerShell
[No specific queries or scripts provided in the article]

## Related Topics
- Incident management
- Triage
- Incident queue
- Alert grouping
- Incident enrichment