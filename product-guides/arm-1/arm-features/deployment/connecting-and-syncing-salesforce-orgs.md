# Connect & Sync Your Salesforce Orgs

The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.

### About Salesforce Org Synchronization <a href="#about-salesforce-org-synchronization" id="about-salesforce-org-synchronization"></a>

The org synchronization provides a mechanism to export single data, or all content items, from a source to a target Salesforce org effortlessly, thereby establishing consistency among data.

When you move changes from a source org to a production org, the [metadata](https://www.autorabit.com/blog/6-benefits-of-restoring-your-metadata-in-salesforce-after-an-outage/) types would be the same. But when you make changes in the production org, there would be an inconsistency between the source org and production org. Org synchronization helps you compare the differences between the metadata types, so you can add or delete metadata types and ensure that both the orgs are in sync.

### How can I connect and sync metadata between two Salesforce orgs? <a href="#how-can-i-connect-and-sync-metadata-between-two-salesforce-orgs" id="how-can-i-connect-and-sync-metadata-between-two-salesforce-orgs"></a>

To perform org synchronization, follow the below steps:

1. Log in to your ARM account.
2. Click on the **`Deployment`** tile on the left side of the screen.
3. Go to the **`Org Synchronization History`** tab.
4.  Click on the **`Get Org Differences`** call-to-action button.<br>

    <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
5.  In the **`Org Differences`** dialog box, you will need to:

    * Give the process a **`Name`**.
    * Select your **`Source Org`** and **`Destination Org`**.
    * Select the **`Exclude Baseline Managed Package Changes`** checkbox if you do not wish to include baseline Managed Package changes during org sync.
    * Select the **`Generate Member Differences`** checkbox to view the metadata member's differences between two Salesforce orgs based on file/data-level comparison.
    * Specify the **`Batch size for Profile Components`** and the **`Batch size for other Components`** to retrieve records. So, the default size for the profile is **500**, and for other components is **2,000**. You can modify it as per your requirement. The bulk retrieve option helps run large jobs that exceed normal processing limits – you can deploy up to **10,000 files** at once or a maximum size of **14MB**. Using batch size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is the best option.

    To go to the next screen, click the **`Get Differences`** button. The next screen may take some time, depending on the number of components in your org.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (3).png" alt="" width="563"><figcaption></figcaption></figure>
6.  On the next screen, you can:

    * View the metadata list included in both source and target org.
    * Add or delete metadata components to/from the target org.
    * View the metadata member's difference report (if any).

    <figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
7. Once done with your selection, click on **`Synchronize Orgs`**.
8. On the next screen, check the **`Validate Deployment`** checkbox to verify whether the synchronization process will be successful or get failed. This is optional.
9. Select the **`Apex Test Level`** to validate your deployment. For detailed information on each Apex test level, refer to the article: [Apex Unit Tests](../../../arm/arm-features/deployment/apex-unit-tests.md).

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="516"><figcaption></figcaption></figure>

10. Click on **`Deploy`**.
11. You'll be taken to the [**`Deployment History`**](../../../arm/arm-features/deployment/monitor-deployments.md) page, where the current synchronization progress can be seen.

#### More information on the Org Synchronization Summary page <a href="#more-information-on-the-org-synchronization-summary-page" id="more-information-on-the-org-synchronization-summary-page"></a>

Synchronization summary information, such as label name, source org, destination org, etc., can be seen on the **`Org Synchronization History`** page.<br>

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

1.  **`Info:`** Click the![](<../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon to view the detailed synchronization report.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>
2. **`Delete:`** Click on the![](<../../../../.gitbook/assets/image (18) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon to delete a sync process. A confirmation message is displayed asking whether you want to delete the label. This process cannot be undone.
3. **`Schedule:`** Click the![](<../../../../.gitbook/assets/image (19) (1) (1) (1) (1) (1) (1) (1).png>)icon to set up when you want to carry out the org synchronization process. On the scheduled date and time, the org synchronization process runs automatically, and voila, you have a repeating schedule.
4. **`Run:`** Click the![](<../../../../.gitbook/assets/image (20) (1) (1) (1) (1) (1) (1) (1).png>)icon to rerun the org synchronization process.
5. **`Status:`**&#x53;tatus of the synchronization process, i.e., successful or failed.
   *   **Log Report:** Click on the![](<../../../../.gitbook/assets/image (21) (1) (1) (1) (1) (1) (1) (1).png>)icon under the **`Status`** column to view the log report for the sync process.<br>

       <figure><img src="../../../../.gitbook/assets/Screenshot 2025-11-20 at 12.00.15 PM.png" alt="" width="563"><figcaption></figcaption></figure>
6. **`Report:`**&#x54;here are two options in this column.
   * Click on the![](<../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1).png>)icon to view the metadata components difference report between the source and the target org.
   * Click on the![](<../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1).png>)icon to download the Diff report in your local system (in PDF or CSV format).

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>
