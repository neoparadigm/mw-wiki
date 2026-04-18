# MW-Wiki — Source Conflicts

Generated: 2026-04-18 17:17

Topics where indexed sources disagree. Review the topic file and the original sources before relying on this guidance.

## Azure App Proxy Configuration
Topic: `azure/app-proxy/app-proxy-configuration`

- [CONFLICT: Oliver Kieselbach does not mention this, but the existing entry includes it]
- [CONFLICT: The new source does not provide specific steps for configuring Conditional Access policies, but it is mentioned in the existing entry]
- [CONFLICT: Oliver Kieselbach does not mention this, but the existing entry includes it]
- [CONFLICT: The new source does not provide specific steps for configuring Conditional Access policies, but it is mentioned in the existing entry]

## Azure Monitor and Log Analytics Workspaces
Topic: `azure/monitoring/azure-monitor-log-analytics`

- [CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure Monitor Agent setup]
- [CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure Monitor Agent setup, but Bert-Jan Pals mentions no specific pitfalls in his article]
- [CONFLICT: Jannik Reinhard does not mention any common pitfalls related to Azure Monitor Agent setup, but Bert-Jan Pals mentions no specific pitfalls in his article]

## Global Secure Access and ZTNA
Topic: `azure/network/global-secure-access`

- [CONFLICT: Michael Morten Sonne mentions the ability to assign specific users and groups to traffic forwarding profiles, which is not explicitly mentioned in the existing entry]
- [CONFLICT: Michael Morten Sonne mentions the ability to assign specific users and groups to traffic forwarding profiles, which is not explicitly mentioned in the existing entry]

## MDE Tamper Protection
Topic: `defender/mde/tamper-protection`

- [CONFLICT: Jeffrey states that the troubleshooting mode allows disabling tamper protection and changing Defender Antivirus settings locally for testing, while the existing entry does not mention this specific functionality.]
- [CONFLICT: Jeffrey states that the troubleshooting mode allows disabling tamper protection and changing Defender Antivirus settings locally for testing, while the existing entry does not mention this specific functionality.]

## Defender Vulnerability Management
Topic: `defender/mde/vulnerability-management`

