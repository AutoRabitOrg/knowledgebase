# Salesforce Org Management

{% hint style="info" %}
**Important Note:** This article is for the **Org Administrator** in particular. The actions discussed in the article will not be available to general users. &#x20;
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

All the org connections added to ARM can be seen on the **Salesforce Org Management** page. This page lists details for the Salesforce orgs you have added and any org that has been shared with you by your team members.

The **Salesforce Org Management** page shows information about:

1. Details of your Salesforce org
2. ALM / Plugins mapped with your Salesforce org
3. List of metadata members available with your Salesforce org
4. Default Apex Test Class configured
5.  User Permissions assigned to your Salesforce org\
    \


    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.14.29 PM.png" alt=""><figcaption></figcaption></figure>

### Salesforce Org - Details <a href="#salesforce-org-details" id="salesforce-org-details"></a>

A summary of the Salesforce org registered with ARM is displayed in this area.\
\


<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

The fields displayed in this section are described in the table below:&#x20;

| Field Name                    | Indicates                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Name`**                    | Name of the Salesforce org given when registering with ARM.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **`Type`**                    | Salesforce org types such as Developer, Sandbox, or Production.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`Environment`**             | Your Salesforce environment, i.e., Production or Development Edition, Sandbox, or Production.                                                                                                                                                                                                                                                                                                                                                                                      |
| **`URL`**                     | Salesforce login URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **`Registered Date`**         | Date of account activation.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **`Access Type`**             | Authorization type such as OAuth, Standard. For the _Standard_ Access type, the username, password, and security token will be displayed.                                                                                                                                                                                                                                                                                                                                          |
| **`Re-Authenticate`**         | If the OAuth token has expired for a saved connection, click this to re-enter your user credentials and refresh the connection so ARM can continue to connect to it.                                                                                                                                                                                                                                                                                                               |
| **`Test Connection`**         | To check if the connection has been authenticated or not. Once clicked, a success message is displayed once the authentication is complete.                                                                                                                                                                                                                                                                                                                                        |
| **`Person Accounts Enabled`** | When you do business with individual consumers, you can enable the Person Accounts. Person accounts apply to organizations that operate on a business-to-consumer model. Remember that you cannot disable Person Accounts once you enable them. For more information, refer to the article published in Salesforce: [https://help.salesforce.com/articleView?id=account\_person\_enable.htm\&type=5](https://help.salesforce.com/articleView?id=account_person_enable.htm\&type=5) |
| **`nCino Package Enabled`**   | This checkbox is selected by default if your Salesforce org is enabled with nCino objects. Unselecting the checkbox will remove the nCino objects configured with your Salesforce Org, and you'll be unable to use the nCino metadata and data for deployment.                                                                                                                                                                                                                     |

About nCino Package Enabled: Selecting the **Enable nCino package** previously required getting all nCino deployed packages of the Salesforce org; however, users without **Modify All Data** and **Download App** permissions could not register the org in the ARM application. To avoid this, the mandatory option to load nCino deployed packages while registering a Salesforce org has been disabled.

**Additional options under 'Salesforce Org - Details' section**\


<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.15.59 PM.png" alt=""><figcaption></figcaption></figure>

1. **`Clone:`** ARM clone functionality creates duplicate records to reduce unnecessary retyping.
2. **`View/Download Audit Log:`** The audit log shows the recent changes made to your org. It lists the date of the change, who made it, and what the change was. All objects include fields to store the name of the user who created the record and who last modified the record. This provides some basic auditing information. Use the **`Download Audit Log`** button to save the audit log in your local system.
3.  **`Generate Code Coverage Report:`** This function allows you to run all available Apex Test Classes in the Salesforce org and generate a code coverage report. The code coverage report will be emailed to your registered email id with the CSV file attached. The CSV file will contain the failed test classes that require the user's attention to resolve. Select **`Do you want us to update the test classes?`** checkbox to avoid classes from getting overwritten after deployment.\


    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
4.  Attached is the sample email that will be notified to the user whenever the code coverage is run.

    * Code Coverage with a success rate of more than 75%

    <figure><img src="../../../../.gitbook/assets/image (8) (2).png" alt="" width="375"><figcaption></figcaption></figure>

    * Code Coverage with a failure count of more than 20

    <figure><img src="../../../../.gitbook/assets/image (9) (2).png" alt="" width="341"><figcaption></figcaption></figure>

    * Code Coverage with failure count of less than 20 (detailed error report will be included in the email body)

    <figure><img src="../../../../.gitbook/assets/image (10) (2).png" alt="" width="301"><figcaption></figcaption></figure>

### Salesforce Org - Mappings <a href="#salesforce-org-mappings" id="salesforce-org-mappings"></a>

Mapping your Salesforce org with your version control system or ALM configured in ARM. This helps create a control during a commit, merge, or deployment action performed on your Salesforce org or version control branch.\
\


<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.13.05 PM.png" alt="" width="563"><figcaption></figcaption></figure>

Suppose you want to connect your Salesforce Org with Version Control as a **`GIT`**.&#x20;

1. Click on the **`Mapping`** button for Version Control as **`GIT`**.
2. Select the respective version control **`Repository`** and the **`Branch`** for your GIT.
3.  Click **`Test Connection`** to authenticate your connection.\


    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
4. Remember to click on **`Save Mappings`** to save the details, or else you need to repeat the above steps.

In another scenario, let us assume you also like to configure JIRA (ALM tool) with your Salesforce org.&#x20;

{% hint style="info" %}
**Important Note:** To proceed ahead with the below steps, make sure the JIRA is successfully integrated with ARM ([LEARN MORE](../../../arm/integration-and-plugins/jira.md))
{% endhint %}

1. Click on the **`Mapping`** button beside JIRA.&#x20;
2. Select the **`Jira`** label and the **`Project`** from the drop-down list.&#x20;
3.  Click on **`Save Mappings`** to save the details, and you're done.\
    \


    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Salesforce Org - Skip Members <a href="#salesforce-org-skip-members" id="salesforce-org-skip-members"></a>

In this section, you can add certain metadata members from your Salesforce org that will be skipped whenever any deployment happens to the org.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.28.02 PM.png" alt=""><figcaption></figcaption></figure>

Suppose you want to skip **Analytics Cloud Integration User**, **Analytics Cloud Security User**, and **Authenticated Website** metadata members for the **`Profile`** metadata type. In such a case, select the **`Type`** as **`Profile`** under and click the **`Fetch Members`** button.

Select the metadata members from the list. These members will be skipped each time the deployment is performed on the above Salesforce org. Click **`OK`**.

<figure><img src="../../../../.gitbook/assets/image (15) (2).png" alt="" width="563"><figcaption></figcaption></figure>

Similarly, you can add different metadata members for various metadata types. Additionally, if you remember certain members you like to add manually, you can enter the **`Enter members manually`** field and click **`Add`**.

The Salesforce Org- Skip Members section shows a summary of the selected metadata members. Click on **`Save Members`** to save the steps configured.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.28.02 PM (1).png" alt=""><figcaption></figcaption></figure>

### Salesforce Org - Default Apex Test Class Configuration <a href="#salesforce-org-default-apex-test-class-configuration" id="salesforce-org-default-apex-test-class-configuration"></a>

This section is about configuring the default Apex Class for your Salesforce Org. This topic is covered in a separate article. Refer to the article [HERE](../../../arm/troubleshoot/how-tos/default-apex-class-configuration.md).\
\


<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Salesforce Org - User Permissions <a href="#salesforce-org-user-permissions" id="salesforce-org-user-permissions"></a>

The list of users allowed to work with your Salesforce Org is available in this section. The administrator may assign permission to its users on various modules of ARM that are feasible with the Salesforce Org.\
\


<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-17 at 7.37.48 PM.png" alt="" width="563"><figcaption></figcaption></figure>

### How do I update or change the username in all of the Salesforce Orgs specified in AutoRABIT? <a href="#how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au" id="how-would-i-go-about-updating-or-changing-the-username-in-all-of-the-salesforce-orgs-specified-in-au"></a>

To update the username on all registered orgs, re-authenticate the orgs in **Admin > SF Org Management** page.
