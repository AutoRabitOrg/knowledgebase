# Vault Connect

### Introduction

This document provides complete information about the new feature Vault Connect, which will enhance the user’s capability to better utilize Vault in viewing archived Salesforce data from an external data source.

### Feature Overview

1. OData protocol is an open and platform-independent protocol that can be integrated with the system of the user’s choice (along with Salesforce) as it exposes REST APIs for consuming and querying data from the underlying archives.
2. External objects support most of the capabilities that standard and custom objects have in Salesforce.
3. No need to install any managed packages or write custom scripts in Salesforce.

### Step-by-Step Guide

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

    * &#x20;How/where to config the external data source;
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
3. Provide **External Data** source.
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

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Salesforce Connect OData 4.0 license subscription.

{% hint style="info" %}
**Note:** Not required for free developer edition org.
{% endhint %}

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

**Example 1:**&#x20;

Define a custom number field, e.g., "Number." Give it length = 3 and decimal places = 1 (scale). It might seem that this is done to restrict the precision of the field to one decimal place. However, on the UI level (on a standard edit page), if you try to type in, for example, 237.631, it will round it off to 237.631. Here precision is 4 and scale is 1. When mapping it back to Salesforce as the external object’s field, the value will be truncated to 237.6.

**Example 2:**&#x20;

Say a field holds info on geo location latitude and longitude and their precision and scale are 5 and 2, respectively. Assign the value as 77.2090, then when mapping it back to Salesforce as the external object’s field, it will be truncated to 77.20.