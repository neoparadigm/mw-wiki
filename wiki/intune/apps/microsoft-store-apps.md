---
conflict_topics:
- intune/apps/powershell-scripts
- identity/pim/break-glass-accounts
conflicts:
- '[CONFLICT: Anoop C Nair says this method aligns well with Windows Autopilot and
  Speech Packs for language management, existing entry does not mention this.]'
- '[CONFLICT: Anoop C Nair''s blog post provides a detailed guide on deploying Natural
  Voice Packs to Windows 11 using Intune. The existing entry does not include this
  information.]'
context_note: Microsoft Store Apps is part of the intune domain. Synthesised from
  4 community sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-06-06'
  title: How To Configure App Data Sharing Using SharedLocal Folder In Windows 10
    With Intune Policy HTMD Blog
  url: https://www.anoopcnair.com/app-data-sharing-folder-in-windows-10-intune
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-05-22'
  title: Best Guide To Deploy And Update Visual Studio Code Using Intune HTMD Blog
  url: https://www.anoopcnair.com/deploy-visual-studio-code-using-intune
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-03-11'
  title: Easy Method To Install Speech Pack Using Microsoft Intune HTMD Blog
  url: https://www.anoopcnair.com/install-speech-pack-using-microsoft-intune
- author: Anoop C Nair
  crawled: '2026-04-18'
  date: '2025-05-08'
  title: Simple Method To Deploy Natural Voice Pack To Windows 11 Using Intune HTMD
    Blog
  url: https://www.anoopcnair.com/natural-voice-pack-to-windows-11-using-intune
stale_after: '2026-06-02'
title: Microsoft Store App Deployment
topic: intune/apps/microsoft-store-apps
---

# Microsoft Store App Deployment and Visual Studio Code Deployment using Intune

## Microsoft Store App Deployment

### Overview
This topic discusses how to configure app data sharing using the SharedLocal folder in Windows 10 with Intune Policy for Microsoft Store apps, as well as a guide on deploying and updating Visual Studio Code using the new Microsoft Store method. This policy is crucial for managing shared and personal content on a device, especially in environments where multiple users share a single device, such as offices or schools.

### Key Concepts
- Shared Local folder
- Windows Storage API
- Enabling/disabling app data sharing
- Intune Policy deployment
- CSP (Configuration Service Provider) details
- OMA-URI for configuring the policy
- Visual Studio Code features and benefits
- Speech Packs (New Source)
- Natural Voice Pack (New Source)

### Configuration
To configure app data sharing using the SharedLocal folder in Windows 10 with Intune Policy:

1. Sign in to Microsoft Intune.
2. Go to Devices > Configuration.
3. Click Create and then new policy.
4. Choose the platform as Windows 10 and later.
5. For Profile type, select Templates and then choose Custom.
6. Provide a Name – e.g., “Shared User App Data.”
7. Add a Description if needed.
8. Click on + Add under OMA-URI Settings to configure the specific setting.
   - Enter a name for this setting, such as Shared User App Data.
   - Briefly describe the setting, e.g., “Allow Shared User App Data microsoft store app.”
   - Enter the following OMA-URI path: ./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowSharedUserAppData
   - Set the Data type to Integer.
     - Enter the value:
       - 1 to enable the administrator account.
       - 0 to disable the administrator account.
9. After entering the above details, click Save.

### Best Guide To Deploy And Update Visual Studio Code Using Intune

In this section, we’ll learn how to deploy and update **Visual Studio Code** using **Intune Microsoft Store app (new)** method. The new Microsoft Store version of Visual Studio Code **(VS Code)** offers a modern, streamlined experience for Windows users, especially in enterprise environments.

Distributed through the Microsoft Store as a **Win32 app using MSIX packaging**, it ensures **better security**, **auto-updates**, and **system integration**, making it an ideal choice for organizations standardizing app deployments across managed devices.

With **Microsoft Intune**, deploying this **Store-based VS Code** is now **simpler** and **more efficient**. Intune supports the integration with the Microsoft Store (new), allowing IT admins to search, add, and assign [VS Code](https://www.anoopcnair.com/visual-studio-code-installation-using-intune/) directly to users or devices. This eliminates the need for packaging or scripting custom installers, reducing deployment time and errors.

Additionally, the Store version aligns well with **[Windows Autopilot](https://www.anoopcnair.com/windows-autopilot-next-generation-with-i)** for seamless device provisioning and app deployment.

### Simple Method To Deploy Natural Voice Pack To Windows 11 Using Intune HTMD Blog

In this blog post, I’ll be explaining how to deploy **Natural Voice Pack** to **Windows 11** using **Microsoft Intune**. With the **Microsoft Intune Store app (new)** deployment capability, IT admins can easily deliver Natural Voice packages to Windows 11 devices directly from the Microsoft Store.

This modern method **streamlines** app deployment by allowing you to search and assign Store apps, including voice packages, without needing to package or script them manually. Natural Voice features, like Microsoft **Aria**, **Jenny** or **Guy** voices, are available in the Microsoft Store as standalone apps.

This approach ensures a more reliable and **manageable deployment** experience, especially at scale. Combined with compliance policies or accessibility profiles, Intune can ensure users have the required voice assets for accessibility tools, reading aloud, or immersive reader features, improving overall productivity and inclusivity.

Natural Voice Packs are essential in Windows 11 to provide a more **human-like**, expressive, and intelligible **text-to-speech (TTS)** experience. These enhanced voices offer significant improvements over traditional robotic-sounding voices, making spoken content more engaging and easier to understand, especially for users who rely on **screen readers** or **narration tools**.

[CONFLICT: Anoop C Nair's blog post provides a detailed guide on deploying Natural Voice Packs to Windows 11 using Intune. The existing entry does not include this information.]