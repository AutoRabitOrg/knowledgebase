# Configure a Webhook in GitHub

Webhooks allow external services to be notified when certain events happen. When the specified events happen, we’ll send a POST request to each of the URLs you provide.

1. Go to [https://github.com/login](https://github.com/login) and sign in to GitHub with your username and password.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom1.png" alt=""><figcaption></figcaption></figure>

2. Select the related repository you own.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom21.png" alt=""><figcaption></figcaption></figure>

3. Click on **'Settings'** on the right panel.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom31.png" alt=""><figcaption></figcaption></figure>

4. Then click on **'Webhooks & Services'** on the left panel. Click on the '**Add WebHook'** Button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom41.png" alt=""><figcaption></figcaption></figure>

5. In the URL form field, paste the copied URL or enter the payload URL manually. The payload URL is the URL of the server that will receive the webhook POST requests.**Payload URL:** <_InstanceURL/autorabitrest/webhook/triggerSCMPushrequest_>

**For ex:** **Instance:** https://login.autorabit.com\
**Payload URL:** https://login.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom51.png" alt=""><figcaption></figcaption></figure>

6. Select **'application/json'** as the content type. The **application/json** content type will deliver the JSON payload directly as the body of the POST request.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom61.png" alt=""><figcaption></figcaption></figure>

7. Select **'Just the push events.'** Events are at the core of webhooks. These webhooks fire whenever a certain action is taken on the repository, which your server's payload URL intercepts and acts upon.
8. Click **Add Webhook**.

&#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom71.png" alt="" width="563"><figcaption></figcaption></figure>

9. However, to trigger the webhook using pull request, you need to select **'Let me select individual events'** and select the **Pull requests** checkbox.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGITHUBcustom81.png" alt="" width="375"><figcaption></figcaption></figure>

10. Click on **Add webhook** to save the webhook.