- [CONFLICT: Jeffrey's blog post provides additional information on XSPM not present in the existing entry]
- [CONFLICT: Jeffrey's blog post provides additional insights into MDVM usage]
- [CONFLICT: Jeffrey's blog post provides additional insights into MDVM usage; New source highlights the integration with XSPM]
- [CONFLICT: Jeffrey's blog post provides additional insights into MDVM usage; New source highlights the integration with XSPM]

## AiTM Proxy Attacks and Defence
Topic: `identity/conditional-access/aitm-defence`

- [CONFLICT: Jeffrey says Automatic Attack Disruption, existing entry does not mention it]
- [CONFLICT: Jeffrey says this is a recent development, existing entry does not mention it]
- [CONFLICT: Jeffrey says this is a recent development, existing entry does not mention it]

## Conditional Access — Authentication Flows
Topic: `identity/conditional-access/authentication-flows`

- [CONFLICT: Daniel Chronlund says Conditions and Access Controls are distinct, existing entry does not make this distinction]
- [CONFLICT: Daniel Chronlund says X, existing entry does not make this distinction]
- [CONFLICT: Daniel Chronlund says Conditions and Access Controls are distinct, existing entry does not make this distinction]

## Blocking Device Code Flow
Topic: `identity/conditional-access/device-code-flow-blocking`

- [CONFLICT: Existing entry does not mention the specific timeline of the phishing campaign.]
- [CONFLICT: Existing entry does not mention the increased exposure or active attacks due to control implementation.]
- [CONFLICT: Jan Bakker suggests that device code phishing is effective against phishing-resistant MFA like passkeys, while the existing entry does not mention this.]
- [CONFLICT: Jan Bakker suggests a two-step approach for blocking device code flow: creating policies to block it for all users except an exclusion group and trusted locations.]
- [CONFLICT: Jan Bakker suggests that device code phishing is effective against phishing-resistant MFA like passkeys, while the existing entry does not mention this.]
- [CONFLICT: Jan Bakker suggests a two-step approach for blocking device code flow: creating policies to block it for all users except an exclusion group and trusted locations.]

## Blocking Legacy Authentication Protocols
Topic: `identity/conditional-access/legacy-auth-blocking`

- [CONFLICT: Jeffrey mentions POP3/IMAP, but they are not explicitly mentioned in the existing entry]
- [CONFLICT: Jeffrey mentions POP3/IMAP, but they are not explicitly mentioned in the existing entry]

## Admin Consent Workflow and OAuth App Control
Topic: `identity/entra-id/admin-consent-workflow`

- [CONFLICT: Jeffrey mentions consent phishing attacks specifically]
- [CONFLICT: Jeffrey mentions the need for regular audits and reviews]
- [CONFLICT: Jeffrey says X, existing entry says Y]
- [CONFLICT: Jeffrey mentions consent phishing attacks specifically]
- [CONFLICT: Jeffrey mentions the need for regular audits and reviews]
- [CONFLICT: Jeffrey mentions the need for regular audits and reviews]
- [CONFLICT: Jeffrey says X, existing entry says Y]

## Entra ID Protection Risk Policies
Topic: `identity/entra-id/entra-id-protection`

- [CONFLICT: Michael Morten Sonne does not mention Azure AD Identity Protection]
- [CONFLICT: Michael Morten Sonne's new source does not discuss configuration]
- [CONFLICT: Jeffrey states that Sign-In Risk Policy requires a separate policy]
- [CONFLICT: Michael Morten Sonne does not mention Azure AD Identity Protection]
- [CONFLICT: Jeffrey states that Sign-In Risk Policy requires a separate policy]

## External Identities and B2B Collaboration
Topic: `identity/entra-id/external-identities`

- [CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue, while the existing entry does not mention it.]
- [CONFLICT: Michael Morten Sonne says X, existing entry says Y]
- [CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue, while the existing entry does not mention it. Michael Morten Sonne's blog post confirms this feature.]
- [CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue, while the existing entry does not mention it. Michael Morten Sonne's blog post confirms this feature.]
- [CONFLICT: Jeffrey suggests automatic Access Reviews as a solution to this issue, while the existing entry does not mention it.]

## Microsoft Graph API Permissions and Governance
Topic: `identity/entra-id/graph-api-permissions`

- [CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges]
- [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools]
- [CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent API coverage, and support for app-only access]
- [CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges, Jeffrey adds Conditional Access as a tool]
- [CONFLICT: Jeffrey does not mention this specifically]
- [CONFLICT: Jeffrey adds the ability to export Conditional Access configurations]
- [CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges, Jeffrey adds Conditional Access as a tool; CONFLICT: Jan Bakker emphasizes the importance of Graph API in Microsoft 365]
- [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; CONFLICT: Jan Bakker does not specifically mention data exfiltration or privilege escalation risks]
- [CONFLICT: Jeffrey adds the ability to export Conditional Access configurations; Jan Bakker demonstrates how to use browser developer tools and Postman to interact with the Graph API]
- [CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent API coverage, and support for app-only access; Jan Bakker does not specifically mention these points]
- [CONFLICT: This point is shared by all sources]
- [CONFLICT: Michael Morten Sonne mentions the need for regular reviews; Jan Bakker emphasizes the importance of regularly reviewing API calls from the Entra admin center or Microsoft Admin portal]
- [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; Jan Bakker does not specifically mention this]
- [CONFLICT: Michael Morten Sonne mentions coverage gaps and permission challenges, Jeffrey adds Conditional Access as a tool; CONFLICT: Jan Bakker emphasizes the importance of Graph API in Microsoft 365]
- [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; CONFLICT: Jan Bakker does not specifically mention data exfiltration or privilege escalation risks]
- [CONFLICT: Jeffrey does not mention this specifically]
- [CONFLICT: Jeffrey adds the ability to export Conditional Access configurations; Jan Bakker demonstrates how to use browser developer tools and Postman to interact with the Graph API]
- [CONFLICT: Michael Morten Sonne mentions the need for clear roadmap, consistent API coverage, and support for app-only access; Jan Bakker does not specifically mention these points]
- [CONFLICT: This point is shared by all sources]
- [CONFLICT: Michael Morten Sonne mentions the need for regular reviews; Jan Bakker emphasizes the importance of regularly reviewing API calls from the Entra admin center or Microsoft Admin portal]
- [CONFLICT: This point is shared by all sources]
- [CONFLICT: Michael Morten Sonne mentions inconsistencies across tools; Jan Bakker does not specifically mention this]

## Passwordless Authentication Methods
Topic: `identity/entra-id/passwordless-authentication`

- [CONFLICT: Simon Skotheimsvik mentions no pitfalls specific to Offpad, existing entry includes general pitfalls]
- [CONFLICT: Jeffrey does not mention any pitfalls specific to Temporary Access Pass, existing entry includes general pitfalls]
- [CONFLICT: Jeffrey says X, existing entry says Y]
- [CONFLICT: Jan Bakker says that guest users who access your (resource) tenant with MFA enforced are unable to register a passkey, despite having it enabled or registered in their home tenant. This is not mentioned in the existing entry.]
- [CONFLICT: Jan Bakker says that guest users who access your (resource) tenant with MFA enforced are unable to register a passkey, despite having it enabled or registered in their home tenant. This is not mentioned in the existing entry.]

## Service Principal and App Registration Governance
Topic: `identity/entra-id/service-principal-governance`

- [CONFLICT: Michael Morten Sonne does not provide a definition for Service Principal]
- [CONFLICT: Michael Morten Sonne does not mention Client Secret]
- [CONFLICT: Michael Morten Sonne does not provide specific instructions for registering an app]
- [CONFLICT: Michael Morten Sonne does not provide specific instructions for configuring permissions]
- [CONFLICT: Michael Morten Sonne does not mention setting up a client secret]
- [CONFLICT: Michael Morten Sonne does not mention any specific pitfalls]
- [CONFLICT: Michael Morten Sonne does not provide a definition for Service Principal]
- [CONFLICT: Michael Morten Sonne does not mention Client Secret]
- [CONFLICT: Michael Morten Sonne does not provide specific instructions for registering an app]
- [CONFLICT: Michael Morten Sonne does not provide specific instructions for configuring permissions]
- [CONFLICT: Michael Morten Sonne does not mention setting up a client secret]
- [CONFLICT: Michael Morten Sonne does not mention any specific pitfalls]

## Entra Connect Server Hardening
Topic: `identity/hybrid/entra-connect-hardening`

- [CONFLICT: Michael Morten Sonne's new source provides additional details on Microsoft Defender for Identity expanding support to servers with Microsoft Entra Connect and new posture recommendations focusing on Active Directory, but the existing entry does not include this information.]
- [CONFLICT: Michael Morten Sonne says X, existing entry says Y]
- [CONFLICT: Michael Morten Sonne says X, existing entry says Y]

## Break Glass Emergency Access Accounts
Topic: `identity/pim/break-glass-accounts`

- [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
- [CONFLICT: The existing entry does not configure MFA for Break Glass accounts]
- [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
- [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
- [CONFLICT: The existing entry does not configure MFA for Break Glass accounts]
- [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]
- [CONFLICT: The existing entry does not configure MFA for Break Glass accounts]
- [CONFLICT: Daniel Chronlund suggests that MFA should be implemented, but it is not configured for Break Glass accounts according to the existing entry]

## Microsoft Store App Deployment
Topic: `intune/apps/microsoft-store-apps`

- [CONFLICT: Anoop C Nair says this method aligns well with Windows Autopilot and Speech Packs for language management, existing entry does not mention this.]
- [CONFLICT: Anoop C Nair's blog post provides a detailed guide on deploying Natural Voice Packs to Windows 11 using Intune. The existing entry does not include this information.]
- [CONFLICT: Anoop C Nair's blog post provides a detailed guide on deploying Natural Voice Packs to Windows 11 using Intune. The existing entry does not include this information.]

## PowerShell Scripts in Intune
Topic: `intune/apps/powershell-scripts`

- [CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method is not mentioned in the existing entry.]
- [CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method is not mentioned in the existing entry.]
- [CONFLICT: Oliver Kieselbach mentions a method for deploying the agent using MSI packages via OMA-DM channel and EnterpriseDesktopAppManagement CSP, but this method is not mentioned in the existing entry.]

## Win32 App Deployment and Packaging
Topic: `intune/apps/win32-app-deployment`

- [CONFLICT: Oliver Kieselbach mentions .intunewin files but does not provide specific details on common pitfalls related to them]
- [CONFLICT: Oliver Kieselbach says X, existing entry says Y]
- [CONFLICT: Oliver Kieselbach mentions .intunewin files but does not provide specific details on common pitfalls related to them]

## WinGet and Microsoft Store Integration
Topic: `intune/apps/winget-intune`

- [CONFLICT: Oliver Kieselbach provides an example of a specific application being available via winget, while the existing entry does not mention this method.]
- [CONFLICT: Oliver Kieselbach provides specific instructions for SyncML Viewer installation and usage via winget, while the existing entry does not mention this method.]
- [CONFLICT: Anoop C Nair provides more detailed information about the integration between Microsoft Intune and the Microsoft Store, while Oliver Kieselbach's example of SyncML Viewer installation and usage via winget is not mentioned in the new source.]
- [CONFLICT: Oliver Kieselbach provides an example of a specific application being available via winget, while the existing entry does not mention this method.]

## Compliance Policy Design and CA Integration
Topic: `intune/compliance/compliance-policy-design`

- [CONFLICT: Misstep: IT departments enrolling devices on behalf of users, introducing a hidden compliance risk. This contradicts the existing entry's common pitfall about requiring Bitlocker causing delays.]
- [CONFLICT: Misstep: IT departments enrolling devices on behalf of users, introducing a hidden compliance risk. This contradicts the existing entry's common pitfall about requiring Bitlocker causing delays.]

## Custom Compliance Policies and Scripts
Topic: `intune/compliance/custom-compliance`

- [CONFLICT: Oliver Kieselbach's method does not involve creating and filling AAD groups, but it provides a way to download all Proactive Remediation Scripts from Microsoft Intune.]
- [CONFLICT: Oliver Kieselbach's method does not involve creating and filling AAD groups, but it provides a way to download all Proactive Remediation Scripts from Microsoft Intune. Jannik Reinhard's method involves creating custom compliance policies for Windows devices.]
- [CONFLICT: Oliver Kieselbach's method does not involve creating and filling AAD groups, but it provides a way to download all Proactive Remediation Scripts from Microsoft Intune. Jannik Reinhard's method involves creating custom compliance policies for Windows devices.]

## Delivery Optimization for Windows Updates
Topic: `intune/configuration/delivery-optimization`

- [CONFLICT: Oliver Kieselbach's source does not provide information about the MCC acting as a transparent proxy to cache content or the complete list of content supported by DO.]
- [CONFLICT: Oliver Kieselbach says X, existing entry says Y]
- [CONFLICT: Jannik Reinhard's article refers to DO as a cloud managed peer-to-peer technology, while the existing entry does not specify this.]
- [CONFLICT: Michael Niehaus' article mentions a standalone version of MCC, but the existing entry does not mention this.]
- [CONFLICT: Jannik Reinhard's article refers to DO as a cloud managed peer-to-peer technology, while the existing entry does not specify this.]
- [CONFLICT: Michael Niehaus' article mentions a standalone version of MCC, but the existing entry does not mention this.]

## Settings Catalog Configuration Profiles
Topic: `intune/configuration/settings-catalog`

- [CONFLICT: Oliver Kieselbach provides additional detail about the processing and refresh behavior, while the existing entry does not.]
- [CONFLICT: Oliver Kieselbach provides additional detail about the processing and refresh behavior, while the existing entry does not. However, Jannik Reinhard's article introduces a tool that generates meaningful descriptions using Azure OpenAI.]
- [CONFLICT: This content is not present in the existing entry.]
- [CONFLICT: This content is new and not present in the existing entry.]
- [CONFLICT: Oliver Kieselbach provides additional detail about the processing and refresh behavior, while the existing entry does not. However, Jannik Reinhard's article introduces a tool that generates meaningful descriptions using Azure OpenAI.]

## Autopilot User-Driven Mode
Topic: `intune/deployment/autopilot-user-driven`

- [CONFLICT: Oliver Kieselbach's article does not mention custom Azure Automation Runbook, which is still part of the existing entry.]
- [CONFLICT: Oliver Kieselbach's article automates this step manually]
- [CONFLICT: Oliver Kieselbach's article still mentions this step manually]
- [CONFLICT: Oliver Kieselbach's article introduces Autopilot Manager, while the existing entry does not.]
- [CONFLICT: The existing entry does not mention custom Azure Automation Runbook, which is still part of the existing entry.]
- [CONFLICT: Oliver Kieselbach's article automates this step using Autopilot Manager]
- [CONFLICT: Oliver Kieselbach's article introduces Autopilot Manager, while the existing entry does not.]
- [CONFLICT: The existing entry does not mention custom Azure Automation Runbook, which is still part of the existing entry.]
- [CONFLICT: Oliver Kieselbach's article automates this step using Autopilot Manager]

## Co-management with ConfigMgr and Intune
Topic: `intune/deployment/co-management`

- [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that devices can switch between being managed by ConfigMgr and Intune.]
- [CONFLICT: Anoop C Nair does not mention this term specifically, but the concept is implied in his discussion of moving to a fully cloud-native Intune setup.]
- [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that this can be done using workload policies.]
- [CONFLICT: Jeffrey suggests that co-management allows for migration from SCCM to Intune, while the existing entry does not mention this explicitly.]
- [CONFLICT: Jeffrey suggests that co-management allows for migration from SCCM to Intune, while the existing entry does not mention this explicitly.]
- [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that devices can switch between being managed by ConfigMgr and Intune.]
- [CONFLICT: Anoop C Nair does not mention this term specifically, but the concept is implied in his discussion of moving to a fully cloud-native Intune setup.]
- [CONFLICT: Anoop C Nair suggests that in the future, all workloads will be managed from the Intune cloud console, while the existing entry states that this can be done using workload policies.]

## Windows Autopatch Configuration
Topic: `intune/deployment/windows-autopatch`

- [CONFLICT: Simon Skotheimsvik says this is a common silent setting blocking communication with Windows update services, existing entry does not mention this]
- [CONFLICT: Simon Skotheimsvik mentions a specific issue called "Silent Windows Autopatch Killer" that may cause this]
- [CONFLICT: The existing entry mentions "Expedite polices" but does not provide further details. The new source explains that it refers to a feature allowing administrators to prioritize the installation of specific quality updates on devices.]
- [CONFLICT: Simon Skotheimsvik says this is a common silent setting blocking communication with Windows update services, existing entry does not mention this]
- [CONFLICT: Simon Skotheimsvik mentions a specific issue called "Silent Windows Autopatch Killer" that may cause this]
- [CONFLICT: The existing entry mentions "Expedite polices" but does not provide further details. The new source explains that it refers to a feature allowing administrators to prioritize the installation of specific quality updates on devices.]

## Intune Reporting with Log Analytics
Topic: `intune/reporting/intune-reporting-log-analytics`

- [CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention it]
- [CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention it]
- [CONFLICT: Anoop C Nair says this is a new feature, existing entry does not mention it]

## BitLocker Management via Intune
Topic: `intune/security/bitlocker-management`

- [CONFLICT: Oliver Kieselbach emphasizes this point more strongly]
- [CONFLICT: The existing entry does not provide this level of detail]
- [CONFLICT: The new source provides a detailed explanation of HSTI and its purpose for high assurance validation of proper security configuration]
- [CONFLICT: The new source provides more information on the Pre-Boot BitLocker startup PIN]
- [CONFLICT: The new source provides a detailed explanation of HSTI and its purpose for high assurance validation of proper security configuration]
- [CONFLICT: The new source provides more information on the Pre-Boot BitLocker startup PIN]

## Credential Guard and VBS
Topic: `intune/security/credential-guard`

- [CONFLICT: Anoop C Nair provides additional details on the OMA-URI values, but the existing entry does not conflict with this information.]
- [CONFLICT: Anoop C Nair provides additional details on the OMA-URI values, but the existing entry does not conflict with this information.]

## Microsoft Defender for Endpoint via Intune
Topic: `intune/security/defender-for-endpoint-intune`

- [CONFLICT: Anoop C Nair provides troubleshooting tips specific to Cloud PCs, not present in the existing entry.]
- [CONFLICT: Anoop C Nair provides additional information about updating security baselines]
- [CONFLICT: Anoop C Nair provides additional information about updating security baselines]

## Windows LAPS v2 Configuration
Topic: `intune/security/laps-v2`

- [CONFLICT: Simon Skotheimsvik provides alternative approaches for migration and configuration]
- [CONFLICT: Simon Skotheimsvik provides additional options for setting password policies]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might not require this step]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different configuration options]
- [CONFLICT: Michael Morten Sonne's article does not mention this step in the context of managing through Microsoft Intune]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different methods for setting password policies]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might not require this step]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different configuration options]
- [CONFLICT: Michael Morten Sonne's article does not mention this step in the context of managing through Microsoft Intune]
- [CONFLICT: Michael Morten Sonne discusses management through Microsoft Intune which might have different methods for setting password policies]

## WDAC and App Control for Business
Topic: `intune/security/wdac-app-control`

- [CONFLICT: Anoop C Nair does not mention WDAC in this article, but it is a key concept in the existing entry]
- [CONFLICT: Anoop C Nair does not provide specific configuration steps in this article]
- [CONFLICT: Anoop C Nair does not mention WDAC in this article, but it is a key concept in the existing entry]
- [CONFLICT: Anoop C Nair does not provide specific configuration steps in this article]
- [CONFLICT: Anoop C Nair does not mention WDAC in this article, but it is a key concept in the existing entry]
- [CONFLICT: Anoop C Nair does not provide specific configuration steps in this article]

## Windows Security Baseline in Intune
Topic: `intune/security/windows-security-baseline`

- [CONFLICT: Anoop C Nair does not mention Policy and Profile Manager, but it is a built-in role required for managing baselines in Intune.]
- [CONFLICT: Anoop C Nair mentions that older profiles become read-only but can be updated to the latest version for editing, while existing entry does not mention this.]
- [CONFLICT: Anoop C Nair does not mention deploying the created security baseline, but it is an essential step.]
- [CONFLICT: Anoop C Nair does not mention incorrect configuration of settings, but it is an important point to consider.]
- [CONFLICT: Anoop C Nair does not mention Policy and Profile Manager, but it is a built-in role required for managing baselines in Intune.]
- [CONFLICT: Anoop C Nair mentions that older profiles become read-only but can be updated to the latest version for editing, while existing entry does not mention this.]
- [CONFLICT: Anoop C Nair does not mention deploying the created security baseline, but it is an essential step.]
- [CONFLICT: Anoop C Nair does not mention incorrect configuration of settings, but it is an important point to consider.]

## KQL — Identity and Sign-in Detection
Topic: `sentinel/kql/identity-detection-queries`

- [CONFLICT: Bert-Jan Pals says the new content adds Zeek and Azure Resource Graph, existing entry does not mention these topics.]
- [CONFLICT: Bert-Jan Pals says the new content adds Zeek and Azure Resource Graph, existing entry does not mention these topics.]

## Windows Update for Business Policies
Topic: `windows/updates/windows-update-for-business`

- [CONFLICT: Oliver Kieselbach mentions the importance of Delivery Optimization in the context of WUfB, while the existing entry does not explicitly state this.]
- [CONFLICT: Oliver Kieselbach mentions the importance of Delivery Optimization in the context of WUfB, while the existing entry does not explicitly state this.]

