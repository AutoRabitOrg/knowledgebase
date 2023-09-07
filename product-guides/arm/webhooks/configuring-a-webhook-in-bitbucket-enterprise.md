# Configuring a Webhook in Bitbucket Enterprise

1.  Log in to your **Bitbucket** account and select a **Repository** in which you want to configure a Webhook.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinBitbucketEnterprisecustom1.png" alt="" width="375"><figcaption></figcaption></figure>
2.  Click on **Repository Settings** and select **Webhooks**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinBitbucketEnterprisecustom21.png" alt="" width="563"><figcaption></figcaption></figure>
3. Next, click on **Create webhook**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinBitbucketEnterprisecustom31.png" alt=""><figcaption></figcaption></figure>

1. On the next screen, enter the **Webhook** **name**
2.  Next, enter the URL in the given format: **InstanceURL/autorabitrest/webhook/{org-name}/triggerSCMPushrequest**\
    For example, if the instance is **https://login.autorabit.com** and org name as autorabit.com, then the payload URL would be: _**https://login.autorabit.com/autorabitrest/webhook/autorabit.com/triggerSCMPushrequest**_\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinBitbucketEnterprisecustom41.png" alt="" width="375"><figcaption></figcaption></figure>
3. Now fill in the required details and click **Create**.
4. Additionally, a **"webhookinfo.properties"** file will be shared by the AR team that needs to be placed in the **.rabit/org/orgname/config** location.
