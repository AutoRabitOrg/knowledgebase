# CI Job History

The **CI Job History** page offers a consolidated overview of all CI jobs executed to date. In addition to listing previously triggered jobs, it provides various job-level actions and insights. Once a build is completed, jobs can be re-triggered directly from this interface. Users can monitor job statuses, review detailed deployment outcomes, and access build logs, all from a single, centralized location.

**Step-By-Step Guide:**

1.  Click on the "CI Job History" option on the left side navigation pane to access the "CI Job History" page

    <figure><img src="../../../../../.gitbook/assets/1 - CI Job History.png" alt=""><figcaption></figcaption></figure>
2. Use the **search fields**—_Job name_, _Build number_, and _Build label_—to quickly locate specific CI Jobs within the CI Job History page.
3.  Use the **Filters** option to narrow down job history results by date, build status, deploy status, commit status, and triggered user.

    <figure><img src="../../../../../.gitbook/assets/2 - CI Job History.png" alt=""><figcaption></figcaption></figure>
4.  The **Columns** option enables customization of the CI Job History table view by selecting or deselecting specific fields for display.

    <figure><img src="../../../../../.gitbook/assets/3 - CI Job History.png" alt=""><figcaption></figcaption></figure>
5.  Clicking the **Deployment Queue** button displays a prioritized list of CI jobs lined up for deployment. Jobs are executed sequentially from top to bottom based on this order.

    <figure><img src="../../../../../.gitbook/assets/4 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/5 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>
6.  **Commit Queue**\
    The **Commit Queue** allows users to view and manage jobs awaiting commit execution. Jobs are processed top to bottom based on their order of priority.

    <figure><img src="../../../../../.gitbook/assets/6 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/7 - CI Job History.png" alt=""><figcaption></figcaption></figure>
7. **The CI Job History table displays key details such as:**
   1. **Job name**: Displays the name assigned to each CI Job for identification.
   2. **Time of build**: Shows the exact date and time when the build was executed.
   3. **Build number**: Indicates the sequential number assigned to each build of a CI Job.
   4. **Build label**: Represents a custom label associated with the build.
   5. **Build status**: Reflects whether the build was successful or failed using visual indicators.
   6. **Deploy status**: Displays the status of the deployment for the job.
   7. **Commit status**: Shows the success or failure of any commit operations tied to the job.
   8. **Post-deploy status**: Indicates the outcome of post-deployment activities, if configured.
   9. **Actions**: Offers options to re-trigger the job or access additional actions via the menu.
8.  **Triggering a CI Job Build from History**

    * **Build Job (Play icon)**: Click the play icon under the **Actions** column to initiate a build for the selected CI job directly from the history list.

    <figure><img src="../../../../../.gitbook/assets/7.2 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    #### **Build Inputs Panel**

    <figure><img src="../../../../../.gitbook/assets/7.3 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    * **Build Label**: Enter a unique identifier to label the new build for tracking purposes.
    * **Build Comment**: Provide optional context or notes describing the intent or changes in this build.
    * **Deployment Type**: Choose from "Commit and deploy", "Deploy only", or "Commit only" based on the action needed.
    * **Enable Rollback for this Build**: If this option is selected during the job creation, the same state will reflect while job gets triggered.
    * **Build Notes**: Add additional information or annotations relevant to the build; this field is optional.
    * **Trigger Build Button**: Click this button to finalize and initiate the CI job build with the provided inputs
