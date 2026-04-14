---
conflicts:
- '[CONFLICT: Jeffrey suggests implementing this change as soon as possible, while
  the existing entry recommends enabling it to prevent attacks.]'
- '[CONFLICT: Jeffrey emphasizes the importance of not waiting for Microsoft''s change,
  while the existing entry does not mention a specific timeframe.]'
- '[CONFLICT: AshaIyengar21 does not mention password spray attacks or PowerShell.]'
- '[CONFLICT: AshaIyengar21 says X, existing entry says Y]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2020-03-17'
  title: Azure AD Password Spray Attacks with PowerShell and How to Defend your Tenant
  url: https://danielchronlund.com/2020/03/17/azure-ad-password-spray-attacks-with-powershell-and-how-to-defend-your-tenant
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2021-03-15'
  title: Block Legacy Authentication now, and don&#039;t wait for Microsoft
  url: https://jeffreyappel.nl/block-legacy-authentication-now-and-dont-wait-for-microsoft
- author: AshaIyengar21
  crawled: '2026-04-14'
  date: '2024-01-22'
  title: Enable or disable SMTP AUTH in Exchange Online
  url: https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission
stale_after: '2026-06-13'
title: Blocking Legacy Authentication Protocols
topic: identity/conditional-access/legacy-auth-blocking
---

# Blocking Legacy Authentication Protocols

## Blocking Legacy Authentication Protocols

This topic discusses the importance of blocking legacy authentication protocols in Azure Active Directory (Azure AD) to prevent password spray attacks using PowerShell. These attacks can bypass Multi-Factor Authentication (MFA) if legacy authentication is allowed, potentially compromising an organization's security.

