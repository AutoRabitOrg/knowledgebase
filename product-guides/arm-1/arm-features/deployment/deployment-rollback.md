# Rolling Back a Deployment

{% hint style="info" %}
The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### Overview

AutoRABIT ARM has enhanced the Rollback functionality in the **New UI** to support multiple rollback operations from the same Deployment execution.

Previously, users could initiate a rollback only once for a deployment. After the rollback was initiated, the Rollback option was no longer available, even if additional metadata remained in the original deployment package.

With this enhancement, users can selectively roll back metadata from the complete deployment package or from individual revisions and perform additional rollbacks whenever required.

#### Key Enhancements

* **Multiple Rollbacks:** Perform multiple rollback operations against the same deployment execution.
* **Revision-Based Selection:** Identify and select metadata associated with specific revisions.
* **Flexible Rollback Options:** Select metadata using the All Metadata or Revision Based Changes tabs.
* **Duplicate Selection Prevention:** Prevent the same metadata from being selected multiple times.
* **Rollback Tracking:** Exclude successfully rolled-back metadata from subsequent rollback selections.
* **Retry Failed Rollbacks:** Retry metadata components that were not successfully rolled back.

**Availability:** ARM New UI – Deployments.

***

### 1. Accessing Rollback from Deployment History

To initiate a rollback:

1. Log in to AutoRABIT ARM.
2. Navigate to **Deployment > Deployment History**.
3. Locate the deployment execution you want to roll back.
4. Click the **Rollback** option associated with the deployment.
5. The Rollback screen opens, displaying the available metadata selection options.

<figure><img src="../../../../.gitbook/assets/image (3053).png" alt=""><figcaption></figcaption></figure>

**Note:** The Rollback option remains available as long as eligible metadata from the original deployment has not been successfully rolled back.

***

### 2. Selecting Metadata for Rollback

The Rollback screen provides two tabs:

#### All Metadata

The **All Metadata** tab displays the complete metadata available from the prepared rollback package.

It provides a consolidated view of the metadata available for rollback, regardless of the revision that contributed the changes.

<figure><img src="../../../../.gitbook/assets/image (3054).png" alt=""><figcaption></figcaption></figure>

The existing rollback structure is retained, including:

* API Supported metadata
* Constructive changes
* Destructive changes
* API Unsupported metadata
* Pre/Post destructive change options, where applicable

**Steps:**

1. Open the Rollback screen from Deployment History.
2. Select the **All Metadata** tab.
3. Review the available metadata components.
4. Select the components you want to roll back.
5. Proceed with the rollback operation.

This option is useful when you want to roll back selected metadata from the overall deployment package without reviewing individual revisions.

#### Revision Based Changes

<figure><img src="../../../../.gitbook/assets/image (3055).png" alt=""><figcaption></figcaption></figure>

The **Revision Based Changes** tab provides a revision-level view of metadata that contributed to the deployed package.

Users can review individual revisions and select the metadata components associated with them.

Each applicable revision displays information such as:

| Field                | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Revision Number      | Identifies the revision that contributed metadata changes.               |
| Number of Components | Displays the number of metadata components associated with the revision. |
| Metadata Type        | Displays the Salesforce metadata type.                                   |
| Metadata Name        | Displays the metadata component name.                                    |
| Constructive Changes | Identifies added or modified metadata.                                   |
| Destructive Changes  | Identifies deleted metadata.                                             |
| Pre/Post Options     | Displays applicable destructive change options.                          |

**Steps:**

1. Open the Rollback screen.
2. Select **Revision Based Changes**.
3. Review the revisions associated with the deployment.
4. Select the required revision.
5. Review the metadata components associated with that revision.
6. Select the components you want to roll back.
7. If required, select additional metadata from other revisions.
8. Proceed with the rollback operation.

**Note:** Users can select metadata from multiple revisions and include it in a single rollback operation.

***

### 3. Performing Multiple Rollbacks

ARM allows users to perform multiple rollback operations against the same original deployment execution.

After a partial rollback, the Rollback option remains available for metadata that has not yet been successfully rolled back.

#### Example

Consider a deployment containing 10 eligible metadata components.

| Rollback Operation  | Components Rolled Back | Remaining Components |
| ------------------- | ---------------------- | -------------------- |
| Original Deployment | 0                      | 10                   |
| First Rollback      | 4                      | 6                    |
| Second Rollback     | 3                      | 3                    |
| Third Rollback      | 3                      | 0                    |

After the first rollback, the remaining six components continue to be available.

Users can return to the same deployment execution and perform additional rollbacks as required.

Once all eligible metadata has been successfully rolled back, the Rollback option becomes unavailable.

#### Steps to Perform an Additional Rollback

1. Navigate to **Deployment > Deployment History**.
2. Locate the original deployment execution.
3. Click **Rollback**.
4. Select either **All Metadata** or **Revision Based Changes**.
5. Review the remaining eligible metadata.
6. Select the required components.
7. Initiate the rollback.

You can repeat this process until all eligible metadata has been successfully rolled back.

***

### 4. Duplicate Metadata Selection Handling

The same metadata component may be included in multiple revisions or appear in both rollback selection tabs.

ARM prevents duplicate metadata selection within the same rollback operation.

<figure><img src="../../../../.gitbook/assets/image (3056).png" alt=""><figcaption></figcaption></figure>

#### Across Revisions

For example:

* Revision 1 contains `ApexClass: AccountService`.
* Revision 2 also contains `ApexClass: AccountService`.

If you select `AccountService` from Revision 1, the same metadata component under Revision 2 becomes disabled.

If you deselect it from Revision 1, the component becomes available again under Revision 2.

#### Between All Metadata and Revision Based Changes

The same behavior applies across both tabs.

* Metadata selected under All Metadata becomes disabled under Revision Based Changes.
* Metadata selected under Revision Based Changes becomes disabled under All Metadata.
* Deselecting a component makes it available again in the other tab, provided it has not already been successfully rolled back.

This ensures that the same metadata component is not included multiple times in the rollback request.

***

### 5. Handling Failed Rollbacks

ARM tracks rollback completion at the metadata component level.

If a rollback fails, the affected metadata is not considered successfully rolled back and remains available for another attempt.

For example, if five metadata components are selected for rollback and only three are successfully rolled back:

* The three successfully rolled-back components are excluded from subsequent rollback selections.
* The two failed components remain eligible for another attempt.
* The Rollback option remains available.

This allows users to retry failed metadata without affecting components that have already been successfully rolled back.

***

### 6. Rollback History

Each rollback operation maintains its own execution details and remains associated with the original deployment execution.

<figure><img src="../../../../.gitbook/assets/image (3057).png" alt="" width="281"><figcaption></figcaption></figure>

Rollback information includes:

* Rollback status
* Selected metadata components
* Execution timestamp
* Deployment logs
* Salesforce deployment results

This provides traceability for the rollback operations performed against a particular deployment.

***

### Important Considerations

* Multiple rollbacks are supported for the same deployment execution.
* The Rollback option remains available until all eligible metadata has been successfully rolled back.
* Successfully rolled-back metadata cannot be selected again from the same original deployment.
* Failed metadata remains eligible for another attempt.
* Duplicate metadata selection is prevented across revisions and tabs.
* Existing constructive and destructive change handling remains unchanged.
* Existing Salesforce deployment validations and dependency handling continue to apply.
* Revision-based rollback does not automatically resolve Salesforce metadata dependencies.
* Salesforce data rollback is not supported by this enhancement.

