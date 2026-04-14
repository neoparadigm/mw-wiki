---
conflicts:
- '[CONFLICT: Michael Morten Sonne mentions an unspecified list of logged events from
  the new audit feature]'
- '[CONFLICT: Michael Morten Sonne mentions new detections and additional improvements
  and capabilities with Microsoft Defender for Identity]'
- '[CONFLICT: Michael Morten Sonne mentions advanced hunting with Microsoft Defender
  for Identity]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: omondiatieno
  crawled: '2026-04-14'
  date: '2025-04-09'
  title: What is Microsoft Entra Connect and Connect Health. - Microsoft Entra ID
  url: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-01-28'
  title: Entra ID – New build-in audit feature in Entra Connect is finally here! –
    Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-new-build-in-audit-feature-in-entra-connect-is-finally-here
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2024-08-28'
  title: Microsoft Defender for Identity – Expands support to servers with Microsoft
    Entra Connect – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/microsoft-defender-for-identity-expands-support-to-servers-with-microsoft-entra-connect
stale_after: '2026-06-13'
title: Entra Connect Server Hardening
topic: identity/hybrid/entra-connect-hardening
---

# Entra Connect Server Hardening

## Entra Connect Server Hardening

### Overview
Entra Connect Server Hardening is the process of securing and optimizing Microsoft Entra Connect servers to ensure they are resilient against potential threats and maintain a reliable connection to Microsoft 365 and other online services. This includes the new build-in audit feature introduced in the latest version (2.4.129.0) as per [Michael Morten Sonne](https://sonnes.cloud), and expanded support for servers with Entra Connect by Microsoft Defender for Identity ([Microsoft Defender for Identity – Expands support to servers with Microsoft Entra Connect – Blog - Sonne´s Cloud](https://blog.sonnes.cloud/microsoft-defender-for-identity-expands-support-to-servers-with-microsoft-entra-connect/)).

### Key Concepts
- Secure configuration of firewall rules, network settings, and service accounts
- Implementing best practices for patch management, antivirus, and access controls
- Enabling monitoring and logging for enhanced security and troubleshooting (includes the new audit feature and advanced hunting with Microsoft Defender for Identity) [CONFLICT: Michael Morten Sonne mentions new detections and additional improvements and capabilities with Microsoft Defender for Identity]
- Changing audit settings to enable/disable auditing of administrator events via PowerShell or manually (as per [Michael Morten Sonne](https://sonnes.cloud))

### Configuration
1. Configure firewall rules to allow only necessary traffic to and from the Entra Connect server.
2. Set up network segregation to isolate the Entra Connect server from other systems.
3. Use domain accounts with appropriate permissions for Entra Connect services.
4. Install and maintain antivirus software on the Entra Connect server.
5. Regularly apply security patches and updates to the operating system and applications.
6. Enable logging and monitoring for the Entra Connect server, such as Event Viewer or Azure Monitor (includes the new audit feature) [CONFLICT: Michael Morten Sonne mentions advanced hunting with Microsoft Defender for Identity]
7. Change audit settings to enable/disable auditing of administrator events via PowerShell or manually (as per [Michael Morten Sonne](https://sonnes.cloud))
8. Install the new sensor for Microsoft Defender for Identity on Entra Connect servers ([How to install the new sensor](#how-to-install-the-new-sensor) in the new source article)

### Common Pitfalls
- Neglecting to secure network connections between the Entra Connect server and other systems
- Using weak passwords or insecure service accounts
- Failing to regularly apply security patches and updates
- Ignoring logging and monitoring, which can help detect and respond to potential threats
- Not utilizing Microsoft Defender for Identity on Entra Connect servers ([Prerequisites](#prerequisites) in the new source article)

### KQL / PowerShell
This article does not provide specific queries or scripts for Entra Connect Server Hardening. However, it provides information on how to enable/disable the auditing of administrator events via PowerShell as per [Michael Morten Sonne](https://sonnes.cloud). Additionally, Microsoft Defender for Identity offers advanced hunting capabilities ([Advanced hunting](#advanced-hunting) in the new source article).

### Related Topics
- [Entra Connect](whatis-microsoft-entra-connect)
- [AAD Connect](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-aad-connect)
- [Sync Server](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/reference-connect-sync-server-components)
- [MSOL Account](https://learn.microsoft.com/en-us/powershell/module/msonline/?view=msonline-powershell)
- [Hybrid Identity](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-hybrid-identity)
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Microsoft](https://blog.sonnes.cloud/topics/microsoft/)
- [PowerShell](https://blog.sonnes.cloud/topics/general/software/powershell/)
- [Script](https://blog.sonnes.cloud)

## Microsoft Defender for Identity – Expands support to servers with Microsoft Entra Connect

[by Michael Morten Sonne](https://blog.sonnes.cloud/author/michael-morten-sonne/ "View all posts by Michael Morten Sonne")

August 28, 2024

9 minute read

### How to install the new sensor
1. Get the installer needed ([Get the installer needed](#get-the-installer-needed) in the new source article)
2. Install the Microsoft Defender for Identity sensor for Entra ID Connect ([Install the Microsoft Defender for Identity sensor for Entra ID Connect](#install-the-microsoft-defender-for-identity-sensor-for-entra-id-connect) in the new source article)
3. Get sensor versions and types ([Get sensor versions and types](#get-sensor-versions-and-types) in the new source article)

### Advanced hunting
Microsoft Defender for Identity offers advanced hunting capabilities to help security teams investigate and respond to potential threats more effectively. [Advanced hunting](#advanced-hunting) in the new source article provides more information on this topic.

### Conclusion
The expanded support of Microsoft Defender for Identity on servers with Entra Connect brings additional threat detection, improvements, and capabilities to help organizations strengthen their security posture and better protect against sophisticated cyberattacks targeting identity infrastructure.

### References
- [Microsoft Defender for Identity – Expands support to servers with Microsoft Entra Connect – Blog - Sonne´s Cloud](https://blog.sonnes.cloud/microsoft-defender-for-identity-expands-support-to-servers-with-microsoft-entra-connect/)