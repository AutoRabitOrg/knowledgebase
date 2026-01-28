# Compare nCino Environments

## nCino Compare

### Introduction

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

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1503).png" alt=""><figcaption></figcaption></figure>

Retrieve Dataset option from Template or Version Control

1. Select “Template” or “Version Control” to reveal the **Retrieve Dataset** option.
2. Clicking it redirects to the **Deployment History** page.
3. On that page, use **View Dataset** to open the dataset.

**Feature Deployment – Using Salesforce Org**



1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2. Click **Create Dataset** to start a comparison.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1504).png" alt=""><figcaption></figcaption></figure>

Create Dataset option using Salesforce Org

#### Perform Compare



1. Open the deployment and click **Compare**.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1505).png" alt=""><figcaption></figcaption></figure>

Compare button inside deployment view

2. Choose the type of comparison:
   * **Org-to-Org** (select **Salesforce Org**)
   * **Org-to-VC** (select **Version Control**)

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1506).png" alt=""><figcaption></figcaption></figure>

Org-to-Org comparison selection

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1507).png" alt=""><figcaption></figcaption></figure>

Org-to-VC comparison selection

#### Compare Results



1. View differences highlighted in yellow (for changed destination values).
2. Configure comparison using:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1508).png" alt=""><figcaption></figcaption></figure>

Comparison fields and options

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1509).png" alt=""><figcaption></figcaption></figure>

Compare results with yellow highlights

3. Exclude fields from comparison (shown in light gray).
4. Use **Select** to choose current page or all records.
5. Use **Search by Field** to filter results.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1513).png" alt=""><figcaption></figcaption></figure>

Export and field selection options

6. **Change View** to select which fields to show (max 25).

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1514).png" alt=""><figcaption></figcaption></figure>

Change view to customize field display

7. Click **View Record** to compare source vs destination values.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1515).png" alt=""><figcaption></figcaption></figure>

View Record button for detailed comparison

8. Use **Save and Continue** or **Save and Deploy** to proceed.

> **Note:** Record counts are shown on the Object Summary screen before deployment.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1516).png" alt=""><figcaption></figcaption></figure>

Object Summary screen after Save and Deploy

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1517).png" alt=""><figcaption></figcaption></figure>

Iteration staging page before deployment

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1518).png" alt=""><figcaption></figcaption></figure>

Popup showing selected records

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1519).png" alt=""><figcaption></figcaption></figure>

Deploy confirmation screen

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1520).png" alt=""><figcaption></figcaption></figure>

Success and failure record summary

***

### Relational Compare - Global & Record-Level



#### Global Relational Compare



Performs a full compare to identify parent/child records related to selected objects.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1521).png" alt=""><figcaption></figcaption></figure>

Relational compare initiation for related records

1. Choose parent/child object and Unique ID.
2. Select fields to exclude and click **Compare**.

#### Record-Level Relational Compare



Compares one record at a time and lets you drill down further.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1522).png" alt=""><figcaption></figcaption></figure>

Record-level relational compare icon

* Supports multiple levels of nested comparison:
  * Level 1, 2, 3, etc.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1524).png" alt=""><figcaption></figcaption></figure>

Record-level comparison level 1

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1525).png" alt=""><figcaption></figcaption></figure>

Record-level comparison level 2

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1526).png" alt=""><figcaption></figcaption></figure>

Record-level with nested relational compare

* Continue record selection:

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1528).png" alt=""><figcaption></figcaption></figure>

Record selection after relational comparison

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1529).png" alt=""><figcaption></figcaption></figure>

Parent and child record listing

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1530).png" alt=""><figcaption></figcaption></figure>

Additional relational records selected

* Choose:
  * **Save and Continue** – Save and proceed.
  * **Save and Deploy** – Go to deployment screen.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1531).png" alt=""><figcaption></figcaption></figure>

Object Summary screen before final deployment

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1532).png" alt=""><figcaption></figcaption></figure>

Selected records visible for deployment

* View selected records:

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1533).png" alt=""><figcaption></figcaption></figure>

Popup of selected records before deployment

* After deployment:

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1534).png" alt=""><figcaption></figcaption></figure>

Deployment staging confirmation

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(1535).png" alt=""><figcaption></figcaption></figure>

Final deployment result with status
