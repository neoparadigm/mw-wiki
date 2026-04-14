---
conflicts: []
domain: teams
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: surbhigupta12
  crawled: '2026-04-14'
  date: '2024-09-04'
  title: Overview of app policies to manage apps in Teams - Microsoft Teams
  url: https://learn.microsoft.com/en-us/microsoftteams/app-policies
stale_after: '2026-06-13'
title: Teams App Permission Policies
topic: teams/governance/app-permission-policies
---

# Teams App Permission Policies

## Teams App Permission Policies

### Overview
Teams App Permission Policies are used to govern access and usage of apps within Microsoft Teams. They allow administrators to control app behavior, such as configuring user access to specific apps, pinning allowed apps for users, and managing the upload and use of custom apps.

### Key Concepts
- App permission policies control what apps are available to each user in an organization.
- Permission policies work in tandem with Org-wide app settings and allow or block status of individual apps.
- Gradual rollout of apps, restricting access to specific apps for certain groups, and managing custom apps are common use cases for Teams App Permission Policies.

### Configuration
To manage app permission policies in Teams:
1. Navigate to the Microsoft Teams admin center.
2. Go to the "Teams apps" section.
3. Select "Permission policies".
4. Create or edit a policy as needed.

### Common Pitfalls
- Misconfiguring app permission policies can lead to unintended access or blockage of apps for users.
- It's essential to test and validate the impact of changes before applying them to the entire organization.

### KQL / PowerShell
The article does not provide specific queries or scripts related to KQL (Knowledge Query Language) or PowerShell.

### Related Topics
- [Teams app](https://learn.microsoft.com/en-us/microsoftteams/)
- [App permission](https://learn.microsoft.com/en-us/microsoftteams/app-permission-policies)
- [Third-party app](https://learn.microsoft.com/en-us/microsoftteams/third-party-apps)
- [Block app](https://learn.microsoft.com/en-us/microsoftteams/block-apps)
- [App policy](https://learn.microsoft.com/en-us/microsoftteams/app-policies)