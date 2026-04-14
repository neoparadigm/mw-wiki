---
conflicts:
- '[CONFLICT: Oliver Kieselbach''s article provides more detailed information about
  ADMX ingestion.]'
- '[CONFLICT: Oliver Kieselbach''s article suggests that EnableADAL is not explicitly
  present in the ADMX file, but needs to be added as an additional node.]'
- '[CONFLICT: Oliver Kieselbach''s article suggests duplicating the SilentAccountConfig
  policy node as an additional node under the policies node, renaming the attribute
  values "name" and "valueName" to EnableADAL.]'
- '[CONFLICT: Oliver Kieselbach''s article does not provide specific instructions
  for configuring these settings.]'
- '[CONFLICT: Oliver Kieselbach''s article suggests that this step is necessary.]'
domain: sentinel
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-07'
  title: Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive
  url: https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2017-11-07'
  title: Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive
  url: https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive/
stale_after: '2026-05-29'
title: Sentinel Log Coverage and Ingestion Gaps
topic: sentinel/architecture/log-coverage-gaps
---

# Sentinel Log Coverage and Ingestion Gaps (Updated)

## Overview
This topic discusses the configuration of SilentAccountConfig using ADMX ingestion for OneDrive in a Modern Workplace scenario, allowing Windows 10 clients joined to Azure Active Directory and auto enrolled into Intune to automatically configure necessary system settings and present files in OneDrive without further user sign-in.

## Key Concepts
- ADMX ingestion: a feature in Windows 10 1703 that extends policy settings in Intune by parsing an ADMX file and building a MDM policy from it. [CONFLICT: Oliver Kieselbach's article provides more detailed information about ADMX ingestion.]
- OMA-URIs: Open Mobile Alliance Unified Resource Identifiers used to configure the ADMX settings via Intune.
- SilentAccountConfig: a OneDrive setting that configures the user account information from the Windows signed-in user without requiring further sign-in by the user.
- EnableADAL: a registry key used in conjunction with SilentAccountConfig to enable Azure Active Directory Login for OneDrive. [CONFLICT: Oliver Kieselbach's article suggests that EnableADAL is not explicitly present in the ADMX file, but needs to be added as an additional node.]

## Configuration
1. Download the OneDrive ADMX file from `%LocalAppData%\Microsoft\OneDrive\-build-version-\adm\OneDrive.admx`.
2. Copy the complete policyDefinitions node to a new file and remove every policy node except the policy node with SilentAccountConfig. [CONFLICT: Oliver Kieselbach's article suggests duplicating the SilentAccountConfig policy node as an additional node under the policies node, renaming the attribute values "name" and "valueName" to EnableADAL.]
3. Replace `SOFTWARE\Policies\Microsoft\OneDrive` with `SOFTWARE\Microsoft\OneDrive`.
4. Save the new XML file and import it as an ADMX ingestion policy in Intune.
5. Configure the necessary OMA-URI settings for EnableADAL (1) and SilentAccountConfig (0) in Intune. [CONFLICT: Oliver Kieselbach's article does not provide specific instructions for configuring these settings.]

## Common Pitfalls
- Using an outdated or incorrect version of the OneDrive ADMX file may result in errors or unexpected behavior.
- Failing to properly rename the attribute values "name" and "valueName" to EnableADAL can cause the policy to fail. [CONFLICT: Oliver Kieselbach's article suggests that this step is necessary.]
- Incorrectly specifying the registry path for SilentAccountConfig can also lead to issues with the configuration.

## KQL / PowerShell
This article does not provide any specific queries or scripts.

## Related Topics
- log coverage
- data connector
- ingestion
- diagnostic settings
- log gap

## New Source Article: "Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive"
### Author: Oliver Kieselbach
### New source content:
# Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive

Detailed information about ADMX ingestion can be found [here](https://docs.microsoft.com/en-us/windows/client-management/mdm/win32-and-centennial-app-policy-configuration).

In a Modern Workplace scenario, Windows 10 clients joined to Azure Active Directory and auto enrolled into Intune can be configured right after the Azure Active Directory join. To present files in OneDrive without further sign-in by the user, we need to configure OneDrive to silently setup the user account information from the Windows signed-in user.

The following registry keys are used for that:

```
HKCU\SOFTWARE\Microsoft\OneDrive\EnableADAL=1 (dword)
HKLM\SOFTWARE\Policies\Microsoft\OneDrive\SilentAccountConfig=1 (dword)
```

Since we do not have a native Configuration service provider for OneDrive, these settings need to be configured via ADMX ingestion policy. The OneDrive ADMX file can be found at:

```
%LocalAppData%\Microsoft\OneDrive\-build-version-\adm\OneDrive.admx
```

We copy the complete policyDefinitions node to a new file, remove every policy node except the policy node with SilentAccountConfig, and duplicate the SilentAccountConfig policy node as an additional node under the policies node, renaming the attribute values “name” and “valueName” to EnableADAL. The final XML file should look like this:

```
<policyDefinitions xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <policy name="Microsoft OneDrive - EnableADAL" valueName="EnableADAL" id="46">
    <data id="localPolicy">
      <value>1</value>
      <type>dword</type>
    </data>
    <data id="registryHive">HKCU\SOFTWARE\Microsoft\OneDrive</data>
    <data id="registryPath">EnableADAL</data>
  </policy>
  <policy name="Microsoft OneDrive - SilentAccountConfig" valueName="SilentAccountConfig" id="47">
    <data id="localPolicy">
      <value>1</value>
      <type>dword</type>
    </data>
    <data id="registryHive">HKLM\SOFTWARE\Policies\Microsoft\OneDrive</data>
    <data id="registryPath">SilentAccountConfig</data>
  </policy>
</policyDefinitions>
```

Save the new XML file and import it as an ADMX ingestion policy in Intune. Then configure the necessary OMA-URI settings for EnableADAL (1) and SilentAccountConfig (0) in Intune.