# nCino Compare

## Introduction

Compare and selective deployment functionality allows you to perform compare operations on different datasets and from various objects across the orgs and promote the selected/required records to further environments.

## Overview

1. Compare functionality enables you to perform the org-to-org comparison and org to Version Control comparison.
2. You can perform the relational compare operation on the initial dataset retrieved from the initial compare operation performed.
3. At each level of the compare operation, you can perform the individual selection of the records retrieved from both the initial compare and the relational comparison operations.
4. The records selected at different levels of the compare operation can be saved and you can continue with further selection.
5. Once finished with record selection, you can continue with the deployment by clicking on **“Save and Deploy.”**
6. On the object summary screen, you can review the records selected on the compare screen(s) and continue with RBC deployments.

## Step-by-Step Guide

### Initiating Compare Operations

#### Feature Deployment – Template + Version Control

<figure><img src="../../../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

1. On selecting “Template” or “Version Control,” you will see the “Retrieve Dataset” option.
2. Clicking “Retrieve Dataset” will take you to the “Deployment History” page.
3. From the “Deployment History” page for the current deployment, you will see the “View Dataset” option. Clicking on this will open the dataset.

#### Feature Deployment – Template/VC Using Salesforce Org

1. Select “Template Using Salesforce Org/VC Using Salesforce Org” to see “Create Dataset” visible.
2. Click on the “Create Dataset” option to continue performing the ‘compare’ operation after you are taken to the “Deployment History” page.

<figure><img src="../../../../.gitbook/assets/image (1) (5).png" alt=""><figcaption></figcaption></figure>

### Perform Compare

1. Open the deployment, then click on the “Compare” button.

<figure><img src="../../../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

2. Once you click on “Compare,” a pop-up will be shown.
3. The compare operation can be performed either as “Org to Org” or “Version Control.”

#### Org-to-Org Comparison

Select the ‘Salesforce Org’ radio button to perform an Org-to-Org comparison.

<figure><img src="../../../../.gitbook/assets/image (3) (4).png" alt=""><figcaption></figcaption></figure>

#### Org-to-VC Comparison

Select the ‘Version Control’ radio button to perform the Org-to-VC comparison.

<figure><img src="../../../../.gitbook/assets/image (4) (4).png" alt=""><figcaption></figcaption></figure>

### Compare Results

1. Perform either the Org-to-Org or Org-to-VC compare operation.

<figure><img src="../../../../.gitbook/assets/image (5) (4).png" alt=""><figcaption></figcaption></figure>

2. On this screen, you can alter the destination as required.
3. You can select from the following fields on the compare screen:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare
4. Upon completing the required selections, click on the “Compare” button on the pop-up.
5. You can see the results on the “Compare Results” screen.

<figure><img src="../../../../.gitbook/assets/image (6) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (7) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (8) (4).png" alt=""><figcaption></figcaption></figure>

6. **Object:** Users can select one object at a time for comparison against the destination.
7. **Unique ID:** User can select one Unique ID at a time from the dropdown.
8. **Exclude From Compare:** This multi selection checkbox allows users to select fields to be excluded from the comparison.

{% hint style="info" %}
**Note:** You can perform the “Compare” operation to see each time there is a change in the object for the respective selections.
{% endhint %}

9. **Select**: Through this dropdown, you can select either of the options “Select the Current Page Records” or “Select All Records.”
10. You can search through the data from the compare operation using the:
    * **Search By Field**: User can select the field to search.
    * **Value**: User must enter the value to search for.

{% hint style="info" %}
**Note:** Select View Records, LLC\_BI\_lookupKey\_c and Name would be the default fields on the screen that you can see.
{% endhint %}

11. You will see the first 10 fields from the compare result set retrieved from the compare operation in the table view under **“Compare Results.”**
12. **Excluded From Compare:** Users can open the link and verify the fields excluded from the compare.
13. **Export:** The compare results can be exported to Excel through either of these options:

    * **Records on the page:** This will export the records on the current page to Excel.
    * **All Records:** This will export all the records retrieved from the compare operation.

    <figure><img src="../../../../.gitbook/assets/image (9) (4).png" alt=""><figcaption></figcaption></figure>
14. **Change View:** You can click open the link and add/remove the fields to be displayed in the compare results grid.

    * Only 10 fields can be displayed on the grid at a time.

    <figure><img src="../../../../.gitbook/assets/image (10) (4).png" alt=""><figcaption></figcaption></figure>
