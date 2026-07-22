# Feature Deployment History

### Feature Deployment <a href="#feature-deployment" id="feature-deployment"></a>

**Feature Deployment** is a streamlined process that enables the deployment of both **metadata** and **data components** by leveraging a **Feature Migration Template** or a **pre-configured dataset** sourced either from your **Salesforce Org** or **Version Control** system.

### Step-By-Step Guide:

The following flow provides detailed information about the "Feature Deployment History" page layout.&#x20;

1. The **Feature Deployment History** provides a comprehensive log of all deployments previously executed through **AutoRABIT**
2.  Click on the **"Deployment History"** option under the "nCino" module

    <figure><img src="../../../../../.gitbook/assets/1 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
3. Observe the following options available on the "Deployment History" page:
   1. The following are the filters through which the required deployments can be searched by.
      1.  **Deployed By**: Allows you to filter the deployment history by the user who executed the deployment.

          * **All** – Shows deployments by all users.
          * **My Deployments** – Shows deployments initiated by the currently logged-in user.
          * **Others** – Displays deployments performed by other users.

          <figure><img src="../../../../../.gitbook/assets/2 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
   2. **Label Name**: Input the lable name to search the deployments through the label names
   3. **Status**: A dropdown to filter deployments by their execution status (e.g., Success, Failure, In Progress).
   4.  **Filters**: The **Filters** panel allows you to refine and narrow down the list of feature deployments based on specific criteria.

       <figure><img src="../../../../../.gitbook/assets/2.0 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

       1.  &#x20;This is helpful in quickly locating the relevant deployments without manually scrolling through large records.

           **Available Filter Options:**

           * **Feature Name**\
             Enter or select the specific nCino feature (e.g., Forms, Rules Engine, User Interface) you want to filter the deployments by.
           * **Version**\
             Use this to filter deployments by the associated feature version (e.g., "Fall 2023 Rel - v1").
           * **Deployed By**\
             Specify the user who executed the deployment. This is especially useful in multi-user environments to isolate individual contributions.
           * **Date Range**\
             Filter deployments based on when they were executed. You can define a custom date range to focus on a specific time window (e.g., deployments completed in the last month).

           **Additional Options:**

           * **Reset**\
             Clears all selected filter criteria and restores the full deployment list.
           * **Apply**\
             Applies the selected filters to the deployment history list and displays the results instantly.
   5.  **Column Headers Overview**

       The highlighted section displays the key columns in the **Deployment History** table, which provides a comprehensive view of all the feature deployments.&#x20;

       <figure><img src="../../../../../.gitbook/assets/3 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>


   6. Here's what each column represents:
      1.  **Deployment Label**

          This is the name or label assigned to each deployment, either manually by the user or system-generated. It helps in easily identifying and referencing specific deployments.
      2.  **Feature**

          Indicates the specific **nCino feature** that was deployed (e.g., User Interface, Forms, Rules Engine). This allows users to track deployments by functional component.
      3.  **Version**

          Displays the version of the deployed feature or template (e.g., _Fall 2023 Rel - v1_). Helps maintain traceability across different release versions.
      4.  **Iteration**

          Specifies the deployment iteration for that feature. This is particularly useful when the same feature is deployed multiple times with different configurations or updates.
      5.  **Deployed Date**

          Shows the exact **timestamp** when the deployment was executed. This is important for tracking deployment timelines and auditing activity.
      6.  **Status**

          Indicates the result of the deployment with visual markers:

          * Green Check – Success
          * Red Cross – Failed deployment
          * Yellow Exclamation – Partially Successful
          * Dash – Status pending or staging
      7.  **Action Buttons**

          Provides quick-access options for each deployment:

          *   **Deployment Queue**: View all deployments currently in progress or waiting to be executed.

              <figure><img src="../../../../../.gitbook/assets/4 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

              <figure><img src="../../../../../.gitbook/assets/4.0 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
          *   **Commit Queue**: Track metadata or data commits queued or being processed.

              <figure><img src="../../../../../.gitbook/assets/5 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

              <figure><img src="../../../../../.gitbook/assets/5.0 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
          * **Create Feature Deployment**: Start a new deployment by selecting components and configuring the deployment settings.
