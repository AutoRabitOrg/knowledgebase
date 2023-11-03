# Default Apex Class Configuration

{% hint style="info" %}
**Important Note:**&#x20;

This article is for **Org Administrators** in particular. The actions discussed in this article are not available to general users. &#x20;
{% endhint %}

### Configure Default Apex Text Class for your Salesforce Org <a href="#configure-default-apex-text-class-for-your-salesforce-org" id="configure-default-apex-text-class-for-your-salesforce-org"></a>

To configure the default **Apex Test Class** for your Salesforce org, follow the below steps:&#x20;

1. Log in to your ARM account.
2.  Hover your mouse over the **`Admin`** tab and click on the option: **`SF Org Mgmt`**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572076213.png" alt=""><figcaption></figcaption></figure>
3. Select your **`Salesforce Org`** from the list and go to the **`Salesforce Org - Default Apex Test Class Configuration`** section. While deploying through ARM, this works in sync with the **Run Test** based on the **Changes Test** level option. If ARM cannot find dependent test classes, these default classes will run as Specified Tests.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572277097.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572354746.png" alt=""><figcaption></figcaption></figure>

4. Different options to choose from:

**`a. Fetch Current Set:`** This option fetches Apex and Test classes dependency. From the list     fetched, select the required Apex Text Class that you would like to configure and run into the Destination Org

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572495402.png" alt=""><figcaption></figcaption></figure>

**`b. Auto-populate:`** This option will run all local tests and get the complete dependency map

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572534496.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613572679417.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Troubleshooting:**&#x20;

If it takes longer to fetch the test classes using Auto-Populate, refresh the status by clicking the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613573106274.png) icon.
{% endhint %}

{% hint style="info" %}
**Important Note:**&#x20;

If Apex Tests are not being populated, follow the steps below to ensure that the **Store Only Aggregated Code Coverage** check box is unchecked:

1. Log in to your Salesforce org through the browser.
2. Go to **Setup**.
3. Use the **Quick Find/Search** box to open the **Apex Test Execution** page.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689939001273.png)
4. Click on **Options**. The **Apex Test Execution Options** pop-up appears.\
   ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1689939081453.png)
5. Ensure that the **Store Only Aggregated Code Coverage** check box is unselected.
6. Click **OK**, and return to ARM.
{% endhint %}

**`c. Add Manually:`**Manually configure your default Apex Test class.

1. On the next auto-populated screen, enter the **`Apex Test Class`** name and **`Apex Class/Trigger`** name in the respective fields. Mark the Apex class as default, and select the **`Default`** checkbox for such a test class.
2.  Click the **`Add`** button at the top right corner to add another Apex Class name, or click the **`Clone`** icon to copy the details of the previous Apex Class.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613573200619.png" alt="" width="563"><figcaption></figcaption></figure>
3. Click **`OK`**. You can find the manually added Apex class on the previous screen, i.e., the [**`Salesforce Org Management`**](../../arm-features/salesforce-org-management.md) page.

### Manage Apex Class <a href="#manage-apex-class" id="manage-apex-class"></a>

Once you have added an Apex test class or classes, you can perform various actions:

1. Click the **`edit`** icon next to the class name to modify its contents in a simple editor.
2. Click the **`delete`** icon to delete the class from your organization. You can select individual test classes or all the apex test classes in one go.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613573261291.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**:&#x20;

For each code coverage operation executed for your Salesforce org, AutoRABIT will either update or append the Apex Test Class mapping dynamically. Therefore, to view the added or modified Apex Test classes once the code coverage operation is performed, the user must ensure to refresh its Salesforce org from the [**`Salesforce Org Management`**](../../arm-features/salesforce-org-management.md) section.
{% endhint %}
