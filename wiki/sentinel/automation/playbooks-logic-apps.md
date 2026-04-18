---
conflicts: []
context_note: Playbooks Logic Apps is part of the sentinel domain. Synthesised from
  3 community sources.
domain: sentinel
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-03-26'
  title: Automated incident triage with Security Copilot and Microsoft Sentinel/ Defender
    XDR
  url: https://jeffreyappel.nl/automated-incident-triage-with-security-copilot-and-microsoft-sentinel-defender-xdr
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2023-02-08'
  title: Microsoft Defender for Endpoint Automation via Logic Apps and Sentinel
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-automation-via-logic-apps-and-sentinel-part9
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-06-01'
  title: Use automation/playbooks in Microsoft Sentinel during incident update activity
    using update triggers
  url: https://jeffreyappel.nl/use-automation-playbooks-in-microsoft-sentinel-during-incident-update-activity-using-update-triggers
stale_after: '2026-06-17'
title: Sentinel Playbooks and Logic Apps Automation
topic: sentinel/automation/playbooks-logic-apps
---

# Sentinel Playbooks and Logic Apps Automation

## Sentinel Playbooks and Logic Apps Automation

### Overview
Sentinel Playbooks and Logic Apps Automation is a powerful feature in Microsoft Sentinel that enables automated response to security incidents using Security Orchestration, Automation, and Response (SOAR) workflows. This topic matters because it allows for faster and more efficient incident handling by automating repetitive tasks and integrating AI analysis into the alerting process.

### Key Concepts
- SOAR: Security Orchestration, Automation, and Response
- Automation Rules: Defining triggers and actions in Sentinel
- Playbooks: Logic Apps with triggers from Sentinel alerts or incidents
- GenAI analysis: AI-powered data enrichment using Security Copilot
- Microsoft Defender for Endpoint Automation: Automating responses to security incidents using Logic Apps and Defender APIs
- Incident update triggers: Automatically triggering playbooks when an incident is updated (New source article feature)

### Configuration
1. Onboard Security Copilot following the guide: [How to onboard and getting started with Copilot for Security](https://jeffreyappel.nl/how-to-onboard-and-getting-started-with-copilot-for-security/)
2. Create a new playbook in Sentinel and configure it to use the Security Copilot connector for AI-powered data enrichment.
3. Define triggers and conditions for your automation rules to link analytic rules to playbooks.
4. Configure actions within the playbook, such as enrichments of data from third-party source providers or custom automation to auto-enrich or auto-close alerts based on decisions or data matching.
5. Utilize Logic Apps and Defender APIs for additional automation capabilities beyond those provided by Sentinel alone.
6. Set up incident update triggers for your playbooks to automatically run when an incident is updated (New source article feature).

### Common Pitfalls
- Failing to properly configure triggers and conditions for automation rules can lead to missed opportunities for automating incident response.
- Incorrectly setting up the Security Copilot connector may result in issues with AI analysis and data enrichment.
- Misconfigurations or errors in Logic Apps and Defender APIs could potentially cause unintended actions or failures in the automated workflow.

### KQL / PowerShell
[This section is not applicable as the source article does not provide any relevant queries or scripts.]

### Related Topics
- [Playbook](playbook)
- [Logic App](logic-app)
- [SOAR](soar)
- [Automated response](automated-response)
- [Incident automation](incident-automation)
- [Microsoft Defender for Endpoint Automation](microsoft-defender-for-endpoint-automation)
- [Incident update triggers](incident-update-triggers) (New source article topic)

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Use automation/playbooks in Microsoft Sentinel during incident update activity using update triggers

[Security](https://jeffreyappel.nl/category/security/)

# Use automation/playbooks in Microsoft Sentinel during incident update activity using update triggers

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[June 1, 2022](https://jeffreyappel.nl/use-automation-playbooks-in-microsoft-sentinel-during-incident-update-activity-using-update-triggers/)
0


6 min read

Automation is critical for modern SOC environments to handle the volume of upcoming threats and manage day-to-day tasks. Ideally most of the features are automated in Microsoft Sentinel during the incident creation, enrichment, update, and closure. For quite some time playbooks can be used for initial enrichment and actions like triage, creating tickets, etc.

Incidents are always changing or updating with new information; it is now possible to use incident update triggers for automation rules and playbooks.

Announcement public preview: [What’s new: Automate full incident lifecycle with incident update triggers](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/what-s-new-automate-full-incident-lifecycle-with-incident-update/ba-p/3450306)

**Note: Feature currently in preview – blog updated 31-5-2022**

## **Incident update triggers for automation rules and playbooks**

Sentinel incidents can be updated by users, API, Defender Sync, and Automation. Another common situation is where alerts may join the incident part of the incident story; performed by user/API/ Sentinel Alert Grouping or Defender sync. Which gives the result: Severity change, reopened by Defender, changed tactics etc.

Now available is the new feature **incident update triggers for automation rules and playbooks**. This allows you to automatically run playbooks when an incident is updated, ensuring that your automated responses stay up-to-date with the latest information about the incident.

To set up incident update triggers for your playbooks:
1. Navigate to the Automation tab in Sentinel and select Playbooks.
2. Create a new playbook or edit an existing one.
3. In the Trigger section, select "Incident update" as the trigger type.
4. Define the conditions under which the playbook should run when an incident is updated, such as changes to the incident severity or tactics.
5. Configure actions within the playbook, such as enrichments of data from third-party source providers or custom automation to auto-enrich or auto-close alerts based on decisions or data matching.
6. Save and publish your playbook.

With incident update triggers for automation rules and playbooks, you can ensure that your automated responses are always up-to-date with the latest information about incidents in Sentinel. This helps to improve the efficiency and effectiveness of your security operations by reducing manual effort and minimizing the time it takes to respond to incidents.