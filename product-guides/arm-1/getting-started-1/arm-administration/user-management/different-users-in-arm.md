# User Types

AutoRABIT (ARM) separates users into three distinct categories, each with its own set of privileges and responsibilities. Understanding these roles helps administrators grant the right level of access and manage the platform efficiently.

***

## Registered Admin <a href="#registered-admin" id="registered-admin"></a>

The **Registered Admin** is automatically created when someone in your organization purchases an ARM subscription and signs up for the first time. Acting as the primary liaison with AutoRABIT, this user has privileges that no one else—including Org Administrators—can match.

### Special capabilities

* **Subscription Management** – upload license keys, configure seats, and view subscription details.
* **Team Management** – create and configure teams/company settings.
* **Exclusive communication channel** with AutoRABIT for requests such as:
  * Installing or configuring agents
  * Reassigning the Registered Admin role
  * Increasing license counts or extending subscription validity

{% hint style="info" %}
**Important Note:**\
The **Registered Admin** account and the **currently logged-in user** cannot be added, deleted, suspended, reactivated, or delegated. Their roles are fixed and immutable.
{% endhint %}

***

## Org Administrators <a href="#org-administrators" id="org-administrators"></a>

**Org Administrators**—often just called **Admins**—manage the day-to-day configuration of ARM. They can:

* Create, edit, or delete users
* Assign or revoke roles and permissions
* Enforce SSO requirements
* Export user lists to CSV
* Perform nearly every task the Registered Admin can, except those reserved for subscription management

Admins can hold **multiple roles**. When more than one role is assigned, ARM applies the **most permissive** set of rights.

{% hint style="info" %}
The **Registered Admin** and **all Org Administrators** can perform every action listed above.
{% endhint %}

***

## General Users <a href="#general-users" id="general-users"></a>

General users operate ARM based on the permissions granted by their Org Admins. They:

* Cannot access the **Admin** dashboard
* See only the modules and controls assigned through roles
* Focus on development tasks like EZ-Commit, CI jobs, deployments, or data loading—without administrative overhead

Assigning the appropriate role ensures General Users have just enough access to do their work while protecting sensitive settings and data.

***

### Quick Reference

| Category              | Typical Responsibilities                                                                   | Access to Admin Dashboard?               |
| --------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **Registered Admin**  | Subscription, license, team, and agent management; escalation point for AutoRABIT support. | **Yes** (full)                           |
| **Org Administrator** | User/role management, SSO enforcement, environment setup, CI/CD configuration.             | **Yes** (full, except subscription page) |
| **General User**      | Day-to-day dev tasks: commits, merges, deployments, reports, etc.                          | No                                       |

Use these roles to delegate responsibilities appropriately and maintain a secure, well-governed ARM instance.