9.  **Accessing the Build List from CI Job History**

    In the **CI Job History** interface, each row represents an individual CI Job entry with various associated actions. To access detailed build information for any CI Job:

    1. **Build List Navigation**:\
       Click the **ellipsis icon (⋮)** under the **Actions** column for the desired CI Job. From the context menu that appears, select **Build List**. This action navigates to the CI Job Builds screen specific to that CI Job.

    <figure><img src="../../../../../.gitbook/assets/8 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    1. **CI Job Builds Overview**:\
       The **CI Job Builds** screen presents a tabular list of all builds triggered for the selected job. The following attributes are displayed for each build:
       * **Build Number**: Sequential identifier for each build.
       * **Build Name**: Descriptive label assigned to the build.
       * **Triggered Date** and **Triggered By**: Timestamp and initiator of the build.
       * **Commit ID**: The unique identifier of the commit associated with the build.
       * **Build Status**, **Deploy Status**, **Commit Status**, and **Post Deploy Status**: Visual indicators reflecting the outcome of each stage.

    <figure><img src="../../../../../.gitbook/assets/8.1 - CI Job History 2.png" alt=""><figcaption></figcaption></figure>

    The following explains the options available under the actions of the "CI Job Builds" section:

    *   **Build Results**: Displays the overall outcome and statistics of the build process.

        <figure><img src="../../../../../.gitbook/assets/8.1 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.2 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.2 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.2.1 - CI Job History.png" alt=""><figcaption></figcaption></figure>
    *   **Post Deploy Results**: Shows results of deployment validation post-build.

        <figure><img src="../../../../../.gitbook/assets/8.3 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.4 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.5 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>
    *   **Build Info**: Provides basic metadata and configuration details of the build.

        <figure><img src="../../../../../.gitbook/assets/8.6 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.7 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>
    *   **Build Changes**: Lists all the changes included in the selected build.

        <figure><img src="../../../../../.gitbook/assets/8.7.1 - CI Job History.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.7.2 - CI Job History.png" alt=""><figcaption></figcaption></figure>
    *   **Commit Log**: Displays the sequence of commits associated with the build.

        <figure><img src="../../../../../.gitbook/assets/8.8 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.9 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>
    *   **Commit Revision Log**: Shows a list of modified files and their actions in the commit.

        <figure><img src="../../../../../.gitbook/assets/8.10 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.11 - CI Job History (3).png" alt=""><figcaption></figcaption></figure>
    *   **Commit File Diff**: Presents a visual comparison of changes between file versions.

        <figure><img src="../../../../../.gitbook/assets/8.12 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.13 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.14 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.15 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>
    *   **Rollback**: Initiates a rollback of the build deployment from the target org.

        <figure><img src="../../../../../.gitbook/assets/8.16 - CI Job History (3).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.17 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/8.18 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>
    *   **Download Build Backup Snapshot**: Allows you to download a backup archive of the build snapshot.

        <figure><img src="../../../../../.gitbook/assets/8.19 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>
10. **Viewing Build Results**:\
    Within the **CI Job History** screen, click the ellipsis icon corresponding to a specific job entry. Select **Build Results** from the dropdown to view the execution details of that build, including logs, errors (if any), and success metrics.

    <figure><img src="../../../../../.gitbook/assets/9 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/10 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>

    1. The features that are part of the build can be downloaded using the download option
    2. The "logs" of the feature deployment can be observed by clicking on the "View Logs" option available

    <figure><img src="../../../../../.gitbook/assets/11 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>
11. **Accessing Post-Deployment Details from the CI Job History Page**

    To review the logs of post-deployment activities for completed CI jobs:

    1. Navigate to the **CI Job History** page and locate the job of interest.
    2. Open the **Actions** menu (represented by the vertical ellipsis ⋮) corresponding to the selected build.
    3. Choose the **Post Deploy Results** option from the dropdown.

    <figure><img src="../../../../../.gitbook/assets/8.3 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>

    1.  This action opens the **Feature Details** panel that provides build and deployment status specific to each post-deploy Org configured in the CI Job.

        #### Viewing Deployment Logs of Post-Deploy Orgs Within the **Feature Details** panel:

        * Select the desired **Post Deploy Org** from the dropdown at the top-left to filter logs specific to that target Org.
        * Click the **View Logs** icon adjacent to the desired feature to open detailed deployment logs.

        <figure><img src="../../../../../.gitbook/assets/8.4 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>

        The **Feature Logs** panel then displays the **Deploy Log**, outlining each deployment step executed on the selected post-deploy Org, including:

        <figure><img src="../../../../../.gitbook/assets/8.5 - CI Job History (2).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note:**

