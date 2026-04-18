---
conflicts: []
context_note: Compliant Device Requirement is part of the identity domain. It connects
  closely to Defender For Endpoint Intune and Mfa Registration Policy. Synthesised
  from 1 community source.
domain: identity
gaps: []
last_synthesised: '2026-04-18'
prerequisite_topics:
- identity/entra-id/mfa-registration-policy
related_topics:
- intune/security/defender-for-endpoint-intune
- identity/entra-id/mfa-registration-policy
sources:
- author: Jan Bakker
  crawled: '2026-04-18'
  date: '2026-01-12'
  title: Access Azure Virtual Desktop and Windows 365 Cloud PC from non-managed devices
  url: https://janbakker.tech/access-azure-virtual-desktop-and-windows-365-cloud-pc-from-non-managed-devices
stale_after: '2026-06-17'
title: Requiring Compliant or Hybrid-Joined Devices
topic: identity/conditional-access/compliant-device-requirement
---

# Requiring Compliant or Hybrid-Joined Devices

## Overview
Requiring Compliant or Hybrid-Joined Devices is a strategy to secure access to Azure Virtual Desktop and Windows 365 Cloud PC resources by enforcing Conditional Access policies that only allow access from compliant devices or hybrid-joined devices. This topic matters because it helps organizations maintain security while allowing flexibility for users to work from non-managed devices.

## Key Concepts
- Compliant Devices: Devices that meet specific security requirements set by the organization, such as having antivirus software installed and being compliant with a device compliance policy.
- Hybrid-Joined Devices: Devices that are joined to both Azure Active Directory (AAD) and a domain, allowing them to access resources in both environments.
- Conditional Access (CA): A security feature that allows organizations to control access to their resources based on conditions such as device compliance, location, and user risk level.
- Device Compliance Policy: A policy that defines the security requirements for compliant devices, including software updates, antivirus software, and configuration settings.
- BYOD CA: Conditional Access policies that allow users to access corporate resources from their own devices (Bring Your Own Device).

## Configuration
1. Create a device compliance policy in Azure Active Directory (AAD) that defines the security requirements for compliant devices.
2. Assign the device compliance policy to a group of users or devices.
3. Create a Conditional Access policy in AAD that requires compliant devices or hybrid-joined devices for access to Azure Virtual Desktop and Windows 365 Cloud PC resources.
4. Exclude Azure Virtual Desktop, Windows 365, and Windows Cloud Login from the Conditional Access policy if you want to allow unmanaged devices access to these resources with additional security controls.
5. Enforce three controls for the excluded resources: Authentication Strength (device-bound passkeys), Token Protection (to protect the token from being replayed when stolen), and Sign-in Frequency (to enforce a short token lifetime).
6. Register devices in Entra to enable Token Protection, if available.

## Common Pitfalls
- Not excluding Azure Virtual Desktop, Windows 365, and Windows Cloud Login from the Conditional Access policy can result in unmanaged devices accessing corporate resources without additional security controls.
- Failing to register devices in Entra can prevent Token Protection from working as intended.

## KQL / PowerShell
[Not applicable as the article does not provide any relevant queries or scripts.]

## Related Topics
- Compliant device
- Hybrid join
- CA device condition
- Unmanaged device
- BYOD CA