# Version Control

## Registering a Version Control Repository

1. Ensure user credentials are stored in the **Credential Manager** section of AutoRABIT with the Credential Scope set to **Private**. This enables the identification of individual users during code check-in.
2. When registering a **Bitbucket** repository, do **not** include the username in the repository URL.\
   **Incorrect Example:** `https://John@bitbucket.org/Repos/bitbucket-testcases-repo.git`
3. Verify that all users have mapped their credentials for the target branch via the **My Profile** section before using it.
4. Create Branch Types (e.g., Dev, QA, Pre-Prod, Production) during branch creation. This helps to clearly identify **From** and **To** branches for Merge and EZ-Commit processes.

## CI Jobs Related

1. **Distribute CI Jobs Evenly:** Schedule jobs across different times to avoid delays and reduce load, especially in SaaS environments.
2. **Exclude Unnecessary Metadata Types:**
   * **Globally:** Navigate to _My Salesforce Settings_ in the _My Account_ page under _Admin_ and select metadata types to exclude. This applies to all future CI jobs.
   * **Job-specific:** In the _BUILD_ section of the CI job, use **Exclude Metadata Types** to define exclusions for that job only.
3. **Remove Login IP Ranges:** Enable this in the _Additional Profile Packaging Options_ under the _Build_ section to avoid overriding whitelisted IP ranges in Salesforce.
4. **Use Incremental Builds** instead of Full Builds:
   * Only deploys delta changes (avoids redundant deployments).
   * Prevents governor limits from being exceeded.
   * Skips execution if no changes are detected.
5. **Manage Destructive Changes:**
   * Select **Prepare Destructive Changes** in the _Build_ section.
   * Select **Run Destructive Changes** in the _Deploy_ section.
   * Ensures deleted metadata components in the branch are also removed from the destination.
6. **Set Baseline Revision:** To fetch changes from a specific revision onward, configure the **Baseline Revision** during CI job setup.\
   **Example:** If the baseline is set to 9, changes from revisions 10 onward will be fetched.

## Merge Functionality Related

1. **Resolve Merge Conflicts Immediately:** Do this before any other commits are pushed on the same files to avoid cascading conflicts. If resolution is delayed, create a new merge request first to retrieve the latest conflict set.
2. **Prefer Entire Branch Merge:** This avoids missing revisions during merge and maintains a full trace/log of merge actions compared to Single Revision, Release Labels, or Commit Labels.

## External Commit Related

* Adopt a **standard commit message format** for easier tracking and traceability.\
  **Recommended Format:** `<ProjectName#SPRINT#UserStory#Module#DevName#>`

## Why EZ-Commit Displays Components Only for the Selected Salesforce Author

**Overview**

In **AutoRABIT ARM – EZ-Commit**, users may notice that when initiating a commit, the component list—particularly under **Select Manually** mode—only displays metadata items modified by the **Salesforce Org Author** chosen on the initial screen.

This behavior is **intentional** and aligns with ARM’s **metadata filtering best practices** to ensure precise commit operations and traceability.

**Background**

Prior to version **25.4.4**, the EZ-Commit author filter did not consistently apply, leading to a broader list of components that included changes from multiple users.

This was corrected in **v25.4.4**, aligning the functionality with the intended design—retrieving only metadata changes associated with the **selected author** (or all authors, if explicitly chosen).

This change promotes **commit accuracy**, **audit compliance**, and **developer accountability**—key elements in mature **Salesforce DevOps pipelines**.

**Expected Behavior Scenarios**

| **Mode**        | **Author Selected** | **Expected Result**                           |
| --------------- | ------------------- | --------------------------------------------- |
| AutoDraft       | All                 | Retrieves changes made by all users.          |
| AutoDraft       | Specific User       | Retrieves changes made by that specific user. |
| Select Manually | All                 | Retrieves changes made by all users.          |
| Select Manually | Specific User       | Retrieves changes made by that specific user. |

**Note for Sub Users**

If **Skip Mappings** is disabled in **PROFILE → My Role**, the sub-user must be mapped to the correct Salesforce user to view their changes. This ensures accurate retrieval of metadata associated with that user’s commits.

**Summary**

This enhancement reinforces ARM’s **DevOps best practices** by ensuring:

* Precise author-based metadata tracking
* Reduced risk of unintended component commits
* Better visibility into code ownership and change management

The current behavior is **by design** and supports a **more consistent and traceable deployment workflow** in Salesforce DevOps environments.
