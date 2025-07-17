# Setup backup configuration for Salesforce Org

## Overview <a href="#overview" id="overview"></a>

Backup configuration in Vault enables you to create snapshots of your Salesforce Org’s data and metadata. These backups can be full or incremental:

* **Full Backup**: Captures all data and metadata.
* **Incremental Backup**: Captures only data/metadata changed since the last backup.

Backups can be scheduled to run **daily**, **weekly**, **monthly**, or at a **custom interval**.

## Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* Ensure your Salesforce Org is registered with Vault.\
  [Learn More](./)

## How to Set Up a Backup Configuration <a href="#how-to-set-up-a-backup-configuration-for-your-salesforce-org" id="how-to-set-up-a-backup-configuration-for-your-salesforce-org"></a>

1. After registering a Salesforce Org, navigate to the **`Configs`** tab and select **`Add Backup Config`**. If needed, navigate manually via **`Setup`** > your Salesforce Org > **`Configs`** > **`Add Backup Config`**.
2. Choose a configuration type:
   * **Metadata and data excluding special objects**
   * **Special objects (history, audit logs, KAV, etc.)**

<figure><img src="../../../../.gitbook/assets/image (202).png" alt="Configuration type selection screen in Vault"><figcaption></figcaption></figure>

3. Select metadata types from the list to include in the backup.\
   Click **`Next`**.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Metadata selection screen"><figcaption></figcaption></figure>

4. On the **Data** tab, you can:
   * Filter objects
   * Include associated records
   * Apply timestamp-based filtering

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Data object filter and selection options"><figcaption></figcaption></figure>

5. Click a data object (e.g., **Account**) to view and manage its related fields.\
   Exclude any fields as needed.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Viewing and configuring fields for data object Account"><figcaption></figcaption></figure>

6. Select specific members and click **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Object member selection screen" width="563"><figcaption></figcaption></figure>

7. Return to the object list and confirm updates.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Updated data object view after configuration"><figcaption></figcaption></figure>

8. To exclude formula fields, enable **`Excluded Formula Fields`**.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Option to exclude formula fields"><figcaption></figcaption></figure>

9. Use the **Filter** icon to define label-based rules.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Filter icon and rule definition" width="563"><figcaption></figcaption></figure>

10. Use **Record Count Limit** to limit record extraction and validate the filter.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623321914149.png" alt="Record count validation example" width="563"><figcaption></figcaption></figure>

11. Click **`Apply`** to confirm filter settings.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Apply filter button"><figcaption></figcaption></figure>

12. Click **`Next`** to move to the **Scheduling** screen.

## Scheduling Backup <a href="#scheduling-backup" id="scheduling-backup"></a>

1. Provide a **name** and **description** for the backup.

<figure><img src="../../../../.gitbook/assets/image (211).png" alt="Backup scheduling form" width="563"><figcaption></figcaption></figure>

2. Configure Backup Settings:
   * **Bulk API for Data** (serial or parallel)
   * **Batch Size** for Metadata (max 10,000 records)

<figure><img src="../../../../.gitbook/assets/image (212).png" alt="Bulk API toggle for data objects" width="376"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (213).png" alt="Metadata batch size configuration" width="371"><figcaption></figcaption></figure>

3. Choose **Backup Type**:
   * **Full Backup**
   * **Incremental Backup**
4. Set **Email Notifications** recipients.

<figure><img src="../../../../.gitbook/assets/image (214).png" alt="Email notification recipient selection" width="563"><figcaption></figcaption></figure>

5. Enable or disable **Allow multiple backups to run in parallel**.

<figure><img src="../../../../.gitbook/assets/image (215).png" alt="Parallel backup option toggle"><figcaption></figcaption></figure>

6. Define **Backup Frequency** (e.g., every 4 hours via **Specific**).

<figure><img src="../../../../.gitbook/assets/image (216).png" alt="Custom interval backup frequency setting" width="511"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (217).png" alt="Time interval selection example" width="560"><figcaption></figcaption></figure>

7. Set the **Backup Retention Period**.
8. Click **`Save Config`**.
9. Review summary of selected metadata/data and backup plan.

<figure><img src="../../../../.gitbook/assets/image (218).png" alt="Backup configuration summary screen" width="563"><figcaption></figcaption></figure>

10. Click **`Save`**. A success message confirms configuration.
11. You are redirected to the **Configs** tab. Your new configuration will appear at the top.

### Additional Options

* **Schedule Toggle**: Temporarily enable/disable backup schedule.
* **Backup Config Details**: View selected metadata/data.
* **Edit/Delete**: Modify or remove the configuration.
* **Last Backup Status**: Displays most recent backup result.
