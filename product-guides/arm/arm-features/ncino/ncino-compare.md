# nCino Compare

## Introduction

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

<figure>
    <img src="../../../../.gitbook/assets/image (1503).png" alt="Retrieve Dataset option from Template or Version Control">
    <figcaption>Retrieve Dataset option from Template or Version Control</figcaption>
</figure>

1. Select “Template” or “Version Control” to reveal the **Retrieve Dataset** option.
2. Clicking it redirects to the **Deployment History** page.
3. On that page, use **View Dataset** to open the dataset.

#### Feature Deployment – Using Salesforce Org

1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2. Click **Create Dataset** to start a comparison.

<figure>
    <img src="../../../../.gitbook/assets/image (1504).png" alt="Create Dataset option using Salesforce Org" width="375">
    <figcaption>Create Dataset option using Salesforce Org</figcaption>
</figure>

### Perform Compare

1. Open the deployment and click **Compare**.

<figure>
    <img src="../../../../.gitbook/assets/image (1505).png" alt="Compare button inside deployment view" width="375">
    <figcaption>Compare button inside deployment view</figcaption>
</figure>

2. Choose the type of comparison:
   - **Org-to-Org** (select **Salesforce Org**)
   - **Org-to-VC** (select **Version Control**)

<figure>
    <img src="../../../../.gitbook/assets/image (1506).png" alt="Org-to-Org comparison selection" width="375">
    <figcaption>Org-to-Org comparison selection</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1507).png" alt="Org-to-VC comparison selection" width="375">
    <figcaption>Org-to-VC comparison selection</figcaption>
</figure>

### Compare Results

1. View differences highlighted in yellow (for changed destination values).
2. Configure comparison using:
   - Destination
   - Feature Name
   - Object
   - Unique ID
   - Exclude From Compare

<figure>
    <img src="../../../../.gitbook/assets/image (1508).png" alt="Comparison fields and options" width="375">
    <figcaption>Comparison fields and options</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1509).png" alt="Compare results with yellow highlights" width="375">
    <figcaption>Compare results with yellow highlights</figcaption>
</figure>

3. Exclude fields from comparison (shown in light gray).
4. Use **Select** to choose current page or all records.
5. Use **Search by Field** to filter results.

<figure>
    <img src="../../../../.gitbook/assets/image (1513).png" alt="Export and field selection options" width="375">
    <figcaption>Export and field selection options</figcaption>
</figure>

6. **Change View** to select which fields to show (max 25).

<figure>
    <img src="../../../../.gitbook/assets/image (1514).png" alt="Change view to customize field display" width="375">
    <figcaption>Change view to customize field display</figcaption>
</figure>

7. Click **View Record** to compare source vs destination values.

<figure>
    <img src="../../../../.gitbook/assets/image (1515).png" alt="View Record button for detailed comparison" width="375">
    <figcaption>View Record button for detailed comparison</figcaption>
</figure>

8. Use **Save and Continue** or **Save and Deploy** to proceed.

> **Note:** Record counts are shown on the Object Summary screen before deployment.

<figure>
    <img src="../../../../.gitbook/assets/image (1516).png" alt="Object Summary screen after Save and Deploy" width="375">
    <figcaption>Object Summary screen after Save and Deploy</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1517).png" alt="Iteration staging page before deployment" width="375">
    <figcaption>Iteration staging page before deployment</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1518).png" alt="Popup showing selected records" width="375">
    <figcaption>Popup showing selected records</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1519).png" alt="Deploy confirmation screen" width="375">
    <figcaption>Deploy confirmation screen</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1520).png" alt="Success and failure record summary" width="375">
    <figcaption>Success and failure record summary</figcaption>
</figure>

---

## Relational Compare - Global & Record-Level

### Global Relational Compare

Performs a full compare to identify parent/child records related to selected objects.

<figure>
    <img src="../../../../.gitbook/assets/image (1521).png" alt="Relational compare initiation for related records" width="375">
    <figcaption>Relational compare initiation for related records</figcaption>
</figure>

1. Choose parent/child object and Unique ID.
2. Select fields to exclude and click **Compare**.

### Record-Level Relational Compare

Compares one record at a time and lets you drill down further.

<figure>
    <img src="../../../../.gitbook/assets/image (1522).png" alt="Record-level relational compare icon" width="375">
    <figcaption>Record-level relational compare icon</figcaption>
</figure>

- Supports multiple levels of nested comparison:
  - Level 1, 2, 3, etc.

<figure>
    <img src="../../../../.gitbook/assets/image (1524).png" alt="Record-level comparison level 1" width="375">
    <figcaption>Record-level comparison level 1</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1525).png" alt="Record-level comparison level 2" width="375">
    <figcaption>Record-level comparison level 2</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1526).png" alt="Record-level with nested relational compare" width="375">
    <figcaption>Record-level with nested relational compare</figcaption>
</figure>

- Continue record selection:

<figure>
    <img src="../../../../.gitbook/assets/image (1528).png" alt="Record selection after relational comparison" width="375">
    <figcaption>Record selection after relational comparison</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1529).png" alt="Parent and child record listing" width="375">
    <figcaption>Parent and child record listing</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1530).png" alt="Additional relational records selected" width="375">
    <figcaption>Additional relational records selected</figcaption>
</figure>

- Choose:
  - **Save and Continue** – Save and proceed.
  - **Save and Deploy** – Go to deployment screen.

<figure>
    <img src="../../../../.gitbook/assets/image (1531).png" alt="Object Summary screen before final deployment" width="375">
    <figcaption>Object Summary screen before final deployment</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1532).png" alt="Selected records visible for deployment" width="375">
    <figcaption>Selected records visible for deployment</figcaption>
</figure>

- View selected records:

<figure>
    <img src="../../../../.gitbook/assets/image (1533).png" alt="Popup of selected records before deployment" width="375">
    <figcaption>Popup of selected records before deployment</figcaption>
</figure>

- After deployment:

<figure>
    <img src="../../../../.gitbook/assets/image (1534).png" alt="Deployment staging confirmation" width="375">
    <figcaption>Deployment staging confirmation</figcaption>
</figure>

<figure>
    <img src="../../../../.gitbook/assets/image (1535).png" alt="Final deployment result with status" width="375">
    <figcaption>Final deployment result with status</figcaption>
</figure>
