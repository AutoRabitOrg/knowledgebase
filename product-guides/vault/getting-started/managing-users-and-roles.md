# Managing Users and Roles

Creating users and roles allows you to manage who can access a [**Vault™**](https://www.autorabit.com/products/vault-data-backup-recovery/). You can also create different roles that restrict or allow access to certain functionalities. For example, you might have a member of your team who only needs to look at scheduling backup operations for a sandbox but should never be able to perform a **Restore** operation.

{% hint style="info" %}
**Note:** You need **Administrator privileges** to manage a user account.
{% endhint %}

### Creating and Editing Roles <a href="#creating-and-editing-roles" id="creating-and-editing-roles"></a>

You must assign at least one role to each user, with specific role permissions granted to each role. If a user has multiple roles, the role with the greatest permissions trumps any others assigned.

{% hint style="info" %}
**Note:** You need **Administrator privileges** to create or update a role.
{% endhint %}

To create or edit a role:

1. Log in to your Vault™ account.
2. Go to the **Manage Users** module.
3. Go to the **Roles** tab and click **Add Role**.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. Enter a **Name** and **Description** for the role.
5. On the **Permissions** section, select checkboxes for each permission you want users with this role to have.
6. Click **Add Role**.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

7. The newly created role will be displayed on the **Manage Users'** home page. Note:
   * The account with the **Admin** role has the maximum permissions possible and cannot be edited or renamed.
   * The permissions you select determine which dashboard controls are in the user's console and what settings the user can manage.
8. You can also update or delete a role by clicking on the **Edit** and **Delete** icon on the **Manage Users** screen.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Creating Users <a href="#creating-users" id="creating-users"></a>

You can create a new user with just a few clicks. It’s as simple as entering the first name, middle and last name, an email, and selecting a role, Salesforce Orgs (if required), and designation. After you invite users, they receive a confirmation email with a link to create their login password.

{% hint style="info" %}
**Note:** You need **Administrator Privileges** to add user accounts.
{% endhint %}

1. Go to the **Manage Users** module and click on the **Users** tab.
2. Click **Add User**.

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. On the **Add User** wizard:
   * Enter the user's **First**, **Middle**, and **Last Name** and **Email Address**.
   * Select the appropriate **role** from the drop-down list.
     * The **Salesforce Orgs** field will be displayed only if the **Enable Org Access Control** toggle is turned on (in the **Manage Users** screen). In this dropdown, you must choose the Salesforce Orgs you want your user to access. The user will then be allowed to access only those Salesforce Orgs authorized for them. Based on the Salesforce Org access, users can carry out Vault™ operations in their Salesforce Org such as backup, restore, replicate, compare, archival, etc.
     * Enter the user's **designation** and add a short **description** to the user account. These fields are optional.
4. Click **Add User.**

<figure><img src="../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

5. The user will receive an email inviting them to select a password and log in. Newly created users are updated on the **Manage User** homepage. Note:
   * The account with **the Admin** role has the maximum roles and permissions possible and cannot be edited or renamed. By default, the roles will be displayed as **All**, means, the admin has all of the privileges inside Vault.
   * The logged in administrator details are non-editable and therefore will be in disabled mode.
   * The permissions you select determine which dashboard controls are in the user's console and what settings the user can manage.
   * The account verification link emailed to new users expires after **7 days.** Users who do not click the account verification link need an Admin to resend the account verification link to their email address.
   * Users must change their password the first time they log in.
   * The newly added users will be able to view their authorized Salesforce Orgs on the **Salesforce Org List (Setup)** and in the **Manage Users** section.
   * The Org Administrator will have access to all existing orgs or newly added orgs in Vault™.
   * Any sub-user who registers a new org will have full access to it, as well as Admin.

### Editing Users <a href="#editing-users" id="editing-users"></a>

After you’ve created a user, you can change most of their information and permissions. While you can't edit the **Email Address** associated with a user, you can change the remaining fields.

{% hint style="info" %}
**Note:** You need **Administrator Privileges** to manage user accounts.
{% endhint %}

1. Go to the **Manage Users > Users** tab.\
   Look for the user data that needs to be changed. You can view the complete user information using the **Info** icon.
2. Click the **Edit** icon to the right of the user.

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Make any desired changes and click **Save**.
4. View the user's details when you click on the **User Information** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1653039022101.png)) icon.

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="315"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**:

1. By default, all existing sub-users have access to all of the Salesforce Orgs registered. However, the Org Administrator can redefine their sub-users' access to the Salesforce Orgs on the **Manage Users** screen.
2.  The logged in administrator's details is disabled and cannot be edited.

    <figure><img src="../../../.gitbook/assets/image (17) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endhint %}

### Suspending Users <a href="#suspending-users" id="suspending-users"></a>

You can suspend users if you have Manage Users permissions or Administrator privileges. Suspended users can be reactivated later when required.

1. Log in to your Vault™ account.
2. Go to the **Manage Users > Users** tab.
3. Locate the user whose info you would like to change on the list.
4. Activate or deactivate a user account temporarily by sliding the **Activate** icon to either the right or left side.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Click on the **Email** icon to resend email activation to a user email id.
