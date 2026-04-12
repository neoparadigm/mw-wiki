---
conflicts:
- '[CONFLICT: Daniel Chronlund says passkeys are a game-changer in online security,
  existing entry does not mention this.]'
- '[CONFLICT: Daniel Chronlund mentions integrated support for passkeys in Windows
  11, existing entry does not mention this.]'
- '[CONFLICT: Daniel Chronlund states that passkeys offer enhanced security and streamlined
  authentication, existing entry does not mention these benefits.]'
- '[CONFLICT: Daniel Chronlund says X, existing entry says Y]'
- '[CONFLICT: Ugur Koc introduces new Apple Intelligence features, existing entry
  does not mention these.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2021-04-05'
  title: Find Your Weakest Link and Fix It! &#8211; A Layered Approach to Microsoft
    365 Security
  url: https://danielchronlund.com/2021/04/05/find-your-weakest-link-and-fix-it-microsoft-365-security
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-09-26'
  title: '&#8220;Unlocking&#8221; the Future: The Power of Passkeys in Online Security'
  url: https://danielchronlund.com/2023/09/26/unlocking-the-future-the-power-of-passkeys-in-online-security
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2024-08-08'
  title: Simplifying Entra ID Temporary Access Pass Creation with PowerShell
  url: https://danielchronlund.com/2024/08/08/simplifying-entra-id-temporary-access-pass-creation-with-powershell
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-11-07'
  title: Manage Apple Intelligence on macOS with Intune - Ugur Koc
  url: https://ugurkoc.de/manage-apple-intelligence-on-macos-with-intune
stale_after: '2026-06-11'
title: MFA Registration Policy and TAP
topic: identity/entra-id/mfa-registration-policy
---

# MFA Registration Policy and TAP

## Overview
MFA Registration Policy and Temporary Access Pass (TAP) are security features in Microsoft 365 aimed at enhancing account protection by requiring Multi-Factor Authentication (MFA) for users and providing temporary access to accounts when MFA is not available.

