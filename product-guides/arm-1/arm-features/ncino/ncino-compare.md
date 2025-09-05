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

1. **Access Compare Option (Screen Compare - 2)**
   *   From the **Deployment Iterations** page, select the ellipsis (three dots) for a specific iteration.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.png" alt=""><figcaption></figcaption></figure>
   *   Choose **Compare** to analyze dataset differences between environments.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.1.png" alt=""><figcaption></figcaption></figure>
   * This helps validate consistency of deployed records.
2. **Select Comparison Destination (Screen Compare - 3)**
   * In the **Compare** window, select between the destination type:
     *   **Salesforce Org**: Compares records with another Salesforce environment.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.png" alt=""><figcaption></figcaption></figure>
     *   **Version Control**: Compares records with version-controlled data.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.1.png" alt=""><figcaption></figcaption></figure>
   * Choose the destination org or repository to proceed.
3. **Configure Comparison Parameters (Screens Compare - 4 & 4.1)**
   *   Provide details such as:

       * **Feature Name**
       * **Object**
       * **Unique Id** (used to uniquely identify records)

       <figure><img src="../../../../.gitbook/assets/Compare - 4.png" alt=""><figcaption></figcaption></figure>
   *   Optionally, select fields to **exclude from comparison** (e.g., system fields like CreatedDate).

       <figure><img src="../../../../.gitbook/assets/Compare - 4.1.png" alt=""><figcaption></figcaption></figure>
   * Excluding non-essential fields avoids unnecessary mismatches.
4. **Run Comparison (Screen Compare - 5)**
   *   After configuring all parameters, click **Compare**.

       <figure><img src="../../../../.gitbook/assets/Compare - 5.png" alt=""><figcaption></figcaption></figure>
   * The system validates data consistency between the chosen dataset and the destination.
   * This step ensures records are aligned across environments or with version control.

{% hint style="info" %}
Note:- Records with differences were&#x20;
{% endhint %}

5. **Compare Results – Relational Compare Results (Screen Compare - 7)**

*   From the **Compare Results** page, the _Relational Compare Results_ section provides an overview of the comparison context.

    <figure><img src="../../../../.gitbook/assets/Compare - 7.png" alt=""><figcaption></figcaption></figure>
* The **Source** area displays the **org, label name, feature name, and version details** for the dataset being compared.
* The **Destination** area indicates the Salesforce org used for the comparison.
* The **Selected data** section lists the object and unique ID that serve as the basis of the comparison.

1. **Compare Results – Filters and Search Options (Screen Compare - 8)**
   *   The **comparison filters** allow refinement of records during comparison.

       <figure><img src="../../../../.gitbook/assets/Compare - 8.png" alt=""><figcaption></figcaption></figure>
   * Available options include **Object**, **Unique ID**, and **Exclude from compare**, which can be customized to focus only on relevant records.
   * Additional filters such as **Field selection** and **Search value** enable precise comparisons.
   * The option **Show only modified columns** highlights changes between source and destination.
   * A **Columns menu** is available to adjust the visible fields in the results grid.
2. **Filter Records (Screen Compare – 9)**
   * From the Compare Results page, expand the **Filter** dropdown to refine comparison records.
   *   Options available include **All**, **Added**, and **Modified**.

       <figure><img src="../../../../.gitbook/assets/Compare - 9.png" alt=""><figcaption></figcaption></figure>
   * Selecting **Added** shows only new records introduced in the source compared to the destination.
   * Selecting **Modified** highlights only the records with changes between the two environments.
3. **Filter – Added Records (Screen Compare – 10)**
   *   From the **Compare Results** page, select **Added** from the Filter dropdown.

       <figure><img src="../../../../.gitbook/assets/Compare - 10.png" alt=""><figcaption></figcaption></figure>
   * This option displays only the records that exist in the source but are not present in the destination.
   * If no new records are detected, the system will display **No records found**.
4. **Filter – Modified Records (Screen Compare – 11)**
   *   Select **Modified** from the Filter dropdown.

       <figure><img src="../../../../.gitbook/assets/Compare - 11.png" alt=""><figcaption></figcaption></figure>
   * This option highlights only the records that have differences between the source and destination environments.
   *   Modified records are displayed with changes highlighted for quick identification.

       <figure><img src="../../../../.gitbook/assets/Compare - 12.png" alt=""><figcaption></figcaption></figure>
5. **Field Selection (Screen Compare – 12)**
   *   Use the **Fields** dropdown to choose a specific field for comparison.

       <figure><img src="../../../../.gitbook/assets/Compare - 13.png" alt=""><figcaption></figcaption></figure>
   * Available options include system fields (e.g., Id, IsDeleted, CreatedDate) and business fields (e.g., Name, Description).
   * Selecting a field enables targeted filtering and analysis of record-level changes.
