---
conflict_topics:
- defender/mde/vulnerability-management
- identity/conditional-access/authentication-flows
conflicts:
- '[CONFLICT: Jeffrey says Automatic Attack Disruption, existing entry does not mention
  it]'
- '[CONFLICT: Jeffrey says this is a recent development, existing entry does not mention
  it]'
context_note: Aitm Defence is part of the identity domain. Synthesised from 6 community
  sources.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2025-09-01'
  title: AiTM/ MFA phishing attacks in combination with &quot;new&quot; Microsoft
    protections (2026 edition)
  url: https://jeffreyappel.nl/aitm-mfa-phishing-attacks-in-combination-with-new-microsoft-protections-2023-edt
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2023-08-29'
  title: How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM
    &amp; HumOR)
  url: https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-08-08'
  title: Protect against AiTM/ MFA phishing attacks using Microsoft technology
  url: https://jeffreyappel.nl/protect-against-aitm-mfa-phishing-attacks-using-microsoft-technology
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2024-01-25'
  title: Protect against QR Code phishing with Microsoft Defender products
  url: https://jeffreyappel.nl/protect-against-qr-code-phishing-with-microsoft-defender-products
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-08-31'
  title: Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue,
    PRT, OAuth)
  url: https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2022-09-22'
  title: How to mitigate MFA fatigue and learn from the Uber breach for additional
    protection
  url: https://jeffreyappel.nl/how-to-prevent-mfa-fatigue-and-learn-from-the-uber-breach-for-additional-protection
stale_after: '2026-06-02'
title: AiTM Proxy Attacks and Defence
topic: identity/conditional-access/aitm-defence
---

# AiTM Proxy Attacks and Defense

## Overview
Adversary-in-the-middle (AiTM) proxy attacks are a modern form of phishing that exploit vulnerabilities in Microsoft's protections. These attacks have seen an increase in usage, particularly with the removal of basic authentication from Exchange Online, making it crucial to understand and defend against them.

The new source provides additional information about Automatic Attack Disruption, a feature introduced by Microsoft to combat AiTM attacks. This feature uses correlated insights from the Microsoft 365 ecosystem and AI models to stop sophisticated attack techniques while they are in progress [Jeffrey]. The new source also discusses a large-scale phishing campaign using AiTM techniques to bypass multi-factor authentication [CONFLICT: Jeffrey says this is a recent development, existing entry does not mention it].

The new source sheds light on the growing threat of QR Code phishing. Attackers are using QR codes in combination with AiTM methods to bypass existing protections and steal/collect tokens/user credentials [Jeffrey]. It also provides tips for preventing against new modern identity attacks, including AiTM, MFA Fatigue, PRT, and OAuth [New Information from the new source].

## Key Concepts
- Adversary-in-the-middle (AiTM) phishing attacks
- Multifactor Authentication (MFA)
- MFA fatigue
- PRT (Proxyless RDP) attacks
- OAuth attacks
- Session cookie theft
- QR code phishing
- Automatic Attack Disruption
- Modern identity attacks
- MFA/2FA bypass techniques

## Configuration
The article does not provide specific configuration guidance for AiTM proxy defense. It is recommended to follow Microsoft's guidelines for securing various Microsoft products and services, such as Defender for Identity, Windows Event Auditing, Microsoft Sentinel, Microsoft Teams, Automatic Attack Disruption, and the tips provided in the new source [Jeffrey].

## Common Pitfalls
- Relying solely on MFA for protection against AiTM attacks (new addition from the new source)
- Neglecting to implement additional security measures beyond MFA
- Failing to keep up with the latest threats and updates in Microsoft's protections
- Overlooking the importance of Automatic Attack Disruption in the defense strategy
- Ignoring the risks associated with QR code phishing attacks
- Not being aware of modern identity attack techniques and their bypass methods (new addition from the new source)

## KQL / PowerShell
The article does not provide any specific queries or scripts related to AiTM proxy defense.

## Related Topics
- [AiTM](wiki:AiTM)
- [evilginx](wiki:evilginx)
- [adversary-in-the-middle](wiki:adversary-in-the-middle)
- [session cookie](wiki:session_cookie)
- [token replay](wiki:token_replay)
- [Automatic Attack Disruption](wiki:Automatic_Attack_Disruption)
- [Large-scale AiTM attack targeting enterprise users of Microsoft email services (new addition from the new source)](wiki:Large-scale_AiTM_attack_targeting_enterprise_users_of_M
- [MFA Fatigue](wiki:MFA_Fatigue) (new addition from the new source)

New source article: "How to mitigate MFA fatigue and learn from the Uber breach for additional protection"
Author: Jeffrey
New source content:

[...]
(The existing entry remains unchanged as the new source does not provide any new information not already present.)