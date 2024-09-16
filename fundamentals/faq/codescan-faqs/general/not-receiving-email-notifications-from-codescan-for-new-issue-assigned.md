# Not receiving email notifications

**Problem Statement:**\
My team member assigned me issues for a project, yet I have not received any email notifications from CodeScan.

**Probable Cause:**

1. Verify the **notifications feature is turned on** for any new issues in your profile.

<figure><img src="../../../../.gitbook/assets/image (429).png" alt="" width="518"><figcaption></figcaption></figure>

2. If you log in to CodeScan through SSO, ensure the following:
   * Email attributes are configured in SAML configuration.
   * If **SAML username** attribute contains **email** as a value, email security tools may block the notifications.

**Key point to note related to CodeScan Notification issue**

* A notification is never sent to the author of the event.
* The developer will not be notified about their own issues. It's only the assignee who gets notified and not the author.
* If the author of a pull request manually assigns the issue to **themselves**, no email notification is received.
* The author/developer can look at their respective issues from the CodeScan UI.
* You can export issues in the CSV format for all the projects and monitor the issues ([https://knowledgebase.autorabit.com/codescan/docs/exporting-issues-in-codescan-cloud](https://knowledgebase.autorabit.com/codescan/docs/exporting-issues-in-codescan-cloud)) \*\*
