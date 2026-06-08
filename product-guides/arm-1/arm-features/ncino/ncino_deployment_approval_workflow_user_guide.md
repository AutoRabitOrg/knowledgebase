# nCino\_Deployment\_Approval\_Workflow\_User\_Guide

**nCino Deployment Approval Workflow**

User Guide

## Overview

The nCino Deployment Approval workflow adds controlled review to deployment and commit activities. Approval levels are configured first, then selected during deployment setup, tracked in Deployment History, and completed through Level 1 and Level 2 approval actions before deployment and commit execution can proceed.

## Approval Configuration

### Configure approval settings

The approval workflow begins in My Account, where deployment, data deployment, and feature commit approval settings are mapped to Salesforce orgs, repositories, and branches. The configured Level 1 approver and Level 2 approver fields define the approver groups available later in the deployment workflow. Saving these settings makes the approval levels available during nCino deployment and commit configuration.

![](<../../../../.gitbook/assets/Unknown image (115)>)

## Deployment History and Workflow Entry Point

### Review deployment history

The Deployment History page displays deployment records with build, deploy, commit, and post deploy status indicators. The status columns provide the first operational view of whether a deployment has completed, failed, or is waiting for approval. The action menu remains the central location for reviewing build details, approval actions, notifications, and logs.

![](<../../../../.gitbook/assets/Unknown image (116)>)

## Configuring Approvals During Deployment Setup

### Select deployment approval approvers

During nCino deployment configuration, the Destination step presents approval fields when the Deploy to option is enabled. The Level 1 approval field is used to select the first-level deployment approvers for the selected destination org.

![](<../../../../.gitbook/assets/Unknown image (117)>)

### Select Level 2 deployment approvers

The Level 2 approval field is configured alongside the destination org. Selecting Level 2 approvers prepares the deployment request for a second approval stage after Level 1 approval is completed.

![](<../../../../.gitbook/assets/Unknown image (118)>)

### Configure commit approval approvers

When Commit to is enabled, the commit approval fields become part of the same Destination step. The Commit level 1 approval and Commit level 2 approval fields define the commit approval path that runs along with the deployment approval path.

![](<../../../../.gitbook/assets/Unknown image (119)>)

### Review configured approval selections

After approvers are selected for deployment and commit approval levels, the Destination step displays the selected values. The approval inactivity note explains that deployment and commit approvals remaining inactive for 14 days from job creation are automatically rejected.

![](<../../../../.gitbook/assets/Unknown image (120)>)

### Preview deployment details

The Preview step consolidates source details, destination details, job settings, and approval selections before execution. This screen confirms the destination org, deployment approval levels, commit repository, commit branch, and commit approval levels before the deployment request is submitted.

![](<../../../../.gitbook/assets/Unknown image (121)>)

## Submitting and Reviewing the Deployment Request

### Return to deployment history

After the deployment is submitted, the Deployment History page displays the latest deployment entry. The record becomes the control point for monitoring statuses and accessing actions throughout the approval workflow.

![](<../../../../.gitbook/assets/Unknown image (122)>)

### Access the Deploy action

The Deploy action is available from the deployment record when the workflow allows deployment execution.

![](<../../../../.gitbook/assets/Unknown image (123)>)

### Review configured approvers before deployment

The Deploy panel displays the configured approvers for Deployment Level 1, Deployment Level 2, Commit Level 1, and Commit Level 2. This provides a final review of the approval chain before the deployment request is submitted.

![](<../../../../.gitbook/assets/Unknown image (124)>)

### Track deployment approval status

The deployment status indicator displays Waiting for L2 Approval when the request has advanced past the first approval level and is waiting for second-level deployment approval. Hovering over the icon reveals the exact status.

![](<../../../../.gitbook/assets/Unknown image (125)>)

### Preview approval details before deploy and commit

The Preview step can also display configured approval details in the context of review deployment and deploy-and-commit actions. This confirms the approval selections that govern the request before execution continues.

![](<../../../../.gitbook/assets/Unknown image (126)>)

