# Version Control Best Practices

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
   * Only deploys delta changes (avoids redundant deployments)
   * Prevents governor limits from being exceeded
   * Skips execution if no changes are detected
5. **Manage Destructive Changes:**
   * Select **Prepare Destructive Changes** in the _Build_ section
   * Select **Run Destructive Changes** in the _Deploy_ section
   * Ensures deleted metadata components in the branch are also removed from the destination
6. **Set Baseline Revision:** To fetch changes from a specific revision onward, configure the **Baseline Revision** during CI job setup.\
   **Example:** If the baseline is set to 9, changes from revisions 10 onward will be fetched.

## Merge Functionality Related

1. **Resolve Merge Conflicts Immediately:** Do this before any other commits are pushed on the same files to avoid cascading conflicts. If resolution is delayed, create a new merge request first to retrieve the latest conflict set.
2. **Prefer Entire Branch Merge:** This avoids missing revisions during merge and maintains a full trace/log of merge actions compared to Single Revision, Release Labels, or Commit Labels.

## External Commit Related

* Adopt a **standard commit message format** for easier tracking and traceability.\
  **Recommended Format:** `<ProjectName#SPRINT#UserStory#Module#DevName#>`
