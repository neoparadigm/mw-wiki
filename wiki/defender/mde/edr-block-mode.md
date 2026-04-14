---
conflicts:
- '[CONFLICT: The new source does not mention passive mode in the context of EDR,
  only in relation to Microsoft Defender Antivirus.]'
- '[CONFLICT: The new source emphasizes the importance of these capabilities being
  present in the primary antivirus solution.]'
domain: defender
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Jannik Reinhard
  crawled: '2026-04-14'
  date: '2023-10-08'
  title: How to enroll device to Microsoft Defender for Endpoint and how does it work
    (1/2)?
  url: https://jannikreinhard.com/2023/10/08/how-to-enroll-device-to-microsoft-defender-for-endpoint-and-how-does-it-work-1-2
- author: limwainstein
  crawled: '2026-04-14'
  date: '2025-10-20'
  title: Endpoint detection and response in block mode - Microsoft Defender for Endpoint
  url: https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode
stale_after: '2026-07-13'
title: EDR in Block Mode
topic: defender/mde/edr-block-mode
---

# EDR in Block Mode

## Overview
EDR (Endpoint Detection and Response) in Block Mode is a feature of Microsoft Defender for Endpoint that provides added protection from malicious artifacts when Microsoft Defender Antivirus is not the primary antivirus product and is running in passive mode. This feature is available in Defender for Endpoint Plan 2.

[Endpoint detection and response](overview-endpoint-detection-response) (EDR) in block mode works behind the scenes to remediate malicious artifacts that were detected by EDR capabilities. Such artifacts might have been missed by the primary, non-Microsoft antivirus product. EDR in block mode allows Microsoft Defender Antivirus to take actions on post-breach, behavioral EDR detections.

## Key Concepts
- EDR Block Mode: A mode within MDE that blocks potential threats at the endpoint level.
- Potentially Unwanted Applications (PUA): Software that, while not necessarily malicious, can pose a risk to system security and productivity.
- Behavior Analysis: The process of evaluating software behavior to determine if it poses a threat.
- Threat Prevention: Proactive measures taken to stop threats before they can cause harm.
- Passive Mode (EDR): A mode where Microsoft Defender Antivirus runs alongside another antivirus solution, providing additional protection and remediation capabilities for EDR detections. [CONFLICT: The new source does not mention passive mode in the context of EDR, only in relation to Microsoft Defender Antivirus.]

## Configuration
1. Enable EDR Block Mode on the MDE console.
2. Configure policies to define which actions should be blocked.
3. Deploy the policies to target devices.
4. Ensure that your non-Microsoft antivirus solution includes real-time protection, network protection, and attack surface reduction rules capabilities. [CONFLICT: The new source emphasizes the importance of these capabilities being present in the primary antivirus solution.]

## Common Pitfalls
- Overly restrictive policies may block legitimate software, leading to decreased productivity.
- Incorrect configuration of policies can result in insufficient threat protection.
- Relying solely on EDR in Block Mode for protection may lead to gaps if the primary antivirus solution does not have comprehensive capabilities. [NEW: The new source highlights the importance of having a robust primary antivirus solution.]

## KQL / PowerShell
N/A (The source article does not provide any specific queries or scripts related to EDR Block Mode.)

## Related Topics
- EDR block mode
- Third-party AV (comparing MDE with other endpoint security solutions)
- MDE coexistence (configuring MDE alongside other endpoint protection tools)
- EDR (further exploration of Endpoint Detection and Response concepts)
- Microsoft Defender Antivirus (understanding its passive mode and capabilities)