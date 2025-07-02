# Configure a Webhook in GitHub

## A. Create a Webhook API Token from ARM

Follow the steps below to create a webhook API token in ARM:

1. Log in to ARM.
2. Navigate to the **Admin** section and select **API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (940).png" alt=""><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Add a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (941).png" alt=""><figcaption></figcaption></figure>

8. Your API token is now created.

## B. Create Webhook with Authentication on GitHub

Webhooks allow external services to receive notifications about repository events. GitHub sends a POST request to the configured URL when those events occur.

### Steps to Configure:

1. Go to [https://github.com/login](https://github.com/login) and log in.
2. Open your target repository.

<figure><img src="../../../../.gitbook/assets/image (944).png" alt=""><figcaption></figcaption></figure>

3. Click **Settings** in the right panel.

<figure><img src="../../../../.gitbook/assets/image (945).png" alt=""><figcaption></figcaption></figure>

4. In the left menu, click **Webhooks & Services**, then **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (946).png" alt=""><figcaption></figcaption></figure>

5. In the **Payload URL**, enter the webhook endpoint:

<figure><img src="../../../../.gitbook/assets/image (947).png" alt=""><figcaption></figcaption></figure>

6. Enter the **Secret Key** from ARM’s API token.

<figure><img src="../../../../.gitbook/assets/image (948).png" alt=""><figcaption></figcaption></figure>

7. Set **Content Type** to `application/json`.

<figure><img src="../../../../.gitbook/assets/image (949).png" alt=""><figcaption></figcaption></figure>

8. Choose **Just the push events**.
9. Click **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (950).png" alt=""><figcaption></figcaption></figure>

10. To trigger webhooks for pull requests, select **Let me select individual events** and check **Pull requests**.

<figure><img src="../../../../.gitbook/assets/image (951).png" alt=""><figcaption></figcaption></figure>

11. Click **Add webhook** to finalize.

## Smart Commits

Smart Commits allow linking commits to ALM stories using custom comment patterns. For example:

<figure><img src="../../../../.gitbook/assets/image (952).png" alt=""><figcaption></figcaption></figure>

To configure a webhook in your repository:

* Enable the **Enable auto update on webhook** checkbox to reveal the webhook URL.
* For more repository-specific instructions, refer to the [Webhook Configuration Guide](file://product-guides/arm/arm-features/webhooks).
* You may also choose to [Sync External Smart Commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

## For Enterprise Customers

Use the following endpoints for enterprise-specific integrations: /api/webhook/v2//enterprise/trigger-scm-push-request /api/webhook/v2//enterprise/sync-alm-commits
