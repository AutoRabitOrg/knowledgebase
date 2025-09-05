# nCino Compare

#### **Introduction**

The Compare and Selective Deployment functionality in nCino enables users to perform detailed comparisons between datasets and object records across Salesforce environments or between a Salesforce Org and a version control repository. This process helps identify changes and selectively promote only the required records to the intended target environment.

**Overview**

* **Flexible Comparison Options**\
  Perform comparisons between two Salesforce Orgs (_Org-to-Org_) or between a Salesforce Org and a version control repository (_Org-to-Version Control_).
* **Relational Comparison Support**\
  Execute relational comparisons that take into account object relationships, ensuring accuracy in identifying relevant data changes.
* **Granular Record Selection**\
  View and select individual records at any level of the comparison hierarchy, providing full control over what is promoted.
* **Save and Reuse Selections**\
  Save selected records during comparison to revisit or finalize at a later stage, supporting iterative workflows.
* **Deployment Execution**\
  Proceed with deployment using the **Save and Deploy** option, which finalizes the selection and initiates the deployment process.
* **Object Summary and RBC Integration**\
  Access a consolidated _Object Summary_ screen to review selected records before deployment. From here, initiate RBC-based deployments directly.

## Step-by-Step Guide - Initiating Compare Operation

### Initiating Compare Operation

#### Feature Deployment – Template & Version Control&#x20;

1.  Click on "Create Feature Dployment" to initate the featre deployment creation



    <figure><img src="../../../../.gitbook/assets/Compare - 1.png" alt=""><figcaption></figcaption></figure>
2.  Select **“Template”** or **“Version Control”** to reveal the **Retrieve Dataset** option.

    <figure><img src="../../../../.gitbook/assets/Compare - 1.1 (1).png" alt=""><figcaption></figcaption></figure>
3. Clicking it redirects to the **Deployment History** page.
4. On that page, use **View Dataset** to open the dataset.

#### Feature Deployment – Using Salesforce Org

1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2.  Refer the "[Feature Deployment](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/ncino/feature-deployment)" section for the creation of a feature deployment.

    <figure><img src="../../../../.gitbook/assets/Compare - 1.2.png" alt=""><figcaption></figcaption></figure>
3. Click **Retrieve Dataset** to start a comparison.
4. This would redirect the flow to the Deployment History.

#### Perform Compare

1. **Access Compare Option**
   *   From the **Deployment Iterations** page, select the ellipsis (three dots) for a specific iteration.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.png" alt=""><figcaption></figcaption></figure>
   *   Choose **Compare** to analyze dataset differences between environments.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.1.png" alt=""><figcaption></figcaption></figure>
   * This helps validate consistency of deployed records.
2. **Select Comparison Destination**&#x20;
   * In the **Compare** window, select between the destination type:
     *   **Salesforce Org**: Compares records with another Salesforce environment.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.png" alt=""><figcaption></figcaption></figure>
     *   **Version Control**: Compares records with version-controlled data.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.1.png" alt=""><figcaption></figcaption></figure>
   * Choose the destination org or repository to proceed.
3. **Configure Comparison Parameters**
   *   Provide details such as:

       * **Feature Name**
       * **Object**
       * **Unique Id** (used to uniquely identify records)

       <figure><img src="../../../../.gitbook/assets/Compare - 4.png" alt=""><figcaption></figcaption></figure>
   *   Optionally, select fields to **exclude from comparison** (e.g., system fields like CreatedDate).

       <figure><img src="../../../../.gitbook/assets/Compare - 4.1.png" alt=""><figcaption></figcaption></figure>
   * Excluding non-essential fields avoids unnecessary mismatches.
4. **Run Comparison**
   *   After configuring all parameters, click **Compare**.

       <figure><img src="../../../../.gitbook/assets/Compare - 5.png" alt=""><figcaption></figcaption></figure>
   * The system validates data consistency between the chosen dataset and the destination.
   * This step ensures records are aligned across environments or with version control.

{% hint style="info" %}
Note:- Records with differences were&#x20;
{% endhint %}

