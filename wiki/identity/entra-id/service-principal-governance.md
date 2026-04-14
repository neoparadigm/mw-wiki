---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2022-07-21'
  title: Automatically create assignment groups when a app is created
  url: https://jannikreinhard.com/2022/07/21/automatically-create-assignment-groups-when-a-app-is-created
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2022-10-23'
  title: Intune DevOps Tools &#8211; Move objects from Dev to Prod Tenant
  url: https://jannikreinhard.com/2022/10/23/intune-devops-tools-move-objects-from-dev-to-prod-tenant
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2023-02-09'
  title: Microsoft 365 Data Exfiltration &#8211; Attack and Defend
  url: https://danielchronlund.com/2023/02/09/microsoft-365-data-exfiltration-attack-and-defend
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2023-02-19'
  title: Create Smart Groups for Wave Deployment of Configurations in Intune
  url: https://jannikreinhard.com/2023/02/19/create-smart-groups-for-wave-deployment-of-configurations-in-intune
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-08-18'
  title: 'Entra ID – Managed Identity Permission Manager: A Community-Driven Recap
    – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/entra-id-managed-identity-permission-manager-a-community-driven-recap
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-05-13'
  title: Entra ID – Managed Identity Permissions Manager – Performance Stats and Community
    Insights – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-managed-identity-permissions-manager-performance-stats-and-community-insights
stale_after: '2026-06-13'
title: Service Principal and App Registration Governance
topic: identity/entra-id/service-principal-governance
---

# Service Principal and App Registration Governance

