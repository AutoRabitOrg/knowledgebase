# Job Configuration

## Feature Overview

This is a reusable template that can be used to run, clone, and create a job every time a new job begins. This allows you to create a job in the replicate module and reuse the configuration as long as it is required, eliminating the need to recreate the job each time you need to work on the ‘Replicate’ module.

## Step-by-Step Guide

When creating the job configuration, select from: Backup, Hierarchical Backup, Archive, or Salesforce Live Data.

### Job Configuration – Backup, Hierarchical Backup & Archive

1. Access the “Job Config” under the “Replicate” module and create the “New Replicate Config” as shown below.

<figure><img src="../../../../.gitbook/assets/image (86) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. On clicking “New Replicate Config,” you will be prompted with “Replicate Config” with the dropdowns “Source”, “Destination”, and “Replicate Source.”

<figure><img src="../../../../.gitbook/assets/image (87) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Replicate Source has the following values:
   * Backup
   * Hierarchical backup
   * Archive
   * Salesforce Live Date
4. _**For any selection of Backup, Hierarchical Backup & Archive.**_
5. Go to the **“Replicate Config”** page:

<figure><img src="../../../../.gitbook/assets/image (88) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. The following options are available to select:
   * **`Source Org:`** Source of the data for the Replicate operation
   * **`Destination Org:`** Destination where the data will be moved during the Replicate operation
   * **`Replicate Source:`** Defines the kind of data that will be sourced to the Replicate operation
   * **`Configurations:`** For the “Replicate Source” selected, provides the available configurations under the “Replicate Source”
7. You also have the table with the list of configurations created for the source selected.
8. Select the required ‘configs’ from the list of ‘configs’ selected.
9. On clicking “Next”, you will land on the “Select Components” page. There, you'll see “Metadata” and “Data” tabs.

<figure><img src="../../../../.gitbook/assets/image (89) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (91) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. The user can make the required selections under both the “Metadata” & “Data” tabs and continue to the next section.

    * **Include all child objects:** This selection ensures that all the child’s directly related and recursively related objects will be included.
    * **Mappings:** The user can click open and observe how the fields have been mapped for data transfer between the environments.

    <figure><img src="../../../../.gitbook/assets/image (92) (1).png" alt=""><figcaption></figcaption></figure>

*   **Records**: The user can select the records by clicking the icon under the “Records” column.\


    <figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>
* **Search Text:** The user can search the fields.
* **Slider:** By enabling and disabling the slider, the user can make the search case sensitive or case-insensitive
* **Choose File**: The user can input the file using this option..
* **Change View**: The user can the additional fields required to be displayed on the page and can remove the fields that are not required.

<figure><img src="../../../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

11. **Masking Rules:** The user can create and publish the rules under this section.
12. The user clicks on the “New Masking Rule” button to create the rule.
    * The rules that are created in a ‘Job Config’ will be specific to that unless it is published.

![](<../../../../.gitbook/assets/8 (1).png>)

13. The following page will be displayed to the user on clicking the “New Masking Rule” button.

<figure><img src="../../../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

14. The user has to input the following for the creation of a rule:

    * **Rule Name:** Label/Name of the rule being created
    * **Select Object:** The object on which the rule is being created
    * **Field Type:** Type of field on which the rule is being created
    * **Masking Style:** Defines the pattern which will replace the data of the ‘Field Type” selected
    * **“Add To VaultData Masking Rules List”:** By selecting this checkbox, the user can directly add this rule to the global rules list.
    * The user can also publish a rule after saving the rule, by clicking the publish icon on the rule.

    <figure><img src="../../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>
15. Once the user clicks the “Publish”, the following popup is displayed to the user for confirmation.

<figure><img src="../../../../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

16. On clicking “OK”, the rule will be published and available with the global list of rules associated with the ORG.
17. On completing all the required actions, the user can click “Next” to continue to the “Config Details” section.

![](<../../../../.gitbook/assets/12 (2).png>)

18. The user can fill in all required detail for the “Config Details”:

    * **Replicate Config Label**: The user can enter the name of the config to be created.
    * **Batch Size**: The user can specify the custom batch size and which Vault will utilize for processing the data.
    * **Email Notification**: The email to which the notifications can be triggered and sent.
    * The user can switch on all the required triggers available on the page.
    * **Schedule**: The user can set a custom schedule through the “Schedule” option available. The user’s set schedule will be utilized to run the job at different intervals.
    * **Metadata**: The user can observe the selected ‘meta data’ components during the config creation.
    * **Data:** The user can observe the objects that are selected during the config creation.
    * On completing all the required selections, the user can select either “Save” or “Save & Run”.

    <figure><img src="../../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>
