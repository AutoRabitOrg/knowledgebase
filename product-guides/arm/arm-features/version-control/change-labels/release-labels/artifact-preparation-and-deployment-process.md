---
description: >-
  This document outlines the process of preparing an artifact zip based on
  selected revisions, along with an example for better understanding.
---

# Artifact Preparation and Deployment Process

### Example Scenario

**Git Logs**: (_A is the latest revision_)\
`A → B → C → D → E → F → G → H → I → J`

**Selected Revisions**: `B, C, F, G, J`

***

### Artifact Creation Process

1. **Ensure Revision XML Files**\
   For each selected revision, ensure the existence of a corresponding revision XML file containing:
   * Commit details
   * List of added, modified, or deleted files\
     If any XML file is missing, it is dynamically created.
2. **Gather Changed Files**\
   Collect all files added, modified, or deleted across the selected revisions (`B, C, F, G, J`) using the prepared revision XML files.
3. **Checkout the Latest Revision**\
   Switch to the latest revision among the selected ones (e.g., `B`).
4. **Copy Files to Package Directory**\
   Copy all gathered files into a package directory from the latest revision's (`B`) checkout.
5. **Prepare Deployment Files**\
   Create the **package.xml** and **destructiveChanges.xml** files in the package directory.
6. **Create the Artifact Zip**\
   Zip the package directory, which includes the modified files from selected revisions. This zip file is then used for custom deployments.

***

### Deployment Process

#### 1. Full Deployment

For a full deployment, the artifact zip is retrieved from:\
`.rabit->scm->changelabel->{repoid}->{releaselabel_Id}.zip`\
It is deployed as-is.

#### 2. Selective Deployment

For selective deployment:

* Retrieve the **package.xml** from:\
  `{scm->scmcommithistory->{repo_id}->{branch_name}->{release_label_name}}->package.xml/destructive.xml`.
* Display components on the UI for user selection after metadata retrieval.
* Use the selected components to extract the corresponding files from the zip for deployment.

In case of deployment issues, the paths above serve as the **source of truth** to verify components.

### Implementation Considerations

#### **Consideration 1: Potential Missing Files in the Artifact Zip**

**Scenario:**\
Certain files may not appear in the artifact zip even if their revisions are selected.

**Example:**

**Git Logs**: `A → B → C → D`\
**Changes in Revisions**:

* `A`: `A.cls` modified
* `B`: `C.cls` deleted
* `C`: `C.cls` modified
* `D`: `D.cls` modified

**Selected Revisions**: `A, C, D`\
**Result**:\
The artifact zip contains only `A.cls` and `D.cls`, while `C.cls` is missing.

**Reason:**\
The process involves checking out the latest selected revision (`A`). Since `C.cls` was deleted in revision `B`, it does not exist in the checkout directory and is therefore not included in the artifact zip.

***

#### **Consideration 2: No Delta Support for Release Labels**

**Scenario:**\
Release labels currently do not support delta logic for metadata, which may lead to:

* Inclusion of additional metadata beyond the intended changes
* Missing specific modifications

**Example:**\
Adding a new **CustomLabel** results in the artifact containing all CustomLabels because they are stored in a single `CustomLabels.labels` file.

### **Repository Type Exceptions**:

1. **Non-DX Repositories**:\
   Example: Adding a **CustomField** includes the entire `CustomObject` file, encompassing all child metadata (e.g., CustomField, RecordType).
2. **DX Repositories**:\
   Example: Adding a **CustomField** includes only the specific `CustomField` file because metadata is stored separately.

#### **Summary:** These behaviors are inherent to the system’s current file-level change tracking and directory structure. Significant architectural changes would be required to enable delta preparation or refine checkout logic.
