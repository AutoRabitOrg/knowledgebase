# Run a CI Job

Follow the following flow to create a CI Job.

1.  Click on the **"Create"** drop-down to select the "Feature CI Job" option

    <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
2.  Either "Create CI Job", to initiate a CI job.

    <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
3.  Clicking on the "Create --> Feature CI Job" or the "Create Feature CI Job" will land on the following **"CI Jobs"** page

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4. **CI Jobs "Source Type" page will have the following options:**
   1. **Deployment fro, template configuration**: The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control.
   2. **Deploy using salesforce template**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, and based on the configurations, the data is pulled from the source org and later deployed to the destination environment.
   3. **Deploy from version control**: The only difference between this and the Feature Migration template deployment is that here the template is picked up, which is part of version control. Such data is pulled from the version control and deployed to the destination.
   4. **Deploy using Salesforce and version control**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.
5.  **Prerequisites:**

    To be able to access the CI Jobs, the following permissions are required:

    1. Edit, Clone, and Delete permissions are needed to access the nCino CI jobs.
    2. The administrator can provide the required permissions by going to the Users and Roles section of the application.
    3.  The administrator can assign the permissions through this flow Admin > Users > Roles > Feature Migration > Edit, Clone and Delete.

        <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (2).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

**Step-By-Step Guide:**

The following provides a detailed flow on creating the **"Feature CI Jobs"**:

1. The Feature CI Job can be created through the following options:
   1.  Click on the "Feature CI Job" option on the create drop-down

       <figure><img src="../../../../../../.gitbook/assets/3 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
   2.  Click on the "Create feature CI Job" button on the CI Jobs List page to initiate the job creation

       <figure><img src="../../../../../../.gitbook/assets/3.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
   3.  All the CI Jobs history can be accessed through the "CI Jobs History" page. The Feature CI Job creation can be initiated through this screen as well by clicking on the "Create feature CI Job".

       <figure><img src="../../../../../../.gitbook/assets/3.2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

### **Deploy from template configuration**:&#x20;

Clicking the "Feature CI Job"/"Create featue CI Job" will open the following "Source Type" page

<figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (3).png" alt=""><figcaption></figcaption></figure>

1.  Post-DeploymentSource Type: Select the required "Source Type" in the following screen

    <figure><img src="../../../../../../.gitbook/assets/4 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
2.  Fill in all the required details in the "Source" screen.

    <figure><img src="../../../../../../.gitbook/assets/5 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
3.  The following fields are required to be input in the screen:

    1. **Label Name**: Enter a custom name in the field provided. This is a mandatory field, as indicated by the asterisk symbol displayed alongside it..
    2. **Description**: Input the description that fits for the deployment being created. This is an optional field to be input in.
    3. **Feature Type**: The feature type consisits of Standard, Community and All as options to selecte from.
       1. **Standard**: This fetches all the templates that are published by the nCIno
       2. **Community**: These are the templates that are created by the nCino-Users.
       3. **All**: This list of features is a combination of the "Standard & Community" templates.



    <figure><img src="../../../../../../.gitbook/assets/5.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4.  Feature Selection

    In the CI Job creation workflow, the **Feature Type** must be selected first. Once the feature type (e.g., _Community_) is selected, the **Features** section becomes active.
5.  **Search and Select Features**

    1. Use the **Search Features** field to locate the desired features.
    2. Select the checkboxes adjacent to the required features.
    3. The selected features are displayed on the right under **Selected Feature Version(s)**, each accompanied by a delete icon (✖) to remove any selection.
    4. Click on the "=" to pick and move the features across the list and re-arrange them in the desired palce.
    5. The selected list of features will be denoted as (Selected of Total available features).

    <figure><img src="../../../../../../.gitbook/assets/5.1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
6. **Review Selected Features**
   1. Each selected feature is shown with its template name and version at the **"Selected Feature Version(s)"**. The number beside denotes the total number of features selected.
   2. This selection determines the data templates that will be applied in subsequent deployment and commit stages.
7.  **Deployment and Commit Settings**

    1. After selecting features, configure the **Destination Org** and **Version Control Repository** to enable automated deployment and commit actions.
       1. **Deploy To**
          1. Toggle **Deploy To** to enable data deployment to a Salesforce Org.
          2. Select the destination org from the dropdown list .
       2. **Commit To**
          1. Toggle **Commit To** to push changes to a version control system.
          2. Choose the repository and branch to which changes should be committed&#x20;
       3. **Enter Commit Comment**
          * Input a brief description of the commit in the **Commit Comment** field.

    <figure><img src="../../../../../../.gitbook/assets/6 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
8.  **Object Configuration(s)**

    Once features are selected and deployment targets defined, the interface displays configuration parameters for each object in the selected templates.

    1. **Parameters Include:**
       1. **Object Name**\
          Displays the Salesforce object included in the template.
       2. **External ID Mappings**\
          Used to identify matching records between source and destination orgs. Editable by clicking the pencil icon next to the mapping.
       3. **Sorting Criteria**\
          Defines the field used to order records during processing.
       4. **Applied Filters**\
          Displays SOQL queries or filters that limit the data being migrated..&#x20;
