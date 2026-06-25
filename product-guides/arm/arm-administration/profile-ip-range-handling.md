# Profile IP Range Handling

## Profile IP Range Handling – Append and Replace

### Overview

ARM now supports two configurable modes for handling **Profile IP Ranges** during Commit, CI Jobs, and Deployment operations:

* **Append** (Default)
* **Replace**

This enhancement provides greater flexibility for managing Profile IP Ranges while ensuring consistent behavior across all deployment types.

### Configuration

Navigate to:

**ADMIN → Salesforce Settings**

Select one of the following options for **Profile IP Range Handling**:

* **Append** (Default)
* **Replace**

<figure><img src="../../../.gitbook/assets/image (2556).png" alt=""><figcaption></figcaption></figure>

> **Note:** When changing the setting to **Replace**, ARM displays a warning indicating that deployments will synchronize Profile IP Ranges and remove any IP ranges not present in the source or branch metadata.

### Behavior

#### Append (Default)

* Only newly added Profile IP Ranges are committed and deployed.
* Existing IP Ranges in the target organization remain unchanged.
* Deleted IP Ranges are ignored.

#### Replace

* During **Commit**, ARM synchronizes the branch metadata with the complete set of Profile IP Ranges from the source organization.
* During **Deployment**, ARM synchronizes the target organization with the complete set of Profile IP Ranges from the branch metadata.
* IP Ranges that are not present in the source or branch metadata are removed from the target organization.

### Remove IP Ranges

If **Remove IP Ranges** is selected during a deployment or CI Job, ARM removes the entire `loginIpRanges` section from the Profile metadata before deployment.

### Supported Operations

The selected Profile IP Range handling option applies consistently to:

* Commit
* CI Jobs
* Manual Deployments
* Validation Deployments
* Version Control Deployments
* Org-to-Org Deployments

> **Note:** This enhancement applies only to **Profile IP Ranges**. Other Profile metadata continues to follow the existing deployment behavior.
>
> **Note:** This feature is available only when the **`ENABLE_PROFILE_IPRANGES_FEATURE`** feature flag is enabled. To enable this feature for your organization, please contact AutoRABIT Support.
