# Deploy from version control & Deploy using salesforce and version control

**Prerequisites:** Access to CI Jobs requires specific user permissions. The following conditions must be met:

* **Required Permissions**: _Edit_, _Clone_, and _Delete_ permissions are mandatory to interact with nCino CI Jobs.
* **Permission Assignment**: These permissions must be granted by an administrator.
*   **Assignment Path**:\
    The administrator can assign the necessary permissions by navigating through the following path:\
    **Admin > Users > Roles > Feature Migration > Edit, Clone, and Delete**



    <figure><img src="../../../../../../.gitbook/assets/1 - Feature CI Jobs (2).png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../../../../../../.gitbook/assets/2 - Feature CI Jobs (1).png" alt=""><figcaption></figcaption></figure>

## **Step-By-Step Guide:** <a href="#overview" id="overview"></a>

The Feature CI Job can be created through the following options:

1.  Click on the "Feature CI Job" option on the create drop-down

    <figure><img src="../../../../../../.gitbook/assets/3 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
2.  Click on the "Create feature CI Job" button on the CI Jobs List page to initiate the job creation

    <figure><img src="../../../../../../.gitbook/assets/3.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
3.  Access to the complete history of CI Jobs is available through the **CI Jobs History** page. New Feature CI Jobs can also be configured from this screen using the **Create Feature CI Job** button..

    <figure><img src="../../../../../../.gitbook/assets/3.2 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
4.  Initiating the creation of a Feature CI Job navigates to the **"CI Jobs – Source Type"** page.

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Feature CI Jobs.png" alt=""><figcaption></figcaption></figure>
5. **CI Jobs "Source Type" page will have the following options:**
   1. **Deployment from, template configuration**: The data which is part of a feature migration template (either standard or community template) will be picked up and deployed to the destination org or selected version control.
   2. **Deploy using salesforce template**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, and based on the configurations, the data is pulled from the source org and later deployed to the destination environment.
   3. **Deploy from version control**: The only difference between this and the Feature Migration template deployment is that here the template is picked up, which is part of version control. Such data is pulled from the version control and deployed to the destination.
   4. **Deploy using Salesforce and version control**: The object configuration, such as _filters_, _applied mappings,_ and so on, will be picked up from the standard/community template chosen, which is part of version control. Based on the configurations, the data is pulled from the source org and later deployed to the destination environment.

### Deploy From Version Control

1.  Initiating the "Feature CI Job" creation will navigate to the "Source Type" page

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Deploy From Version Control (2).png" alt=""><figcaption></figcaption></figure>
2. Select **"Deploy from version control"** to initiate the deployment
3.  The screen will navigate to the **"Source"** step of the deployment flow

    <figure><img src="../../../../../../.gitbook/assets/1.2 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>
4. Observe the following fields on the layout and provide the required inputs:
   * **Label Name**: Enter a name for the deployment.
   * **Description**: Add a relevant description (optional).
   * **Repository**: Select the repository from the available list.
   * **Branch**: Choose the desired branch.
   * **VC Fetch Type**: Select from three available options under Version Control Fetch Type.
     *   **Entire Branch**: Displays all templates available within the selected version control branch, allowing selection of one or multiple templates as needed.

         <figure><img src="../../../../../../.gitbook/assets/2 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>
     *   **Baseline Revision**: This field pulls a list of available nCino revisions from the selected version control branch. One revision must be selected as the baseline. All templates committed **after** the chosen baseline revision will be included for deployment to the target org.

         <figure><img src="../../../../../../.gitbook/assets/3 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>

         <figure><img src="../../../../../../.gitbook/assets/4 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>

         <figure><img src="../../../../../../.gitbook/assets/4.1 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>
     *   **Revision Range**: Templates are selected based on the specified start and end revisions. All templates committed within this range will be included for deployment to the destination org.

         <figure><img src="../../../../../../.gitbook/assets/5 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>

         <figure><img src="../../../../../../.gitbook/assets/6 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>

         <figure><img src="../../../../../../.gitbook/assets/7 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>

         <figure><img src="../../../../../../.gitbook/assets/8 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>

### Deploy Using Salesforce and Version Control

1.  Initiating the **"Feature CI Job"** creation will navigate to the **"Source Type"** section of the deployment

    <figure><img src="../../../../../../.gitbook/assets/1 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>
2.  Select the **"Deploy using SAlesforce and version control"** option.

    <figure><img src="../../../../../../.gitbook/assets/1 - Deploy using SF and VC (1).png" alt=""><figcaption></figcaption></figure>
