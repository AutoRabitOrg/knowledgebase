# Removing or Suspending Users

Org Administrators can **suspend** (temporarily disable) or **delete** (permanently remove) users when team membership changes.\
Suspension preserves the account record so you can reactivate it later; deletion erases the account and audit trail forever.

> **Tip:** Always suspend first if you think the user might return—reactivation is one click, while deletion requires recreating the account from scratch.

***

## Suspend or Delete a User

1. Sign in with an **administrator** account.
2. Navigate to **Settings › Users**.
3.  Locate the user you want to modify.<br>

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 3.31.55 PM.png" alt=""><figcaption></figcaption></figure>
4. **Delete User** – Select the User and click on **Delete Selected** and Confirm the pop up icon to erase the account permanently.
5.  **Suspend / Activate** – click **Activate/De-activate** to toggle the account’s status.<br>

    <figure><img src="../../../../../.gitbook/assets/image (1903).png" alt=""><figcaption></figcaption></figure>
6. Confirm the action by clicking **OK** in the dialog.

***

### What Happens Next?

| Action      | Result                                                                                              | Can Be Reversed?                                    |
| ----------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Suspend** | User cannot log in; data and permissions remain intact.                                             | **Yes** – click **Activate** to restore access.     |
| **Delete**  | User account is removed from ARM; historical records remain in audit logs but cannot be reassigned. | **No** – must create a new account if needed again. |

***

### Best Practices

* **Suspend first** if unsure—reactivation is easier than re-creating roles, labels, and permissions.
* **Reassign approvals** or scheduled tasks before deleting a user to avoid orphaned work.
* Periodically review **Settings › Users** for suspended accounts you can delete to stay within license limits.