1. Post-deployment activities support up to a maximum of **five Salesforce Orgs**. When multiple Orgs are selected, these activities are executed **sequentially**—the process moves to the next Org only after the current one completes.
2. **Detailed success or failure records** for individual objects are available **only if post-deployment activities are completed successfully across all selected Orgs**.
{% endhint %}

12. **Build Info**

    The **Build Info** option from the CI Job History menu opens a panel displaying metadata for the selected build, including job name, build number, status details, deployment target, and initiator. This summary provides a consolidated view of critical build-level attributes.



    <figure><img src="../../../../../.gitbook/assets/15 - CI Job History.png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../../../../../.gitbook/assets/16 - CI Job History.png" alt=""><figcaption></figcaption></figure>
13. #### Build Changes – CI Jobs History

    The **Build Changes** view, accessible from the contextual menu in the **CI Jobs History** screen, provides a breakdown of metadata components included in a specific CI job build.

    <figure><img src="../../../../../.gitbook/assets/17 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    Upon selecting **Build Changes**, a categorized list of changes is displayed, grouped by metadata categories. Within each category, individual metadata components are listed.

    This helps track the exact metadata items that were part of a specific build, aiding in review, troubleshooting, and audit purposes. A download icon is also available to export this information.

    <figure><img src="../../../../../.gitbook/assets/18 - CI Job History.png" alt=""><figcaption></figcaption></figure>
14. #### Commit Log – Step-wise Execution Breakdown

    Accessing the **Commit Log** from the contextual menu on the CI Jobs History screen opens a detailed breakdown of the step-wise execution performed during the commit process. The log provides a vertical list of steps such as _Checkout_, _Sorting Structure_, _Diff_, _Converting Structure_, _Commit_, and _Delta_.

    <figure><img src="../../../../../.gitbook/assets/19 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    Each step is expandable and includes messages logged in real time, offering complete transparency into how the commit execution was handled.

    <figure><img src="../../../../../.gitbook/assets/20 - CI Job History.png" alt=""><figcaption></figcaption></figure>
15. **Commit Revision Log**

    The **Commit Revision Log** from the CI Jobs History contextual menu opens a panel listing all the files included in the commit, along with their actions—Modified (M) or Deleted (D). Each entry in the log provides the full file path, aiding traceability and audit for changes made in the build.

    <figure><img src="../../../../../.gitbook/assets/21 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/22 - CI Job History.png" alt=""><figcaption></figcaption></figure>
16. #### Commit File Diff – CI Job History

    From the **CI Jobs History** page, selecting the **Commit File Diff** option from a job’s action menu displays the detailed file-level changes grouped under categories like Data and Filters.

    <figure><img src="../../../../../.gitbook/assets/23 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    1. In the Data tab, files are listed with summary stats for additions and deletions, and expanding a file reveals a side-by-side JSON diff view with highlighted insertions and removals.

    <figure><img src="../../../../../.gitbook/assets/24 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/25 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    1. The Filters tab shows query-based changes in JSON format, such as added filter logic or metadata.

    <figure><img src="../../../../../.gitbook/assets/26 - CI Job History.png" alt=""><figcaption></figcaption></figure>
17. **Rollback**

    On the CI Jobs History page, the rollback operation is accessed via the contextual menu in the Actions column by selecting the **Rollback** option.&#x20;

    <figure><img src="../../../../../.gitbook/assets/27 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    This opens the Feature Deployment Rollback dialog, where the user first chooses the org(s) to roll back from under the **Rollback From** dropdown.&#x20;

    <figure><img src="../../../../../.gitbook/assets/28 - CI Job History.png" alt=""><figcaption></figcaption></figure>

    Following this, one or more deployed templates can be selected using the **Rollback Deployed Template(s)** dropdown. After the necessary selections are made, the rollback is initiated by clicking the **Rollback** button.

    <figure><img src="../../../../../.gitbook/assets/29 - CI Job History (1).png" alt=""><figcaption></figcaption></figure>
18. **Download Build Backup Snapshot**

    The **Download Build Backup Snapshot** option in the CI Jobs History page allows downloading a backup of the selected build for archival or restoration purposes.

    <figure><img src="../../../../../.gitbook/assets/30 - CI Job History.png" alt=""><figcaption></figcaption></figure>
