# Version Control Best Practices

### Registering a Version Control Repository <a href="#registering-a-version-control-repository" id="registering-a-version-control-repository"></a>

1. Before getting a repository registered in AutoRABIT, make sure the user’s credentials are saved in the **Credential Manager** section in AutoRABIT and set the Credential Scope as private. This will help identify the individual users for code check-in.
2. While registering the **Bitbucket** repository, ensure the username is not part of the URL. **For example:** _https://John@bitbucket.org/Repos/bitbucket-testcases-repo.git_
3. Ensure users of the branch have their user credential mapping for a branch done in the **My Profile** section prior to using that branch.
4. Creation of Branch Types (e.g., Dev, QA, Pre-Prod, Production) helps you to attach a branch type at the time of branch creation. This helps in easily identifying **From** and **To** branches during Merge, EZ-commit process.

### CI Jobs related <a href="#ci-jobs-related" id="ci-jobs-related"></a>

1. Ensure that your scheduled CI jobs are evenly spread in a day to avoid delays. This helps in reducing the time to run a CI job and it is also especially useful in a SAAS environment as it reduces the load on the application as well.
2. To avoid unnecessary fetching of metadata types while executing a CI job, ensure that you have excluded them.
   1. To set this option at a global level, go to the My Salesforce Settings section in the My Account page under the Admin module and select the metadata types to exclude. This reflects in all CI jobs that are created henceforth and globally across other modules as well.
   2. To restrict this to a specific CI job select the Exclude Metadata Types under the BUILD section and choose the metadata types exclusively.
3. Ensure that **Remove Login IP Ranges** under the **Additional Profile Packaging Options** are selected in the **Build** section while creating new CI Jobs. This will help to avoid overriding whitelisted IP ranges to access Salesforce orgs.
4. Incremental Build is always recommended over Full Build
   1. As it deploys only delta changes (avoids redundant deployments on unchanged metadata components)
   2. The chance of reaching governor limits with the full build is avoided
   3. Skips the build initiation process if there are no metadata changes.
5. Always select the **Prepare Destructive changes** in the **Build** section and **Run Destructive Changes** in the **Deploy** section to automatically delete metadata members from the destination based on the latest changes (to reflect deletion of metadata components) in a specific branch commit history.
6. If you need to fetch only changes from a specific revision, then it is recommended to set the **Baseline revision** while creating a CI job or else all changes are fetched from base revision till head revision. **For ex-**If you set the **Baseline revision** to 9, then all changes from revision 10 till the head revision are fetched.

### Merge Functionality related <a href="#merge-functionality-related" id="merge-functionality-related"></a>

1. Resolve conflicts immediately before any other commits are performed (on the same set of files) on the same branch by other users to avoid fresh conflicts. In case you would like to resolve the conflicts later, please ensure that you submit a new merge request before resolving the conflicts to get the latest conflict list.
2. We strongly recommend **Entire Branch Merge** over Single Revision, Release Labels, and Commit Labels to avoid manual mistakes of missing revisions during the merge. This will also help us to have a trace and log of merges performed.

### External Commit related <a href="#external-commit-related" id="external-commit-related"></a>

Following a standard pattern for commit messages will aid in the easy identification of commits performed, e.g., \<ProjectName#SPRINT#Userstory#Module#Devname#>.
