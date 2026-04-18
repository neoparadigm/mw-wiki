---
conflict_topics:
- identity/entra-id/admin-consent-workflow
- identity/conditional-access/device-code-flow-blocking
conflicts:
- '[CONFLICT: Jeffrey mentions POP3/IMAP, but they are not explicitly mentioned in
  the existing entry]'
context_note: Legacy Auth Blocking is part of the identity domain. It connects closely
  to Smtp Auth Disable. Synthesised from 2 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- exchange/security/smtp-auth-disable
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2021-03-15'
  title: Block Legacy Authentication now, and don&#039;t wait for Microsoft
  url: https://jeffreyappel.nl/block-legacy-authentication-now-and-dont-wait-for-microsoft
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-05-28'
  title: Legacy Authentication; Zo blokkeer je Legacy Authentication voordat Microsoft
    het voor je doet
  url: https://jeffreyappel.nl/legacy-authentication-zo-blokkeer-je-legacy-authentication-voordat-microsoft-het-verplicht
stale_after: '2026-06-17'
title: Blocking Legacy Authentication Protocols
topic: identity/conditional-access/legacy-auth-blocking
---

# Blocking Legacy Authentication Protocols

## Overview
Blocking Legacy Authentication Protocols is crucial for enhancing security in Microsoft cloud services by replacing older protocols with modern authentication services that support multi-factor authentication and modern authentication methods.

## Key Concepts
- Legacy authentication refers to all protocols that use Basic Authentication, which only requires one method of authentication.
- Modern Authentication is based on OAuth 2.0.
- The following legacy authentication protocols are considered: Authenticated SMTP, Autodiscover, Exchange ActiveSync (EAS), Exchange Online PowerShell, and POP3/IMAP (as per the new source). [CONFLICT: Jeffrey mentions POP3/IMAP, but they are not explicitly mentioned in the existing entry]

## Configuration
1. Identify the legacy authentication protocols in use by checking the Microsoft 365 admin center or using PowerShell cmdlets.
2. Configure modern authentication for each identified protocol:
   - For Authenticated SMTP, use TLS/SSL encryption and disable plaintext authentication.
   - For Autodiscover, configure modern authentication in Exchange Online.
   - For EAS and Exchange Online PowerShell, enable multi-factor authentication (MFA) and configure Conditional Access policies to block legacy authentication.
   - For POP3/IMAP, consider migrating to a modern mail client that supports OAuth 2.0 or use Microsoft Graph API for accessing emails [as per the new source].

## Common Pitfalls
- Failing to properly configure modern authentication for each protocol can lead to continued use of legacy authentication.
- Not enabling MFA and Conditional Access policies can leave the environment vulnerable to password threats.
- Neglecting to address POP3/IMAP usage if they are still in use [as per the new source].

## KQL / PowerShell
[The article does not provide specific queries or scripts related to blocking legacy authentication.]

## Related Topics
- Legacy auth
- Basic auth
- SMTP AUTH
- POP3
- IMAP
- Modern Authentication
- OAuth 2.0
- Multi-factor authentication (MFA)
- Conditional Access policies