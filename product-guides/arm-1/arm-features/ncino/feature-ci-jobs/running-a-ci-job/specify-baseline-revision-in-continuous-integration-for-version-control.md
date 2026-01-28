# Set Baseline Revision for Version Control CI

## Introduction

Now users can seamlessly specify the baseline revision from a set of revisions available from the repository.

### Feature Overview

1.  The **Baseline Revision** serves as a reference point in version-controlled deployments. When configuring a CI Job, selecting a baseline revision instructs the system to automatically include all templates committed **after** that specific revision for every subsequent deployment execution.

    Once the baseline revision is set:

    * The system continuously monitors the repository.
    * At runtime, it picks up **all new commits made above the baseline**, ensuring that only incremental changes are deployed.
    * This behavior persists across multiple deployments, allowing the job to stay up to date with the latest committed templates without manual revision selection each time.
2. This mechanism streamlines continuous integration workflows by reducing manual intervention and ensuring deployments always reflect the most recent changes since the defined baseline

#### Step-by-Step Guide



1.  Select the "Deploy From Version Control", option at the "Source Type".



    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/1%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>
2. **On this page, select the following required fields and input the necessary values:**
   1. **Label Name**: Enter the preferred label to identify the CI job.
   2. **Description**: Provide a relevant description outlining the purpose of the deployment.
   3. **Repository**: Select the appropriate repository from the available list.
   4. **Branch**: Choose the required branch associated with the selected repository.
   5. **VC Fetch Type**: Select the required "Fetch Type" from the available list.
   6. **From Revision**: Select the starting revision to define the lower boundary of the revision range.
   7. **To Revision**: Select the ending revision to define the upper boundary of the revision range.
3.  **VC Fetch Type:** Select the "Baseline Revision" from the available list.



    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/2%20-%20Baseline%20Revision%20(1).png" alt=""><figcaption></figcaption></figure>
4.  Select the "Baseline Revision" from the available list of versions.

    &#x20;

    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/3%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/4%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>
5.  **Destination**: Select the target org where the deployment should be executed.



    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/5%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>
6.  **Job Settings**: The "Job Settings" screen allows configuration of deployment behaviors, scheduling options, user notifications, and post-deployment dataset propagation in a CI Job.



    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/6%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>
7.  **Preview**: The final preview screen summarizes source, destination, and job settings, confirming that all commits after the selected baseline revision will be included in the CI job deployment.



    <figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/7%20-%20Baseline%20Revision.png" alt=""><figcaption></figcaption></figure>
