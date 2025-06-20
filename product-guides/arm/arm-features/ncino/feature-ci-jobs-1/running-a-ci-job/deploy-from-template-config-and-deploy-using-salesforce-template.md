# Deploy From Template Config & Deploy Using Salesforce Template

Follow the following flow to create a CI Job.

1.  Click on the **"Create"** drop-down to select the "Feature CI Job" option

    <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
2.  Either select the **"Create feature CI job"**, to initiate a CI job from the **"CI Job List"**.

    <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
3.  Initiating the  "Feature CI Job" creation will land on the following **"CI Jobs - Source Type"** page.

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4. **CI Jobs "Source Type" page will have the following options:**
   1. **Deployment from, template configuration**: The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control.
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
   3.  Access to the complete history of CI Jobs is available through the **CI Jobs History** page. New Feature CI Jobs can also be configured from this screen using the **Create Feature CI Job** button..

       <figure><img src="../../../../../../.gitbook/assets/3.2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

### **Deploy from template configuration**:&#x20;

1. Initiating the **"Feature CI Job"** creation will open the following **"Source Type"** page.
2. **Source Type:** Select the required **"Source Type"** in the following screen.

<figure><img src="../../../../../../.gitbook/assets/4 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

3. Fill in all the required details in the "Source" screen.

<figure><img src="../../../../../../.gitbook/assets/5 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

4. The following fields must be completed as part of the initial CI Job setup:
   * **Label Name**\
     A custom name must be provided in this field. It is mandatory and is indicated by the asterisk symbol next to the input box.
   * **Description**\
     An optional field where a relevant description can be entered to identify the purpose or scope of the deployment.
   * **Feature Type**\
     This dropdown includes three options for selecting the type of template to be used:
     * **Standard**: Displays templates officially published by nCino.
     * **Community**: Displays templates created and shared by nCino users.
     * **All**: Combines both Standard and Community templates in a single list for broader selection.

<figure><img src="../../../../../../.gitbook/assets/5.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

5. Feature Selection

In the CI Job creation workflow, the **Feature Type** must be selected first. Once the feature type (e.g., _Community_) is selected, the **Features** section becomes active.

1.  **Search and Select Features**

    1. Use the **Search Features** field to locate the desired features.
    2. Select the checkboxes adjacent to the required features.
    3. The selected features are displayed on the right under **Selected Feature Version(s)**, each accompanied by a delete icon (✖) to remove any selection.
    4. The selected list of features will be denoted as (Selected of Total available features).

    <figure><img src="../../../../../../.gitbook/assets/5.1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
2. **Review Selected Features**
   1. Each selected feature is shown with its template name and version at the **"Selected Feature Version(s)"**. The number beside denotes the total number of features selected.
   2. This selection determines the data templates that will be applied in subsequent deployment and commit stages.
   3. Click and hold the "=" icon to pick and move the features across the list and re-arrange them in the desired order.

### Deploy Using Salesforce Template

1.  Initiating the **"Feature CI Job"** will navigate the interface will navigate to the **"Source Type"** page where an appropriate option can be selected.

    <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (3).png" alt=""><figcaption></figcaption></figure>
2.  Select the option "Deploy using salesforce template".

    <figure><img src="../../../../../../.gitbook/assets/1 - Deploy Using Salesforce Template.png" alt=""><figcaption></figcaption></figure>
3.  The interface will navigate to the "Source" page where the required selections can be made.

    <figure><img src="../../../../../../.gitbook/assets/2 - Deploy Using Salesforce Template.png" alt=""><figcaption></figcaption></figure>
4.  **The following fields are required to be input in the screen:**

    1. **Label Name**: Enter a custom name in the field provided. This is a mandatory field, as indicated by the asterisk symbol displayed alongside it..
    2. **Description**: Input the description that fits for the deployment being created. This is an optional field to be input in.
    3. **Feature Type**: The feature type consisits of Standard, Community and All as options to select from.
       1. **Standard**: This fetches all the templates that are published by the nCIno
       2. **Community**: These are the templates that are created by the nCino-Users.
       3. **All**: This list of features is a combination of the "Standard & Community" templates.

    <figure><img src="../../../../../../.gitbook/assets/3 - Deploy Using Salesforce Template.png" alt=""><figcaption></figcaption></figure>
