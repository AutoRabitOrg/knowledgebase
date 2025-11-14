# Running a CI Job

### Overview <a href="#overview" id="overview"></a>

ARM facilitates the creation of CI jobs, allowing users to migrate or deploy nCino data and metadata into their destination environments using the following ways:

| Deployment Methods                   | Description                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature Migration Template           | The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control. For more information, refer [Feature Migration template](../../../../../arm/arm-features/deployment/destructive-changes.md) section. |
| Template using Salesforce Org        | The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, and based on the configurations, the data is pulled from the source org and later deployed to the destination environment.                                                  |
| Version Control                      | The only difference between this and the Feature Migration template deployment is that here the template is picked up, which is part of version control. Such data is pulled from the version control and deployed to the destination.                                                                                 |
| Version Control using Salesforce Org | The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.                    |

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before you proceed with CI job creation, you must have the below permissions:&#x20;

1. You're allowed to access the **CI Jobs** section. The admin can assign the required permission to you by visiting the **`Admin > Roles`** tab and creating a role with the above permission enabled.&#x20;
2. To create a CI job, you must have **Create CI Job** permission. The admin can assign the same by visiting the **`Admin > Roles`** tab and creating a role with the above permission enabled.
3. You should be able to **edit/modify** your existing CI job only if special permission for **CI Job List** is assigned.

_**For example,** you will need **Edit** and **Delete** permissions to edit or delete your existing job_.

<figure><img src="../../../../../../.gitbook/assets/image (1348).png" alt="" width="563"><figcaption></figcaption></figure>

### Creating a CI Job <a href="#creating-a-ci-job" id="creating-a-ci-job"></a>

1. Log in to your AutoRABIT account.&#x20;
2. Hover your mouse over the **`nCino`** module and click on **`CI Jobs`**.
3. Click on **`Create CI Job,`** available on the top corner of the screen.
4. On the next screen, give the job a descriptive name in the **`Job Name`** field and briefly describe it.
5.  Next, you must choose the appropriate **deployment method** for your CI job configuration.

    <figure><img src="../../../../../../.gitbook/assets/image (1349).png" alt=""><figcaption></figcaption></figure>

    * **`Deployment via template:`** You'll be asked to choose the _template type_, i.e., standard or community. The data which is part of the standard or community template chosen will be picked up and deployed to the destination org or selected version control.&#x20;

    <figure><img src="../../../../../../.gitbook/assets/image (1350).png" alt=""><figcaption></figcaption></figure>

    * **`Deployment via template using Salesforce Org:`** The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.

    <figure><img src="../../../../../../.gitbook/assets/image (1351).png" alt=""><figcaption></figcaption></figure>

    * **`Deploment via Version Control:`** Select the template which is part of the version control branch. Such data is pulled from the version control and deployed to the destination.&#x20;

    <figure><img src="../../../../../../.gitbook/assets/image (1352).png" alt=""><figcaption></figcaption></figure>
6.  You can choose from _three additional deployment types_ when you select the **`Deployment From Version Control`**&#x6F;ption.

    *   **`Entire Branch:`** All of the templates from the version control branch will be populated, and you can choose any of them or all.

        <figure><img src="../../../../../../.gitbook/assets/image (1353).png" alt=""><figcaption></figcaption></figure>
    * **`Baseline Revision:`** The nCino revisions are pulled from the version control branch, and you must select one from the list. All the revisions above the set baseline revision will be picked up, which implies the templates committed above the baseline revision will be picked up, and you can deploy those templates to the target org. **For example,** if you want to include templates from the _top three versions_, you must select the _fourth revision_ as the baseline revision.

    <figure><img src="../../../../../../.gitbook/assets/image (1354).png" alt="" width="563"><figcaption></figcaption></figure>

    * **`Revision Range:`** The templates are picked up based on the _from_ and _to revisions_, and you can deploy those templates to the destination org.

    <figure><img src="../../../../../../.gitbook/assets/image (1355).png" alt=""><figcaption></figcaption></figure>

    * **`Deployment via Version Control using Salesforce Org:`**&#x54;he object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.

    <figure><img src="../../../../../../.gitbook/assets/image (1356).png" alt=""><figcaption></figcaption></figure>
7. Select the template(s) from the populated templates list for the CI job process. Click on the **`template`**, select the **`template version`**. Repeat the step for more template selection. Use the **`Select All`** checkbox to select all the templates for deployment to be carried out. The template chosen will get listed under the **`Selected Versions`** tab.

<figure><img src="../../../../../../.gitbook/assets/image (1357).png" alt=""><figcaption></figcaption></figure>