## Key Concepts
- Multi-Factor Authentication (MFA)
- Temporary Access Pass (TAP)
- Conditional Access Policies
- Azure Active Directory (Azure AD)
- Security Info
- Self-Service MFA
- [Passkeys] (#unlocking-the-future-the-power-of-passkeys-in-online-security)
- PowerShell Script for TAP Creation (see below)

## Configuration
1. Set up a Conditional Access policy in the Azure portal to require MFA for users.
2. Configure Temporary Access Pass settings, such as duration and usage limits, within the same Conditional Access policy.
3. Assign the policy to the relevant user groups or individual users.
4. Users who are unable to complete MFA can request a TAP to access their accounts temporarily.
5. [Integrated support for passkeys in Windows 11] (#unlocking-the-future-the-power-of-passkeys-in-online-security) allows users to authenticate using biometrics or device PIN instead of passwords.
6. To create a TAP via PowerShell, follow the steps outlined in [Simplifying Entra ID Temporary Access Pass Creation with PowerShell] (#simplifying-entra-id-temporary-access-pass-creation-with-powershell).
7. **[Genmoji]** (#manage-apple-intelligence-on-macos-with-intune) is a new emoji generator using AI to create custom emojis on the spot, available on Apple devices.
8. **[Image Playground]** (#manage-apple-intelligence-on-macos-with-intune) is an AI-driven tool that lets users play around with photos, offering options like background changes and object removal.
9. **[Writing Tools]** (#manage-apple-intelligence-on-macos-with-intune) help polish text by providing grammar checks and tone suggestions.
10. **[Mail Summary]** (#manage-apple-intelligence-on-macos-with-intune) generates short, actionable summaries of emails to help users manage their inbox more efficiently.
11. **[Apple Intelligence with ChatGPT Integration]** (#manage-apple-intelligence-on-macos-with-intune) enhances Siri's capabilities by offering conversational AI for managing tasks and finding information.

## Common Pitfalls
- Incorrectly configuring Conditional Access policies may result in disrupted user access or increased helpdesk tickets.
- Failing to properly communicate the need for MFA and TAP to users can lead to resistance or confusion.
- Overlooking the importance of setting appropriate TAP duration and usage limits can expose accounts to unnecessary risk.
- [Overreliance on passwords may not provide the same level of security as passkeys] (#unlocking-the-future-the-power-of-passkeys-in-online-security).

## KQL / PowerShell
[The article does not provide any specific queries or scripts related to MFA Registration Policy and TAP.]

## Related Topics
- MFA registration
- Temporary Access Pass (TAP)
- Security Info
- Self-Service MFA
- [Passkeys] (#unlocking-the-future-the-power-of-passkeys-in-online-security)
- [Simplifying Entra ID Temporary Access Pass Creation with PowerShell] (#simplifying-entra-id-temporary-access-pass-creation-with-powershell)
- [Manage Apple Intelligence on macOS with Intune] (#manage-apple-intelligence-on-macos-with-intune)

[CONFLICT: Daniel Chronlund says passkeys are a game-changer in online security, existing entry does not mention this.]
[CONFLICT: Daniel Chronlund mentions integrated support for passkeys in Windows 11, existing entry does not mention this.]
[CONFLICT: Daniel Chronlund states that passkeys offer enhanced security and streamlined authentication, existing entry does not mention these benefits.]
[CONFLICT: Ugur Koc introduces new Apple Intelligence features, existing entry does not mention these.]

## Simplifying Entra ID Temporary Access Pass Creation with PowerShell

Simplifying Entra ID Temporary Access Pass Creation with

## Manage Apple Intelligence on macOS with Intune

If you’re managing macOS devices with Intune, Apple Intelligence is worth getting to know. This new set of AI-powered tools from Apple makes interacting with devices smoother and smarter. Available on iPhone, iPad, and now Mac, Apple Intelligence is designed to simplify everyday tasks – whether that’s a more natural-sounding Siri, quick editing tools for writing, or advanced image recognition in Photos to help you find what you need in seconds. It’s all about making things easier and more intuitive for users, which can be a huge win for productivity.

**So, What Exactly is Apple Intelligence?**

Think of Apple Intelligence as your device’s supercharged personal assistant. It’s a set of AI-driven tools built right into Apple’s ecosystem, making things like typing, organizing photos, and managing reminders faster and easier. Plus, with Apple’s focus on privacy, most of the processing happens directly on your device or with minimal cloud involvement – perfect for workplaces that prioritize data privacy.

In this post, we’ll explore how to tap into Apple Intelligence features within Intune to create a smoother, more efficient macOS experience for your users.

Table of Contents

[Toggle](#)

## What features are new with Apple Intelligence?

Here’s a quick look at what Apple Intelligence brings to the table:

**Genmoji**
Apple’s new emoji generator uses AI to create custom emojis on the spot. Think of it as your personal emoji artist, crafting unique expressions based on your prompts. Whether you need a quick reaction or something special for messaging, Genmoji has you covered.

**Image Playground**
Image Playground is a fun, powerful tool that lets you play around with photos using AI-driven enhancements. With options like background changes and object removal, it brings a mini creative suite right into your Photos app, making editing easy and intuitive.

**Writing Tools**
These new tools help polish your text – whether you’re drafting an email or editing a document. From grammar checks to tone suggestions, Apple’s Writing Tools make it simple to refine your writing without a separate editor.

**Mail Summary**
For anyone swamped by their inbox, Mail Summary is a lifesaver. Apple Intelligence scans your emails to generate short, actionable summaries, so you can get the gist without reading every message. It’s perfect for staying on top of things while reducing inbox overwhelm.

**Apple Intelligence with ChatGPT Integration**
In version 15.2, Siri has received a significant upgrade with ChatGPT integration. This brings conversational AI to your interactions, allowing Siri to tackle more complex questions, offer nuanced responses, and carry on a back-and-forth conversation to get you the information you need. Siri is now a much smarter, hands-free assistant for managing tasks and finding information.