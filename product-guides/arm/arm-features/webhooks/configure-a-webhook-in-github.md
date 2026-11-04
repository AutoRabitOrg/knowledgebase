# Configure a Webhook in GitHub

{% hint style="info" %}
After the 25.3.9 release, the structure of the webhook payload URL was updated. Customers need to update the webhook URL in the repository settings of their remote repo. Some customers are still using the old webhook URL containing **autorabitrest**, which should now be replaced with api.

Example:

Old URL: [https://na25.autorabit.com/**autorabitrest/**&#x77;ebhook/triggerSCMPushrequest](https://na25.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest)

Updated URL:[ ](https://na25.autorabit.com/api/webhook/v2/%3COrgName%3E/trigger-scm-push-request)[https://na25.autorabit.com/api/webhook/v2/\<OrgName>/trigger-scm-push-request](https://na25.autorabit.com/api/webhook/v2/%3COrgName%3E/trigger-scm-push-request)

Unless you update the Payload URL, you might face pull request/trigger build-on-commit jobs triggering.
{% endhint %}

## A. Create a Webhook API Token from ARM

Follow the steps below to create a webhook API token in ARM:

1. Log in to ARM.
2. Navigate to the **Admin** section and select **API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (3479).png" alt=""><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Add a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (3480).png" alt=""><figcaption></figcaption></figure>

8. Your API token is now created.

## B. Create Webhook with Authentication on GitHub

Webhooks allow external services to receive notifications about repository events. GitHub sends a POST request to the configured URL when those events occur.

### Steps to Configure:

1. Go to [https://github.com/login](https://github.com/login) and log in.
2. Open your target repository.

<figure><img src="../../../../.gitbook/assets/image (3483).png" alt=""><figcaption></figcaption></figure>

3. Click **Settings** in the right panel.

<figure><img src="../../../../.gitbook/assets/image (3484).png" alt=""><figcaption></figcaption></figure>

4. In the left menu, click **Webhooks & Services**, then **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (3485).png" alt=""><figcaption></figcaption></figure>

5. In the **Payload URL**, enter the webhook endpoint:

<figure><img src="../../../../.gitbook/assets/image (3486).png" alt=""><figcaption></figcaption></figure>

6. Enter the **Secret Key** from ARM’s API token.

<figure><img src="../../../../.gitbook/assets/image (3487).png" alt=""><figcaption></figcaption></figure>

7. Set **Content Type** to `application/json`.

<figure><img src="../../../../.gitbook/assets/image (3488).png" alt=""><figcaption></figcaption></figure>

8. Choose **Just the push events**.
9. Click **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (3489).png" alt=""><figcaption></figcaption></figure>

10. To trigger webhooks for pull requests, select **Let me select individual events** and check **Pull requests**.

<figure><img src="../../../../.gitbook/assets/image (3490).png" alt=""><figcaption></figcaption></figure>

11. Click **Add webhook** to finalize.

## Smart Commits

Smart Commits allow linking commits to ALM stories using custom comment patterns. For example:

<figure><img src="../../../../.gitbook/assets/image (3491).png" alt=""><figcaption></figcaption></figure>

To configure a webhook in your repository:

* Enable the **Enable auto update on webhook** checkbox to reveal the webhook URL.
* For more repository-specific instructions, refer to the [Webhook Configuration Guide](file://product-guides/arm/arm-features/webhooks).
* You may also choose to [Sync External Smart Commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

## For Enterprise Customers

Use the following endpoints for enterprise-specific integrations: /api/webhook/v2//enterprise/trigger-scm-push-request /api/webhook/v2//enterprise/sync-alm-commits
