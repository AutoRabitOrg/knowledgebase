# Delegating Approvals to Another User

{% hint style="info" %}
**Important Note:** The steps below can be performed only by an **Org Administrator**. General users do not have access to the delegation feature.&#x20;
{% endhint %}

When a teammate is on vacation or otherwise unavailable, an administrator can **delegate** that user’s approvals, scheduled tasks, and repository access to an active colleague. The original account is deactivated, and the delegate steps in with identical permissions.

***

## Delegate a User’s Responsibilities

1. Log in to **AutoRABIT**.
2.  Hover over **`Admin`** and click **`Users`**.

    <figure><img src="../../../../.gitbook/assets/image (639).png" alt="Admin › Users option in the navigation menu"><figcaption></figcaption></figure>
3.  Locate the **user** whose responsibilities you need to delegate and click **Delegate**.

    <figure><img src="../../../../.gitbook/assets/image (640).png" alt="Delegate button in the Users list"><figcaption></figcaption></figure>
4. The delegation wizard opens and lists everything tied to the departing user:
   * **Salesforce Orgs** registered in their name.
   * **Version Control Repositories** and branch permissions.
   * Any **scheduled tasks** or **approval queues**.

{% hint style="info" %}
* To ensure the delegate can reach private repos, choose a **default global credential** from the drop-down.
* Alternatively, click **+** to create a new credential and assign it immediately (see [**Create New Credential**](../../../arm/troubleshoot/how-tos/create-users-credentials.md) for details).
* **Super Admin** and the **currently logged-in user** cannot be delegated.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (641).png" alt="Delegation wizard showing tabs for Salesforce Orgs and Version Control Repositories"><figcaption></figcaption></figure>

5. At the bottom of the wizard, pick the **delegate user** from the drop-down list of active users.
6.  Click **Release User** to finalize the transfer.

    <figure><img src="../../../../.gitbook/assets/image (642).png" alt="Release User confirmation dialog" width="408"><figcaption></figcaption></figure>

{% hint style="info" %}
* The delegate **must be active**.
* The original user is **deactivated** automatically once delegation is complete.
{% endhint %}

***

## View Delegation Logs and Reports

After delegation, you’ll find two helpful links next to the user record in **Admin › Users**:

* **Log Details** – a detailed audit trail of the delegation process (successes, warnings, errors).
* **User Delegation Report** – a summary of all tasks, approvals, and schedules now owned by the delegate.

<figure><img src="../../../../.gitbook/assets/image (643).png" alt="Users list with Log Details and User Delegation Report icons"><figcaption></figcaption></figure>
