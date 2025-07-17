# Alerts & Notifications

### Overview <a href="#overview" id="overview"></a>

You can configure alerts to notify you or your team members of events that require attention based on criteria configured in an alert. They are email-based alert notifications sent for records that have been added, modified, or deleted and meet the alert conditions. The notification includes a copy of the records. When you create a notification, you define who should receive it and under what conditions.

### How to Set Up Alerts? <a href="#how-to-set-up-alerts" id="how-to-set-up-alerts"></a>

Follow these steps to generate an email alert when configured conditions are met for records in your Salesforce Org:

1. Login to your Vault account.
2. From the dashboard, click **Setup** and then click on your **Salesforce Org**.

<figure><img src="../../../.gitbook/assets/image (141).png" alt="Setup page for selecting Salesforce Org in Vault" width="563"><figcaption><p>Selecting Salesforce Org from Setup</p></figcaption></figure>

3. Navigate to the **Alerts** tab and click **Add Alert Rules**.

<figure><img src="../../../.gitbook/assets/image (142).png" alt="Add Alert Rules button under Alerts tab" width="563"><figcaption><p>Adding alert rules</p></figcaption></figure>

4. On the **Add Alert** page, enter a **Rule Name**.

<figure><img src="../../../.gitbook/assets/image (143).png" alt="Entering rule name for alert" width="560"><figcaption><p>Rule name entry</p></figcaption></figure>

5. Choose the category: **metadata** or **data**.
   * **Data:** Select up to 10 **object(s)** from your [Salesforce Org](registering-salesforce-org/) and define the **alert threshold value**. Email notification triggers when this value is met.

<figure><img src="../../../.gitbook/assets/image (144).png" alt="Data alert configuration in Vault" width="554"><figcaption><p>Configuring data-based alerts</p></figcaption></figure>

* **Metadata:** Choose up to 10 [metadata members](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) and define the **alert value**.

<figure><img src="../../../.gitbook/assets/image (145).png" alt="Metadata alert configuration in Vault" width="559"><figcaption><p>Configuring metadata-based alerts</p></figcaption></figure>

* Choose alert criteria — added, modified, deleted, or all.
* Vault evaluates alert rules daily at **01:30 AM UTC**.
* Select alert recipients. The default is the Salesforce Org author in Vault. You can add more teammates:
  * Click **Edit** to choose additional recipients.
  * Click **Apply** after selection.

<figure><img src="../../../.gitbook/assets/image (146).png" alt="Selecting alert recipients in Vault" width="559"><figcaption><p>Selecting recipients</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (147).png" alt="Apply button to confirm recipient selection" width="563"><figcaption><p>Applying recipient selections</p></figcaption></figure>

6. On the **Add Alert** page, review your configuration and click **Submit**.

<figure><img src="../../../.gitbook/assets/image (148).png" alt="Submit alert configuration in Vault" width="558"><figcaption><p>Submit the alert</p></figcaption></figure>

7. The new alert appears under **Alert Rules** in the **Alerts** tab.
8. Triggered alerts display under the **Alert History** tab.

### Editing Alerts <a href="#editing-alerts" id="editing-alerts"></a>

To modify an existing alert:

1. From the **Setup** Console, choose your **Salesforce Org** and click **Alerts**.
2. In **Alert Rules**, locate the alert and click the **Edit** icon.
3. In the **Edit Alert** window, apply necessary changes and click **Submit**.

<figure><img src="../../../.gitbook/assets/image (149).png" alt="Editing an alert rule in Vault" width="563"><figcaption><p>Editing an alert</p></figcaption></figure>

### Deleting Alerts <a href="#deleting-alerts" id="deleting-alerts"></a>

To delete an alert:

1. From the **Setup** Console, choose your **Salesforce Org** and click **Alerts**.
2. In **Alert Rules**, locate the alert and click the **Delete** icon.

<figure><img src="../../../.gitbook/assets/image (150).png" alt="Deleting an alert rule in Vault" width="563"><figcaption><p>Deleting an alert</p></figcaption></figure>
