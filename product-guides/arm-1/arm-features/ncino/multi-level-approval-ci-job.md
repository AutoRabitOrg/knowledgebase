# Multi-Level Approval - CI Job

**CI Job Approval Workflow**

**User Guide**

_Multi-level Deployment and Commit Approval Flow_

This guide describes the CI Job approval workflow from approval configuration through build execution, approval processing, deployment and commit execution, and final build review. a

## 1. Configure Approval Settings

Approval setup defines who can approve deployment and commit requests. The configuration is the foundation for all approval actions shown later in the CI Job workflow.

### Approval settings configuration

![](<../../../../.gitbook/assets/Unknown image (40)>)

The approval workflow begins in My Account, where approval settings are maintained for deployment, data deployment, and feature commit activities. The Deployment - Approval Settings, Data Deployment - Approval Settings, and Feature Commit - Approval Settings sections define the Salesforce orgs, repositories, branches, and Level 1 and Level 2 approvers that will be available during CI Job configuration.

## 2. Associate Approval Levels with the CI Job

After approval levels are configured, they are assigned to a CI Job during destination and commit setup. The selected approvers determine who participates in each approval stage after the build is triggered.

### Destination approval fields are available during CI Job setup

![](<../../../../.gitbook/assets/Unknown image (1) (1) (1) (1)>)

During CI Job configuration, the Destination step displays separate approval fields for deployment and commit activities. Selecting the destination org makes the Level 1 approval and Level 2 approval fields available for deployment. The commit section provides the corresponding Commit level 1 approval and Commit level 2 approval fields after repository and branch information is selected.

### Level 2 deployment approval selection

![](<../../../../.gitbook/assets/Unknown image (2) (1) (1) (1)>)

The Level 2 approval field provides the list of configured approvers for the selected destination. This selection completes the secondary deployment approval configuration for the job and determines who can review the deployment request at the second approval level.

### Commit approval selection after branch selection

![](<../../../../.gitbook/assets/Unknown image (3) (1) (1) (1)>)

After the repository and branch are selected, the commit approval fields become active. The Commit level 1 approval list displays available approvers for the first commit approval stage. The approval selection is linked to the configured repository and branch context.

### Commit Level 2 approval selection

![](<../../../../.gitbook/assets/Unknown image (4) (1) (1) (1)>)

The Commit level 2 approval field captures the final commit approver for the job. A note on the page explains that deployment and commit approvals that remain inactive for 14 days from the time of job creation are automatically rejected, ensuring that pending approval requests do not remain open indefinitely.

## 3. Trigger the Build and Review Initial Status

The build trigger starts the approval-controlled lifecycle. The build status, deployment status, and commit status columns show how the request progresses after submission.

### CI Job List with trigger build action

![](<../../../../.gitbook/assets/Unknown image (5) (1) (1) (1)>)

After the CI Job is configured, it appears in the CI Job List. The Trigger build action is available from the Actions column and starts the approval-controlled build workflow for the selected job.

### Trigger build panel with approval details

![](<../../../../.gitbook/assets/Unknown image (6) (1) (1) (1)>)

The Trigger build panel summarizes the CI job details, source details, destination details, selected deployment approvers, and selected commit approvers. This review confirms the approval chain before the build is submitted.

### CI Job History after build submission

![](<../../../../.gitbook/assets/Unknown image (7) (1) (1)>)

Once the build is submitted, the CI Job History page displays the new build record. The build status begins processing while the deployment and commit approval states are tracked separately in their respective columns.

### Deployment status waiting for L1 approval

![](<../../../../.gitbook/assets/Unknown image (8) (1) (1)>)

The Deploy status icon displays the tooltip Waiting for L1 Approval. This indicates that the build has completed the initial stage and the deployment request is pending review by the Level 1 deployment approver.

### Commit status waiting for L1 approval

![](<../../../../.gitbook/assets/Unknown image (9) (1) (1)>)

The Commit status icon displays the tooltip Waiting for L1 Approval. This indicates that the commit request is also pending Level 1 approval as part of the same first approval stage.

### Build action menu before approval completion

![](<../../../../.gitbook/assets/Unknown image (10) (1) (1)>)

The build action menu provides access to Build list, Build results, Build info, Build changes, Edit approvals, Notify approvals, and Build log download. These actions support build review, approval management, and notification handling while the request is pending approval.

### Build list view for the selected job

![](<../../../../.gitbook/assets/Unknown image (11) (1) (1)>)

