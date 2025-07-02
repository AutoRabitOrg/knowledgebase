# CI Job List screen

The **CI Job List** screen displays all created jobs, sorted by their **most recently created or modified date**.

<figure><img src="../../../../../.gitbook/assets/1 - Feature CI Jobs (4).png" alt=""><figcaption></figcaption></figure>

**Step-By-Step Guide:**

1.  The **CI Jobs List** screen provides filters to narrow down the jobs by **Modified by**, **Created date range**, or **Modified date range**, along with an option to reset or apply the selected criteria.

    <figure><img src="../../../../../.gitbook/assets/2 - Feature CI Jobs (2).png" alt=""><figcaption></figcaption></figure>
2.  The **Columns** dropdown in the CI Jobs List view allows users to selectively display relevant columns such as Job name, Job type, Modified by, Modified on, Source Org, and Source Repo Name, offering a customizable tabular layout for job visibility.

    <figure><img src="../../../../../.gitbook/assets/3 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
3.  The **Deployment Queue** panel, accessible from the CI Jobs List screen, displays a prioritized sequence of CI jobs scheduled for deployment. Jobs are executed sequentially from top to bottom based on the listed priority. This ensures controlled deployment order and allows users to validate or rearrange job sequence before initiating the execution. If no jobs are currently queued, the table remains empty.

    <figure><img src="../../../../../.gitbook/assets/4 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/5 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4.  The **Commit Queue** section provides a dedicated interface for managing commit-triggered CI jobs. Accessed by selecting the **Commit queue** button from the CI Jobs List screen, this panel displays a list of queued commit-based jobs—if available—along with metadata including repository, branch, commit message, author, date, job type, and options to remove entries. Jobs in this queue are arranged in priority order and executed sequentially from top to bottom. If no commit jobs are currently queued, the pane explicitly indicates that no jobs are found.

    <figure><img src="../../../../../.gitbook/assets/6 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/7 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
5.  **Job Info**

    The contextual menu under the “Actions” column of the CI Jobs List screen includes a **Job Info** option, which opens a side panel displaying metadata for the selected CI job. This includes job name, commit repository and branch, created and modified by details, associated destination and post-deploy orgs, and relevant timestamps.

    <figure><img src="../../../../../.gitbook/assets/8 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/9 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
6.  **Edit**

    The **Edit** option available in the contextual menu under the “Actions” column of the CI Jobs List screen enables modification of an existing CI job. Upon selection, it opens the job configuration interface pre-populated with the current settings, allowing updates to any of the defined parameters before saving the changes.

    <figure><img src="../../../../../.gitbook/assets/10 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/11 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
7.  **Clone**

    The CI Jobs List interface includes the option to duplicate an existing CI job by using the **Clone** action from the job’s action menu. Upon selecting **Clone**, a pop-up modal titled _"Clone Job: \[Job Name]"_ appears, prompting for a new job name. A unique name must be entered into the provided field to proceed. Once the name is specified, clicking **Clone** creates a duplicate of the original CI job with the same configurations, which can then be managed independently. This feature simplifies the reuse of similar job setups by eliminating the need to configure each new job from scratch.

    <figure><img src="../../../../../.gitbook/assets/12 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/13 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/14 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
8.  **Delete**

    To remove a CI Job from the CI Jobs List, the user can initiate deletion from the actions menu (represented by the vertical ellipsis) associated with the respective job entry. Upon selecting **Delete**, a confirmation dialog appears prompting the user to confirm the deletion of the specified CI Job. This dialog clearly mentions the job name and provides **Cancel** and **Delete** buttons. Choosing **Delete** finalizes the removal of the job from the queue, while **Cancel** aborts the operation and retains the job in the list.

    <figure><img src="../../../../../.gitbook/assets/15 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/16 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
9.  **Trigger Build**

    Once a job is available in the CI Job List, it can be executed by selecting the **Trigger Build** option available in the Actions menu of the respective job. Upon selecting this option, a _Trigger Build_ panel opens, displaying the job’s configuration details including source and destination specifications such as the change origin, destination org, commit repository, branch, and associated post-deployment orgs.

    <figure><img src="../../../../../.gitbook/assets/17 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

    The panel also includes **Build Inputs** where a label for the build must be specified. Additionally, optional fields are provided to enter build comments and notes. A **Deployment type** must also be chosen, which can be one of the following:

    * Commit and deploy
    * Deploy only
    * Commit only

    <figure><img src="../../../../../.gitbook/assets/18 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

    After providing the necessary inputs, clicking the **Trigger build** button initiates the execution of the job. Once triggered, the page automatically transitions to the **CI Job History** screen. This page lists all historical builds associated with various CI Jobs, including the newly triggered one. For each record, the screen displays the job name, time of build, build number, build label, and respective status indicators for build, deployment, commit, and post-deployment actions. This centralized view allows users to monitor the outcome and status of each build run.

    <figure><img src="../../../../../.gitbook/assets/19 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
