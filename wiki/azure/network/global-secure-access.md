---
conflict_topics:
- defender/mde/tamper-protection
- azure/monitoring/azure-monitor-log-analytics
conflicts:
- '[CONFLICT: Michael Morten Sonne mentions the ability to assign specific users and
  groups to traffic forwarding profiles, which is not explicitly mentioned in the
  existing entry]'
context_note: Global Secure Access is part of the azure domain. Synthesised from 6
  community sources.
domain: azure
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: ''
  title: Discover more from Sonne´s Cloud
  url: https://blog.sonnes.cloud/2025/10
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-06-05'
  title: Entra ID – Global Secure Access Client – Assign users and groups to forwarding
    profiles – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-global-secure-access-client-assign-users-and-groups-to-forwarding-profiles
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-02-17'
  title: Entra ID – Global Secure Access Client – What it is about – Part 1 – Blog
    - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-global-secure-access-client-part-1
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-02-21'
  title: Entra ID – Global Secure Access Client – Installation of the Agent on Windows
    – Part 2 – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-global-secure-access-client-part-2
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-03-06'
  title: Entra ID – Global Secure Access Client – Setup of the Microsoft 365 Profile
    – Part 3 – Blog - Sonne´s Cloud
  url: https://blog.sonnes.cloud/entra-id-global-secure-access-client-setup-of-the-microsoft-365-profile-part-3
- author: Michael Morten Sonne
  crawled: '2026-04-18'
  date: '2024-07-14'
  title: Entra ID – Global Secure Access – Now Generally Available! – Blog - Sonne´s
    Cloud
  url: https://blog.sonnes.cloud/entra-id-global-secure-access-now-generally-available
stale_after: '2026-06-02'
title: Global Secure Access and ZTNA
topic: azure/network/global-secure-access
---

# Global Secure Access and ZTNA

## Overview
Global Secure Access (GSA) and Zero Trust Network Access (ZTNA) are security solutions provided by Microsoft's Entra suite that enable secure access to applications and resources for users, regardless of their location or device. These solutions are crucial in today's hybrid work environment where remote access is essential.

