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
- Allowing Device Code Flow for all users may expose accounts to phishing attacks, it is recommended to restrict its use to trusted locations and specific user groups.

### KQL / PowerShell
This article does not provide any specific queries or scripts related to authentication flows.

### Related Topics
- [Authentication Flow](wiki:authentication_flow)
- [Device Code](wiki:device_code)
- [Legacy Auth](wiki:legacy_auth)
- [OAuth](wiki:oauth)
- [CA Policy](wiki:ca_policy)
- [Authentication Transfer](wiki:authentication_transfer)
- [Device Code Flow](wiki:device_code_flow)

New source article: "Block authentication flows with Conditional Access policy - Microsoft Entra ID"
Author: kenwith
New source content:
[...] (The existing entry already covers this section)

---

#### Share via

Facebook

x.com

LinkedIn

Email

---

Note
A

New source article: "How to restrict Device Code Flow in Entra ID"
Author: Jan Bakker
New source content:
[...] (The existing entry already covers the configuration section)

---

#### Share via

Facebook

x.com

LinkedIn

Email