# Configure a Webhook in GitHub Enterprise

## A. Create a Webhook API Token from ARM

Follow these steps to create a webhook API token in ARM:

1. Log in to ARM.
2. Navigate to the **Admin** section and select **API Token**.
3. Click on **Create API Token**.

   ![API Token Creation](../../../../.gitbook/assets/image%20(953).png)

4. Enter a **Token Name**.
5. Set **Type** to **webhook**.
6. (Optional) Provide a **Description**.
7. Click on **Create Option**.

   ![Webhook Token Configuration](../../../../.gitbook/assets/image%20(954).png)

8. Your new API token is now created.

## B. Create Webhook with Authentication on GitHub

Webhooks notify external services when specific events occur. To configure a webhook in GitHub:

1. Sign in to [GitHub](https://github.com/login).
2. Navigate to the desired repository.
3. Click on **Settings** in the repository's menu.

   ![Repository Settings](../../../../.gitbook/assets/image%20(957).png)

4. In the left sidebar, click on **Webhooks**.
5. Click on **Add webhook**.

   ![Add Webhook](../../../../.gitbook/assets/image%20(958).png)

6. In the **Payload URL** field, enter:

# Configure a Webhook in GitHub Enterprise

## A. Create a Webhook API Token from ARM

Follow these steps to create a webhook API token in ARM:

1. Log in to ARM.
2. Navigate to the **Admin** section and select **API Token**.
3. Click on **Create API Token**.

   ![API Token Creation](../../../../.gitbook/assets/image%20(953).png)

4. Enter a **Token Name**.
5. Set **Type** to **webhook**.
6. (Optional) Provide a **Description**.
7. Click on **Create Option**.

   ![Webhook Token Configuration](../../../../.gitbook/assets/image%20(954).png)

8. Your new API token is now created.

## B. Create Webhook with Authentication on GitHub

Webhooks notify external services when specific events occur. To configure a webhook in GitHub:

1. Sign in to [GitHub](https://github.com/login).
2. Navigate to the desired repository.
3. Click on **Settings** in the repository's menu.

   ![Repository Settings](../../../../.gitbook/assets/image%20(957).png)

4. In the left sidebar, click on **Webhooks**.
5. Click on **Add webhook**.

   ![Add Webhook](../../../../.gitbook/assets/image%20(958).png)

6. In the **Payload URL** field, enter:

For example, if your instance is `https://login.autorabit.com` and your organization name is `autorabit.com`, the payload URL would be:

![Payload URL Configuration](../../../../.gitbook/assets/image%20(959).png)

7. In the **Secret** field, enter the API token generated from ARM.

![Secret Key Entry](../../../../.gitbook/assets/image%20(960).png)

8. Set **Content type** to **application/json**.

![Content Type Selection](../../../../.gitbook/assets/image%20(961).png)

9. Under **Which events would you like to trigger this webhook?**, select **Just the push event**.
10. Click **Add webhook**.

 ![Add Webhook Confirmation](../../../../.gitbook/assets/image%20(962).png)

11. To trigger the webhook on pull requests, select **Let me select individual events** and check **Pull requests**.

 ![Pull Request Event Selection](../../../../.gitbook/assets/image%20(963).png)

12. Click **Add webhook** to save the configuration.

## Smart Commits

Smart Commits allow you to associate Git commits with ALM stories using specific patterns. For example:


To configure Smart Commits:

- Select the **Enable auto update on webhook** checkbox to reveal the required webhook URL.
- For more information on configuring webhooks in different repositories, refer to the [Webhook Setup Guide](file://product-guides/arm/arm-features/webhooks).
- You can also choose to [sync external smart commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

![Smart Commit Configuration](../../../../.gitbook/assets/image%20(964).png)

## For Enterprise Customers

GitHub Enterprise users should raise a support ticket to [support@autorabit.com](mailto:support@autorabit.com) to have their repository URL added to the `webhookurls.properties` file.

Use the following endpoints for enterprise configurations:

/api/webhook/v2/<orgname>/enterprise/trigger-scm-push-request

/api/webhook/v2/<orgname>/enterprise/sync-alm-commits