8. Use the **`up/down`** arrow button to move the selected versions up and down or the **`delete`** button to remove a version from the list. Based on the selection, the top version will be deployed initially, and the process continues for the remaining versions.

<figure><img src="../../../../../../.gitbook/assets/image (1358).png" alt="" width="410"><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note:**

1. The most recent version of the template is selected by default
2. The name of the selected version will be in the format **"Template Name- Selected Version."**
{% endhint %}

9. Click **`Next`** to proceed to the next screen.
10. Choose your destination environment.

    * **`Destination Org:`** Select your _target org_ to which the templates will get deployed.
    * **`Version Control:`** Select your _repository_ and _branch_ to commit the templates.

    <figure><img src="../../../../../../.gitbook/assets/image (1359).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Point to Note:** Committing to the version control will not be available for _**Deployment via Version Control**_ and _**Deployment via Version Control using Salesforce Org** feature_.
{% endhint %}

11. Under **`Object Configuration`**, view the objects available for your selected templates. Click on the **+** sign will render the object list and the applied mappings and filters for each template version.

<figure><img src="../../../../../../.gitbook/assets/image (1360).png" alt=""><figcaption></figcaption></figure>

12. **`Applied Mapping:`** The application will default use AutoRABIT external ID for record mapping between source and destination org. Users will have the option to choose their own external ID based on the requirement.\
    **LookupKey\_\_c** is auto-chosen as a default field. If the _lookupKey\_\_c_  field is unavailable, **AutorabitExtId\_\_c**  would be the next choice, and similarly, **Name** will be the third preference if both _lookupKey\_\_c_ and _AutorabitExtId\_\_c_ are unavailable.

    * In the **`'Source'`** field, you must select the source field whose values will be populated in the destination external Id field.
    * &#x20;In the **`'Destination'`** field, you must select the required field from the destination org, whose values will remain unique for all the records.

    <figure><img src="../../../../../../.gitbook/assets/image (1361).png" alt=""><figcaption></figcaption></figure>
13. **`Applied Filters:`** If any filter is applied to the objects, such a filter will be displayed here. You can edit the applied filter (if required) using the **`Edit`** icon. _Editing of the filter is currently not allowed for deployment via the template._

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1677391749901.png" alt=""><figcaption></figcaption></figure>

14. Click **`Next`** to proceed to the next screen.
15. Under the **`Notifications`** section, select the user email id to send email notifications on the success or failure of a build. Use the **`Add User Email (s)`** button to add the custom email address of the users to get notified of the CI job pass or fail. &#x20;

<figure><img src="../../../../../../.gitbook/assets/image (1362).png" alt=""><figcaption></figcaption></figure>

16. Next, under the **`Schedule`** section, you can schedule the process it must run.

    * **`Daily:`** The process will run daily at the scheduled time or interval set.
    * **`Weekly:`** The process will run weekly on the scheduled day and time.
    * **`No schedule:`** The process will only be saved; you can run it when required.

    <figure><img src="../../../../../../.gitbook/assets/image (1363).png" alt=""><figcaption></figcaption></figure>
17. Select other destination orgs under the **`Post Deployment Activities section`**. This will allow the package from the build to be reused to deploy the same data in various Salesforce environments as a post-deployment successful activity.

<figure><img src="../../../../../../.gitbook/assets/image (1364).png" alt=""><figcaption></figcaption></figure>

18. Click **`Next`** to proceed to the final screen. This is the summary page for the CI job that you're about to create. You can view the template details and the mappings/ filters you applied for the last time before the job gets created.

<figure><img src="../../../../../../.gitbook/assets/image (1365).png" alt="" width="563"><figcaption></figcaption></figure>

19. Before you conclude, select the criteria that you can set for the deployment process to continue.

    * **`Disable Workflow Rules:`** This option will deactivate the workflow rules associated with objects in the deployment.
    * **`Disable Validation Rules:`** This option will deactivate the validation rules associated with objects as part of the deployment.
    * **`Use Bulk API (Batch API will be used if the option is not enabled):`** You can transfer bulk records from the source and destination org.
    * **`Insert/update with Null Values:`** This will either insert or update record field values with null (if the value is null in source org) in destination org.
    * **`Use UTF-8 file encoding for file read and write operations:`** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabets. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default as per Salesforce.

    <figure><img src="../../../../../../.gitbook/assets/image (1366).png" alt="" width="462"><figcaption></figcaption></figure>
20. Click **`Save`** to complete the job creation process. You'll be redirected to the [CI Result](broken-reference) screen, where you can trigger a build for your configured job to run the CI operation. Select your CI job from the dropdown on the top right corner of the CI Results screen and click the **`Build Now`** button to trigger a build for your recently created job.
