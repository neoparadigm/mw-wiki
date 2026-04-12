---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow/
stale_after: '2026-06-11'
title: Blocking Device Code Flow
topic: identity/conditional-access/device-code-flow-blocking
---

# Blocking Device Code Flow

## Blocking Device Code Flow

### Overview
The Device Authorization Flow is a method used for authentication in Microsoft services where a code generated on another device or service is entered to authenticate without Multi-Factor Authentication (MFA) or additional authentication. This flow has been abused in sophisticated phishing campaigns, known as Storm-2372 attacks, which target various sectors including government/IT services and critical industries. Blocking this flow is crucial for securing modern workplaces against these attacks.

### Key Concepts
- Device Authorization Flow
- Storm-2372 attacks
- Phishing campaigns
- Russian state interests
- AiTM/ Token tactics
- Modern identity attacks
- MFA phishing attacks
- QR Code phishing
- PRT (Passwordless Authentication)
- OAuth

### Configuration
1. Implement controls against AiTM/Token tactics and other modern identity attacks.
2. Monitor for suspicious activities related to the Device Authorization Flow.
3. Configure Microsoft Defender products to protect against QR Code phishing.
4. Use Microsoft's recommended practices for securing Microsoft Copilot Studio agents with real-time protection.
5. Protect Microsoft Teams with Microsoft 365 Defender.
6. Automatic Windows Event Auditing configuration for Defender for Identity v3.x.
7. Archive Defender logs natively in Defender XDR up to 12 years.
8. Implement cost management for Microsoft Sentinel data lake usage.

### Common Pitfalls
- Lack of awareness and understanding of the Device Authorization Flow and its potential for abuse.
- Insufficient monitoring and control over the use of this flow in various services.
- Inadequate protection against QR Code phishing and other related attacks.

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to blocking Device Code Flow.]

### Related Topics
- device code
- device code flow
- microsoft.com/devicelogin
- CA block
- token theft