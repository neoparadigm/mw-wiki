---
conflicts:
- '[CONFLICT: Jeffrey mentions browser extensions, but this topic does not directly
  relate to Azure AD]'
- '[CONFLICT: Jeffrey mentions phishing attacks related to browser extensions, but
  this topic does not directly relate to Azure AD]'
- '[CONFLICT: Jeffrey mentions browser extensions, but this topic is not directly
  related to the existing entry]'
- '[CONFLICT: Jeffrey mentions phishing attacks related to AzureAD OAuth Consent phishing
  attempts, which is a more specific type of attack]'
- '[CONFLICT: The existing entry mentions browser extensions, but this topic does
  not directly relate to Azure AD]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-06-07'
  title: Controle op Azure AD machtigingen met de Admin consent workflow; zo werkt
    het
  url: https://jeffreyappel.nl/controle-op-azure-ad-machtigingen-met-de-admin-consent-workflow-zo-werkt-het
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2025-01-05'
  title: How to check and block &quot;malicious&quot; browser extensions with Microsoft
    Defender and Intune?
  url: https://jeffreyappel.nl/how-to-check-and-block-malicious-browser-extension-with-microsoft-defender-and-intune
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2022-02-02'
  title: Protect against AzureAD OAuth Consent phishing attempts (Illicit consent
    attack)
  url: https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack
stale_after: '2026-06-11'
title: Admin Consent Workflow and OAuth App Control
topic: identity/entra-id/admin-consent-workflow
---

# Admin Consent Workflow and OAuth App Control

## Overview
The Admin Consent Workflow and OAuth App Control is a crucial aspect of securing Azure Active Directory (Azure AD) permissions by preventing unwanted permissions before it's too late. This topic matters because as more applications are connected via the cloud, it becomes essential to ensure that the single identity associated with these apps is securely managed.

## Key Concepts
- Admin Consent Workflow
- OAuth App Control
- Preventing unauthorized access and data breaches
- Phishing attacks targeting app permissions [CONFLICT: Jeffrey mentions phishing attacks related to AzureAD OAuth Consent phishing attempts, which is a more specific type of attack]
- [CONFLICT: The existing entry mentions browser extensions, but this topic does not directly relate to Azure AD]

## Configuration
1. Navigate to Azure Active Directory > App registrations > Enterprise applications
2. Select the application for which you want to manage permissions
3. Go to API permissions > Add a permission > Application permissions
4. Choose the appropriate permissions based on your requirements
5. Grant admin consent for the selected permissions

## Common Pitfalls
- Lack of control over app permissions can lead to data breaches and unauthorized access
- Phishing attacks can exploit OAuth apps to gain access to sensitive organizational data [Updated with more specific type of attack: AzureAD OAuth Consent phishing attempts]

## Related Topics
- Admin Consent
- User Consent
- OAuth App
- Consent Phishing
- App Permissions
- AzureAD OAuth Consent phishing attempts (Illicit consent attack) [Added new topic based on the new source]
- [CONFLICT: Jeffrey mentions browser extensions, but this topic is not directly related to the existing entry]

New source article: "How to check and block 'malicious' browser extensions with Microsoft Defender and Intune?"
Author: Jeffrey
New source content: [Not applicable as it does not relate to Azure AD]

New source article: "Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)"
Author: Jeffrey
New source content: [Added new section based on the new source]

## Blog Post

> [Security](https://jeffreyappel.nl/category/security/) > Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)

[Security](https://jeffreyappel.nl/category/security/)

# Protect against AzureAD OAuth Consent phishing attempts (Illicit consent attack)

[Jeffrey](https://jeffreyappel.nl/author/contact/),
[February 2, 2022](https://jeffreyappel.nl/protect-against-oauth-consent-phishing-attempts-illicit-consent-attack/)
1


10 min read

**In the last couple of months, there is a large increase visible in consent phishing emails ([illicit consent attacks](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/detect-and-remediate-illicit-consent-grants?view=o365-worldwide)). Microsoft threat analysts are tracking a continued increase in consent phishing attempts/mails. This blog described some of the Microsoft prevention/detection capabilities against OAuth Consent phishing.**

## What is consent phishing?

Consent phishing attacks (Illicit consent attacks) abuse legitimate cloud service providers, including Microsoft, Meta, Google, and others that use OAuth 2.0 authorization. OAuth 2.0 is a widely used protocol that allows third-party apps to access account details and perform an action on their behalf.

The main goal of a consent phishing attack is to let users grant permissions (content) to apps that are owned by the malicious attacker. The attacker then tricks an end-user into granting that application consent to access their data.

The difference in comparison with a credential attack is that the user uses a valid identity provider and no fake landing page for sign-in or any other method for credential harvesting. In a consent phishing attack, the user sign-in takes place on the identity provider itself. Targeted users who grant the permissions allow attackers to make API on their behalf through the OAuth 2.0 protocol.

## How does Microsoft protect against AzureAD OAuth Consent Phishing?

Microsoft has several built-in protections to help prevent and detect illicit consent attacks:

1. **Azure AD Identity Protection**: This service uses machine learning to identify risky sign-ins, suspicious user activities, and leaked credentials. It can also automatically block risky sign-ins and notify admins about potential threats.

2. **Microsoft Defender for Identity (MDI)**: MDI provides advanced threat protection by using behavioral analytics to detect anomalous activities in your Azure AD environment. It can help identify and investigate illicit consent attacks, as well as other types of threats.

3. **Azure AD Conditional Access policies**: Admins can use conditional access policies to require multi-factor authentication (MFA) for users who are trying to grant permissions to apps that have been flagged as risky or suspicious. This helps ensure that only authorized users can consent to app permissions.

4. **Microsoft Defender for Endpoint (MDE)**: MDE provides endpoint protection by using AI and machine learning to detect and respond to threats in real-time. It can help protect against malware, ransomware, and other types of attacks that may be used in conjunction with illicit consent attacks.

5. **Azure AD App Registration Firewall**: This feature allows admins to control which IP addresses can access their app registrations, helping prevent unauthorized access from known malicious sources.

By using these protections together, organizations can significantly reduce the risk of falling victim to illicit consent attacks and other types of threats that target Azure AD OAuth apps.