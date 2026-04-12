---
conflicts: []
domain: identity
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Jan Bakker
  crawled: '2026-04-12'
  date: '2026-01-12'
  title: Access Azure Virtual Desktop and Windows 365 Cloud PC from non-managed devices
  url: https://janbakker.tech/access-azure-virtual-desktop-and-windows-365-cloud-pc-from-non-managed-devices
stale_after: '2026-06-11'
title: Requiring Compliant or Hybrid-Joined Devices
topic: identity/conditional-access/compliant-device-requirement
---

# Requiring Compliant or Hybrid-Joined Devices

## Overview
Requiring compliant or hybrid-joined devices is a strategy used to secure access to Azure Virtual Desktop and Windows 365 Cloud PC resources from managed devices only. This approach ensures that only devices meeting specific compliance standards can access corporate resources, enhancing security and reducing potential risks associated with Bring Your Own Device (BYOD) scenarios.

## Key Concepts
- Compliant Devices: Devices that meet the organization's security and compliance requirements.
- Hybrid-Joined Devices: Devices joined to both Azure Active Directory (AAD) and a domain, providing seamless access to on-premises and cloud resources.
- Conditional Access (CA): A policy that controls user access to organizational resources based on conditions such as device compliance status.
- BYOD CA Policy: A conditional access policy that allows unmanaged devices to access corporate resources with specific exceptions and security controls in place.

## Configuration
1. Configure cross-tenant access settings to trust compliant devices from other tenants, covering MSP and external contractor scenarios.
2. Exclude Azure Virtual Desktop, Windows 365, and Windows Cloud Login resources from the Conditional Access policy for unmanaged devices.
3. Create a new policy for excluded resources, enforcing authentication strength (device-bound passkeys), token protection, and sign-in frequency to minimize potential security risks.
4. Register end-user devices with Entra ID for full Token Protection functionality.

## Common Pitfalls
- Failing to exclude Azure Virtual Desktop, Windows 365, and Windows Cloud Login resources from the Conditional Access policy for unmanaged devices can result in unsecured access to corporate resources.
- Not enforcing strong authentication methods (e.g., device-bound passkeys) and token protection on excluded resources can increase the risk of security breaches.
- Inadequate user education about device registration and the importance of compliance can lead to a higher number of non-compliant devices attempting to access corporate resources.

## KQL / PowerShell
[The article does not provide any relevant queries or scripts.]

## Related Topics
- Compliant Device
- Hybrid Join
- CA Device Condition
- Unmanaged Device
- BYOD CA