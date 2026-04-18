---
conflicts: []
context_note: External Access Federation is part of the teams domain. Synthesised
  from 2 community sources.
domain: teams
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2021-02-22'
  title: Manage Teams External Access for Allowed Domains Using PowerShell and Teams
    Approvals
  url: https://danielchronlund.com/2021/02/22/manage-teams-external-access-for-allowed-domains-using-powershell-and-teams-approvals
- author: officedocspr5
  crawled: '2026-04-18'
  date: '2025-11-19'
  title: IT Admins - Manage external meetings and chat with people and organizations
    using Microsoft identities - Microsoft Teams
  url: https://learn.microsoft.com/en-us/microsoftteams/manage-external-access
stale_after: '2026-06-17'
title: Teams External Access and Federation Control
topic: teams/security/external-access-federation
---

# Teams External Access and Federation Control

## Overview
This topic discusses the automation of managing Teams external access for allowed domains using PowerShell and Teams Approvals. The approach is particularly useful in highly regulated industries where Microsoft 365 tenants are locked down, and Teams federation needs to be controlled due to security or compliance reasons.

The new source article provides additional information on managing external meetings and chat with people and organizations using Microsoft identities in Microsoft Teams.

## Key Concepts
- Teams External Access
- Federated Domains
- PowerShell Scripting
- Azure Automation
- Teams Approvals
- Microsoft Identities

## Configuration
1. Install the Microsoft Teams PowerShell module if not already installed: `Install-Module MicrosoftTeams`
2. Connect to Microsoft Teams using PowerShell: `New-CsOnlineSession | Import-PSSession`
3. Run the provided PowerShell script to enable federation for allowed domains only, and implement an approval flow using Teams Approvals.
4. Configure external access with other Microsoft 365 organizations (chat and meetings), Teams users not managed by an organization (those users with a [Microsoft account](https://account.microsoft.com)) (chat only), and Skype users (chat only). Users in your organization can accept or block incoming chats from people outside the organization.

## Common Pitfalls
- Enabling federation on a tenant level may not meet specific security or compliance requirements. It is recommended to block or allow specific domains instead.
- Manual configuration of Teams federation can be time-consuming and error-prone, making automation essential for scalability.

## KQL / PowerShell
```powershell
# Function to add allowed domain for Teams federation.
function Enable-TeamsFederationForAllowedDomainsOnly {
    param (
        [parameter(Mandatory = $true)]
        [string[]]$AllowedDomains,

        [parameter(Mandatory = $false)]
        [switch]$RemoveExistingDomains
    )

    # Remove existing domains (if requested).
    if ($RemoveExistingDomains) {
        Write-Verbose -Verbose -Message "Removing existing domains..."
        Set-CsTenantFederationConfiguration -AllowPublicUsers $false
    }

    # Add allowed domains for Teams federation.
    foreach ($domain in $AllowedDomains) {
        Write-Verbose -Verbose -Message "Adding domain: $domain"
        New-CsTenantFederationTrustedDomain -Name $domain -Verified $true
    }
}
```

## Related Topics
- [Teams external](wiki:teams_external)
- [federation](wiki:federation)
- [external user](wiki:external_user)
- [block domain](wiki:block_domain)
- [Teams phishing](wiki:teams_phishing)
- [Microsoft identities](#IT Admins - Manage external meetings and chat with people and organizations using Microsoft identities)

New source article: "IT Admins - Manage external meetings and chat with people and organizations using Microsoft identities - Microsoft Teams"
Author: officedocspr5
New source content added.