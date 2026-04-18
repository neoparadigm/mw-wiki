---
conflict_topics:
- identity/conditional-access/authentication-flows
- identity/conditional-access/legacy-auth-blocking
conflicts:
- '[CONFLICT: Existing entry does not mention the specific timeline of the phishing
  campaign.]'
- '[CONFLICT: Existing entry does not mention the increased exposure or active attacks
  due to control implementation.]'
- '[CONFLICT: Jan Bakker suggests that device code phishing is effective against phishing-resistant
  MFA like passkeys, while the existing entry does not mention this.]'
- '[CONFLICT: Jan Bakker suggests a two-step approach for blocking device code flow:
  creating policies to block it for all users except an exclusion group and trusted
  locations.]'
context_note: Device Code Flow Blocking is part of the identity domain. Synthesised
  from 3 community sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow/
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow
- author: Jan Bakker
  crawled: '2026-04-18'
  date: '2025-05-06'
  title: How to restrict Device Code Flow in Entra ID
  url: https://janbakker.tech/how-to-restrict-device-code-flow-in-entra-id/
stale_after: '2026-06-17'
title: Blocking Device Code Flow
topic: identity/conditional-access/device-code-flow-blocking
---

# Blocking Device Code Flow

## Overview
The topic "Blocking Device Code Flow" is crucial for securing modern workplaces against sophisticated phishing campaigns like Storm-2372, which abuse the device code authorization flow. These attacks target various sectors and are linked to Russian state interests. [New source: Jeffrey states that there has been a sophisticated phishing campaign actively leveraging the device code authorization flow since August 2024, primarily targeting government/IT services and critical industries (Storm-2372).]

[CONFLICT: Jan Bakker suggests that device code phishing is effective against phishing-resistant MFA like passkeys, while the existing entry does not mention this.]

## Key Concepts
- Device Authorization Flow: A method used for authentication without a web browser, making it easier for attackers to bypass existing controls.
- Microsoft.com/devicelogin: The website where the device code is entered for authentication.
- Token Theft: The unauthorized use of authentication tokens for malicious purposes. [New source: Jeffrey mentions AiTM/ MFA phishing attacks as an example of advanced techniques used to get identity access.]

## Configuration
The article does not provide specific configuration guidance for blocking Device Code Flow. It is recommended to implement a multi-layered security strategy, including Microsoft Defender products and controls against AiTM/ Token tactics, as well as staying updated on new techniques used by attackers. [New source: Jeffrey provides examples of blogs related to more advanced techniques used to get identity access.]

[CONFLICT: Jan Bakker suggests a two-step approach for blocking device code flow: creating policies to block it for all users except an exclusion group and trusted locations.]

## Common Pitfalls
- Lack of awareness about the risks associated with Device Code Flow and insufficient security measures.
- Inadequate monitoring and response to potential threats related to device code abuse. [New source: Jeffrey mentions that victims are always researching new ways to bypass existing controls and evaluating with the new techniques.]

## KQL / PowerShell
The article does not include any relevant queries or scripts for blocking Device Code Flow.

## Related Topics
- Device code
- Device code flow
- microsoft.com/devicelogin
- CA block
- Token theft
- AiTM/ MFA phishing attacks [New source]
- Exclusion group (new concept from Jan Bakker)
- Trusted Locations (new concept from Jan Bakker)

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > How to protect against Device Code Flow abuse (Storm-2372 attacks) and block the authentication flow

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 16, 2025](https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow/)
7


12 min read

Since August 2024 there has been a sophisticated phishing campaign actively leveraging the device code authorization flow. Currently, there is a wide range of attacks targeting a wide range of sectors including government/ IT services and critical industries. The attack is known as *[Storm-2372](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phi

New source article: "How to restrict Device Code Flow in Entra ID"
Author: Jan Bakker
New source content:
# How to restrict Device Code Flow in Entra ID

How to restrict Device Code Flow in Entra ID - JanBakker.tech

- May 6, 2025May 6, 2025
- [Entra](https://janbakker.tech/category/entra/), [Security](https://janbakker.tech/category/security/)
- 6 min read

For good reasons, device code flow in Entra ID is getting a lot of attention. Attackers heavily use it to get access to Microsoft 365 accounts and data. Device code phishing is very effective, as phishing-resistant MFA, like passkeys, are not helping here. The victim will simply hand over an access token to the attacker. The attacker does not care how authentication is being done.

Microsoft recommends [blocking device code flow](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows) wherever possible and allowing it only where necessary. And that’s exactly where this post will fit in. The purpose of this post is to restrict device code flow and make it available only for those who need it.

Device code flow on itself is a very neat feature that serves many use cases. So, blocking it for everyone might not be the best approach. In my opinion, it should *at least* be blocked for frontline workers, who will most likely fall for this type of attack if it lands in their email or chat. Next, think about your admins, especially when they are not working from a separate admin device like a PAW. I see device code flow mainly used by Teams Room devices, and by developers and administrators who need to authenticate on devices and services without interfaces.

For legitimate use cases, device code flow can be allowed but restricted to trusted locations.
To build that, we need **two** Conditional Access policies:

Block Device Code Flow for All Users, except an **exclusion group**

Name: **Global-AllUsers-DeviceCodeFlow-Block**
Users: Include: **All Users**
Users: Exclude: *Your Exclusion Group*
Target Resources: **All resources (formerly ‘All cloud apps’)**
Conditions: Authentication flows > **Device Code Flow**
Grant: **BLOCK**


Block Devoce Code Flow for All Users, except **Trusted Locations**

Name: **Global-AllUsers-DeviceCodeFlow-TrustedLocationsOnly**
Users: Include: **All Users**
Target Resources: **All resources (formerly ‘All cloud apps’)**
Conditions: Authentication flows > **Device Code Flow**
Conditions: Locations: Include: **Any network or location**
Conditions: Locations: Exclude: **All trusted networks and locations** (or select specific networks)
Grant: **BLOCK**

This gives us two controls over the device code flow feature:

- Who can use it? (Exclusion group).
- From where can they use it? (Named Locations).

Members of the exclusion group can use Device Code Flow from Trusted Locations only, while all other users are blocked. Trusted/Named Locations can be defined [here](https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/~/NamedLocations/menuId//fromNav/) and marked as trusted.

If you want strict contr