---
conflicts:
- '[CONFLICT: Jeffrey says that TAP makes recovery easier when a user loses or forgets
  their strong Passwordless authentication, while the existing entry does not mention
  this.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2024-08-08'
  title: Simplifying Entra ID Temporary Access Pass Creation with PowerShell
  url: https://danielchronlund.com/2024/08/08/simplifying-entra-id-temporary-access-pass-creation-with-powershell
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2020-07-08'
  title: Apps vanuit Cloud App Security blokkeren via Microsoft Defender ATP + Microsoft
    Endpoint Manager
  url: https://jeffreyappel.nl/apps-vanuit-cloud-app-security-blokkeren-via-microsoft-defender-atp-microsoft-endpoint-manager
- author: Jeffrey
  crawled: '2026-04-12'
  date: '2021-02-16'
  title: Go fully passwordless with the new Azure AD Temporary Access Pass feature
  url: https://jeffreyappel.nl/go-fully-passwordless-with-the-new-azure-ad-temporary-access-pass-feature
- author: Jan Bakker
  crawled: '2026-04-12'
  date: '2026-01-25'
  title: Least privilege for Temporary Access Pass creation
  url: https://janbakker.tech/least-privilege-for-temporary-access-pass-creation
- author: Jan Bakker
  crawled: '2026-04-12'
  date: '2026-02-06'
  title: The hidden risk of using aka.ms shortURLs for Microsoft portals
  url: https://janbakker.tech/the-hidden-risk-of-using-aka-ms-shorturls-for-microsoft-portals
stale_after: '2026-06-11'
title: MFA Registration Policy and TAP
topic: identity/entra-id/mfa-registration-policy
---

# MFA Registration Policy and TAP, and Apps Blocking via Microsoft Defender ATP + Microsoft Endpoint Manager

This topic focuses on configuring Multi-Factor Authentication (MFA) registration policies and Temporary Access Passes (TAPs) in Microsoft Entra ID, using PowerShell for streamlined management. It also covers the process of blocking apps from Cloud App Security via Microsoft Defender ATP + Microsoft Endpoint Manager.

## Key Concepts
- MFA Registration Policy
- Temporary Access Pass (TAP)
- PowerShell Scripting
- Microsoft Graph API
- Shadow IT Discovery
- Microsoft Cloud App Security
- Microsoft Defender ATP
- Microsoft Endpoint Manager
- Azure AD Temporary Access Pass feature
- [New Information] The potential risks associated with using aka.ms short URLs for Microsoft portals, as discussed in the article "The hidden risk of using aka.ms shortURLs for Microsoft portals" by Jan Bakker.

## Configuration
1. Set up the environment by connecting to Graph and installing necessary PowerShell modules for MFA registration policy and TAP management.
2. Retrieve a list of users, present them in a grid view for selection, and choose the desired user.
3. Generate a list of dates for the next 30 days, select the start date for the TAP.
4. Provide a list of hours in the day to specify when the TAP should start.
5. Specify the TAP duration in hours (between 1 and 8), which is then converted to minutes.
6. Choose whether the TAP can be used only once.
7. Create the TAP using the PowerShell script with all parameters set.
8. Configure Microsoft Endpoint Manager to block apps from Cloud App Security via Microsoft Defender ATP.
9. Introduce the new Azure AD Temporary Access Pass feature, which allows for configuring a temporary password for users and enrolling passwordless authentication methods (FIDO2, Passwordless Phone Sign-in). The TAP expires after use.
10. [CONFLICT: Jeffrey says that TAP makes recovery easier when a user loses or forgets their strong Passwordless authentication, while the existing entry does not mention this.]
11. [New Information] Be cautious when using aka.ms short URLs in manuals or providing them over the phone due to potential risks of mistyping and phishing attempts.
12. [ENHANCEMENT: Add information about managing least privilege for Temporary Access Pass creation, as described in the new source.]

## Common Pitfalls
- Ensuring proper permissions are granted for the user account.
- Verifying that the selected user has an MFA registration policy in place before creating a TAP.
- Double-checking the start date, time, and duration of the TAP to avoid errors or misconfigurations.
- Ensuring Shadow IT discovery is enabled via Microsoft Cloud App Security.
- Properly configuring Microsoft Endpoint Manager to block apps from Cloud App Security via Microsoft Defender ATP.
- [CONFLICT: Jeffrey says that TAP makes recovery easier when a user loses or forgets their strong Passwordless authentication, while the existing entry does not mention this.]
10. [ENHANCEMENT: Add information about the importance of enforcing phishing-resistant MFA for least privilege roles, activating roles using Principal Policy Assignments (PPAs) and Conditional Access policies, as well as being cautious when using aka.ms short URLs in manuals or providing them over the phone due to potential risks of mistyping and phishing attempts.]
11. [ENHANCEMENT: Add information about the potential risks associated with using aka.ms short URLs for Microsoft portals, as discussed in the article "The hidden risk of using aka.ms shortURLs for Microsoft portals" by Jan Bakker.]