# Delegate Approvals to another User

{% hint style="info" %}
**Important Note:** This article is for the **'Org Administrator'** in particular. The actions discussed in the article will not be available to the General Users. &#x20;
{% endhint %}

If a user is out of the office, the admin can delegate his/her responsibilities to another user.

To delegate user permissions and tasks to another user:

1. Login to your AutoRABIT account.
2. Hover your mouse over the **`Admin`** tab and click on the **`Users`** option.

<figure><img src="broken-reference" alt="" width="251"><figcaption></figcaption></figure>

3. Locate the **user** you'd like to delegate his permission and tasks to another user.&#x20;
4. Click **`Delegate`**.

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

5. The next screen gets divided into multiple sections where each section contains roles and permissions exercised by the current user and such roles/permissions will get delegated to a different user. **For example-** the **`Salesforce Orgs`** tab contains all the Salesforce Orgs that are registered on his name, the **`Version Control Repositories`** section will contain the list of repositories and branches for each VCS (Version Control System) that the user had registered in AutoRABIT and the repositories permission allotted to him/her.

{% hint style="info" %}
**Important Note:**

1. In order to make sure the delegated user can access the repositories, the admin needs to set a default global credential from the drop-down list. Also, once the credential is allotted to the delegated user, he/she needs to update the credentials when logged into AutoRABIT for the first time.
2. The admin also has a provision to create a new credential and allot the same to the user. This will ensure the delegated user can access the user's repositories using the credential allotted to him. To know more about  how to create a new credential, refer to the article: [Create New Credential](https://knowledgebase.autorabit.com/arm/docs/create-users-credentials)
3. **Super Admin** and the **user currently logged in** are disabled for ALL actions. Their roles cannot be delegated to other users.
{% endhint %}

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

6. Finally, choose the user to whom you want to delegate your task and approvals.
7. Click **`Release User`**.

<figure><img src="broken-reference" alt="" width="408"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. You must select an active user as a delegate.
2. The user who delegates his tasks/approvals will be deactivated.
{% endhint %}

8.  For delegated users, you can find the delegation report and the log details on the **`Users`** screen.

    * **`Log Details:`** The log contains information about events and activities that have occurred during the user delegation process. It may contain errors, informational events or warnings, or our application problem.
    * **`User delegation report:`** View the summary list of approvals/ scheduled tasks that are delegated to the user.

    <figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>