The Build list option opens the CI Job Builds view for the selected job. The build record shows build number, build name, triggered date, triggered by, build status, deploy status, commit status, and available actions.

### Approval status in the build list

![](<../../../../.gitbook/assets/Unknown image (12) (1) (1)>)

Within the build list, the Deploy status and Commit status columns display approval-state icons. Hovering over these icons shows the current approval state, allowing the approval progress to be monitored directly from the build record.

### Build action menu in the build list

![](<../../../../.gitbook/assets/Unknown image (13) (1)>)

The Actions menu in the build list provides the same workflow options available from CI Job History. Edit Approvals and Notify Approvals remain available while approvals are pending.

## 4. Manage Approvers and Notifications

Pending builds provide controls to update approval assignments and resend approval notifications. These actions keep the approval flow manageable without recreating the build.

### Edit Approvals panel

![](<../../../../.gitbook/assets/Unknown image (14) (1)>)

The Edit Approvals panel displays the current deployment and commit approval assignments. Deployment approvals and Commit approvals are separated into Level 1 and Level 2 fields, allowing approvers to be reviewed or updated without recreating the build.

### Updating deployment Level 1 approvers

![](<../../../../.gitbook/assets/Unknown image (15) (1)>)

The Level 1 dropdown under Deployment approvals displays available approvers. Updating this list changes who can act on the first deployment approval stage for the current build.

### Saving updated approval assignments

![](<../../../../.gitbook/assets/Unknown image (16) (1)>)

After approval assignments are reviewed or updated, the Save action stores the changes. Updated approvers are used for the remaining approval actions in the workflow.

### Deploy Approval and Commit Approval actions

![](<../../../../.gitbook/assets/Unknown image (17) (1)>)

The action menu now exposes Deploy approval and Commit approval. These actions open the approval decision panels for the pending deployment and commit requests.

### Notify Approvals action

![](<../../../../.gitbook/assets/Unknown image (18) (1)>)

The Notify approvals action sends or resends approval notifications to the configured approvers. This is useful when pending approval requests need to be brought back to the attention of the assigned approvers.

## 5. Complete Level 1 Approvals

The first approval stage consists of Deployment L1 approval followed by Commit L1 approval. Both Level 1 approvals must be completed before the workflow moves to Level 2.

### Deployment L1 approval panel

![](<../../../../.gitbook/assets/Unknown image (19) (1)>)

The Deployment L1 Approvals panel opens from the Deploy approval action. The approver selects an approval action, either Approve or Reject, and provides comments before submitting the decision.

### Deployment L1 approval action selected

![](<../../../../.gitbook/assets/Unknown image (20) (1)>)

After Approve is selected, the comments field remains required. The Submit action is available, but the approval cannot be completed until comments are provided.

### Deployment L1 comment validation

![](<../../../../.gitbook/assets/Unknown image (21) (1)>)

If the approval decision is submitted without comments, the system displays the warning Please enter a comment. This validation ensures that each approval decision includes an audit comment.

### Deployment L1 approval submitted with comments

![](<../../../../.gitbook/assets/Unknown image (22) (1)>)

After comments are entered, the approver submits the Deployment L1 approval. The workflow records the approval decision and progresses to the next approval activity in the sequence.

### Workflow moves to Commit L1 approval

![](<../../../../.gitbook/assets/Unknown image (23) (1)>)

After Deployment L1 approval is completed, the Commit status displays Waiting for L1 Approval. This confirms that the first-level commit approval is the next pending action in the same approval stage.

### Commit L1 status remains pending

![](<../../../../.gitbook/assets/Unknown image (24) (1)>)

The build remains available in the CI Job Builds view while the commit approval awaits action. The Deploy status reflects the completed deployment approval stage, and the Commit status continues to indicate the pending Level 1 commit approval.

### Commit Approval action selected

![](<../../../../.gitbook/assets/Unknown image (25) (1)>)

The Commit approval action is selected from the build action menu to open the approval panel for the pending Commit L1 approval request.

### Commit L1 approval panel

![](<../../../../.gitbook/assets/Unknown image (26) (1)>)

The Commit L1 Approvals panel presents the same approval decision model as deployment approvals. The approver selects Approve or Reject and provides comments before submission.

### Commit L1 approval submitted with comments

![](<../../../../.gitbook/assets/Unknown image (27) (1)>)

The Commit L1 approval decision is submitted with comments. Once accepted, the first approval stage is completed for both deployment and commit activities.

## 6. Complete Level 2 Approvals

