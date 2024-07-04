# Configure a Webhook in GitHub Enterprise

## A. Create a Webhook API Token from ARM

Follow the instructions below to create a webhook API token from ARM.

1. Log in to ARM.
2. Click on the Admin section, then select '**API Token**.'
3. Click on '**Create API Token**.'

<figure><img src="../../../../.gitbook/assets/image (953).png" alt=""><figcaption></figcaption></figure>

4. Enter the token **name**.
5. Select Type as "**webhook**."
6. Enter a **description** if required.
7. Click on '**Create Option**.'

<figure><img src="../../../../.gitbook/assets/image (954).png" alt=""><figcaption></figcaption></figure>

8. Your new API token is created.

## B. Create Webhook with Authentication on GitHub

Webhooks allow external services to be notified when certain events happen. When the specified events happen, we’ll send a POST request to each of the URLs you provide.

1. Go to [https://github.com/login](https://github.com/login) and sign in to GitHub with your username and password.

<figure><img src="../../../../.gitbook/assets/image (955).png" alt="" width="272"><figcaption></figcaption></figure>

2. Select the related repository you own.

<figure><img src="../../../../.gitbook/assets/image (956).png" alt=""><figcaption></figcaption></figure>

3. Click on **'Settings'** on the right panel.

<figure><img src="../../../../.gitbook/assets/image (957).png" alt=""><figcaption></figcaption></figure>

4. Then click on **'Webhooks & Services'** on the left panel. Click on the '**Add WebHook'** Button.

<figure><img src="../../../../.gitbook/assets/image (958).png" alt=""><figcaption></figcaption></figure>

5. In the URL form field, paste the copied URL or enter the payload URL manually. The payload URL is the URL of the server that will receive the webhook POST requests. \
   **Payload URL:** \<instance\_url>/api/webhook/v2/\<orgname>/trigger-scm-push-request\
   **For example, using instance:** https://login.autorabit.com\
   **Payload URL:** [https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

<figure><img src="../../../../.gitbook/assets/image (959).png" alt=""><figcaption></figcaption></figure>

6. Enter the Secret Key generated in ARM as an API token.

<figure><img src="../../../../.gitbook/assets/image (960).png" alt=""><figcaption></figcaption></figure>

7. Select **'application/json'** as the content type. The **application/json** content type will deliver the JSON payload directly as the body of the POST request.

<figure><img src="../../../../.gitbook/assets/image (961).png" alt=""><figcaption></figcaption></figure>

8. Select **'Just the push events.'** Events are at the core of webhooks. These webhooks fire whenever a certain action is taken on the repository, which your server's payload URL intercepts and acts upon.
9. Click **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (962).png" alt="" width="563"><figcaption></figcaption></figure>

10. However, to trigger the webhook using pull request, you need to select **'Let me select individual events'** and select the **Pull requests** checkbox.

<figure><img src="../../../../.gitbook/assets/image (963).png" alt="" width="563"><figcaption></figcaption></figure>

11. Click on **Add webhook** to save the webhook.

## Smart Commits

In this section, you can select the pattern used to read the comment in a revision associated with your ALM story. For example, _'**git commit m \[project123] # add README file into the project**.'_

<figure><img src="../../../../.gitbook/assets/image (964).png" alt="" width="563"><figcaption></figcaption></figure>

If you want to configure a webhook in your repository, select the ‘**Enable auto update on webhook**’ checkbox to reveal the URL required for the webhook settings. For more information on how to configure a webhook in different repositories, refer [HERE](file://product-guides/arm/arm-features/webhooks). You can also choose to [sync external smart commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

## For Enterprise Customers

Also, as a one-time configuration, GitHub **enterprise** users should raise a support ticket to [support@autorabit.com](mailto:support@autorabit.com) to get their repo URL added to the “**webhookurls.properties”** file.

&#x20;/api/webhook/v2/\<orgname>/`enterprise`/trigger-scm-push-request

/api/webhook/v2/\<orgname>/`enterprise`/sync-alm-commits
