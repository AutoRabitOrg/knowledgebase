# Not receiving email notifications from CodeScan for new issue assigned

**Problem Statement:**\
My team member assigned me issues for a project, yet, I have not received any email notification from CodeScan?

**Probable Cause:**

1.  Verify the **notifications feature is turned on** for any new issues in your profile.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-B5TEX58T.png" alt=""><figcaption></figcaption></figure>
2. If you login to CodeScan through SSO, ensure the following:
   1. Email attributes are configured in SAML configuration.
   2. If **SAML username** attribute contains **email** as a value, email security tools may block the notifications.

***

**Key point to note related to CodeScan Notification issue**

* A notification is never sent to the author of the event.
* The developer will not get notified about their own issues. It's only the assignee who gets notified and not the author.
* In case the author of pull request manually assigns the issue to **himself**, no email notification is received.
* The author/developer can look at their respective issues from the CodeScan UI.
* You can export issues in the CSV format for all the projects and monitor the issues ([https://knowledgebase.autorabit.com/codescan/docs/exporting-issues-in-codescan-cloud](https://knowledgebase.autorabit.com/codescan/docs/exporting-issues-in-codescan-cloud)) \*\*
