# Commits Summary

## Overview

In AutoRABIT ARM, the **Commits Summary** screen provides detailed information about each commit or merge, including diffs of modifications. Commits are organized by the date they were made in ARM. By default, only commits by the logged-in user are displayed in reverse chronological order (most recent first).

## Accessing the Commits Screen

1. Navigate to **Version Control > Commits** to access the **Commits** screen.
2. For optimal viewing, set your browser's zoom level to **80%** (Chrome/Firefox).

## Viewing Commits

- To view all commits (including those by teammates), toggle the **Created By Me** switch to the left.
- To filter commits pending reviewer approval, toggle the **Pending Approvals** switch to the right.
- Use the search field to filter commits by label, revision number, or comment. *Note: Search is case-sensitive.*

<figure>
  <img src="../../../../../.gitbook/assets/image (1061).png" alt="Commits screen showing filter and search options">
  <figcaption>Commits screen with search and filter toggles</figcaption>
</figure>

## Commit Details

Each commit entry displays:

- **Commit Type Initials**:
  - PV: Prevalidation Commit
  - EZ: EZ-Commit
  - M: Merge Commit
  - VM: Validate and Merge
  - BB: Branching Baseline
  - RC: Revert Commit
  - CI: Commit from CI Job
  - DR: Dry Run
  - EC: External Commit
- Commit label name
- Commit message
- Committer's username
- Commit creation date
- Version Control repository, destination, and source branch details
- Salesforce Org details (if applicable)
- Commit Revision label
- Commit/Merge status

## Quick Merge

Quick Merge allows direct merging from the Commits screen without navigating to the New Merge screen.

1. Hover over the three dots beside the desired commit.
2. Click **Quick Merge**.
3. Confirm the action in the pop-up.

<figure>
  <img src="../../../../../.gitbook/assets/image (1062).png" alt="Quick Merge menu option on Commits screen">
  <figcaption>Quick Merge action in the menu</figcaption>
</figure>

**Note:** Quick Merge is not available for:
- Prevalidation Merge commits pending approval
- Already merged commits

## Detailed View

1. Hover over the three dots beside a commit and click **Detailed View**.

<figure>
  <img src="../../../../../.gitbook/assets/image (1064).png" alt="Accessing detailed commit view">
  <figcaption>Accessing detailed view from commit menu</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1065).png" alt="Three-dot menu beside a prevalidated commit">
  <figcaption>Detailed view access for prevalidated commits</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1066).png" alt="Red dot indicating failed prevalidation">
  <figcaption>Indicator for failed prevalidation</figcaption>
</figure>

The detailed view includes:
- Commit details
- Merge/EZ-Commit configuration
- Pull Request section (for EZ-Commits only)
- Reviewer comments
- Metadata diffs
- Deployment validation
- Code Analysis
- Logs and ALM integration

<figure>
  <img src="../../../../../.gitbook/assets/image (1067).png" alt="Commit details summary panel">
  <figcaption>Commit summary details</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1068).png" alt="Dropdown showing in-depth configuration">
  <figcaption>Expanded view of selected features</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1069).png" alt="EZ-Commit pull request details">
  <figcaption>Pull request details in EZ-Commit</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1070).png" alt="Step-by-step commit process view">
  <figcaption>Visual display of commit steps</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1071).png" alt="Reviewer comments section">
  <figcaption>Comments by reviewers</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1072).png" alt="Commit reports and code analysis section">
  <figcaption>Commit details report panel</figcaption>
</figure>

## Code Analysis File

Static Code Analysis (SCA) is part of the security development lifecycle. Tools include ApexPMD, Checkmarx, Salesforce Scanner, and CodeScan. Violations are displayed by file and line.

<figure>
  <img src="../../../../../.gitbook/assets/image (1079).png" alt="Static code analysis report example">
  <figcaption>Sample Static Code Analysis output</figcaption>
</figure>

## Files Changed

ARM compares metadata changes between branches/orgs. RED indicates deletions or changes from the source; GREEN indicates changes in the destination.

<figure>
  <img src="../../../../../.gitbook/assets/image (1080).png" alt="Metadata diff showing insertions and deletions">
  <figcaption>Metadata diff view</figcaption>
</figure>

<figure>
  <img src="../../../../../.gitbook/assets/image (1082).png" alt="Expanded inline diff with download option">
  <figcaption>Inline diff and download options</figcaption>
</figure>

## Commit Status Types

- **Completed**: Successful commit/merge.
- **Failed**: Validation/deployment failed.
- **Merge Conflicts**: Conflicting files during merge.
- **Auto Rejected**: Review not completed in time.
- **Review Pending**: Awaiting reviewer action.
- **No Modifications**: No differences found.

<figure>
  <img src="../../../../../.gitbook/assets/image (1085).png" alt="Completed commit status">
  <figcaption>Completed status</figcaption>
</figure>

## Filtering Commits

Filter options include:

- Repository and Branch
- Content (label, revision, comments)
- Pending Approvals
- Date Range
- Commit Type
- Author
- Board (Salesforce or Vlocity)

<figure>
  <img src="../../../../../.gitbook/assets/image (1092).png" alt="Filter by repository and branch">
  <figcaption>Repository and branch filters</figcaption>
</figure>

## Delete Commits/Merges

Only users who created the commit or org admins can delete commits (unmerged only).

<figure>
  <img src="../../../../../.gitbook/assets/image (1100).png" alt="Delete commit option in menu">
  <figcaption>Delete Commit option</figcaption>
</figure>

**Note:**
- Deleted commits are not recoverable.
- An email notification is sent upon deletion.

## Commit Workspace

Parallel commits from the same source org to different VC branches are shown in the **Commit Workspace**. Users may remove commits queued for deployment.

<figure>
  <img src="../../../../../.gitbook/assets/image (1103).png" alt="Commit workspace showing queued commits">
  <figcaption>Commit queue overview</figcaption>
</figure>

## Deployment Workspace

Prevalidated deployments waiting in the queue are listed in the **Deployment Workspace**.

<figure>
  <img src="../../../../../.gitbook/assets/image (1105).png" alt="Deployment workspace with pending validations">
  <figcaption>Prevalidation queue view</figcaption>
</figure>
