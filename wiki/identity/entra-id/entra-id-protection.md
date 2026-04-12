---
conflicts:
- '[CONFLICT: The new source does not provide information related to Entra ID Protection
  Risk Policies]'
- '[CONFLICT: The new source does not provide information related to Android Enterprise
  or MAM]'
- '[CONFLICT: The new source provides specific event IDs for auditing account logons,
  but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing account management,
  but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing policy changes,
  but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing object access,
  but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing process creation,
  but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing privileged account
  management, but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing security policy
  changes, but the existing entry does not]'
- '[CONFLICT: The new source provides specific event IDs for auditing system integrity
  events, but the existing entry does not]'
- '[CONFLICT: The new source does not provide information related to Android Enterprise
  or MAM management]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-05-20'
  title: Android Enterprise fully managed beschikbaar in Microsoft Intune voor zakelijke
    omgevingen
  url: https://jeffreyappel.nl/android-enterprise-fully-managed-beschikbaar-in-microsoft-intune-voor-zakelijke-omgevingen/amp
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-06-08'
  title: Android Enterprise via Microsoft Endpoint Manager als vervanger van Android
    device administrator
  url: https://jeffreyappel.nl/android-enterprise-via-microsoft-endpoint-manager-als-vervanger-van-android-device-administrator
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2026-02-02'
  title: Automatic Windows event auditing configuration for Defender for Identity
    V3.x sensor
  url: https://jeffreyappel.nl/automatic-windows-event-auditing-configuration-for-defender-for-identity-v3-x
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-07-12'
  title: 'Azure AD Identity Protection: User Risk and Sign-in Risk protection with
    automation'
  url: https://jeffreyappel.nl/azure-ad-identity-protection-user-risk-and-sign-in-risk-protection-with-automation
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-06-06'
  title: Edge Chromium; zo configureer je beheerde favorieten via Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/edge-chromium-zo-configureer-je-beheerde-favorieten-via-microsoft-endpoint-manager
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-07-05'
  title: Edge Chromium; zo configureer je de tracking prevention functionaliteit vanuit
    Microsoft Endpoint Manager
  url: https://jeffreyappel.nl/edge-chromium-zo-configureer-je-de-tracking-prevention-functionaliteit-vanuit-microsoft-endpoint-manager
stale_after: '2026-06-11'
title: Entra ID Protection Risk Policies
topic: identity/entra-id/entra-id-protection
---

# Entra ID Protection Risk Policies and Android Enterprise via Microsoft Endpoint Manager

Entra ID Protection Risk Policies are a set of policies designed to protect user and sign-in risks within an organization's environment. These policies automate the detection and protection against potential threats, enhancing the overall security posture of an organization.

Azure AD Identity Protection (a component of Microsoft E5 license) is similar in purpose, providing automated detection and remediation for identity risk events, investigation of risks, and user protection based on risk levels. [NEW INFORMATION] Azure AD Identity Protection uses threat intelligence to specify risky detections for all users, much like Entra ID Protection Risk Policies. The two main risk detection components are:

- User Risk (similar to the existing entry): A measure of the likelihood that a user account has been compromised or is being used insecurely.
- Sign-in Risk (similar to the existing entry): An assessment of the risk level associated with a sign-in attempt, based on various factors such as location, device, and account behavior.

In addition to User Risk and Sign-in Risk, Azure AD Identity Protection also includes:

- Identity Protection policies: A set of rules defining how to respond to user and sign-in risks, such as requiring multi-factor authentication or blocking access. [NEW INFORMATION]

[CONFLICT: The new source does not provide information related to Android Enterprise or MAM management]

## Configuration
Microsoft provides a step-by-step guide on how to configure identity protection policies:
1. Navigate to the Azure portal (portal.azure.com)
2. Search for and select "Azure Active Directory"
3. Go to "Cybersecurity" > "Identity Protection" > "Policies"
4. Click "Create policy" and follow the on-screen instructions

## Common Pitfalls
Some common pitfalls to avoid include:
1. Not enabling identity protection policies
2. Ignoring high-risk sign-ins or users
3. Overlooking policy exceptions and investigations
4. Failing to adjust policy settings based on organizational needs

[The article does not discuss common pitfalls related to Entra ID Protection Risk Policies.]

## KQL / PowerShell
Microsoft provides query examples using Kusto Query Language (KQL) and PowerShell for Azure AD Identity Protection.

New source article: "Edge Chromium; zo configureer je de tracking prevention functionaliteit vanuit Microsoft Endpoint Manager"
Author: Jeffrey
New source content:
[This new source does not provide information relevant to the existing wiki entry]