6. **Search Records (Screen Compare – 13)**
   *   Enter a specific **Search Value** in combination with the selected field to locate records quickly.

       <figure><img src="../../../../.gitbook/assets/Compare - 14.png" alt=""><figcaption></figcaption></figure>
   * For example, searching by **Name** with value `RGC-000025111` will return the corresponding record.
   * This feature ensures faster navigation when working with large datasets.
7. **Show Only Modified Columns (Screen Compare – 14)**
   *   Toggle the **Show only modified columns** option to simplify the comparison view.

       <figure><img src="../../../../.gitbook/assets/Compare - 15.png" alt=""><figcaption></figcaption></figure>
   * When enabled, the display is restricted to columns that contain differences.
   * This helps reduce noise and focus on changes between environments.
8. **Column Selection (Screen Compare – 15)**
   *   Use the **Columns** dropdown to customize which fields are displayed in the comparison results.

       <figure><img src="../../../../.gitbook/assets/Compare - 16.png" alt=""><figcaption></figcaption></figure>
   * Specific fields can be checked or unchecked to include or exclude them from the grid.
   * This provides flexibility to tailor the view according to analysis needs.
9. **Download Compare Results (Screen Compare – 16)**
   *   Select the **Download** icon to export comparison results.

       <figure><img src="../../../../.gitbook/assets/Compare - 17.png" alt=""><figcaption></figcaption></figure>
   * Options include downloading either **Records displayed on the page** or **All Records**.
   * Exported results allow further review or archival outside the system.
10. **View Record (Screen Compare – 18)**
    * From the Compare Results page, locate the row you want to inspect.
    *   Click the **View record** (document) icon to open field-level details.

        <figure><img src="../../../../.gitbook/assets/Compare - 18.png" alt=""><figcaption></figcaption></figure>
    * Use this option when you need to drill into a single record before taking further action.
11. **Record Details (Screen Compare – 19)**
    *   When the record is opened, a detailed comparison window displays the record values from both the **Source** and **Destination**.

        <figure><img src="../../../../.gitbook/assets/Compare - 19.png" alt=""><figcaption></figcaption></figure>
    * Each field is listed side by side, with differences highlighted for quick identification.
    * This view allows you to precisely verify changes between the two environments.
12. **Open Related Records (Screen Compare – 20)**
    *   From the Compare Results grid, select the **Related records** icon to include parent–child relational data in the comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 20.png" alt=""><figcaption></figcaption></figure>
    * This feature helps in validating complex datasets where related objects must also be compared.
13. **Configure Related Records (Screen Compare – 21)**
    * In the Related Records setup window, provide details for both the **Parent** and **Child** objects.
    *   Each section requires selecting the **Object**, **Unique Id**, and optional **Exclude from compare** fields.

        <figure><img src="../../../../.gitbook/assets/Compare - 21.png" alt=""><figcaption></figcaption></figure>
    * Once configured, relational comparisons can be executed across linked datasets.
14. **Parent Object Selection (Screen Compare – 22)**
    *   Under the Parent section, select the Salesforce object that will serve as the parent in the comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 22.png" alt=""><figcaption></figcaption></figure>
    * For example, you may choose **LLC\_BI\_\_Risk\_Grade\_Template\_\_c**.
    * Exclude fields that are not relevant, such as system fields, to avoid unnecessary mismatches.
15. **Parent Configuration (Screen Compare – 23)**
    *   The Parent section is completed by configuring the **Object**, **Unique Id**, and **Excluded fields**.

        <figure><img src="../../../../.gitbook/assets/Compare - 23.png" alt=""><figcaption></figcaption></figure>
    * This ensures that parent records are correctly matched and compared during the execution.
16. **Child Object Selection (Screen Compare – 24)**
    *   Under the Child section, select the Salesforce object related to the parent.

        <figure><img src="../../../../.gitbook/assets/Compare - 24.png" alt=""><figcaption></figcaption></figure>
    * For example, you may choose **LLC\_BI\_\_Risk\_Grade\_Factor\_\_c**.
    * This establishes the parent–child link for the relational comparison.
17. **Child Configuration and Run (Screen Compare – 25)**
    *   The Child section is completed by configuring the **Object**, **Unique Id**, and **Excluded fields**.

        <figure><img src="../../../../.gitbook/assets/Compare - 25.png" alt=""><figcaption></figcaption></figure>
    * With both Parent and Child sections set, click **Compare** to execute the relational comparison.
    * The system then evaluates parent and child records together to provide accurate results.
