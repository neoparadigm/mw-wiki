---
conflicts: []
context_note: Avd Security Baseline is part of the azure domain. It connects closely
  to Pim For Groups. Synthesised from 2 community sources.
domain: azure
gaps: []
last_synthesised: '2026-04-18'
related_topics:
- identity/pim/pim-for-groups
sources:
- author: cawerner
  crawled: '2026-04-18'
  date: '2025-06-20'
  title: Security recommendations for Azure Virtual Desktop - Azure Virtual Desktop
  url: https://learn.microsoft.com/en-us/azure/virtual-desktop/security-recommendations
- author: kenwith
  crawled: '2026-04-18'
  date: '2025-05-06'
  title: Apply Zero Trust principles to Azure Virtual Desktop
  url: https://learn.microsoft.com/en-us/security/zero-trust/azure-infrastructure-avd
stale_after: '2026-06-17'
title: Azure Virtual Desktop Security Baseline
topic: azure/avd/avd-security-baseline
---

# Azure Virtual Desktop Security Baseline

## Azure Virtual Desktop Security Baseline

### Overview
Azure Virtual Desktop (AVD) is a managed virtual desktop service offering advanced security features to keep your organization secure. This entry provides recommendations for securing AVD deployments, focusing on components that require customer or partner management.

### Key Concepts
- Azure Virtual Desktop architecture and components
- Shared security responsibilities between Microsoft and customers/partners
- Security boundaries in Windows and their role in isolating devices, networks, virtual machines, and applications
- [Zero Trust principles](zero-trust-overview) applied to Azure Virtual Desktop

### Configuration
- Implement multifactor authentication and conditional access for identity management
- Secure user devices (mobile and PC) by applying appropriate policies and updates
- Configure app security according to your organization's or customer's needs
- Manage the session host operating system with up-to-date patches and configurations
- Set deployment configuration based on your specific requirements
- Implement network controls such as firewalls, VPNs, and access policies
- Limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection
- Specify allowed network traffic flows between hub and spoke VNets with Azure Firewall
- Use Role Based Access Control (RBAC) for virtual machines
- Isolate the components of an Azure Virtual Desktop deployment
- Protect data in all three modes: data at rest, data in transit, data in use
- Prevent traffic flows between workloads with Azure Firewall
- Use double encryption for end-to-end encryption, enable encryption at host, secure maintenance for virtual machines, and Microsoft Defender for Servers for threat detection
- Use Azure Virtual Desktop security, governance, management, and monitoring features to improve defenses and collect session host analytics

### Common Pitfalls
- Neglecting to secure identity, user devices, apps, session hosts, deployment configurations, network controls, and data can lead to security vulnerabilities
- Failing to keep components up-to-date can expose your environment to known security risks

### KQL / PowerShell
[Not applicable as the source article does not provide any specific queries or scripts]

### Related Topics
- AVD security
- Azure Virtual Desktop
- WVD (Windows Virtual Desktop)
- FSLogix
- Session host hardening
- [Zero Trust principles](zero-trust-overview)