3.  Selecting this option will land on the "Source" section of the flow.

    <figure><img src="../../../../../../.gitbook/assets/1.1 - Deploy using SF and VC (1).png" alt=""><figcaption></figcaption></figure>
4. Observe the following fields on the layout and provide the required inputs:
   * **Label Name**: Enter a name for the deployment.
   * **Description**: Add a relevant description (optional).
   * **Repository**: Select the repository from the available list.
   * **Branch**: Choose the desired branch.
   * **VC Fetch Type**: Select from three available options under Version Control Fetch Type.
     *   **Entire Branch**: Displays all templates available within the selected version control branch, allowing selection of one or multiple templates as needed.



         <figure><img src="../../../../../../.gitbook/assets/1.1 - Deploy using SF and VC.png" alt=""><figcaption></figcaption></figure>
5. Based on the  "VC FEtch Type" selected, the "Features", "Versions" and "Selected Feature Version(s) will be populated as shown above

{% hint style="info" %}
The deployment settings for both **"Deploy From Version Control"** and **"Deploy Using Salesforce and Version Control"** share a common configuration structure.
{% endhint %}

### **Deployment Settings**

1.  Select the features, configure the **Destination Org** and **Version Control Repository** to enable automated deployment and commit actions.

    1. **Deploy To**
       1. Toggle **Deploy To** to enable data deployment to a Salesforce Org.
       2. Select the destination org from the dropdown list .
    2. **Commit To**
       1. Toggle **Commit To** to push changes to a version control system.
       2. Choose the repository and branch to which changes should be committed&#x20;

    <figure><img src="../../../../../../.gitbook/assets/9 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>
2.  **Object Configuration(s)**

    Once the deployment targets defined, the interface displays configuration parameters for each object in the selected templates.

    1. **Parameters Include:**
       1. **Object Name**\
          Displays the Salesforce object included in the template.
       2. **External ID Mappings**\
          Used to identify matching records between source and destination orgs. Editable by clicking the pencil icon next to the mapping.
       3. **Applied Filters**\
          Displays SOQL queries or filters that limit the data being migrated..&#x20;
3.  **Editing External ID Mappings**

    External ID mappings can be configured for each object to facilitate accurate record matching between the source and destination environments.

    1. Click the **pencil icon** beside the External ID Mapping of the object to edit.
    2. In the **External ID Mappings** window:
       * Select the **Source External ID** from the dropdown.
       * Select the corresponding **Destination External ID**.

    <figure><img src="../../../../../../.gitbook/assets/9.1 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../../.gitbook/assets/10 - Deploy From Version Control (1).png" alt=""><figcaption></figcaption></figure>
4.  **Deployment Options**

    The **Deployment Options** section defines key behaviors that control how the CI Job executes in the Salesforce environment. These toggles enable or disable specific mechanisms that influence data handling, automation, and commit actions during deployment.

    The available deployment toggles include:

    * **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment
    * **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in a go from the source and destination org.
    * **Use UTF-8 file encoding for file read and write operations:** Use **UTF-8** as the internal representation for all string data. Text is automatically transcoded between the local encoding and UTF-8 when reading from or writing to files.
      * **Enable UTF-8** if your data contains **only English alphabets**.
      * **Disable UTF-8** if your data includes **non-English characters** to avoid encoding issues.
      * UTF-8 should be **enabled by default**, aligning with Salesforce’s recommended encoding standards.
    * **Automap User/Owner Data:**&#x20;
    * **Disable Validation Rules:** Select this option to temporarily deactivate validation rules on objects included in the deployment. This helps ensure smoother deployments without interruptions caused by rule enforcement.
    * **Insert/Update with Null Values:** When enabled, this option allows fields with `null` values in the source org to be inserted or updated as `null` in the destination org. It ensures data consistency by reflecting blank or cleared values during migration.
    * **Enable Rollback:** Enable this option to allow rollback of the deployment, if needed. Only components explicitly marked for **“Rollback”** during deployment will be eligible for rollback after completion.
5.  **Post-Deployment Activities**:

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

    <figure><img src="../../../../../../.gitbook/assets/14 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>
8.  Click **Save** to create a CI Job configuration. On clicking "Save", the interface will navigate to the "CI Job List" page.



    <figure><img src="../../../../../../.gitbook/assets/15 - Deploy From Version Control.png" alt=""><figcaption></figcaption></figure>



























































































