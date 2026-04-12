---
conflicts:
- '[CONFLICT: Jeffrey''s article mentions MDTI, but does not provide any new information
  about AiTM proxy attacks.]'
- '[CONFLICT: Jeffrey mentions MFA prompt spamming/ MFA fatigue, but does not provide
  information about AiTM proxy attacks.]'
- '[CONFLICT: Bert-Jan Pals says X, existing entry says Y]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2023-08-29'
  title: How to use Automatic Attack Disruption in Microsoft 365 Defender (BEC, AiTM
    &amp; HumOR)
  url: https://jeffreyappel.nl/how-to-use-automatic-attack-disruption-in-microsoft-365-defender-bec-aitm-humor
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2023-05-03'
  title: How works Microsoft Defender Threat Intelligence / Defender TI - and what
    is the difference between free and paid
  url: https://jeffreyappel.nl/how-works-microsoft-defender-threat-intelligence-defender-ti-and-what-is-the-difference-between-free-and-paid
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-04-21'
  title: MFA prompt spamming/ MFA fatigue - What can you do to prevent/ detect attacks?
  url: https://jeffreyappel.nl/mfa-prompt-spamming-mfa-fatigue-what-can-you-do-to-prevent-detect-attacks
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-08-08'
  title: Protect against AiTM/ MFA phishing attacks using Microsoft technology
  url: https://jeffreyappel.nl/protect-against-aitm-mfa-phishing-attacks-using-microsoft-technology
- author: Bert-Jan Pals
  crawled: '2026-04-12'
  date: ''
  title: KQL Cafe - February 2023
  url: https://kqlcafe.com/shownotes/2023/KQL%20Cafe%20-%20February%202023
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-08-31'
  title: Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue,
    PRT, OAuth)
  url: https://jeffreyappel.nl/tips-for-preventing-against-new-modern-identity-attacks-aitm-mfa-fatigue-prt-oauth
stale_after: '2026-05-27'
title: AiTM Proxy Attacks and Defence
topic: identity/conditional-access/aitm-defence
---

# AiTM Proxy Attacks and Defence

## AiTM Proxy Attacks and Defense

### Overview
AiTM (Adversary-in-the-Middle) proxy attacks are sophisticated cyberattacks where an attacker intercepts and manipulates communication between two parties, often for the purpose of stealing sensitive information or gaining unauthorized access. Microsoft's Automatic Attack Disruption feature aims to counter these attacks by using correlated insights from the Microsoft 365 ecosystem and AI models to stop such attacks while they are in progress.

[CONFLICT: Jeffrey mentions MFA prompt spamming/ MFA fatigue, but does not provide information about AiTM proxy attacks.]

### Key Concepts
- AiTM (Adversary-in-the-Middle) proxy attacks: Techniques used by attackers to intercept and manipulate communication between two parties. [CONFLICT: Jeffrey mentions MFA prompt spamming/ MFA fatigue, but does not provide information about AiTM proxy attacks.]
- Automatic Attack Disruption: Microsoft's feature that uses AI models and correlated insights from the Microsoft 365 ecosystem to stop AiTM attacks in progress.
- XDR (Extended Detection and Response): Microsoft's security solution that correlates signals from multiple products to identify advanced attacks.
- High-fidelity alerts: Alerts with a high level of confidence that an attack is taking place.

### Configuration
1. Ensure all prerequisites for Automatic Attack Disruption are correctly enabled and configured. The feature is built-in and does not require additional setup.
2. Monitor high-fidelity alerts for signs of AiTM proxy attacks.
3. When an AiTM attack is detected, Microsoft 365 Defender XDR will disrupt the attack by containing the assets that the attacker is using via the attack disruption capability.

### Common Pitfalls
- False positives: Misidentifying regular network activity as an AiTM proxy attack. This can be mitigated by calculating high-fidelity attacks to avoid false positives.
- Incomplete configuration: Failing to correctly enable and configure all prerequisites for Automatic Attack Disruption.

### Tips for preventing against new modern identity attacks (AiTM, MFA Fatigue, PRT, OAuth)
[New Information]
- MFA prompt spamming/ MFA fatigue: A technique where attackers send multiple authentication prompts to a user in an attempt to overwhelm them and gain access. This can be mitigated by implementing multi-factor authentication (MFA) best practices, such as using app passwords, conditional access policies, and education about phishing attempts.

### KQL / PowerShell
[The article does not provide any relevant queries or scripts specific to AiTM proxy attacks.]

### Related Topics
- AiTM (Adversary-in-the-Middle)
- evilginx
- adversary-in-the-middle
- session cookie
- token replay
- MFA prompt spamming/ MFA fatigue

## Microsoft Defender Threat Intelligence

Microsoft Defender Threat Intelligence (MDTI), previously known as RiskIQ, brings threat Intelligence data together from multiple sources. It is available in a free community version and paid version. MDTI can act as a standalone product and allows the option for ingesting TI data into Microsoft Sentinel or Microsoft 365 Defender.

[CONFLICT: Jeffrey's article mentions MDTI, but does not provide any new information about AiTM proxy attacks.]

### Related Topics
- Microsoft Defender Threat Intelligence (MDTI)
- RiskIQ
- threat intelligence (TI)
- Microsoft Sentinel
- Microsoft 365 Defender