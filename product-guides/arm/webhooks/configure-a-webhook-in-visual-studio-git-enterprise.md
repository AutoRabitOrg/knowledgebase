# Configure a webhook in Visual Studio GIT Enterprise

1. Login to your **Visual Studio GIT** account.
2. Select a repository in which you want to configure a webhook and click on **Settings**.
3.  Select **Service Hooks > Webhooks**. Click **Next**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITEnterprisecustom1.png" alt=""><figcaption></figcaption></figure>
4.  In the **Service Hook subscription** screen, do the following:

    1. Select **Trigger on this type of event** as **"Code pushed."**
    2. Select **Repository**, **Branch,** and click **Next**.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITEnterprisecustom21.png" alt=""><figcaption></figcaption></figure>
5.  On the next screen, enter the URL in the following format: **InstanceURL/autorabitrest/webhook/{org-name}/triggerSCMPushrequest**\
    For example, if the instance is **https://login.autorabit.com**, then the payload URL would be:\
    _https://login.autorabit.com/autorabitrest/webhook/autorabit.com/triggerSCMPushrequest_

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITEnterprisecustom31.png" alt=""><figcaption></figcaption></figure>
6. Click **Finish**.
7. Additionally, a "**webhookinfo.properties"** file will be shared by the AR team that needs to be placed in the **.rabit/org/orgname/config** location.