## Key Concepts
- Global Secure Access: A cloud-based service that provides secure access to on-premises and cloud applications using conditional access policies. [CONFLICT: Michael Morten Sonne mentions the ability to assign specific users and groups to traffic forwarding profiles, which is not explicitly mentioned in the existing entry]
- Zero Trust Network Access (ZTNA): A security model that assumes all traffic is untrusted, requiring strict verification of every user and device before granting access to resources.
- Entra Internet Access: A component of GSA that provides secure internet access for users, protecting them from threats while they browse the web.
- Entra Private Access: A component of GSA that provides secure access to on-premises applications from anywhere, using a software-defined perimeter approach.
- Traffic forwarding profiles (newly added from the new source)
- Session Management (newly added from the new source)
- [Assigning users and groups to traffic forwarding profiles](https://blog.sonnes.cloud/entra-id-global-secure-access-client-assign-users-and-groups-to-forwarding-profiles/) (newly added from the new source)
- [Session Management](#session-management) (newly added from the new source)

## Configuration
The configuration of Global Secure Access and ZTNA involves setting up conditional access policies, defining application access rules, configuring network connectors for on-premises integration, assigning specific users and groups to traffic forwarding profiles (as per the new source), and possibly other steps as detailed in [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/) section of Sonne's Cloud blog and [Microsoft Entra admin center](#microsoft-entra-admin-center) (newly added from the new source).

## Common Pitfalls
Common pitfalls include misconfiguring conditional access policies, which can lead to either overly restrictive or overly permissive access, and failing to properly secure on-premises network connectors.

## KQL / PowerShell
The article does not provide any specific queries or scripts related to Global Secure Access or ZTNA configuration. However, the [PowerShell](https://blog.sonnes.cloud/topics/general/software/powershell/) section of Sonne's Cloud blog may contain relevant scripts and tools for managing these solutions.

## Related Topics
- Global Secure Access
- GSA
- ZTNA
- Entra Internet Access
- Entra Private Access
- [Assigning users and groups to traffic forwarding profiles](https://blog.sonnes.cloud/entra-id-global-secure-access-client-assign-users-and-groups-to-forwarding-profiles/) (newly added from the new source)
- [Session Management](#session-management) (newly added from the new source)
- [Cool tools](https://blog.sonnes.cloud/topics/general/software/cool-tools/)
- [Global Secure Access](https://blog.sonnes.cloud/topics/global-secure-access/)
- [Identity](https://blog.sonne

New source article: "Entra ID – Global Secure Access – Now Generally Available! – Blog - Sonne´s Cloud"
Author: Michael Morten Sonne
New source content:

## Unified security for modern threats
In today's digital landscape, the need for robust security is more pressing than ever. While advancements in technology offer increased scalability, efficiency, and cost savings, they also present opportunities for cyber threats. Isolated identity and network access solutions often lead to fragmented security postures, making organizations vulnerable to sophisticated attacks.

Microsoft's SSE solution addresses this challenge by unifying identity and network access controls, ensuring a consistent security approach across all applications and resources.

### Key components of Microsoft’s SSE Solution
- Azure Active Directory (Azure AD)
- Conditional Access
- Identity Protection
- Cloud App Security
- Advanced Threat Protection (ATP)
- Microsoft Defender for Endpoint
- Microsoft Defender for Identity

### Benefits of Microsoft SSE
- Simplified security management
- Improved threat protection
- Enhanced user experience
- Increased productivity
- Cost savings

### Transitioning from VPNs to Zero Trust Network Access (ZTNA)
#### Increasing remote work and VPN reliance
With the rise of remote work, traditional Virtual Private Networks (VPNs) have become increasingly important for secure access to corporate resources. However, they come with their own set of challenges.

#### Limitations of traditional VPNs
- Scalability issues
- Performance degradation
- Security vulnerabilities
- Complex management

#### Shift to Zero Trust Network Access (ZTNA)
ZTNA is a security model that assumes all traffic is untrusted, requiring strict verification of every user and device before granting access to resources. This approach offers several benefits over traditional VPNs:

- Improved scalability
- Enhanced performance
- Increased security
- Simplified management

#### Challenges in Migrating to ZTNA
Despite its advantages, migrating from VPNs to ZTNA can be challenging due to factors such as:

- Legacy applications and infrastructure
- Complex network configurations
- User resistance to change
- Lack of expertise or resources for implementation

#### Solutions offered by Microsoft Entra Private Access
Microsoft Entra Private Access provides a software-defined perimeter (SDP) approach to ZTNA, allowing organizations to securely access on-premises applications from anywhere. It addresses the challenges mentioned above by:

- Supporting legacy applications and infrastructure
- Improving performance through SDP
- Simplifying management with centralized control
- Offering user-friendly experiences

#### Future-proofing Cyber Strategy
By adopting Microsoft's SSE solution, organizations can future-proof their cyber strategy by:

- Embracing a unified security approach
- Leveraging advanced threat protection capabilities
- Enhancing identity and access management
- Simplifying security operations
- Reducing costs through consolidation and automation

## Licensing
Microsoft's SSE solution is available as part of the Microsoft 365 E5, Microsoft 365 F3, and standalone licenses for Azure AD Premium P2 and Entra Suite.

## Supported platforms
Microsoft's SSE solution supports a wide range of platforms, including Windows, macOS, iOS, Android, Linux, and web browsers.

## Read my other blogs
- [Azure AD/Entra ID](https://blog.sonnes.cloud/topics/azure-ad-entra-id/)
- [Global Secure Access](https://blog.sonnes.cloud/topics/global-secure-access/)
- [Identity](https://blog.sonnes.cloud/topics/identity/)
- [Security](https://blog.sonnes.cloud/topics/security/)

# Conclusion
Microsoft's SSE solution offers a comprehensive approach to securing access to applications and resources in today's digital landscape. By unifying identity and network access controls, organizations can improve security, simplify management, and enhance the user experience. The shift from traditional VPNs to ZTNA is an important step towards future-proofing cyber strategies.

# References
[Microsoft Entra Suite](https://www.microsoft.com/en-us/microsoft-365/business/entra)
[Microsoft Security Service Edge (SSE)](https://docs.microsoft.com/en-us/security/sse/)
[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/)