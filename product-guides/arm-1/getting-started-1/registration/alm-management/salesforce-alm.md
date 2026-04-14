# Salesforce ALM

## Configuring ALM Integration and Work Item Updates in Salesforce

### Overview

This guide explains how to configure ALM integration in AutoRABIT ARM and enable automatic updates to Salesforce Work Items (such as User Stories or Bugs) based on commit, merge, and CI job activities.

***

### Prerequisites

* Administrator access to AutoRABIT ARM
* A registered Salesforce Org
* Required custom fields available in Salesforce for mapping

***

### Step 1: Register ALM

1. Log in to ARM as an administrator.
2. Navigate to Settings **→ ALM**.
3. Click **Register ALM**.
4. Provide the following details:
   * **ALM Name** – Enter a friendly label
   * **ALM Type** – Select the platform (e.g., Salesforce)

***

### Step 2: Configure Field Mapping for Work Item Updates

To enable automatic updates of Work Items based on commit actions, configure the following fields:

#### a. Salesforce Org

Select the Salesforce Org where Work Item updates should be applied.

#### b. Object / Work Item Type

Choose the object representing Work Items (e.g., `User_Story__c`, `Bug__c`).

#### c. Title Field

Map the field representing the project or feature (e.g., `Project__c`).

#### d. Assignee Field

Select the field that stores the assigned user.

#### e. Status Field

Choose the field that represents Work Item status (e.g., New, In Progress, Closed).

#### f. Comment Field

Select the field where commit-related comments will be added.

***

### Step 3: Configure Post Commit Action

Under **Post Commit Action**, select:

* **Update ALM Work Item Status**

Configure the following fields:

* **ALM Type** – Select the integrated tool (e.g., Salesforce)
* **ALM Label** – Choose the label for the commit
* **ALM Project** – Select project/module (e.g., User Story, Bug)
* **ALM Work Item** – Select the Work Item ID
* **ALM Work Item Status** – Choose the new status (e.g., To Do, Done)
* **Current Status** – Displays current Work Item status

***

### Step 4: Complete the Commit

Click **Commit** after configuration.

#### System Actions

* Performs the commit
* Updates the Work Item status automatically
* Adds commit metadata to the configured comment field

***

### Sample Post-Commit Comment

\[Message] Saas tool Integration-2\[Repository] \*\*\*\*\*\*\*\*\*\*\[Branch] 18235\_test\[Revision] 3637289\[Committed by] user@example.com\[Committed metadata members] {Apex Class=\[A000, A0000]}\
\[Pre-validation Results]Label Name = \*\*\*\*\*\*\*\*\*\*Apex Test Results = NAStatic Analysis = NADeployment Org = NAOverall Validate Deployment Status = NAApproved By = approver@example.com

***

### Integration Settings

By default, Work Items from inactive sprints are hidden.

#### Available Options

* Display work items from inactive sprints
* Enable global filter criteria on work items

#### Additional Configuration

* Select fields/columns to display
* Apply filter criteria to refine Work Item list
* Repeat for multiple fields if needed

Click **Save Settings** after configuration.

**Note:** To remove a filter, use the delete icon next to the rule.

***

### Extended ALM Integration Support

ALM updates are supported across multiple processes:

* Commits
* Merge Requests
* EZ Merge
* CI Jobs

#### Admin Configuration Enhancements

Two new tabs are introduced in ALM configuration:

* **Smart Commits**
* **Merge Request Settings**

These reuse existing ALM configuration and require no additional setup.

***

### CI Job Integration

#### Location

CI → Job Configuration

#### New Option

* **Update ALM Work Item Status**

#### Trigger Conditions

* CI Job Success
* CI Job Warning

When enabled, Work Item status updates automatically after job execution.

***

### EZ Merge & Merge Request Support

* ALM updates trigger automatically after successful merges
* No additional configuration required
* Uses existing field mappings

#### Supported Fields

* ALM Type
* ALM Label
* ALM Project
* Work Item
* New Status
* Current Status

***

### Behavior Summary

* Configure ALM once → works across commits, merges, and CI jobs
* Work Item status updates automatically based on actions
* Comments include execution metadata (commit, merge, or job details)
* Respects role-based access controls

***

### Important Notes & Limitations

#### 1. Handling Multiple Revisions per Work Item

* A single Work Item (User Story / Bug) may have multiple revisions (commits).
* During Merge or CI processes, selecting only a subset of revisions can lead to incomplete tracking.

**Limitation:**

* If only one revision is selected:
  * Work Item status will still be updated
  * Remaining pending changes will not be reflected

**Recommendation:**

* Always select all revisions related to a Work Item to ensure accurate updates.

***

#### 2. Impact of Partial Revision Selection

* Work Item may move to a completed state even if all changes are not deployed.

**Impact:**

* Future changes to the same Work Item will not automatically update status
* Manual updates in Salesforce will be required

***

#### 3. Merge Operation Behavior

* If all revisions are selected in a single merge, the Work Item status updates immediately.

**Limitation:**

* Status may update before actual deployment to the target Org

***

#### 4. Recommendation: Prefer CI Job-Based Updates

**Best Practice:**

* Use CI Job integration for Work Item updates instead of relying only on merge operations

**Reason:**

* Updates occur after execution results (Success/Warning)
* Provides better alignment with actual deployment status

***

#### 5. Field Mapping Accuracy

* Incorrect mappings can cause:
  * Failed updates
  * Incorrect statuses
  * Missing comments

**Recommendation:**

* Validate all field mappings before enabling automation

***

#### 6. Work Item Visibility

* Work Items from inactive sprints are hidden by default

**Recommendation:**

* Use filters and settings to control visibility based on requirements

***

### Best Practices

* Always select all revisions for a Work Item
* Avoid partial revision updates
* Prefer CI Job-based updates over merge-based updates
* Validate field mappings thoroughly
* Use filters to manage large Work Item lists effectively
