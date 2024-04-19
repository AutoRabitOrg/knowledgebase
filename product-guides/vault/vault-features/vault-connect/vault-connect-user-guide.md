# Vault Connect User Guide

### Introduction

This document provides complete information about the new feature Vault Connect, which will enhance the user’s capability to better utilize Vault in viewing archived Salesforce data from an external data source.

### Feature Overview

1. OData protocol is an open and platform-independent protocol that can be integrated with the system of the user’s choice (along with Salesforce) as it exposes REST APIs for consuming and querying data from the underlying archives.
2. External objects support most of the capabilities that standard and custom objects have in Salesforce.
3. No need to install any managed packages or write custom scripts in Salesforce.

### Step-by-Step Guide

**Create Connect Config**

1. Log in to the **Vault** application.

![A screenshot of a computer

Description automatically generated](<../../../../.gitbook/assets/0 (2).png>)

Navigate to the setup module of the Vault application.

Click on the required **Org**.

![](<../../../../.gitbook/assets/1 (2).png>)

1. Click on the **Connect (Beta)** module of the Vault application.
2. On landing on the **Connect (Beta)** tab of the Vault setup, the user will see the following message on the screen:

![](<../../../../.gitbook/assets/2 (2).png>)

1. Once the customer reaches out to AutoRABIT support team as specified on the above screen, our technical team will perform due diligence to enable **Vault Connect** for the customer(s).
2. When **Vault Connect** is enabled on the application, the user will see the following screen on the **Connect (Beta)** tab of the Vault Setup module.

![](<../../../../.gitbook/assets/3 (2).png>)

1. Click on the **Add Connect Config** button on the application.

![](<../../../../.gitbook/assets/4 (2).png>)

1. A pop-up will be displayed with t**he following information:**
   1. How/where to config the external data source;
   2. OData URL for configuring the external data source; and
   3. What to select when creating Auth. Providers.

![](<../../../../.gitbook/assets/5 (2).png>)

Copy the URL from the pop-up shown.

**Note:** The same URL can be copied from the pop-up and opened by clicking on the information icon available beside the **Add Connect Config** button.

![](<../../../../.gitbook/assets/6 (2).png>)

![A screenshot of a computer

Description automatically generated](<../../../../.gitbook/assets/7 (2).png>)

Select the required config from the **Archive Config** section and click on the **Next** button.

![](<../../../../.gitbook/assets/8 (2).png>)

On clicking **Next,** you will be redirected to the **Jobs** section.

![](<../../../../.gitbook/assets/9 (2).png>)

1. Select the required **Job** and click on **Next**.
2. On clicking **Next**, you will be redirected to the **Objects** section.

![](<../../../../.gitbook/assets/10 (2).png>)

The following operations can be performed:

Include/exclude the required objects from the list of objects available.

![](<../../../../.gitbook/assets/11 (2).png>)

1. Include/exclude the fields as required from the list of Fields available.
   1. Click on the **File** icon from the **Fields** column.

![](<../../../../.gitbook/assets/12 (1).png>)

The following pop-up will be displayed, where the user can exclude the fields as required and click on **Apply** field.

![](<../../../../.gitbook/assets/13 (1).png>)

On clicking **Save**, you will be prompted to enter the **Name** and **Description** for the config being created.

![](<../../../../.gitbook/assets/14 (1).png>)

1. On entering the required details, click on **Save.**
2. On clicking **Save**, you will be shown a pop-up that says, **“Config has been created/updated successfully,”** and you will be redirected to the **Connect Config Summary**.

![](<../../../../.gitbook/assets/15 (1).png>)

1. On the **Connect Config Summary**, you can view all the configurations created.
2. **View the Archived Data In Salesforce**
   1. Log in to the Salesforce org for which you want to view the data.
   2. **Create Auth. Providers**
      1. **Go to** → **Auth. Providers** under setup.
      2. **Click on the Auth. Providers under setup.**

![](<../../../../.gitbook/assets/16 (1).png>)

