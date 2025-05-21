# Integration User License

### Why Use an Integration User License for Guard?

Guard automates security actions in your Salesforce org, helping adhere to security policies and automatically remediating issues. To ensure that these actions are properly attributed and not mixed up with individual user activities, we recommend using a Salesforce Integration User License.

The Integration User License is a special license in Salesforce meant exclusively for integration users, allowing external systems like Guard to interact with your Salesforce org. By using this license, all actions performed by Guard are clearly attributed to the integration user, ensuring accurate and transparent audit logs.

### Setting Up an Integration User for Guard

To ensure Guard can properly access and manage security policies in your Salesforce org, you need to assign the correct Integration User License and Permissions.

1.  **Assign the Salesforce Integration User License**\
    The Integration User License is a special Salesforce license designed for automated processes, like Guard. By using this license, all actions performed by Guard are attributed to a dedicated integration user, keeping audit logs clean and ensuring proper access control.\
    \
    By default, the Salesforce Integration Profile (which comes with this license) only includes basic API access. It does not grant access to standard or custom objects in your org. That’s where the next step comes in.\


    <figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption><p>Integration User License</p></figcaption></figure>


2.  #### Assign the Salesforce API Integration Permission Set License (PSL)

    Since the Integration User License alone does not provide access to objects and permissions needed by Guard, you must assign the Salesforce API Integration Permission Set License (PSL).\


    <figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption><p>Assign the Salesforce API Integration Permission Set License</p></figcaption></figure>

    \
    The Salesforce API Integration PSL includes administrative permissions that were originally part of the System Administrator profile but are now assigned separately. This license enables the integration user to be assigned additional permissions via permission sets.
3.  #### Assign the Required Permission Set

    A Permission Set defines specific access to Salesforce objects and features. Once the Salesforce API Integration PSL is assigned, you need to create and assign a Permission Set that grants the integration user the exact permissions Guard needs, such as:

    * Modify All Data
    * View Health Check
    * Customize Application
    * Manage Password Policies
    * Assign Permission Sets
    * Manage Users

    \
    If a permission set is assigned **without** the required PSL, you’ll receive an assignment error.\
    \
    To assign needed permissions, open Permission Set created for integration users and proceed to System Permissions:\


    <figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption><p>Permission Set Overview</p></figcaption></figure>

    \
    Click Edit to update permissions:\


    <figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption><p>Edit System Permissions</p></figcaption></figure>

    \
    Make sure to enable all the permissions lived above. They are located under both **System** and **Users** groups:\


    <figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption><p>Permission Sets - Modify All Data</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Permissions - Users</p></figcaption></figure>

    \
    After all the needed permissions are enabled, save the changes and assign the permission set to the Integration user.

