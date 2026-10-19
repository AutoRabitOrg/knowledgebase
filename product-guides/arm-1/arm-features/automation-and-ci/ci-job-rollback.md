# Rolling Back a CI Build

{% hint style="info" %}
For the best experience, set your browser zoom to **80%** in Chrome or Firefox.
{% endhint %}

### Overview

AutoRABIT ARM has enhanced the Rollback functionality in the **New UI** to support multiple rollback operations from the same CI Job execution.

Previously, users could initiate a rollback only once for a CI Job execution. After initiating the rollback, the Rollback option was no longer available, even if additional metadata needed to be rolled back.

With this enhancement, users can perform multiple rollbacks and selectively roll back metadata from the complete deployed package or from specific revisions.

#### Key Enhancements

* **Multiple Rollbacks:** Perform multiple rollback operations from the same CI Job execution.
* **Revision-Based Rollback:** Select metadata associated with individual revisions.
* **Flexible Metadata Selection:** Choose metadata using the All Metadata or Revision Based Changes tabs.
* **Duplicate Selection Prevention:** Prevent the same metadata from being selected multiple times.
* **Rollback Tracking:** Successfully rolled-back metadata is excluded from subsequent rollback selections.
* **Retry Failed Rollbacks:** Metadata that fails during rollback remains available for another attempt.

**Availability:** ARM New UI – CI Jobs.

***

### 1. Accessing Rollback from CI Job History

To initiate a rollback:

1. Log in to AutoRABIT ARM.
2. Navigate to **CI Jobs > CI Job History**.
3. Select the required CI Job.
4. Locate the build for which you want to perform a rollback.
5. Click the **Rollback** option for the corresponding build.
6. The Rollback screen opens, displaying the available metadata selection options.

**Note:** The Rollback option remains available as long as eligible metadata from the original CI Job execution has not been successfully rolled back.

### 2. Selecting Metadata for Rollback

The Rollback screen provides two tabs:

#### All Metadata

The **All Metadata** tab displays the complete metadata available from the prepared rollback package, regardless of the revision that contributed the changes.

This tab retains the existing rollback structure, including:

* API Supported metadata
* Constructive changes
* Destructive changes
* API Unsupported metadata
* Pre/Post destructive changes, where applicable

**Steps:**

1. Open the Rollback screen.
2. Select the **All Metadata** tab.
3. Review the available metadata components.
4. Select the components you want to roll back.
5. Proceed with the rollback operation.

This option is useful when you want to roll back selected metadata from the overall CI Job deployment package without reviewing individual revisions.

#### Revision Based Changes

The **Revision Based Changes** tab allows users to view and select metadata based on the revisions that contributed changes to the deployed package.

Each applicable revision displays information such as:

| Field                | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Revision Number      | Identifies the revision associated with the metadata changes.            |
| Number of Components | Displays the number of metadata components associated with the revision. |
| Metadata Type        | Displays the Salesforce metadata type.                                   |
| Metadata Name        | Displays the metadata component name.                                    |
| Constructive Changes | Identifies added or modified metadata.                                   |
| Destructive Changes  | Identifies deleted metadata.                                             |
| Pre/Post Options     | Displays applicable destructive change options.                          |

**Steps:**

1. Open the Rollback screen from CI Job History.
2. Select **Revision Based Changes**.
3. Review the available revisions.
4. Select the required revision.
5. Review the metadata components associated with that revision.
6. Select the components you want to roll back.
7. If required, select additional components from other revisions.
8. Proceed with the rollback operation.

**Note:** Users can select metadata from one or multiple revisions within the same rollback operation.

***

### 3. Performing Multiple Rollbacks

ARM allows multiple rollback operations against the same original CI Job execution.

After a successful partial rollback, the Rollback option remains available for the remaining eligible metadata.

#### Example

Consider a CI Job deployment containing 10 eligible metadata components.

| Rollback Operation        | Components Rolled Back | Remaining Components |
| ------------------------- | ---------------------- | -------------------- |
| Original CI Job Execution | 0                      | 10                   |
| First Rollback            | 4                      | 6                    |
| Second Rollback           | 3                      | 3                    |
| Third Rollback            | 3                      | 0                    |

After the first rollback, users can return to the same CI Job execution and roll back additional metadata.

Once all eligible metadata components have been successfully rolled back, the Rollback option becomes unavailable.

#### Steps to Perform an Additional Rollback

1. Navigate to **CI Jobs > CI Job History**.
2. Open the original CI Job execution.
3. Click **Rollback**.
4. Select either **All Metadata** or **Revision Based Changes**.
5. Review the remaining eligible metadata.
6. Select the required components.
7. Initiate the rollback.

This process can be repeated until all eligible metadata has been successfully rolled back.

***

### 4. Duplicate Metadata Selection Handling

The same metadata component may appear in multiple revisions or in both rollback selection tabs.

ARM automatically prevents duplicate selection within the same rollback operation.

#### Across Revisions

For example:

* Revision 1 contains `ApexClass: AccountService`.
* Revision 2 also contains `ApexClass: AccountService`.

If you select `AccountService` from Revision 1, the same component under Revision 2 becomes disabled.

If you deselect it from Revision 1, it becomes available again under Revision 2.

#### Between All Metadata and Revision Based Changes

The same behavior applies across both tabs.

* Metadata selected under All Metadata becomes disabled under Revision Based Changes.
* Metadata selected under Revision Based Changes becomes disabled under All Metadata.
* Deselecting a component makes it available again in the other tab, provided it has not already been successfully rolled back.

This ensures that each metadata component is included only once in the rollback request.

***

### 5. Handling Failed Rollbacks

ARM tracks rollback completion at the metadata component level.

If a rollback fails, the affected metadata remains eligible for another rollback attempt.

For example, if five metadata components are selected and only three are successfully rolled back:

* The three successfully rolled-back components are excluded from subsequent rollback selections.
* The two failed components remain eligible for another attempt.
* The Rollback option remains available.

This allows users to retry failed metadata without selecting components that have already been successfully rolled back.

***

### 6. Rollback History

Each rollback operation maintains its own execution details and remains associated with the original CI Job execution.

Rollback information includes:

* Rollback status
* Selected metadata components
* Execution timestamp
* Deployment logs
* Salesforce deployment results

This provides visibility into the rollback operations performed against a particular CI Job execution.
