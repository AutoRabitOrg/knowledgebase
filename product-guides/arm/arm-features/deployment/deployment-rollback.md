# Deployment Rollback

{% hint style="info" %}
The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### About Deployment Rollback <a href="#about-deployment-rollback" id="about-deployment-rollback"></a>

ARM can take a snapshot of your orgs' metadata and copy or deploy it to another org. This will allow you to deploy/rollback changes in a few clicks. The ability to compare two different snapshots (from other orgs) and see the details of what changed can help you track down the cause of problems when they arise.

### How can I roll back my deployment? <a href="#how-can-i-roll-back-my-deployment" id="how-can-i-roll-back-my-deployment"></a>

Before rolling back your deployment, ensure the rollback feature is turned on for your deployment. This implies that the **`Take Backup`** checkbox is selected on the **`Deployment Settings`** screen when a deployment is run. The deployment will not be able to be rolled back if the checkbox is not enabled.

<figure><img src="../../../../.gitbook/assets/image (1668).png" alt=""><figcaption><p>Deployment Settings</p></figcaption></figure>

Next,

1. Go to the **`Deployment History`** screen and choose the deployment label from the list for which you would like to trigger the rollback.
2.  Click **`Rollback`**.\


    <figure><img src="../../../../.gitbook/assets/image (1669).png" alt=""><figcaption><p>Rollback Screen</p></figcaption></figure>
3. Find the metadata components that will be rolled back (under the **`Constructive Changes`** section).

<figure><img src="../../../../.gitbook/assets/image (60) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** In previous releases, ARM didn't have the option to exclude the members while doing the rollback. However, in the recent release, you will now have the feasibility to exclude/deselect the metadata members from the **`Constructive Changes`** section.
{% endhint %}

4. In the "**`Choose your Pre/ Post Destructive Changes`**" screen, you’ll see the list of metadata components present in your target org but not in your source org. Select the checkbox next to a component you want to delete, which is deleted when you deploy. The excluded components' details are logged and can be found in **Rollback Iteration Log**.
5.  You can choose the destructive changes method to delete your components from your target org to sync up the orgs.

    * **`Post Destructive Changes:`** The post destructive changes feature will delete the unwanted fields or metadata components from your destination Salesforce org when the deployment is successful.
    * **`Pre Destructive Changes:`** Pre-destructive changes will delete unwanted fields or metadata components from your destination Salesforce org before the deployments begin.

    <figure><img src="../../../../.gitbook/assets/image (61) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (62) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Remember:** You must add the version number before continuing with destructive changes for active flow metadata. See the [FlowDefinition guide](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowdefinition.htm) for more detail.
{% endhint %}

6. Select the **`Apex Test level`** to validate your deployment. For detailed information on each test level, refer to the article: [Apex Unit Tests](apex-unit-tests.md)

<figure><img src="../../../../.gitbook/assets/image (63) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Next, you will find two more deployment options to choose from:
   * **Deploy purge on delete**: Salesforce uses a recycle bin metaphor for data that users delete. Instead of removing the data, Salesforce flags it as deleted and makes it visible through the recycle bin. ARM has a provision to identify the components that users want to delete and permanently delete them from their Salesforce environment instead of keeping the deleted components in recycle bin. Once purged, they can not be recovered.
   * **Ignore warnings:** This option will allow the rollback to continue even if warnings can cause the deployment to fail.
8. Add information about the current rollback deployment process in the **`Deployment Notes`** box.
9. Type **`Rollback`** in the field provided and click on **`Yes`**.

<figure><img src="../../../../.gitbook/assets/image (64) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. After successfully rolling back your changes, your deployment will be stored in the [Deployment History](monitor-deployments.md) section, tagged as a rollback. You can view the usual deployment report from here, download the package, and even re-deploy the rollback if you wish!\


### Selective Rollback

Selective rollback allows you to revert only specific components from a deployment instead of rolling back the entire set of changes. This is especially useful when only a few components are causing issues and the rest of the deployment is stable.

In AutoRABIT, selective rollback can be performed using the following steps:

1. Navigate to the deployment history.
2. Choose the specific deployment you want to roll back from. For example, a deployment was made with the following components:

* **Apex Class:** A1V
* **Apex Class:** AccountAnalyzer
*   **Custom Object:** AA\_Parts\_\_c\


    <figure><img src="../../../../.gitbook/assets/image (1670).png" alt=""><figcaption><p>Rollback Selection</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1665).png" alt=""><figcaption><p>Deployment History</p></figcaption></figure>

3. Select only the components you want to revert (instead of choosing the entire deployment). Instead of rolling back all three components, only A1V was selected for rollback.

<figure><img src="../../../../.gitbook/assets/image (1666).png" alt=""><figcaption><p>Selective Rollback Components</p></figcaption></figure>

4. Confirm the rollback to apply changes.
5. The selective rollback was successfully completed.

<figure><img src="../../../../.gitbook/assets/image (1667).png" alt=""><figcaption><p>Successful Selective Rollback</p></figcaption></figure>

