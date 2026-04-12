---
conflicts:
- '[CONFLICT: Anoop C Nair suggests that "Require Bitlocker" uses the Windows Health
  Attestation Service for evaluation and does not require a reboot, while "Require
  encryption of data storage on device" does not require a reboot to evaluate but
  may block users from accessing corporate resources until the drive is fully encrypted.]'
- '[CONFLICT: Anoop C Nair suggests that "Require Bitlocker" uses the Windows Health
  Attestation Service for evaluation and does not require a reboot, while "Require
  encryption of data storage on device" does not require a reboot but may block users
  from accessing corporate resources until the drive is fully encrypted.]'
- '[CONFLICT: Anoop C Nair suggests that "Require Bitlocker" uses the Windows Health
  Attestation Service for evaluation and does not require a reboot, while "Require
  encryption of data storage on device" does not require a reboot but may block users
  from accessing corporate resources until the drive is fully encrypted. Jeffrey''s
  article mentions that Microsoft Defender ATP for Android also includes Bitlocker
  protection.]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2024-04-30'
  title: Automate Microsoft Intune Device Compliance Report Using Graph API HTMD Blog
  url: https://www.anoopcnair.com/automate-intune-device-compliance-report-graph
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2021-11-15'
  title: Managing Windows Bitlocker Compliance Policy Using Intune | MS Graph | Grace
    Period HTMD Blog
  url: https://www.anoopcnair.com/bitlocker-compliance-policy-using-intune
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-04-08'
  title: Create Custom Dashboards Alerts And 30-Day Compliance Trends Using MS Intune
    And Azure Log Analytics HTMD Blog
  url: https://www.anoopcnair.com/compliance-ms-intune-and-azure-log-analytics
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-06-25'
  title: 'Microsoft Defender ATP voor Android: Zo werkt de configuratie en gebruikerservaring
    tijdens de public preview'
  url: https://jeffreyappel.nl/microsoft-defender-atp-voor-android-zo-werkt-de-configuratie-en-gebruikerservaring-tijdens-de-public-preview
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2026-04-09'
  title: Unified Windows 365 Monitoring And Reporting Experience In Microsoft Intune
    HTMD Blog
  url: https://www.anoopcnair.com/microsoft-new-windows-365-monitoring-platform
stale_after: '2026-06-11'
title: Compliance Policy Design and CA Integration
topic: intune/compliance/compliance-policy-design
---

# Compliance Policy Design and CA Integration

## Compliance Policy Design and CA Integration

### Overview
This topic discusses automating the generation of Microsoft Intune Device Compliance reports using Graph API and PowerShell, as well as managing Windows Bitlocker compliance policy using Intune and MS Graph. The processes are crucial for organizations to monitor device compliance, identify areas requiring attention, and take corrective action as necessary.

### Key Concepts
- **Intune Device Compliance Report**: A report that provides an overview of compliance settings in policies, lists non-compliant devices, analyzes trends, and reviews individual device noncompliant settings.
- **Microsoft Graph API**: An API that allows access to data, intelligence, and insights from Microsoft 365 and other Microsoft Cloud services through a single endpoint.
- **PowerShell**: A scripting language developed for system administration tasks.
- **Bitlocker Compliance Policy Settings in Intune**: Two different mechanisms for evaluating Bitlocker encryption as part of an Intune compliance policy: "Require Bitlocker" and "Require encryption of data storage on device". [CONFLICT: Anoop C Nair suggests that "Require Bitlocker" uses the Windows Health Attestation Service for evaluation and does not require a reboot, while "Require encryption of data storage on device" does not require a reboot but may block users from accessing corporate resources until the drive is fully encrypted. Jeffrey's article mentions that Microsoft Defender ATP for Android also includes Bitlocker protection.]
- **Azure Log Analytics**: A service that collects and analyzes machine data from various sources for better insights. [New]
- **Microsoft Defender ATP for Android**: A security solution for mobile devices, currently in public preview, offering features such as web protection, malware scanning, and blocking access to sensitive data based on device risk. [New source: Microsoft Defender ATP voor Android: Zo werkt de configuratie en gebruikerservaring tijdens de public preview]
- **Unified Windows 365 Monitoring And Reporting Experience In Microsoft Intune HTMD Blog**: A new monitoring and reporting platform for Windows 365, built directly into the Microsoft Intune admin center. This platform brings together Cloud PC health, performance, and configuration data into a single dashboard, making it easier for administrators to monitor everything in one place. [New source]

### Configuration
1. Install the required modules: `Install-Module -Name AzureAD` and `Install-Module -Name MSOnline`.
2. Connect to your Azure AD: `Connect-AzureAD`.
3. Get the Intune device compliance report: `Get-MgDeviceComplianceReport`. Customize the report by applying filters and clicking on the **Generate Report** button. [No change]
4. To manage Windows Bitlocker compliance policy using Intune, you can use either "Require Bitlocker" or "Require encryption of data storage on device". [CONFLICT: Anoop C Nair suggests that "Require Bitlocker" uses the Windows Health Attestation Service for evaluation and does not require a reboot, while "Require encryption of data storage on device" does not require a reboot but may block users from accessing corporate resources until the drive is fully encrypted.]
5. To create custom dashboards, alerts, and 30-day compliance trends using MS Intune and Azure Log Analytics
6. [Unified Windows 365 Monitoring and Reporting Experience in Microsoft Intune](https://www.anoopcnair.com/unified-windows-365-monitoring-and-reporting-experience-in-microsoft-intune/) for a centralized monitoring experience, faster issue detection, no need for manual data exports, and better visibility into system performance and configuration. [New source]

New source article: "Unified Windows 365 Monitoring And Reporting Experience In Microsoft Intune HTMD Blog"
Author: Anoop C Nair
New source content:
# Unified Windows 365 Monitoring And Reporting Experience In Microsoft Intune HTMD Blog

Unified Windows 365 Monitoring And Reporting Experience In Microsoft Intune HTMD Blog

## **Key Takeaways**

- Simple and centralized **monitoring experience**
- Faster **issue detection** and troubleshooting
- No need for manual **data exports**
- Better visibility into system **performance** and configuration

In this post, we are discussing Microsoft Introduces New **Windows 365** Monitoring Platform in Public Preview. Microsoft introduced a new **monitoring** and reporting **platform** for Windows 365, which is now available in public preview. This new feature is built directly into the **[Microsoft Intune](https://www.anoopcnair.com/microsoft-intune-stateful-ftp-filtering-setting/) admin center,** making it easier for organizations to monitor their **Cloud PCs** in one place.

Table of Contents

## Table of Contents

## **Unified Windows 365 Monitoring and Reporting Experience in Microsoft Intune**

Now, everything is available in a single dashboard, making the process quicker and easier. Microsoft introduced this update with a focus on improving **usability** and making monitoring more user-friendly. With simple dashboards and **ready made reports**, even support teams with less experience can easily identify issues and take action faster.

- **[Create Custom Dashboards Alerts and 30-Day Compliance Trends using MS Intune and Azure Log Analytics](https://www.anoopcnair.com/compliance-ms-intune-and-azure-log-analytics/)**
- [**Intune Device Compliance Reports | Endpoint Manager**](https://howtomanagedevices.com/intune/5176/intune-device-compliance-reports-endpoint-manager/)
- [**Easiest Method to Enable MFA for Admins using Azure AD Conditional Access**](https://www.anoopcnair.com/enable-mfa-for-admins-aad-conditional-access/)
- [**Managing Windows Bitlocker Compliance Policy Using Intune | MS Graph | Grace Period**](https://www.anoopcnair.com/bitlocker-compliance-policy-using-intune/)