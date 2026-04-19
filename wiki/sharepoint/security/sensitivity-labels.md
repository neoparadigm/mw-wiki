---
conflicts: []
context_note: Sensitivity Labels is part of the sharepoint domain. Synthesised from
  1 community source.
domain: sharepoint
gaps: []
last_synthesised: '2026-04-18'
sources:
- author: Tony Redmond
  crawled: '2026-04-18'
  date: '2025-06-30'
  title: 'Practical Graph: Assigning Sensitivity Labels to SharePoint Files with the
    PowerShell SDK'
  url: https://practical365.com/assign-sensitivity-labels-cmdlet
stale_after: '2026-06-17'
title: Sensitivity Labels for SharePoint and OneDrive
topic: sharepoint/security/sensitivity-labels
---

# Sensitivity Labels for SharePoint and OneDrive

## Sensitivity Labels for SharePoint and OneDrive

### Overview
Sensitivity labels are used to classify and protect sensitive data in SharePoint and OneDrive. They provide a simple way to enforce information protection policies across an organization, ensuring that sensitive information is handled appropriately.

### Key Concepts
- Sensitivity labels: Classification tags applied to files to indicate their level of sensitivity and the protection measures required.
- Information Protection (MIP): A Microsoft service that helps organizations protect sensitive data by applying labels, encryption, and access controls.
- Label Policy: A set of rules defining how sensitivity labels are assigned to files based on specific criteria such as file type, content, or user.
- Auto Labeling: Automatic assignment of sensitivity labels to files based on predefined rules and machine learning algorithms.

### Configuration
1. Create sensitivity labels in the Microsoft 365 compliance center.
2. Assign permissions for users to manage sensitivity labels.
3. Configure label policies to automatically or manually apply labels to files.
4. Use PowerShell cmdlets like `Set-MgDriveItemSensitivityLabel` to assign labels to specific files.

### Common Pitfalls
- Overwriting existing labels: The `assignSensitivityLabel` API overwrites any previously assigned sensitivity label, including labels set by auto-label policies and manually assigned by users. It's important to check for existing labels before deciding to apply a new one.
- Incorrect label assignment: Misconfigured label policies or manual assignments can lead to inappropriate protection of sensitive data.
- Lack of user awareness: Users may not understand the importance of sensitivity labels and how they affect their work, leading to incorrect labeling or bypassing of protections.

### KQL / PowerShell
```powershell
# Assign a sensitivity label to a file using PowerShell
If ($FileType -in $ValidFileTypes) {
   Try {
     Set-MgDriveItemSensitivityLabel -DriveId $DriveId -DriveItemId $File.Id -SensitivityLabelId $SensitivityLabelId -ErrorAction Stop
     $Status = $true
   } Catch {
     Write-Host ("Error applying label {0} to {1} ({2})" -f $SensitivityLabelName, $File.Name, $_.Exception.Message) -ForegroundColor Red
   }
}
```

### Related Topics
- Sensitivity label
- MIP
- Information protection
- Label policy
- Auto labeling