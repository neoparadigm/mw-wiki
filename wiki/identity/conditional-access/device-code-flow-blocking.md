---
conflicts:
- '[CONFLICT: Anoop C Nair adds information about Microsoft Entra Tenant Health Monitoring,
  which was not present in the existing entry.]'
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
- author: Anoop C Nair
  crawled: '2026-04-12'
  date: '2025-03-14'
  title: How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations
    HTMD Blog
  url: https://www.anoopcnair.com/how-to-monitor-microsoft-entra-tenant-health
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow
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
- Microsoft Entra Tenant Health Monitoring
- [How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations HTMD Blog](#How_To_Monitor_Microsoft_Entra_Tenant_Health_And_Detect_Potential_Degradations) (New source)
- [Access Microsoft Entra Tenant Health Monitoring in Entra Portal](#How_To_Access_Microsoft_Entra_Tenant_Health_Monitoring_in_Entra_Portal) (New source)
- [How to protect against Device Code Flow abuse (Storm-2372 attacks) and block the authentication flow](#How_to_protect_against_Device_Code_Flow_abuse_Storm-2372_attacks_and_block_the_authentication_flow) (New source)

### Configuration
1. Implement controls against AiTM/Token tactics and other modern identity attacks.
2. Monitor for suspicious activities related to the Device Authorization Flow.
3. Configure Microsoft Defender products to protect against QR Code phishing.
4. Use Microsoft's recommended practices for securing Microsoft Copilot Studio agents with real-time protection. (New source)
5. Protect Microsoft Teams with Microsoft 365 Defender. (New source)
6. Automatic Windows Event Auditing configuration for Defender for Identity v3.x.
7. Archive Defender logs natively in Defender XDR up to 12 years.
8. Implement cost management for Microsoft Sentinel data lake usage.
9. [Access Microsoft Entra Tenant Health Monitoring in Entra Portal](#How_To_Access_Microsoft_Entra_Tenant_Health_Monitoring_in_Entra_Portal) (New source)
10. [Follow Jeffrey's guide on how to protect against Device Code Flow abuse and block the authentication flow](#How_to_protect_against_Device_Code_Flow_abuse_Storm-2372_attacks_and_block_the_authentication_flow) (New source)

### Common Pitfalls
- Lack of awareness and understanding of the Device Authorization Flow and its potential for abuse.
- Insufficient monitoring and control over the use of this flow in various services.
- Inadequate protection against QR Code phishing and other related attacks.
- [Lack of monitoring tenant health, which can lead to potential degradations (How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations HTMD Blog)](#How_To_Monitor_Microsoft_Entra_Tenant_Health_And_Detect_Potential_Degradations)
- [Failure to implement Jeffrey's recommended practices for securing Microsoft Copilot Studio agents with real-time protection](#How_to_protect_against_Device_Code_Flow_abuse_Storm-2372_attacks_and_block_the_authentication_flow)
- [Neglecting to protect Microsoft Teams with Microsoft 365 Defender](#How_to_protect_against_Device_Code_Flow_abuse_Storm-2372_attacks_and_block_the_authentication_flow)

### KQL / PowerShell
[The article does not provide any specific queries or scripts related to blocking Device Code Flow.]

### Related Topics
- device code
- device code flow
- microsoft.com/devicelogin
- CA block
- token theft
- Microsoft Entra Tenant Health Monitoring
- [How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations HTMD Blog](#How_To_Monitor_Microsoft_Entra_Tenant_Health_And_Detect_Potential_Degradations) (New source)
- [How to protect against Device Code Flow abuse (Storm-2372 attacks) and block the authentication flow](#How_to_protect_against_Device_Code_Flow_abuse_Storm-2372_attacks_and_block_the_authentication_flow) (New source)

### CONFLICT: Anoop C Nair says Microsoft Entra Tenant Health Monitoring, Jeffrey says How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations HTMD Blog is the new source for this information.

### CONFLICT: Jeffrey says to follow his guide on how to protect against Device Code Flow abuse and block the authentication flow, existing entry does not have this information.