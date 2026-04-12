---
conflicts:
- '[CONFLICT: Daniel Chronlund says this is the purpose of CA, existing entry does
  not mention it]'
- '[CONFLICT: Daniel Chronlund says this can happen, existing entry does not mention
  it]'
- '[CONFLICT: Daniel Chronlund says X, existing entry does not mention it]'
- '[CONFLICT: Daniel Chronlund says X, existing entry says Y]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2018-11-19'
  title: Fetch Data from Microsoft Graph with PowerShell (Paging Support)
  url: https://danielchronlund.com/2018/11/19/fetch-data-from-microsoft-graph-with-powershell-paging-support
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2018-11-21'
  title: Azure AD Conditional Access Policy Design Baseline
  url: https://danielchronlund.com/2018/11/21/azure-ad-conditional-access-policy-design-baseline
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2018-12-12'
  title: Conditional Access Logs in Azure AD
  url: https://danielchronlund.com/2018/12/12/conditional-access-logs-in-azure-ad
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2019-11-07'
  title: Automatic Deployment of Conditional Access with PowerShell and Microsoft
    Graph
  url: https://danielchronlund.com/2019/11/07/automatic-deployment-of-conditional-access-with-powershell-and-microsoft-graph
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2019-11-07'
  title: Safe Conditional Access Deployment with Report-Only Mode and the Insights
    Dashboard
  url: https://danielchronlund.com/2019/11/07/safe-conditional-access-deployment-with-report-only-mode-and-the-insights-dashboard
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-02-26'
  title: My Collection of Basic Microsoft Graph PowerShell Functions
  url: https://danielchronlund.com/2020/02/26/my-collection-of-basic-microsoft-graph-powershell-functions
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-10-20'
  title: Export your Conditional Access Policy Assignments to Excel
  url: https://danielchronlund.com/2020/10/20/export-your-conditional-access-policy-assignments-to-excel
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2020-11-25'
  title: How to Manage Conditional Access as Code &#8211; The Ultimate Guide
  url: https://danielchronlund.com/2020/11/25/how-to-manage-conditional-access-as-code-the-ultimate-guide
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-01-25'
  title: A Security MVP&#8217;s Take on Cloud Security in 2023
  url: https://danielchronlund.com/2023/01/25/a-security-mvps-take-on-cloud-security-in-2023
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-11-24'
  title: Conditional Access &#8216;What If&#8217; Simulation with PowerShell
  url: https://danielchronlund.com/2023/11/24/conditional-access-what-if-simulation-with-powershell
stale_after: '2026-06-11'
title: Conditional Access — Authentication Flows
topic: identity/conditional-access/authentication-flows
---

# Conditional Access — Authentication Flows

## Overview
This topic discusses how to fetch data from Microsoft Graph using PowerShell with paging support, and also provides information about Azure AD Conditional Access Policy Design Baseline and Conditional Access Logs in Azure AD. Additionally, it includes a Proof of Concept, a PowerShell script that deploys a complete Conditional Access policy design based on the baseline.

## Key Concepts
- Registering an application in Azure AD
- Granting permissions to the registered application
- Using PowerShell function `Get-GraphApiResult` for fetching data from Microsoft Graph API
- Paging support for handling large datasets
- Understanding the purpose and conditions of Azure AD Conditional Access Policies ([CONFLICT: Daniel Chronlund says this is the purpose of CA, existing entry does not mention it])
- Reviewing Conditional Access logs in Azure AD (New from source)
- Automatic Deployment of Conditional Access with PowerShell and Microsoft Graph (New from source)
- Safe Conditional Access Deployment with Report-Only Mode and the Insights Dashboard (New from source)
- My Collection of Basic Microsoft Graph PowerShell Functions (New from source)
- Exporting Conditional Access Policy Assignments to Excel (New from source, [Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/))
- **[NEW] How to Manage Conditional Access as Code — The Ultimate Guide** (Source: Daniel Chronlund)
  - Reasons for managing Conditional Access policies as code
  - Preparations and installation of the DCToolbox PowerShell module
- A Security MVP's Take on Cloud Security in 2023 (New source article)
  - Discussion on the importance of IT hygiene and cyber security posture in Sweden due to ongoing cyber attacks
  - Emphasis on making break glass accounts less obvious to avoid attracting attackers
- **[NEW] Conditional Access 'What If' Simulation with PowerShell** (Source: Daniel Chronlund)
  - Introduction of a PowerShell script for simulating the effects of Conditional Access policies without enforcing them
  - Capabilities similar to the built-in What If tool in the Entra ID portal, including policy testing, risk assessment, user experience analysis, compliance validation, and troubleshooting

## Configuration
1. Register an application in Azure AD as described in the article.
2. Save the Application ID and Key generated during registration.
3. Use the provided PowerShell function `Get-GraphApiResult` to fetch data from Microsoft Graph API, providing the required parameters: ClientID, ClientSecret, TenantName, and Graph URI.

## Common Pitfalls
- Not saving the Application ID and Key after registering the application in Azure AD.
- Granting insufficient permissions to the registered application.
- Incorrectly specifying the tenant name or Graph URI.
- Overthinking CA configurations ([CONFLICT: Daniel Chronlund says this can happen, existing entry does not mention it])
- Failing to understand Conditional Access logs and their implications (New from source)
- Not following instructions in the script for automatic deployment of Conditional Access policies (New from source)
- Inadequate testing due to lack of Report-only mode or Insights dashboard (New from source)
- Not exporting Conditional Access Policy Assignments to Excel when needed (New from source, [Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/))
- Not using the Conditional Access 'What If' Simulation with PowerShell for testing and troubleshooting (New from source, [Daniel Chronlund](https://danielchronlund.com/author/danielchronlund/))