---
conflicts:
- '[CONFLICT: kenwith says PRT, existing entry does not mention it]'
context_note: Token Protection is part of the identity domain. Synthesised from 1
  community source.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-10-22'
  title: Fast response with Azure AD Continuous Access Evaluation (CAE) and Conditional
    Access
  url: https://jeffreyappel.nl/fast-response-with-azure-ad-continuous-access-evaluation-cae-and-conditional-access
- author: kenwith
  crawled: '2026-04-18'
  date: '2026-03-24'
  title: How Token Protection Enhances Conditional Access Policies - Microsoft Entra
    ID
  url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection
stale_after: '2026-06-17'
title: Token Protection and CAE
topic: identity/conditional-access/token-protection
---

# Token Protection and CAE

## Token Protection and CAE

### Overview
Azure AD Continuous Access Evaluation (CAE) is a feature in Previews that provides more control over token lifetime and evaluates Conditional Access Policies and user changes in real-time, improving security response time compared to the traditional one-hour token validity. Token Protection is a Conditional Access session control that attempts to reduce token replay attacks by ensuring only device bound sign-in session tokens, like Primary Refresh Tokens (PRTs), are accepted by Microsoft Entra ID when applications request access to protected resources [(Source: kenwith)](#).

### Key Concepts
- Azure Active Directory (AzureAD)
- OAuth 2.0 access tokens
- Continuous access evaluation
- Elevated user risk detection by Azure AD Identity Protection
- User account deletion or disablement
- Password change or reset for a user
- Multi-factor authentication for a user
- Token refresh and extension
- Device bound sign-in session tokens (e.g., Primary Refresh Tokens)

### Configuration
The article does not provide specific configuration guidance. It is recommended to consult Microsoft documentation for detailed steps on enabling and configuring Azure AD Continuous Access Evaluation and Token Protection [(Source: kenwith)](#).

### Common Pitfalls
- Failing to understand the importance of fast response times in security incidents and not utilizing CAE when necessary.
- Misconfiguring Conditional Access Policies or user changes, leading to unintended access restrictions or security breaches.

### KQL / PowerShell
The article does not include any relevant queries or scripts.

### Related Topics
- [Token Protection](token_protection)
- [CAE (Continuous Access Evaluation)](cae)
- [Continuous access evaluation](continuous_access_evaluation)
- [Token binding](token_binding)
- [Session token](session_token)
- [Primary Refresh Token (PRT)](#)

[CONFLICT: kenwith says PRT, existing entry does not mention it]