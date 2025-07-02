# CI Job Results

### Overview <a href="#overview" id="overview"></a>

The **CI Job Results** screen displays the list of builds triggered for your CI Jobs to date. You can trigger new builds and access detailed build information including status, logs, author, and more.

### Navigating to CI Job Result Screen <a href="#navigating-to-ci-job-result-screen" id="navigating-to-ci-job-result-screen"></a>

1. Hover over the **nCino** module and click [**CI Jobs**](https://knowledgebase.autorabit.com/docs/ci-job-list-screen).
2. By default, you'll be directed to the **Job Results** tab. If not, click on it. Builds are listed in reverse chronological order.

<figure><img src="../../../../../.gitbook/assets/image (1367).png" alt="CI Job Results default view"><figcaption><p>CI Job Results default view</p></figcaption></figure>

### Trigger a Build <a href="#trigger-a-build" id="trigger-a-build"></a>

3. In the **CI Job Results** screen, select your job from the **All Jobs** dropdown.

<figure><img src="../../../../../.gitbook/assets/image (1368).png" alt="All Jobs dropdown menu to select CI jobs"><figcaption><p>All Jobs dropdown menu to select CI jobs</p></figcaption></figure>

4. If no build exists, “No builds exist” will be displayed. To create a new build, click **Build Now**.

<figure><img src="../../../../../.gitbook/assets/image (1369).png" alt="Option to trigger a new build"><figcaption><p>Option to trigger a new build</p></figcaption></figure>

5. On the next screen, the left pane shows job summary details (label, source/destination org, deployment method, etc.).

<figure><img src="../../../../../.gitbook/assets/image (1370).png" alt="CI Job summary before triggering build"><figcaption><p>CI Job summary before triggering build</p></figcaption></figure>

6. Under **Build Inputs**, enter the **title** and any **comments**.
7. Choose a **Deployment Type**:
   * **Commit and Deploy** – Commits and deploys to destination org.
   * **Deploy only** – Deploys only.
   * **Commit only** – Commits only.
8. Optionally, add notes in the **Notes** section.
9. Click **Trigger Build**. If credentials are validated, the build will start.

<figure><img src="../../../../../.gitbook/assets/image (1371).png" alt="Trigger Build interface with inputs"><figcaption><p>Trigger Build interface with inputs</p></figcaption></figure>

10. You’ll return to the **Job Results** screen where build status is displayed.

### Build Log and Object Detail <a href="#build-log-and-object-detail" id="build-log-and-object-detail"></a>

11. Click a job in the list or select via **All Jobs** dropdown.

<figure><img src="../../../../../.gitbook/assets/image (1372).png" alt="Selecting a CI Job to view details"><figcaption><p>Selecting a CI Job to view details</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1373).png" alt="Alternate job selection via dropdown"><figcaption><p>Alternate job selection via dropdown</p></figcaption></figure>

12. From the build list, select a build to view logs and object data.

<figure><img src="../../../../../.gitbook/assets/image (1374).png" alt="CI build list with selectable builds"><figcaption><p>CI build list with selectable builds</p></figcaption></figure>

13. Under the **Data** tab, view [nCino](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) objects with success/fail counts.

<figure><img src="../../../../../.gitbook/assets/image (1375).png" alt="Data tab with deployment success/failure counts"><figcaption><p>Data tab with deployment success/failure counts</p></figcaption></figure>

14. Click an object to view detailed information.

<figure><img src="../../../../../.gitbook/assets/image (1376).png" alt="Object detail panel showing deployment info"><figcaption><p>Object detail panel showing deployment info</p></figcaption></figure>

15. The **Success/Failed** tab shows deployment outcomes by record count.

<figure><img src="../../../../../.gitbook/assets/image (1377).png" alt="Success and Failed tabs with record counts"><figcaption><p>Success and Failed tabs with record counts</p></figcaption></figure>

Click a count link for full details:

<figure><img src="../../../../../.gitbook/assets/image (1378).png" alt="Detailed record results by success/failure"><figcaption><p>Detailed record results by success/failure</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1379).png" alt="Record breakdown per status"><figcaption><p>Record breakdown per status</p></figcaption></figure>

16. The **Log** tab contains commit/deployment logs. Use the download icon (!\[Download log icon]\(../../../../../.gitbook/assets/image (1380).png)) to save the ZIP file.

<figure><img src="../../../../../.gitbook/assets/image (1381).png" alt="Build log tab with export option"><figcaption><p>Build log tab with export option</p></figcaption></figure>

17. **Post-Deployment Activities**: Shows results per Salesforce org. Use the dropdown to toggle between orgs.

<figure><img src="../../../../../.gitbook/assets/image (1382).png" alt="Post-deployment activities with success/failure summary"><figcaption><p>Post-deployment activities with success/failure summary</p></figcaption></figure>

> **Note:**
>
> 1. A maximum of 5 Salesforce Orgs are supported.
> 2. Activities are sequential. Success/failure details are visible only after all post-deployment steps complete.

***

### Download Backup Snapshot

#### Introduction

You can download backup snapshots of CI jobs, either per template or in bulk.

#### Steps

1. Go to any CI Job.
2. Click a template under the build.

<figure><img src="../../../../../.gitbook/assets/image (1486).png" alt="CI job build view with template links"><figcaption><p>CI job build view with template links</p></figcaption></figure>

3. Click the download icon beside each object.

<figure><img src="../../../../../.gitbook/assets/image (1487).png" alt="Download icons for individual objects"><figcaption><p>Download icons for individual objects</p></figcaption></figure>

4. Hover over the three-dot menu in the top banner.

<figure><img src="../../../../../.gitbook/assets/image (1488).png" alt="Three-dot menu to access build changes"><figcaption><p>Three-dot menu to access build changes</p></figcaption></figure>

5. Click **Build Changes** to access the download page.

<figure><img src="../../../../../.gitbook/assets/image (1489).png" alt="Build Changes page with Download button"><figcaption><p>Build Changes page with Download button</p></figcaption></figure>

6. Click **Download** to save all templates in that build.

***

### Commit and Deployment Workspace <a href="#commit-and-deployment-workspace" id="commit-and-deployment-workspace"></a>

* **Commit Workspace** – Displays queued commits for the same repository/branch, enabling parallel commit operations.
* **Deployment Workspace** – Shows ongoing deployment progress. Click the icon at the right side of the page.

<figure><img src="../../../../../.gitbook/assets/image (1383).png" alt="Commit Workspace panel"><figcaption><p>Commit Workspace panel</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (1384).png" alt="Deployment Workspace view"><figcaption><p>Deployment Workspace view</p></figcaption></figure>

***

### CI Job Results 'Advanced Search' Filter <a href="#ci-job-results-advanced-search-filter" id="ci-job-results-advanced-search-filter"></a>

<figure><img src="../../../../../.gitbook/assets/image (1385).png" alt="Advanced Search filter options for CI Job Results"><figcaption><p>Advanced Search filter options for CI Job Results</p></figcaption></figure>

1. **Filter by Job Name/Build Number** – Filter builds by job label or build number.
2. **Triggered By** – Filter by the user who initiated the build.
3. **Filter by Created/Modified Date** – Use **From Date** and **To Date** fields.
4. **Filter by Build Label Name** – Filter by build label.
5. **Filter by Build Status** – Filter by build success/failure.
6. **Filter by Deploy Status** – Filter by deployment type (commit, deploy, or both).
