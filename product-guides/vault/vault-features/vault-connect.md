# Vault Connect

## Introduction

This document provides complete information about the new feature Vault Connect, which will enhance the user’s capability to better utilize Vault in viewing archived Salesforce data from an external data source.

## Feature Overview

1. OData protocol is an open and platform-independent protocol that can be integrated with the system of the user’s choice (along with Salesforce) as it exposes REST APIs for consuming and querying data from the underlying archives.
2. External objects support most of the capabilities that standard and custom objects have in Salesforce.
3. No need to install any managed packages or write custom scripts in Salesforce.

## Step-by-Step Guide

**Create Connect Config**

1. Log in to the **Vault** application.

<figure><img src="../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the setup module of the Vault application. Click on the required Org.

<figure><img src="../../../.gitbook/assets/image (351).png" alt="" width="563"><figcaption></figcaption></figure>

3. Click on the **Connect (Beta)** module of the Vault application.
4. &#x20;On landing on the Connect (Beta) tab of the Vault setup, the user will see the following message on the screen:

<figure><img src="../../../.gitbook/assets/image (352).png" alt="" width="563"><figcaption></figcaption></figure>

5. Once the customer reaches out to AutoRABIT support team as specified on the above screen, our technical team will perform due diligence to enable Vault Connect for the customer(s).
6. When Vault Connect is enabled on the application, the user will see the following screen on the Connect (Beta) tab of the Vault Setup module.

<figure><img src="../../../.gitbook/assets/image (353).png" alt="" width="563"><figcaption></figcaption></figure>

7. Click on the **Add Connect Config** button on the application.

<figure><img src="../../../.gitbook/assets/image (354).png" alt="" width="563"><figcaption></figcaption></figure>

8.  A pop-up will be displayed with the following information:

    * How/where to config the external data source;
    * OData URL for configuring the external data source; and
    * What to select when creating Auth. Providers.

    <figure><img src="../../../.gitbook/assets/image (355).png" alt="" width="563"><figcaption></figcaption></figure>
9. Copy the URL from the pop-up shown.&#x20;

{% hint style="info" %}
**Note:** The same URL can be copied from the pop-up and opened by clicking on the information icon available beside the **Add Connect Config** button.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (356).png" alt="" width="563"><figcaption></figcaption></figure>

10. Select the required config from the Archive Config section and click on the **Next** button.

<figure><img src="../../../.gitbook/assets/image (357).png" alt="" width="563"><figcaption></figcaption></figure>

11. On clicking **Next,** you will be redirected to the **Jobs** section.

<figure><img src="../../../.gitbook/assets/image (358).png" alt="" width="563"><figcaption></figcaption></figure>

12. Select the required **Job** and click on Next.
13. On clicking Next, you will be redirected to the **Objects** section.

<figure><img src="../../../.gitbook/assets/image (359).png" alt="" width="563"><figcaption></figcaption></figure>

14. The following operations can be performed:

    * Include/exclude the required objects from the list of objects available.

    <figure><img src="../../../.gitbook/assets/image (360).png" alt="" width="563"><figcaption></figcaption></figure>

    * &#x20;Include/exclude the fields as required from the list of Fields available. Click on the **File** icon from the **Fields** column.

    <figure><img src="../../../.gitbook/assets/image (361).png" alt="" width="563"><figcaption></figcaption></figure>
15. The following pop-up will be displayed, where the user can exclude the fields as required and click on **Apply** field.

<figure><img src="../../../.gitbook/assets/image (362).png" alt="" width="545"><figcaption></figcaption></figure>

16. On clicking Save, you will be prompted to enter the **Name** and **Description** for the config being created.

<figure><img src="../../../.gitbook/assets/image (363).png" alt="" width="563"><figcaption></figcaption></figure>

17. On entering the required details, click on **Save.**
18. On clicking Save, you will be shown a pop-up that says, **“Config has been created/updated successfully,”** and you will be redirected to the **Connect Config Summary**.

<figure><img src="../../../.gitbook/assets/image (364).png" alt="" width="563"><figcaption></figcaption></figure>

19. On the Connect Config Summary, you can view all the configurations created.

#### **View the Archived Data In Salesforce**

1. &#x20;Log in to the Salesforce org for which you want to view the data.
2.  **Create Auth. Providers**

    * Go to → Auth. Providers under setup.
    * Click on the Auth. Providers under setup.

    <figure><img src="../../../.gitbook/assets/image (365).png" alt=""><figcaption></figcaption></figure>