5. **Compare Results – Relational Compare Results**

*   From the **Compare Results** page, the _Relational Compare Results_ section provides an overview of the comparison context.

    <figure><img src="../../../../.gitbook/assets/Compare - 7.png" alt=""><figcaption></figcaption></figure>
* The **Source** area displays the **org, label name, feature name, and version details** for the dataset being compared.
* The **Destination** area indicates the Salesforce org used for the comparison.
* The **Selected data** section lists the object and unique ID that serve as the basis of the comparison.

1. **Compare Results – Filters and Search Options**
   *   The **comparison filters** allow refinement of records during comparison.

       <figure><img src="../../../../.gitbook/assets/Compare - 8.png" alt=""><figcaption></figcaption></figure>
   * Available options include **Object**, **Unique ID**, and **Exclude from compare**, which can be customized to focus only on relevant records.
   * Additional filters such as **Field selection** and **Search value** enable precise comparisons.
   * The option **Show only modified columns** highlights changes between source and destination.
   * A **Columns menu** is available to adjust the visible fields in the results grid.
2. **Filter Records**
   * From the Compare Results page, expand the **Filter** dropdown to refine comparison records.
   *   Options available include **All**, **Added**, and **Modified**.

       <figure><img src="../../../../.gitbook/assets/Compare - 9.png" alt=""><figcaption></figcaption></figure>
   * Selecting **Added** shows only new records introduced in the source compared to the destination.
   * Selecting **Modified** highlights only the records with changes between the two environments.
3. **Filter – Added Records**
   *   From the **Compare Results** page, select **Added** from the Filter dropdown.

       <figure><img src="../../../../.gitbook/assets/Compare - 10.png" alt=""><figcaption></figcaption></figure>
   * This option displays only the records that exist in the source but are not present in the destination.
   * If no new records are detected, the system will display **No records found**.
4. **Filter – Modified Records**
   *   Select **Modified** from the Filter dropdown.

       <figure><img src="../../../../.gitbook/assets/Compare - 11.png" alt=""><figcaption></figcaption></figure>
   * This option highlights only the records that have differences between the source and destination environments.
   *   Modified records are displayed with changes highlighted for quick identification.

       <figure><img src="../../../../.gitbook/assets/Compare - 12.png" alt=""><figcaption></figcaption></figure>
5. **Field Selection**
   *   Use the **Fields** dropdown to choose a specific field for comparison.

       <figure><img src="../../../../.gitbook/assets/Compare - 13.png" alt=""><figcaption></figcaption></figure>
   * Available options include system fields (e.g., Id, IsDeleted, CreatedDate) and business fields (e.g., Name, Description).
   * Selecting a field enables targeted filtering and analysis of record-level changes.
6. **Search Records**
   *   Enter a specific **Search Value** in combination with the selected field to locate records quickly.

       <figure><img src="../../../../.gitbook/assets/Compare - 14.png" alt=""><figcaption></figcaption></figure>
   * For example, searching by **Name** with value `RGC-000025111` will return the corresponding record.
   * This feature ensures faster navigation when working with large datasets.
7. **Show Only Modified Columns**
   *   Toggle the **Show only modified columns** option to simplify the comparison view.

       <figure><img src="../../../../.gitbook/assets/Compare - 15.png" alt=""><figcaption></figcaption></figure>
   * When enabled, the display is restricted to columns that contain differences.
   * This helps reduce noise and focus on changes between environments.
8. **Column Selection**
   *   Use the **Columns** dropdown to customize which fields are displayed in the comparison results.

       <figure><img src="../../../../.gitbook/assets/Compare - 16.png" alt=""><figcaption></figcaption></figure>
   * Specific fields can be checked or unchecked to include or exclude them from the grid.
   * This provides flexibility to tailor the view according to analysis needs.
9. **Download Compare Results**
   *   Select the **Download** icon to export comparison results.

       <figure><img src="../../../../.gitbook/assets/Compare - 17.png" alt=""><figcaption></figcaption></figure>
   * Options include downloading either **Records displayed on the page** or **All Records**.
   * Exported results allow further review or archival outside the system.
