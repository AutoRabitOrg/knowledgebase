# Notifications (Mail Server Settings)

{% hint style="info" %}
**Important Note**: This article is for the **'Org Administrator'** in particular. The actions discussed in the article will not be available to the General Users. &#x20;
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

You can use the mail server settings in this article to manually set up your email to send and receive an email with an iCloud email account. AutoRABIT requires mail server settings to send the AutoRABIT notification emails for events like build failures, build success, deployment failure, merge reports, etc.&#x20;

Begin the process by hovering your mouse over the **Admin** module and selecting the option: **Notifications**.

<figure><img src="../../../../.gitbook/assets/image (754).png" alt="" width="235"><figcaption></figcaption></figure>

You’ll then be presented with a screen divided into **Mail Settings,** **Send a Test Mail,** and **Teams/Slack Settings** sections.&#x20;

#### Mail Settings <a href="#mail-settings" id="mail-settings"></a>

To set up a mail client it’s necessary to configure the server that will take care of the delivery of your emails. And here’s the standard procedure of mail configuration and adding the right parameters in the **Mail Settings** section:

<figure><img src="../../../../.gitbook/assets/image (755).png" alt="" width="536"><figcaption></figcaption></figure>

Fill in the required details as listed below (mandatory fields are marked with an asterisk (\*) mark.&#x20;

1. **Host Name:** Your incoming mail server name. _Ex- smtp.office365.com_
2. **Port:** The port number your incoming mail server uses. _Ex- Port 25_
3. **User Name:** The email address you want to set up. _Ex- yourusername@autorabit.com_
4. **Password:** The password associated with your email account.
5. **Protocol:** The protocol to manage the transmission and outgoing mail over the internet. And, is your email encrypted using SSL? If YES, then select the **SSL/TLS if available** checkbox.
6. **Email From:** Enter the email addresses from which you want to receive email notifications while configuring the mail server.&#x20;
7. Select the **Email Notifications** checkbox to receive notification alerts.
8. **Custom Email Template:** AutoRABIT comes with its default email template styles but you can also create your own. Simply enable the **Custom Email Template** field and add your logo at the top or bottom of the page. You can add footer text too. Once you're happy with your template, save it.
9. To clear all the data in the **Mail Settings** section and fill in the fields once again, you can use the **Reset** button.

<figure><img src="../../../../.gitbook/assets/image (756).png" alt="" width="563"><figcaption></figcaption></figure>

How to reset your Mail preferences?You won't be able to switch back to the default AutoRABIT mail preferences once you have configured your own email template. To switch back to the default email style, you can email us at [support@autorabit.com](mailto:%20support@autorabit.com) and we can get it done for you.

#### Send a Test Mail <a href="#send-a-test-mail" id="send-a-test-mail"></a>

Before using your customized email style, be sure to preview it once to be sure everything is displaying correctly. Simply enter your email address in the **Recipient** field and click on the **Test** button to receive a test mail notification. Sample email notification attached.

<figure><img src="../../../../.gitbook/assets/image (757).png" alt=""><figcaption></figcaption></figure>

#### Teams/Slack Settings <a href="#teamsslack-settings" id="teamsslack-settings"></a>

When an event is triggered in ARM, email notifications are sent to the selected individuals. If you want to send notifications for particular events to an entire group within your organization through **Teams** or **Slack**, then integrate your Teams or Slack application with ARM using the respective **Webhook Integration URL**. For more information on configuring a webhook on **Teams**, click [HERE](../../../arm/arm-features/automation-and-ci/webhooks/configure-a-webhook-in-teams.md). For **Slack**, click [HERE](../../../arm/arm-features/automation-and-ci/webhooks/configure-a-webhook-in-slack.md).

1. Select either **Teams** or **Slack** as per your organization's requirements.
2. Enter a **Channel Name** and the **Webhook Integration URL**.&#x20;
3. Click on **Test Connection**. A **Test connection Successful** notification will be displayed.

<figure><img src="../../../../.gitbook/assets/image (758).png" alt=""><figcaption></figcaption></figure>

4. If the test connection fails, an error message will be displayed. Check and re-enter the correct webhook URL.

<figure><img src="../../../../.gitbook/assets/image (759).png" alt=""><figcaption></figcaption></figure>

5. After a successful test connection, click **Save**.

{% hint style="info" %}
**Important Note:** The first channel that you add is automatically configured to all the events by default. To remove the channel from any notification type, click on the![](<../../../../.gitbook/assets/image (760).png>)icon. Channels added after that will have to be configured to events manually.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (761).png" alt=""><figcaption></figcaption></figure>

6. To add another channel, click on the (**+**) icon. You can add up to **10** channels.

<figure><img src="../../../../.gitbook/assets/image (762).png" alt=""><figcaption></figcaption></figure>

7. To delete a channel, click on the (**x**) icon and then click **YES** on the confirmation message.

**Notification Configuration**

This section is a guide to configuring the channels to the notification types. You can select which group(s) on Teams or Slack should get a notification when a particular event is triggered.&#x20;

<figure><img src="../../../../.gitbook/assets/image (763).png" alt="" width="563"><figcaption></figcaption></figure>

1. Select the checkbox for the **Notification Type** that you want to configure.
2. Click in the **Selected channels** field to display a list of configured channels.

<figure><img src="../../../../.gitbook/assets/image (764).png" alt=""><figcaption></figcaption></figure>

3. Click the channel that you want to send the notification to when this event is triggered. You can select up to five channels for each notification type, which means that you can select as many channels as you have configured.
4. You can select multiple checkboxes for numerous notification types and select the channels to which you want to send notifications for each event.
5. Click **Save**. All the selected **Notification types** will be saved simultaneously.&#x20;
6. When an event is triggered in ARM, the configured channels will receive a notification.\
   The image below is an example of what these notifications look like on Teams.

<figure><img src="../../../../.gitbook/assets/image (765).png" alt=""><figcaption></figcaption></figure>

## Email Admin Settings

### Purpose

This guide walks AutoRABIT administrators through configuring outbound **email** notifications and managing restricted recipient lists. Use it when onboarding a new org or revisiting your notification strategy.

***

### 1  Accessing the Page

1. Sign in with an account that has **Admin** privileges.
2. In the global navigation bar choose **Admin › Notifications**.
3. The page opens with **three** stacked configuration sections:
   * **Mail Settings** (SMTP)
   * **Send a Test Email**
   * **Restricted Emails**

***

### 2  Mail Settings (SMTP)

| Field                     | Description                                                | Typical Examples               |
| ------------------------- | ---------------------------------------------------------- | ------------------------------ |
| **Host Name**             | FQDN or IP address of your SMTP server.                    | `smtp.company.com`             |
| **Port**                  | Network port the server listens on.                        | `25`, `465` (SSL), `587` (TLS) |
| **User Name**             | Service account allowed to relay mail.                     | `notifications@company.com`    |
| **Password**              | Password or app‑specific token for the above user.         | _••••••_                       |
| **Protocol**              | Transport security: `SMTP`, `SMTP (SSL)`, or `SMTP (TLS)`. | `SMTP (TLS)`                   |
| **Email From**            | The **From:** address recipients will see.                 | `noreply@company.com`          |
| **Email Notifications**   | Toggle **Enabled / Disabled** globally.                    | _Enabled_                      |
| **Custom Email Template** | Toggle to enable org‑specific templates.                   | _Enabled_                      |

> **Remember:** Click **Save** (upper right) after any change. Settings apply immediately to future emails.

#### 2.1  Send a Test Email

1. Enter one or more addresses (comma‑separated) in **Recipient**.
2. Click **Test**.
3. Confirm delivery in the inbox; if nothing arrives, re‑check credentials, firewall rules, or SPF/DKIM settings.

***

### 3  Restricted Emails

Block specific addresses from ever receiving system mail (e.g., DLs, test accounts, ex‑employees).

* Type/paste an address and press **Enter** to add it.
* Click the **×** in a pill to remove.
* **Delete All** wipes the list.
* Click **Save** afterward.

***

### 4  Notification Configuration Matrix

Map **system events** to **delivery channels**.

| Column                | Purpose                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------ |
| **Notification Type** | Event emitted by AutoRABIT (e.g., _EZ‑Commit Gated Check‑in_, _Merge Request_, _PRD Deploy – Custom_). |
| **Select Channel**    | Dropdown containing **Email** or _None_.                                                               |

**Steps**

1. Tick the checkbox beside each event.
2. Choose **Email** or _None_ in the same row.
3. Scroll and click the main **Save** button.

> **Tip:** Keep noise low by selecting only critical events.

***

### 5  Best Practices & Troubleshooting

| Issue                      | Resolution                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Test email fails           | Verify SMTP host/port, credentials, firewall, and that the **From** address is authorized.          |
| Emails marked as spam      | Use a real domain and configure SPF/DKIM/DMARC.                                                     |
| No notifications delivered | Ensure **Email Notifications** toggle is _Enabled_, event checkboxes are ticked, and page is saved. |

&#x20;
