# Notifications (Mail Server Settings)

{% hint style="info" %}
**Important Note**: This article is for the **'Org Administrator'** in particular. The actions discussed in the article will not be available to the General Users. &#x20;
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

You can use the mail server settings in this article to manually set up your email to send and receive an email with an iCloud email account. AutoRABIT requires mail server settings to send the AutoRABIT notification emails for events like build failures, build success, deployment failure, merge reports, etc.&#x20;

Begin the process by hovering your mouse over the **Admin** module and selecting the option: **Notifications**.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662654752785.png" alt=""><figcaption></figcaption></figure>

You’ll then be presented with a screen divided into **Mail Settings,** **Send a Test Mail,** and **Teams/Slack Settings** sections.&#x20;

#### Mail Settings <a href="#mail-settings" id="mail-settings"></a>

To set up a mail client it’s necessary to configure the server that will take care of the delivery of your emails. And here’s the standard procedure of mail configuration and adding the right parameters in the **Mail Settings** section:\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662654855524.png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required details as listed below (mandatory fields are marked with an asterisk (\*) mark.&#x20;

1. **Host Name:** Your incoming mail server name. _Ex- smtp.office365.com_
2. **Port:** The port number your incoming mail server uses. _Ex- Port 25_
3. **User Name:** The email address you want to set up. _Ex- yourusername@autorabit.com_
4. **Password:** The password associated with your email account.
5. **Protocol:** The protocol to manage the transmission and outgoing mail over the internet. And, is your email encrypted using SSL? If YES, then select the **SSL/TLS if available** checkbox.
6. **Email From:** Enter the email addresses from which you want to receive email notifications while configuring the mail server.&#x20;
7. Select the **Email Notifications** checkbox to receive notification alerts.
8. **Custom Email Template:** AutoRABIT comes with its default email template styles but you can also create your own. Simply enable the **Custom Email Template** field and add your logo at the top or bottom of the page. You can add footer text too. Once you're happy with your template, save it.
9.  To clear all the data in the **Mail Settings** section and fill in the fields once again, you can use the **Reset** button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662655171009.png" alt="" width="563"><figcaption></figcaption></figure>

How to reset your Mail preferences?You won't be able to switch back to the default AutoRABIT mail preferences once you have configured your own email template. To switch back to the default email style, you can email us at [support@autorabit.com](mailto:%20support@autorabit.com) and we can get it done for you.

#### Send a Test Mail <a href="#send-a-test-mail" id="send-a-test-mail"></a>

Before using your customized email style, be sure to preview it once to be sure everything is displaying correctly. Simply enter your email address in the **Recipient** field and click on the **Test** button to receive a test mail notification. Sample email notification attached.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662655305998.png" alt=""><figcaption></figcaption></figure>

#### Teams/Slack Settings <a href="#teamsslack-settings" id="teamsslack-settings"></a>

When an event is triggered in ARM, email notifications are sent to the selected individuals. If you want to send notifications for particular events to an entire group within your organization through **Teams** or **Slack**, then integrate your Teams or Slack application with ARM using the respective **Webhook Integration URL**. For more information on configuring a webhook on **Teams**, click [HERE](webhooks/configure-a-webhook-in-teams.md). For **Slack**, click [HERE](webhooks/configure-a-webhook-in-slack.md).

1. Select either **Teams** or **Slack** as per your organization's requirements.\

2. Enter a **Channel Name** and the **Webhook Integration URL**.&#x20;
3. Click on **Test Connection**. A **Test connection Successful** notification will be displayed.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662631251991.png" alt=""><figcaption></figcaption></figure>

\
If the test connection fails, an error message will be displayed. Check and re-enter the correct webhook URL.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662631127875.png" alt=""><figcaption></figcaption></figure>

1. After a successful test connection, click **Save**.\


{% hint style="info" %}
**Important Note:** The first channel that you add is automatically configured to all the events by default. To remove the channel from any notification type, click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1663134872455.png) icon. Channels added after that will have to be configured to events manually.
{% endhint %}

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662631704201.png" alt=""><figcaption></figcaption></figure>

1.  To add another channel, click on the (**+**) icon. You can add up to **10** channels.\
    \


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662968596475.png" alt=""><figcaption></figcaption></figure>
2. To delete a channel, click on the (**x**) icon and then click **YES** on the confirmation message.

**Notification Configuration**

This section is a guide to configuring the channels to the notification types. You can select which group(s) on Teams or Slack should get a notification when a particular event is triggered.&#x20;

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662652799821.png)

1. Select the checkbox for the **Notification Type** that you want to configure.
2.  Click in the **Selected channels** field to display a list of configured channels.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662653039398.png" alt=""><figcaption></figcaption></figure>
3. Click the channel that you want to send the notification to when this event is triggered. You can select up to five channels for each notification type, which means that you can select as many channels as you have configured.
4. You can select multiple checkboxes for numerous notification types and select the channels to which you want to send notifications for each event.
5. Click **Save**. All the selected **Notification types** will be saved simultaneously.&#x20;
6.  When an event is triggered in ARM, the configured channels will receive a notification.\
    The image below is an example of what these notifications look like on Teams.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1662654062218.png" alt=""><figcaption></figcaption></figure>
