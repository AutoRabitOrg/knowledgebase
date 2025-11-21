# Default Apex Class Configuration

{% hint style="info" %}
**Important Note:** This article is for **Org Administrators** in particular. The actions discussed in this article are not available to general users. &#x20;
{% endhint %}

### Configure Default Apex Test Class for your Salesforce Org <a href="#configure-default-apex-text-class-for-your-salesforce-org" id="configure-default-apex-text-class-for-your-salesforce-org"></a>

To configure the default **Apex Test Class** for your Salesforce org, follow the below steps:&#x20;

1. Log in to your ARM account.
2. Hover your mouse over the **`Admin`** tab and click on the option: **`SF Org Mgmt`**.

<figure><img src="../../../../.gitbook/assets/image (769).png" alt="" width="173"><figcaption></figcaption></figure>

3. Select your **`Salesforce Org`** from the list and go to the **`Salesforce Org - Default Apex Test Class Configuration`** section. While deploying through ARM, this works in sync with the **Run Test** based on the **Changes Test** level option. If ARM cannot find dependent test classes, these default classes will run as Specified Tests.

<figure><img src="../../../../.gitbook/assets/image (770).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1609) (1).png" alt=""><figcaption></figcaption></figure>

* Delete: You can delete the Apex Test Class from the Default Apex Test Class Configuration.
* Edit: You can add or delete Apex Class/Trigger for the Apex Test Class.
* Checkbox: This for selecting the Apex Test Class as part of the Default Apex Test Class, and you can click on save.
* Clear: This will clear your Default Apex Test Class Configuration for your Salesforce Org.

4. Different options to choose from:

&#x20;    **`a. Fetch Current Set:`** This option fetches Apex and Test classes dependency. From the list     fetched, select the required Apex Test Class that you would like to configure and run into the Destination Org

<figure><img src="../../../../.gitbook/assets/image (772).png" alt=""><figcaption></figcaption></figure>

&#x20;    **`b. Auto-populate:`** This option will run all local tests and get the complete dependency map

<figure><img src="../../../../.gitbook/assets/image (773).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (774).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Troubleshooting:** If it takes longer to fetch the test classes using Auto-Populate, refresh the status by clicking the![](<../../../../.gitbook/assets/image (775).png>)icon.
{% endhint %}

{% hint style="info" %}
**Important Note:** If Apex Tests are not being populated, follow the steps below to ensure that the **Store Only Aggregated Code Coverage** check box is unchecked:

1. Log in to your Salesforce org through the browser.
2. Go to **Setup**.
3. Use the **Quick Find/Search** box to open the **Apex Test Execution** page.<br>

![](<../../../../.gitbook/assets/image (776).png>)

4. Click on **Options**. The **Apex Test Execution Options** pop-up appears.

![](<../../../../.gitbook/assets/image (777).png>)

5. Ensure that the **Store Only Aggregated Code Coverage** check box is unselected.
6. Click **OK**, and return to ARM.
{% endhint %}

&#x20;    **`c. Add Manually:`**&#x4D;anually configure your default Apex Test class.

5. On the next auto-populated screen, enter the **`Apex Test Class`** name and **`Apex Class/Trigger`** name in the respective fields. Mark the Apex class as default, and select the **`Default`** checkbox for such a test class.
6. Click the **`Add`** button at the top right corner to add another Apex Class name, or click the **`Clone`** icon to copy the details of the previous Apex Class.

<figure><img src="../../../../.gitbook/assets/image (778).png" alt="" width="563"><figcaption></figcaption></figure>

7. Click **`OK`**. You can find the manually added Apex class on the previous screen, i.e., the [**`Salesforce Org Management`**](../../../arm/registration/salesforce-org/salesforce-org-management.md) page.

### Manage Apex Class <a href="#manage-apex-class" id="manage-apex-class"></a>

Once you have added an Apex test class or classes, you can perform various actions:

1. Click the **`edit`** icon next to the class name to modify its contents in a simple editor.
2. Click the **`delete`** icon to delete the class from your organization. You can select individual test classes or all the apex test classes in one go.

<figure><img src="../../../../.gitbook/assets/image (779).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** For each code coverage operation executed for your Salesforce org, AutoRABIT will either update or append the Apex Test Class mapping dynamically. Therefore, to view the added or modified Apex Test classes once the code coverage operation is performed, the user must ensure to refresh its Salesforce org from the [**`Salesforce Org Management`**](../../../arm/registration/salesforce-org/salesforce-org-management.md) section.
{% endhint %}
