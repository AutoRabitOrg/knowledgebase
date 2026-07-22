# Configure a Webhook in Visual Studio GIT

{% hint style="info" %}
After the 25.3.9 release, the structure of the webhook payload URL was updated. Customers need to update the webhook URL in the repository settings of their remote repo. Some customers are still using the old webhook URL containing **autorabitrest**, which should now be replaced with api.

Example:

Old URL: [https://na25.autorabit.com/**autorabitrest/**&#x77;ebhook/triggerSCMPushrequest](https://na25.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest)

Updated URL: [https://na25.autorabit.com/api/webhook/v2/\<OrgName>/trigger-scm-push-request](https://na25.autorabit.com/api/webhook/v2/%3COrgName%3E/trigger-scm-push-request)

Unless you update the Payload URL, you might face pull request/trigger build-on-commit jobs triggering.
{% endhint %}

## A. Create a Webhook API Token from ARM

1. Log in to ARM.
2. Navigate to **Admin Section > API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../../.gitbook/assets/image (991).png" alt="API Token creation screen in ARM"><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Enter a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../../.gitbook/assets/image (992).png" alt="Webhook API token details input screen in ARM"><figcaption></figcaption></figure>

8. Your webhook API token is now created.

***

## B. Create a Webhook with Authentication in Visual Studio Git

1. Log in to your Microsoft Visual Studio Git account.
2. Navigate to the project’s **Service Hooks** page:

<figure><img src="../../../../../.gitbook/assets/image (993).png" alt="Service Hooks settings page in Visual Studio Git"><figcaption></figcaption></figure>

3. Click **Create Subscription**.
4. The wizard will display a list of available services for integration.

<figure><img src="../../../../../.gitbook/assets/image (994).png" alt="Integration service selection wizard in Visual Studio Git" width="563"><figcaption></figcaption></figure>

5. Click **Next** to select an event trigger and optionally configure filters.

<figure><img src="../../../../../.gitbook/assets/image (995).png" alt="Trigger events configuration screen"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (996).png" alt="Additional filters screen for webhook trigger events"><figcaption></figcaption></figure>

6. Enter the **Payload URL** to which webhook POST requests will be sent. Use the format:

Example:\
[https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

7. Configure **Basic Authentication**:

* **Username:** Your ARM login username
* **Password:** Webhook API Token generated from ARM

<figure><img src="../../../../../.gitbook/assets/image (997).png" alt="Basic authentication fields in webhook configuration screen"><figcaption></figcaption></figure>

8. Re-enter your AutoRABIT username and webhook token to complete authentication.

{% hint style="info" %}
**Note:** For events like _Pull Request Created_ or _Pull Request Updated_, use the same URL and credentials.
{% endhint %}

9. Review the configuration, test the subscription, and complete the setup.

<figure><img src="../../../../../.gitbook/assets/image (998).png" alt="Test and confirm webhook subscription setup" width="563"><figcaption></figcaption></figure>

10. Click **Finish**. The webhook will now appear in the **Service Hooks** tab.

<figure><img src="../../../../../.gitbook/assets/image (999).png" alt="Service Hooks tab showing configured webhook in Visual Studio Git"><figcaption></figcaption></figure>

11. Once triggered, verify webhook success from the service hook tab. You can also view webhook history to see trigger count and outcomes.

***

## Smart Commits

Use custom commit message patterns to link commits to ALM stories.\
Example:

<figure><img src="../../../../../.gitbook/assets/image (990).png" alt="Smart commit configuration in Visual Studio Git" width="563"><figcaption></figcaption></figure>

To reveal the webhook configuration URL:

* Enable the **auto update on webhook** checkbox.

For additional help, refer to:

* [Webhook Setup Guide](file://product-guides/arm/arm-features/webhooks)
* [Sync External Smart Commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary)

***

## For Enterprise Customers

Use these endpoints for enterprise configuration: /api/webhook/v2//enterprise/trigger-scm-push-request /api/webhook/v2//enterprise/sync-alm-commits