Click on **New.**

![](<../../../../.gitbook/assets/17 (1).png>)

Select the **Provider Type 🡪 Salesforce.**

![](<../../../../.gitbook/assets/18 (1).png>)

Provide **Name** and **URL Suffix** and click on **Save.**

* **Note:** Do not change the remaining settings on the layout.

![](<../../../../.gitbook/assets/19 (1).png>)

1. On completing the required selections, click on the **Save** button.
2. **Create External Data Sources**
   1. **Go to** → **External Data Sources** under setup.

![](<../../../../.gitbook/assets/20 (1).png>)

Click on **New External Data Sources.**

1. _P_rovide External Data Source.
2. _Provide Name._
3. _Type → Salesforce Data: OData 4.0_

**Identity type** → Named Principal

**Authentication Protocol** → OAuth 2.0

**Authentication Provider** → On clicking the **LookUp** glass, you can select the **“Auth. Provider”** created earlier.

Select the **Authentication Provider.**

Click on **Save on the External Data Sources screen.**

On **Save**, click the **Validate and Sync.**

You will be shown all the objects selected as part of the config creation.

On selecting the required objects, the Sync button on Salesforce will be enabled.

Select all the objects you want to sync or select which objects’ data you want to view in Salesforce.

Click on the **Sync** button.

On completion, you can see all the objects selected.

* **Create Tabs:** Customers can view the archived data under these tabs.
  1. **Go to → Tabs** under **setup**.
     1. Click on the **New** button.

Under **Objects**, you can see the objects that are part of the Config created with the naming convention **“Object\_\_X”.**

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Salesforce Connect OData 4.0 license subscription.

**Note:** Not required for free developer edition org

### Limitations <a href="#limitations" id="limitations"></a>

1. Files and attachments are not supported for viewing through external objects in Salesforce. This will be supported in the upcoming version of Vault Connect scheduled for the end of Q4’23.
2. Salesforce OData 4.0 adapter has a limitation on the number of callouts per hour. This will be addressed with the support for the Salesforce OData 4.01 adapter in subsequent versions of the capability.
3. Relationships between external objects and Salesforce objects need to be established manually (like if cases are archived and they are related to accounts that are not archived, the reference to accounts that are in the Salesforce object will be available in the external object but will not be reflected as a lookup relationship). The plan is to support the automated recreation of these references by the end of Q4 2023.
4. All the limitations of Salesforce external objects are applicable as mentioned in this article: [Help and Training Community](https://help.salesforce.com/s/articleView?language=en\_US\&id=sf.platform\_connect\_general\_limits.htm\&type=5)
5. The solution only supports customers configured with AWS S3 as a storage option in Vault.
6. There is a max limit of 5GB of archived data per customer supported for connecting to Salesforce external data source as part of the beta program. This can be extended to a higher limit by raising a request with [support@autorabit.com](mailto:support@autorabit.com).
7. Fields of type XmlObjectWrapper are not supported.
8.  Fields of the object that have soapType as double, values will be truncated according to the precision and scale, as defined in the metadata of the object’s field.

    **For example:** If a field holds decimal value information for that object, precision and scale values will be predefined.

    **Precision:** The maximum number of digits in a numeric value includes all numbers to the left and to the right of the decimal point (but excludes the decimal point character).

    **Scale:** The number of digits to the right of the decimal point in a numeric value must be less than the precision value.

**Example 1:**\
Define a custom number field, e.g., "Number." Give it length = 3 and decimal places = 1 (scale). It might seem that this is done to restrict the precision of the field to one decimal place. However, on the UI level (on a standard edit page), if you try to type in 237.631, here, precision is 4 and scale is 1. When mapping it back to Salesforce as the external object’s field, the value will be truncated to 237.6.\


**Example 2:**\
Say a field holds info on geolocation latitude and longitude and their precision and scale are 5 and 2, respectively. Let the value it holds be 77.2090, then when mapping it back to Salesforce as the external object’s field, it will be truncated to 77.20.