[New Source: Block Legacy Authentication now, and don't wait for Microsoft]
According to Jeffrey, it is recommended to implement the blocking of legacy authentication as soon as possible and switch users to the latest modern authentication protocol due to its vulnerability. Microsoft has announced that they will be turning off legacy authentication, but it is advised not to wait for this change. [CONFLICT: AshaIyengar21 does not mention password spray attacks or PowerShell.]

[New Source: Enable or disable SMTP AUTH in Exchange Online]
AshaIyengar21 discusses the use of SMTP AUTH (SMTP client email submissions) for scenarios such as POP3 and IMAP4 clients, applications, reporting servers, and multifunction devices that generate and send email messages. The article emphasizes the importance of disabling SMTP AUTH in an Exchange Online organization, and enabling it only for accounts that still require it.

## Key Concepts
- Legacy authentication vs Modern authentication
- Office 365 reporting API endpoint
- Password spray attack
- Basic authentication
- Smart Lockout in Azure AD
- SMTP AUTH (SMTP client email submissions)

## Configuration
1. Enable Conditional Access to protect your organization from password spray attacks by blocking legacy authentication. [CONFLICT: Jeffrey suggests implementing this change as soon as possible, while the existing entry recommends enabling it to prevent attacks.]
2. Review and adjust the Conditional Access policies to ensure they are appropriate for your organization's needs.
3. Monitor the security logs regularly to detect any potential threats or unauthorized access attempts.
4. Disable SMTP AUTH in your organization if not already done, following the guidelines provided in [Enable or disable SMTP AUTH in Exchange Online].

## Common Pitfalls
- Allowing legacy authentication in Azure AD, which bypasses MFA and leaves the tenant vulnerable to password spray attacks. [CONFLICT: Jeffrey emphasizes the importance of not waiting for Microsoft's change, while the existing entry does not mention a specific timeframe.]
- Using more than four passwords at a time in a password spray attack script, potentially triggering Smart Lockout and locking users out of their accounts.
- Enabling SMTP AUTH without proper consideration, as it may be unnecessary for most modern email clients.

## KQL / PowerShell
The article includes a PowerShell script for demonstration purposes only. It performs a password spray attack against Azure AD using the legacy Office 365 reporting API with basic authentication. However, this script should not be used in an unethical or unlawful manner.

```powershell
function Invoke-AzureAdPasswordSprayAttack {
    # ... (omitted for brevity)
}
```

## Related Topics
- [Legacy auth](legacy_auth)
- [Basic auth](basic_auth)
- [SMTP AUTH](smtp_auth)
- [POP3](pop3)
- [IMAP](imap)

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Block Legacy Authentication now, and don’t wait for Microsoft

[Modern Workplace](https://jeffreyappel.nl/category/modern-workplace/), [Security](https://jeffreyappel.nl/category/security/)

> [Exchange Online](https://docs.microsoft.com/en-us/exchange/exchange-online/?view=exchon-2023) > Enable or disable authenticated client SMTP submission (SMTP AUTH) in Exchange Online

[Microsoft 365](https://docs.microsoft.com/en-us/microsoft-365/)

# Block Legacy Authentication now, and don’t wait for Microsoft

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[March 15, 2021](https://jeffreyappel.nl/block-legacy-authentication-now-and-dont-wait-for-microsoft/)
0


6 min read

**Legacy authentication is the most comprom

# Enable or disable authenticated client SMTP submission (SMTP AUTH) in Exchange Online

[AshaIyengar21](https://docs.microsoft.com/en-us/exchange/author/asha-iyengar-21),
[March 15, 2021](https://docs.microsoft.com/en-us/exchange/exchange-online/authenticated-client-smtp-submission/enable-or-disable-authenticated-client-smtp-submission-in-exchange-online)
0


12 min read

**SMTP client email submissions (also known as *authenticated SMTP submissions* or *SMTP AUTH*) are used in the following scenarios in Office 365 and Microsoft 365:

- POP3 and IMAP4 clients. These protocols only allow clients to *receive* email messages, so they need to use authenticated SMTP to *send* email messages.
- Applications, reporting servers, and multifunction devices that generate and send email messages.

The SMTP AUTH protocol is used for SMTP client email submissions, typically on TCP port 587. SMTP AUTH supports modern authentication (Modern Auth) through OAuth in addition to basic authentication. For more information, see [Authenticate an IMAP, POP or SMTP connection using OAuth](/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth).

Virtually all modern email clients that connect to Exchange Online mailboxes in Office 365 or Microsoft 365 (for example, Outlook, Outlook on the web, iOS Mail, Outlook for iOS and Android, etc.) don't use SMTP AUTH to send email messages.

Therefore, we highly recommend that you disable SMTP AUTH in your Exchange Online organization, and enable it only for the accounts (mailboxes) that still require it. There are two settings that can help you do this:

- An organization-wide setting to disable (or enable) SMTP AUTH.
- A per-mailbox setting that overrides the tenant-wide setting.

These settings only apply to mailboxes that are hosted in Exchange Online (Office 365 or Microsoft 365).

Note

- If *security defaults* is enabled in your organization, SMTP AUTH is already disabled in Exchange Online. To use SMTP AUTH, you need to disable *security defaults*. For more information, see [Security defaults in Microsoft Entra ID](/en-us/entra/fundamentals/security-defaults)
- If your authentication policy disables basic authentication for SMTP, clients cannot use the SMTP AUTH protocol even if you enable the settings outlined in this article. For more information, see [Disable Basic authentication in Exchange Online](/en-us/exchange/clients-and-mobile-in-exchange-online/disable-basic-authentication-in-exchange-online).

## Disable SMTP AUTH in your organization

You can disable (or enable) SMTP AUTH globally for your organization in the EAC or by using [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

To disable SMTP

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: AshaIyengar21 says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.

---

The updated wiki entry is as follows:

# Blocking Legacy Authentication Protocols

## Blocking Legacy Authentication Protocols

This topic discusses the importance of blocking legacy authentication protocols in Azure Active Directory (Azure AD) to prevent password spray attacks using PowerShell. These attacks can bypass Multi-Factor Authentication (MFA