9.  **Editing External ID Mappings**

    External ID mappings can be configured for each object to facilitate accurate record matching between the source and destination environments.

    1. Click the **pencil icon** beside the External ID Mapping of the object to edit.
    2. In the **External ID Mappings** modal:
       * Select the **Source External ID** from the dropdown.
       * Select the corresponding **Destination External ID**.

    <figure><img src="../../../../../../.gitbook/assets/6.1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
10. **Accessing Sorting Criteria Settings**

    1. Navigate to the **CI Jobs** module and proceed to the **Destination** step after selecting the appropriate source and target configurations.
    2. Within the data template section (e.g., `sitncino-BrandTemplate1194`), locate the **Sorting Criteria** column corresponding to each object listed.
    3. Click the **pencil icon** adjacent to the sorting field to launch the **Field Sorting** configuration pane.

    <figure><img src="../../../../../../.gitbook/assets/7 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
11. **Selecting a Field for Sorting**

    In the **Field Sorting** dialog:

    * A complete list of fields for the selected object is displayed.
    * Select the desired field to define the sort order. For instance, `LLC_BI__lookupKey__c` may be used to ensure consistent order for `LLC_BI__Branch__c` object records.
    * Only one field can be selected per object for sorting.
    * After selection, click **Save** to confirm the configuration.

    <figure><img src="../../../../../../.gitbook/assets/7.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
12. **Post-Deployment Activities**:&#x20;

    This functionality allows for seamless replication of the deployed dataset across multiple orgs, ensuring data consistency and reducing manual effort.



    <figure><img src="../../../../../../.gitbook/assets/8 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

    **Steps to Configure:**

    1.  **Locate the Section**:\
        Navigate to the **Post Deployment Activities** section at the bottom of the **Job Settings** screen.

        1. **Enable Dataset Propagation**:
           * Check the option labeled **Deploy the same dataset to**.
           * A dropdown field will appear next to the label.
        2. **Choose Target Orgs**:
           * Click on the dropdown to view the list of available organizations.
           * Select one or more target orgs by checking the boxes.
           * The selected orgs will be listed below the dropdown, and the count of selected orgs will be shown.

        <figure><img src="../../../../../../.gitbook/assets/8.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
13. **CI Job Scheduling**

    The scheduling feature within the CI Jobs configuration allows automated execution of data deployment jobs at specified intervals. This configuration ensures consistency and reduces the need for manual intervention.

    1.  **No Schedule (Manual Execution)**

        1. By default, the “No Schedule” option is selected. In this mode, the CI Job is not bound to any automated time-based execution. The job must be manually triggered whenever deployment is required.

        <figure><img src="../../../../../../.gitbook/assets/9 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
    2.  **Daily Schedule Configuration**

        When the “Daily” option is selected, additional configuration fields appear under the **Repeats** section:

        1. **On specific time**: Allows selection of a fixed time at which the job will execute every day (e.g., 00:00).
        2. **At fixed interval**: Enables the job to run repeatedly throughout the day at specified intervals (e.g., every 1 hour starting from 00:00).
        3. This flexibility is ideal for scenarios that require high-frequency updates to the destination environment.

        <figure><img src="../../../../../../.gitbook/assets/9.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
    3.  **Weekly Schedule Configuration**

        1. Selecting the “Weekly” option provides scheduling granularity across specific days of the week:
           1. The preferred day(s) can be selected (e.g., Sunday).
           2. A specific execution time can be set (e.g., 00:00).
           3. This is suitable for environments that require less frequent, periodic data refreshes or updates.

        <figure><img src="../../../../../../.gitbook/assets/9.2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
14. **Preview**: The preview screen provides a holistic view of the configurations selected for the deployment

    <figure><img src="../../../../../../.gitbook/assets/10 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
15. Click **Save** to create a CI Job configuration. Clickin on save will land the user on the "CI Job List" page.





























































ARM facilitates the creation of CI jobs, allowing users to migrate or deploy nCino data and metadata into their destination environments using the following ways:

| Deployment Methods                   | Description                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature Migration Template           | The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control. For more information, refer [Feature Migration template](../../../deployment/destructive-changes.md) section.     |
| Template using Salesforce Org        | The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, and based on the configurations, the data is pulled from the source org and later deployed to the destination environment.                               |
| Version Control                      | The only difference between this and the Feature Migration template deployment is that here the template is picked up, which is part of version control. Such data is pulled from the version control and deployed to the destination.                                                              |
| Version Control using Salesforce Org | The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment. |

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
20. Click **`Save`** to complete the job creation process. You'll be redirected to the [CI Result](../../feature-ci-jobs/ci-job-results.md) screen, where you can trigger a build for your configured job to run the CI operation. Select your CI job from the dropdown on the top right corner of the CI Results screen and click the **`Build Now`** button to trigger a build for your recently created job.
