# Commits Summary

## Overview

In AutoRABIT ARM, the **Commits Summary** screen provides detailed information about each commit or merge, including diffs of modifications. Commits are organized by the date they were made in ARM. By default, only commits by the logged-in user are displayed in reverse chronological order (most recent first).

## Accessing the Commits Screen

1. Navigate to **Version Control > Commits** to access the **Commits** screen.
2. For optimal viewing, set your browser's zoom level to **80%** (Chrome/Firefox).

## Viewing Commits

* To view all commits (including those by teammates), Click the **Created By Me** switch to the left.
* To filter commits pending reviewer approval, Click the **Pending Approvals** switch to the right.
*   Use the search field to filter commits by Commit Type, Board, Created by and Created Range, revision number, or comment. _Note: Search is case-sensitive._\
    \


    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-17 at 8.40.55 PM.png" alt=""><figcaption></figcaption></figure>

## Commit Details

Each commit entry displays:

* **Commit Type Initials**:
  * PV: Prevalidation Commit
  * EZ: EZ-Commit
  * M: Merge Commit
  * VM: Validate and Merge
  * BB: Branching Baseline
  * RC: Revert Commit
  * CI: Commit from CI Job
  * DR: Dry Run
  * EC: External Commit
* Commit label name
* Commit message
* Committer's username
* Commit creation date
* Version Control repository, destination, and source branch details
* Salesforce Org details (if applicable)
* Commit Revision label
* Commit/Merge status

## Quick Merge

Quick Merge allows direct merging from the Commits screen without navigating to the New Merge screen.

1. Hover over the three dots beside the desired commit.
2. Click **Quick Merge**.
3.  Confirm the action in the pop-up.\


    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-17 at 8.43.45 PM.png" alt=""><figcaption></figcaption></figure>

**Note:** Quick Merge is not available for:

* Prevalidation Merge commits pending approval
* Already merged commits

## Detailed View

1.  Hover over the three dots beside a commit and click **Detailed View**.\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1989).png" alt="" width="276"><figcaption></figcaption></figure>

The detailed view includes:

* Commit details
* Merge/EZ-Commit configuration
* Pull Request section (for EZ-Commits only)
* Reviewer comments
* Metadata diffs
* Deployment validation
* Code Analysis
*   Logs and ALM integration\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1990).png" alt=""><figcaption></figcaption></figure>

    \


    <figure><img src="../../../../../.gitbook/assets/image (1991).png" alt=""><figcaption><p>Visual display of Commit steps</p></figcaption></figure>

    \


    <figure><img src="../../../../../.gitbook/assets/image (1992).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-17 at 8.55.45 PM.png" alt=""><figcaption><p>Commit details Report panel</p></figcaption></figure>

## Code Analysis File

Static Code Analysis (SCA) is part of the security development lifecycle. Tools include ApexPMD, Checkmarx, Salesforce Scanner, and CodeScan. Violations are displayed by file and line\


<figure><img src="../../../../../.gitbook/assets/image (1993).png" alt=""><figcaption><p>Sample Static Code Analysis Report in EZ Commit details</p></figcaption></figure>

## Files Changed

ARM compares metadata changes between branches/orgs. RED indicates deletions or changes from the source; GREEN indicates changes in the destination.\
\


<figure><img src="../../../../../.gitbook/assets/image (1995).png" alt=""><figcaption><p>Metadata Diff view</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1996).png" alt=""><figcaption><p>Inline diff and download options</p></figcaption></figure>

## Commit Status Types

* **Completed**: Successful commit/merge.
* **Failed**: Validation/deployment failed.
* **Merge Conflicts**: Conflicting files during merge.
* **Auto Rejected**: Review not completed in time.
* **Review Pending**: Awaiting reviewer action.
*   **No Modifications**: No differences found.\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1997).png" alt=""><figcaption></figcaption></figure>

## Filtering Commits

Filter options include:

* Repository and Branch
* Created by me
* All or Pending Approvals
* Pending Approvals
* Date Range
* Commit Type
* Created by
*   Board (Salesforce or Vlocity)\
    \


    <figure><img src="../../../../../.gitbook/assets/image (1998).png" alt=""><figcaption></figcaption></figure>

## Delete Commits/Merges

Only users who created the commit or org admins can delete commits (unmerged only).

<figure><img src="../../../../../.gitbook/assets/image (1999).png" alt=""><figcaption></figcaption></figure>

**Note:**

* Deleted commits are not recoverable.
* An email notification is sent upon deletion.

## Commit Workspace

Parallel commits from the same source org to different VC branches are shown in the **Commit Workspace**. Users may remove commits queued for deployment.

<figure><img src="../../../../../.gitbook/assets/image (1103).png" alt="Commit workspace showing queued commits"><figcaption><p>Commit queue overview</p></figcaption></figure>

## Deployment Workspace

Prevalidated deployments waiting in the queue are listed in the **Deployment Workspace**.

<figure><img src="../../../../../.gitbook/assets/image (1105).png" alt="Deployment workspace with pending validations"><figcaption><p>Prevalidation queue view</p></figcaption></figure>
