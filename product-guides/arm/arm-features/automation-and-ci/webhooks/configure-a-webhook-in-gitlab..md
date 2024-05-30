# Configure a Webhook in GitLab

## A. Create a Webhook API token from ARM

1. Log in to ARM.
2. Click on Admin -> API Token.
3. Click on 'Create API Token.'

<figure><img src="../../../../../.gitbook/assets/image (31) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Enter the token name.
5. Select Type as “webhook.”
6. Enter a Description if required.
7. Click on 'Create Option.'&#x20;

<figure><img src="../../../../../.gitbook/assets/image (32) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

8. Your new API token is created.

***

## B. Create a Webhook with Authentication on GitLab

1. Log in to your GitLab account and select a Repository in which you want to configure a Webhook.

<figure><img src="../../../../../.gitbook/assets/image (29) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Navigate to Settings > Integrations.

<figure><img src="../../../../../.gitbook/assets/image (28) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, enter the URL in the given format: \
   Payload URL: < instance\_url>/api/webhook/v2/\<orgname>/trigger-scm-push-request\
   For example: If the instance is https://login.autorabit.com, then the payload URL would be: [https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request](https://login.autorabit.com/api/webhook/v2/autorabit.com/trigger-scm-push-request)

<figure><img src="../../../../../.gitbook/assets/image (27) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Now fill in the details and click Add webhook.

***

## &#x20;Smart Commits

In this section, you can select the pattern used to read the comment in a revision associated with your ALM story. For example, _**'git commit m \[project123] # add README file into the project'.**_

<figure><img src="../../../../../.gitbook/assets/image (26) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

If you want to configure a webhook in your repository, select the '**Enable auto update on webhook'** checkbox to reveal the URL required for the webhook settings. For more information on how to configure a webhook in different repositories, refer [HERE](file://product-guides/arm/arm-features/webhooks). You can also choose to [sync external smart commits](file://product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary).

## &#x20;For Enterprise customers

&#x20;/api/webhook/v2/\<orgname>/`enterprise`/trigger-scm-push-request

/api/webhook/v2/\<orgname>/`enterprise`/sync-alm-commits

&#x20;
