---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-08-01'
  title: Microsoft Entra ID Honeypot Accounts with Microsoft Sentinel
  url: https://danielchronlund.com/2023/08/01/microsoft-entra-id-honeypot-accounts-with-microsoft-sentinel
stale_after: '2026-06-11'
title: Blocking Device Code Flow
topic: identity/conditional-access/device-code-flow-blocking
---

# Blocking Device Code Flow

## Blocking Device Code Flow
Microsoft Entra ID (Azure AD) allows for device code flow authentication, which can be used to sign in to an account without providing a password. However, this method can potentially be exploited by attackers to steal tokens and gain unauthorized access.

## Key Concepts
- Device code flow: A method of authenticating to Azure AD without providing a password, using a device code and verification code.
- Token theft: The unauthorized acquisition of security tokens, which can grant an attacker access to sensitive resources.
- Microsoft Graph: An API that provides programmatic access to data within Microsoft 365, including Azure AD user accounts.

## Configuration
To block device code flow in Azure AD, you can create a custom conditional access policy that denies access via this method. Here's how to do it using PowerShell:

1. Install the DCToolbox module for Microsoft 365 security, conditional access, and automation.
2. Connect to Azure AD with device code flow using the following script:

```
# Connect to Azure AD with device code flow.
$ClientID = 'Your_Client_Id'
$ClientSecret = 'Your_Client_Secret'
$TenantID = 'Your_Tenant_Id'

$AccessToken = Invoke-DCAzureADDeviceAuthFlow -ReturnAccessTokenInsteadOfRefreshToken -ClientID $ClientID -TenantID $TenantID
```
Replace `Your_Client_Id`, `Your_Client_Secret`, and `Your_Tenant_Id` with the appropriate values for your Entra ID application and tenant.

3. Create a custom conditional access policy that blocks device code flow:

```
# Set the policy scope (e.g., users, groups, or cloud apps)
$Scope = "Users"

# Define the policy rules
$Rules = @(
    # Block device code flow
    New-Object -TypeName Microsoft.Open.AzureAD.Model.ConditionalAccessRule -Property @{
        RuleType    = "None"
        Operator    = "and"
        Control     = "Block"
        ClientAppType = "All client apps"
        Conditions  = @(
            New-Object -TypeName Microsoft.Open.AzureAD.Model.ClientAppCondition -Property @{
                ClientAppTypeOrOperator = "or"
                Value                   = "multiFactorAuthentication"
            }
        )
    }
)

# Create the policy object
$PolicyObject = New-Object -TypeName Microsoft.Open.AzureAD.Model.ConditionalAccessPolicy -Property @{
    DisplayName          = "Block Device Code Flow"
    Conditions           = $Rules
    Session              = New-Object -TypeName Microsoft.Open.AzureAD.Model.Session
    State                = "Enabled"
    EnforcedDeviceCompliance     = "Block"
}

# Apply the policy to the specified scope
New-MCASconditionalAccessPolicy -Policy $PolicyObject -Scope $Scope
```
Replace `$Scope` with the appropriate value for your policy (e.g., users, groups, or cloud apps).

## Common Pitfalls
- Failing to properly configure the conditional access policy can result in legitimate users being blocked from signing in.
- Not using a custom policy can lead to device code flow remaining enabled by default, potentially exposing your organization to token theft attacks.

## KQL / PowerShell
N/A

## Related Topics
- [Device code](device_code)
- [Device code flow](device_code_flow)
- [microsoft.com/devicelogin](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-device-code-flow)
- [CA block](conditional_access_block)
- [Token theft](token_theft)