3. Click on **New.**

<figure><img src="../../../.gitbook/assets/image (366).png" alt=""><figcaption></figcaption></figure>

&#x20;4\. Select the **Provider Type – Salesforce.**

<figure><img src="../../../.gitbook/assets/image (367).png" alt=""><figcaption></figcaption></figure>

5. Provide **Name** and **URL Suffix** and click on **Save.**

{% hint style="info" %}
**Note:** Do not change the remaining settings on the layout.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (368).png" alt=""><figcaption></figcaption></figure>

6. On completing the required selections, click on the Save button.&#x20;

#### Create External Data Sources

1. **Go to** → **External Data Sources** under setup.

<figure><img src="../../../.gitbook/assets/image (369).png" alt=""><figcaption></figcaption></figure>

2. Click on **New External Data Sources.**
3. Provide **External Data** **Source**.
   * Provide Name.
   * Type → Salesforce Data: OData 4.0
   * **Identity type** → Named Principal
   * **Authentication Protocol** → OAuth 2.0
   * **Authentication Provider** → On clicking the **LookUp** glass, you can select the **“Auth. Provider”** created earlier.
   * Select the **Authentication Provider.**
   * Click on **Save on the External Data Sources screen.**
   * On **Save**, click the **Validate and Sync.**
   * You will be shown all the objects selected as part of the config creation.
   * On selecting the required objects, the Sync button on Salesforce will be enabled.
   * Select all the objects you want to sync or select which objects’ data you want to view in Salesforce.
   * Click on the **Sync** button.
   * On completion, you can see all the objects selected.
4. **Create Tabs:** Customers can view the archived data under these tabs.
   * **Go to → Tabs** under setup.
   * Click on the **New** button.
5. Under **Objects**, you can see the objects that are part of the Config created with the naming convention **“Object\_\_X”.**



## Sync with Salesforce

**Overview**

This feature enables the user to sync the latest metadata changes on Salesforce with Vault Connect. The user can also view the data in the same structure and the same relationship hierarchies in the connected external objects.

**Step-by-Step Guide:**

1. Log in to the Vault application.
2.  Click on any Org to navigate to Vault – Connect.\


    <figure><img src="../../../.gitbook/assets/image (68) (2).png" alt=""><figcaption></figcaption></figure>
3.  Click on the “Connect” tab to go to the Connect application.\


    <figure><img src="../../../.gitbook/assets/image (2) (1) (2).png" alt=""><figcaption></figcaption></figure>
4. Click on the “**Sync with Salesforce**” button to initiate the sync procedure
   * Please observe the information icon for informational purposes.
5.  On initiating “**Sync with Salesforce,**” the user will go to the “Sync history” page.\


    <figure><img src="../../../.gitbook/assets/image (3) (1) (2).png" alt=""><figcaption></figcaption></figure>
6. This page will provide information on how many times the sync has happened to date.
7.  On clicking “**Sync with Salesforce,**” the following pop-up will be displayed.\


    <figure><img src="../../../.gitbook/assets/image (4) (1) (2).png" alt=""><figcaption></figcaption></figure>
8.  Clicking on “**Confirm**” will redirect the user to the object list page, where the list of objects is shown.\


    <figure><img src="../../../.gitbook/assets/image (5) (1) (2).png" alt=""><figcaption></figcaption></figure>
9.  Click on “View Logs” to display the related logs.\


    <figure><img src="../../../.gitbook/assets/image (6) (1) (2).png" alt=""><figcaption></figcaption></figure>
10. Logs can be downloaded using the "Download" button.
11. Click on any of the objects to open the related pop-up and make the required selections.\


    <figure><img src="../../../.gitbook/assets/image (7) (1) (2).png" alt=""><figcaption></figcaption></figure>
12. Field Label Name: The field label can be updated to a custom name by clicking on the pencil icon provided.
13. Reference to: If a field has a pencil icon beside it, then “Type” for that field will be set to “Reference.”
14. For polymorphic fields, at least one reference has to be selected.

    * For polymorphic fields, a pencil icon will be displayed beside the fields under the “Reference to” column.

    <figure><img src="../../../.gitbook/assets/image (8) (1) (2).png" alt=""><figcaption></figcaption></figure>
