# Integrate ServiceNow with ARM

**Integrate ServiceNow with ARM**

**Step 1: Store your user's ServiceNow credential in ARM**

This is an initial step where the user's ServiceNow credentials, such as username and password, are stored in ARM.

1. Log in to your ARM account.
2.  Hover your mouse over the **Admin** module and click on the **Credentials** tab.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-m79xgces.png" alt="" width="375"><figcaption></figcaption></figure>
3.  Next, click on **Create Credential** from the right navigation bar.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-zzb508f9.png" alt=""><figcaption></figcaption></figure>
4. On the next pop-up screen, enter a **Credential name**.
5. Choose the **Credential Type** as '**User name with Password.'**
6. Enter your ServiceNow **username** and **password;** we will store this encrypted.
7. Please double-check that you are using your ServiceNow username instead of the email address that you use to log in to ServiceNow.
8.  Click **Save**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-4foegunu.png" alt="" width="375"><figcaption></figcaption></figure>

**Step 2: Integrate ServiceNow with ARM**

1. If you're logged out from your account, log in again into ARM with your credentials.
2. Go to **Admin > My Account** section.
3.  Click on **New ALM System** under the **ALM Management** section.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-zsueqar9.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Select **ALM type** as '**SERVICENOW'** from the dropdown.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-j58agzsw.png" alt="" width="375"><figcaption></figcaption></figure>
5. Enter the **label name** of your own choice.
6. Enter your ServiceNow subdomain (e.g., _https://\[subdomain].atlassian.net_) in the **URL** field.
7. Select the same **user's credential** created in **Step 1**.
8. Click **Test Connection** to check whether the connection has been authenticated. If so, a ‘success’ message is displayed after the authentication is completed.
9. Click **Save** and your ServiceNow integration is ready.
10. Once you log in, ServiceNow is integrated with your ARM account, and you can start logging bugs and issues with just one click directly to ServiceNow.

**Limitation:**

**ServiceNow OAuth** access type is currently supported for **Cloud versions** only. This function is on-demand, so if you want to make it available for your organization, please get in touch with our experts at **support@autorabit.com**.

**Configuring ServiceNow Work Items in ARM**

You and your team members have a provision to perform actions on ServiceNow issues or update the ServiceNow work items while running a commit or during a CI job.

**In EZ-Commit**

In the **EZ-Commit** screen and under the **Post Commit** section, you should:

1. Select the checkbox: **Update ALM Workitem Status**
2. Select the **ALM type** as **SERVICENOW.**
3. Select the **ALM Label, project,** **sprint** and ALM work item for which the commit is planned.
4.  Select the **work item** and the **status**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-t30lgwo4.png" alt=""><figcaption></figcaption></figure>
5. Once the changes are committed to the version control system, the status of the ALM work item is updated and reflected in your ALM system.

**In CI Job**

**Important Notes:**

Configuring the ServiceNow work items is applicable to the following CI jobs:

* Package from Version Control
* Deploy from Version Control
* Deploy from the SFDX branch to a Salesforce Org
* Install an Unlocked Package from a Version Control Branch

1. Go to the **Build** section under the **New Create CI Job** screen.
2.  Select the **Map ALM Project (Ex: ServiceNow)** checkbox.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-y62sa96d.png" alt="" width="375"><figcaption></figcaption></figure>
3. Go to the **ALM** section. Here you can configure the work item type status in ServiceNow ALM to include in the build.
4. Select the **ALM type** as **SERVICENOW.**
5.  Select the **ALM Label** and its related **Projects**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-az06b6wx.png" alt=""><figcaption></figcaption></figure>
6.  The active sprint(s) for the above-selected Project will be available in the **Sprint** dropdown. ARM has given provisions for you to update multiple sprints related to tasks or bugs and update the status on the go when running the CI Job. You can select either one of the sprints or, if you wish to update the status for all the sprints, leave it as default, i.e., keep **'All Active Sprints'** in the selected mode.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-v4jbuoxx.png" alt=""><figcaption></figcaption></figure>
7. Select the **Work Item** type. Here you can select multiple work items to update the status for in your ALM. To use all the work item types, keep the **'All Work Item Type'** option selected by default.

![A white background with black lines  Description automatically generated](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-22x1ae1w.png)

Based on the above work item selected, you need to update the status for each work item type. See the screenshot below.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/servicenow-image-801c4d00.png" alt=""><figcaption></figcaption></figure>
