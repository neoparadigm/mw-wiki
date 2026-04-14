---
conflicts:
- '[CONFLICT: Jeffrey states that MFA-only is not enough to stay protected against
  the latest threats in 2026, while the existing entry does not mention this.]'
- '[CONFLICT: Jeffrey states that MFA-only is not enough to stay protected against
  the latest threats in 2026, while the existing entry does not mention this]'
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-14'
  date: '2020-08-05'
  title: 'Checklist: How to Not Fall for Fake Office 365 Email Phishing Attempts'
  url: https://danielchronlund.com/2020/08/05/checklist-how-to-not-fall-for-fake-office-365-email-phishing-attempts
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-09-01'
  title: AiTM/ MFA phishing attacks in combination with &quot;new&quot; Microsoft
    protections (2026 edition)
  url: https://jeffreyappel.nl/aitm-mfa-phishing-attacks-in-combination-with-new-microsoft-protections-2023-edt
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2025-03-03'
  title: Configure automatic Attack Disruption in Microsoft Defender XDR
  url: https://jeffreyappel.nl/configure-automatic-attack-disruption-in-microsoft-defender-xdr
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2026-02-03'
  title: How to protect Microsoft Teams with Microsoft Defender
  url: https://jeffreyappel.nl/how-to-protect-microsoft-teams-with-microsoft-365-defender
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2023-08-29'
  title: How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM
    &amp; HumOR)
  url: https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2022-04-21'
  title: MFA prompt spamming/ MFA fatigue - What can you do to prevent/ detect attacks?
  url: https://jeffreyappel.nl/mfa-prompt-spamming-mfa-fatigue-what-can-you-do-to-prevent-detect-attacks
stale_after: '2026-05-29'
title: AiTM Proxy Attacks and Defence
topic: identity/conditional-access/aitm-defence
---

# AiTM Proxy Attacks and Defence

## Overview
AiTM Proxy Attacks and Defence is a topic related to cybersecurity, specifically focusing on attacks where an adversary intercepts and manipulates traffic between a user and a legitimate application, such as Office 365. These attacks can lead to unauthorized access, data theft, and other malicious activities.

## Key Concepts
- AiTM (Adversary-in-the-Middle) Proxy Attacks: Techniques used by attackers to intercept and manipulate network traffic between a user and an application.
- Evilginx: A type of AiTM attack that targets session cookies and tokens for authentication purposes.
- Session Cookie: A small piece of data stored on the user’s computer by the web browser, which is used to help a website remember information about the user.
- Token Replay: An AiTM technique where an attacker captures and reuses authentication tokens to gain unauthorized access.
- Multi-stage AiTM phishing campaigns
- Business email compromise campaigns
- Microsoft Defender
- MFA prompt spamming/ MFA fatigue (New)
- [CONFLICT: Jeffrey states that MFA-only is not enough to stay protected against the latest threats in 2026, while the existing entry does not mention this]

## New Information (from "How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM & HumOR)" by Jeffrey and "MFA prompt spamming/ MFA fatigue - What can you do to prevent/ detect attacks?" by Jeffrey)
- Microsoft's Automatic Attack Disruption feature, introduced in 2023, uses correlated insights from the Microsoft 365 ecosystem and AI models to stop sophisticated attack techniques while they are in progress. This includes support for AiTM attacks. The feature works by disrupting the attack by containing the assets that the attacker is using via the attack disruption capability. (From "How to use Automatic Attack Disruption in Microsoft 365 Defender")
- MFA prompt spamming/ MFA fatigue is a quite new term and seeing more after the LAPSUS$ attack. It is a trending topic in combination with the more recent adversary-in-the-middle phishing attempts. (From "MFA prompt spamming/ MFA fatigue - What can you do to prevent/ detect attacks?")
- [CONFLICT: Jeffrey states that MFA-only is not enough to stay protected against the latest threats in 2026, while the existing entry does not mention this]

## Configuration (updated)
The article recommends using Office 365 Advanced Threat Protection (ATP) P2, which includes an Attack Simulator that can help identify potential AiTM attacks. Additionally, it suggests implementing the latest Microsoft protections introduced in 2026 to combat the rise in AiTM/ MFA phishing attacks and configuring automatic Attack Disruption in Microsoft Defender XDR. It also advises on how to prevent and detect MFA fatigue attacks.

## Common Pitfalls
- Lack of user awareness: Users may unknowingly click on malicious links or provide sensitive information, leading to successful AiTM attacks.
- Insufficient security measures: Inadequate security configurations in Office 365 and other applications can make them vulnerable to AiTM attacks.
- [CONFLICT: Jeffrey states that MFA-only is not enough to stay protected against the latest threats in 2026, while the existing entry does not mention this]
- MFA fatigue: Users may become tired of constantly verifying their identity through MFA prompts, leading to a decrease in security vigilance and potential successful attacks.

## KQL / PowerShell
The article provides information on how to archive Defender logs natively in Defender XDR up to 12 years and automatic Windows event auditing configuration for Defender for Identity v3 x.

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > MFA prompt spamming/ MFA fatigue – What can you do to prevent/ detect attacks?
> [Security](https://jeffreyappel.nl/category/security/)
>
> # MFA prompt spamming/ MFA fatigue – What can you do to prevent/ detect attacks?
>
> [Jeffrey](https://jeffreyappel.nl/author/contact/),
> [April 21, 2022](https://jeffreyappel.nl/mfa-prompt-spamming-mfa-fatigue-what-can-you-do-to-prevent-detect-attacks/)
> 1
>
> 10 min read
>
> MFA prompt spamming/ MFA fatigue is a quite new term and seeing more after the LAPSUS$ attack. Currently there are many MFA options including SMS, One Time Passwords (OTP), and push notifications from the Microsoft Authenticator app. And while the intent of these methods is to provide extra protection, attackers use new ways of attacks. Push Notification/ MFA Fatigue/ MFA spamming is a trending topic in combination with the more recent adversary-in-the-middle phishing attempts.
>
> The most common question when discussing MFA prompt spamming; MFA is secure right? Yes – it depends on the type of MFA. Of course, it’s better than no MFA configured. SMS is always better in comparison without any second factor enabled.
>
> Blog updated: 14-07-2022: Adding adversary-in-the-middle (AiTM) and general information Blog updated: 02-10-2022: New related published blog post: [How to mitigate MFA fatigue and learn from the Uber breach for additional protection](https://jeffreyappel.nl/how-to-prevent-mfa-fatigue-and-learn-from-the-uber-breach-for-additional-protection/)
>
> |  |
> | --- |
> | ****Blog information:**** Blog published: April 21, 2022 Blog latest updated: February 4, 2023 |