# CI Job Results

### Overview <a href="#overview" id="overview"></a>

The **CI Job Results** screen will display the list of builds triggered for your CI Jobs to date. In addition, you can even trigger a new build or find detailed build info for your existing jobs, such as build status, log reports, author details, etc.

### Navigating to CI Job Result Screen <a href="#navigating-to-ci-job-result-screen" id="navigating-to-ci-job-result-screen"></a>

1. Hover your mouse over the **nCino** module and click on [**CI Jobs**](https://knowledgebase.autorabit.com/docs/ci-job-list-screen).&#x20;
2. By default, you will be redirected to the **Job Results** tab; if not, click on the **Job Results** tab. The list of CI job builds will display in reverse chronological order; the newest will display on the top of the list.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618511905044.png" alt=""><figcaption></figcaption></figure>

### Trigger a Build <a href="#trigger-a-build" id="trigger-a-build"></a>

To trigger a new build for your CI Job, follow the below steps:&#x20;

3.  From the **CI Job Results** screen, select your job from the **All Jobs** dropdown field. The dropdown here allows switching between the [CI Jobs](https://knowledgebase.autorabit.com/docs/ci-job-list-screen) created.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618518022364.png" alt=""><figcaption></figcaption></figure>
4.  If no build is created yet,  **'No builds exist'** gets displayed, or if the build is already triggered for the job and you wish to trigger another build, click on **Build Now** besides your selected job.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618517978535.png" alt=""><figcaption></figcaption></figure>
5.  The left side on the next screen will have summary details of your CI job configured, i,e.,  _job label, source/destination org, deployment method chosen,_ etc.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678133503355.png" alt="" width="563"><figcaption></figcaption></figure>
6. Under the **Build inputs** section, enter the **title** of the build and add **comments,** if any.&#x20;
7. Choose the **Deployment Type:**
   1. **Commit and Deploy:** Both commit and deployment will undergo if chosen&#x20;
   2. **Deploy only:** Deployment happens to the selected destination org only.
   3. **Commit only:** Committing the changes to the version control branch only.
8. Add any additional information in the **Notes** section. However, this is optional.
9. Click on **Trigger Build**. It will validate the user credentials, and the build will get triggered upon successful validation.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618518113793.png" alt=""><figcaption></figcaption></figure>

10. You'll be redirected to the **Job Results** main screen, where you can find your recently triggered build status.

### Build Log and Object detail <a href="#build-log-and-object-detail" id="build-log-and-object-detail"></a>

11. From the **CI Job Results** screen, click on the CI Job from the list to view the build details or use the **All Jobs** drop-down to look for your job.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678133898002.png" alt=""><figcaption></figcaption></figure>

or,

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678133954594.png" alt=""><figcaption></figcaption></figure>

12. From the list of build lists triggered, look for the build for which you want to see the log and object details. Click on the build once you found it.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134024870.png" alt=""><figcaption></figcaption></figure>

13. For each template deployed, the **Data** tab will list all the [nCino](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) objects committed or deployed, along with the _success/fail_ count.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134140561.png" alt=""><figcaption></figcaption></figure>

14. Click on the **object** to view its detailed object information displayed on the right side of the screen.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134248933.png" alt=""><figcaption></figcaption></figure>

15. The number of records successfully deployed or failed to deploy can be seen under the **Success/ Failed** tab.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134312754.png" alt=""><figcaption></figcaption></figure>

To view the detailed object records that were successfully deployed or failed to deploy, click on the **number link** (under _Success_ or _Failed_).

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678135889393.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678135689661.png" alt=""><figcaption></figcaption></figure>

16. The **Log** tab contains the detailed report of the commit/deployment performed. Each commit/deployment has several "steps," which contain a subset of logs; such logs can be seen here. You can view complete log information in the user interface or save it to your local machine using![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-59.png) icon. The file usually gets downloaded in ZIP format.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134488158.png" alt=""><figcaption></figcaption></figure>

17. **Post-Deployment Activities:** The post-deployment activities information is displayed on this tab. If you have selected more than one Salesforce org as your destination, select the respective org from the **Salesforce Org** drop-down to view the detailed success/failure objects count.

{% hint style="info" %}
**Point to Note:**

1. A maximum of 5 Salesforce Orgs will be considered for post-deployment activities. For multiple Salesforce Orgs opted, the post-deployment activities will be carried out sequentially, meaning the next post-deployment activities will be carried out only if the current post-deployment activities are done.&#x20;
2. The success or failure detailed object records can be seen only if the post-deployment activities are successfully carried out for all of the Salesforce Orgs.
{% endhint %}

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1678134863022.png" alt=""><figcaption></figcaption></figure>

### Commit and Deployment Workspace <a href="#commit-and-deployment-workspace" id="commit-and-deployment-workspace"></a>

**Commit Workspace:** When various commits are deployed to a branch, the queue commits will be mentioned here. The main concept of introducing the commit workspace is to allow parallel commits to the same version control repository/branch.

**Deployment Workspace:** View the ongoing deployment process by clicking on the **Deployment Workspace** icon on the right side of the page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618513120786.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-102.png" alt="" width="563"><figcaption></figcaption></figure>

### CI Job Results 'Advanced Search' Filter <a href="#ci-job-results-advanced-search-filter" id="ci-job-results-advanced-search-filter"></a>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618513233041.png" alt=""><figcaption></figcaption></figure>

1. **Filter by Job Name/ Build Number:** Filter the builds by CI job label name and the build number.&#x20;
2. **Triggered By**: Filter the builds by the author.
3. **Filter by Created/ Modified Date:** If you want to view job lists that get authored between any two dates, use the **'From Date'** and **'To Date'** to narrow down the list of build lists.
4. **Filter by Build Label Name**: Filter the builds by build label name.
5. **Filter by Build Status**: Filter the list based on build status, i.e., success or failed.
6. **Filter by Deploy Status**: Filter the build via deployment type, i.e., commit and deploy or deploy or commit.