The second approval stage consists of Deployment L2 approval followed by Commit L2 approval. Completion of these approvals makes the deployment and commit execution actions available.

### Deployment status waiting for L2 approval

![](<../../../../.gitbook/assets/Unknown image (24) (1)>)

After both Level 1 approvals are completed, the workflow advances to the second approval level. The Deploy status icon displays Waiting for L2 Approval, indicating that Deployment L2 approval is pending.

### Commit status waiting for L2 approval

![](<../../../../.gitbook/assets/Unknown image (158)>)

The Commit status icon also displays Waiting for L2 Approval. This confirms that the second approval level is active for both deployment and commit approval paths.

### Second-level approval actions available

![](<../../../../.gitbook/assets/Unknown image (159)>)

The action menu continues to provide Deploy approval and Commit approval while the Level 2 approvals are pending. Each action opens the corresponding Level 2 approval decision panel.

### Deployment L2 approval panel

![](<../../../../.gitbook/assets/Unknown image (160)>)

The Deployment L2 Approvals panel is used by the second-level deployment approver to review the request and select the required approval action.

### Deployment L2 approval action selected

![](<../../../../.gitbook/assets/Unknown image (161)>)

After Approve is selected for Deployment L2, comments are still required before submission. The system applies the same approval-comment rule across all approval levels.

### Deployment L2 comment validation

![](<../../../../.gitbook/assets/Unknown image (162)>)

Submitting Deployment L2 approval without comments displays the warning Please enter a comment. This keeps approval history complete and consistent.

### Deployment L2 approval submitted with comments

![](<../../../../.gitbook/assets/Unknown image (163)>)

After comments are entered, the Deployment L2 approval is submitted. The deployment approval path is completed after this final deployment approval decision.

### Commit status waiting for L2 approval after Deployment L2 completion

![](<../../../../.gitbook/assets/Unknown image (164)>)

After Deployment L2 approval is completed, the Commit status remains Waiting for L2 Approval. This confirms that the final pending approval action is the second-level commit approval.

### Deployment approval completed while commit approval continues

![](<../../../../.gitbook/assets/Unknown image (165)>)

The build list reflects that deployment approval has progressed while commit approval remains pending. The workflow continues until the Commit L2 approval is completed.

### Commit Approval action for L2 review

![](<../../../../.gitbook/assets/Unknown image (166)>)

The Commit approval action opens the Commit L2 approval workflow. This action is used to complete the final approval stage before commit execution becomes available.

### Commit L2 approval panel

![](<../../../../.gitbook/assets/Unknown image (167)>)

The Commit L2 Approvals panel presents the final commit approval decision. The approver selects Approve or Reject and provides comments to complete the review.

### Commit L2 approval submitted with comments

![](<../../../../.gitbook/assets/Unknown image (168)>)

After comments are added, the Commit L2 approval is submitted. This completes the Level 2 approval stage for the commit workflow.

## 7. Review Approved States and Available Actions

After approval completion, the status icons change to Approved and execution actions become available from the build row.

### Deployment approval approved

![](<../../../../.gitbook/assets/Unknown image (169)>)

The Deploy status icon displays Approved after all deployment approval stages are completed. This status confirms that deployment governance requirements are satisfied.

### Deploy action becomes available

![](<../../../../.gitbook/assets/Unknown image (170)>)

After deployment approval is completed, the Deploy action becomes available in the Actions column. This action starts deployment processing for the approved build.

### Commit approval approved

![](<../../../../.gitbook/assets/Unknown image (171)>)

The Commit status icon displays Approved after the Commit L2 approval is completed. This confirms that all configured commit approvals are complete.

### Commit action becomes available

![](<../../../../.gitbook/assets/Unknown image (172)>)

The Commit action becomes available after commit approvals are completed. This action starts commit execution for the approved changes.

### Deploy and Commit actions available

![](<../../../../.gitbook/assets/Unknown image (170)>)

When both deployment and commit approvals are completed, the build provides execution actions for Deploy, Commit, and Deploy & Commit depending on the configured operation.

## 8. Execute Deploy and Commit Operations

Approved builds can be deployed, committed, or executed using the combined Deploy & Commit action. The system displays processing and success indicators during execution.

### Deploy execution starts

![](<../../../../.gitbook/assets/Unknown image (173)>)

Selecting Deploy triggers deployment execution. The system displays Please wait... Triggering deploy... while the deployment request is submitted.

### Deployment trigger success message

![](<../../../../.gitbook/assets/Unknown image (174)>)

