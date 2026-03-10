# Integration User

### Why Use an Integration User License for Guard?

Guard automates security actions in your Salesforce org, helping adhere to security policies and automatically remediating issues. To ensure that these actions are properly attributed and not mixed up with individual user activities, we recommend using a Salesforce Integration User License.

The Integration User License is a special license in Salesforce meant exclusively for integration users, allowing external systems like Guard to interact with your Salesforce org. By using this license, all actions performed by Guard are clearly attributed to the integration user, ensuring accurate and transparent audit logs.

{% hint style="info" %}
A Salesforce org can be connected to Guard using a System Administrator Profile, as it provides all required permissions for the integration. However, many organizations choose to configure a dedicated Integration User for this purpose, in line with common Salesforce best practices. Using a separate Integration User can help distinguish integration activity from individual user activity and align with internal governance or security policies.
{% endhint %}

### Setting Up an Integration User for Guard

To ensure Guard can properly access and manage security policies in your Salesforce org, you need to assign the correct Integration User License and Permissions.

#### 1. Assign the Salesforce Integration User License

The Integration User License is a special Salesforce license designed for automated processes, like Guard. By using this license, all actions performed by Guard are attributed to a dedicated integration user, keeping audit logs clean and ensuring proper access control.\
\
By default, the Salesforce Integration Profile (which comes with this license) only includes basic API access. It does not grant access to standard or custom objects in your org. That’s where the next step comes in.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (2).png" alt=""><figcaption><p>Integration User License</p></figcaption></figure>

#### 2. Assign the Salesforce API Integration Permission Set License (PSL)

Since the Integration User License alone does not provide access to objects and permissions needed by Guard, you must assign the Salesforce API Integration Permission Set License (PSL).<br>

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (2).png" alt=""><figcaption><p>Assign the Salesforce API Integration Permission Set License</p></figcaption></figure>

The Salesforce API Integration PSL includes administrative permissions that were originally part of the System Administrator profile but are now assigned separately. This license enables the integration user to be assigned additional permissions via permission sets.

#### 3. Assign the Required Permission Set

A Permission Set defines specific access to Salesforce objects and features. Once the Salesforce API Integration PSL is assigned, proceed to create and assign a Permission Set that grants the Integration user permissions required for the Guard application:

| Product Area                                      | Permissions Required                                                                                             | Rationale                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Risk Assessment                                   | (Modify All Data OR Modify Metadata Through Metadata API Functions), View Health Check, Manage Password Policies | <p>The Risk Assessment uses the Metadata API to scan the metadata of an org and find misconfigurations.</p><p>Access to the Metadata API requires either Modify All Data or Modify Metadata Through Metadata API Functions.</p><p>To categorise and remediate some of the misconfigurations, the View Health Check and Manage Password Policies permissions are required.</p>                                      |
| Automated Data Classification                     | Customize Application                                                                                            | Automated Data Classification allows syncing Guard’s classification back to Salesforce’s custom field definitions. To change custom fields, Customize Application is required.                                                                                                                                                                                                                                     |
| Access Control Policies / Authorization Policies  | Assign Permission Sets                                                                                           | This feature allows Guard to remove permission sets from unauthorised users. To remove permission set assignments, Assign Permission Sets is required.                                                                                                                                                                                                                                                             |
| Permissions Explorer                              | View Setup and Configuration, Assign Permission Sets and Manage Users                                            | This feature queries the PermissionSetAssignment object to show user access patterns. As per Salesforce official docs, this object is restricted to users with these 3 permissions.                                                                                                                                                                                                                                |
| API Dashboard                                     | Customize Application                                                                                            | This page queries the OauthToken Tooling API object, which requires the Customize Application permission.                                                                                                                                                                                                                                                                                                          |
| User Security Overview / User Activity Monitoring | View Setup and Configuration, Assign Permission Sets and Manage Users                                            | Similar to other features mentioned above, this page requires access to user details, login history, permission set assignments, and more. All these are governed by the 3 permissions on the left.                                                                                                                                                                                                                |
| Change Monitoring                                 | View Setup and Configuration                                                                                     | This feature queries the SetupAuditTrail object, which is restricted by View Setup and Configuration.                                                                                                                                                                                                                                                                                                              |
| Public File Exposure                              | No specific permissions required                                                                                 | Salesforce applies the following access rules: [https://developer.salesforce.com/docs/atlas.en-us.260.0.object\_reference.meta/object\_reference/sforce\_api\_objects\_contentdistribution.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_contentdistribution.htm)                                                                         |
| Connecting a Salesforce org to Guard              | Approve Uninstalled Connected Apps                                                                               | <p>The very first time an admin connects to the AutoRABIT Connected App, this permission is required so that Salesforce does not block the connection.</p><p>Once the connection is established, the admin should formally install the app and grant access through profile and permission sets. Future users will not need this permission.</p><p>An alternative is to use the AutoRABIT External Client App.</p> |

* Modify All Data
* View Health Check
* Customize Application
* Manage Password Policies
* Assign Permission Sets
* Manage Users
* Approve Uninstalled Connected Apps

{% hint style="info" %}
The Integration User requires elevated permissions to allow Guard to access and evaluate Salesforce configuration, security settings, and user access controls. These permissions are necessary for the application to function as intended and provide full visibility into the org’s security and configuration posture.
{% endhint %}

If a permission set is assigned **without** the required PSL, you’ll receive an assignment error.\
\
To assign needed permissions, open the Permission Set created for integration users and proceed to System Permissions:

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (2).png" alt=""><figcaption><p>Permission Set Overview</p></figcaption></figure>

Click Edit to update permissions:

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (2).png" alt=""><figcaption><p>Edit System Permissions</p></figcaption></figure>

Make sure to enable all the permissions mentioned above. They are located under both the **System** and **Users** groups:

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (2).png" alt=""><figcaption><p>Permission Sets - Modify All Data</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (2).png" alt=""><figcaption><p>Permissions - Users</p></figcaption></figure>

Once all listed permissions are enabled, please save the changes and assign this Permission Set to the Integration user.