4. **Actions Menu:** The **Actions menu** provides contextual options for each deployment entry:
   1.  **Deploy**\
       Initiates the deployment process for the selected configuration again. This option is visible when the deployment can be re-executed.

       <figure><img src="../../../../../.gitbook/assets/6 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
   2.  **Deploy Configuration Panel**

       After selecting **Deploy** from the Actions menu, this screen allows you to configure deployment options and choose the **destination org** where your metadata and data will be deployed.

       <figure><img src="../../../../../.gitbook/assets/6.1 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
   3.  **Destination Org**

       Use the dropdown to select the Salesforce org to which the deployment should be executed.

       <figure><img src="../../../../../.gitbook/assets/6.2 - Feature Deployment History Page (1).png" alt=""><figcaption></figcaption></figure>
   4.  **Deployment Options**

       Toggle the following settings as needed for the deployment:

       * **Disable Workflow Rules** – Temporarily disables workflow rules during deployment.
       * **Disable Validation Rules** – Prevents validation rules from interfering with the deployment process.
       * **Use Bulk API** – Enables deployment via Salesforce Bulk API for better performance with large datasets.
       * **Use UTF-8 File Encoding** – Ensures proper encoding, especially when handling multilingual or special characters.
       * **Insert/Update With Null Values** – Allows null values from the source to overwrite values in the target org.
       * **Automap User/Owner Data** – Automatically maps user and owner fields during deployment.
       * **Enable Rollback** – Allows rollback of components marked for rollback post-deployment if needed.
   5.  **External Field Mappings**

       Use this to map **External ID fields** for each object between source and destination orgs:

       * **Source** – Select the field from the source dataset (typically a CSV or metadata).
       * **Destination** – Select the corresponding External ID field from the destination org.
   6.  **Deploy / Cancel**

       Once all configurations are in place:

       * Click **Deploy** to initiate the deployment.
       * Click **Cancel** to exit without making changes.
5.  **Re-Deploy Configuration Panel**

    Selecting **Re-Deploy** from the Actions menu in the Deployment History opens the configuration screen, which mirrors the initial deployment setup.

    <figure><img src="../../../../../.gitbook/assets/7 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
6.  #### **Editable External Field Mappings**

    The **External Field Mappings** section displays object-level mappings between source and destination environments. Each row in the mapping table includes:



    <figure><img src="../../../../../.gitbook/assets/7.0 - Feature Deployment History Page (2).png" alt=""><figcaption></figcaption></figure>

    *   **Object Name**: Identifies the object included in the deployment.

        * **Source**: Dropdown menu to select the external ID field from the source dataset.
        * **Destination**: Dropdown menu to assign the corresponding external ID field in the destination org.
        * **Actions**:
          * ✏️ Modify the selected mapping fields if needed.
          * ✅ Confirm the mapping.
          * ❌ Remove the mapping.

        <figure><img src="../../../../../.gitbook/assets/7.1 - Feature Deployment History Page (3).png" alt=""><figcaption></figcaption></figure>
7.  #### **Deployment History – Summary and Iterations**

    The **Actions** menu for each entry in the Deployment History includes two key options: **Summary** and **Iterations**. These provide detailed insights into individual deployments and their versioned executions.

    <figure><img src="../../../../../.gitbook/assets/8 - Feature Deployment History Page (1).png" alt=""><figcaption></figcaption></figure>
8.  #### **Deployment Summary**

    Selecting **Summary** opens a side panel displaying key information related to the selected deployment:

    * **Label**: Name of the deployment execution.
    * **Feature**: The nCino feature associated with the deployment.
    * **Status**: Execution status (e.g., Success).
    * **Version**: Version of the feature being deployed.
    * **Created By**: The identity of the initiator of the deployment.
    * **Created Date**: Timestamp when the deployment was executed.
    * **Duration**: Time taken to complete the deployment.
    * **Source Branch**: Git branch from which the deployment was triggered.
    * **Source Repository**: The Git repository associated with the deployment.
    * **Description**: Any notes or context added for the deployment (if available).



    <figure><img src="../../../../../.gitbook/assets/8.0 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
