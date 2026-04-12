---
conflicts:
- '[CONFLICT: Daniel Chronlund''s article does not provide additional information
  on this concept.]'
- '[CONFLICT: Daniel Chronlund''s article does not provide additional information
  on this step.]'
- '[CONFLICT: Daniel Chronlund''s article does not provide additional information
  on this point.]'
- '[CONFLICT: Daniel Chronlund''s article provides additional information on this
  concept, including the introduction of a PowerShell tool (Deploy-DCConditionalAccessBaselinePoC)
  that automates the deployment of named locations.]'
- '[CONFLICT: Daniel Chronlund''s article provides additional information on this
  step.]'
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2018-11-23'
  title: How Multiple Conditional Access Policies Are Applied
  url: https://danielchronlund.com/2018/11/23/how-multiple-conditional-access-policies-are-applied
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2023-09-29'
  title: How To Deploy a Complete Entra ID Conditional Access PoC in Under 5 Minutes
  url: https://danielchronlund.com/2023/09/29/how-to-deploy-a-complete-entra-id-conditional-access-poc-in-under-5-minutes
- author: Daniel Chronlund
  crawled: '2026-04-12'
  date: '2024-11-21'
  title: Conditional Access Gallery &#8211; Point, Select, and Deploy in Minutes
  url: https://danielchronlund.com/2024/11/21/conditional-access-gallery-point-select-and-deploy-in-minutes
stale_after: '2026-07-11'
title: Named Locations and IP-Based Conditions
topic: identity/conditional-access/named-locations
---

# Named Locations and IP-Based Conditions

## Overview
Named Locations and IP-Based Conditions are essential components in Microsoft's Conditional Access policies, enabling administrators to control access based on specific geographical locations or IP addresses. This topic matters because it allows for fine-grained security controls that can help prevent unauthorized access and data breaches.

## Key Concepts
- Named Locations: Custom defined geographical areas used in Conditional Access policies to specify allowed or blocked locations. [CONFLICT: Daniel Chronlund's article provides additional information on this concept, including the introduction of a PowerShell tool (Deploy-DCConditionalAccessBaselinePoC) that automates the deployment of named locations.]
- Trusted IP: A specific IP address or range of IP addresses that are considered safe and allowed for accessing resources within a Conditional Access policy.
- Country Filter: A feature that restricts access to users based on their country of origin, as determined by their IP address. [CONFLICT: Daniel Chronlund's article does not provide additional information on this concept.]
- Impossible Travel: A scenario where a user attempts to authenticate from two different locations at the same time, which can be used to detect fraudulent activities. [CONFLICT: Daniel Chronlund's article does not provide additional information on this concept.]
- Sign-in Location: The location from which a user is currently signing in, as reported by Microsoft's Azure Active Directory (Azure AD).

## Addition from new source
- **Deploy-DCConditionalAccessBaselinePoC**: A PowerShell tool that automates the deployment of a Conditional Access proof-of-concept design in your organization within minutes. It handles all dependencies, creates necessary groups and named locations, uploads a Terms of Use template, and deploys the policy design baseline from Daniel Chronlund's website in report-only mode.
- **Conditional Access Gallery**: A collection of pre-configured Conditional Access templates that can be quickly deployed using the Invoke-DCConditionalAccessGallery PowerShell tool. This tool automates the creation of all dependencies, including groups and named locations, and documents the new policy design for you.

## Configuration
1. Create Named Locations in the Azure portal under Azure Active Directory > Security > Conditional Access > Named locations. [CONFLICT: Daniel Chronlund's article provides additional information on this step.]
2. Define Trusted IP ranges and Country Filters within your Conditional Access policies, either as conditions or access controls.
3. Configure Impossible Travel settings by creating a policy with the "Block access" access control and setting the "Impossible travel" condition to "On".
4. Monitor sign-in locations using Azure AD reports and adjust policies accordingly. [CONFLICT: Daniel Chronlund's article does not provide additional information on this step.]
5. To deploy a Conditional Access proof-of-concept design using Deploy-DCConditionalAccessBaselinePoC, follow the instructions provided in Daniel Chronlund's blog post.
6. To quickly deploy pre-configured Conditional Access templates using the Conditional Access Gallery, use the Invoke-DCConditionalAccessGallery PowerShell tool.

## Common Pitfalls
- Incorrectly defining Named Locations can lead to either overly restrictive or permissive policies, potentially causing legitimate users to be blocked or unauthorized access to occur.
- Trusted IP ranges should be updated regularly to account for changes in network configurations and to ensure that only trusted devices are allowed access.
- Country Filters may not always accurately determine a user's country of origin due to the complexity of IP address mapping.
- Impossible Travel settings can generate false positives if users frequently travel or work remotely, so it is important to carefully configure these settings and monitor for false positives.
- The Conditional Access Gallery templates may not cover all specific use cases, so administrators should review and adjust the policies as needed after deployment.