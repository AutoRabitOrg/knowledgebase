# Backup Configuration for your Salesforce Org

The configuration backup job creates a snapshot of the data/metadata from your Salesforce Org and retrieves data required for successful restore from it.

1. Go to **Setup** Module and select your [Salesforce Org](https://knowledgebase.autorabit.com/vault/docs/registering-salesforce-org) configured with nCino objects.
2. Go to the **Configs** tab and click on **Add Backup Config** button.
3. A popup will display asking you to choose the **Environment**. Here, select the second option i.e., [**nCino**](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/). Click **OK**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317781771.png" alt="" width="375"><figcaption></figcaption></figure>

1.  The next screen will display the entire nCino objects configured for Salesforce org. Here, you can either select/deselect the objects which will be part of the backup configuration.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317795665.png" alt=""><figcaption></figcaption></figure>
2. Click on either the individual object or **Feature Objects** button to view the object-related members on the next screen. Here, you have a provision to exclude certain members from getting backed up.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317815151.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317839535.png" alt="" width="375"><figcaption></figcaption></figure>

1. Once you are done with the selection of nCino objects, set up when you would like to carry out the **Org Backup** operation.

### Schedule Backup Process <a href="#schedule-backup-process" id="schedule-backup-process"></a>

Once you are done with the selection of nCino objects, set up when you would like to carry out the **Org Backup** operation.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317855440.png" alt=""><figcaption></figcaption></figure>

1. Give a **name** for the backup operation.
2. Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Screenshot%202021-09-22%20134023\(2\).png) icon to go to the **Backup Setting** page which allows you to enable Bulk API retrieval.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317869673.png" alt="" width="375"><figcaption></figcaption></figure>

1. Select the **Backup Type:**
   * **Full-Backup**: Full backup is a method of backup where all the files and folders selected for the backup will be backed up.
   * **Incremental-Backup**: An incremental backup operation will result in copying only the objects that have been changed since the last backup operation. The modified time stamp on files is typically used and compared to the timestamp of the last backup.
2. Select the email notification checkbox to receive an email notification whenever the objects are being backed up from your Salesforce Org.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317885132.png" alt="" width="563"><figcaption></figcaption></figure>

1.  Next, choose the frequency for backup i.e., either **daily**, **weekly**, **monthly,** or at any **specific interval**.\
    Say, you want the schedule of the backup process to run every **4 hours**, then select the **Specific** option and mention the time frame as **4 hours**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317911709.png" alt="" width="563"><figcaption></figcaption></figure>
2. You can specify till what time period you want to retain the backed data under the **Backup Retention period** field.
3. Click **Save Config**.
4. The next screen will display the summary list of nCino objects selected and the manner in which the backup will be carried out.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623317930969.png" alt="" width="563"><figcaption></figcaption></figure>

1. Click **Save**. A confirmation message will get displayed stating the backup is successfully configured for your Salesforce org.
2. You will be next redirected to the **Configs** page where you will find your newly added backup configured for your Salesforce Org.
3. **Additional options**:
   * **Schedule**: The user can either enable or disable the backup schedule of a Salesforce org temporarily by sliding the **Schedule** icon on either the right or left side.
   * **Backup Config Details**: Click on the ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Screenshot%202021-09-22%20134023\(3\).png) icon to view the list of metadata/data members of Salesforce org that will be backed up based on the process scheduled.
   * **Actions (Edit/Delete)**:  The user can either delete the backup scheduled using Delete (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/2\(1\).png)) icon or update the metadata/data components from being backed up using the **Edit** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/1.png)) icon.
   * **Last Backup Status**: Last backup activity status will be displayed in this section.