10. **View Record**
    * From the Compare Results page, locate the row you want to inspect.
    *   Click the **View record** (document) icon to open field-level details.

        <figure><img src="../../../../.gitbook/assets/Compare - 18.png" alt=""><figcaption></figcaption></figure>
    * Use this option when you need to drill into a single record before taking further action.
11. **Record Details**
    *   When the record is opened, a detailed comparison window displays the record values from both the **Source** and **Destination**.

        <figure><img src="../../../../.gitbook/assets/Compare - 19.png" alt=""><figcaption></figcaption></figure>
    * Each field is listed side by side, with differences highlighted for quick identification.
    * This view allows you to precisely verify changes between the two environments.
12. **Open Related Records**
    *   From the Compare Results grid, select the **Related records** icon to include parent–child relational data in the comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 20.png" alt=""><figcaption></figcaption></figure>
    * This feature helps in validating complex datasets where related objects must also be compared.
13. **Configure Related Records**
    * In the Related Records setup window, provide details for both the **Parent** and **Child** objects.
    *   Each section requires selecting the **Object**, **Unique Id**, and optional **Exclude from compare** fields.

        <figure><img src="../../../../.gitbook/assets/Compare - 21.png" alt=""><figcaption></figcaption></figure>
    * Once configured, relational comparisons can be executed across linked datasets.
14. **Parent Object Selection**
    *   Under the Parent section, select the Salesforce object that will serve as the parent in the comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 22.png" alt=""><figcaption></figcaption></figure>
    * For example, you may choose **LLC\_BI\_\_Risk\_Grade\_Template\_\_c**.
    * Exclude fields that are not relevant, such as system fields, to avoid unnecessary mismatches.
15. **Parent Configuration**
    *   The Parent section is completed by configuring the **Object**, **Unique Id**, and **Excluded fields**.

        <figure><img src="../../../../.gitbook/assets/Compare - 23.png" alt=""><figcaption></figcaption></figure>
    * This ensures that parent records are correctly matched and compared during the execution.
16. **Child Object Selection**
    *   Under the Child section, select the Salesforce object related to the parent.

        <figure><img src="../../../../.gitbook/assets/Compare - 24.png" alt=""><figcaption></figcaption></figure>
    * For example, you may choose **LLC\_BI\_\_Risk\_Grade\_Factor\_\_c**.
    * This establishes the parent–child link for the relational comparison.
17. **Child Configuration and Run**
    *   The Child section is completed by configuring the **Object**, **Unique Id**, and **Excluded fields**.

        <figure><img src="../../../../.gitbook/assets/Compare - 25.png" alt=""><figcaption></figcaption></figure>
    * With both Parent and Child sections set, click **Compare** to execute the relational comparison.
    * The system then evaluates parent and child records together to provide accurate results.
18. **Pagination Controls**
    * From the **Compare Results** page, scroll to the bottom of the results table.
    *   Use the **Previous**, **Next**, and page number controls to navigate through record sets.

        <figure><img src="../../../../.gitbook/assets/Compare - 26.png" alt=""><figcaption></figcaption></figure>
    * This allows reviewing large datasets when records exceed the page display limit.
19. **Save and Continue / Save and Deploy**
    *   From the **Compare Results** page, select the records you want to apply actions on.

        <figure><img src="../../../../.gitbook/assets/Compare - 27.png" alt=""><figcaption></figcaption></figure>
    * Click **Save and continue** to save progress without deploying changes.
    * Click **Save and deploy** to save and deploy the compared records to the target org.
    * This ensures flexibility depending on whether deployment is needed immediately.
20. **Access Related Records**
    *   From the **Compare Results** page, select the **Related records** (linked arrows) icon for a row.

        <figure><img src="../../../../.gitbook/assets/Compare - 28.png" alt=""><figcaption></figcaption></figure>
    * This opens options to configure parent or child objects for relational comparison.
    * Use this to validate hierarchical or dependent data between the source and destination orgs.
