# Test Environment Setup

### Test Environment Setup: Overview <a href="#test-environment-setup-overview" id="test-environment-setup-overview"></a>

This enables data transfer from .csv files to the destination sandbox more conveniently and reduces run time using a test environment.

### Create a New Test Environment Setup <a href="#create-a-new-test-environment-setup" id="create-a-new-test-environment-setup"></a>

1. Hover your mouse over the [**`Dataloader`**](./) module and select **`Dataloader Test Environment Setup`**.

<figure><img src="../../../../.gitbook/assets/image (1116).png" alt="" width="332"><figcaption></figcaption></figure>

2. Click on **`Create New Job`**.

<figure><img src="../../../../.gitbook/assets/image (1117).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, select your **`Destination Org`**.

<figure><img src="../../../../.gitbook/assets/image (1118).png" alt=""><figcaption></figcaption></figure>

4. Click **`Login and Fetch Objects`**. This lists all the objects available in your destination org.
5. Select one of the objects from the list of objects being displayed. Here, we will call this object the **`Master Object`**.

<figure><img src="../../../../.gitbook/assets/image (1119).png" alt=""><figcaption></figcaption></figure>

6. To view the dependencies of the master object with respect to its parent object, click on the **`Show Dependencies`** icon.

<figure><img src="../../../../.gitbook/assets/image (1120).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1121).png" alt="" width="342"><figcaption></figcaption></figure>

7. Click the **`Switch to Graph View`** button to view the same report in the graphical format.

<figure><img src="../../../../.gitbook/assets/image (1122).png" alt="" width="395"><figcaption></figcaption></figure>

8. Under the **`Source of data`** section, upload the CSV file from your local machine in zip format.

<figure><img src="../../../../.gitbook/assets/image (1123).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** Upload the zip file containing object-related CSV with a .csv file name equal to the object API name. Having parent objects related to CSV in the zip file is optional. But records from those objects are migrated if and only if respective CSVs are uploaded.
{% endhint %}

9. In the **`Job Details`** section, give the job a **`Name`**.
10. Select the category from the **`Job Group`** field. This is important to arrange related jobs into a single category.
11. **`Master Object`** and **`External ID`** details are auto-populated.
12. Click **`Save`**.

<figure><img src="../../../../.gitbook/assets/image (1124).png" alt=""><figcaption></figcaption></figure>

13. The user is redirected to the **`Test Environment Setup summary`** page, where your recently created job is displayed at the top of the list.
14. Click **`Run`** to initiate the job.

<figure><img src="../../../../.gitbook/assets/image (1126).png" alt=""><figcaption></figcaption></figure>

15. The below table lists the deployment criteria for your job:

| Configurations                 | Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Disable Workflows`**        | All the workflows of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, workflows are reactivated.                                                                                                                                                                                                                                                                                                                                                                     |
| **`Disable Validation Rules`** | Validation rules verify that the data a user enters in a record meets the criteria you specify before the user can save the record. On selection, all the validation rules of the Salesforce objects are deactivated, and the data is transferred from the source to the destination sandbox. Once the migration is complete, validation rules are reactivated.                                                                                                                                                                                                     |
| **`Use Bulk API`**             | <p>The Bulk API is based on REST principles and is optimized for inserting, updating, and deleting large data sets.</p><p>You can use the Bulk API to process jobs in serial or parallel mode. Processing batches serially means running them one after another, while processing batches in parallel means running multiple batches simultaneously.</p><p></p><p><strong>Note:</strong> When you run a Bulk API job, processing more batches in parallel means giving that job a higher degree of parallelism, giving your overall run better data throughput.</p> |

<figure><img src="../../../../.gitbook/assets/image (1127).png" alt="" width="473"><figcaption></figcaption></figure>

16. Click **`Run`**.

#### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (1128).png" alt=""><figcaption></figcaption></figure>

1. **`Edit:`** Allows users to modify the process details according to their requirements.
2. **`Delete:`** Deletes a process.
3. **`Clone:`** Creates a copy (clone) of the selected process.
4. **`Log:`** Provides information about the execution of a process.

### Schema (Grid View) <a href="#schema-grid-view" id="schema-grid-view"></a>

This section lets you view the master object and its related information for the test environment setup job. For the setup run with disabled validation/workflow rules, ARM lists all the validation rules set under **`VR/WFR`** section. The UI lists all the workflow/validation rules; users must enable them for the disabled rules (if required).

<figure><img src="../../../../.gitbook/assets/image (1129).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1130).png" alt=""><figcaption></figcaption></figure>
