# Users, Roles & Permissions

AutoRABIT (ARM) organizes access with **users**, **roles**, and **permissions**. Understanding these layers helps you grant just-right privileges while keeping administrative tasks manageable.

***

## Users in ARM <a href="#users-in-arm" id="users-in-arm"></a>

### Super Administrator <a href="#super-administrator" id="super-administrator"></a>

The **Super Administrator** (Super Admin) has the highest privileges in ARM.

* Create other admins
* Install and configure agents
* Add users to admin groups

> **Super Admin safeguards**\
> &#xNAN;_&#x53;uper Admin_ and **the currently logged-in user** are locked for **all** user-management actions: they cannot be added, deleted, suspended, edited, or delegated.

### Org Administrators <a href="#org-administrators" id="org-administrators"></a>

**Org Administrators** (Admins) access the **Settings Dashboard** to manage users, roles, and modules. An admin can hold multiple roles; ARM always applies the most permissive combination.

Admin-level capabilities include:

* Add, edit, or delete users
* Export user lists to CSV
* Enforce SSO
* Manage roles and permissions

### General Users <a href="#general-users" id="general-users"></a>

General users work in ARM modules according to permissions their Admin assigns. They **do not** see the Admin Dashboard.

***

## Create a New User Account <a href="#create-a-new-user-account" id="create-a-new-user-account"></a>

1. Log in to ARM.
2.  Go to **Settings › Users** and click **Add User**.\


    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.46.31 PM.png" alt=""><figcaption></figcaption></figure>
3.  Fill **User Details** and assign **Role Permissions**.\


    <figure><img src="../../../../.gitbook/assets/image (24).png" alt="" width="375"><figcaption></figcaption></figure>
4. Choose **Save & Activate** (immediate) or **Save Now & Activate Later**.
5. The new user receives an email to set a password.
6. The user appears in **Admin › Users**.

***

## Edit a User Account <a href="#edit-a-user-account" id="edit-a-user-account"></a>

1.  In **Settings › Users**, Locate the user and Click on **Actions** and click **Edit**.\


    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.50.01 PM.png" alt=""><figcaption></figcaption></figure>
2. Update fields (Username and Email are immutable).
3. Click **Save**.

***

## Delete or Suspend a User <a href="#delete-or-suspend-a-users-account" id="delete-or-suspend-a-users-account"></a>

*   **Delete User** – permanently remove the account.\


    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.52.36 PM.png" alt=""><figcaption></figcaption></figure>
*   **Activate / De-activate** – toggle suspension.\
    \


    <figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.53.42 PM.png" alt=""><figcaption></figcaption></figure>

Confirm the action to proceed.

***

## Enforce Single Sign-On (SSO) <a href="#enforce-single-signon-sso" id="enforce-single-signon-sso"></a>

1. Open **My Account** › **SSO Configuration**.
2. Check **Disable login with AutoRABIT credentials** and click **Save**.

Admins can still log in with username/password.\
To override SSO for select users, uncheck **Enforce SSO** next to their names.\
\


<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.57.01 PM.png" alt=""><figcaption></figcaption></figure>

> When you disable standard login, **Enforce SSO** auto-checks for all users.

***

## Export Users <a href="#export-users" id="export-users"></a>

Admins can download all user data as CSV.

1.  In **Settings › Users**, click **Export All Users**.\


    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  Select fields and click **Export**.\


    <figure><img src="../../../../.gitbook/assets/image (3) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
3. A CSV downloads to your computer.

> **Location privacy** – If a user blocks location sharing, ARM uses IP-based location.

***

## Creating and Editing Roles <a href="#creating-and-editing-roles" id="creating-and-editing-roles"></a>

1.  Go to **Settings › Users › Roles**.\


    <figure><img src="../../../../.gitbook/assets/image (4) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
2.  Click **Create Role**.\


    <figure><img src="../../../../.gitbook/assets/image (5) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
3.  Provide a **Role Name**, **Description**, and tick permissions.\
    \


    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
4. Click **Save**.

> _The default **Admin** role has full permissions and cannot be edited or renamed._

***

## User Permissions <a href="#user-permission" id="user-permission"></a>

1.  Open **Settings › Permissions**.\


    <figure><img src="../../../../.gitbook/assets/image (7) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>
2.  Select two or more users and click **Bulk Assignment**.\
    \


    <figure><img src="../../../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. Go to **Roles** and select the required role\
   \- Repeat the same process for **Salesforce Orgs**, **CI Jobs**, and **Version Control**.\
   \- Once all selections are made, click **Save**.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-08-16 at 3.14.41 PM.png" alt="" width="563"><figcaption></figcaption></figure>

Admins are hidden on this screen because they already hold full access.

***

## FAQ

### I’m an admin but can’t see certain branches or commits.

Your ARM account may belong to a different organization than those resources.

### Why can’t I see the User Management section anymore?

Your roles/permissions were changed. Contact another Org Administrator.

### Deleted users still appear in lists.

* Their **credentials** may still exist in **Settings › Credential Manager**.
* Repositories may reference those credentials—update or re-register.

### Why do some users lack access to certain ARM features?

Check their roles in **Settings › Roles**; only Admins have unrestricted access.
