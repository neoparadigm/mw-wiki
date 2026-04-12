---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2024-08-08'
  title: Simplifying Entra ID Temporary Access Pass Creation with PowerShell
  url: https://danielchronlund.com/2024/08/08/simplifying-entra-id-temporary-access-pass-creation-with-powershell
stale_after: '2026-06-11'
title: MFA Registration Policy and TAP
topic: identity/entra-id/mfa-registration-policy
---

# MFA Registration Policy and TAP

## MFA Registration Policy and TAP

This topic focuses on configuring Multi-Factor Authentication (MFA) registration policies and Temporary Access Passes (TAPs) in Microsoft Entra ID, using PowerShell for streamlined management.

## Key Concepts
- MFA Registration Policy
- Temporary Access Pass (TAP)
- PowerShell Scripting
- Microsoft Graph API

## Configuration
1. Set up the environment by connecting to Graph and installing necessary PowerShell modules.
2. Retrieve a list of users, present them in a grid view for selection, and choose the desired user.
3. Generate a list of dates for the next 30 days, select the start date for the TAP.
4. Provide a list of hours in the day to specify when the TAP should start.
5. Specify the TAP duration in hours (between 1 and 8), which is then converted to minutes.
6. Choose whether the TAP can be used only once.
7. Create the TAP using the PowerShell script with all parameters set.

## Common Pitfalls
- Ensuring proper permissions are granted for the user account.
- Verifying that the selected user has an MFA registration policy in place before creating a TAP.
- Double-checking the start date, time, and duration of the TAP to avoid errors or misconfigurations.

## KQL / PowerShell
```powershell
# Connect to Graph:
Connect-MgGraph -NoWelcome -Scopes "User.Read.All", "UserAuthenticationMethod.ReadWrite.All"

# Install PowerShell Console GUI Tools:
Install-Module Microsoft.PowerShell.ConsoleGuiTools -Scope CurrentUser -Force

# ... (The rest of the script as described in the article)
```

## Related Topics
- MFA registration
- Temporary access pass
- security info
- self-service MFA