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

![](../../../../.gitbook/assets/0.png)

1. On selecting “Template” or “Version Control,” you will see the “Retrieve Dataset” option.
2. Clicking “Retrieve Dataset” will take you to the “Deployment History” page.
3. From the “Deployment History” page for the current deployment, you will see the “View Dataset” option. Clicking on this will open the dataset.

#### Feature Deployment – Template/VC Using Salesforce Org

1. Select “Template Using Salesforce Org/VC Using Salesforce Org” to see “Create Dataset” visible.
2. Click on the “Create Dataset” option to continue performing the ‘compare’ operation after you are taken to the “Deployment History” page.

![](../../../../.gitbook/assets/1.png)

### Perform Compare

1. Open the deployment, then click on the “Compare” button.

![](../../../../.gitbook/assets/2.png)

2. Once you click on “Compare,” a pop-up will be shown.
3. The compare operation can be performed either as “Org to Org” or “Version Control.”

#### Org-to-Org Comparison

Select the ‘Salesforce Org’ radio button to perform an Org-to-Org comparison.

![](../../../../.gitbook/assets/3.png)

#### Org-to-VC Comparison

Select the ‘Version Control’ radio button to perform the Org-to-VC comparison.

![](../../../../.gitbook/assets/4.png)

### Compare Results

1. Perform either the Org-to-Org or Org-to-VC compare operation.

![](../../../../.gitbook/assets/5.png)

2. On this screen, you can alter the destination as required.
3. You can select from the following fields on the compare screen:
   * Destination
   * Feature Name
   * Object
   * Unique ID
   * Exclude From Compare
4. Upon completing the required selections, click on the “Compare” button on the pop-up.
5. You can see the results on the “Compare Results” screen.

![](../../../../.gitbook/assets/6.png)

![](../../../../.gitbook/assets/7.png)

![](../../../../.gitbook/assets/8.png)

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

![](../../../../.gitbook/assets/9.png)

14. **Change View:** You can click open the link and add/remove the fields to be displayed in the compare results grid.
    * Only 10 fields can be displayed on the grid at a time.

![](../../../../.gitbook/assets/10.png)

15. **Save and Continue:** Click on ‘OK’ to continue with the selection for “selective deployment.”
16. **Save and Deploy:** Click on ‘OK’ to continue with the deployment(s). You will be taken to the deployment page with the selected records displayed.

{% hint style="info" %}
**Note:** Count of the selected records can be seen on the **“Object Summary”** screen, while being redirected to the deployment page.
{% endhint %}

17. Upon clicking **“Save and Deploy,”** you can see the object summary of all the records selected.

![](../../../../.gitbook/assets/11.png)

1. Once you click on the **“Save and Deploy”** button, you will be redirected to the deployment page with the **“Iteration – Staging”** designation.

![](../../../../.gitbook/assets/12.png)

2. Clicking on the total under **“Selected Records”** will show you the record(s) in a pop-up.

![](../../../../.gitbook/assets/13.png)

![](../../../../.gitbook/assets/14.png)

3. Click on **“Deploy”** to perform the deployment of the selected records.
4. On successful deployment, the iteration will be changed to “1” and users can see **Success** and **Failure** records.

![](../../../../.gitbook/assets/15.png)

5. You can see the “Success” and “Failure” results of the deployments.

### Relational Compare - Global & Record-Level

#### Global Relational Compare

This will compare the selected object with the object in the destination and identify and highlight the related parent and child records.

1. Clicking on the relational compare icon beside the column **“Related Records”** will display a pop-up.
   * This will perform a global-level relational compare operation on all the records that are retrieved as part of the initial compare operation.

![](../../../../.gitbook/assets/16.png)

2. **You can make selection on parent and child sections:**
   * **Object:** Select the required items from the list of objects for comparison
   * **Unique ID:** Select the unique ID from the list.
   * **Exclude From Compare:** Select the records to be excluded from the compare operation.
3. Click on the **Compare** icon to initiate the compare operation.
4. On completing the comparison, the identified records will be highlighted.

#### Record-Level Relational Compare

1. Click on the record-level relational compare icon to perform the relational compare operation.

![](../../../../.gitbook/assets/17.png)

2. **You can make the respective selection(s) on parent and child sections:**
   * **Object:** Select the required object from the list of objects for comparison
   * **Unique ID:** Select the unique id from the available list.
   * **Exclude From Compare:** Select the records to be excluded from the compare operation.
   * Click on the compare icon to initiate the compare operation
   * Upon completing the compare operation, you will be taken to the “Level 1” relational compare results page.
     * You can continue to perform the relational compare operation to the ‘nth’ level or indefinitely.

![](../../../../.gitbook/assets/18.png)

3. **View Records:** You can see the details of the _**record on which the record-level comparison is performed**_.
4. You can both collapse and expand the “Relational Parent” and “Relational Child” sections, as observed above.
   * The “Relational Parent” and “Relational Child” sections are collapsed for the convenience of viewing.
5. As shown below, you can perform the relational compare at different levels.

![](../../../../.gitbook/assets/19.png)

![](../../../../.gitbook/assets/20.png)

6. You can perform the **‘Global Relational Compare’** and the **‘Record-Level Comparison’** at these levels too, as displayed in the following screenshot.
7. You can continue to select from the set of records that are extracted from the compare operation.
8. Upon concluding the records selection, you can either:
   * **Save and Continue**: Save the initial record selections and can continue with the further selection of records or performing relational compare operations.
   * **Save and Deploy**: You can continue to save and deploy the records. On selecting this, you will be taken to the deployment page, where the selected records can be deployed to further environments.
9. You can see the “Object Summary” for reviewing the selected records.
10. By clicking on the total displayed under the **“Selected Records”**, you can see the records in a pop-up.
11. Once you click on the “Save and Deploy” button, you will be redirected to the deployment page with the **“Iteration – Staging.”**
12. Click on **“Deploy”** to perform the deployment of the selected records.
13. On successful deployment of the records, the iteration will be changed to “1” and you can see Success and Failed records.
14. You can see the **“Success”** & **“Failed”** counts of the deployed records on the above screen.
