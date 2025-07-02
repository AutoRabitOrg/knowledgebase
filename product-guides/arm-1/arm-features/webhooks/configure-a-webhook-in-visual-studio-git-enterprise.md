# Configure a webhook in Visual Studio GIT Enterprise

## A. Create a Webhook API Token from ARM

1. Log in to ARM.
2. Navigate to **Admin Section > API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (1000).png" alt="API Token creation screen in ARM"><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Enter a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (1001).png" alt="ARM webhook API token created confirmation screen"><figcaption></figcaption></figure>

8. Your webhook API token is now created.

***

## B. Create a Webhook with Authentication on Visual Studio Git

1. Log in to your Microsoft Visual Studio Git account.
2. Navigate to the project’s **Service Hooks** page:\
   `https://{orgName}/{projectname}/settings/serviceHooks`

<figure><img src="../../../../.gitbook/assets/image (1002).png" alt="Service Hooks tab in Visual Studio Git settings"><figcaption></figcaption></figure>

3. Click **Create Subscription**.
4. The wizard will list all services available for integration.

<figure><img src="../../../../.gitbook/assets/image (1003).png" alt="Integration services selection wizard" width="563"><figcaption></figcaption></figure>

5. Click **Next** to view a list of trigger events. Select a trigger and set filters as needed.

<figure><img src="../../../../.gitbook/assets/image (1004).png" alt="List of webhook trigger events in Visual Studio Git"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1005).png" alt="Filter configuration options for webhook events"><figcaption></figcaption></figure>

6. Enter the **Payload URL**, which is the endpoint to receive webhook POST requests. Use the URL format:

Example:\
[https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

7. Configure **Basic Authentication**:

* **Username:** Your AutoRABIT login username
* **Password:** Webhook API Token from ARM

<figure><img src="../../../../.gitbook/assets/image (1006).png" alt="Authentication setup for webhook in Visual Studio Git"><figcaption></figcaption></figure>

8. Re-enter your AutoRABIT username and API token to authenticate.

{% hint style="info" %}
**Note:** If you wish to trigger events such as _Pull Request_ or _Pull Request Updated_, use the same URL and credentials as configured above.
{% endhint %}

9. Confirm your settings, test the subscription, and finish the wizard.

<figure><img src="../../../../.gitbook/assets/image (1007).png" alt="Service hook test and confirmation screen" width="563"><figcaption></figcaption></figure>

10. Click **Finish**. The new webhook will be listed under **Service Hooks**.

<figure><img src="../../../../.gitbook/assets/image (1008).png" alt="List of active service hooks in Visual Studio Git"><figcaption></figcaption></figure>

11. After a build is triggered via webhook and completes successfully, refresh the tab to verify success. Use the webhook history to review trigger events and results.

***

## Smart Commits

Define a pattern to associate commits with ALM stories.\
Example:

<figure><img src="../../../../.gitbook/assets/image (1009).png" alt="Smart commit pattern configuration screen" width="563"><figcaption></figcaption></figure>

To configure a webhook in your repository:

* Enable the **auto update on webhook** checkbox to display the required URL.
* For repository-specific instructions, refer to the [Webhook Guide](file://product-guides/arm/arm-features/webhooks).
* To sync external smart commits, see the [Version Control Repositories Summary](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

***

## For Enterprise Customers

Use the following endpoints for enterprise environments: /api/webhook/v2//enterprise/trigger-scm-push-request /api/webhook/v2//enterprise/sync-alm-commits
