---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jan Bakker
  crawled: '2026-04-14'
  date: '2026-01-12'
  title: Access Azure Virtual Desktop and Windows 365 Cloud PC from non-managed devices
  url: https://janbakker.tech/access-azure-virtual-desktop-and-windows-365-cloud-pc-from-non-managed-devices
stale_after: '2026-06-13'
title: Requiring Compliant or Hybrid-Joined Devices
topic: identity/conditional-access/compliant-device-requirement
---

# Requiring Compliant or Hybrid-Joined Devices

## Overview
Requiring compliant or hybrid-joined devices is a crucial aspect of securing access to Azure Virtual Desktop and Windows 365 Cloud PC resources in organizations that allow Bring Your Own Device (BYOD) scenarios. This topic matters because it helps maintain security while enabling productivity and flexibility for end-users.

## Key Concepts
- Compliant devices: Devices that meet specific security requirements set by the organization, such as having the latest updates, antivirus software, and adhering to Conditional Access policies.
- Hybrid-joined devices: Devices that are both joined to Azure Active Directory (AAD) and a domain, providing seamless access to on-premises and cloud resources.
- Clean-source principle: A security principle requiring all security dependencies to be as trustworthy as the object being secured.
- Conditional Access policies: Policies that control access to resources based on various conditions such as device compliance, location, and user risk level.

## Configuration
1. Configure cross-tenant access settings to trust compliant devices from other tenants for MSP, external contractor, or partner scenarios.
2. Exclude Azure Virtual Desktop, Windows 365, and Windows Cloud Login resources from Conditional Access policies if using the Windows App on unmanaged devices.
3. Create a new policy for excluded resources, enforcing authentication strength (device-bound passkeys), token protection, and sign-in frequency to minimize security risks.
4. Register end-user devices with Entra ID for full Token Protection functionality.

## Common Pitfalls
- Failing to exclude Azure Virtual Desktop, Windows 365, and Windows Cloud Login resources from Conditional Access policies on unmanaged devices can lead to bypassing security controls.
- Not registering end-user devices with Entra ID may limit the effectiveness of Token Protection.

## KQL / PowerShell
[The article does not provide any relevant queries or scripts.]

## Related Topics
- Compliant device
- Hybrid join
- CA device condition
- Unmanaged device
- BYOD Conditional Access