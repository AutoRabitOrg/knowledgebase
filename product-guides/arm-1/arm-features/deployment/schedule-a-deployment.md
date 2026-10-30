# Schedule a Deployment

## Scheduled Deployments with Approval Workflow – User Guide

### Overview

The **Scheduled Deployments with Approval Workflow** enhancement in AutoRABIT ARM allows users to schedule deployments for a specific date, time, and time zone.

This feature enables organizations to execute deployments automatically during planned maintenance windows without requiring manual intervention.

For deployments requiring approval, ARM follows the existing **L1/L2 approval workflow**, ensuring that all required approvals are completed before the scheduled deployment executes.

**Availability:** New UI Only\
**Module:** Deployment\
**Feature Flag:** `SCHEDULED_DEPLOYMENTS`

### Key Features

* **Schedule Deployments:** Configure deployments to execute automatically at a selected date, time, and time zone.
* **Approval Workflow Integration:** Supports existing L1/L2 approval processes before deployment execution.
* **Edit Scheduled Deployments:** Modify the scheduled date and time before execution.
* **Cancel Scheduled Deployments:** Cancel pending schedules without deploying changes.
* **Deploy Now:** Execute a scheduled deployment immediately, superseding its existing schedule.
* **Post-Validation Scheduling:** Schedule actual deployments after successful validation.

### How to Schedule a Deployment

1. Log in to AutoRABIT ARM and navigate to **Deployment → Create Deployment**.
2. Configure the deployment source, destination org, and metadata components.
3. Complete the **Deployment Settings** step.
4. Navigate to **Review & Deploy**.
5. Click **Schedule**.
6. Select the required **Date, Time, and Time Zone**.
7. Confirm the schedule.

Once scheduled, the deployment appears in **Deployment History** with the status **Scheduled**.

<figure><img src="../../../../.gitbook/assets/image (3294).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3295).png" alt="" width="185"><figcaption></figcaption></figure>

### Scheduling Deployments After Validation

<figure><img src="../../../../.gitbook/assets/image (3296).png" alt=""><figcaption></figcaption></figure>

ARM also supports scheduling deployments that have already completed validation successfully.

1. Create a deployment and enable **Validate Only**.
2. Submit the deployment for validation.
3. Once validation completes successfully, navigate to **Deployment → History**.
4. Select the validated deployment.
5. Click **Schedule deployment**.
6. Configure the preferred date, time, and time zone.
7. Confirm the schedule.

**Note:** The Schedule option is not available during the initial Validate-Only operation. Users can schedule the actual deployment only after validation completes successfully.

### Approval Workflow for Scheduled Deployments

If the destination Salesforce org requires approval, ARM follows the existing approval workflow.

1. When a deployment is scheduled, ARM initiates the configured approval process.
2. The deployment moves through **L1 Approval Pending** and **L2 Approval Pending**, as applicable.
3. Approvers review and approve the deployment using the existing approval process.
4. Once all required approvals are completed, the deployment remains scheduled until the configured execution time.
5. ARM automatically executes the deployment at the scheduled time.

**Important:** Deployments requiring approval will execute only after all required approvals are completed. If approvals are not completed before the scheduled time, the deployment will not execute automatically.

### Managing Scheduled Deployments

Users can manage scheduled deployments through **Deployment → History**.

#### Edit a Scheduled Deployment

<figure><img src="../../../../.gitbook/assets/image (3297).png" alt=""><figcaption></figcaption></figure>

1. Navigate to **Deployment → History**.
2. Select the deployment with the **Scheduled** status.
3. Click **Edit Schedule**.
4. Update the required date and time.
5. Click **Save Schedule**.

The deployment schedule is updated with the new execution time.

_Screenshot 2: Edit Schedule option in Deployment History._

#### Cancel a Scheduled Deployment

1. Navigate to **Deployment → History**.
2. Select the scheduled deployment.
3. Click **Cancel Schedule**.
4. Confirm the cancellation.

The scheduled execution is cancelled, and the deployment remains available as a draft. No deployment is performed.

#### Deploy Immediately

Users can execute a scheduled deployment immediately by selecting **Deploy Now** from Deployment History.

This action supersedes the existing schedule and initiates the deployment immediately, subject to any applicable approval requirements.
