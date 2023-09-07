# Slack integration with Zapier

Zapier is a service that allows you to easily manage webhooks between apps. With Zapier, you can get notifications on your Slack channels when a scan is run.

Note:

This can be done at an Organisation level or a Project level. At the Organisation level, all scans will trigger the webhook. To choose this, use the **Administration > Webhooks** menu, either from the Organisation page or a Project overview page.

1. First, sign up to Zapier and click **Make a Zap**.
2. Use the App search bar to find **Webhooks by Zapier** and then select it. Choose **Catch Hook** as the trigger event and then click on **Continue**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(350\).png)
3. You will be provided with a Custom **Webhook URL**, copy this URL.
4. Now login into CodeScan Cloud and go to **Administration > Webhooks** menu at either the Organisation or Project level (see note above).
5. Create a **new webhook** using the custom URL and give it a name you will remember.
6. Now **run** a **scan** to trigger the webhook. This will allow you to find the the webhook in zapier and customise the output as we'll see soon.
7. Next, search for **Slack** and select it. Choose the **Action Event** that you want.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(351\).png)
8. Click **CONTINUE** and add your Slack Account. Click **CONTINUE**.
9. Customise the message to your liking using the webhook fields, your own text, and Zapier's formatting options.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(352\).png)
10. Click **CONTINUE**, then send a test to Slack.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(353\).png)
