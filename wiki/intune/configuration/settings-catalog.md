---
conflict_topics:
- intune/configuration/delivery-optimization
- intune/deployment/autopilot-user-driven
conflicts:
- '[CONFLICT: Oliver Kieselbach provides additional detail about the processing and
  refresh behavior, while the existing entry does not.]'
- '[CONFLICT: Oliver Kieselbach provides additional detail about the processing and
  refresh behavior, while the existing entry does not. However, Jannik Reinhard''s
  article introduces a tool that generates meaningful descriptions using Azure OpenAI.]'
- '[CONFLICT: This content is not present in the existing entry.]'
- '[CONFLICT: This content is new and not present in the existing entry.]'
context_note: Settings Catalog is part of the intune domain. Synthesised from 6 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2019-07-18'
  title: Intune Policy Processing on Windows 10 explained
  url: https://oliverkieselbach.com/2019/07/18/intune-policy-processing-on-windows-10-explained
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2019-07-18'
  title: Intune Policy Processing on Windows 10 explained
  url: https://oliverkieselbach.com/2019/07/18/intune-policy-processing-on-windows-10-explained/
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2026-03-28'
  title: AI-Powered Intune Policy Descriptions &amp; Conflict Analysis
  url: https://jannikreinhard.com/2026/03/28/ai-powered-intune-policy-descriptions-conflict-analysis
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-02-07'
  title: How To Enable Add Provisioning Package Using Intune Settings Catalog Policy
    HTMD Blog
  url: https://www.anoopcnair.com/add-provisioning-package-using-intune-settings
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2026-02-25'
  title: Reducing Data Exposure Risks By Restricting Offline Files Settings Using
    Intune Policy HTMD Blog
  url: https://www.anoopcnair.com/data-risks-by-restricting-offline-files-intune
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-06-02'
  title: Allow Or Block Prevents Files From Being Uploaded While In Deprecated Application
    Guard Policy Using Intune HTMD Blog
  url: https://www.anoopcnair.com/deprecated-application-guard-policy-intune
stale_after: '2026-06-02'
title: Settings Catalog Configuration Profiles
topic: intune/configuration/settings-catalog
---

# Settings Catalog Configuration Profiles

## Settings Catalog Configuration Profiles

This topic discusses the architecture and processing of Intune Policy Processing on Windows 10, focusing on MDM managed devices and the use of device configuration profiles to manage endpoints. The article also provides an in-depth explanation of the process, including changes with Windows 10 version 1903.

## Key Concepts
- MDM (Mobile Device Management) system (Intune)
- MDM client on Windows 10 OS
- Open Mobile Alliance (OMA) Device Management (OMA-DM) protocol
- SyncML format for data transfer
- HTTPS as transport layer
- Configuration Service Providers (CSP’s)
- OMA-URI’s (Open Mobile Alliance – Uniform Resource Identifier)
- Policy CSP
- [Configuration Service Extensions (CSE's)](https://docs.microsoft.com/en-us/windows/client-management/mdm/configuration-service-provider-reference?WT.mc_id=EM-MVP-5003177)
- [AI-Powered Intune Policy Descriptions & Conflict Analysis](#ai-powered-intune-policy-descriptions--conflict-analysis) (new source content added)
- [How To Enable Add Provisioning Package Using Intune Settings Catalog Policy](#how-to-enable-add-provisioning-package-using-intune-settings-catalog-policy-htmd-blog) (new source content added)
- [Reducing Data Exposure Risks By Restricting Offline Files Settings Using Intune Policy HTMD Blog](#reducing-data-exposure-risks-by-restricting-offline-files-settings-using-intune-policy-htmd-blog) (new source content added)
- [Allow Or Block Prevents Files From Being Uploaded While In Deprecated Application Guard Policy Using Intune HTMD Blog](#allow-or-block-prevents-files-from-being-uploaded-while-in-deprecated-application-guard-policy-using-intune-htmd-blog) (new source content added)

## Configuration
The article explains the general process of how Intune and the MDM client work together to exchange data based on the OMA-DM protocol and XML format, as well as providing details about the refresh behavior. It also covers changes with Windows 10 version 1903. [CONFLICT: Oliver Kieselbach provides additional detail about the processing and refresh behavior, while the existing entry does not. However, Jannik Reinhard's article introduces a tool that generates meaningful descriptions using Azure OpenAI.]

## Common Pitfalls
No common pitfalls are mentioned in the article.

## KQL / PowerShell
The article does not include any relevant queries or scripts.

## Related Topics
- settings catalog
- configuration profile
- policy CSP
- settings catalog policy
- administrative template
- Configuration Service Extensions (CSE's)
- [AI-Powered Intune Policy Descriptions & Conflict Analysis](#ai-powered-intune-policy-descriptions--conflict-analysis)
- [How To Enable Add Provisioning Package Using Intune Settings Catalog Policy](#how-to-enable-add-provisioning-package-using-intune-settings-catalog-policy-htmd-blog)
- [Reducing Data Exposure Risks By Restricting Offline Files Settings Using Intune Policy HTMD Blog](#reducing-data-exposure-risks-by-restricting-offline-files-settings-using-intune-policy-htmd-blog)
- [Allow Or Block Prevents Files From Being Uploaded While In Deprecated Application Guard Policy Using Intune HTMD Blog](#allow-or-block-prevents-files-from-being-uploaded-while-in-deprecated-application-guard-policy-using-intune-htmd-blog)

## AI-Powered Intune Policy Descriptions & Conflict Analysis

Jannik Reinhard introduces a tool that fetches all your Intune policies via the Microsoft Graph API, generates meaningful descriptions using Azure OpenAI, and provides conflict analysis.

## How To Enable Add Provisioning Package Using Intune Settings Catalog Policy

This article explains how to enable adding provisioning packages using Intune Settings Catalog Policy. It includes steps for signing in to the Microsoft Intune admin center, creating a profile, selecting Windows 10 and later as the platform, setting the profile type to Settings Catalog, and configuring the policy accordingly.

## Reducing Data Exposure Risks By Restricting Offline Files Settings Using Intune Policy HTMD Blog

This article discusses how to reduce data exposure risks by restricting offline files settings using Intune Policy. It provides steps for creating a profile, selecting Windows 10 and later as the platform, setting the profile type to Settings Catalog, and configuring the policy accordingly.

## Allow Or Block Prevents Files From Being Uploaded While In Deprecated Application Guard Policy Using Intune HTMD Blog

This article explains how to allow or block files from being uploaded while in deprecated Application Guard Policy using Intune. It provides steps for creating a profile, selecting Windows 10 and later as the platform, setting the profile type to Settings Catalog, and configuring the policy accordingly to prevent file uploads when Edge is running in Application Guard mode.