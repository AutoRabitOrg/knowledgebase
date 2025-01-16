# Restoring nCino Features

### Overview <a href="#overview" id="overview"></a>

This article deals with the procedure for recovering the metadata/data to your respective Salesforce Org and provides information about the menu options that are available for restoring information in [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/).

### Procedure <a href="#procedure" id="procedure"></a>

1. Login to your Vault account.
2. Click **Restore** from the Vault dashboard page and click on **Restore Now**.

<figure><img src="../../../../../.gitbook/assets/image (300).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, select your source **Salesforce Org configured with nCino objects**.

<figure><img src="../../../../../.gitbook/assets/image (301).png" alt=""><figcaption></figcaption></figure>

4. Next, select the restore source as **nCino Features** and its configuration from the drop-down. Click **Get Details and** the nCino configured list will get displayed.

<figure><img src="../../../../../.gitbook/assets/image (302).png" alt=""><figcaption></figcaption></figure>

5. Click on **Selective Restore**.

#### Selective Restore <a href="#selective-restore" id="selective-restore"></a>

This option allows you to select specific metadata/data that gets restored only to the target org.

<figure><img src="../../../../../.gitbook/assets/image (303).png" alt=""><figcaption></figcaption></figure>

1. Click on the **Selective Restore** button.
2. Choose one of the backups from the list and click on **Trigger Restore**.

<figure><img src="../../../../../.gitbook/assets/image (304).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, enter the **label** of your choice or leave the default label which was auto-generated.
4. Specify the **batch size** for components to retrieve records. 10K is the max batch size that you can set per batch. This option is useful in running large jobs that would exceed normal processing limits. As per the Salesforce governor limit, you can deploy or retrieve up to 10,000 files at once or a max size of 40MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches are your best solution.
5. Next, you can select the criteria for the restore to get performed:
   * **Disable Workflows**: On selection, all the workflows of the Salesforce objects will be deactivated, and the data would be transferred from the source to the destination sandbox. Once the restore is completed, workflows will get activated.
   * **Disable Validation rules**: Validation rules verify that the data a user enters in a record meets the criteria you specify before the user can save the record. On selection, all the validation rules of the Salesforce objects will be deactivated, and the data would be transferred from the source to the destination sandbox. Once the restore is done, validation rules will get activated.
6. Click **Restore Now**.

<figure><img src="../../../../../.gitbook/assets/image (305).png" alt="" width="512"><figcaption></figcaption></figure>

7. You will be redirected to the **Restore** homepage which will show you the progress of the restore operation recently triggered.
8. Click on the **Restore Label** to view the list of metadata/data being replicated to the org. Click on **Export** to save the restored metadata/data info in CSV format locally.
9. Click on the **Backup info** to get a snapshot of the backup operation performed.
10. Under the **Action** tab:

    * View the summary report using the **Restore summary** icon.
    * View the replicate log details using the **Log** icon.
    * For an ongoing replicate operation, you can abort the process in between using the **Abort** icon.

    <figure><img src="../../../../../.gitbook/assets/image (306).png" alt=""><figcaption></figcaption></figure>
