---
description: The following documentation is specific to Bitbucket Enterprise customers.
---

# Configure a Webhook in Bitbucket Enterprise

## A. **Create a Webhook API token in ARM**

1. Log in to ARM.
2. Click on **Admin Section -> API Token**.
3. Click on **Create API Token**.

<figure><img src="../../../../../.gitbook/assets/image (985).png" alt=""><figcaption></figcaption></figure>

4. Enter the token name.
5. Select Type as “webhook.”
6. Enter Description if required.
7. Click on **Create Option**.

<figure><img src="../../../../../.gitbook/assets/image (986).png" alt=""><figcaption></figcaption></figure>

8. Your New API Token is created

## B. Create a Webhook with authentication in Bitbucket&#x20;

1. Log in to your Bitbucket account and select a Repository in which you want to configure a Webhook.
2. Click **Settings** and select [Webhooks](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/webhooks).



<figure><img src="../../../../../.gitbook/assets/image (988).png" alt=""><figcaption></figcaption></figure>

3. In the webhook configuration section, enter the following URL format: \
   `<instance_url>/api/webhook/v2/<orgname>/enterprise/trigger-scm-push-request` \
   \
   For example, if the instance is https://login.autorabit.com, then the payload URL would be: https://login.autorabit.com/api/webhook/v2/autorabit.com/enterprise/trigger-scm-push-request\
   \
   For ALM commits, use the following format: \
   `<instance_url>/api/webhook/v2/<orgname>/enterprise/sync-alm-commits`
4. Fill in the details and click Save.

## **Smart Commits**

In this section, you can select the pattern used to read the comment in a revision associated with your ALM story. For example, _'git commit m \[project123] # add README file into the project'._

<figure><img src="../../../../../.gitbook/assets/image (989).png" alt="" width="563"><figcaption></figcaption></figure>

If you want to configure a webhook in your repository, select the 'Enable auto update on webhook' checkbox to reveal the URL required for the webhook settings. For more information on how to configure a webhook in different repositories, refer [HERE](file://product-guides/arm/arm-features/webhooks). You can also choose to [sync external smart commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).
