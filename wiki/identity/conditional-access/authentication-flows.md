---
conflicts:
- '[CONFLICT: kenwith says "authentication transfer", existing entry does not mention
  this]'
- '[CONFLICT: Jan Bakker does not mention this]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2018-11-21'
  title: Azure AD Conditional Access Policy Design Baseline
  url: https://danielchronlund.com/2018/11/21/azure-ad-conditional-access-policy-design-baseline
- author: kenwith
  crawled: '2026-04-12'
  date: '2026-04-07'
  title: Block authentication flows with Conditional Access policy - Microsoft Entra
    ID
  url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows
- author: Jan Bakker
  crawled: '2026-04-12'
  date: '2025-05-06'
  title: How to restrict Device Code Flow in Entra ID
  url: https://janbakker.tech/how-to-restrict-device-code-flow-in-entra-id/
- author: Jannik Reinhard
  crawled: '2026-04-12'
  date: '2026-02-22'
  title: Why CLI Tools Are Beating MCP for AI Agents
  url: https://jannikreinhard.com/2026/02/22/why-cli-tools-are-beating-mcp-for-ai-agents
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-03-03'
  title: Configure automatic Attack Disruption in Microsoft Defender XDR
  url: https://jeffreyappel.nl/configure-automatic-attack-disruption-in-microsoft-defender-xdr
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-07-07'
  title: What is Microsoft Defender for Endpoint (MDE)?
  url: https://jeffreyappel.nl/microsoft-defender-for-endpoint-series-what-is-defender-for-endpoint-part1
stale_after: '2026-06-11'
title: Conditional Access — Authentication Flows
topic: identity/conditional-access/authentication-flows
---

# Conditional Access — Authentication Flows

## Conditional Access — Authentication Flows

### Overview
This topic discusses the various authentication flows available in Azure AD Conditional Access (CA), and how they can be used to secure access to resources based on specific conditions. Understanding these authentication flows is crucial for implementing effective CA policies.

### Key Concepts
- **Multi-Factor Authentication (MFA):** A security measure that requires users to provide two or more verification factors to authenticate.
- **Passwordless Authentication:** A method of authentication that does not require a password, such as using a mobile app or hardware token.
- **Work Accounts:** User accounts that are managed by Azure AD and used for accessing cloud applications.
- **Personal Accounts:** User accounts that are not managed by Azure AD, such as Microsoft accounts (e.g., Outlook.com).
- **Azure AD Join:** The process of joining a device to Azure AD, which allows the device to be managed and secured by CA policies.
- **Hybrid Azure AD Join:** The process of joining a device to both the on-premises Active Directory (AD) and Azure AD, allowing the device to be managed by both CA policies and Group Policy Objects (GPOs).
- **Authentication Transfer:** A method of authentication where a user can authenticate using another user's session. [CONFLICT: Jan Bakker does not mention this]
- **Device Code Flow:** A method of authentication that allows users to authenticate via a device code, often used for devices without interfaces or for Teams Room devices.
- **CLI Tools:** Command Line Interface tools used by AI agents for efficient context management. [New Concept: Added from "Why CLI Tools Are Beating MCP for AI Agents"]
- **Automatic Attack Disruption:** A response capability in Microsoft Defender XDR that protects the environment against sophisticated, high-impact attacks by containing assets used by attackers (Source: Jeffrey) [New Concept from "What is Microsoft Defender for Endpoint (MDE)?"]
- **Microsoft Defender for Endpoint (MDE):** A comprehensive solution for preventing, detecting, and automating the investigation and response to cyber threats across endpoints. [New Concept from "What is Microsoft Defender for Endpoint (MDE)?"]

### Configuration
1. Navigate to the Azure portal and open the Conditional Access blade.
2. Create a new policy or edit an existing one.
3. In the Cloud Apps section, select the apps that the policy will apply to.
4. In the Users and Groups section, specify the users or groups that the policy will affect.
5. In the Conditions section, configure the conditions under which the policy will be enforced (e.g., device platform, location, client app).
6. In the Access Control section, select the authentication method(s) that users must use to authenticate when the policy is triggered.
7. Save the policy.

### Common Pitfalls
- Failing to exclude Global Admin accounts from CA policies can result in locking yourself out of the tenant.
- Using overly restrictive policies can unintentionally block legitimate users or devices.
- Not testing CA policies thoroughly before deploying them can lead to unexpected issues.
- Allowing Device Code Flow for all users may expose accounts to phishing attacks, it is recommended to limit its use. [New information from "What is Microsoft Defender for Endpoint (MDE)?"]

New source article: "What is Microsoft Defender for Endpoint (MDE)?"
Author: Jeffrey
New source content:
# What is Microsoft Defender for Endpoint (MDE)?

Microsoft Defender for Endpoint (MDE) is a comprehensive solution for preventing, detecting, and automating the investigation and response to cyber threats across endpoints. It includes features such as Advanced Threat Protection (ATP), Endpoint Detection and Response (EDR), and Automatic Attack Disruption. MDE provides real-time protection against malware, ransomware, and other advanced threats, and offers automated investigation and response capabilities to help organizations quickly contain and remediate security incidents.

[March 30, 2026](https://jeffreyappel.nl/automatic-migration-from-defender-for-identity-sensor-v2-to-v3-x-and-gmsa-changes/)

[March 23, 2026](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/)

[February 12, 2026](https://jeffreyappel.nl/how-to-secure-microsoft-copilot-studio-agents-with-real-time-protection/)

[February 3, 2026](https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender/)

[January 20, 2026](https://jeffreyappel.nl/how-to-archive-defender-logs-natively-in-defender-xdr-up-to-12-years/)

[January 6, 2026](https://jeffreyappel.nl/microsoft-sentinel-cost-management-how-to-get-insights-in-data-lake-usage/)