15. **Save and Continue:** Click on ‘OK’ to continue with the selection for “selective deployment.”
16. **Save and Deploy:** Click on ‘OK’ to continue with the deployment(s). You will be taken to the deployment page with the selected records displayed.

{% hint style="info" %}
**Note:** Count of the selected records can be seen on the **“Object Summary”** screen, while being redirected to the deployment page.
{% endhint %}

17. Upon clicking **“Save and Deploy,”** you can see the object summary of all the records selected.

<figure><img src="../../../../.gitbook/assets/image (11) (4).png" alt=""><figcaption></figcaption></figure>

18. Once you click on the **“Save and Deploy”** button, you will be redirected to the deployment page with the **“Iteration – Staging”** designation.

<figure><img src="../../../../.gitbook/assets/image (12) (4).png" alt=""><figcaption></figcaption></figure>

19. Clicking on the total under **“Selected Records”** will show you the record(s) in a pop-up.

<figure><img src="../../../../.gitbook/assets/image (13) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (14) (4).png" alt=""><figcaption></figcaption></figure>

20. Click on **“Deploy”** to perform the deployment of the selected records.
21. On successful deployment, the iteration will be changed to “1” and users can see **Success** and **Failure** records.

<figure><img src="../../../../.gitbook/assets/image (15) (4).png" alt=""><figcaption></figcaption></figure>

22. You can see the “Success” and “Failure” results of the deployments.

### Relational Compare - Global & Record-Level

#### Global Relational Compare

This will compare the selected object with the object in the destination and identify and highlight the related parent and child records.

1.  Clicking on the relational compare icon beside the column **“Related Records”** will display a pop-up.

    * This will perform a global-level relational compare operation on all the records that are retrieved as part of the initial compare operation.

    <figure><img src="../../../../.gitbook/assets/image (16) (4).png" alt=""><figcaption></figcaption></figure>
2. **You can make a selection on parent and child sections:**
   * **Object:** Select the required items from the list of objects for comparison
   * **Unique ID:** Select the unique ID from the list.
   * **Exclude From Compare:** Select the records to be excluded from the compare operation.
3. Click on the **Compare** icon to initiate the compare operation.
4. On completing the comparison, the identified records will be highlighted.

#### Record-Level Relational Compare

1. Click on the record-level relational compare icon to perform the relational compare operation.

<figure><img src="../../../../.gitbook/assets/image (17) (4).png" alt=""><figcaption></figcaption></figure>

2. **You can make the respective selection(s) on parent and child sections:**
   * **Object:** Select the required object from the list of objects for comparison
   * **Unique ID:** Select the unique id from the available list.
   * **Exclude From Compare:** Select the records to be excluded from the compare operation.
   * Click on the compare icon to initiate the compare operation
   *   Upon completing the compare operation, you will be taken to the “Level 1” relational compare results page.

       * You can continue to perform the relational compare operation to the ‘nth’ level or indefinitely.

       <figure><img src="../../../../.gitbook/assets/image (18) (4).png" alt=""><figcaption></figcaption></figure>
3. **View Records:** You can see the details of the _**record on which the record-level comparison is performed**_.
4. You can both collapse and expand the “Relational Parent” and “Relational Child” sections, as observed above.
   * The “Relational Parent” and “Relational Child” sections are collapsed for the convenience of viewing.
5. As shown below, you can perform the relational comparison at different levels.

<figure><img src="../../../../.gitbook/assets/image (19) (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (20) (4).png" alt=""><figcaption></figcaption></figure>

6. You can perform the **‘Global Relational Compare’** and the **‘Record-Level Comparison’** at these levels too, as displayed in the following screenshot.
7. You can continue to select from the set of records that are extracted from the compare operation.
8. Upon concluding the records selection, you can either:
   * **Save and Continue**: Save the initial record selections and continue to select additional records or perform relational compare operations.
   * **Save and Deploy**: You can continue to save and deploy the records. On selecting this, you will be taken to the deployment page, where the selected records can be deployed to further environments.
9. You can see the “Object Summary” for reviewing the selected records.
10. By clicking on the total displayed under **“Selected Records,”** you can see the records in a pop-up.
11. Once you click on the “Save and Deploy” button, you will be redirected to the deployment page with the **“Iteration – Staging.”**
12. Click on **“Deploy”** to perform the deployment of the selected records.
13. Upon successful deployment of the records, the iteration will be changed to “1” and you can see Success and Failed records.
14. You can see the **“Success”** & **“Failed”** counts of the deployed records on the above screen.