9. This view provides a quick snapshot of the deployment details for auditing and traceability.
10. #### **Deployment Iterations**

    Selecting **Iterations** opens a full-page view showing all versioned executions for a given deployment label. Each iteration represents a separate execution attempt for the same deployment configuration.

    <figure><img src="../../../../../.gitbook/assets/9 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
11. The **Deployment Iterations** table includes the following columns:

    * **Iteration No**: Numeric order of each execution.
    * **Destination SF Org Name**: Target Salesforce org used for deployment.
    * **Created Date**: Timestamp when the iteration was initiated.
    * **Duration**: Total time taken for the iteration to complete.
    * **Status**: Indicates whether the iteration succeeded, failed, or is in progress.
    * **Actions**: Options to re-deploy or view further details for each iteration.

    This screen allows tracking of multiple deployment attempts for a single feature, ensuring version control and deployment consistency.

    <figure><img src="../../../../../.gitbook/assets/9.0 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
12. #### Re-Deploy Panel:  When selecting “Re-Deploy,” a side panel opens with redeployment options.

    1. **Destination Org**: Dropdown to select the target Salesforce org.
    2. **Deployment Settings**:
       * Disable Workflow Rules
       * Disable Validation Rules
       * Use Bulk API
       * Insert/Update With Null Values
       * Use UTF-8 Encoding
       * Automap User/Owner Data
       * Enable Rollback
       * **External Field Mappings**:
         * **Object name**: Lists each object participating in the deployment.
         * **Source & Destination**: Defines field-level mappings used to match source and target data.
         * **Actions**: Edit or delete mapping rows.

    <figure><img src="../../../../../.gitbook/assets/9.2 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/9.3 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
13. **Iteration Actions**

    From the **Actions** menu on the Iteration list:

    * **Deploy:** Clicking on this will open the "Deployment" window where the deployments can be performed.
    * **Iteration Details**: Opens a breakdown of objects deployed in that iteration.
    * [**Compare**](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/ncino/ncino-compare): Triggers a differential view between iterations.

    <figure><img src="../../../../../.gitbook/assets/9.4 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
14. #### Feature Details View

    Presents deployment statistics for each object in the selected iteration.

    * **Name**: API name of the deployed object.
    * **Retrieved count**: Total records fetched from the source.
    * **Status**: Success icon if the object deployed without errors.
    * **Success count**: Number of records successfully deployed.
    * **Failed count**: Number of records that failed during deployment.

    Icons beside each count enable download of corresponding data.

    <figure><img src="../../../../../.gitbook/assets/9.5 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
15. #### Download & Log Access

    Two options available in the top-right corner:

    *   **Download**: Exports object deployment data.

        <figure><img src="../../../../../.gitbook/assets/9.6 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
    *   **View Logs**: Opens detailed deployment logs.

        <figure><img src="../../../../../.gitbook/assets/9.7 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/9.7.1 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
16. #### Retrieved Count Drill-Down: Clicking on a number under "Retrieved count" opens a list of deployed records.

    *   **Destination Id**: Salesforce record IDs in the destination org.

        <figure><img src="../../../../../.gitbook/assets/9.8 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/9.8.1 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>
    * **Status**: Indicates action taken on each record (e.g., "Item Updated").

    #### Success Count Drill-Down: Similarly, selecting a number under "Success count" shows the same list as retrieved count.

    *   Confirms that all retrieved records were processed successfully.

        <figure><img src="../../../../../.gitbook/assets/9.9 - Feature Deployment History Page (1).png" alt=""><figcaption></figcaption></figure>

        <figure><img src="../../../../../.gitbook/assets/9.9.1 - Feature Deployment History Page.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: AutoRABIT recommends fixing the errors generated and redeploying the process once again until the status changes to **Success**.
{% endhint %}



