---
conflict_topics:
- identity/entra-id/service-principal-governance
- identity/entra-id/graph-api-permissions
conflicts:
- '[CONFLICT: Simon Skotheimsvik mentions no pitfalls specific to Offpad, existing
  entry includes general pitfalls]'
- '[CONFLICT: Jeffrey does not mention any pitfalls specific to Temporary Access Pass,
  existing entry includes general pitfalls]'
- '[CONFLICT: Jeffrey says X, existing entry says Y]'
- '[CONFLICT: Jan Bakker says that guest users who access your (resource) tenant with
  MFA enforced are unable to register a passkey, despite having it enabled or registered
  in their home tenant. This is not mentioned in the existing entry.]'
context_note: Passwordless Authentication is part of the identity domain. Synthesised
  from 6 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-09-04'
  title: How to activate the new options for Passwordless authentication
  url: https://jannikreinhard.com/2022/09/04/how-to-activate-the-new-options-for-passwordless-authentication
- author: Daniel Chronlund
  crawled: '2026-04-18'
  date: '2023-09-26'
  title: '&#8220;Unlocking&#8221; the Future: The Power of Passkeys in Online Security'
  url: https://danielchronlund.com/2023/09/26/unlocking-the-future-the-power-of-passkeys-in-online-security
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2024-02-20'
  title: 'Simon does FIDO2 Magic: Using the Offpad with Microsoft 365'
  url: https://skotheimsvik.no/fido2-magic-using-the-offpad-with-microsoft-365
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-02-16'
  title: Go fully passwordless with the new Azure AD Temporary Access Pass feature
  url: https://jeffreyappel.nl/go-fully-passwordless-with-the-new-azure-ad-temporary-access-pass-feature
- author: Simon Skotheimsvik
  crawled: '2026-04-18'
  date: '2023-04-26'
  title: 'Simon does Hack Your Security with One Trick: Strong Authentication'
  url: https://skotheimsvik.no/hack-your-security-with-one-trick-strong-authentication
- author: Jan Bakker
  crawled: '2026-04-18'
  date: '2025-12-19'
  title: How to enable passkeys for guest users in Entra ID
  url: https://janbakker.tech/how-to-enable-passkeys-for-guest-users-in-entra-id
stale_after: '2026-06-17'
title: Passwordless Authentication Methods
topic: identity/entra-id/passwordless-authentication
---

# Passwordless Authentication Methods

## Passwordless Authentication Methods

Passwordless authentication is a method for logging into Windows or other Microsoft services without requiring a password. This approach provides both convenience and high security by eliminating the need for users to remember complex passwords.

## Key Concepts
- WhfB (Windows Hello for Business)
- Fido2
- Authenticator app
- Strong Credential flow
- Push notification service (APNS, FCM)
- Private key authentication via pin or biometric
- Nonce and proof-of-presence challenge
- [Passkeys](#new-passkeys)
- Offpad (New source content)
- [Temporary Access Pass (New Source Content: "Go fully passwordless with the new Azure AD Temporary Access Pass feature")]
- [How to enable passkeys for guest users in Entra ID (New Source Content: Jan Bakker)]
- [Simon does Hack Your Security with One Trick: Strong Authentication]

## Configuration
1. Open the Azure Ad in the Browser (<https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview>)
2. Navigate to **Security** > **Authentication methods** > **Policies**
3. Select **Microsoft Authenticator**, enable the option, and set authentication mode to **Passwordless**
4. Configure new options as needed (require number matching for push notification, show application name, show geographic location)
5. Save the changes
6. Open <https://aka.ms/mysecurityinfo>, add the Authenticator app as a sign-in method, download the app, scan the code with the app, and activate login per phone
7. [New Source Content: Configuration for Offpad]
8. [Configuration for guest users in Entra ID (New Source Content: Jan Bakker)]
9. [Simon does Hack Your Security with One Trick: Strong Authentication - Enable FIDO2 Security Key Method in the Tenant, Onboard a FIDO2 key for a user, Introducing Strong MFA Methods To The Users, Choose FIDO key to sign In]
10. [Force Strong Authentication for Sensitive Operations sections from Simon does Hack Your Security with One Trick: Strong Authentication - Authentication Strengths, Conditional Access Policy with Authentication Strength, Add Strong Authentication to PIM, Configure Authentication Context, Conditional Access Policy using the Authentication Context, PIM with CA authentication context, PIM Requiring Strong Auth]
11. [Force Specific FIDO2 Key Brands sections from Simon does Hack Your Security with One Trick: Strong Authentication - FIDO2 Key Restrictions in Authentication Methods]
12. [Strong Authentication on Auto section from Simon does Hack Your Security with One Trick: Strong Authentication]
13. [Feitian Toolbox section from Simon does Hack Your Security with One Trick: Strong Authentication]
14. [Track The Usage sections from Simon does Hack Your Security with One Trick: Strong Authentication - Track Down the SMS'ers, Track Down the Password'ers]
15. [Wrapping Up section from Simon does Hack Your Security with One Trick: Strong Authentication]

## Common Pitfalls
- Ensuring that the logged-in user is also the one accessing services (WhfB only works for users who are logging in to Windows)
- [CONFLICT: Jan Bakker says that guest users who access your (resource) tenant with MFA enforced are unable to register a passkey, despite having it enabled or registered in their home tenant. This is not mentioned in the existing entry.]