# Feature Deployment Summary

### Feature Deployment <a href="#feature-deployment" id="feature-deployment"></a>

Feature Deployment is a deployment process that will allow you to easily deploy both metadata and data components using the feature migration template or using the dataset configured either from your Salesforce Org or Version Control.

### Feature Deployment History <a href="#feature-deployment-history" id="feature-deployment-history"></a>

The **Feature Deployment History** lists every deployment you have previously run using [AutoRABIT](https://www.autorabit.com/). It is also where you can view detailed deployment reports or re-deploy the nCino objects to your Salesforce Org/ Version Control.

### Accessing Feature Deployment History Page <a href="#accessing-feature-deployment-history-page" id="accessing-feature-deployment-history-page"></a>

You can visit **ncino > Deployment History** to view the Feature Deployment summary page or you'll be auto-redirected to this page whenever you trigger a deployment (using Feature Deployment).

<figure><img src="../../../../../.gitbook/assets/image (48) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

By default, the jobs are listed in reverse chronological order; that is, the most recent job shows up first. Deployment history is shared amongst team members in AutoRABIT, so you may see deployments performed by other members of your team.&#x20;

**My Deployments** tab lists all of the deployment operations you have performed. The **Others** tab will list all other deployments made in AutoRABIT by your team.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (49) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (50) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Navigating Feature Deployment History <a href="#navigating-feature-deployment-history" id="navigating-feature-deployment-history"></a>

For each deployment, the following information is displayed:

1. **Deployment label**: The deployment label name. You can search for deployments by label name using the search filter in the top right of the page
2. **Feature Name**: Feature name assigned to the deployment
3. **Status**: Successful, Failed, Partially Failed, or In progress
4. **Deployment Version**: Version number for the deployment
5. **Source**: The source Salesforce Org&#x20;
6. **Date**: The date and time of the deployment
7. **Owner**: Which user performed the deployment
8. **Iteration**: The number of revisions for your deployment; for dataset deployments, the iteration number will appear as _"dataset"_
9. **Destination**: Target [salesforce org](https://knowledgebase.autorabit.com/docs/salesforce-org)
10. **Redeploy**: Redeploy will allow you to re-trigger the deployment process again \[Refer to _**"Re-trigger the Deployment"**_ section on this page]

### Filtering Deployment History <a href="#filtering-deployment-history" id="filtering-deployment-history"></a>

You can search for items in your history using the search box in the top right of the page.

<figure><img src="../../../../../.gitbook/assets/image (51) (1) (1) (1) (1).png" alt="" width="476"><figcaption></figcaption></figure>

You can view all deployments (default), or only successful, failed, partially failed, in-progress or timeout deployments, or filter results by deployment label, feature name, the owner who carried out the deployment, or between to/fro dates.

<figure><img src="../../../../../.gitbook/assets/image (52) (1) (1) (1).png" alt="" width="381"><figcaption></figcaption></figure>

To filter the deployment via **Feature Name**, you will have the versions list auto-populated to fetch the exact result.

<figure><img src="../../../../../.gitbook/assets/image (53) (1) (1) (1).png" alt="" width="379"><figcaption></figcaption></figure>

### Data Retrieval Workspace <a href="#data-retrieval-workspace" id="data-retrieval-workspace"></a>

Deployments will be in the queue for dataset refresh jobs and will be displayed under **Data Retrieval Workspace**.

Applicable only if the deployment is carried via:

1. Template using [Version Control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/)
2. Version Control using Salesforce Org

<figure><img src="../../../../../.gitbook/assets/image (54) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (55) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Viewing the Deployment Summary <a href="#viewing-the-deployment-summary" id="viewing-the-deployment-summary"></a>

Click on one of the **Labels** to view the detailed deployment summary info.

<figure><img src="../../../../../.gitbook/assets/image (56) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (57) (1).png" alt=""><figcaption></figcaption></figure>

**Feature Template- Revision Details**

For each template revision, you can find the list of all data nCino objects that were either deployed or failed. View the individual object deployment details by clicking on the object or view the success or failed count directly.

<figure><img src="../../../../../.gitbook/assets/image (58) (1).png" alt=""><figcaption></figcaption></figure>

**Object Information:** Click on the **object** to view their detailed information on the right side of the page.

<figure><img src="../../../../../.gitbook/assets/image (59) (1).png" alt="" width="346"><figcaption></figcaption></figure>

**Retrieved:** This section will tell you the total records that are being retrieved. You can even download the records on your local machine. The file format is downloaded in CSV format.

**Success**: Now, the selected records can be downloaded using the download option. Click on the success record count.

<figure><img src="../../../../../.gitbook/assets/image (1536).png" alt=""><figcaption></figcaption></figure>

Click on “Success Count” for the pop-up to appear. A download option will be available for you to select. Click on the download option for the records to be downloaded. You will see the ‘.csv’ file being downloaded.

<figure><img src="../../../../../.gitbook/assets/image (1537).png" alt=""><figcaption></figcaption></figure>

**Failed**: The failed records can be downloaded using the download option available. Click on the failure count for the pop-up to open. Use the ‘Download’ button on the pop-up to download the failed records.

<figure><img src="../../../../../.gitbook/assets/image (1538).png" alt=""><figcaption></figcaption></figure>

**Deployment Log**

View individual deployment steps that are carried out under the **Deployment Log** section. Each deployment has a number of "steps", which contain a subset of logs, such logs can be seen here. You can either view compete log information in the user interface or save it to your local machine using ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-297.png)icon. The file usually gets downloaded in **ZIP** format.&#x20;

<figure><img src="../../../../../.gitbook/assets/image (62) (1).png" alt=""><figcaption></figcaption></figure>

### Re-triggering the Deployment <a href="#retriggering-the-deployment" id="retriggering-the-deployment"></a>

Once you have fixed the deployment error or you like to re-trigger the deployment once again, you can click on the **Re-Deploy** button to quickly restart your deployment.

<figure><img src="../../../../../.gitbook/assets/image (63) (1).png" alt=""><figcaption></figcaption></figure>

Choose the **'Destination Org'** and the deployment criteria you want to set for the deployment process.

<figure><img src="../../../../../.gitbook/assets/image (64) (1).png" alt="" width="512"><figcaption></figcaption></figure>

Once the deployment is re-triggered, a new iteration gets auto-generated with new deployment log details. If the deployment gets failed due to any metadata or data objects, such a report can be found on this page.&#x20;

{% hint style="info" %}
**Important Note**: AutoRABIT recommends fixing the errors generated and redeploying the process once again until the status changes to **Success**.
{% endhint %}
