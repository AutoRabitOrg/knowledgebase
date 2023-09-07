# Google Cloud Platform

### Customer Hosted GCP Storage Environment <a href="#customer-hosted-gcp-storage-environment" id="customer-hosted-gcp-storage-environment"></a>

To use GCP as your storage environment to backup your metadata and data objects, you need to configure it in the Vault application first.

1. Head to the **Backup Environment** tab under the **Settings** module.
2. Select **GCP** as the Storage Type.
3. Enter the **Label Name** of your choice
4. Enter your **Cloud Storage Bucket Name**. To create a new storage bucket, follow the below steps:
   1. In the Google Cloud Console, go to the Cloud Storage **Browser** page.
   2. Click **Create bucket**.
   3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**.&#x20;
      1. For **Name your bucket**, enter a name that meets the [bucket naming requirements](https://cloud.google.com/storage/docs/naming-buckets).
      2. For **Choose where to store your data**, select a [Location type](https://cloud.google.com/storage/docs/locations) and [Location](https://cloud.google.com/storage/docs/locations#available-locations) option where the bucket data will be permanently stored.&#x20;
      3. For **Choose a default storage class for your data**, select a [storage class](https://cloud.google.com/storage/docs/storage-classes) for the bucket. The default storage class is assigned by default to all objects uploaded to the bucket.&#x20;
      4. For **Choose how to control access to objects**, select an **Access control** option. The access control model determines how you [control access](https://cloud.google.com/storage/docs/access-control) to the bucket's objects.&#x20;
      5. For **Advanced settings (optional)**, add **bucket labels**, set a [retention policy](https://cloud.google.com/storage/docs/bucket-lock), and choose an [encryption method](https://cloud.google.com/storage/docs/encryption).
      6. Click **Create**.
   4.  In the **Project ID** field, enter the project ID for which you would like to add them in Vault. You can find the details in the **Settings** tab in your Google Cloud Console.Steps to create a new Project

       1. Go to the **Manage resources** page in the Cloud Console.
       2. On the **Select organization** drop-down list at the top of the page, select the organization in which you want to create a project. If you are a free trial user, skip this step, as this list does not appear.
       3. Click **Create Project**.
       4. In the **New Project** window that appears, enter a project name and select a billing account as applicable. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters.
       5. Enter the parent organization or folder in the **Location** box. That resource will be the hierarchical parent of the new project.
       6. When you're finished entering new project details, click **Create**.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623236040736.png" alt=""><figcaption></figcaption></figure>
5. Now, upload the **GC Storage Credential File** for your GCP service account from your local system. The file is in JSON format. If you haven't created a service account yet, you can create a new one by following the below steps:
   1. In the Cloud Console, go to the **Service Accounts** page.
   2. Select a project.&#x20;
   3.  Click **Create Service Account**.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623236064512.png" alt=""><figcaption></figcaption></figure>
   4. Enter a **service account name** to display in the Cloud Console.&#x20;
   5. The Cloud Console generates a service account ID based on this name. Edit the ID if necessary. You cannot change the ID later.&#x20;
   6. **Optional:** Enter a description of the service account.
   7. If you do not want to set access controls now, click **Done** to finish creating the service account. To set access controls now, click **Create** and continue to the next step.![create service account](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623236076290.png)
   8. **Optional:** Choose one or more **IAM roles** to grant to the service account on the project.&#x20;
   9. When you are done adding roles, click **Continue**.&#x20;
   10. **Optional:** In the **Service account users role** field, add members that can [impersonate the service account](https://cloud.google.com/iam/docs/impersonating-service-accounts#allow-impersonation).
   11. **Optional:** In the **Service account admins role** field, add members that can manage the service account.
   12. Click **Done** to finish creating the service account.
   13. Go to the **Actions** tab and select the option: **Manage Keys**

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623236106290.png" alt=""><figcaption></figcaption></figure>
   14. In the **Keys** tab, go to **Add Key > Create new key.**
   15. Select the Key type as **JSON** and click on **Create**. The file gets downloaded to your local system.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623236125657.png" alt=""><figcaption></figcaption></figure>
   16. Upload the downloaded JSON file in the **GC Storage Credential File** field.
6. In **Region**, choose the GCP Region where your bucket resides.
7. Click **Save Settings**.

### Vault Hosted Backup Environment <a href="#vault-hosted-backup-environment" id="vault-hosted-backup-environment"></a>

To select the default Vault hosted environment to work on the Vault functionalities:&#x20;

1. Select the checkbox: [**ARVault Hosted Backup Environment**](https://www.autorabit.com/products/vault-data-backup-recovery/)**.**
2. Choose the **Region** where you want the bucket to reside.
3. Click **Save Settings.**
