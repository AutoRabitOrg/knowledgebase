---
description: The following documentation is specific to Bitbucket Enterprise customers.
---

# Configure a Webhook in Bitbucket Enterprise

{% hint style="info" %}
As of 9 September 2025, app username and passwords have been deprecated as a type of authentication method. However, as of 9 June 2026, all existing app passwords will be disabled. Users are required to create API tokens and migrate this function prior to the deadline to avoid disruptions: [https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/).
{% endhint %}

{% hint style="info" %}
After the 25.3.9 release, the structure of the webhook payload URL was updated. Customers need to update the webhook URL in the repository settings of their remote repo. Some customers are still using the old webhook URL containing **autorabitrest**, which should now be replaced with api.

Example:

Old URL: [https://na25.autorabit.com/**autorabitrest/**&#x77;ebhook/triggerSCMPushrequest](https://na25.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest)

Updated URL: [https://na25.autorabit.com/api/webhook/v2/\<OrgName>/trigger-scm-push-request](https://na25.autorabit.com/api/webhook/v2/%3COrgName%3E/trigger-scm-push-request)

Unless you update the Payload URL, you might face pull request/trigger build-on-commit jobs triggering.
{% endhint %}

## A. Create a Webhook API Token in ARM

1. Log in to ARM.
2. Navigate to **Admin Section > API Token**.
3. Click **Create API Token**.

<figure><img src="../../../../.gitbook/assets/image (985).png" alt="Create API Token screen in ARM"><figcaption></figcaption></figure>

4. Enter a **Token Name**.
5. Select **Type** as **webhook**.
6. (Optional) Add a **Description**.
7. Click **Create Option**.

<figure><img src="../../../../.gitbook/assets/image (986).png" alt="Webhook token details input screen in ARM"><figcaption></figcaption></figure>

8. Your webhook API token is now created.

***

## B. Create a Webhook with Authentication in Bitbucket

1. Log in to your **Bitbucket** account and open the target repository.
2. Go to **Settings** and select [**Webhooks**](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/webhooks).

<figure><img src="../../../../.gitbook/assets/image (988).png" alt="Bitbucket Webhooks configuration section"><figcaption></figcaption></figure>

3. In the webhook configuration form, use the following URL formats:
   *   For SCM push events:

       ```
       https://login.autorabit.com/api/webhook/v2/<orgname>/enterprise/trigger-scm-push-request
       ```
   *   For ALM commit syncs:

       ```
       https://login.autorabit.com/api/webhook/v2/<orgname>/enterprise/sync-alm-commits
       ```
4. Enter the webhook details and click **Save**.

***

## Smart Commits

Configure commit message patterns that associate commits with ALM stories.\
Example:

<figure><img src="../../../../.gitbook/assets/image (989).png" alt="Smart commit example and configuration options" width="563"><figcaption></figcaption></figure>

To configure a webhook:

* Enable the **auto update on webhook** checkbox to display the webhook URL.
* For setup in other repository types, refer to the [Webhook Guide](file://product-guides/arm/arm-features/webhooks).
* To integrate with external smart commit systems, see the [Version Control Repositories Summary](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).
