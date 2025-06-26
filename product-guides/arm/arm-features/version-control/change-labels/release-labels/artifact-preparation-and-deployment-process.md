---
description: >
  This document outlines the process of preparing an artifact ZIP based on
  selected revisions, along with an example for better understanding.
---

# Artifact Preparation and Deployment Process

## Example Scenario

**Git Logs**: (_A is the latest revision_)  
`A → B → C → D → E → F → G → H → I → J`  
**Selected Revisions**: `B, C, F, G, J`

---

## Artifact Creation Process

1. **Ensure Revision XML Files**  
   For each selected revision, ensure the presence of a corresponding revision XML file containing:
   - Commit details
   - List of added, modified, or deleted files  
   _If any XML file is missing, it is dynamically generated._

2. **Gather Changed Files**  
   Collect all added, modified, or deleted files from the selected revisions (`B, C, F, G, J`) using the XML files.

3. **Checkout the Latest Revision**  
   Switch to the latest selected revision (e.g., `B`).

4. **Copy Files to Package Directory**  
   Copy all gathered files into a package directory from the checkout of the latest selected revision.

5. **Prepare Deployment Files**  
   Generate `package.xml` and `destructiveChanges.xml` within the package directory.

6. **Create the Artifact ZIP**  
   Archive the package directory, which includes the selected files and metadata files. This ZIP file is used for custom deployments.

---

## Deployment Process

### 1. Full Deployment

Retrieve the artifact ZIP from:  
`.rabit → scm → changelabel → {repo_id} → {release_label_id}.zip`  
Deploy the ZIP as-is.

### 2. Selective Deployment

For selective deployments:

- Retrieve `package.xml` and `destructiveChanges.xml` from:  
  `scm → scmcommithistory → {repo_id} → {branch_name} → {release_label_name}`
- Display metadata components in the UI for user selection.
- Based on selection, extract corresponding files from the artifact ZIP for deployment.

> If deployment issues occur, these paths serve as the source of truth for verification.

---

## Implementation Considerations

### Consideration 1: Potential Missing Files in the Artifact ZIP

**Scenario:**  
Files may be missing from the ZIP even if their revisions were selected.

**Example:**  
**Git Log**: `A → B → C → D`  
**Changes:**
- `A`: `A.cls` modified
- `B`: `C.cls` deleted
- `C`: `C.cls` modified
- `D`: `D.cls` modified  

**Selected Revisions**: `A, C, D`  
**Result**:  
The ZIP contains `A.cls` and `D.cls`, but not `C.cls`.

**Reason:**  
The latest selected revision is `A`. Since `C.cls` was deleted in `B`, it doesn’t exist in the checkout of `A`, and thus is excluded.

---

### Consideration 2: No Delta Support for Release Labels

**Scenario:**  
Release labels do not currently support delta metadata logic, which may result in:

- Unintended inclusion of extra metadata
- Missing specific modifications

**Example:**  
Adding a `CustomLabel` results in the entire `CustomLabels.labels` file being included, even if only one label was changed.

---

## Repository Type Exceptions

### 1. Non-DX Repositories  
Modifying a `CustomField` includes the entire `CustomObject` file, which contains all child metadata (e.g., `CustomField`, `RecordType`).

### 2. DX Repositories  
Only the specific `CustomField` file is included, as metadata is stored modularly.

---

## Summary

These behaviors are a result of the system's current file-level change tracking and repository structure. Supporting delta-level preparation would require significant architectural changes, particularly in how the system identifies and retrieves file differences.
