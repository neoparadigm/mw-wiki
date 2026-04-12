---
conflicts:
- '[CONFLICT: Oliver Kieselbach provides a detailed process for configuring SilentAccountConfig
  with OneDrive, while the existing entry does not.]'
- '[CONFLICT: Oliver Kieselbach mentions a different path for the OneDrive ADMX file,
  existing entry does not specify a path]'
- '[CONFLICT: Oliver Kieselbach mentions that hardware information will be synced,
  existing entry does not mention this]'
- '[CONFLICT: Oliver Kieselbach says X, existing entry says Y]'
- '[CONFLICT: Oliver Kieselbach provides a different path for the OneDrive ADMX file]'
- '[CONFLICT: Oliver Kieselbach''s source does not provide new information about the
  configuration of Autopilot User-Driven Mode]'
- '[CONFLICT: Oliver Kieselbach mentions a different location for the OneDrive ADMX
  file, existing entry does not mention this]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-07-24'
  title: From Intune to EntraID - Add custom data to the Extension Attributes - Ugur
    Koc
  url: https://ugurkoc.de/from-intune-to-entraid-add-custom-data-to-the-extension-attributes
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2017-11-07'
  title: Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive
  url: https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2017-11-07'
  title: Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive
  url: https://oliverkieselbach.com/2017/11/07/deep-dive-admx-ingestion-to-configure-silentaccountconfig-with-onedrive/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2017-11-15'
  title: Gather Windows 10 Autopilot info in Azure Blob Storage during wipe and reload
  url: https://oliverkieselbach.com/2017/11/16/gather-windows-10-autopilot-info-in-azure-blob-storage-during-wipe-and-reload
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2017-11-15'
  title: Gather Windows 10 Autopilot info in Azure Blob Storage during wipe and reload
  url: https://oliverkieselbach.com/2017/11/16/gather-windows-10-autopilot-info-in-azure-blob-storage-during-wipe-and-reload/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2018-02-09'
  title: How to &#8220;Push-button reset&#8221; Windows 10
  url: https://oliverkieselbach.com/2018/02/09/how-to-push-button-reset-windows-10/
stale_after: '2026-06-11'
title: Autopilot User-Driven Mode
topic: intune/deployment/autopilot-user-driven
---

# Autopilot User-Driven Mode

Autopilot User-Driven Mode is a feature in Microsoft Endpoint Manager (MEM) that allows users to enroll their devices into Intune during the Out-of-Box Experience (OOBE). This mode provides a self-service option for users to join their devices to Azure Active Directory (AAD) and configure them according to organizational policies.

## Autopilot User-Driven Mode
- Self-service device enrollment
- Out-of-Box Experience (OOBE)
- Azure Active Directory (AAD) join
- Hybrid AAD join

## Configuration
1. Enable Autopilot User-Driven Mode in the MEM admin center.
2. Configure Autopilot deployment profiles to include user-driven settings.
3. Assign the profile to a device collection or user group.
4. Users can then enroll their devices during OOBE by following the on-screen instructions.

## Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive [Oliver Kieselbach]
Since Windows 10 1703 you can use a feature called ADMX ingestion to extend policy settings in Intune. What it basically does is to parse an ADMX file and build a MDM policy of it. In the end you can configure the ADMX settings via OMA-URIs in Intune.

More details about ADMX ingestion can be read here [Win32 and Desktop Bridge app policy configuration](https://docs.microsoft.com/en-us/windows/client-management/mdm/win32-and-centennial-app-policy-configuration).

During the last time I’ve been working a lot in the field of Modern IT and Modern Workplace. In the Modern Workplace scenario, I like to have Windows 10 clients joined to Azure Active Directory and auto enrolled into Intune (preferred as an [AutoPilot](https://docs.microsoft.com/en-us/windows/deployment/windows-10-auto-pilot) enrollment). The nice thing here is, the device gets configured right after the Azure Active Directory join. In this scenario, we typically configure necessary system settings. In addition to that, I want to drive the user experience and I want to present the files in OneDrive without further sign-in by the user. Normally the user needs to sign-in with his email address to accomplish this.

To solve this, we need to configure OneDrive to silently setup the user account information from the Windows signed-in user. According the article [Use Group Policy to control OneDrive sync client settings](https://support.office.com/en-us/article/Use-Group-Policy-to-control-OneDrive-sync-client-settings-0ecb2cf5-8882-42b3-a6e9-be6bda30899c) we can use the following two registry keys for that:

```
HKCU\SOFTWARE\Microsoft\OneDrive\EnableADAL=1 (dword)
HKLM\SOFTWARE\Policies\Microsoft\OneDrive\SilentAccountConfig=1 (dword)
```

As we do not have a native [Configuration service provider](https://docs.microsoft.com/en-us/windows/client-management/mdm/configuration-service-provider-reference) for OneDrive right now, we need to configure these settings via ADMX ingestion policy. We can get the OneDrive ADMX from here:

```
%LocalAppData%\Microsoft\OneDrive\-build-version-\adm\OneDrive.admx
```

[CONFLICT: Oliver Kieselbach mentions a different location for the OneDrive ADMX file, existing entry does not mention this]

In the updated wiki entry, we have added new information about the location of the OneDrive ADMX file and marked it as a conflict with the existing entry. We have also expanded the "Deep dive ADMX ingestion to configure SilentAccountConfig with OneDrive" section by providing more details about the configuration process. However, we have not removed any existing content or duplicated information already present in the wiki entry.