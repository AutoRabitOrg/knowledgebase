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

## Step-by-Step Guide

### Initiating Compare Operation



## Step-by-Step Guide - Initiating Compare Operation

#### Feature Deployment – Template & Version Control

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
   * From the **Compare Results** page, select **Added** from the Filter dropdown.
   * This option displays only the records that exist in the source but are not present in the destination.
   * If no new records are detected, the system will display **No records found**.
4. **Filter – Modified Records (Screen Compare – 11)**
   * Select **Modified** from the Filter dropdown.
   * This option highlights only the records that have differences between the source and destination environments.
   * Modified records are displayed with changes highlighted for quick identification.
5. **Field Selection (Screen Compare – 12)**
   * Use the **Fields** dropdown to choose a specific field for comparison.
   * Available options include system fields (e.g., Id, IsDeleted, CreatedDate) and business fields (e.g., Name, Description).
   * Selecting a field enables targeted filtering and analysis of record-level changes.
6. **Search Records (Screen Compare – 13)**
   * Enter a specific **Search Value** in combination with the selected field to locate records quickly.
   * For example, searching by **Name** with value `RGC-000025111` will return the corresponding record.
   * This feature ensures faster navigation when working with large datasets.
7. **Show Only Modified Columns (Screen Compare – 14)**
   * Toggle the **Show only modified columns** option to simplify the comparison view.
   * When enabled, the display is restricted to columns that contain differences.
   * This helps reduce noise and focus on changes between environments.
8. **Column Selection (Screen Compare – 15)**
   * Use the **Columns** dropdown to customize which fields are displayed in the comparison results.
   * Specific fields can be checked or unchecked to include or exclude them from the grid.
   * This provides flexibility to tailor the view according to analysis needs.
9. **Download Compare Results (Screen Compare – 16)**
   * Select the **Download** icon to export comparison results.
   * Options include downloading either **Records displayed on the page** or **All Records**.
   * Exported results allow further review or archival outside the system.
10. **Save Actions (Screen Compare – 17)**
    * After reviewing comparison results, choose one of the available save actions:
      * **Save and continue**: Retains progress and allows further configuration before deployment.
      * **Save and deploy**: Finalizes and directly deploys the compared records to the target environment.
      * These options provide flexibility between staged review and immediate deployment.











































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
