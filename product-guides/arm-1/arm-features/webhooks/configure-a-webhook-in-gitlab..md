# Configure a Webhook in GitLab

## A. Create a Webhook API Token from ARM

1. Log in to ARM.
2. Navigate to **Admin > API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (974).png" alt=""><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Add a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (975).png" alt=""><figcaption></figcaption></figure>

8. Your API token is now created.

## B. Create a Webhook with Authentication on GitLab

1. Log in to your GitLab account and select the target repository.

<figure><img src="../../../../.gitbook/assets/image (976).png" alt=""><figcaption></figcaption></figure>

2. Go to **Settings > Integrations**.

<figure><img src="../../../../.gitbook/assets/image (977).png" alt=""><figcaption></figcaption></figure>

3. In the **URL** field, enter the webhook endpoint:

For example:\
[https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

<figure><img src="../../../../.gitbook/assets/image (978).png" alt=""><figcaption></figcaption></figure>

4. Complete the configuration and click **Add Webhook**.

## Smart Commits

Define the pattern used to extract ALM-related information from commit messages. For example:

<figure><img src="../../../../.gitbook/assets/image (979).png" alt=""><figcaption></figcaption></figure>

To enable automatic updates via webhook:

* Check the **Enable auto update on webhook** option.
* This will display the required webhook URL for use in repository settings.

For more detailed setup across repositories, refer to the [Webhook Configuration Guide](file://product-guides/arm/arm-features/webhooks).\
To integrate with external Smart Commit systems, see the [Version Control Repositories Summary](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

## For Enterprise Customers

Use the following endpoints for enterprise-specific configurations: /api/webhook/v2//enterprise/trigger-scm-push-request /api/webhook/v2//enterprise/sync-alm-commits
