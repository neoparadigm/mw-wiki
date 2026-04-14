---
conflicts:
- '[CONFLICT: The new source provides an additional method (Conditional Access App
  Control) for blocking downloads, which is not mentioned in the existing entry.]'
- '[CONFLICT: The new source discusses Microsoft Azure''s Trusted Signing service,
  which is not directly related to WDAC and App Control for Business in the context
  of this wiki entry.]'
- '[CONFLICT: New source introduces this concept]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2020-07-10'
  title: Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/downloads-blokkeren-via-conditional-access-app-control
- author: Jeffrey
  crawled: '2026-04-14'
  date: '2020-07-10'
  title: Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/downloads-blokkeren-via-conditional-access-app-control/amp
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2025-03-25'
  title: 'Microsoft Azure – Secure your Code with Trusted Signing: A Practical Guide
    – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/microsoft-azure-secure-your-code-with-trusted-signing-a-practical-guide
- author: Anoop C Nair
  crawled: '2026-04-14'
  date: '2026-04-06'
  title: Windows 11 April 2026 Update Introduces Smart App Control Without Reinstallation
    HTMD Blog
  url: https://www.anoopcnair.com/windows-11-april-2026-update-smart-app-control
stale_after: '2026-06-13'
title: WDAC and App Control for Business
topic: intune/security/wdac-app-control
---

# WDAC and App Control for Business

## WDAC and App Control for Business

WDAC (Windows Defender Application Control) and App Control is a security feature in Microsoft Endpoint Manager that allows administrators to control which applications can run on devices within their organization. This topic matters because it helps organizations maintain security and compliance by preventing unauthorized or potentially harmful applications from running.

## Key Concepts
- WDAC (Windows Defender Application Control)
- App Control
- Code Integrity Policy
- Allow List
- Deny List
- Smart App Control [CONFLICT: New source introduces this concept]

## Configuration
1. In the Microsoft Endpoint Manager admin center, navigate to **Devices** > **Configuration profiles** > **Templates library**.
2. Search for "Application control" and select the template named "Windows Defender Application Control - Code Integrity Policy".
3. Click on **Create profile**, choose the platform (Windows 10 or later), and give the profile a name.
4. Under **Configuration settings**, configure the policy as needed, such as adding applications to the allow list or deny list. This can also be done using Conditional Access App Control, as detailed in [Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint Manager](#downloads-blokkeren-via-conditional-access-app-control-vanuit-microsoft-endpoint-manager).
5. Deploy the profile to the appropriate groups of devices.
6. [New information] With the Windows 11 April 2026 Update, Smart App Control can be managed without reinstalling the operating system. It is accessible through the Windows Security app and allows only trusted apps to run while blocking untrusted ones. You can turn Smart App Control on or off.

## Common Pitfalls
- Not testing the policy thoroughly before deploying it to production devices.
- Forgetting to update the allow and deny lists when new applications are added or removed from the organization.
- Failing to properly configure exceptions for necessary but potentially risky applications.
- [New information] Neglecting to enable Smart App Control after the Windows 11 April 2026 Update.

## KQL / PowerShell
[This article does not provide any relevant queries or scripts]

## Related Topics
- [WDAC](wiki:WDAC)
- [App Control](wiki:App_Control)
- [Application control](wiki:Application_control)
- [Code integrity](wiki:Code_integrity)
- [Allow list](wiki:Allow_list)
- [Conditional Access App Control](wiki:Conditional_Access_App_Control)
- [Smart App Control](#smart-app-control)

## Additional Information from New Source
- [Microsoft Azure – Secure your Code with Trusted Signing: A Practical Guide](#microsoft-azure---secure-your-code-with-trusted-signing-a-practical-guide)
  - Introduction
    - What is the Trusted Signing Service?
    - Key features of Trusted Signing
    - Benefits of Microsoft Trusted Signing
  - Structure of the service
    - SKU (Pricing tier) overview
    - Trust models
      - Public Trust Model
      - Private Trust Model
- [Windows 11 April 2026 Update Introduces Smart App Control Without Reinstallation HTMD Blog](#windows-11-april-2026-update-introduces-smart-app-control-without-reinstallation-htmd-blog)
  - Key Takeaways
    - Smart App Control no longer requires reinstalling Windows to manage it.
    - It is accessible through the Windows Security app.
    - The feature allows only trusted apps to run, blocking untrusted ones.
    - You can now turn Smart App Control on or off.