15. An error will be displayed under the ‘error’ column if no references were selected under the “Reference to” column.\


    <figure><img src="../../../.gitbook/assets/image (9) (1) (2).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (10) (1) (2).png" alt=""><figcaption></figcaption></figure>
16. On completing the selection(s), click on the “**Sync with Salesforce**” button to continue with the sync procedure.\


    <figure><img src="../../../.gitbook/assets/image (11) (1) (2).png" alt=""><figcaption></figcaption></figure>
17. An information pop-up will be displayed on clicking the “**Sync with Salesforce**” button.\


    <figure><img src="../../../.gitbook/assets/image (12) (1) (2).png" alt=""><figcaption></figcaption></figure>
18. Clicking on “CONFIRM” will display a success message pop-up.\


    <figure><img src="../../../.gitbook/assets/image (13) (1) (2).png" alt=""><figcaption></figcaption></figure>
19. The latest job can be observed as the top entry on the “Sync history” page.\


    <figure><img src="../../../.gitbook/assets/image (14) (1) (2).png" alt=""><figcaption></figcaption></figure>
20. Clicking on the latest job will provide the list of objects from the job.\


    <figure><img src="../../../.gitbook/assets/image (15) (1) (2).png" alt=""><figcaption></figcaption></figure>
21. Hovering over the list of fields under the References column, the list of fields selected under the references will be displayed to the user.\


    <figure><img src="../../../.gitbook/assets/image (16) (1) (2).png" alt=""><figcaption></figcaption></figure>


22. After performing the “**Sync With Salesforce**”, the user has to go to the “External Objects” and select the required object.\


    <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
23. To add the related lists to the page layout of the parent object, the user first has to set the field-level security by going to the field under the object. The permission should be set to 'visible.'
24. The user can only view data to which they have access.

    <figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
25. After setting the permissions to visible, the user should continue to edit the parent object(s) to add related lists to the page layouts.\


    <figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
26. Click edit on the “**Page Layouts.**”\


    <figure><img src="../../../.gitbook/assets/image (3) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
27. On opening the page layouts, the user can view the “Related Lists” on the left side pane as highlighted.

    <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>
28. Click on the related lists and continue to add the required related lists to the layout to view under the related lists section.
29. After completing the required configuration, the user can continue to open the object on which the configuration is done to view the related list items when the parent record is opened.

***

## Global Search: Prerequisites, Limitations, and Troubleshooting

### Prerequisite: Enabling Global Search with Vault Connect <a href="#prerequisite-enabling-global-search-with-vault-connect" id="prerequisite-enabling-global-search-with-vault-connect"></a>

#### **Steps to Enable Global Search** <a href="#steps-to-enable-global-search" id="steps-to-enable-global-search"></a>

1. **Access Setup:**
   * Go to **Setup** in Salesforce.
2. **Search for External Data Sources:**
   * In the Quick Find box, search for **External Data Sources**.
3. **Edit External Data Source:**
   * Select the external data source you created for Vault Connect.
   * Click on **Edit**.
4. **Enable Free-Text Search Expressions:**
   * Enable the checkbox labeled **Use Free-Text Search Expressions**.

By following these steps, you will enable **global search** functionality for **Vault Connect** in Salesforce.



### Limitations of Querying Archived Data via Vault Connect <a href="#limitations-of-querying-archived-data-via-vault-connect" id="limitations-of-querying-archived-data-via-vault-connect"></a>

#### 1. Indexed Fields Only <a href="#id-1.-indexed-fields-only" id="id-1.-indexed-fields-only"></a>

* Search and queries are restricted to indexed fields from the original object in Salesforce.
* **Note**: To determine what is indexed in a Salesforce object, run the following query from the Salesforce developer console:\
  SELECT QualifiedApiName FROM FieldDefinition WHERE EntityDefinition.QualifiedApiName =\<Salesforce object Name> and IsIndexed = true

#### 2. Complete Value Searches <a href="#id-2.-complete-value-searches" id="id-2.-complete-value-searches"></a>

* Only complete value searches or queries using the equals (=) operator will work on indexed fields.

#### 3. Non-Indexed Fields <a href="#id-3.-non-indexed-fields" id="id-3.-non-indexed-fields"></a>

* Queries or Salesforce functionalities that require a query on non-indexed fields may or may not work.
* **Impact**: As the size of your archived data increases, these queries are more likely to result in timeouts.

