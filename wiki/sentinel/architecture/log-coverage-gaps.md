---
conflicts: []
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-07'
  title: Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive
  url: https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive
stale_after: '2026-05-29'
title: Sentinel Log Coverage and Ingestion Gaps
topic: sentinel/architecture/log-coverage-gaps
---

# Sentinel Log Coverage and Ingestion Gaps

## Overview
This topic discusses the configuration of SilentAccountConfig using ADMX ingestion for OneDrive in a Modern Workplace scenario, allowing Windows 10 clients joined to Azure Active Directory and auto enrolled into Intune to automatically configure necessary system settings and present files in OneDrive without further user sign-in.

## Key Concepts
- ADMX ingestion: a feature in Windows 10 1703 that extends policy settings in Intune by parsing an ADMX file and building a MDM policy from it.
- OMA-URIs: Open Mobile Alliance Unified Resource Identifiers used to configure the ADMX settings via Intune.
- SilentAccountConfig: a OneDrive setting that configures the user account information from the Windows signed-in user without requiring further sign-in by the user.
- EnableADAL: a registry key used in conjunction with SilentAccountConfig to enable Azure Active Directory Login for OneDrive.

## Configuration
1. Download the OneDrive ADMX file from `%LocalAppData%\Microsoft\OneDrive\-build-version-\adm\OneDrive.admx`.
2. Copy the complete policyDefinitions node to a new file and remove every policy node except the policy node with SilentAccountConfig.
3. Duplicate the policy node SilentAccountConfig as an additional node under the policies node, rename the attribute values "name" and "valueName" to EnableADAL.
4. Replace `SOFTWARE\Policies\Microsoft\OneDrive` with `SOFTWARE\Microsoft\OneDrive`.
5. Save the new XML file and import it as an ADMX ingestion policy in Intune.
6. Configure the necessary OMA-URI settings for EnableADAL (1) and SilentAccountConfig (0) in Intune.

## Common Pitfalls
- Using an outdated or incorrect version of the OneDrive ADMX file may result in errors or unexpected behavior.
- Failing to properly rename the attribute values "name" and "valueName" to EnableADAL can cause the policy to fail.
- Incorrectly specifying the registry path for SilentAccountConfig can also lead to issues with the configuration.

## KQL / PowerShell
This article does not provide any specific queries or scripts.

## Related Topics
- log coverage
- data connector
- ingestion
- diagnostic settings
- log gap