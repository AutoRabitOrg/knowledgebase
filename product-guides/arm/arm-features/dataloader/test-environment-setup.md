# Test Environment Setup

### Test Environment Setup: Overview <a href="#test-environment-setup-overview" id="test-environment-setup-overview"></a>

The test environment in ARM supports convenient data transfer from CSV files to destination sandboxes and helps reduce job execution time. This is particularly useful for validating data migration scenarios prior to full execution.

***

### Create a New Test Environment Setup <a href="#create-a-new-test-environment-setup" id="create-a-new-test-environment-setup"></a>

1. Navigate to the **DataLoader** module and select **DataLoader Test Environment Setup**.

<figure><img src="../../../../.gitbook/assets/image (1116).png" alt="Navigation to Data Loader Test Environment Setup module" width="332"><figcaption></figcaption></figure>

2. Click on **Create New Job**.

<figure><img src="../../../../.gitbook/assets/image (1117).png" alt="Button to initiate a new test environment job"><figcaption></figcaption></figure>

3. Select your **Destination Org**.

<figure><img src="../../../../.gitbook/assets/image (1118).png" alt="Dropdown to select destination Salesforce org"><figcaption></figcaption></figure>

4. Click **Login and Fetch Objects** to display all objects from the destination org.
5. Choose a **Master Object** from the list.

<figure><img src="../../../../.gitbook/assets/image (1119).png" alt="Master object selection screen"><figcaption></figcaption></figure>

6. Click the **Show Dependencies** icon to view hierarchical relationships with parent objects.

<figure><img src="../../../../.gitbook/assets/image (1120).png" alt="Dependency analysis button for the selected object"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1121).png" alt="Text-based dependency relationship view" width="342"><figcaption></figcaption></figure>

7. Use **Switch to Graph View** to see a visual hierarchy.

<figure><img src="../../../../.gitbook/assets/image (1122).png" alt="Graphical representation of object dependencies" width="395"><figcaption></figcaption></figure>

8. Under **Source of Data**, upload a `.zip` file containing the object-specific `.csv` files.

<figure><img src="../../../../.gitbook/assets/image (1123).png" alt="Upload interface for CSV zip files"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** The `.csv` file name must match the object’s API name. Uploading CSVs for parent objects is optional, but required if you want their records migrated too.
{% endhint %}

9. Provide a **Name** for the job and choose a **Job Group** to categorize it.
10. The **Master Object** and **External ID** will auto-populate.
11. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (1124).png" alt="Test environment setup form with master object details"><figcaption></figcaption></figure>

12. You’ll be redirected to the **Test Environment Setup Summary** page.
13. Click **Run** to initiate the data migration job.

<figure><img src="../../../../.gitbook/assets/image (1126).png" alt="Job summary page showing list of configurations and run option"><figcaption></figcaption></figure>

***

### Deployment Criteria Options

| Configurations               | Descriptions                                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disable Workflows**        | Temporarily disables Salesforce workflows during migration, and re-enables them afterward.                                                                                                                                 |
| **Disable Validation Rules** | Turns off validation rules to allow data migration. Rules are restored once the migration is complete.                                                                                                                     |
| **Use Bulk API**             | Uses Salesforce Bulk API to increase performance for large data volumes. Jobs can be processed in **serial** (one after another) or **parallel** (simultaneously). For faster data throughput, parallel mode is preferred. |

<figure><img src="../../../../.gitbook/assets/image (1127).png" alt="UI for selecting workflow, validation, and Bulk API options" width="473"><figcaption></figcaption></figure>

14. Click **Run** to execute the job.

***

### More Options <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (1128).png" alt="Action menu with edit, delete, clone, and log options"><figcaption></figcaption></figure>

1. **Edit:** Modify job settings.
2. **Delete:** Remove a job setup.
3. **Clone:** Create a duplicate of the configuration.
4. **Log:** View execution history and status.

***

### Schema (Grid View) <a href="#schema-grid-view" id="schema-grid-view"></a>

This section visualizes the master object schema and its dependencies. When validation or workflow rules are disabled, ARM displays these rules under the **VR/WFR** section. You can review and re-enable them manually if necessary.

<figure><img src="../../../../.gitbook/assets/image (1129).png" alt="Grid view showing object schema and relationship"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1130).png" alt="Section listing validation and workflow rules for review"><figcaption></figcaption></figure>
