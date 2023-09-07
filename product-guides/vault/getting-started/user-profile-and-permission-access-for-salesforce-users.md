# User Profile and Permission Access for Salesforce Users

### Enable API access for users in Salesforce <a href="#enable-api-access-for-users-in-salesforce" id="enable-api-access-for-users-in-salesforce"></a>

API access needs to be enabled in Salesforce for all users for you to be able to connect [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) to your Salesforce account. This requires Salesforce Administrator credentials. Your Salesforce Administrator controls your Profile and Permission Sets.

Follow the steps below to:

* [Enable API access in Salesforce by Profile](https://knowledgebase.autorabit.com/vault/docs/user-permissions-and-access#enable-api-access-in-salesforce-by-profile)
* [Enable API access in Salesforce by Permission Set](https://knowledgebase.autorabit.com/vault/docs/user-permissions-and-access#enable-api-access-in-salesforce-by-permission-set)

#### Enable API access in Salesforce by Profile <a href="#enable-api-access-in-salesforce-by-profile" id="enable-api-access-in-salesforce-by-profile"></a>

1.  Click the Gear icon and click **Setup**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-G2JYQA7E.png" alt="" width="563"><figcaption></figcaption></figure>
2.  Type **profiles** into the Quick Find box and select **Profiles**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ILBCM1A0.png" alt="" width="188"><figcaption></figcaption></figure>
3.  Click **Edit** against the Profile you wish to enable API access for.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GWLPM48M.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Scroll down to **Administrative Permissions** and check the **API Enabled** box and click **Save**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-2YAMB63Y.png" alt="" width="563"><figcaption></figcaption></figure>

#### Enable API Access in Salesforce by Permission Set <a href="#enable-api-access-in-salesforce-by-permission-set" id="enable-api-access-in-salesforce-by-permission-set"></a>

1.  Click the Gear icon and click **Setup**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JTX9P5S2.png" alt="" width="375"><figcaption></figcaption></figure>
2.  Type **permission** into the Quick Find box and select Permission Sets.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-6EOIRL3C.png" alt=""><figcaption></figcaption></figure>
3.  Select the Permission Set you wish to enable API access for.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-VNY690C8.png" alt=""><figcaption></figcaption></figure>
4.  Scroll down to **System** and click **System Permissions**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-6P6HS3O9.png" alt=""><figcaption></figcaption></figure>
5.  Click **Edit**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-I0GC105X.png" alt=""><figcaption></figcaption></figure>
6.  Check the **API Enabled** box and click **Save**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Y1NA0ARM.png" alt=""><figcaption></figcaption></figure>

### Object and Field Permissions <a href="#object-and-field-permissions" id="object-and-field-permissions"></a>

Object permissions specify the base-level access users have to create, read, edit, and delete records for each object. The Salesforce Administrator can manage object permissions in permission sets and profiles.

Field permissions specify the access level for each field in an object.

The following permissions specify the access that users have to objects.

| PERMISSION | DESCRIPTION                               |
| ---------- | ----------------------------------------- |
| Read       | Users can only view records of this type. |
| Create     | Users can read and create records.        |
| Edit       | Users can read and update records.        |
| Delete     | Users can read, edit, and delete records. |

**Backup operation in Vault:** The registered users should have **read** access to all objects, fields, files, and metadata for which the backup is needed.

**Restore/Replicate/Archive operation in Vault:** The user should have **create**, **edit**, and **delete** access to all the objects, fields, and metadata for which the restore operation must be performed.

Also, the integration user must have access to the Metadata, Soap, Bulk, and Tooling APIs.

#### Assign custom object permissions to Standard User in Salesforce <a href="#assign-custom-object-permissions-to-standard-user-in-salesforce" id="assign-custom-object-permissions-to-standard-user-in-salesforce"></a>

One of the key tasks of Salesforce administrator is to assign the privileges to the appropriate users.

1. Within Salesforce, click on **Setup** and then click on **Manage Users**.
2. Under the **Manage Users** tree click on **Profiles**
3.  Once the Profiles appear on the right, select which Profile you want to edit and click on the **Edit** link next to the corresponding profile.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1SIAIMWV.png" alt=""><figcaption></figcaption></figure>
4. Scroll down to the section labeled **Custom Object Permissions**
5.  Specify the object permissions.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Q6851TM2.png" alt="" width="375"><figcaption></figcaption></figure>

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-MLWP4HDS.png)

7. Click **Save**.
