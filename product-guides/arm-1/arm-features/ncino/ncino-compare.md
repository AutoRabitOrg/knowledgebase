# Compare nCino Environments

## nCino Compare

**Introduction**

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

### Step-by-Step Guide

#### Initiating Compare Operation

Introduction

The compare and selective deployment functionality allows you to perform comparisons across datasets and objects between different Salesforce orgs or version control repositories. You can then promote selected records to target environments.

### Overview

1. Perform Org-to-Org or Org-to-Version Control (VC) comparisons.
2. Run relational comparisons on initial datasets.
3. Select individual records at any comparison level.
4. Save selections and continue comparing or proceed to deployment.
5. Finalize deployment using the **Save and Deploy** option.
6. Review selected records on the Object Summary screen and initiate RBC deployments.

### Step-by-Step Guide

#### Initiating Compare Operation

**Feature Deployment – Template & Version Control**

1. Select “Template” or “Version Control” to reveal the **Retrieve Dataset** option.
2. Clicking it redirects to the **Deployment History** page.
3. On that page, use **View Dataset** to open the dataset.

**Feature Deployment – Using Salesforce Org**

1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2. Click **Create Dataset** to start a comparison.

#### Perform Compare

1. Open the deployment and click **Compare**.
2. Choose the type of comparison:
   * **Org-to-Org** (select **Salesforce Org**)
   * **Org-to-VC** (select **Version Control**)

#### Compare Results

1. View differences highlighted in yellow (for changed destination values).
2. Configure comparison using:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare
3. Exclude fields from comparison (shown in light gray).
4. Use **Select** to choose current page or all records.
5. Use **Search by Field** to filter results.
6. **Change View** to select which fields to show (max 25).
7. Click **View Record** to compare source vs destination values.
8. Use **Save and Continue** or **Save and Deploy** to proceed.

> **Note:** Record counts are shown on the Object Summary screen before deployment.

***

### Relational Compare - Global & Record-Level

#### Global Relational Compare

Performs a full compare to identify parent/child records related to selected objects.

1. Choose parent/child object and Unique ID.
2. Select fields to exclude and click **Compare**.

#### Record-Level Relational Compare

Compares one record at a time and lets you drill down further.

* Supports multiple levels of nested comparison:
  * Level 1, 2, 3, etc.
* Continue record selection:
* Choose:
  * **Save and Continue** – Save and proceed.
  * **Save and Deploy** – Go to deployment screen.
* View selected records:
* After deployment:
