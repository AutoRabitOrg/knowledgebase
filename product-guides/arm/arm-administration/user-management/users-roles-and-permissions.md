# Users, Roles & Permissions

### Users in ARM <a href="#users-in-arm" id="users-in-arm"></a>

#### **Super Administrator** <a href="#super-administrator" id="super-administrator"></a>

The Super Administrator (or Super Admin) is the person who has the highest permissions of all the admins. This role can create other admins, assign or remove permissions, and perform all other admin activities. Deciding who and how many users you assign as super admin users requires significant consideration because they have the highest level of access and can make changes that affect the entire network.

Super admin permissions are required for the following:

1. Creating other admins
2. Installing and configuring agents
3. Adding users to admin groups

#### **Org Administrators** <a href="#org-administrators" id="org-administrators"></a>

Org Administrators (or Admins) are users with permission to access the ARM administration dashboard. The Admin can assign multiple roles to an individual admin if their job requires them to perform actions spanning multiple roles. You can share the responsibility of managing your ARM account by assigning administrator roles to other users.&#x20;

As an administrator for your organization, you can see a list of all the roles and privileges assigned to your users. This information can help you quickly determine a user's level of access to your organization's account.

#### **General Users** <a href="#general-users" id="general-users"></a>

General users have access to the ARM application based on the permission assigned by their Org Administrator. They are not allowed to access the Administration dashboard.

Important Note**Super Admin** and the **user currently logged in** are disabled for ALL actions. They cannot be added, deleted, suspended, activated, deactivated, edited, or their roles delegated to other users.

### Create a New User Account <a href="#create-a-new-user-account" id="create-a-new-user-account"></a>

To create a new user account:

1. Log in to your ARM account.&#x20;
2. Hover your mouse over the **`Admin`** tab and click on the **`Users`**.
3. Click the **`Add User`** button.

<figure><img src="../../../../.gitbook/assets/image (606).png" alt=""><figcaption></figcaption></figure>

4. Fill in the **`User Details`** and configure the **`Role Permissions`**.
5. Click **`Save & Activate`** to activate the users or **`Save Now & Activate Later`** to save the user details. They can be activated later from this page.

<figure><img src="../../../../.gitbook/assets/image (607).png" alt=""><figcaption></figcaption></figure>

6. Your colleague will receive an email inviting them to set their password and log in.
7. Newly created users are updated in the **`Users`** tab under the **`Admin`** module.

### Edit a User Account <a href="#edit-a-user-account" id="edit-a-user-account"></a>

After you’ve created a user, you can change most of their information and permissions. While you can't edit the **`Username`** and **`Email`** associated with a user, you can change the remaining fields.&#x20;

1. Log in to your ARM account.&#x20;
2. Go to the **`Users`** tab. Locate the user to whom you would like to make changes.
3. Click on the **`Edit`** icon.

<figure><img src="../../../../.gitbook/assets/image (609).png" alt=""><figcaption></figcaption></figure>

4. Make any desired changes and click on **`Save`**.

### Delete or Suspend a User's Account <a href="#delete-or-suspend-a-users-account" id="delete-or-suspend-a-users-account"></a>

If you have user management permissions, you can suspend or delete users. Suspended users can be reactivated; deleted users are permanently removed.&#x20;

1. Sign in using an administrator account.
2. Navigate to **`Admin > Users`** tab. Locate and select the user you'd like to make changes to.
3. Click on **`Delete User`** to delete the user account permanently.

<figure><img src="../../../../.gitbook/assets/image (610).png" alt=""><figcaption></figcaption></figure>

4. You can temporarily block users' access to your organization's services by suspending their accounts. Select the user and click on **`Activate/De-activate`** button.

<figure><img src="../../../../.gitbook/assets/image (611).png" alt=""><figcaption></figcaption></figure>

5. Click **`OK`** to confirm your selection.

### Enforce single sign-on (SSO) <a href="#enforce-single-signon-sso" id="enforce-single-signon-sso"></a>

You can enable an option to enforce SSO for members of your team. This will make it mandatory for all team members to log in via SSO.

