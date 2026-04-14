---
conflicts: []
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Michael Morten Sonne
  crawled: '2026-04-14'
  date: '2026-03-02'
  title: 'Defender for Endpoint – New feature is out: Live response file library!
    – Blog - Sonne´s Cloud'
  url: https://blog.sonnes.cloud/defender-for-endpoint-new-feature-is-out-live-response-file-library
stale_after: '2026-06-13'
title: Enrollment Status Page Configuration
topic: intune/deployment/enrollment-status-page
---

# Enrollment Status Page Configuration

## Overview
The Live response file library is a centralized repository within Microsoft Defender for Endpoint where security teams can upload and manage files used during Live Response sessions on endpoints. This feature addresses a long-standing pain point in SOC by enabling pre-staging of response tooling, centralized governance, inline script inspection, and lifecycle hygiene.

## Key Concepts
- Centralized file storage: Upload files once and make them available for all Live Response sessions.
- Support for multiple file types: Common formats such as .exe, .ps1, etc.
- Security Copilot integration: Analyzes scripts stored in the library to provide behavior summaries, security context, and execution risk considerations.

## Configuration
1. Navigate to the Defender for Endpoint portal.
2. Go to Incident Response > Live Response.
3. Click on Library Management.
4. Upload your files to the library.

## Common Pitfalls
- Not properly validating scripts before execution.
- Failing to remove outdated or redundant tools, leading to script sprawl and inconsistency.

## KQL / PowerShell
N/A (The article does not provide any specific queries or scripts.)

## Related Topics
- Microsoft Defender for Endpoint
- Microsoft Defender XDR (Microsoft 365 Defender)
- Script
- Security
- ESP error