## Overview
This topic discusses automating the creation of assignment groups when a new app is created in Microsoft Endpoint Manager (MEM). The process saves time by eliminating the need to manually create groups for available/required and uninstall assignments for each app. It also introduces methods for:
- Automating group creation using PowerShell scripts [(as outlined in the original entry)](#configuration)
- Moving objects from a Dev tenant to a Prod tenant using Intune DevOps Tools, which allows for better release management processes ([as outlined in the original entry](#configuration))
- Creating Smart Groups for Wave Deployment of Configurations in Intune [(new source by Jannik Reinhard)](#create-smart-groups)
- Managing Identity Permissions using a PowerShell tool, as outlined in the article "Entra ID – Managed Identity Permission Manager: A Community-Driven Recap" by Michael Morten Sonne ([new source](#managed-identity-permission-manager))
- [Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights – Blog - Sonne’s Cloud](#sonnes-cloud) (new source by Michael Morten Sonne)

## Key Concepts
- Azure Active Directory (AAD)
- App registration
- API permissions
- Microsoft Graph
- DeviceManagementApps.ReadWrite.All
- Group.Create
- Automation Account
- Runbook
- PowerShell script
- Variables
- Secret Value and App ID
- Certificates & secrets
- Schedules
- Intune DevOps Tools
- Service Principal
- Client secret
- Certificate auth
- SP governance
- Files.Read.All, Files.ReadWrite.All, Sites.Read.All, Sites.ReadWrite.All (Microsoft Graph permissions associated with data exfiltration risks)
- GroupMember.Read.All, Group.Read.All, Directory.Read.All, Group.ReadWrite.All, Directory.ReadWrite.All (Microsoft Graph permissions required for enumerating Microsoft 365 groups and SharePoint document libraries)
- Wave Deployment Groups (new source by Jannik Reinhard)
- Managed Identity (new source by Michael Morten Sonne)

## Configuration
1. Create a new app registration in AAD for both Dev and Prod tenants, following the steps outlined in the original entry.
2. Add API permissions for Microsoft Graph with DeviceManagementApps.ReadWrite.All and Group.Create for the Prod tenant, and DeviceManagementApps.Read.All and DeviceManagementConfiguration.Read.All for the Dev tenant.
3. Grant admin consent for the permissions.
4. Create a client secret for both tenants.
5. Create an Automation Account.
6. Create a runbook, insert the provided PowerShell script, enter the group prefix, save, test, publish, and link to a schedule in both Dev and Prod tenants. [(as outlined in the original entry)](#configuration)
7. For moving objects from Dev to Prod tenant, follow the steps outlined in the new source article: Intune DevOps Tools - Move objects from Dev to Prod Tenant.
8. To create Smart Groups for Wave Deployment of Configurations in Intune, follow the steps outlined in the new source content by Jannik Reinhard [(new source)](#create-smart-groups)
9. To manage Identity Permissions, use the PowerShell tool outlined in the article "Entra ID – Managed Identity Permission Manager: A Community-Driven Recap" by Michael Morten Sonne ([new source](#managed-identity-permission-manager))
10. [Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights – Blog - Sonne’s Cloud](#sonnes-cloud) (new source by Michael Morten Sonne)

## Key Concepts from the new source:
- Managed Identity Permission Manager
- PowerShell tool for managing permissions for Managed Identities in Azure/Entra ID

## CONFLICT: Michael Morten Sonne says "Entra ID – Managed Identity Permissions Manager" is a PowerShell tool, existing entry does not mention it as a tool.

## New source article: "Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights – Blog - Sonne’s Cloud"
Author: Michael Morten Sonne
New source content:
# Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights – Blog - Sonne’s Cloud

Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights – Blog - Sonne’s Cloud


- [Code Repository](https://blog.sonnes.cloud/topics/general/code-repository/)
- [Cool tools](https://blog.sonnes.cloud/topics/general/software/cool-tools/)
- [GitHub](https://blog.sonnes.cloud/topics/github/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [My tools](https://blog.sonnes.cloud/topics/my-tools/)
- [PowerShell](https://blog.sonnes.cloud/topics/general/software/powershell/)
- [Security](https://blog.sonnes.cloud/topics/security/)

# Entra ID – Managed Identity Permissions Manager – Performance Stats and Community Insights

[byMichael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

May 13, 2025

7 minute read





Last Updated on May 13, 2025 by [Michael Morten Sonne](https://sonnes.cloud)

##### Table of Contents

1. [Introduction](#introduction)
   1. [What is a Managed Identity?](#what-is-a-managed-identity)
      1. [Types of Managed Identities](#types-of-managed-identities)
      2. [Key benefits of Managed Identities](#key-benefits-of-managed-identities)
      3. [Common use cases](#common-use-cases)
   2. [Locate a Managed Identity](#locate-a-managed-identity)
   3. [What about API Permissions?](#what-about-api-permissions)
   4. [What is Microsoft Graph?](#what-is-microsoft-graph)
2. [So why this tool is needed?](#so-why-this-tool-is-needed)
   1. [How my PowerShell Tool fills the gaps](#how-my-powershell-tool-fills-the-gaps)
   2. [How this tool will help you](#how-this-tool-will-help-you)
3. [The tool itself](#the-tool-itself)
   1. [Changelog](#changelog)
   2. [Sample use of the tool](#sample-use-of-the-tool)
   3. [Prerequisites](#prerequisites)
4. [How to get the tool](#how-to-get-the-tool)
   1. [The trust on the tool in the community and customers at my work (and Microsoft)](#the-trust-on-the-tool-in-the-community-and-customers-at-my-work-and-microsoft)
5. [Conclusion](#conclusion)
6. [References](#references)

# Introduction

Here is a small update on my tool for managing permissions for **Managed Identities** in **Azure/Entra ID** in general – how it doing it and so – I created it as this has been a long-standing challenge. Microsoft has yet not provided a built-in interface for this, leaving administrators reliant on **PowerShell** to handle permissions – even if the “same” exists for **App Registrations** and **Enterprise Applications**.

To bridge this gap, I as many of you know developed this **PowerShell-based**tool some time ago to the **community**as a [Microsoft MVP](https://mvp.microsoft.com/en-US/mvp/profile/b6a5bd91-5ebd-4c84-8965-023a95273093?wt.mc_id=MVP_353010), and this tool simplifies and streamlines the management of