# nCino Compare

## Introduction

Compare and selective deployment functionality allows you to perform compare operations on different datasets and from various objects across the Orgs and promote the selected/required records to further environments.

## Overview

1. Compare functionality enables you to perform the Org-to-Org comparison and Org-to-VC comparison.
2. You can perform the relational compare operation on the initial dataset retrieved from the initial compare operation performed.
3. At each level of the compare operation, you can perform the individual selection of the records retrieved from both the initial compare and the relational comparison operation.
4. The records selected at different levels of the compare operation can be saved and you can continue with further selection.
5. Once you are done with record selection, you can continue with the deployment by clicking on the “Save and Deploy” button.
6. On the object summary screen, you can review the records selected on the compare screen(s) and continue with RBC deployments.

## Step-by-Step Guide

### Initiating Compare Operation

#### Feature Deployment – Template & Version Control

&#x20;<img src="../../../../.gitbook/assets/image (1503).png" alt="" data-size="original">

1. On selecting the “Template” OR “Version Control”, you will see the “Retrieve Dataset” option.
2. On clicking the “Retrieve Dataset” option, you will land on the “Deployment History” page.
3. On “Deployment History” page, for the deployment being done, you will have the “View Dataset” option. Clicking on this option, will open the dataset.

### Feature Deployment – Template/VC Using Salesforce ORG

1. Select “Template Using Salesforce Org/VC Using Salesforce Org” to see “Create Dataset” visible.
2. Click on the “Create Dataset” option to continue performing the ‘compare’ operation after you are taken to the “Deployment History” page.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1504).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

### Perform Compare

1. Open the deployment, then click on the “Compare” button..

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1505).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

2. Once you click on “Compare,” a pop-up will be shown.
3. The compare operation can be performed as either “Org to Org” or “Version Control.”

#### Org-to-Org Comparison

Select the ‘Salesforce Org’ radio button to perform an Org-to-Org comparison.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1506).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

#### Org-to-VC Comparison

Select the ‘Version Control’ radio button to perform the Org-to-VC comparison.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1507).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

### Compare Results

1. Perform either the Org-to-Org or Org-to-VC compare operation.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1508).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

2. On this screen, you can alter the destination as required.
3. You can select from the following fields on the compare screen:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare                                                           &#x20;
4. Upon completing the required selections, click on the “Compare” button on the pop-up.
5. You can see the results on the “Compare Results” screen.
6. Across the compare results screen, the differences between ORGs, which are otherwise called as changes are highlighted in yellow on the “destination ORG value”.
   * Differences in record values are highlighted at the relational compare level as well. &#x20;

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1509).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1510).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1511).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

7. Object: You can select one object at a time for comparison against the destination.
8. Unique ID: You   can select one Unique ID at a time from the drop-down.
9. Exclude From Compare: This multi select checkbox allows the users to select the required fields to be excluded from the comparison.

Note: _The user can perform “Compare” operation each time, for change in the object, and for the respective selections._

{% hint style="info" %}
Note: _Users can perform “Compare” operations each time a change in the object occurs and for the respective selections._
{% endhint %}

* Fields excluded from compare are represented in a light gray color on the grid. Observe the following screenshot for reference.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1512).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

10. Select: Through this dropdown, you can select either of the options “Select the Current Page Records” or “Select All Records”.
11. You can search through the data from the compare operation using the:
    * Search By Field: User can select the field to search.
    * Value: User must enter the value to search for.

NOTE: - The columns Select, View Records, LLC\_BI\_lookupKey\_c and Name would be the default fields on the grid.

12. The first 25 fields from the compare result set retrieved from the compare operation are shown in the table view under “Compare Results.”
13. Excluded From Compare: Users can open the link and verify the fields excluded from the compare.
14. Export: The compare results can be exported to Excel through either of these options:
    * Records on the page: This will export the records on the current page to Excel.
    * All Records: This will export all the records retrieved from the compare operation.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1513).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

15. Change View: You can click open the ‘Change View’ link and add/remove the fields to be displayed on the compare results grid.
    * Only 25 fields are displayed on the grid at any given point of time.
    * Fields excluded from compare are highlighted in a gray hue on the change view screen.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1514).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

16. View Record: Is useful for viewing the entire record from source and destination at one place.
    * Click on the “View Record” icon highlighted below to view the record value from both source and destination.
    * Click on the “View Record” icon to view the pop-up with record details from ‘Source & Destination’.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1515).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

