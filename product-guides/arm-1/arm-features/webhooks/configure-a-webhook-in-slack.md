# Configure a Webhook in Slack

1. Log in to your **Slack** account.
2. Navigate to [https://api.slack.com/](https://api.slack.com/)
3. Click **Create an app**.

<figure><img src="../../../../.gitbook/assets/image (1018).png" alt="Slack API homepage with Create an app button highlighted" width="527"><figcaption></figcaption></figure>

4. On the **Create an app** screen, click **From scratch**.

<figure><img src="../../../../.gitbook/assets/image (1019).png" alt="Slack app creation screen with From scratch option selected" width="443"><figcaption></figcaption></figure>

5. Enter an **App Name**, choose a **Workspace** from the dropdown, and click **Create App**.

<figure><img src="../../../../.gitbook/assets/image (1020).png" alt="Slack app naming and workspace selection screen" width="441"><figcaption></figcaption></figure>

6. In the app settings, click **Incoming Webhooks** under **Features** or **Add features and functionality**.

<figure><img src="../../../../.gitbook/assets/image (1021).png" alt="Slack app features page with Incoming Webhooks highlighted" width="563"><figcaption></figcaption></figure>

7. Activate **Incoming Webhooks** by toggling the switch from disabled to enabled.

<figure><img src="../../../../.gitbook/assets/image (1022).png" alt="Toggle switch in disabled state"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1023).png" alt="Toggle switch in enabled state"><figcaption></figcaption></figure>

8. Scroll down and click **Add New Webhook to Workspace**.

<figure><img src="../../../../.gitbook/assets/image (1024).png" alt="Add new webhook to workspace button in Slack app configuration" width="458"><figcaption></figcaption></figure>

9. Choose the **channel** where notifications should be sent and click **Allow**.

<figure><img src="../../../../.gitbook/assets/image (1025).png" alt="Slack channel selection screen for webhook integration" width="352"><figcaption></figcaption></figure>

10. After authorization, you'll return to the previous screen. Scroll down and click **Copy** to get the webhook URL.

<figure><img src="../../../../.gitbook/assets/image (1026).png" alt="Slack webhook URL section with Copy button" width="461"><figcaption></figcaption></figure>

The webhook URL can be reused or deleted from this section in Slack.

11. Finally, integrate your Slack webhook URL with ARM. For more guidance, refer to [this configuration guide](../../../arm/troubleshoot/how-tos/configure-mail-server-settings.md).
