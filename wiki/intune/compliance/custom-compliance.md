---
conflict_topics:
- intune/compliance/compliance-policy-design
- intune/configuration/delivery-optimization
conflicts:
- '[CONFLICT: Oliver Kieselbach''s method does not involve creating and filling AAD
  groups, but it provides a way to download all Proactive Remediation Scripts from
  Microsoft Intune.]'
- '[CONFLICT: Oliver Kieselbach''s method does not involve creating and filling AAD
  groups, but it provides a way to download all Proactive Remediation Scripts from
  Microsoft Intune. Jannik Reinhard''s method involves creating custom compliance
  policies for Windows devices.]'
context_note: Custom Compliance is part of the intune domain. Synthesised from 3 community
  sources.
domain: intune
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2022-08-28'
  title: Create and Fill AAD Group based on an local attributes
  url: https://jannikreinhard.com/2022/08/28/create-and-fill-aad-group-based-on-an-local-attributes
- author: Oliver Kieselbach
  crawled: '2026-04-18'
  date: '2022-09-07'
  title: Get back your Intune Proactive Remediation Scripts
  url: https://oliverkieselbach.com/2022/09/07/get-back-your-intune-proactive-remediation-scripts
- author: Jannik Reinhard
  crawled: '2026-04-18'
  date: '2023-02-26'
  title: How to use Custom Compliance Script + Example script
  url: https://jannikreinhard.com/2023/02/26/how-to-use-custom-compliance-script-example-script
stale_after: '2026-06-17'
title: Custom Compliance Policies and Scripts
topic: intune/compliance/custom-compliance
---

# Custom Compliance Policies and Scripts

## Custom Compliance Policies and Scripts

Custom Compliance Policies and Scripts allow for creating and filling Azure Active Directory (AAD) groups based on local attributes such as device manufacture, using Endpoint Analytics and Azure Automation. This technique can be used to make more specific accesses, manage application access rights, or perform other tasks that require granular control over client devices.

The new source article "Get back your Intune Proactive Remediation Scripts" by Oliver Kieselbach introduces a method for downloading all Proactive Remediation Scripts from Microsoft Intune using the Intune PowerShell SDK. This method is not directly related to creating and filling AAD groups based on local attributes, but it might be useful for managing scripts within an organization.

The article "How to use Custom Compliance Script + Example script" by Jannik Reinhard provides a detailed explanation of how to create custom compliance policies for Windows devices. This includes writing PowerShell scripts and JSON files for defining custom settings and values that are considered compliant, as well as a detection script that queries the device and returns the value when a compliance policy is evaluated.

[CONFLICT: Oliver Kieselbach's method does not involve creating and filling AAD groups, but it provides a way to download all Proactive Remediation Scripts from Microsoft Intune. Jannik Reinhard's method involves creating custom compliance policies for Windows devices.]

## Key Concepts
- Endpoint Analytics Detection script
- Azure Automation Runbook
- App Registration
- Variables (Secret Value, TenantId, App ID)
- PowerShell scripts for creating and filling AAD groups based on local attributes
- Intune Proactive Remediation Scripts (from the new source article)
- Custom Compliance Policies (from Jannik Reinhard's article)

## Configuration
1. Deploy an Endpoint Analytics Script to collect the value from client devices with device manufacture information.
2. Create an App Registration in Azure Active Directory with necessary permissions (Microsoft Graph, DeviceManagementConfiguration.Read.All, Group.Create, and GroupMember.ReadWriteAll).
3. Create an Automation Account in Azure.
4. Create a Runbook in the Automation Account with PowerShell script for creating and filling AAD groups based on local attributes.
5. Link the created schedule to the Runbook.

## How to write a compliance script (from Jannik Reinhard's article)

In the PowerShell script you have all the freedom that PowerShell offers you. The output must be a json. This output json can contain several checks. Here is an example script:

```
$avActive = $false
if(Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct){
    $avActive = $true
}

$freeStorage = [math]::Round((Get-PSDrive -Name C).Free / 1024 / 1024 / 1024)
$output = @{ AvActive = $avActive; FreeStorage = $freeStorage}
return $output | ConvertTo-Json -Compress
```

This script checks if an AV is activated and returns the free storage in GB.

## Json (from Jannik Reinhard's article)

The json describes how to deal with the output. This is the more complicated thing but lets also check this step by step but if you need more information check this [link](https://learn.microsoft.com/en-us/mem/intune/protect/compliance-custom-json).

The json is build out of an array of rules. If you have only one rule the array contains only one entry but if you have multiple checks, each check has its own object with a name, displayName, and operator properties. The value property contains the PowerShell script that performs the compliance check. Here is an example JSON:

```
{
  "rules": [
    {
      "name": "AntiVirus",
      "displayName": "Is Anti-virus software installed?",
      "operator": "Equals",
      "value": "[{\"script\": \"$avActive\"}]"
    },
    {
      "name": "FreeStorage",
      "displayName": "Does the device have enough free storage?",
      "operator": "GreaterThanOrEqual",
      "value": "[{\"script\": \"$freeStorage >= 50\"}]"
    }
  ]
}
```

## Common Pitfalls
- Incorrect configuration of App Registration or Runbook permissions may result in errors or failure to create or fill AAD groups.
- Misconfigured scripts or schedules can lead to unnecessary resource consumption or incorrect group memberships.
- Misconfiguration of custom compliance policies, such as incorrect JSON syntax or PowerShell script errors, can prevent the policy from functioning correctly.

## KQL / PowerShell
[The article does not provide any specific queries or scripts in KQL or PowerShell format.]

## Related Topics
- Custom Compliance
- Compliance Script
- Discovery Script
- Custom Setting
- Compliance JSON
- Intune Proactive Remediation Scripts (from the new source article)
- Custom Compliance Policies (from Jannik Reinhard's article)