After the deployment request is submitted successfully, a Success notification appears. The deployment status then moves into processing until execution completes.

### Deploy action after approval completion

![](<../../../../.gitbook/assets/Unknown image (171)>)

The Deploy action remains visible from the build record when deployment can be executed independently. The tooltip confirms the action label as Deploy.

### Commit execution starts

![](<../../../../.gitbook/assets/Unknown image (175)>)

Selecting Commit triggers commit execution. The system displays Please wait... Triggering commit... while the commit request is submitted.

### Commit trigger success and processing status

![](<../../../../.gitbook/assets/Unknown image (176)>)

After commit execution is submitted, a Success notification appears. Deploy and Commit status icons display processing indicators while the operations complete.

### Post-execution action menu with commit artifacts

![](<../../../../.gitbook/assets/Unknown image (177)>)

After commit execution begins, the action menu includes commit-related artifacts such as Commit log, Commit revision log, and Commit file diff in addition to build results and build information.

### Build completes with commit ID and successful statuses

![](<../../../../.gitbook/assets/Unknown image (178)>)

When processing completes, the build record displays the generated Commit ID and successful status indicators for Build status, Deploy status, and Commit status. This confirms that the approval-controlled workflow has completed successfully.

## 9. Review Completed Build Details

After execution, the completed build can be reviewed through history, action menus, and the Build Information panel, which provides approval and execution traceability.

### CI Job History after completion

![](<../../../../.gitbook/assets/Unknown image (179)>)

The completed build is also visible from CI Job History. The status indicators allow completed approval-controlled builds to be reviewed alongside other CI Job runs.

### Build list refresh or processing state

![](<../../../../.gitbook/assets/Unknown image (180)>)

The build list may briefly display a processing overlay while status updates are refreshed. This indicates that the system is updating the build record after execution.

### Build Info action

![](<../../../../.gitbook/assets/Unknown image (181)>)

The Build info option is available from the action menu after workflow completion. This option opens a consolidated panel containing build, deployment, commit, and approval information.

### Build Information panel

![](<../../../../.gitbook/assets/Unknown image (182)>)

The Build Information panel provides a centralized audit view of the completed build. It displays job details, build number, build name, build status, deploy status, commit status, deployed Salesforce org, trigger information, Level 1 and Level 2 approvers, and the comments captured during deployment and commit approvals.

## CI Jobs: Rerun Builds and Manage Approvals

The following flow follows the CI Job through a new build submission and the resulting approval status review. It explains how the deployment type determines which approval selections are relevant, and how the submitted build is monitored from CI Job History.

## Start a new build from CI Job History

The nCino > CI Job History page provides the starting point for rerunning an existing CI Job. The table presents previous build entries and their Build status, Deploy status, and Commit status. Locate the intended CI Job and use its available build action to open the Trigger build panel. This creates a new build attempt without changing the earlier history entry.

<figure><img src="../../../../.gitbook/assets/image (3298).png" alt=""><figcaption></figcaption></figure>

<p align="center">CI Job History: identify the CI Job and its available actions</p>

The Trigger build panel retains the selected job context. The CI job details, Source details, and Destination details sections identify the source organization, deployment destination, and commit target associated with the job. Review these values before entering the inputs for the new build.

<figure><img src="../../../../.gitbook/assets/image (3299).png" alt=""><figcaption></figcaption></figure>

<p align="center">Trigger build: verify job context and destination information</p>

## Define the rerun operation

In Build inputs, provide a Build label and, where appropriate, a Build comment and Build notes. The Deployment type controls the requested operation: Commit and deploy performs both actions; Deploy only requests deployment; Commit only requests a repository commit. Select the option that matches the intended rerun. Approval selections are relevant to the operations enabled for that build.

<figure><img src="../../../../.gitbook/assets/image (3300).png" alt=""><figcaption></figcaption></figure>

<p align="center">Deployment type and approval-related controls</p>

When approval controls are available, open the corresponding approver selector. The selectable entries are presented within the control, allowing the appropriate approvers to be chosen for the configured level. The available choices depend on the approval setup associated with the CI Job.

<figure><img src="../../../../.gitbook/assets/image (3301).png" alt=""><figcaption></figcaption></figure>

<p align="center">Open the approver list for the selected operation</p>

## Configure the approval levels

For an approval-enabled deployment or commit, the first approval stage is Level 1. Open the Level 1 selector and choose the required approvers. Where multiple selections are supported, the field summarizes the selected entries. Review the displayed selection before moving to the next approval level.

