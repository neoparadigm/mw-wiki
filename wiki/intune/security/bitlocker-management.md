---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-12'
sources:
- author: Ugur Koc
  crawled: '2026-04-12'
  date: '2025-07-14'
  title: 'KQL Queries Made Easy: My Intune Admin Journey with Copilot - Ugur Koc'
  url: https://ugurkoc.de/kql-queries-made-easy-my-intune-admin-journey-with-copilot
stale_after: '2026-07-11'
title: BitLocker Management via Intune
topic: intune/security/bitlocker-management
---

# BitLocker Management via Intune

## Overview
BitLocker Management via Intune provides administrators with the ability to manage BitLocker encryption on Windows devices through Microsoft Endpoint Manager (Intune). This topic matters as it ensures data protection and compliance by encrypting sensitive data stored on devices.

## Key Concepts
- BitLocker: A full disk encryption feature included in Windows Vista and later versions that helps protect data by providing encryption for fixed drives.
- Microsoft Endpoint Manager (Intune): A cloud-based service used to manage mobile devices, PCs, and applications.
- Encryption: The process of converting plaintext into ciphertext to ensure confidentiality, integrity, and authenticity of data.
- Recovery Key: A backup key used to recover access to encrypted data in case the BitLocker recovery password is lost or forgotten.
- Silent Encryption: Automatic encryption of drives without user interaction.
- BitLocker Policy: A set of rules that dictate how BitLocker operates on a device, including encryption requirements and recovery options.

## Configuration
1. In the Microsoft Endpoint Manager admin center, navigate to Tenant administration > Connectors and tokens > Connectors.
2. Click Add, select Intune connector, and then click Next.
3. Enter a name for the connector and click Next.
4. Configure settings as needed, such as enabling BitLocker management, and then click Next.
5. Review the summary and click Create to create the connector.
6. Navigate to Devices > Windows > Configuration Manager > Baseline Policies.
7. Click Create to create a new policy, select BitLocker Drive Encryption, and then click Next.
8. Configure settings for the policy, such as encryption type, recovery options, and silent encryption, and then click Next.
9. Review the summary and click Create to create the policy.
10. Assign the policy to the appropriate groups of devices.

## Common Pitfalls
- Not enabling BitLocker management for the Intune connector can prevent administrators from managing BitLocker on devices.
- Failing to configure recovery options properly can result in lost access to encrypted data if the recovery password is forgotten or lost.
- Incorrectly configuring encryption types, such as using XTS-AES instead of AES-256, can weaken the security of encrypted data.

## KQL / PowerShell
The article does not provide any specific queries or scripts for BitLocker management via Intune. However, you can use Kusto Query Language (KQL) to query device data in Log Analytics and PowerShell to manage BitLocker on devices directly.

## Related Topics
- BitLocker
- Encryption
- Recovery Key
- Silent Encryption
- BitLocker Policy