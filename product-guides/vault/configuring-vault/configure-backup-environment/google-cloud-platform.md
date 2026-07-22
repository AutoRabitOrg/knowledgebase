# Google Cloud Platform

## Customer-Hosted GCP Storage Environment <a href="#customer-hosted-gcp-storage-environment" id="customer-hosted-gcp-storage-environment"></a>

To use GCP as your storage environment to back up metadata and data objects, configure it within the Vault application as follows:

1. Navigate to the **Backup Environment** tab under the **Settings** module.
2. Select **GCP** as the Storage Type.
3. Enter a **Label Name** for your environment.
4. Enter your **Cloud Storage Bucket Name**. To create a bucket:

    1. In the Google Cloud Console, go to the **Cloud Storage Browser**.
    2. Click **Create bucket**.
    3. On the bucket creation page, complete the following:

       - **Name**: Choose a valid name following [bucket naming requirements](https://cloud.google.com/storage/docs/naming-buckets).
       - **Location**: Select a [Location type and region](https://cloud.google.com/storage/docs/locations).
       - **Storage class**: Pick a [default storage class](https://cloud.google.com/storage/docs/storage-classes).
       - **Access control**: Choose an appropriate [access model](https://cloud.google.com/storage/docs/access-control).
       - Optional: Configure labels, [retention policy](https://cloud.google.com/storage/docs/bucket-lock), and [encryption](https://cloud.google.com/storage/docs/encryption).

       - Click **Create**.

    4. In the **Project ID** field, enter the relevant project ID (visible under **Settings** in your GCP Console). To create a project:

       - Go to the **Manage resources** page.
       - Click **Create Project**.
       - Enter a **name**, **billing account**, and **location**.
       - Click **Create**.

<figure>
  <img src="../../../../.gitbook/assets/image (100) (1).png" alt="Creating a GCP Project">
  <figcaption>Create GCP Project</figcaption>
</figure>

5. Upload the **GC Storage Credential File** (.json) for your GCP service account. To create one:

    - Go to the **Service Accounts** page.
    - Select a project and click **Create Service Account**.

<figure>
  <img src="../../../../.gitbook/assets/image (101) (1).png" alt="Creating a GCP service account">
  <figcaption>Create Service Account</figcaption>
</figure>

    - Provide a name and optional description.
    - Click **Done**, or **Create** to proceed with role assignment.

<figure>
  <img src="../../../../.gitbook/assets/image (103) (1).png" alt="GCP service account info form" width="298">
  <figcaption>Service Account Details</figcaption>
</figure>

    - Optionally assign IAM roles and service account users/admins.
    - Click **Done**.
    - Under **Actions**, choose **Manage Keys**.

<figure>
  <img src="../../../../.gitbook/assets/image (104) (1).png" alt="Manage keys for service account" width="563">
  <figcaption>Manage Service Account Keys</figcaption>
</figure>

    - Go to **Add Key > Create new key**.
    - Choose **JSON** and click **Create** to download the key.

<figure>
  <img src="../../../../.gitbook/assets/image (105) (1).png" alt="Create and download GCP service account key" width="546">
  <figcaption>Download JSON Key</figcaption>
</figure>

    - Upload this JSON file under the **GC Storage Credential File** field.

6. In **Region**, choose the region where your GCP bucket resides.
7. Click **Save Settings**.

---

## Vault Hosted Backup Environment <a href="#vault-hosted-backup-environment" id="vault-hosted-backup-environment"></a>

To use Vault’s hosted environment for backups:

1. Check the box: [**AR Vault Hosted Backup Environment**](https://www.autorabit.com/products/vault-data-backup-recovery/).
2. Select the desired **Region** for your data.
3. Click **Save Settings**.
