# CI Job List

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

The **CI Job List** screen displays the CI jobs you created to date inside ARM. The list is displayed in chronological order, meaning the most recent jobs will be displayed at the top.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675971662181.png" alt=""><figcaption></figcaption></figure>

**The CI jobs deployed will have** ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624787522949.png)**symbols next to them, and the ones with only validated CI Jobs will have** ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624787497205.png)**symbols next to it.**

#### Filtering Options: <a href="#filtering-options" id="filtering-options"></a>

You can use the filtering options on this page to narrow your search for a CI job.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675971898047.png" alt=""><figcaption></figcaption></figure>

1. **Group By:** Limit your search to jobs from a particular group by typing the group name in this field or scrolling down through the dropdown list. To display jobs from all groups, select **All Groups**.
2. **Job Name:** Search for a job by typing the job name in this field or scrolling down through the dropdown list.
3. **Last Modified Date Range:** By using this filter, you may narrow down the jobs based on when they were created or modified. By default, the **last seven days'** jobs are displayed. The jobs created/modified within the previous 14 days, 30 days, or 24 hours can be filtered. Use the **custom range** filter to specify more criteria. Then, choose the date and time range for when you wish to view the jobs.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675973254356.png" alt="" width="563"><figcaption></figcaption></figure>

1. **Filter options (**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1666868865860.png)**):**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675971944798.png" alt="" width="375"><figcaption></figcaption></figure>

1. **Job Source Type:** Choose the source type as **Sandbox** or **Version Control**. To include jobs from both source types, select **All**.
   * **Sandbox:** Select the **Source Org** from the dropdown list for the sandbox as the **source type**. To include jobs from all source orgs, select **All**.
   *   **Version Control:** Select the **Source Repository** from the dropdown list for the version control source type. To include jobs from all repositories, select **All**. Also, select the **Source Branch** from the dropdown list.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1666873520341.png" alt="" width="563"><figcaption></figcaption></figure>
2. **Destination Org:** Select the **Destination Org** from the dropdown list. To include jobs from all destination orgs, select **All**.

**More options on this page:**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1675973438641.png" alt="" width="563"><figcaption></figcaption></figure>

1. **Info:** The info icon gives you detailed information for your CI job, such as source/destination org, version control repo/branch, date and time stamp for the job created, etc.
2. **Clone:** Create a new job using information from the existing job.
3.  **Edit:** Update or modify the details for your CI jobs. If the job is already in progress, a popup screen appears when you click **Save**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1657179593976.png" alt=""><figcaption></figcaption></figure>

    * If you click **YES**, the job in progress will be aborted, the job details will be saved, the screen will be redirected to the **CI jobs Result** page, and queued jobs will start running.&#x20;
    *   If you click **NO**, the job details will not be saved and remain on the same screen.\
        \
        If you want to deploy compiled objects of **FlexCard** and **OmniScript** for Vlocity, you must verify 2 things:\


        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1681473879014.png" alt="" width="375"><figcaption></figcaption></figure>
    * The destination org must be registered with **OAuth**. If it is registered with **Standard**, you must register it with OAuth first and then proceed with the deployment. If the org is registered with Standard, the deployment will fail and the following message will display in the log: **`To deploy compiled versions of OmniScript and FlexCards, Please re-register your destination org with OAuth and update the Local Compilation key in the My Account section`**.
    * You must select the **Local Compilation** checkbox in the **My Account** section and enter the **Access Key**.&#x20;
      * The following message will be displayed in the log if you do not select this option: **`Deployment will be performed without local compilation due to the absence of Access Key of Vlocity's Private NPM Repository`**.&#x20;
      * The following message will be displayed in the log if you select this option but enter the wrong key: **`Deployment is completed without local compilation due to the incorrect Access Key of Vlocity's Private NPM Repository`**.
4. **Activate/De-Activate:** This allows you to deactivate the CI jobs for a brief session. Earlier, this provision was not there, and the users used to delete the CI jobs, which they did not want to trigger a new build. Now, you can deactivate them and re-activate them later whenever you wish to trigger a build.
5. **Delete:** Deletes the job from the list. This cannot be undone.

{% hint style="info" %}
**Important Note about the deactivated CI jobs**:

* No schedules will run post deactivation
* Any hook configured for deactivation of the CI job post will not get processed
* The Builds and Deploys queues will get removed
* CI job won't trigger using the API
* The **Edit** and **Clone** features are inaccessible for deactivated CI jobs
* When selected during the post-deployment sequence, deactivated CI work will affect the configuration of the parent CI job
* Trigger a new build for deactivated CI jobs is not allowed.
{% endhint %}
