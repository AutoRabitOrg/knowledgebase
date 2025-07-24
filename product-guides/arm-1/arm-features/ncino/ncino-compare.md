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





































Introduction

The compare and selective deployment functionality allows you to perform comparisons across datasets and objects between different Salesforce orgs or version control repositories. You can then promote selected records to target environments.

## Overview

1. Perform Org-to-Org or Org-to-Version Control (VC) comparisons.
2. Run relational comparisons on initial datasets.
3. Select individual records at any comparison level.
4. Save selections and continue comparing or proceed to deployment.
5. Finalize deployment using the **Save and Deploy** option.
6. Review selected records on the Object Summary screen and initiate RBC deployments.

## Step-by-Step Guide

### Initiating Compare Operation

#### Feature Deployment – Template & Version Control

<figure><img src="../../../../.gitbook/assets/image (1503).png" alt="Retrieve Dataset option from Template or Version Control"><figcaption><p>Retrieve Dataset option from Template or Version Control</p></figcaption></figure>

1. Select “Template” or “Version Control” to reveal the **Retrieve Dataset** option.
2. Clicking it redirects to the **Deployment History** page.
3. On that page, use **View Dataset** to open the dataset.

#### Feature Deployment – Using Salesforce Org

1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2. Click **Create Dataset** to start a comparison.

<figure><img src="../../../../.gitbook/assets/image (1504).png" alt="Create Dataset option using Salesforce Org" width="375"><figcaption><p>Create Dataset option using Salesforce Org</p></figcaption></figure>

### Perform Compare

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