18. **Pagination Controls (Screen Compare – 26)**
    * From the **Compare Results** page, scroll to the bottom of the results table.
    *   Use the **Previous**, **Next**, and page number controls to navigate through record sets.

        <figure><img src="../../../../.gitbook/assets/Compare - 26.png" alt=""><figcaption></figcaption></figure>
    * This allows reviewing large datasets when records exceed the page display limit.
19. **Save and Continue / Save and Deploy (Screen Compare – 27)**
    *   From the **Compare Results** page, select the records you want to apply actions on.

        <figure><img src="../../../../.gitbook/assets/Compare - 27.png" alt=""><figcaption></figcaption></figure>
    * Click **Save and continue** to save progress without deploying changes.
    * Click **Save and deploy** to save and deploy the compared records to the target org.
    * This ensures flexibility depending on whether deployment is needed immediately.
20. **Access Related Records (Screen Compare – 28)**
    *   From the **Compare Results** page, select the **Related records** (linked arrows) icon for a row.

        <figure><img src="../../../../.gitbook/assets/Compare - 28.png" alt=""><figcaption></figcaption></figure>
    * This opens options to configure parent or child objects for relational comparison.
    * Use this to validate hierarchical or dependent data between the source and destination orgs.
21. #### Run Relational Compare (Screen Compare – 29)
    * From the **Related Records** window, verify that both the parent and child objects are configured.
    *   Click the **Compare** button at the bottom right to execute the relational comparison.

        <figure><img src="../../../../.gitbook/assets/Compare - 29.png" alt=""><figcaption></figcaption></figure>
    * This initiates the process of analyzing parent–child relationships between the source and destination environments.
22. #### Relational Compare Results – Parent (Screen Compare – 30)
    * The **Compare Results** page displays relational results after the comparison runs.
    *   The selected **Source** and **Destination** records are shown with details such as _Id, Name, SystemModstamp, and Group Number_.

        <figure><img src="../../../../.gitbook/assets/Compare - 30.png" alt=""><figcaption></figcaption></figure>
    * The **Relational Parent** section expands, showing parent object comparisons for validation.
    * This ensures parent records are aligned before reviewing related child data.
23. #### Relational Compare Results – Child (Screen Compare – 31)
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

24. **Preserve Child Record Selection (Screen Compare – 32)**
    * From the Relational Compare Results page, navigate to the Relational Child section.
    *   Select the desired child records using the checkboxes.

        <figure><img src="../../../../.gitbook/assets/Compare - 32.png" alt=""><figcaption></figcaption></figure>
    * Click **Save and continue** to preserve your record selections.
    * This action ensures selections are stored before proceeding further in the deployment flow.
25. **Confirmation of Record Selection (Screen Compare – 33)**
    *   After saving, a success message appears at the top right of the screen.

        <figure><img src="../../../../.gitbook/assets/Compare - 33.png" alt=""><figcaption></figcaption></figure>
    * The message confirms that your record selections have been preserved.
    * Continue with the next steps to choose records for deployment.
26. **Deploy Selected Records (Screen Compare – 34)**
    * From the Relational Compare Results page, review the preserved records.
    *   Click **Save and deploy** at the bottom right to initiate deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 34.png" alt=""><figcaption></figcaption></figure>
    * This action begins the process of pushing the selected data to the destination environment.
27. **Review Object Summary (Screen Compare – 35)**
    *   The **Object Summary** window displays the list of objects included in the deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 35.png" alt=""><figcaption></figcaption></figure>
    * Each object name is listed along with the count of selected records.
    * This provides a consolidated overview of deployment scope before committing.
28. **Confirm Object Summary (Screen Compare – 36)**
    * Review the listed objects and selected records in the Object Summary window.
    *   Click **OK** to confirm and proceed with deployment.

        <figure><img src="../../../../.gitbook/assets/Compare - 36.png" alt=""><figcaption></figcaption></figure>
    * The system redirects you back to the results page, with data now prepared for commit.
29. #### Deployment Staging (Screen Compare – 37)
    *   From the Deployment Iterations page, observe that the deployment is marked as **Staging** immediately after clicking **Save & Deploy**.


    * At this stage, the deployment is prepared but not yet executed to the destination org.
    * To proceed with the actual deployment, click the **Deploy** or **Re-deploy** button (rocket icon) under the Actions column.
    * This ensures deployment is only executed once explicitly triggered.











































1. Open the deployment and click **Compare**.

<figure><img src="../../../../.gitbook/assets/image (1505).png" alt="Compare button inside deployment view" width="375"><figcaption><p>Compare button inside deployment view</p></figcaption></figure>

2. Choose the type of comparison:
   * **Org-to-Org** (select **Salesforce Org**)
   * **Org-to-VC** (select **Version Control**)