To enforce SSO, you need to enable the SSO login configuration. Go to the **`My Account`** page, and under the **`SSO Configuration`**, select the **`Disable login with AutoRABIT credentials`** checkbox. Click **`Save`**. Your team members will now be forced to log in via SSO only. Even if SSO is enforced, you, as an org administrator, can log in using either standard authentication (username/password) or SSO.

#### How to override single sign-on (SSO)? <a href="#how-to-override-single-signon-sso" id="how-to-override-single-signon-sso"></a>

If you, an org admin, want to override the SSO configuration for an individual team member or group of users, you uncheck the **`Enforce SSO`** boxes after selecting the team members from the list.

<figure><img src="../../../../.gitbook/assets/image (612).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** When the **`Disable login with AutoRABIT credentials`** option is selected, the **`Enforce SSO`** checkboxes are automatically checked for all users.
{% endhint %}

### Export Users <a href="#export-users" id="export-users"></a>

If you have **`Admin`** permissions, you can export a CSV file of all the users currently in your account. The CSV export will contain the following user information:

| Fields                | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `First Name`          | First Name                                                         |
| `Last Name`           | Last Name                                                          |
| `Status`              | User status - active or deactivated                                |
| `Email`               | Email address                                                      |
| `Login Name`          | Login Username                                                     |
| `Role`                | Assigned role                                                      |
| `Job Title`           | Job title                                                          |
| `Last Login Date`     | Last login date and time                                           |
| `Created Date`        | Date when the account was created                                  |
| `Created By`          | The user who created the account                                   |
| `Last Modified Date`  | Date when the account was last modified                            |
| `Last Modified By`    | The user who modified the account most recently                    |
| `Login Type`          | Login type: Standard or SSO                                        |
| `Last Login IP`       | The IP address of the user at the time of the last login           |
| `Last Login Lat/Long` | Geographical coordinates of the user at the time of the last login |
| `Last Login Location` | City, state, and country of the user at the time of the last login |
| `Last Login Browser`  | The user's browser at the time of the last login                   |
| `Deactivated Date`    | Date when the account was deactivated (if applicable)              |
| `Deactivated By`      | The user who deactivated the user account                          |

{% hint style="info" %}
**Important Note:** When a user logs in to ARM, the browser pop-up message will ask permission to access the location details. If you **allow** permission, the location details will be retrieved through your browser, but if you **deny** permission, the location details will be retrieved through your IP Address.
{% endhint %}

**To export all user's details in CSV:**

1. On the **`Users`** screen, in the upper right, click **`Export All Users`**.

<figure><img src="../../../../.gitbook/assets/image (613).png" alt=""><figcaption></figcaption></figure>

2. The fields you can export will be displayed on the next screen. Click the **`Export`** button after choosing the fields you want to export as CSV.

<figure><img src="../../../../.gitbook/assets/image (614).png" alt="" width="511"><figcaption></figcaption></figure>

3. Fields like _`First Name`_, _`Last Name`_, _`Status`_, _`Email`_, and _`Login Name`_ are automatically selected by default when a CSV file is exported. If necessary, you can exclude them from being exported.
4. Your export will begin processing, and the CSV file will be downloaded on your local machine.

**Export Data Limitations**

The parameters in the CSV for previously registered users (older than 60 days) will be slightly different:

* CreatedDate = OrgCreatedDate
* CreatedByName = registered user of the org
* LastModifiedDate, LastModifiedByName, Deactivated Date, and Deactivate by fields will be null

As expected, the exported CSV file will contain the newest parameter data and changes for newly registered users.

### Creating and Editing Roles <a href="#creating-and-editing-roles" id="creating-and-editing-roles"></a>

You must assign at least one role to each user, with specific permissions granted to each role. If a user has multiple roles, the role with the most significant permissions trumps any others assigned.&#x20;

1. Hover your mouse over the **`Admin`** tab and click the **`Roles`** option.

<figure><img src="../../../../.gitbook/assets/image (615).png" alt="" width="251"><figcaption></figcaption></figure>

2. Click on the **`Create Role`** button.

<figure><img src="../../../../.gitbook/assets/image (616).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, enter a **`Role Name`** and **`Description`** for the role. On the **`Permissions`** tab, select the checkboxes to assign the roles you want users to have.

<figure><img src="../../../../.gitbook/assets/image (617).png" alt="" width="563"><figcaption></figcaption></figure>

4. Click **`Save`**.

{% hint style="info" %}
**Important Note:**

1. The Admin has the maximum permissions and cannot be edited or renamed.
2. The permissions you select determine which dashboard controls are in the Admin console and what settings the user can manage.
{% endhint %}

### User Permissions <a href="#user-permission" id="user-permission"></a>

This section summarizes the permissions assigned to the user. It allows them to view the type of access and actions they can perform in ARM. For example, users with the **`View Setup and Configuration`** permission can view Setup pages, and users with the **`API Enabled`** permission can access any Salesforce API.

To assign users to a role and permission, use the following steps:

1. From the ARM home page, click and go to the **`Permissions`** tab.

<figure><img src="../../../../.gitbook/assets/image (618).png" alt="" width="251"><figcaption></figcaption></figure>

2. Select at least **two users** for whom you would like to assign permissions from the user's list view.
3. Click on **`Bulk Assignment`**.

<figure><img src="../../../../.gitbook/assets/image (619).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** User(s) with the Admin role is not displayed on the **Permissions** page.
{% endhint %}

4. On the next screen, select the **`roles`** to be assigned and select the module(s) you would like to add to these users.
5. Click **`Save`**.
6. You can click the user's name to open the user's record in detail view from the **`User Permission`** page.

<figure><img src="../../../../.gitbook/assets/image (622).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (621).png" alt="" width="563"><figcaption></figcaption></figure>

### FAQ <a href="#i-have-admin-access-so-why-cant-i-see-some-users-branches-and-commits-that-are-listed-under-my-organ" id="i-have-admin-access-so-why-cant-i-see-some-users-branches-and-commits-that-are-listed-under-my-organ"></a>

### I have admin access, so why can't I see some users' branches and commits that are listed under my organization? <a href="#i-have-admin-access-so-why-cant-i-see-some-users-branches-and-commits-that-are-listed-under-my-organ" id="i-have-admin-access-so-why-cant-i-see-some-users-branches-and-commits-that-are-listed-under-my-organ"></a>

If your user account is associated with a different organization, this can happen.

### Why can’t I see the User Management section anymore to add a user like I could before? <a href="#i-want-to-add-a-user-like-i-could-before-why-cant-i-see-the-user-management-section-anymore" id="i-want-to-add-a-user-like-i-could-before-why-cant-i-see-the-user-management-section-anymore"></a>

The **User Permissions** and **Roles** in your organization may have been rearranged. Please contact your Admin and they should be able to grant you the necessary permissions again.

### Why am I able to see some users who are deleted in AutoRABIT? <a href="#why-am-i-able-to-see-some-of-the-users-that-are-deleted-in-autorabit" id="why-am-i-able-to-see-some-of-the-users-that-are-deleted-in-autorabit"></a>

1. **The deleted user's credential exists in AutoRABIT**: Go to _**Admin > Credential Manager**_ and type in the username that exists. You should find a record if it is still there.
2. [**Version Control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) **repository is registered with the existing user's credentials**: Get your existing user credentials updated with the new user details with the help of your admin. To do so, go to **Credential Manager** section and search for the existing user credential and get it updated with the new user details. Or create a user credential for the new user and re-register the existing version control repository with it.

### Why do my users not have access to all the features available in ARM? <a href="#why-my-users-do-not-have-access-to-all-of-features-available-in-arm" id="why-my-users-do-not-have-access-to-all-of-features-available-in-arm"></a>

1. Your users may not have the authority to access the modules that they are looking for; nevertheless, users with administrator privileges only will have access to certain features. To see the user's available roles in AutoRABIT, go to the **Admin > Roles** section.
2. For the necessary permissions, contact your **Org Admin**.



