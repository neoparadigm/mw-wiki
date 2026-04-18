---
conflict_topics:
- intune/security/defender-for-endpoint-intune
- intune/security/windows-security-baseline
conflicts:
- '[CONFLICT: Anoop C Nair does not mention WDAC in this article, but it is a key
  concept in the existing entry]'
- '[CONFLICT: Anoop C Nair does not provide specific configuration steps in this article]'
- '[CONFLICT: jsuther1974 says X, existing entry says Y]'
- '[CONFLICT: The existing entry does not mention Smart App Control]'
- '[CONFLICT: The existing entry does not provide details about trust levels or how
  Smart App Control determines whether an app is trusted]'
- '[CONFLICT: The existing entry does not mention this feature]'
- '[CONFLICT: The new source does not provide additional information about this concept]'
context_note: Wdac App Control is part of the intune domain. Synthesised from 3 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-07-10'
  title: Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/downloads-blokkeren-via-conditional-access-app-control
- author: Jeffrey
  crawled: '2026-04-18'
  date: '2020-07-10'
  title: Downloads blokkeren via Conditional Access App Control vanuit Microsoft Endpoint
    Manager
  url: https://jeffreyappel.nl/downloads-blokkeren-via-conditional-access-app-control/amp
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2026-04-06'
  title: Windows 11 April 2026 Update Introduces Smart App Control Without Reinstallation
    HTMD Blog
  url: https://www.anoopcnair.com/windows-11-april-2026-update-smart-app-control
- author: jsuther1974
  crawled: '2026-04-18'
  date: '2026-03-29'
  title: Application Control for Windows
  url: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol
- author: jsuther1974
  crawled: '2026-04-18'
  date: '2026-03-29'
  title: Application Control for Windows
  url: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac
stale_after: '2026-06-17'
title: WDAC and App Control for Business
topic: intune/security/wdac-app-control
---

# WDAC and App Control for Business

WDAC (Windows Defender Application Control) and App Control are security features in Microsoft Endpoint Manager that allow administrators to control which applications can run on devices within their organization, enhancing security by preventing unauthorized or potentially harmful software from executing.

## Key Concepts
- WDAC: A feature of Windows Defender that enforces a whitelist of approved applications and blocks all other executables from running. [CONFLICT: Anoop C Nair does not mention WDAC in this article, but it is a key concept in the existing entry]
- App Control: An extension of WDAC that allows for more granular control over application execution, including the ability to create allow lists and exceptions.
- Code Integrity: The process of ensuring that code running on a device has not been tampered with or compromised.
- Allow List: A list of approved applications that are allowed to run on a device.

## New Information from the new source:
- Windows 11 April 2026 Update introduces Smart App Control, which no longer requires reinstalling Windows to manage it. [CONFLICT: The existing entry does not mention Smart App Control]
- Smart App Control is accessible through the Windows Security app and allows only trusted apps to run, blocking untrusted ones. [CONFLICT: The existing entry does not provide details about trust levels or how Smart App Control determines whether an app is trusted]
- You can now turn Smart App Control on or off. [CONFLICT: The existing entry does not mention this feature]

## Configuration
1. In the Microsoft Endpoint Manager admin center, navigate to **Devices > Windows > App control policies**.
2. Click **Create** to create a new policy.
3. Choose the platform (Windows 10 or later) and select the scope (e.g., all devices or a specific group).
4. Configure the rules for the policy, including the allow list and any exceptions.
5. Assign the policy to the appropriate groups of devices.
6. Deploy the policy to the devices. [CONFLICT: Anoop C Nair does not provide specific configuration steps in this article]

## Microsoft Cloud App Security (MCAS)
Microsoft Cloud App Security is a Cloud App Security Broker (CASB) that provides a standard set of configurations, templates, and possibilities for integration with Microsoft products and online services. It allows for the blocking of downloads via Conditional Access/Conditional Access App Control during user sessions.

### Conditional Access App Control
Conditional Access App Control enables the routing of user sessions through a reverse proxy, allowing for specific actions such as download blocking during a session. [CONFLICT: The new source does not provide additional information about this concept]

## Return the complete updated wiki entry body (without frontmatter).
# WDAC and App Control for Business

WDAC (Windows Defender Application Control) and App Control are security features in Microsoft Endpoint Manager that allow adminis

New source article: "Application Control for Windows"
Author: jsuther1974
New source content:
# Application Control for Windows

- Applies to: ✅ [Windows 11](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows 10](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client), ✅ [Windows Server 2025](https://learn.microsoft.com/windows/release-health/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows/release-health/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows/release-health/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows/release-health/windows-server-release-info)

Feedback

Summarize this article for me

Note

Some capabilities of App Control for Business are only available on specific Windows versions. Learn more about [App Control feature availability](feature-availability).

Your organization's data is one of its most valuable assets... and adversaries want it. No matter what security controls you apply over your data, there are no controls to fully protect your most vulnerable target: the trusted user sitting at the keyboard. When a user runs a process, that process shares the same access to your data that the user has. So your sensitive information is easily transmitted, modified, deleted, or encrypted when a user, intentionally or not, runs malicious software. And with thousands of new malicious files created every day, relying solely on traditional methods like antivirus (AV) solutions gives you an inadequate defense against new attacks.

Application control changes Windows from a place where all code runs unless your AV solution confidently predicts it's bad, to one where code runs only if your policy says so. The cyber threats you face change rapidly, and your defenses need to change too. Government and security organizations, like the Australian Signals Directorate, frequently cite application control as one of the most effective ways to address the threat of executable file-based malware (.exe, .dll, etc.). It works alongside your AV solution to help mitigate security threats by restricting the apps that users can run and even what code runs in the System Core (kernel).

Important

Although application control can significantly harden your computers against malicious code, it's not a replacement for antivirus. You should continue 

Task: Update the wiki entry by:
1. Adding any NEW information from the new source not already present
2. Marking any CONFLICTS between sources with [CONFLICT: jsuther1974 says X, existing entry says Y]
3. Improving or expanding existing sections if the new source adds depth
4. NOT duplicating content already present
5. NOT removing existing content

Return the complete updated wiki entry body (without frontmatter).
If the new source adds nothing new, return the existing entry unchanged.