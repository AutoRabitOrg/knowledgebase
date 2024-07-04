# Pipelines

### Pipeline: Overview <a href="#pipeline-overview" id="pipeline-overview"></a>

A pipeline is a unidirectional flow that defines how changes start from the development orgs and finish in a production org to be migrated.

The pipeline provides insight into:&#x20;

1. Branches spread across different stages of the DevOps Cycle (Development, Integration, QA, UAT, and Production).
2. Sync status (added/ removed components) between a mapped Salesforce Org and a branch.
3. Commits ahead of or behind each stage.

### Navigating to Pipeline Dashboard Page <a href="#navigating-to-pipeline-dashboard-page" id="navigating-to-pipeline-dashboard-page"></a>

The **Pipeline** screen will allow you to view the different environments and the connection in your pipeline. Also, the commits ahead and behind each environment and the deployment status for every environment can be seen here.

1. Hover your mouse over the **DASHBOARD** tile and select the option: **PIPELINE.**
2. Select the **Repository** to visualize your branching landscape across your development team.
3. Click on the![](<../../../../.gitbook/assets/image (936).png>)icon to get the latest data.
4. The message below is shown for a repository whose pipeline has not yet been configured. Steps to set up the repository pipeline can also be seen.

<figure><img src="../../../../.gitbook/assets/image (937).png" alt=""><figcaption></figcaption></figure>

5. The following screen will appear if your repository is configured with the pipeline:

<figure><img src="../../../../.gitbook/assets/image (938).png" alt="" width="563"><figcaption></figcaption></figure>

6. Apart from the **Deployment** status, you can see in each environment the number of commits ahead or behind. The forward arrow indicates the commits an upper branch is ahead by, while the backward arrow indicates the commits by which the lower branches are behind.

<figure><img src="../../../../.gitbook/assets/image (939).png" alt="" width="317"><figcaption></figcaption></figure>

### Known Limitations <a href="#known-limitations" id="known-limitations"></a>

1. The pipeline displays information for the GIT repository only.
2. Development, Integration, QA, UAT, and Production are all supported branch categories. The information will not be fetched on the **Pipeline** screen if branch types other than those mentioned are configured.