## Approval Status Visibility and Workflow Actions

### Identify Waiting for L1 Approval in Deploy Status

The Deploy Status column displays Waiting for L1 Approval when the deployment approval request is pending at the first approval level. This status confirms that deployment cannot proceed until the first-level deployment approval is completed.

![](<../../../../.gitbook/assets/Unknown image (127)>)

### Identify Waiting for L1 Approval in Commit Status

The Commit Status column displays Waiting for L1 Approval when the commit approval request is pending at the first approval level. The deployment and commit approval paths are visible together on the same deployment record.

![](<../../../../.gitbook/assets/Unknown image (128)>)

### Open workflow actions

The action menu provides access to review and approval functions, including Summary, Revisions, Build Approvals, and Notify Approvals. These options support monitoring, approval action, and reminder notification workflows for the selected deployment.

![](<../../../../.gitbook/assets/Unknown image (129)>)

## Managing Approval Assignments and Notifications

### Edit approvers

The Edit Approvals panel allows approvers to be reviewed or updated after the deployment record is created. Deployment approvals and commit approvals are separated into Level 1 and Level 2 fields so each stage can be managed independently.

![](<../../../../.gitbook/assets/Unknown image (130)>)

### Modify approver selections

Opening an approval selector displays the available approver list. Additional approvers can be selected when approval responsibility needs to be adjusted before the pending stage is completed.

![](<../../../../.gitbook/assets/Unknown image (131)>)

### Save updated approvers

After the approval selections are updated, the Save action applies the changes to the deployment record. Updated approver assignments are then used for the remaining approval workflow.

![](<../../../../.gitbook/assets/Unknown image (132)>)

### Notify approvers

The Notify Approvals action is available from the action menu. It sends or resends approval notifications to the configured approvers so pending approval requests can be acted upon.

![](<../../../../.gitbook/assets/Unknown image (133)>)

## Deployment Revision Review

### Open deployment revisions

The Deployment Revisions page displays revision-level status for the selected deployment label. The same status indicators are available here, including Waiting for L1 Approval in the Deploy Status column.

![](<../../../../.gitbook/assets/Unknown image (134)>)

### Review commit approval status in revisions

The Deployment Revisions page also shows the Commit Status column. When the commit request is pending, the tooltip displays Waiting for L1 Approval.

![](<../../../../.gitbook/assets/Unknown image (135)>)

## Completing Level 1 Approvals

The approval flow progresses as a single coordinated workflow. Deployment L1 approval is completed first, followed by Commit L1 approval. The status icons show which approval action is waiting at each stage.

### Select Deploy Approval

The Deploy Approval action opens the approval dialog for the current deployment approval stage. This action is used by the assigned approver to submit the deployment approval decision.

![](<../../../../.gitbook/assets/Unknown image (136)>)

### Complete Deployment L1 approval

The Deployment L1 Approvals dialog presents the approval action selector with Approve and Reject options. The approver selects the appropriate action and provides comments before submitting the decision.

![](<../../../../.gitbook/assets/Unknown image (137)>)

### Validate approval comments

Approval comments are mandatory. When the Submit action is attempted without comments, the system displays the warning Please enter a comment. The request cannot proceed until comments are provided.

![](<../../../../.gitbook/assets/Unknown image (138)>)

### Move deployment approval to L2

After Deployment L1 approval is submitted successfully, the Deploy Status changes to Waiting for L2 Approval. This indicates that the deployment request has progressed to the second approval level.

![](<../../../../.gitbook/assets/Unknown image (139)>)

### Continue with Commit L1 approval

The Commit Status remains Waiting for L1 Approval until the first-level commit approver submits a decision. This keeps the deployment and commit approval paths visible as part of the same workflow.

![](<../../../../.gitbook/assets/Unknown image (140)>)

### Open Commit Approval

The Commit Approval action opens the approval dialog for the current commit approval stage. This action becomes the next required activity after Deployment L1 approval has progressed.

![](<../../../../.gitbook/assets/Unknown image (141)>)

### Complete Commit L1 approval

