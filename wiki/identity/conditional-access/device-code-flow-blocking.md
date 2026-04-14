---
conflicts:
- '[CONFLICT: Jeffrey''s article mentions Storm-2372 attacks, but the existing entry
  does not.]'
- '[CONFLICT: Jeffrey''s article mentions a specific phishing campaign known as Storm-2372.]'
- '[CONFLICT: Jeffrey''s article does not provide specific configuration steps.]'
- '[CONFLICT: Jeffrey''s article does not mention common pitfalls.]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2025-03-14'
  title: How To Monitor Microsoft Entra Tenant Health And Detect Potential Degradations
    HTMD Blog
  url: https://www.anoopcnair.com/how-to-monitor-microsoft-entra-tenant-health
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow/
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-02-16'
  title: How to protect against Device Code Flow abuse (Storm-2372 attacks) and block
    the authentication flow
  url: https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow
- author: Jan Bakker
  crawled: '2026-04-14'
  date: '2025-05-06'
  title: How to restrict Device Code Flow in Entra ID
  url: https://janbakker.tech/how-to-restrict-device-code-flow-in-entra-id/
stale_after: '2026-06-13'
title: Blocking Device Code Flow
topic: identity/conditional-access/device-code-flow-blocking
---

# Blocking Device Code Flow

## Overview
Blocking Device Code Flow is a security feature in Microsoft Entra ID to protect tenants from phishing attacks by preventing unauthorized access through device code flows. This measure is crucial for maintaining tenant health and securing user data. [CONFLICT: Jeffrey's article mentions Storm-2372 attacks, but the existing entry does not.]

## Key Concepts
- Device Code Flow: A method used for sign-in authentication where a device code is generated and sent to the user's device, which they then enter on the application or service they are trying to access.
- Phishing Attacks: Cyber attacks that aim to trick users into revealing sensitive information such as passwords or personal data. [CONFLICT: Jeffrey's article mentions a specific phishing campaign known as Storm-2372.]
- Tenant Health: The overall state of a Microsoft Entra tenant, including its security, performance, and reliability.
- Storm-2372 Attacks: A sophisticated phishing campaign that leverages the device code authorization flow, targeting various sectors such as government/IT services and critical industries. [NEW: added from Jeffrey's article]
- Trusted Locations: Specific network or location where device code flow is allowed for users in an exclusion group. [NEW: added from Jan Bakker's article]

## Configuration
To block device code flows in Microsoft Entra ID, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#home).
2. Navigate to **Security** > **Authentication methods** > **Device authentication**.
3. Under **Device authentication settings**, find the **Block device code flow** toggle and enable it.
4. Click on **Save** to apply the changes. [CONFLICT: Jeffrey's article does not provide specific configuration steps.]

## Common Pitfalls
- Enabling this feature may impact users who rely on device code flows for sign-in, so it's essential to communicate the change and provide alternative authentication methods if necessary.
- Carefully consider the balance between security and usability when deciding whether to block device code flows. [CONFLICT: Jeffrey's article does not mention common pitfalls.]
- Be aware of sophisticated phishing campaigns like Storm-2372 that aim to bypass existing controls and evaluate new techniques used for identity access. [NEW: added from Jeffrey's article]
- To allow device code flow only for specific users in trusted locations, create two Conditional Access policies as described in Jan Bakker's article. [NEW: added from Jan Bakker's article]

## Related Topics
- Device code
- Device code flow
- [Microsoft documentation on Device Login](https://docs.microsoft.com/devicelogin)
- CA block
- Token theft
- Storm-2372 attacks
- Trusted Locations

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > How to protect against Device Code Flow abuse (Storm-2372 attacks) and block the authentication flow

[Security](https://jeffreyappel.nl/category/security/)

# How to protect against Device Code Flow abuse (Storm-2372 attacks) and block the authentication flow

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 16, 2025](https://jeffreyappel.nl/how-to-protect-against-device-code-flow-abuse-storm-2372-attacks-and-block-the-authentication-flow/)
7

Since August 2024 there has been a sophisticated phishing campaign known as Storm-2372 that heavily uses device code flow to gain access to Microsoft 365 accounts and data. Device code phishing is effective, as it bypasses phishing-resistant MFA like passkeys. The victim will simply hand over an access token to the attacker.

Microsoft recommends blocking device code flow wherever possible and allowing it only where necessary.

## How to restrict Device Code Flow in Entra ID

[Jan Bakker](https://janbakker.tech/),
[May 6, 2025]

For good reasons, device code flow in Entra ID is getting a lot of attention. Attackers heavily use it to get access to Microsoft 365 accounts and data. Device code phishing is very effective, as phishing-resistant MFA, like passkeys, are not helping here. The victim will simply hand over an access token to the attacker. The attacker does not care how authentication is being done.

Microsoft recommends blocking device code flow wherever possible and allowing it only where necessary. And that’s exactly where this post will fit in. The purpose of this post is to restrict device code flow and make it available only for those who need it.

Device code flow on itself is a very neat feature that serves many use cases. So, blocking it for everyone might not be the best approach. In my opinion, it should at least be blocked for frontline workers, who will most likely fall for this type of attack if it lands in their email or chat. Next, think about your admins, especially when they are not working from a separate admin device like a PAW. I see device code flow mainly used by Teams Room devices, and by developers and administrators who need to authenticate on devices and services without interfaces.

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

If you want strict control over device code flow, consider implementing these Conditional Access policies in your tenant.