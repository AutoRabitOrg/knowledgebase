# User Management

## User Management

AutoRABIT’s Guard provides flexible role-based access control to ensure security and efficiency when managing Salesforce orgs and users. This article outlines the available roles, their permissions, and the actions they can perform.

### Roles Overview

AutoRABIT Guard currently supports three roles:

1. **Tenant Manager**
   1. Can use everything in Guard and CodeScan 2.0 (if enabled).&#x20;
   2. Manages user access and permissions for the workspace.
2. **Guard Admin**
   1. Has full access to Guard’s org management features.
   2. Cannot manage users.
3. **Guard User**
   1. Has limited access, primarily focused on using Guard’s features without altering settings and configurations.
   2. Cannot manage other users or delete Salesforce orgs.

### Access Levels & Permissions

| **Action**                                                       | **Tenant Manager** | **Guard Admin** | **Guard User** |
| ---------------------------------------------------------------- | ------------------ | --------------- | -------------- |
| Register and Edit Salesforce Orgs                                | ✅                  | ✅               | ❌              |
| Delete Salesforce Orgs                                           | ✅                  | ✅               | ❌              |
| Create Users                                                     | ✅                  | ❌               | ❌              |
| Activate / Deactivate Users                                      | ✅                  | ❌               | ❌              |
| Unblock Users                                                    | ✅                  | ❌               | ❌              |
| Delete Users                                                     | ✅                  | ❌               | ❌              |
| View Guard features (analysis and results)                       | ✅                  | ✅               | ✅              |
| Manage and configure Guard features (run scans, receive exports) | ✅                  | ✅               | ❌              |

### Blocked and Deactivated Users

#### When a User is Blocked

* Typical Scenarios:
  * Suspicious activity detected on the account.
  * Security breach or compromised credentials.
  * Temporary restriction.
* Impact:
  * The user is temporarily prevented from accessing Guard.
  * Their account remains active in the system and can be unblocked later.
* Tenant Manager Actions:
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
* Tenant Manager Actions:
  * If needed again, reactivate the user instead of creating a new account.
  * Otherwise, keep the account deactivated for compliance and auditing.

#### Quick Reference

| Action     | Use Case                                   | Tenant Manager Can…        |
| ---------- | ------------------------------------------ | -------------------------- |
| Block      | Temporary suspension (e.g., security risk) | Unblock to restore access  |
| Deactivate | Long-term or permanent removal             | Reactivate if needed later |

### Example Scenarios

* Scenario 1: Adding a New Salesforce Org
  * An Admin logs in, registers the org, and assigns access to specific users.
  * Standard Users can then interact with that org but cannot register or delete it.
* Scenario 2: Managing a Team Member
  * If a user leaves the team, the Tenant Manager can deactivate or delete their Guard account.
  * Standard Users have no visibility into these actions.

### Best Practices

* Assign the Guard User role to team members who only need access to View Data.
* Regularly audit user access and deactivate accounts that are no longer in use.

&#x20;
