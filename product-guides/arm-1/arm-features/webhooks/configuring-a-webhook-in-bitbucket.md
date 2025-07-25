# Configure a Webhook in Bitbucket

## Create a Webhook API Token from ARM

1. Log in to ARM.
2. Navigate to **Admin Section > API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (980).png" alt="API Token creation screen in ARM"><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Add a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (981).png" alt="Webhook token configuration form in ARM"><figcaption></figcaption></figure>

8. Your webhook API token is now created.

***

## Create a Webhook with Authentication in Bitbucket

1. Log in to your **Bitbucket** account and open the repository where you want to configure the webhook.

<figure><img src="../../../../.gitbook/assets/image (982).png" alt="Bitbucket repository interface with Webhook option" width="563"><figcaption></figcaption></figure>

2. Go to **Settings** and select [**Webhooks**](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/webhooks).
3. Enter the **Webhook URL** in the following format:

Example:\
[https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

<figure><img src="../../../../.gitbook/assets/image (983).png" alt="Webhook URL configuration in Bitbucket settings" width="563"><figcaption></figcaption></figure>

4. Complete the form and click **Save**.

***

## Smart Commits

Define patterns to associate Git commits with ALM stories.\
Example:

<figure><img src="../../../../.gitbook/assets/image (984).png" alt="Smart commit example and configuration interface" width="563"><figcaption></figcaption></figure>

To enable automatic webhook URL retrieval:

* Check the **Enable auto update on webhook** box.
* For guidance on other repositories, see the [Webhook Setup Guide](file://product-guides/arm/arm-features/webhooks).
* To sync with external ALM tools, refer to the [Smart Commit Integration Guide](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

***

## For Enterprise Customers

Use these endpoint URLs for enterprise configurations:

/api/webhook/v2//enterprise/trigger-scm-push-request

/api/webhook/v2//enterprise/sync-alm-commits
