# Restoring Knowledge Articles with Vault

### What is Salesforce Knowledge and why do you need it? <a href="#what-is-salesforce-knowledge-and-why-do-you-need-it" id="what-is-salesforce-knowledge-and-why-do-you-need-it"></a>

Salesforce Knowledge allows you to build a Knowledge Base for storing and managing documentation to service your internal agents, website visitors, partners, and customers.

Users can create and manage a knowledge base with your company information and securely share it when and where it's needed. Salesforce Knowledge helps you establish a self-service model for your customers to solve their queries, leading to case deflection and increasing customer satisfaction.

Vault can restore/replicate knowledge data `Knowledge__kav` records with rich text and large image files.

### Point to Consider <a href="#point-to-consider" id="point-to-consider"></a>

* Knowledge Articles should exist in your Salesforce org.
* Restoring of the KAV (knowledge objects) to be always processed in a different job.
* To restore/replicate other metadata/data objects, run a different job, including all the required metadata and data objects.

### Process <a href="#process" id="process"></a>

To restore Knowledge data objects with Vault, follow the below steps:

> Similar steps are to be followed for **replicating** KAV objects in Vault. Replicate the KAV objects by navigating to the `Replicate` module.

1. Login to your **Vault** account and navigate to the **`Restore`** module.
2. In the **`Restore`** page, select your **`Salesforce org`** configured with KAV objects.

<figure><img src="../../../../.gitbook/assets/image (261).png" alt=""><figcaption></figcaption></figure>

3. Select the **`Restore Source`** from the dropdown.
4. Click on **`Restore Now`**.
5. On the next screen, choose the **`backup configuration`** from the dropdown if not auto-selected.
6. Click on **`Get Details`**. Based on the **`restore source`** and **`configuration`** selection, the backup configured list will get displayed.
7. Select the **backups** from the list for restoration.
8. Click on **`Selective Restore`**.

<figure><img src="../../../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

9. Go to the **`Data`** tab and slide the toggle bar to the right side for **`KAV Object only`**. This will allow viewing the KAV-related objects only in the list.
10. Select the **KAV object**.

<figure><img src="../../../../.gitbook/assets/image (263).png" alt=""><figcaption></figcaption></figure>

11. You also have multiple configurations to choose from under the **`Data`** tab:
    * **`Schema:`** This option will allow you to view all the child objects for your selected kav object.
    * **`Selected Records:`** This will allow you to choose the records for your object. By default, all the records available in the objects will be auto-selected.
    * **`Selected Fields:`** This will allow you to select the fields for your object. By default, all the fields available in the objects will be auto-selected.
12. Click on **`Trigger Restore`**.

{% hint style="info" %}
**Point to Note:**

If you choose to deploy KAV objects along with other metadata/data objects, the Vault application will not allow you to continue further. The message below pops up:&#x20;

`Ensure only KAV object is selected for this restore job. KAV is a special object and can be processed only in separate job. To restore other data objects/ metadata run another job including all the required metadata and data objects.`
{% endhint %}

13. On the **`Selected Data To Restore`** screen, enter the **label** of your choice or leave the auto-generated default label.
14. Specify the **batch size** for components to retrieve records.
15. Choose the recipients from the **`Email notification`** dropdown who should receive notifications whenever the action is performed. The currently logged-in recipient will automatically be checked by default.
16. Select the criteria for performing the restore and click on **`Restore Now`**.

<figure><img src="../../../../.gitbook/assets/image (264).png" alt="" width="563"><figcaption></figcaption></figure>

17. You'll be taken to the **`Restore Summary`** screen, which will display the status of the recently triggered restore activity.
18. Once the restore operation is successfully triggered, the status changes to **`Ready to link kav to case`**.

<figure><img src="../../../../.gitbook/assets/image (265).png" alt=""><figcaption></figcaption></figure>

19. Under the **`Actions`** tab, you can perform additional operations:
    * For an ongoing restore operation, you can **abort** the process in between using the **`Abort`**![](<../../../../.gitbook/assets/image (71) (1).png>)icon.
    * View the **restore summary report** using![](<../../../../.gitbook/assets/image (72) (1).png>)icon.
    * View the **restore log report** using![](<../../../../.gitbook/assets/image (73) (1).png>)icon.
    * Trigger **linking kav to case** using![](<../../../../.gitbook/assets/image (74) (1).png>)icon.

{% hint style="info" %}
**Points to Note:**

* To ensure successful linking, do confirm that the **kav records** for linking are in `Published` status in Salesforce.
* Once the Kav record is successfully linked, the job status changes to complete (![](<../../../../.gitbook/assets/image (76) (1).png>)) state.
* The **`trigger`** (![](<../../../../.gitbook/assets/image (75) (1).png>)) button will not be available; henceforth, linking kav to case is triggered.
{% endhint %}
