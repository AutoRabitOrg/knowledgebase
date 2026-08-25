# Salesforce Integration User Setup

## ARVault Salesforce Integration User Setup

Create a dedicated Salesforce integration user and grant the permissions required for ARVault backup and restore operations.

{% hint style="info" %}
**Purpose:** The integration user is the identity that the ARVault CC token impersonates. Use a dedicated service account that is not tied to an individual user.
{% endhint %}

## Setup overview

{% stepper %}
{% step %}
### Create the Salesforce integration user
{% endstep %}

{% step %}
### Create and configure the ARVault permission set
{% endstep %}

{% step %}
### Assign the permission set to the integration user
{% endstep %}

{% step %}
### Add conditional permissions when the corresponding ARVault functionality is required
{% endstep %}
{% endstepper %}

## Create the integration user

Navigate to Setup > Users > Users > New User in Salesforce.

### Enter the following user details

* **First Name:** ARVault
* **Last Name:** Integration
* **Alias:** arvint
* **Email:** Use a real, monitored mailbox for password resets and administrative notifications.
* **Username:** arvault-integration@.com. The username must be globally unique across all Salesforce organizations.
* **Nickname:** arvault-integration
* **User License:** Salesforce Integration. This license must be selected.
* **Profile:** Salesforce API Only System Integrations, which is the default profile for this license.

### Complete the user creation

{% stepper %}
{% step %}
### Clear password notification

Clear **Generate new password and notify user immediately** because the service account does not sign in interactively.
{% endstep %}

{% step %}
### Save the user

Select **Save**.
{% endstep %}
{% endstepper %}

{% hint style="success" %}
**Expected result:** The new integration user appears in Setup > Users with the status Active.
{% endhint %}

## Grant ARVault permissions

The default integration profile is intentionally minimal. Create a permission set to provide the data and metadata access required for backup and restore operations.

### Create the permission set

{% stepper %}
{% step %}
### Create a new permission set

Go to Setup > Permission Sets > New.
{% endstep %}

{% step %}
### Enter the permission set details

Enter **ARVault Integration Access** in **Label**. The API Name is populated automatically.

Select **Salesforce API Integration** in **License**. Do not leave the license as --None-- and do not clone the permission set from a profile.
{% endstep %}

{% step %}
### Save the permission set

Select **Save**.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
**Important:** The Salesforce Integration user license does not allow permissions such as Import Solutions, Run Reports, Send Email, Manage Letterheads, or Chatter and Communities permissions. Selecting Salesforce API Integration as the permission-set license hides unsupported permissions and prevents assignment failures.
{% endhint %}

### Enable the validated minimum permissions

Open the permission set and select System Permissions > Edit. Enable the following permissions, validated end-to-end against a live organization on July 2, 2026.

| **Permission**                                 | **Purpose**                                                                                                                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Modify All Data                                | Provides read and write access to all records on all standard, custom, and future objects. It includes read access equivalent to View All Data, so View All Data does not need to be selected separately.                    |
| Modify Metadata Through Metadata API Functions | Allows Metadata API retrieve and deploy operations for standard metadata types such as CustomObject, Profile, PermissionSet, Flow, and Layout. Keeping this permission explicit supports audit clarity and defense in depth. |
| Author Apex                                    | Allows retrieval and deployment of Apex classes and triggers through the Metadata API and provides Tooling API access to ApexClass and ApexTrigger.                                                                          |

Select **Save** after enabling the permissions.

{% hint style="info" %}
**API Enabled:** This permission does not appear in System Permissions when the permission-set license is Salesforce API Integration. API access is implicit in the license and remains enabled.
{% endhint %}

{% hint style="info" %}
**Object Settings:** When Modify All Data is enabled, per-object Read, Create, Edit, and Delete permissions do not need to be configured. Per-object grants apply only to a least-privilege approach that does not use Modify All Data.
{% endhint %}

### Assign the permission set

{% stepper %}
{% step %}
### Open the integration user

Go to Setup > Users and open the integration user.
{% endstep %}

{% step %}
### Edit permission set assignments

In Permission Set Assignments, select **Edit Assignments**.
{% endstep %}

{% step %}
### Enable the ARVault permission set

Move **ARVault Integration Access** from Available to Enabled.
{% endstep %}

{% step %}
### Save the assignment

Select **Save**.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
**Troubleshooting:** If assignment fails with The user license doesn't allow the permission: , the permission set uses the wrong license. Delete the permission set and recreate it with Salesforce API Integration selected.
{% endhint %}

## Add permissions for extended coverage

Enable the following permissions only when the corresponding ARVault operation or Salesforce configuration requires them.

### Full metadata coverage

| **Permission**                      | **When to enable**                                                                                                                                                                                                               |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manage Profiles and Permission Sets | Enable when ARVault backs up or restores Profile or PermissionSet metadata definitions. Without it, listMetadata works, but deployment of these types fails with INSUFFICIENT\_ACCESS. This permission can be added proactively. |

### Situational permissions

| **Permission**       | **When to enable**                                                                                                                                                                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View Encrypted Data  | Enable when the organization uses Shield Platform Encryption and plaintext values are required in backups. If it remains disabled, backups still work, but encrypted fields are masked. |
| Bulk API Hard Delete | Enable when ARVault performs hard-delete operations that bypass the Recycle Bin during restore reconciliation.                                                                          |
| View All Users       | Enable for explicit queries of all User records. Modify All Data generally provides the required access; add this permission only if access issues occur on the User object.            |

## Configuration check

* The integration user appears as Active in Setup > Users.
* The user license is Salesforce Integration.
* The assigned profile is Salesforce API Only System Integrations.
* The ARVault Integration Access permission set uses the Salesforce API Integration license.
* Modify All Data, Modify Metadata Through Metadata API Functions, and Author Apex are enabled.
* The permission set is assigned to the integration user without errors.
* Conditional permissions are enabled only when their related functionality is required.