19. **Save:** Will save the config created. It will not trigger the job automatically while saving the job.
    * The user will observe “Save” on the “Replication Config Info” page if “Save” is selected.
20. &#x20;**Save & Run:** Will save the config created and will trigger the job created to run, and, redirect the user to the “Job History” page.
    * The user can observe the related job running on the “Job History” page.
    * The user will see “Save & Run” on the “Replication Config Info” page if “Save & Run” is selected.

### Job Configuration – Salesforce Live Data

1. The user selects “Salesforce Live Data” on the “Replicate Config” window.

<figure><img src="../../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

2. If the user selects “Salesforce Live Data”, then the user will land directly on the “Select Components” section of the Flow.
3. The User Can Verify Both The “Metadata” & “Data” tabs to go through the metadata components and objects in the data tabs, as shown below:

<figure><img src="../../../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

4. **Include all child objects:** Ensures that all the child’s directly related and the recursively related child’s will also be included.
   * To ensure optimal performance, only fixed objects are allowed to be selected. If any further child objects are to be selected, the selection can be made by going through the schema.
5.  **Mappings**: The user will click on the mappings to map the fields on the source against the fields on the destination.&#x20;

    * The mappings section contains three tabs: Fields, Record Type & Related Picklist.&#x20;
    * The user can perform 'Automap' & 'Clear All' on the values of the tabs.

    <figure><img src="../../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>
6. **Fields**: The fields on source are mapped against the field(s) on the destination.
7. **Record Type**: The record type on the source is mapped against the record type on the destination.
8. **Restricted Picklist**: On selecting the ‘restricted picklist’ from the source, the source field values will be mapped against the field values on the destination.
9. On completing the required selection on the tabs under the mappings, the users can perform ‘**Apply’ & ‘Clear All.’**
10. **Filters**: The user can input the query and can set the filter criteria for the records to be filtered. Once the user clicks “Publish”, a popup is displayed to the user for confirmation.
11. On clicking “OK” the rule will be published and be available with the global list of rules associated with the ORG.
12. On completing all the required actions, the user can click “NEXT” to continue to the “Config Details” section.
13. **Ignore Failed Records:** Enabling it will ensure that the nulls available in the source ORG will be pushed to the destination ORG.
14. **Save:** This saves the config created. It will not trigger the job automatically while saving the job.

    The user will see “Save” on the “Replication Config Info” page if “Save” is selected.
15. **Save & Run:** Will save the config created and will trigger the job created to run and redirect the user to the “Job History” page.
    * The user can observe the related job running on the “Job History” page.
    * The user will observe “Save & Run” on the “Replication Config Info” page if “Save & Run” is selected.

### Job Configuration – Actions

1. Every entry has the following actions: Run, Edit, Clone, Schedule, & Delete.

<figure><img src="../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

2.  **Run:** By clicking on the run icon, the following “Select Data to Replicate” screen will pop up.

    * Clicking “Replicate Now” will trigger the job and will create a new entry on the “Job History” page.
    * The user can verify and update any/all the details provided by the user during the “Job Config” creation.
    * Any changes or updates done to the “Config” created will only be applicable to the entry created in the “Job History” section. The Config will remain as it is created in its original state.

    <figure><img src="../../../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>
3. **Edit**: If the user clicks on the edit icon, the user will land on the edit flow of the Config, and, the user can perform modifications to the “Job Config” created.
   * The changes made to the config will affect the config entirely.
4.  **Clone**: Clicking on the clone icon will pop the “Replicate Config” window to the user.

    * The user can select the “Source” and “Destination” ORGs and enter the label and click “Clone” to commence the clone operation.
    * The “Masking Rules” of the selected destination ORG, will be displayed to the user for selection.
    * On clicking 'Clone', an entry will be created on the “Job History” page.

    <figure><img src="../../../../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>
5.  **Schedule**: Will set a schedule for the config to automatically run periodically.

    * On clicking the “Schedule” icon, the “Replication Config Schedule” will be displayed to the user.
    * The user can select all the required entries to set the schedule.
    * On completing the required selection, the user can click on the “Save Schedule” button to save/set the schedule to the config being edited.

    <figure><img src="../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>
6. **Delete**: Will delete the CONFIG from the list of configs available. If a config is deleted, the corresponding job in the history will not be deleted.
