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

A Permission Set defines specific access to Salesforce objects and features. Once the Salesforce API Integration PSL is assigned, proceed to create and assign a Permission Set that grants the Integration user permissions **required** for the Guard application:

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
