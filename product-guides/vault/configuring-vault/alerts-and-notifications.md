# Alerts & Notifications

### Overview <a href="#overview" id="overview"></a>

You can configure alerts to notify you or your team members of events that require attention based on criteria configured in an alert. They are email-based alert notifications that are sent out for records that have been added, modified, or deleted and that meet the alert conditions. The notification will include a copy of the records. When you create a notification, you set the conditions for who should receive it.

### How to set up Alerts? <a href="#how-to-set-up-alerts" id="how-to-set-up-alerts"></a>

Use the following steps to generate an email alert once the conditions configured is met for records in your Salesforce Org:

1. Login to your Vault account.
2.  From the dashboard, click **Setup** and then click on your **Salesforce Org**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321568006.png" alt=""><figcaption></figcaption></figure>
3. Go to the **Alerts** tab, and click on **Add Alert Rules**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321577308.png" alt=""><figcaption></figcaption></figure>

1.  On the **Add Alert** page, in the **Rule Name** field, type the name of the alert.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321592092.png" alt=""><figcaption></figcaption></figure>
2.  Next, select the category that you want to associate with this alert i.e., **metadata** or **data**.

    1. **Data:** For data, select the **object(s)** (max of 10 objects) from your [Salesforce Org](https://knowledgebase.autorabit.com/vault/docs/registering-salesforce-org) and enter the **alert values**. Once the alert threshold value reaches, an email notification triggers.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321602429.png" alt="" width="563"><figcaption></figcaption></figure>

    1. **Metadata:** For [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/), select the metadata members (max 10 members) from the list and enter the **alert value**.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321612184.png" alt="" width="563"><figcaption></figcaption></figure>
3. Select the alert criteria, whether the records were either added, modified or deleted, or all together.
4. Vault has a preconfigured alert that is triggered daily at **01:30 AM** **UTC** to evaluate the alert rule.
5. Select the recipients for the alert. By default, the author who configured the Salesforce Org in Vault will get auto-selected, however, you can add further teammates to notify about the alert. To do so, click on **Edit** and select the recipients who all be notified after the alert criteria are met, and then click **Apply**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321628355.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321638958.png" alt="" width="563"><figcaption></figcaption></figure>

1.  On the **Add Alert** page, review your selections, and then click **Submit**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321648786.png" alt="" width="563"><figcaption></figcaption></figure>
2. The new alert appears under **Alert Rules** on the **Alert** tab.
3. For all alert conditions that are met, that information will get displayed in the **Alert history** tab.

### Editing Alerts <a href="#editing-alerts" id="editing-alerts"></a>

You can modify the options of an alert using the **Edit Alert** wizard.

1. From the **Setup** Console, select your **Salesforce Org** and click **Alerts**.
2. In the **Alert Rules** section, search for the alert that you want to modify and then click the **Edit** icon.
3.  In the **Edit Alert** window, make the necessary changes and click **Submit**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321661135.png" alt="" width="563"><figcaption></figcaption></figure>

### Deleting Alerts <a href="#deleting-alerts" id="deleting-alerts"></a>

You can delete alerts.

1. From the **Setup** Console, select your **Salesforce Org** and click **Alerts**.
2. In the **Alert Rules** section, search for the alert that you want to delete and then click the **Delete** icon.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321672005.png" alt="" width="563"><figcaption></figcaption></figure>
