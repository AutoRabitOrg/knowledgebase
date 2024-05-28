# Configuring a Webhook in Bitbucket Enterprise

## A. **Create a Webhook API token from ARM**

1. Log in to ARM.
2. Click on Admin Section -> API Token.
3. Click on Create API Token.

<figure><img src="../../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Enter the token name.
5. Select Type as “webhook.”
6. Enter Description if required.
7. Click on Create Option.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Your New API Token is created

***

## B. Create a webhook with authentication in Bitbucket&#x20;

1. Log in to your Bitbucket account and select a Repository in which you want to configure a Webhook.

<figure><img src="../../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Click Settings and select [Webhooks](https://knowledgebase.autorabit.com/product-guides/codescan/codescan-integration/webhooks).
3. Next, enter the URL in the given format: \
   \<instance\_url>/api/webhook/v2/\<orgname>/trigger-scm-push-request \
   For example, if the instance is https://login.autorabit.com, then the payload URL would be: [https://login.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest](https://login.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest).

<figure><img src="../../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Now fill in the details and click Save.

***

## **Smart Commits**

In this section, you can select the pattern used to read the comment in a revision associated with your ALM story. For example, _'git commit m \[project123] # add README file into the project'_

<figure><img src="../../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

If you want to configure a webhook in your repository, select the 'Enable auto update on webhook' checkbox to reveal the URL required for the webhook settings. For more information on how to configure a webhook in different repositories, refer [HERE](file://product-guides/arm/arm-features/webhooks). You can also choose to [sync external smart commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

***

## For Enterprise customers

/api/webhook/v2/\<orgname>/`enterprise`/trigger-scm-push-request

/api/webhook/v2/\<orgname>/`enterprise`/sync-alm-commits