The Commit L1 Approvals dialog captures the approval decision and comments for the commit workflow. Submitting the approval advances the commit approval path to the next level.

![](<../../../../.gitbook/assets/Unknown image (142)>)

## Completing Level 2 Approvals

After the Level 1 approvals are completed, the workflow proceeds to Level 2. Deployment L2 approval is completed first, followed by Commit L2 approval.

### Review Waiting for L2 Approval after Commit L1

After the first-level approvals are completed, the workflow shows the request waiting for second-level approval. The status indicators identify the remaining approval stage before execution actions become available.

![](<../../../../.gitbook/assets/Unknown image (143)>)

### Confirm deployment L2 pending status

The Deploy Status tooltip displays Waiting for L2 Approval while the deployment approval request is awaiting the second-level approver decision.

![](<../../../../.gitbook/assets/Unknown image (139)>)

### Open the next approval action

The action menu is used again to access the remaining approval action. The available approval option corresponds to the current pending approval state.

![](<../../../../.gitbook/assets/Unknown image (144)>)

### Complete Deployment L2 approval

The Deployment L2 Approvals dialog records the second-level deployment approval decision. The approver selects the approval action, enters comments, and submits the decision to complete the deployment approval path.

![](<../../../../.gitbook/assets/Unknown image (145)>)

### Open Commit L2 approval

After Deployment L2 approval is completed, the workflow proceeds to the commit approval path at Level 2. The Commit Approval action opens the final commit approval dialog.

![](<../../../../.gitbook/assets/Unknown image (146)>)

### Complete Commit L2 approval

The Commit L2 Approvals dialog captures the final commit approval decision and comments. Once submitted, the commit approval path is completed.

![](<../../../../.gitbook/assets/Unknown image (147)>)

## Approved State and Summary Review

### Confirm deployment approval completion

The Deploy Status indicator changes to Approved after all required deployment approvals are completed. The tooltip confirms that deployment approval has been approved.

![](<../../../../.gitbook/assets/Unknown image (148)>)

### Confirm commit approval completion

The Commit Status indicator changes to Approved after all required commit approvals are completed. At this point, the deployment and commit approval requirements have both been satisfied.

![](<../../../../.gitbook/assets/Unknown image (149)>)

### Review deployment summary

The Deployment Summary panel provides a consolidated view of deployment metadata, source and destination details, approval status, and approval comments. This view supports audit review after approval decisions are recorded.

![](<../../../../.gitbook/assets/Unknown image (150)>)

## Executing Approved Deployment and Commit Actions

### Deploy approved changes

The Deployment Revisions page provides the Deploy action after approvals are completed. The tooltip identifies the deploy action that initiates deployment execution for the approved revision.

![](<../../../../.gitbook/assets/Unknown image (151)>)

### Commit approved changes

The Commit action becomes available when commit approval is complete. The tooltip identifies the commit action used to initiate the commit operation.

![](<../../../../.gitbook/assets/Unknown image (152)>)

### Deploy and commit together

The Deploy & Commit action initiates both deployment and commit processing from the approved revision. This option is available when both deployment and commit approval paths are completed.

![](<../../../../.gitbook/assets/Unknown image (153)>)

{% hint style="info" %}
### Note:-

### Review completed revision actions

After approval completion, the revision row displays successful build, deploy, and commit status indicators with execution actions available from the Actions column. This confirms that the record is ready for approved execution or review.
{% endhint %}

### Monitor deployment processing

When deployment is triggered, a processing overlay displays Please wait... and Triggering deploy.... This indicates that the system has accepted the deployment action and is initiating processing.

![](<../../../../.gitbook/assets/Unknown image (154)>)

![](<../../../../.gitbook/assets/Unknown image (155)>)

### Monitor deployment processing

When commit is triggered, a processing overlay displays Please wait... and Triggering commit.... This indicates that the system has accepted the commit request and is initiating processing

![](<../../../../.gitbook/assets/Unknown image (156)>)

![](<../../../../.gitbook/assets/Unknown image (157)>)
