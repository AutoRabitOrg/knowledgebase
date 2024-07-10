# CI Job Rollback

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

The rollback feature is very useful to roll back a deployment as soon as you realize that something went wrong with the CI job or you accidentally deploy something unwanted.

### How to roll back a deployment <a href="#how-to-roll-back-a-deployment" id="how-to-roll-back-a-deployment"></a>

Here we will learn how to roll back deployment with your CI Jobs. The objective is to roll back to the old release or version of a deployment.

#### **Prerequisites:**  <a href="#prerequisites" id="prerequisites"></a>

The **Rollback** checkbox is selected while creating a new CI job

#### Steps: <a href="#steps" id="steps"></a>

1. Go to the **CI JOB RESULTS** screen and choose the deployment label from the list for which you would like to trigger the rollback.
2. &#x20;Click on the **Rollback** (![](<../../../../.gitbook/assets/image (1200).png>)) icon.

<figure><img src="../../../../.gitbook/assets/image (1201).png" alt=""><figcaption></figcaption></figure>

3. Find the list of metadata components that will be rollbacked (under the **API Supported >** **Constructive changes** section). By default, all the components that were part of the deployment are selected.

<figure><img src="../../../../.gitbook/assets/image (1202).png" alt="" width="526"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1203).png" alt=""><figcaption></figcaption></figure>

4. In the **"Choose your Pre/ Post Destructive Changes,"** you’ll see the list of metadata components that are present in your target environment but not in your source environment. Simply tick the box next to a component you want to delete, and that component will be deleted when you deploy. The excluded component's details are logged and can be found in **Rollback Iteration Log**.

<figure><img src="../../../../.gitbook/assets/image (1204).png" alt=""><figcaption></figcaption></figure>

5. You can choose the destructive changes method to delete your components from your target environment to sync up the changes.
   * **Post Destructive Changes:** The post destructive changes feature will delete the unwanted fields or metadata components from your destination environment when the deployment is successful.
   * **Pre-Destructive Changes:** Pre-destructive changes will delete unwanted fields or metadata components from your destination environment before the deployments begin.

{% hint style="info" %}
**Point to Remember:** For active flow metadata, you must add the version number before continuing with destructive changes. See the [FlowDefinition guide](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_flowdefinition.htm) for more detail.
{% endhint %}

6. The **API Un-Supported** section will list down all the unsupported API metadata types. You can include these components as a part of pre or post-destructive changes as well.

<figure><img src="../../../../.gitbook/assets/image (1205).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note**: We advise against using the unsupported APIs components during the rollback process, as this might result in deployment rollback failure.
{% endhint %}

7.  Under **Additional Deployment Options**, you have below options to choose from:

    * **Validate Only:** This allows you to prevalidate the deployment so you can catch any problematic changes early and make sure that when the time comes to deploy, you’ll be able to release successfully. Actual deployment doesn't happen when this feature has been opted.
    * **Deploy purge on delete**: Salesforce uses a Recycle Bin metaphor for data that users delete. Instead of removing the data, Salesforce flags the data as deleted and makes it visible through the Recycle Bin. AutoRABIT has a provision to identify the components that users want to delete and permanently delete them from their Salesforce environment instead of keeping the deleted components in recycle bin. Once purged, they can not be recovered.
    * **Ignore warnings:** This option will allow the rollback to continue even if there are warnings that can cause the deployment to fail.

    <figure><img src="../../../../.gitbook/assets/image (1206).png" alt=""><figcaption></figcaption></figure>
8. Select the **Apex Test level** to validate your deployment. For detailed information on each test level, refer to the article: [Apex Unit Tests](https://knowledgebase.autorabit.com/arm/docs/apex-unit-tests)

<figure><img src="../../../../.gitbook/assets/image (1207).png" alt=""><figcaption></figcaption></figure>

9. Click **Rollback**.
10. After successfully rolling back your changes, your deployment will be stored in the **CI Job Results** screen, tagged as a rollback. From here, you can view the usual deployment report, download the package, and even re-deploy the rollback if you wish!
