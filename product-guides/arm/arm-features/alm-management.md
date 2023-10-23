# ALM Management

{% hint style="info" %}
Important Note

This article is for the **Org Administrator** in particular. The actions discussed in the article will not be available to general users.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

We've added a new section called **`ALM Management`** to the **`Admin`** module with the release of ARM 21.6. This section contains detailed information on your ALM's active and inactive sprints. It also lists work items and allows you to establish criteria for updating work item status by mapping your ALM with your version control repository.

### Registering an ALM <a href="#registering-an-alm" id="registering-an-alm"></a>

1. Log in to ARM as an admin.
2. Navigate to **`Admin > ALM Mgmt`**.
3.  Click **`Register ALM`** on the **`ALM Mgmt.`** screen.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1663212097872.png" alt="" width="563"><figcaption></figcaption></figure>
4. Configure the following settings:
   1.  For **`IBMRTC`**, **`CA Agile Central`**, **`VersionOne`**, and **`Azure DevOps:`**\


       * **`ALM Name:`** Enter a **name** for your ALM connection.
       * **`ALM Type:`** Select the **ALM type**.
       * **`ALM URL:`** Add the **ALM server URL**.
       * **`Credentials:`** Specify your credentials. Refer to the [Credential Manager](../create-users-credentials.md) section for more info on creating and storing your credential inside ARM.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1663236280440.png" alt="" width="375"><figcaption></figcaption></figure>
   2.  For **`JIRA:`** \


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1663236363451.png" alt="" width="375"><figcaption></figcaption></figure>

       * **`ALM Name:`** Enter a name for your ALM connection.
       * **`ALM Type:`** Select **`JIRA`**.
       * **`Access Type:`**Select one of the following:
         * **`Standard:`** Add the **`ALM URL`** and specify your **`Credentials`**.
         *   **`OAuth:`** Select the access type as **`OAuth`**, and click on **`Validate & Save`**. You will be redirected to the ALM's website to authenticate your credentials and grant permission.\
             Important Notes:

             * Jira OAuth access type is currently supported for **Cloud versions** only.
             * OAuth access type will only be available while registering ALM if the credentials have been successfully registered in the **ALM Settings** section. For more information on registering Jira OAuth credentials, click [here](../getting-started/arm-administration/user-management/manage-users-account-settings/).



             <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1663236337273.png" alt="" width="375"><figcaption></figcaption></figure>

             * The **Access Token** expires in one hour. The **Refresh Token** expires every **90 days**.
5. Click on **`Test Connection`** to authenticate your credentials.
6. Click **`Save`**.
7. Once your [ALM](../alm-labels.md) is registered successfully, you can view it in the **`ALM List`** menu.
8. Use the **`AR Comments`** toggle button to turn off the Jira comments from AR. By default, the Jira comments are ON for newly registered and existing ALMs.
9. Use the **`Access Type`** drop-down list to switch between **`Standard`** and **`OAuth`**. Click on **`Re-Authenticate`** if your credentials have expired. This is only applicable to Jira ALMs.

Limitation:Jira OAuth access type is currently supported for **Cloud versions** only. This function is on-demand, so if you'd want to make it available for your organization, please contact our experts at [support@autorabit.com](mailto:support@autorabit.com).

#### Integration Settings <a href="#integration-settings" id="integration-settings"></a>

By default, we do not display the work items from the inactive sprints; however, if you want to view the hidden items, you can do so from this section.

1. Select the following checkbox to view the work items from the inactive sprints: **`Display work items from inactive sprints (we recommend setting up global filter criteria if are enabling this)`**
2. **`Enable global filter criteria on work items`**: This checkbox allows you to specify filter criteria.
   * You can select which fields are displayed by selecting the necessary column/field. However, you can refine the list of work items displayed by configuring a worklist filter.
   * Repeat these steps for each field if you want to set filter criteria.
3.  Click **`Save Settings`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664368843952.png" alt="" width="563"><figcaption></figcaption></figure>

**Note:** To remove a field's filter criteria, click on the ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-QT6MJ131.png) icon to the right of the rule.

#### Smart Commits <a href="#smart-commits" id="smart-commits"></a>

In this section, you can select the pattern used to read the comment in a revision associated with your ALM story. For example, _'git commit m **\[project123]** # add README file into the project'_\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682079131324.png" alt="" width="375"><figcaption></figcaption></figure>

If you want to configure a webhook in your repository, select the **Enable auto update on webhook** checkbox to reveal the URL required for the webhook settings. For more information on how to configure a webhook in different repositories, refer [HERE](../webhooks/). You can also choose to [sync external smart commits](version-control/version-control-repositories-summary.md).

#### Repository Mappings <a href="#repository-mappings" id="repository-mappings"></a>

A global setting that lets you manage work items effectively for Merge requests. You can have your work items automatically updated in your ALM system based on the chosen criteria (Source Branch, ALM Status, etc.). Whenever a new merge request is initiated with this global setting enabled, the work items are automatically moved to a different status in ALM post-successful merge.

Points to Note:

* Repository mapping must be done to use smart commits sync functionality.&#x20;
* The ALM work item status is only updated when performed via merge requests.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664369162933.png" alt="" width="563"><figcaption></figcaption></figure>

1. Select your version control **`Repository`**.
2. Select the **`Source Branch`**. If you cannot view your branch from the dropdown list, please click on the **`Don't see your branch? Register here`** link.
3. Select your configured **`ALM Project`**.
4.  When you click on the **`ALM Work Item Status`** field, a popup page appears, which allows you to select the **`Work Item Type`**, the current item status, and the item status to update.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664369094399.png" alt="" width="375"><figcaption></figcaption></figure>
5. Click **`Save`**.\
   Important Note:Only those branches and repo configurations for which the user has permissions will be visible in the respective dropdown lists. The repos or branches for which the user does not have permissions will be hidden.
6.  Also, the ALM can be configured not to send e-mail notifications of work item updates to the concerned person. Type the email address(es) in the **`Notify exception status updates to`** field.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664369286308.png" alt="" width="563"><figcaption></figcaption></figure>
