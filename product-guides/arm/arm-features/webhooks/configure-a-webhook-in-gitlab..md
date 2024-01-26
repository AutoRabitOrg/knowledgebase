# Configure a webhook in GitLab.

1.  Login to your **GitLab** account and select a **Repository** in which you want to configure a Webhook.&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGitlabcustom1.png" alt=""><figcaption></figcaption></figure>
2.  Navigate to **Settings** **>** **Integrations**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGitlabcustom21.png" alt=""><figcaption></figcaption></figure>
3.  On the next screen, enter the URL in the given format: **InstanceURL/autorabitrest/webhook/triggerSCMPushrequest**\
    **For example**, if the instance is **https://login.autorabit.com**, then the **payload URL** would be:\
    **https://login.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest**&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinGitlabcustom31.png" alt=""><figcaption></figcaption></figure>
4. Now fill in the details and click **Add webhook**.
