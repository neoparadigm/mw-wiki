---
conflicts:
- '[CONFLICT: Oliver Kieselbach suggests using device certificates for Wi-Fi authentication]'
- '[CONFLICT: Oliver Kieselbach suggests using device certificates with SCEPman for
  device certificate deployment]'
- '[CONFLICT: existing entry mentions Intune but not SCEPman]'
- '[CONFLICT: Oliver Kieselbach suggests using device certificates with SCEPman for
  device certificate deployment; Jannik Reinhard does not mention this]'
- '[CONFLICT: existing entry mentions Intune but not SCEPman, and Jannik Reinhard
  does not explicitly state that it is an alternative solution]'
- '[CONFLICT: This is a new topic not directly related to app registration governance]'
- '[CONFLICT: existing entry does not mention SCEPman, and Jannik Reinhard does not
  explicitly state that it is an alternative solution]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-02-09'
  title: Microsoft 365 Data Exfiltration &#8211; Attack and Defend
  url: https://danielchronlund.com/2023/02/09/microsoft-365-data-exfiltration-attack-and-defend
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-12'
  date: '2019-07-02'
  title: The easy way to deploy device certificates with Intune
  url: https://oliverkieselbach.com/2019/07/02/the-easy-way-to-deploy-device-certificates-with-intune/comment-page-2
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-07-12'
  title: Detect anomalies in your Intune environment  with Azure Cognitive Services
    &#8211; Part 1 Device Compliance
  url: https://jannikreinhard.com/2022/07/12/detect-anomalies-in-your-intune-environment-with-azure-cognitive-services
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2022-07-21'
  title: Automatically create assignment groups when a app is created
  url: https://jannikreinhard.com/2022/07/21/automatically-create-assignment-groups-when-a-app-is-created
stale_after: '2026-06-11'
title: Service Principal and App Registration Governance
topic: identity/entra-id/service-principal-governance
---

# Service Principal and App Registration Governance

Service principal and app registration governance is crucial for securing Microsoft 365 tenants by managing access to sensitive data through properly configured Azure AD applications and Microsoft Graph permissions.

## Key Concepts
- Insecure app registrations with privileged API permissions assigned
- Possible privilege escalation paths
- Possible data exfiltration
- Risky API permissions such as Files.Read.All, Files.ReadWrite.All, Sites.Read.All, Sites.ReadWrite.All, GroupMember.Read.All, Group.Read.All, Directory.Read.All, Group.ReadWrite.All, and Directory.ReadWrite.All
- The use of client secrets instead of certificates for highly privileged app registrations [CONFLICT: Oliver Kieselbach suggests using device certificates with SCEPman for device certificate deployment; Jannik Reinhard does not mention this]
- Automatically creating assignment groups when a new app is created (new addition based on the new source article) [CONFLICT: This is a new topic not directly related to app registration governance]
- Device certificate deployment with Intune as an alternative solution for device certificate deployment (new addition based on the new source article) [CONFLICT: existing entry mentions Intune but not SCEPman, and Jannik Reinhard does not explicitly state that it is an alternative solution]

## Configuration
1. Review all app registrations in Azure AD to identify any with risky API permissions or insecure configurations.
2. Implement Multi-Factor Authentication (MFA) for all application administrators and service principals.
3. Use certificates instead of client secrets for highly privileged app registrations [CONFLICT: Oliver Kieselbach suggests using device certificates with SCEPman for device certificate deployment] or deploy device certificates with Intune as an alternative solution (new addition based on the new source article)
4. Deploy device certificates with Intune (new addition based on the new source article) [CONFLICT: existing entry does not mention SCEPman, and Jannik Reinhard does not explicitly state that it is an alternative solution]
5. Automatically create assignment groups when a new app is created (new addition based on the new source article)
6. Regularly audit and revoke unused or unnecessary app registrations.
7. Limit the number of Application Administrators in the tenant to only those who require access.

## Common Pitfalls
- Failing to regularly review and manage app registrations, leading to insecure configurations and potential data exfiltration.
- Granting too many permissions to an application, increasing the risk of privilege escalation and data exposure.
- Using client secrets instead of certificates for highly privileged app registrations [CONFLICT: Oliver Kieselbach suggests using device certificates with SCEPman for device certificate deployment] or failing to deploy device certificates for Wi-Fi authentication (new addition based on the new source article)
- Failing to implement automatic creation of assignment groups when a new app is created (new pitfall based on the new source article)