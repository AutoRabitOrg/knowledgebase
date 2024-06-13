# Subscription Management

{% hint style="info" %}
**Important Notes**:&#x20;

This article is for the **registered user** in particular. **General users** do not have access to the Subscriptions tab.

* Only the **Registered User** can view the **Subscription Management** page.
* The **Team Administrator** cannot view the **Subscription Management** page.
* **Org Admins** added by the **Registered User** also cannot view the **Subscriptions** page.
{% endhint %}

## Feature Availability

### Subscription Tab Feature Availability

{% hint style="info" %}
**NOTE:** The below-highlighted Subscription button will only appear if a customer procures more than 20+ licenses to manage different Teams.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Subscription Management: Overview <a href="#subscription-management-overview" id="subscription-management-overview"></a>

ARM offers an easy and centralized solution for a **Registered User** of your organization to manage team subscriptions and accounts. This ensures tracking of all subscription activity, ensuring everything is logged, and nothing is lost. You use the **Subscription Management (SM)** interface to review and manage how purchased subscriptions are used on your production instance.

### Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your ARM account using the **Registered User** credentials.&#x20;
2.  Hover your mouse over the **`Admin`** tab and click on **`Subscriptions`**.

    <div align="left">

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613371366434.png" alt=""><figcaption></figcaption></figure>

    </div>
3. Your active plan details will be shown on the dashboard with details like:
   1. **`Total Subscriptions:`** Number of licenses purchased by the organization. Only the Registered User of your organization can view the Subscription Management section.&#x20;
   2. **`Total Subscription Allotted:`** Number of licenses utilized to date.
   3.  **`Total Subscription Available:`** Total number of licenses available.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613372997657.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: By default, ARM considers you as part of a team, and if the subscription available denotes 'zero', it means you completely utilize the entire team subscription for your team only.&#x20;
{% endhint %}

### Adding and Configuring Teams  <a href="#adding-and-configuring-teams" id="adding-and-configuring-teams"></a>

This section is about creating the teams and assigning members to those teams. This allows you to assign tasks to specific groups of people in your organization.&#x20;

1. Log in to the **`Subscription Management`** dashboard using the Registered User credential.&#x20;
2. On the right side of the screen, click **`Create Team`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373030633.png" alt=""><figcaption></figcaption></figure>

3. Enter a **name** for your team.
4. Choose a **`Team Administrator`** or click on the![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613371626189.png)icon to create a user account and assign them permission as a Team Administrator. Fill in the required details; the newly created user will be assigned as a Team Administrator.

{% hint style="info" %}
**Important Notes**:

* Only the **delegated** or **released users** list will be displayed in the **Team Administrator** dropdown field. For more information on delegated or released users, please refer [HERE](user-management/delegate-approvals-to-another-user.md).
* **Users** assigned to a team are **not** allowed to join another **team**.
{% endhint %}

5. Next, enter the number of licenses required in the **`Team Subscriptions`** field.
6. If you would like to add the current logged-in registered user as part of the team, select the checkbox: **`Grant access to this team for`**

{% hint style="info" %}
**Important Note**: The granted user will not be counted as a part of the subscribed licenses on the team.
{% endhint %}

7. &#x20;Click **`Save`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373334482.png" alt="" width="375"><figcaption></figcaption></figure>

8. The newly created team will be displayed on the **`Subscription Management`** home page.&#x20;
9. For each team created, the following information is displayed:
   * **`Team Name:`** Name of the Team
   * **`Created Date:`** Date/time stamp for the team created
   * **`Team Admin:`** Team Administrator assigned to the current team
   * **`Subs. Allotted:`** Number of licenses allotted to the team
   * **`Subs. Consumed:`** Number of licenses consumed
   * **`Subs. Available:`** Number of licenses pending
10. Additional options:
    1. **`Add New Resource:`** Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373619889.png) symbol to add new resources to the team. The team administrator can create users with their login. However, if you need to add resources from the existing login, follow the steps mentioned in the [Delegate Users](user-management/delegate-approvals-to-another-user.md) section.
    2. **`Edit Team:`** Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373639447.png)icon to modify the team details, like assigning a new team administrator, changing the subscription licenses, etc.&#x20;
    3. **`Delete a Team:`** Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373655253.png) icon to delete the team. This process cannot be undone.

{% hint style="info" %}
**Important Note:** If the current **Team Administrator** is replaced with another **Team Administrator**, then the **entire permissions** that the current administrator holds will be delegated to the new **administrator**.
{% endhint %}

## Managing Licenses for Enterprise Users <a href="#managing-licenses-for-enterprise-users" id="managing-licenses-for-enterprise-users"></a>

As an _Account Administrator_ for your ARM account, you can manage the user licenses you have subscribed to for your organization.

#### Purchase Additional User Licenses <a href="#purchase-additional-user-licenses" id="purchase-additional-user-licenses"></a>

You must submit a support ticket to purchase extra licenses for your organization. Our Customer Success (CS) team will provide you with a new license key, which you must upload to the **Subscription Management** page.

**Step 1: Upload License Key**

Navigate to **`Admin > Subscription Management`** once you've received the license key file from us. You'll see a summary of the _Total Subscription_ count, _Total Subscription Allotted_ so far, and _Total Subscription Available_ (which can be assigned to a user or team).&#x20;

Click on **`Choose File`** and upload the **`license key`** (.l4j file format). Click **`Upload`**.&#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1648659860162.png" alt=""><figcaption></figcaption></figure>

The total subscription counts will be changed based on the user's license specified in the key.

ErrorIf an incorrect file is selected, a notification popup stating that the file is incorrect is displayed. Click on the **Reset** button and select the correct file.

**Step 2: Updating Allotted Subscriptions**

After uploading the license key, the administrator can allot the available subscriptions to the desired team.

1. Look for the desired team on the **Subscription Management** page.
2. Then, under the **`Actions`** tab, click on the **Edit (**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613373639447.png) **)** icon to update the subscription count for a team.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1648660359443.png" alt=""><figcaption></figcaption></figure>

3. The number of user licenses available for your account is displayed in the **`Subscriptions Available`** field.
4. In the **`Team Subscriptions`** section, click on the **`-`** or **`+`** buttons to update the license count, then click **`Save`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1648660371823.png" alt="" width="375"><figcaption></figcaption></figure>

All fields on the **Subscription Management** page will get updated.





