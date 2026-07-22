# User Profile and Permission Access for Salesforce Users

## Enable API Access for Users in Salesforce <a href="#enable-api-access-for-users-in-salesforce" id="enable-api-access-for-users-in-salesforce"></a>

To connect [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) with Salesforce, API access must be enabled for all users. This requires Salesforce Administrator privileges. Follow the steps below based on whether you're managing access via Profile or Permission Set.

***

### Enable API Access by Profile <a href="#enable-api-access-in-salesforce-by-profile" id="enable-api-access-in-salesforce-by-profile"></a>

1.  Click the **Gear** icon and choose **Setup**.

    ![Setup Gear Icon](<../../../.gitbook/assets/image (73) (1) (1) (1) (1) (1) (1) (1) (1).png>)
2.  In the Quick Find box, type **Profiles** and select it.

    ![Profiles Search](<../../../.gitbook/assets/image (74) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)
3.  Click **Edit** beside the target Profile.

    ![Edit Profile](<../../../.gitbook/assets/image (75) (1) (1) (1) (1) (1) (1) (1) (1).png>)
4.  Scroll to **Administrative Permissions**, enable **API Enabled**, and click **Save**.

    ![API Enabled Checkbox](<../../../.gitbook/assets/image (76) (1) (1) (1) (1) (1) (1) (1) (1).png>)

***

### Enable API Access by Permission Set <a href="#enable-api-access-in-salesforce-by-permission-set" id="enable-api-access-in-salesforce-by-permission-set"></a>

1.  Click the **Gear** icon and select **Setup**.

    ![Setup Gear](<../../../.gitbook/assets/image (73) (1) (1) (1) (1) (1) (1) (1) (1).png>)
2.  In the Quick Find box, type **Permission Sets** and select it.

    ![Permission Sets](<../../../.gitbook/assets/image (81) (1) (1) (1) (1) (1) (1).png>)
3.  Choose the desired **Permission Set**.

    ![Select Permission Set](<../../../.gitbook/assets/image (82) (1) (1) (1) (1) (1).png>)
4.  Scroll to **System**, click **System Permissions**.

    ![System Permissions](<../../../.gitbook/assets/image (83) (1) (1) (1) (1) (1).png>)
5.  Click **Edit**, check **API Enabled**, and **Save**.

    ![Enable API in Permissions](<../../../.gitbook/assets/image (84) (1) (1) (1) (1) (1).png>)

***

## Object and Field Permissions <a href="#object-and-field-permissions" id="object-and-field-permissions"></a>

Salesforce object permissions define what actions users can perform on object records, while field permissions control visibility and editability of fields.

| PERMISSION | DESCRIPTION             |
| ---------- | ----------------------- |
| Read       | View records only       |
| Create     | Create new records      |
| Edit       | Update existing records |
| Delete     | Remove records          |

* **For Vault Backups:** Users need **read** access to relevant objects, fields, files, and metadata.
* **For Restore, Replicate, Archive:** Users need **create**, **edit**, and **delete** permissions.
* Ensure integration users have access to **Metadata**, **SOAP**, **Bulk**, and **Tooling APIs**.

***

## Assign Custom Object Permissions to Standard User <a href="#assign-custom-object-permissions-to-standard-user-in-salesforce" id="assign-custom-object-permissions-to-standard-user-in-salesforce"></a>

1. In Salesforce, go to **Setup > Manage Users > Profiles**.
2.  Click **Edit** next to the profile to modify.

    ![Edit Profile](<../../../.gitbook/assets/image (79) (1) (1) (1) (1) (1) (1) (1) (1).png>)
3.  Scroll to **Custom Object Permissions** and configure as needed.

    ![Custom Object Permissions](<../../../.gitbook/assets/image (77) (1) (1) (1) (1) (1) (1) (1) (1).png>)

    ![Permission Table](<../../../.gitbook/assets/image (78) (1) (1) (1) (1) (1) (1) (1) (1).png>)
4. Click **Save**.