&#x20;

### Troubleshooting Guide: Verifying Salesforce Queries to External Database (Vault Connect) <a href="#troubleshooting-guide-verifying-salesforce-queries-to-external-database-vault-connect" id="troubleshooting-guide-verifying-salesforce-queries-to-external-database-vault-connect"></a>

#### Issue <a href="#issue" id="issue"></a>

* **Symptom:** Records are not visible in the external object or global search is not functioning.

#### Steps to Verify Salesforce Queries to Vault Connect <a href="#steps-to-verify-salesforce-queries-to-vault-connect" id="steps-to-verify-salesforce-queries-to-vault-connect"></a>

1. **Open Developer Console:**
   * Navigate to the Developer Console in Salesforce.
2. **Change Log Level:**
   * Click on the **Debug** tab.
   * Select **Change Log Levels**.
3. **Adjust General Settings:**
   * Under the **General Setting** for your user, click on **Add / Change** under the **Debug Level Action**.
4. **Set Callout Level to Finest:**
   * Change the callout level to **Finest**.
5. **Check Logs:**
   * Look for logs with the operation **"/aura"**. These logs will capture the details of the callouts from Salesforce to Vault Connect.

#### Resolution <a href="#resolution" id="resolution"></a>

1. **Validate and Sync External Data Source:**
   * Go to **Setup**.
   * Search for **External Data Sources**.
   * Click the external data source you created for Vault Connect.
   * Click on **Validate and Sync**.
2. **Reestablish Link:**
   * Completing the **Validate and Sync** will ensure that the link between Salesforce and the external data source is reestablished if there is any problem.

By following these steps, you can troubleshoot and resolve issues related to the visibility of records in external objects and the functionality of global search.

### Prerequisites

Salesforce Connect OData 4.0 license subscription.

{% hint style="info" %}
**Note:** Not required for free developer edition org.
{% endhint %}

### Limitations <a href="#limitations" id="limitations"></a>

1. Files are not supported for viewing through external objects in Salesforce.&#x20;
2. Salesforce OData 4.0 adapter has a limitation on the number of callouts per hour. This will be addressed with the support for the Salesforce OData 4.01 adapter in subsequent versions of the capability.
3. All the limitations of Salesforce external objects are applicable as mentioned in this article: [Help and Training Community](https://help.salesforce.com/s/articleView?language=en\_US\&id=sf.platform\_connect\_general\_limits.htm\&type=5)
4. The solution only supports customers configured with AWS S3 as a storage option in Vault.
5. There is a max limit of 5GB of archived data per customer supported for connecting to Salesforce external data source as part of the beta program. This can be extended to a higher limit by raising a request with [support@autorabit.com](mailto:support@autorabit.com).
6. Fields of type XmlObjectWrapper are not supported.
7.  Fields of the object that have soapType as double, values will be truncated according to the precision and scale, as defined in the metadata of the object’s field.

    **For example:** If a field holds decimal value information for that object, precision and scale values will be predefined.

    **Precision:** The maximum number of digits in a numeric value includes all numbers to the left and the right of the decimal point (but excludes the decimal point character).

    **Scale:** The number of digits to the right of the decimal point in a numeric value must be less than the precision value.\
    **Example 1:**&#x20;

    Define a custom number field, e.g., "Number." Give it length = 3 and decimal places = 1 (scale). It might seem that this is done to restrict the precision of the field to one decimal place. However, on the UI level (on a standard edit page), if you try to type in, for example, 237.631, it will round it off to 237.631. Here precision is 4 and scale is 1. When mapping it back to Salesforce as the external object’s field, the value will be truncated to 237.6.

    **Example 2:**&#x20;

    Say a field holds info on geolocation latitude and longitude and their precision and scale are 5 and 2, respectively. Assign the value as 77.2090, then when mapping it back to Salesforce as the external object’s field, it will be truncated to 77.20.
8. Field type "time" is not supported in this version.
9. No more than four external lookup fields can be added to your page layout. On Lightning Experience record pages, a Record Detail component that contains more than four external lookup fields breaks the page at runtime. Please refer to the following documentation for more information on the limitations related to the layouts [https://help.salesforce.com/s/articleView?id=sf.layouts\_limitations.htm\&type=5](https://help.salesforce.com/s/articleView?id=sf.layouts\_limitations.htm\&type=5).&#x20;



