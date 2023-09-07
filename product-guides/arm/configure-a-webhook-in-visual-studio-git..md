# Configure a webhook in Visual Studio GIT.

1. Login to your **Visual Studio GIT** account.
2. Select a repository in which you want to configure a webhook and click on **Settings**.
3.  Select **Service Hooks > Webhooks**. Click **Next**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITcustom1.png" alt=""><figcaption></figcaption></figure>
4. In the **Service Hook subscription** screen, do the following:
   1. Select **Trigger on this type of event** as **"Code pushed."**
   2.  Select **Repository**, **Branch,** and click **Next**.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITcustom21.png" alt=""><figcaption></figcaption></figure>
5.  On the next screen, enter the URL in the following format: **InstanceURL/autorabitrest/webhook/triggerSCMPushrequest**\
    For _example_, if the instance is **https://login.autorabit.com** , then the payload URL would be:\
    _https://login.autorabit.com/autorabitrest/webhook/triggerSCMPushrequest_

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/drexHowtoconfigureaWebhookinVisualStudioGITcustom31.png" alt=""><figcaption></figcaption></figure>
6. Click **Finish**.