<figure><img src="../../../../.gitbook/assets/image (1506).png" alt="Org-to-Org comparison selection" width="375"><figcaption><p>Org-to-Org comparison selection</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1507).png" alt="Org-to-VC comparison selection" width="375"><figcaption><p>Org-to-VC comparison selection</p></figcaption></figure>

### Compare Results

1. View differences highlighted in yellow (for changed destination values).
2. Configure comparison using:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare

<figure><img src="../../../../.gitbook/assets/image (1508).png" alt="Comparison fields and options" width="375"><figcaption><p>Comparison fields and options</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1509).png" alt="Compare results with yellow highlights" width="375"><figcaption><p>Compare results with yellow highlights</p></figcaption></figure>

3. Exclude fields from comparison (shown in light gray).
4. Use **Select** to choose current page or all records.
5. Use **Search by Field** to filter results.

<figure><img src="../../../../.gitbook/assets/image (1513).png" alt="Export and field selection options" width="375"><figcaption><p>Export and field selection options</p></figcaption></figure>

6. **Change View** to select which fields to show (max 25).

<figure><img src="../../../../.gitbook/assets/image (1514).png" alt="Change view to customize field display" width="375"><figcaption><p>Change view to customize field display</p></figcaption></figure>

7. Click **View Record** to compare source vs destination values.

<figure><img src="../../../../.gitbook/assets/image (1515).png" alt="View Record button for detailed comparison" width="375"><figcaption><p>View Record button for detailed comparison</p></figcaption></figure>

8. Use **Save and Continue** or **Save and Deploy** to proceed.

> **Note:** Record counts are shown on the Object Summary screen before deployment.

<figure><img src="../../../../.gitbook/assets/image (1516).png" alt="Object Summary screen after Save and Deploy" width="375"><figcaption><p>Object Summary screen after Save and Deploy</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1517).png" alt="Iteration staging page before deployment" width="375"><figcaption><p>Iteration staging page before deployment</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1518).png" alt="Popup showing selected records" width="375"><figcaption><p>Popup showing selected records</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1519).png" alt="Deploy confirmation screen" width="375"><figcaption><p>Deploy confirmation screen</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1520).png" alt="Success and failure record summary" width="375"><figcaption><p>Success and failure record summary</p></figcaption></figure>

***

## Relational Compare - Global & Record-Level

### Global Relational Compare

Performs a full compare to identify parent/child records related to selected objects.

<figure><img src="../../../../.gitbook/assets/image (1521).png" alt="Relational compare initiation for related records" width="375"><figcaption><p>Relational compare initiation for related records</p></figcaption></figure>

1. Choose parent/child object and Unique ID.
2. Select fields to exclude and click **Compare**.

### Record-Level Relational Compare

Compares one record at a time and lets you drill down further.

<figure><img src="../../../../.gitbook/assets/image (1522).png" alt="Record-level relational compare icon" width="375"><figcaption><p>Record-level relational compare icon</p></figcaption></figure>

* Supports multiple levels of nested comparison:
  * Level 1, 2, 3, etc.

<figure><img src="../../../../.gitbook/assets/image (1524).png" alt="Record-level comparison level 1" width="375"><figcaption><p>Record-level comparison level 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1525).png" alt="Record-level comparison level 2" width="375"><figcaption><p>Record-level comparison level 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1526).png" alt="Record-level with nested relational compare" width="375"><figcaption><p>Record-level with nested relational compare</p></figcaption></figure>

* Continue record selection:

<figure><img src="../../../../.gitbook/assets/image (1528).png" alt="Record selection after relational comparison" width="375"><figcaption><p>Record selection after relational comparison</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1529).png" alt="Parent and child record listing" width="375"><figcaption><p>Parent and child record listing</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1530).png" alt="Additional relational records selected" width="375"><figcaption><p>Additional relational records selected</p></figcaption></figure>

* Choose:
  * **Save and Continue** – Save and proceed.
  * **Save and Deploy** – Go to deployment screen.

<figure><img src="../../../../.gitbook/assets/image (1531).png" alt="Object Summary screen before final deployment" width="375"><figcaption><p>Object Summary screen before final deployment</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1532).png" alt="Selected records visible for deployment" width="375"><figcaption><p>Selected records visible for deployment</p></figcaption></figure>

* View selected records:

<figure><img src="../../../../.gitbook/assets/image (1533).png" alt="Popup of selected records before deployment" width="375"><figcaption><p>Popup of selected records before deployment</p></figcaption></figure>

* After deployment:

<figure><img src="../../../../.gitbook/assets/image (1534).png" alt="Deployment staging confirmation" width="375"><figcaption><p>Deployment staging confirmation</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1535).png" alt="Final deployment result with status" width="375"><figcaption><p>Final deployment result with status</p></figcaption></figure>