<figure><img src="../../../../.gitbook/assets/image (3302).png" alt=""><figcaption></figcaption></figure>

<p align="center">Select approvers for the first approval level</p>

<figure><img src="../../../../.gitbook/assets/image (3303).png" alt=""><figcaption></figcaption></figure>

<p align="center">Review the selected Level 1 approvers</p>

Continue within the approval controls to include any additional approvers required by the job configuration. The selections should reflect the intended approval routing before the build is submitted.

<figure><img src="../../../../.gitbook/assets/image (3304).png" alt=""><figcaption></figcaption></figure>

<p align="center">Add approvers to the relevant selection</p>

The second approval stage is Level 2. Open its selector and choose the approvers responsible for the subsequent review. Level 1 and Level 2 remain distinct approval stages; the build proceeds through the configured stages rather than treating every selected approver as part of one undifferentiated list.

<figure><img src="../../../../.gitbook/assets/image (3305).png" alt=""><figcaption></figcaption></figure>

<p align="center">Open the next approval-level selector</p>

<figure><img src="../../../../.gitbook/assets/image (3306).png" alt=""><figcaption></figcaption></figure>

<p align="center">Select Level 2 approvers</p>

<figure><img src="../../../../.gitbook/assets/image (3307).png" alt=""><figcaption></figcaption></figure>

<p align="center">Review the selected approvers for the next level</p>

After completing the relevant selectors, verify that the required deployment and/or commit approval fields reflect the intended approvers. For a combined Commit and deploy build, the approval information for both operations must be considered.

<figure><img src="../../../../.gitbook/assets/image (3308).png" alt=""><figcaption></figcaption></figure>

<p align="center">Review the completed approval selections</p>

<figure><img src="../../../../.gitbook/assets/image (3309).png" alt=""><figcaption></figcaption></figure>

<p align="center">Confirm the build inputs before submission</p>

## Trigger the rerun and return to history

Select Trigger build after confirming the Build label, Deployment type, and applicable approvers. The interface processes the submission and returns to CI Job History. Submission initiates the build workflow; it does not by itself mean that deployment or commit approval has been completed.

<figure><img src="../../../../.gitbook/assets/image (3310).png" alt=""><figcaption></figcaption></figure>

<p align="center">Trigger build: submission in progress</p>

<figure><img src="../../../../.gitbook/assets/image (3311).png" alt=""><figcaption></figcaption></figure>

<p align="center">CI Job History: the new build appears in the history</p>

## Interpret approval-related statuses

The newly submitted build is tracked using separate Build status, Deploy status, and Commit status indicators. Inspect the relevant operation status rather than relying only on the overall build result. Hovering over a status icon displays its current meaning, including an approval-waiting state when the corresponding operation has not yet received the required approval.

<figure><img src="../../../../.gitbook/assets/image (3312).png" alt=""><figcaption></figcaption></figure>

<p align="center">Inspect the deployment status tooltip</p>

<figure><img src="../../../../.gitbook/assets/image (3313).png" alt=""><figcaption></figcaption></figure>

<p align="center">Inspect the commit status tooltip</p>

For a CI Job configured with multi-level approvals, the applicable Level 1 approvals are completed before the workflow advances to Level 2. Once the required approvals are obtained, the corresponding deployment or commit can proceed according to the existing CI Job approval workflow. The final result is reflected in the operation-specific status fields.

## Scheduled reruns while approval is pending

When approvers are enabled, a build that is awaiting approval must complete the required approval and subsequent deployment and/or commit before the next scheduled execution. This prevents a new scheduled build from being created while the earlier build remains blocked in the approval workflow.

The CI Job History and build details remain the reference points for reviewing the build outcome and determining whether a further rerun is appropriate.

## Key System Behaviors

Approval inactivity handling: Deployment and commit approvals that remain inactive for 14 days from the time of job creation are automatically rejected.

Mandatory comments: Comments are required for every approval decision. The system displays Please enter a comment when an approval is submitted without comments.

Status visibility: The icons identify current states such as Waiting for L1 Approval, Waiting for L2 Approval, Approved, Deploy, Commit, and Deploy & Commit.

Approval sequencing: Deployment L1 and Commit L1 are completed before the workflow proceeds to Deployment L2 and Commit L2.

Execution gating: Deploy, Commit, and Deploy & Commit actions become available only after the required approval stages are completed.

Auditability: Build Information, approval comments, commit logs, revision logs, and file diffs provide traceability after the workflow completes.
