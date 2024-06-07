# Slack integration with Zapier

Zapier is a service that allows you to easily manage webhooks between apps. With Zapier, you can get notifications on your Slack channels when a scan is run.

{% hint style="info" %}
**Note:** This can be done at an Organisation level or a Project level. At the Organisation level, all scans will trigger the webhook. To choose this, use the **Administration > Webhooks** menu, either from the Organisation page or a Project overview page.
{% endhint %}

1. First, sign up to Zapier and click **Make a Zap**.
2. Use the App search bar to find **Webhooks by Zapier** and then select it. Choose **Catch Hook** as the trigger event and then click on **Continue**.

<figure><img src="../../../../.gitbook/assets/image (534).png" alt="" width="503"><figcaption></figcaption></figure>

3. You will be provided with a Custom **Webhook URL**, copy this URL.
4. Now login into CodeScan Cloud and go to **Administration > Webhooks** menu at either the Organisation or Project level (see note above).
5. Create a **new webhook** using the custom URL and give it a name you will remember.
6. Now **run** a **scan** to trigger the webhook. This will allow you to find the the webhook in zapier and customise the output as we'll see soon.
7. Next, search for **Slack** and select it. Choose the **Action Event** that you want.

<figure><img src="../../../../.gitbook/assets/image (533).png" alt="" width="506"><figcaption></figcaption></figure>

8. Click **CONTINUE** and add your Slack Account. Click **CONTINUE**.
9. Customise the message to your liking using the webhook fields, your own text, and Zapier's formatting options.

<figure><img src="../../../../.gitbook/assets/image (532).png" alt="" width="505"><figcaption></figcaption></figure>

10. Click **CONTINUE**, then send a test to Slack.

<figure><img src="../../../../.gitbook/assets/image (531).png" alt=""><figcaption></figcaption></figure>
