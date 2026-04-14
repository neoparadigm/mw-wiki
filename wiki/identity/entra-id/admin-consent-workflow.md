---
conflicts:
- '[CONFLICT: Jeffrey adds "Illicit consent attacks"]'
- '[CONFLICT: Jeffrey adds "consent phishing attacks (Illicit consent attacks)"]'
- '[CONFLICT: This section provides additional details not present in the existing
  entry]'
- '[CONFLICT: Jeffrey says X, existing entry says Y]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2020-06-07'
  title: Controle op Azure AD machtigingen met de Admin consent workflow; zo werkt
    het
  url: https://jeffreyappel.nl/controle-op-azure-ad-machtigingen-met-de-admin-consent-workflow-zo-werkt-het
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2022-02-02'
  title: Protect against AzureAD OAuth Consent phishing attempts (Illicit consent
    attack)
  url: https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack
stale_after: '2026-06-13'
title: Admin Consent Workflow and OAuth App Control
topic: identity/entra-id/admin-consent-workflow
---

# Admin Consent Workflow and OAuth App Control

## Admin Consent Workflow and OAuth App Control

### Overview
This topic discusses controlling Azure AD permissions using the Admin consent workflow, which helps prevent unwanted permissions before it's too late when integrating various cloud applications with Azure AD. The new source article provides additional insights into protecting against AzureAD OAuth Consent phishing attempts (Illicit consent attack).

### Key Concepts
- Beveiligen van de identiteit
- Admin consent workflow
- OAuth app control
- Phishing for consent
- App permissions
- [CONFLICT: Jeffrey adds "Illicit consent attacks"]

### Configuration
The article does not provide specific configuration guidance. However, the new source provides information on Microsoft prevention/detection capabilities against OAuth Consent phishing.

### Common Pitfalls
- Lack of control over new applications and access permissions, which can lead to excessive permissions being granted. This is especially problematic when apps have malicious intentions to gain access to an organization's data through OAUTH. [CONFLICT: Jeffrey adds "consent phishing attacks (Illicit consent attacks)"]

### KQL / PowerShell
No relevant queries or scripts provided in the article.

### Related Topics
- Admin consent
- User consent
- OAuth app
- Consent phishing
- App permissions
- Illicit consent attacks

## Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)
[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 2, 2022](https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack/)
1

10 min read

**In the last couple of months, there is a large increase visible in consent phishing emails ([illicit consent attacks](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/detect-and-remediate-illicit-consent-grants?view=o365-worldwide)). Microsoft threat analysts are tracking a continued increase in consent phishing attempts/mails. This blog described some of the Microsoft prevention/detection capabilities against OAuth Consent phishing.**

## What is consent phishing?

Consent phishing attacks (Illicit consent attacks) abuse legitimate cloud service providers, including Microsoft, Meta, Google, and others that use OAuth 2.0 authorization. OAuth 2.0 is a widely used protocol that allows third-party apps to access account details and perform an action on their behalf.

The main goal of a consent phishing attack is to let users grant permissions (content) to apps that are owned by the malicious attacker. The attacker then tricks an end-user into granting that application consent to access their data. [CONFLICT: This section provides additional details not present in the existing entry]

The difference in comparison with a credential attack is that the user uses a valid identity provider and no fake landing page for sign-in or any other method for credential harvesting. In a consent phishing attack, the user sign-in takes place on the identity provider itself. Targeted users who grant the permissions allow attackers to make API on their behalf through OAuth 2.0 authorization. [CONFLICT: This section provides additional details not present in the existing entry]

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: Jeffrey says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content