21. #### Run Relational Compare
    * From the **Related Records** window, verify that both the parent and child objects are configured.
    *   Click the **Compare** button at the bottom right to execute the relational comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 29.png" alt=""><figcaption></figcaption></figure>
    * This initiates the process of analyzing parent–child relationships between the source and destination environments.
22. #### Relational Compare Results – Parent
    * The **Compare Results** page displays relational results after the comparison runs.
    *   The selected **Source** and **Destination** records are shown with details such as _Id, Name, SystemModstamp, and Group Number_.

        <figure><img src="../../../../.gitbook/assets/Compare - 30.png" alt=""><figcaption></figcaption></figure>
    * The **Relational Parent** section expands, showing parent object comparisons for validation.
    * This ensures parent records are aligned before reviewing related child data.
23. #### Relational Compare Results – Child
    * Scroll within the **Compare Results** page to access the **Relational Child** section.
    *   All related child records appear under the parent comparison, with fields like _Id, Name, and SystemModstamp_.

        <figure><img src="../../../../.gitbook/assets/Compare - 31.png" alt=""><figcaption></figcaption></figure>
    * Use the checkboxes to select specific child records for further processing.
    * Finalize the process by clicking **Save and continue** or **Save and deploy** to apply changes.

{% hint style="info" %}
#### Relational Compare (Multi-Level)

* The relational compare feature supports performing comparisons across multiple hierarchical levels.
* Parent–child relationships can be expanded iteratively, enabling analysis down to the nth level.
* Each level of comparison preserves the context of the higher level, ensuring consistent and accurate evaluation across linked records.
* This functionality is essential when working with complex datasets where dependencies exist between multiple related objects.
{% endhint %}

24. **Preserve Child Record Selection**
    * From the Relational Compare Results page, navigate to the Relational Child section.
    *   Select the desired child records using the checkboxes.

        <figure><img src="../../../../.gitbook/assets/Compare - 32.png" alt=""><figcaption></figcaption></figure>
    * Click **Save and continue** to preserve your record selections.
    * This action ensures selections are stored before proceeding further in the deployment flow.
25. **Confirmation of Record Selection**
    *   After saving, a success message appears at the top right of the screen.

        <figure><img src="../../../../.gitbook/assets/Compare - 33.png" alt=""><figcaption></figcaption></figure>
    * The message confirms that your record selections have been preserved.
    * Continue with the next steps to choose records for deployment.
26. **Deploy Selected Records**
    * From the Relational Compare Results page, review the preserved records.
    *   Click **Save and deploy** at the bottom right to initiate deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 34.png" alt=""><figcaption></figcaption></figure>
    * This action begins the process of pushing the selected data to the destination environment.
27. **Review Object Summary**
    *   The **Object Summary** window displays the list of objects included in the deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 35.png" alt=""><figcaption></figcaption></figure>
    * Each object name is listed along with the count of selected records.
    * This provides a consolidated overview of deployment scope before committing.
28. **Confirm Object Summary**
    * Review the listed objects and selected records in the Object Summary window.
    *   Click **OK** to confirm and proceed with deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 36.png" alt=""><figcaption></figcaption></figure>
    * The system redirects you back to the results page, with data now prepared for commit.
29. #### Deployment Staging
    * From the Deployment Iterations page, observe that the deployment is marked as **Staging** immediately after clicking **Save & Deploy**.
    *   At this stage, the deployment is prepared but not yet executed to the destination org.

        <figure><img src="../../../../.gitbook/assets/Compare - 37 (2).png" alt=""><figcaption></figcaption></figure>
    * To proceed with the actual deployment, click the **Deploy** or **Re-deploy** button (rocket icon) under the Actions column.
    * This ensures deployment is only executed once explicitly triggered.
    *   To observe the details of the compare operation, click on the "Iteration Details" option.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.1.1.png" alt=""><figcaption></figcaption></figure>
30. **Deployment Iteration Details**
    * From the Deployment Iterations page, click the **iteration label** to expand feature details.
    *   The panel on the right displays the **feature package name** associated with the deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.2.png" alt=""><figcaption></figcaption></figure>
    * Use this to review which feature package is linked before proceeding further.
