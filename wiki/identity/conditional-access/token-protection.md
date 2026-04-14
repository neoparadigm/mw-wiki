---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2020-10-22'
  title: Fast response with Azure AD Continuous Access Evaluation (CAE) and Conditional
    Access
  url: https://jeffreyappel.nl/fast-response-with-azure-ad-continuous-access-evaluation-cae-and-conditional-access
stale_after: '2026-06-13'
title: Token Protection and CAE
topic: identity/conditional-access/token-protection
---

# Token Protection and CAE

## Token Protection and CAE

### Overview
Azure AD Continuous Access Evaluation (CAE) is a feature in Previews that allows for faster response to security incidents by evaluating Conditional Access Policies and user changes in real-time, as opposed to the traditional lifetime of a token which defaults to one hour. This is crucial for situations where immediate action is required, such as blocking a user due to a data breach.

### Key Concepts
- Continuous access evaluation (CAE)
- OAuth 2.0 access tokens
- Token lifetime
- Elevated user risk detected by Azure AD Identity Protection
- User account deletion or disablement
- Password change or reset
- Multi-factor authentication
- Administrator token revocation

### Configuration
The article does not provide specific configuration guidance for CAE. It is recommended to consult Microsoft documentation for the latest instructions on enabling and configuring CAE.

### Common Pitfalls
- Failing to understand the importance of immediate response in security incidents and not utilizing CAE when necessary.
- Not being aware of the scenarios where CAE is currently supported (elevated user risk, account deletion/disablement, password change, MFA enablement, token revocation).

### KQL / PowerShell
The article does not include any relevant queries or scripts.

### Related Topics
- Token protection
- CAE
- Continuous access evaluation
- Token binding
- Session token