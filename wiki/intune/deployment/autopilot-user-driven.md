---
conflicts:
- '[CONFLICT: Ugur Koc mentions potential challenges with Homebrew]'
- '[CONFLICT: Ugur Koc mentions potential challenges with Homebrew and Enroll Ubuntu
  24.04 into Intune]'
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2024-11-19'
  title: Git Fundamentals for Cloud Admins
  url: https://danielchronlund.com/2024/11/19/git-fundamentals-for-cloud-admins
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-01-09'
  title: Block Homebrew on MacOS with Intune - Ugur Koc
  url: https://ugurkoc.de/block-homebrew-on-macos-with-intune
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-12-16'
  title: Enroll Ubuntu 24.04 into Intune - Ugur Koc
  url: https://ugurkoc.de/enroll-ubuntu-24-04-into-intune
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-07-24'
  title: From Intune to EntraID - Add custom data to the Extension Attributes - Ugur
    Koc
  url: https://ugurkoc.de/from-intune-to-entraid-add-custom-data-to-the-extension-attributes
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2024-10-13'
  title: 'The macOS Sequoia Aftermath: What Happened and How Can We Prevent Similar
    Issues? - Ugur Koc'
  url: https://ugurkoc.de/the-macos-sequoia-aftermath-what-happened-and-how-can-we-prevent-similar-issues
stale_after: '2026-06-11'
title: Autopilot User-Driven Mode
topic: intune/deployment/autopilot-user-driven
---

# Autopilot User-Driven Mode

## Autopilot User-Driven Mode

Autopilot User-Driven Mode is a configuration in Microsoft Endpoint Manager (MEM) that allows users to perform self-service actions within the scope of predefined policies, enhancing user productivity and reducing IT intervention. This topic matters as it empowers end-users to manage their devices while maintaining compliance with organizational policies.

## Key Concepts
- User-Driven Mode
- Self-Service Actions
- Policy Scope
- Compliance Enforcement
- Homebrew (MacOS) [New information from Ugur Koc]
  - Implications of Homebrew: When software is installed using Homebrew on MacOS, it is typically installed in user context, not system context. This can lead to conflicts with organizational patch management and vulnerability reporting. [New information from Ugur Koc]
- Enroll Ubuntu 24.04 into Intune - Ugur Koc
- Extension Attributes (New information from Ugur Koc's "From Intune to EntraID - Add custom data to the Extension Attributes")

## Configuration
1. Navigate to the Endpoint Manager admin center.
2. Go to Devices > Windows > Troubleshooter > Autopilot Deployment Profiles.
3. Create a new profile or edit an existing one, and enable User-Driven Mode.
4. Define the self-service actions available within the policy scope.
5. Assign the profile to target devices.

## Common Pitfalls
- Incorrectly defining the policy scope may result in users performing unauthorized actions. [CONFLICT: Ugur Koc mentions potential challenges with Homebrew and Enroll Ubuntu 24.04 into Intune]
- Lack of proper testing can lead to unexpected behavior or user frustration.
- Insufficient communication with end-users about available self-service options may cause confusion.
- Failure to write custom data to Extension Attributes for devices in EntraID might result in difficulty tracking and managing devices (from Ugur Koc's "From Intune to EntraID - Add custom data to the Extension Attributes")

## Homebrew (MacOS)
[New information from Ugur Koc]
Homebrew for MacOS is a popular tool that simplifies software installation, often bypassing local privileges and ignoring application management. It can be installed using commands in the Terminal. Upon running a script to block Homebrew, the installation process may encounter permission issues or alias execution problems.

## Enroll Ubuntu 24.04 into Intune - Ugur Koc
Enroll Ubuntu 24.04 into Intune - Ugur Koc
Microsoft Intune supports managing Ubuntu Linux devices, including the latest Ubuntu 24.04. Enrolling these devices provides a more comprehensive view of all devices within your organization. This journey begins by using Intune to register them in Entra ID, ensuring better management and integration.

## The macOS Sequoia Aftermath: What Happened and How Can We Prevent Similar Issues? - Ugur Koc
[New source content]
It’s Tuesday the 17th of September – a frosty morning. I wake up early, ready to start the day. The smell of my Americano with oat milk fills the air as I sip slowly, preparing for my first meeting. The day is off to a good start. Naturally, I check Intune to see how many people have already installed MacOS Sequoia, which was only released to the public yesterday.
Before I can even finish my coffee, a ping on Teams interrupts my moment of calm: *“I’m having issues opening websites in Safari,”* a colleague reports.
Coffee in hand, I pause and then jump into action.
I open Edge, curious. A quick look at X and Reddit confirms it: I’m not alone. Users are reporting DNS errors, VPN connection issues, and a ton of other strange problems. There’s one common link – they’re all on macOS Sequoia. This was a serious problem, as users across different environments were experiencing similar connectivity issues.
Don’t get me wrong – I love Day Zero Support when it works. If the features are solid, it’s a win-win for everyone. But being part of the AppleSeed program means you’re supposed to give feedback. And this time, we did. There were reports during beta testing – Beta 5, in particular – that highlighted severe issues: internet connectivity dropping, third-party security software malfunctioning (likely due to network filter clashes), and VPN connections failing altogether.
Apple was aware of the issue but perhaps underestimated its extent or impact.
So, here’s where we stand. There’s still no official statement from Apple, and we’re left with questions.
What went wrong? Could it have been prevented? And most importantly – how do we avoid finding ourselves in this position again? Let’s try to break it down.
Before we dive into the details, here’s a quick recommendation: if you’re interested in learning more about managing macOS devices with Intune, I highly recommend visiting [IntuneMacAdmins.com](https://IntuneMacAdmins.com). It’s a comprehensive resource for IT professionals looking to manage macOS devices using Microsoft Endpoint Manager (MEM) and other tools.