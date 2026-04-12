---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-09-21'
  title: Conditional Access Ring Based Deployment with DCToolbox
  url: https://danielchronlund.com/2021/09/21/conditional-access-ring-based-deployment-with-dctoolbox
stale_after: '2026-06-11'
title: Token Protection and CAE
topic: identity/conditional-access/token-protection
---

# Token Protection and CAE

## Token Protection and CAE

Token Protection and Conditional Access Evaluation (CAE) are security features in Microsoft Azure Active Directory (Azure AD) that help protect against unauthorized access to applications and data. These features are crucial for maintaining the security of modern workplaces by enforcing strong authentication and conditional access policies.

## Key Concepts
- Token Protection: A set of security measures applied to access tokens issued by Azure AD, including token signing, encryption, and anti-phishing protection.
- Conditional Access Evaluation (CAE): A feature that evaluates the risk level of a user's sign-in attempt before granting or denying access to resources.
- Token binding: A mechanism that associates an access token with the client application making the request, helping to prevent unauthorized access and replay attacks.
- Session token: A short-lived token issued after successful authentication, used for subsequent requests within the same session to avoid repeated authentication.

## Configuration
1. Enable Token Protection in Azure AD by navigating to `Azure Active Directory > Security > Authentication methods > Token signing and encryption`.
2. Configure Conditional Access policies to enforce CAE by creating a new policy, selecting users or groups, and applying the necessary access controls under `Conditions > Client app > Require client app compliance` and `Conditions > Grant > Cloud apps or actions > Select apps that can be accessed`.
3. Enable token binding for specific applications by navigating to `Azure Active Directory > App registrations > Your app > Authentication > Advanced settings > Token lifetime > Enable token binding`.

## Common Pitfalls
- Misconfiguring Conditional Access policies can lead to denied access for legitimate users or increased risk of unauthorized access.
- Failing to enable token protection and token binding for critical applications can leave them vulnerable to attacks.
- Incorrectly configuring session tokens can result in extended sessions, increasing the risk of unauthorized access over an extended period.

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to Token Protection and CAE.]

## Related Topics
- [Token protection](wiki:token_protection)
- [CAE](wiki:conditional_access_evaluation)
- [Continuous access evaluation](wiki:continuous_access_evaluation)
- [Token binding](wiki:token_binding)
- [Session token](wiki:session_token)