31. **Feature Object Overview**
    *   Expanding the feature package displays the **objects included** in the deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.3.png" alt=""><figcaption></figcaption></figure>
    * Each object shows its **name**, **available count**, and **selected count** of records.
    * This allows validation of the exact objects and record counts being deployed.
32. **Object Deployment Details & Validation Summary**
    *   From the Feature Details panel, click an object (e.g., _Eligibility\_\_c_) to open its deployment details.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.4.png" alt=""><figcaption></figcaption></figure>
    * The object view shows applied filters, external ID mappings, and configuration elements like **validation rules** and **workflow rules**.
    *   Summaries are provided for both failed and successful records:

        * **Failed Records Summary** highlights issues such as storage limits, bad picklists, trigger errors, or other causes.
        * **Successful Records Summary** displays DML operations with record counts for **updates** and **creates**.



        <figure><img src="../../../../.gitbook/assets/Compare - 37.5.png" alt=""><figcaption></figcaption></figure>
    * Use this information to validate that object-level deployments are configured correctly and no unexpected errors occurred.
33. **View Object Records**
    *   From the **Feature Details** panel, locate the object (e.g., _Eligibility\_\_c_) and check the **Selected count** column to see how many records were included in the deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.6.png" alt=""><figcaption></figcaption></figure>
    * Click the selected count value to expand and view the **Object Records** list.
    *   The records table displays detailed fields such as **Id, OwnerId, IsDeleted, Name, RecordTypeId, CreatedDate, and CreatedById**.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.7.png" alt=""><figcaption></figcaption></figure>
    * Use this view to validate which records were specifically chosen for deployment and confirm their metadata details before execution.
34. **Logs Verification**
    *   Click **View Logs** to open the **Feature Logs** panel.

        <figure><img src="../../../../.gitbook/assets/Compare - 37.8.png" alt=""><figcaption></figcaption></figure>
    *   Inspect each step of the process:

        * Deployment Initialization
        * Data Retrieval
        * Object Configuration
        * Commit Initialization
        * Data Deployment

        <figure><img src="../../../../.gitbook/assets/Compare - 37.9.png" alt=""><figcaption></figcaption></figure>
    * Ensure each step is marked complete (✔) to validate a successful deployment.
35. **Deploy to Destination**
    *   From the Deployment Iterations page, initiate deployment by clicking the **Deploy** button (rocket icon) beside the staging iteration.

        <figure><img src="../../../../.gitbook/assets/Compare - 38.png" alt=""><figcaption></figcaption></figure>
    *   Configure deployment options such as disabling workflow/validation rules, handling null values, and adjusting field mappings.

        <figure><img src="../../../../.gitbook/assets/Compare - 39.png" alt=""><figcaption></figcaption></figure>
    *   Confirm the action by selecting **Deploy** to begin the process.

        <figure><img src="../../../../.gitbook/assets/Compare - 40.png" alt=""><figcaption></figcaption></figure>
    * Once the deployment is completed, an **Iteration number** is automatically assigned, which uniquely identifies the run for tracking and review.
36. **Deployment Iteration Results**
    *   After deployment, the **Deployment Iterations** page lists all iterations with their respective statuses.

        <figure><img src="../../../../.gitbook/assets/Compare - 42.png" alt=""><figcaption></figcaption></figure>
    * A green check mark indicates successful completion, while each new deployment adds an iteration to the list.
    *   Use the **Iteration Details** option under Actions to drill into a specific run.

        <figure><img src="../../../../.gitbook/assets/Compare - 43.png" alt=""><figcaption></figcaption></figure>
    *   Within the feature details, review record-level outcomes such as **retrieved counts, success counts, and failed counts** for each object.

        <figure><img src="../../../../.gitbook/assets/Compare - 44.png" alt=""><figcaption></figcaption></figure>
    *   Selecting an object displays a breakdown of updates, showing exactly which records were created or updated in the destination org.

        <figure><img src="../../../../.gitbook/assets/Compare - 45.png" alt=""><figcaption></figcaption></figure>