17. Save And Continue: You can click on this to perform the “selective deployment”.
18. Save And Deploy: Click on ‘OK’ to continue with the deployment(s). You will be taken to the deployment page with the selected records displayed.

<mark style="background-color:blue;">**NOTE**</mark><mark style="background-color:blue;">: A count of the selected records is shown on the “Object Summary” screen, while the user is being redirected to the deployment page.</mark>

19. On Clicking “Save and Deploy,” you can view the object summary of all the records selected.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1516).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

20. &#x20;Once the user clicks on the “Save and Deploy” button, you will be redirected to the deployment page with the “Iteration – Staging”.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1517).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

21. Clicking on the total under “Selected Records” will show you the record(s) in a pop-up.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1518).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1519).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

22. Click on “Deploy” to perform the deployment of the selected records.
23. On successful deployment, the iteration will be changed to “1” and users can see Success and Failure records.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1520).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

24. &#x20;You can see the “Success” and “Failure” results of the deployments.

### Relational Compare - Global & Record-Level

**Global Relational Compare**

This will compare the selected object with the object in the destination and identify and highlight the related parent and child records.

1. Clicking on the relational compare icon beside the column “Related Records” will display a pop-up.
   * This will perform a global-level relational compare operation on all the records that are retrieved as part of the initial compare operation.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1521).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

2. You can make a selection on parent and child sections:
   * Object: Select the required items from the list of objects for comparison
   * Unique ID: Select the unique ID from the list.
3. Exclude From Compare: Select the records to be excluded from the compare operation.
4. Click on the Compare icon to initiate the compare operation.
5. On completing the comparison, the identified records will be highlighted.

**Record-Level Relational Compare:**

1. Click on the record-level relational compare icon to perform the relational compare operation.

<div align="left">

<figure><img src="../../../../.gitbook/assets/image (1522).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

2. You can make the respective selection(s) on parent and child sections:
   * Object: Select the required object from the list of objects for comparison
   * Unique ID: Select the unique id from the available list.
   * Exclude From Compare: Select the records to be excluded from the compare operation.
   * Click on the compare icon to initiate the compare operation
   * Upon completing the compare operation, you will be taken to the “Level 1” relational compare results page.
     * You can continue to perform the relational compare operation to the ‘nth’ level or indefinitely.
3. View Records: You can see the details of the record on which the record-level comparison is performed.
4. You can both collapse and expand the “Relational Parent” and “Relational Child” sections, as observed above.
   1. The “Relational Parent” and “Relational Child” sections are collapsed for the convenience of viewing.
5. As shown below, you can perform the relational comparison at different levels.\
   ![](<../../../../.gitbook/assets/image (1524).png>)\
   \
   ![](<../../../../.gitbook/assets/image (1525).png>)
6. You can perform the ‘Global Relational Compare’ and the ‘Record Level Comparison’ at these levels too, as displayed in the below screenshot.\
   ![](<../../../../.gitbook/assets/image (1526).png>)
7. You can continue to select from the set of records that are extracted from the compare operation.\
   ![](<../../../../.gitbook/assets/image (1528).png>)\
   \
   ![](<../../../../.gitbook/assets/image (1529).png>)\
   \
   ![](<../../../../.gitbook/assets/image (1530).png>)
8. On concluding the records selection, the user can either,
   * Save and Continue: Save the initial record selections and continue to select other records to perform relational compare operations.
   * Save and Deploy: Saves the current selection of records and navigate you to the deployment page, where the selected records can be deployed to further environments.
9. Please observe the “Object Summary” for reviewing the selected records.\
   ![](<../../../../.gitbook/assets/image (1531).png>)\
   \
   ![](<../../../../.gitbook/assets/image (1532).png>)
10. By clicking on the total displayed under the “Selected Records”, you can view the records in a pop-up.\
    ![](<../../../../.gitbook/assets/image (1533).png>)
11. Once the user clicks on the “Save and Deploy” button, you will be redirected to the deployment page with the “Iteration – Staging.”\
    ![](<../../../../.gitbook/assets/image (1534).png>)
12. Click on the “Deploy” button to perform the deployment of the selected records.
13. On successful deployment of the records, the Iteration will be changed to “1” and you can observe success and failed records.\
    ![](<../../../../.gitbook/assets/image (1535).png>)
14. Once the deployment is done, you can observe the “Success” & “Failed” counts of the deployed records on the above screen.

***
