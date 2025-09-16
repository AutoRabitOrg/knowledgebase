# User Management

## User Management

AutoRABIT’s Guard provides flexible role-based access control to ensure security and efficiency when managing Salesforce orgs and users. This article outlines the available roles, their permissions, and the actions they can perform.

### Roles Overview

Guard currently supports two roles:

1. **Admin**
   1. Has full access to Guard’s user and org management features.
   2. Can configure, add, and remove Salesforce orgs.
   3. Manages user access and permissions for the workspace.
2. **Standard User**
   1. Has limited access, primarily focused on using Guard’s features without altering settings and configurations.
   2. Cannot manage other users or delete Salesforce orgs.

&#x20;

### Access Levels & Permissions

| Action                                                      | Admin | Standard User |
| ----------------------------------------------------------- | ----- | ------------- |
| Register and Edit Salesforce Orgs                           | ✅     | ❌             |
| Delete Salesforce Orgs                                      | ✅     | ❌             |
| Create Users                                                | ✅     | ❌             |
| Activate / Deactivate Users                                 | ✅     | ❌             |
| Unblock Users                                               | ✅     | ❌             |
| Delete Users                                                | ✅     | ❌             |
| Access Guard Features (analysis, scanning, reporting, etc.) | ✅     | ✅             |

&#x20;

### Blocked and Deactivated Users

#### When a User is Blocked

* Typical Scenarios:
  * Suspicious activity detected on the account.
  * Security breach or compromised credentials.
  * Temporary restriction.
* Impact:
  * The user is temporarily prevented from accessing Guard.
  * Their account remains active in the system and can be unblocked later.
* Admin Actions:
  * Review the reason for blocking.
  * If safe, unblock the user in User Management to restore access.

#### When a User is Deactivated

* Typical Scenarios:
  * Employee leaves the organization.
  * Team members no longer need access.
  * Role change makes Guard access unnecessary.
* Impact:
  * The user is permanently removed from active use of Guard.
  * Their access cannot be restored unless reactivated by an Admin.
* Admin Actions:
  * If needed again, reactivate the user instead of creating a new account.
  * Otherwise, keep the account deactivated for compliance and auditing.

&#x20;

#### Quick Reference

| Action     | Use Case                                   | Admin Can…                 |
| ---------- | ------------------------------------------ | -------------------------- |
| Block      | Temporary suspension (e.g., security risk) | Unblock to restore access  |
| Deactivate | Long-term or permanent removal             | Reactivate if needed later |

&#x20;

### Example Scenarios

* Scenario 1: Adding a New Salesforce Org
  * An Admin logs in, registers the org, and assigns access to specific users.
  * Standard Users can then interact with that org but cannot register or delete it.
* Scenario 2: Managing a Team Member
  * If a user leaves the team, the Admin can deactivate or delete their Guard account.
  * Standard Users have no visibility into these actions.

### Best Practices

* Always maintain at least two Admin users for redundancy.
* Assign the Standard User role to team members who only need access to View Data
* Regularly audit user access and deactivate accounts that are no longer in use.

With this role-based structure, Guard ensures a balance between security and usability, giving Admins full control while allowing Standard Users to operate safely without the ability to make system-wide changes.

&#x20;
