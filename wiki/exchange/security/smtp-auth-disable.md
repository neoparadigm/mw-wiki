---
conflicts: []
context_note: Smtp Auth Disable is part of the exchange domain. It connects closely
  to Legacy Auth Blocking. Synthesised from 1 community source.
domain: exchange
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- identity/conditional-access/legacy-auth-blocking
sources:
- author: AshaIyengar21
  crawled: '2026-04-18'
  date: '2024-01-22'
  title: Enable or disable SMTP AUTH in Exchange Online
  url: https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission
stale_after: '2026-07-17'
title: Disabling SMTP AUTH and Legacy Protocols
topic: exchange/security/smtp-auth-disable
---

# Disabling SMTP AUTH and Legacy Protocols

## Overview
Disabling SMTP AUTH and Legacy Protocols in Exchange Online is crucial for enhancing security by preventing unauthenticated email submissions. This topic matters as it helps organizations control access to their mailboxes and protect against potential threats.

## Key Concepts
- SMTP AUTH: Authenticated Submission of Simple Mail Transfer Protocol (SMTP) client emails.
- Legacy Protocols: Outdated protocols like POP3 and IMAP4 that require authenticated SMTP for sending emails.
- Modern Auth: Modern authentication methods used in SMTP AUTH, such as OAuth.
- Security Defaults: A feature in Microsoft Entra ID that disables SMTP AUTH by default.
- Basic Authentication: An older authentication method that can be disabled to prevent the use of SMTP AUTH.

## Configuration
To disable SMTP AUTH globally for your organization, you can either use the Exchange Admin Center (EAC) or Exchange Online PowerShell:

### EAC Method
1. Navigate to the **Mail Flow** settings page in the [Settings](https://admin.exchange.microsoft.com/#/settings).
2. Toggle the setting labeled **Turn off SMTP AUTH protocol for your organization**.

### PowerShell Method
1. Connect to Exchange Online PowerShell.
2. Run the command: `Set-TransportConfig -SmtpClientAuthenticationDisabled $true`

To enable SMTP AUTH for specific mailboxes, use the following PowerShell command:
```
Set-Mailbox <mailbox> -SmtpClientAuthenticationRequired $false
```
Replace `<mailbox>` with the desired mailbox.

## Common Pitfalls
- Failing to disable SMTP AUTH globally and only disabling it for specific mailboxes can lead to security vulnerabilities.
- Enabling SMTP AUTH when security defaults are enabled or basic authentication is disabled for SMTP may cause issues.

## KQL / PowerShell
```powershell
Get-TransportConfig | Format-List SmtpClientAuthenticationDisabled
Set-Mailbox <mailbox> -SmtpClientAuthenticationRequired $false
```

## Related Topics
- [SMTP AUTH](/path/to/smtp_auth)
- [Disable SMTP](/path/to/disable_smtp)
- [Legacy Protocol](/path/to/legacy_protocol)
- [POP3 disable](/path/to/pop3_disable)
- [IMAP disable](/path/to/imap_disable)