5.  **Feature Selection**

    In the CI Job creation workflow, the **Feature Type** must be selected first. Once the feature type (e.g., _Community_) is selected, the **Features** section becomes active.

    <figure><img src="../../../../../../.gitbook/assets/2 - Deploy Using Salesforce Template (1).png" alt=""><figcaption></figcaption></figure>
6. **Search and Select Features**
   1. Use the **Search Features** field to locate the desired features.
   2. Select the checkboxes adjacent to the required features.
   3. The selected features are displayed on the right under **Selected Feature Version(s)**, each accompanied by a delete icon (✖) to remove any selection.
   4. Click on the "=" to pick and move the features across the list and re-arrange them in the desired palce.
   5. The selected list of features will be denoted as (Selected/Total available features).
7. **Review Selected Features**
   1. Each selected feature is shown with its template name and version at the **"Selected Feature Version(s)"**. The number beside denotes the total number of features selected.
   2. This selection determines the data templates that will be applied in subsequent deployment and commit stages.
   3. Click and hold the "=" icon to pick and move the features across the list and re-arrange them in the desired order.

{% hint style="info" %}
The deployment settings for both **"Deploy From Template"** and **"Deploy Using Salesforce Template"** share a common configuration structure.
{% endhint %}

### **Deployment Settings**

1. Select the features, configure the **Destination Org** and **Version Control Repository** to enable automated deployment and commit actions.
   1. **Deploy To**
      1. Toggle **Deploy To** to enable data deployment to a Salesforce Org.
      2. Select the destination org from the dropdown list .
   2. **Commit To**
      1. Toggle **Commit To** to push changes to a version control system.
      2. Choose the repository and branch to which changes should be committed&#x20;
   3. **Enter Commit Comment**
      * Input a brief description of the commit in the **Commit Comment** field.

<figure><img src="../../../../../../.gitbook/assets/6 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>

1.  **Object Configuration(s)**

    Once the deployment targets defined, the interface displays configuration parameters for each object in the selected templates.

    1. **Parameters Include:**
       1. **Object Name**\
          Displays the Salesforce object included in the template.
       2. **External ID Mappings**\
          Used to identify matching records between source and destination orgs. Editable by clicking the pencil icon next to the mapping.
       3. **Sorting Criteria**\
          Defines the field used to order records during processing.
       4. **Applied Filters**\
          Displays SOQL queries or filters that limit the data being migrated..&#x20;
2.  **Editing External ID Mappings**

    External ID mappings can be configured for each object to facilitate accurate record matching between the source and destination environments.

    1. Click the **pencil icon** beside the External ID Mapping of the object to edit.
    2. In the **External ID Mappings** window:
       * Select the **Source External ID** from the dropdown.
       * Select the corresponding **Destination External ID**.

    <figure><img src="../../../../../../.gitbook/assets/6.1 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>
3.  **Accessing Sorting Criteria Settings**

    1. Within the **'Destination'** section, locate the **Sorting Criteria** column corresponding to each object listed.
    2. Click the **pencil icon** adjacent to the sorting field to launch the **Field Sorting** configuration pane.

    <figure><img src="../../../../../../.gitbook/assets/7 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4.  **Selecting a Field for Sorting:** In the **Field Sorting** window

    * A complete list of fields for the selected object is displayed.
    * Select the desired field to define the sort order.
    * Only one field can be selected per object for sorting.
    * After selection, click **Save** to confirm the configuration.

    <figure><img src="../../../../../../.gitbook/assets/7.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
5.  **Post-Deployment Activities**:&#x20;

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
6.  **CI Job Scheduling**

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
7.  **Preview**: The preview screen provides a holistic view of the configurations selected for the deployment

    <figure><img src="../../../../../../.gitbook/assets/10 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
8.  Click **Save** to create a CI Job configuration. Clickin on save will land the user on the "CI Job List" page.















