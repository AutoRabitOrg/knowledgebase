# Permissions

Assigning the right **permissions** determines what each user can see and do inside AutoRABIT (ARM).\
This page shows Org Administrators how to grant roles, module access, and branch access so teammates have just the access they need—nothing more, nothing less.

_Users with the **Admin** role manage their own permissions under that role and therefore do **not** appear in the Permissions list._

***

**Assign Permissions to Users**

1.  Open **Settings › Permissions**.<br>

    <figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
2.  Select two or more users and click **Bulk Assignment**.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. Go to **Roles** and select the required role\
   \- Repeat the same process for **Salesforce Orgs**, **CI Jobs**, and **Version Control**.\
   \- Once all selections are made, click **Save**.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 3.14.41 PM.png" alt="" width="563"><figcaption></figcaption></figure>

Admins are hidden on this screen because they already hold full access.



***

## Provide Branch Access to a User <a href="#to-provide-branch-access-to-a-user" id="to-provide-branch-access-to-a-user"></a>

Need to restrict or expand Git access? Grant repository or branch permissions here.

1.  In **`Settings › Permissions`**, click the user’s name.<br>

    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 7.39.55 PM.png" alt="" width="563"><figcaption></figcaption></figure>
2.  Scroll to the **`Version Control`** section. Check the branches the user should see.\
    <br>

    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 7.38.10 PM.png" alt="" width="563"><figcaption></figcaption></figure>
3. To grant access to **every** branch inside a repo, tick the **Repository** checkbox.
4. Click **Save**.

***

### Tips & Notes

* **Bulk Assignment** is perfect for onboarding large teams—select everyone and apply the standard role set once.
* If a user needs temporary access to a sensitive branch, grant it, set a calendar reminder, and remove it later.
* Remember that Admin-role users manage their own permissions and are hidden from the Permissions tab.
