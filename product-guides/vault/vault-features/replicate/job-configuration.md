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

10. Make the required selections under the “Metadata” tab.
11. Navigate to the “Data” tab to make the rquired selection(s).
12. Schema Viewer:

    The schema viewer feature in Vault provides a structured view of parent and child relationships for Salesforce objects. This capability enables efficient navigation, selection, and dependency management while configuring data operations. Enhanced search controls, visual indicators, and guided navigation improve usability when working with complex object hierarchies.

    1. **Accessing Account Hierarchy**
       1. From the Edit Configuration screen, objects are displayed in a tabular list under the Data step.
       2.  Selecting the Hierarchy icon corresponding to an object opens the Account Hierarchy view.

           <figure><img src="../../../../.gitbook/assets/image (2359).png" alt=""><figcaption></figcaption></figure>
       3. The hierarchy view opens in a modal window, preserving the current configuration context.
    2. **Hierarchy Layout and Navigation**
       1. The selected object is displayed as the root node of the hierarchy.
       2.  Child objects are listed beneath the root, reflecting direct and indirect relationships.

           <figure><img src="../../../../.gitbook/assets/image (2360).png" alt=""><figcaption></figcaption></figure>
       3. Expand and collapse controls allow traversal across multiple hierarchy levels.
       4. Each object card displays:
          * Object name
          * Relationship type (Lookup or Master-Detail)
          * Selection checkbox
          * Visual hierarchy connector
    3. Search Functionality within Hierarchy
       1. The search bar is available at the top of the hierarchy view.
       2.  As typing begins in the search bar:

           1. Matching objects within the current hierarchy are highlighted.
           2. The info icon is automatically opened the first time typing is initiated.

           <figure><img src="../../../../.gitbook/assets/image (2361).png" alt=""><figcaption></figcaption></figure>
    4. The info icon can be manually reopened at any time by selecting the icon.
    5.  **Search Help (Info Icon)**

        The Search Help panel explains how search operates within the hierarchy:

        <figure><img src="../../../../.gitbook/assets/image (2367).png" alt=""><figcaption></figcaption></figure>

        1. **Typing**
           1. Highlights matching objects only within the currently displayed hierarchy.
           2. Does not change navigation or hierarchy depth.
           3. **Selecting from results**
              1. Performs a global hierarchy search.
              2. Automatically navigates to the object’s location within the schema tree.
    6.  **Search Direction Options**

        The Search Direction dropdown controls how search results are evaluated:

        1. **Children Only**
           * Searches only downstream child objects of the current root.
        2. **Parents Only**
           * Searches only upstream parent objects.
        3.  **Both (Parents & Children)**

            Searches across the entire hierarchy path.
    7.  If no valid path exists for the selected direction, a contextual message is displayed indicating that the object is not reachable from the current root.

        <figure><img src="../../../../.gitbook/assets/image (2362).png" alt=""><figcaption></figcaption></figure>
    8. **Search Results Feedback**
       1. **A result banner displays:**
          * Number of matches found on the current page.
            * Navigation arrows to move between matches.
       2.  **When a match is located successfully:**

           * A confirmation message indicates the object has been found.

           The hierarchy scrolls automatically to the object’s position.
    9. “Only Matches” Toggle
       1.  The Only Matches toggle is available alongside search results.

           <figure><img src="../../../../.gitbook/assets/image (2363).png" alt=""><figcaption></figcaption></figure>
    10. **When enabled:**
        1. Only objects matching the search criteria are displayed.
        2. Non-relevant hierarchy nodes are temporarily hidden.
    11. **When disabled:**
        1. The full hierarchy view is restored.
    12. **Root Object Navigation**
        1. The Root option is displayed at the top of the hierarchy view.
        2.  Clicking the Root option redirects the view back to the root object of the hierarchy.

            <figure><img src="../../../../.gitbook/assets/image (2364).png" alt=""><figcaption></figcaption></figure>
    13. This action resets the navigation context without clearing selected objects.
    14. **Path and Navigation Indicators**
        1.  A breadcrumb-style Path indicator displays the traversal route from the root object to the selected object.

            <figure><img src="../../../../.gitbook/assets/image (2365).png" alt=""><figcaption></figcaption></figure>
    15. A Go Back option allows navigation to the previous hierarchy level.
    16. A Returning to indicator clarifies the navigation context when moving back up the hierarchy.
    17. **Object Selection Behaviour**
        1. Selecting an object automatically selects dependent objects based on relationship rules.
        2. Objects selected due to dependency are visually marked.
        3. If cascading relationships exist:
           * A Cascade Delete indicator is shown for impacted child objects.
        4. Deselection follows dependency rules to prevent inconsistent configurations.
    18. **Visual Indicators and States**
        1. Highlighted text indicates active search matches.
        2. Color-coded badges differentiate:
           * Root objects
           * Selected objects
    19. **Saving Hierarchy Configuration**
        1.  The Save button persists all selections made within the hierarchy view.

            <figure><img src="../../../../.gitbook/assets/image (2366).png" alt=""><figcaption></figcaption></figure>
        2. Validation is performed before saving to ensure dependency consistency.
        3. On successful save, the hierarchy modal closes and returns to the configuration screen.
    20. **Key Functional Notes**
        1. Clicking the Root option always redirects to the root object.
        2. The info icon auto-opens only on the first typing interaction and remains manually accessible thereafter.
        3. Enabling Only Matches limits results strictly to relevant search outcomes without altering selection state.
    21. **Summary**

        The schema viewer feature in Vault enables precise object selection, dependency awareness, and efficient navigation across complex schemas. Enhanced search controls, guided feedback, and visual indicators ensure clarity, accuracy, and confidence while configuring data operations.
13. Click on the following sections and make the required selections:

    * **Include all child objects:** This selection ensures that all the child’s directly related and recursively related objects will be included.
    * **Mappings:** The user can click open and observe how the fields have been mapped for data transfer between the environments.

    <figure><img src="../../../../.gitbook/assets/image (92) (1).png" alt=""><figcaption></figcaption></figure>

*   **Records**: The user can select the records by clicking the icon under the “Records” column.<br>

    <figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **Search Text:** The user can search the fields.
* **Slider:** By enabling and disabling the slider, the user can make the search case sensitive or case-insensitive
* **Choose File**: The user can input the file using this option..
* **Change View**: The user can the additional fields required to be displayed on the page and can remove the fields that are not required.

<figure><img src="../../../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

11. **Masking Rules:** The user can create and publish the rules under this section.
12. The user clicks on the “New Masking Rule” button to create the rule.
    * The rules that are created in a ‘Job Config’ will be specific to that unless it is published.

![](<../../../../.gitbook/assets/8 (1) (1).png>)

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
17. On completing all the required actions, the user can click “Next” to continue to the “Config Details” section.<br>

    <figure><img src="../../../../.gitbook/assets/image (1555).png" alt=""><figcaption></figcaption></figure>
18. The user can fill in all required detail for the “Config Details”:

    * **Replicate Config Label**: The user can enter the name of the config to be created.
    * **Batch Size**: The user can specify the custom batch size and which Vault will utilize for processing the data.
    * **Email Notification**: The email to which the notifications can be triggered and sent.
    * The user can switch on all the required triggers available on the page.
    * **Schedule**: The user can set a custom schedule through the “Schedule” option available. The user’s set schedule will be utilized to run the job at different intervals.
    * **Metadata**: The user can observe the selected ‘meta data’ components during the config creation.
    * **Data:** The user can observe the objects that are selected during the config creation.
    * On completing all the required selections, the user can select either “Save” or “Save & Run”.

    <figure><img src="../../../../.gitbook/assets/image (1556).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (1557).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (1558).png" alt=""><figcaption></figcaption></figure>
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

1.  Every entry has the following actions: Run, Edit, Clone, Schedule, & Delete.<br>

    <figure><img src="../../../../.gitbook/assets/image (1560).png" alt=""><figcaption></figcaption></figure>
2.  **Run:** By clicking on the run icon, the following “Select Data to Replicate” screen will pop up.

    * Clicking “Replicate Now” will trigger the job and will create a new entry on the “Job History” page.
    * The user can verify and update any/all the details provided by the user during the “Job Config” creation.
    * Any changes or updates done to the “Config” created will only be applicable to the entry created in the “Job History” section. The Config will remain as it is created in its original state.

    <figure><img src="../../../../.gitbook/assets/image (1559).png" alt=""><figcaption></figcaption></figure>
3. **Edit**: If the user clicks on the edit icon, the user will land on the edit flow of the Config, and, the user can perform modifications to the “Job Config” created.
   * The changes made to the config will affect the config entirely.
4.  **Clone**: Clicking on the clone icon will pop the “Replicate Config” window to the user.

    * The user can select the “Source” and “Destination” ORGs and enter the label and click “Clone” to commence the clone operation.
    * The “Masking Rules” of the selected destination ORG, will be displayed to the user for selection.
    * On clicking 'Clone', an entry will be created on the “Job History” page.

    <figure><img src="../../../../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>


5.  **Additional Cloning Validations:**

    1.  ### Feature Details

        When the cloning of a job is initiated, the following notification will be displayed upon identifying any differences between environments.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

    1.  For any changes identified, the respective differences will be identified and displayed under the “Objects, Fields, Record Types and Picklist Values”.

        1. A warning can be observed on the top of the pop-up, which states that the target environment is missing the respective metadata.

        <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

        1.  Please verify the following information displayed on the pop-up and may continue to clone by clicking on “CONFIRM”.

            Only on user confirmation by clicking on “CONFIRM” button the replication will be initiated.
6.  **Schedule**: Will set a schedule for the config to automatically run periodically.

    * On clicking the “Schedule” icon, the “Replication Config Schedule” will be displayed to the user.
    * The user can select all the required entries to set the schedule.
    * On completing the required selection, the user can click on the “Save Schedule” button to save/set the schedule to the config being edited.

    <figure><img src="../../../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>
7. **Delete**: Will delete the CONFIG from the list of configs available. If a config is deleted, the corresponding job in the history will not be deleted.

### Excluding Feed Items

Vault now automatically identifies and excludes system-generated FeedItems during the Replicate processes. This ensures these items do not cause any failures during the operation.

#### Key Features

1. **Automatic Identification**: System-generated FeedItems are detected and excluded without requiring manual intervention.
2. **Error Prevention**: By excluding these FeedItems, potential errors during Replicate processes are avoided.
3. **Logging for Transparency**: All excluded FeedItems are logged for tracking purposes, providing clear visibility into the process.

#### Logs

The following is a sample log for reference, showing the excluded system-generated Feeditems:

<figure><img src="../../../../.gitbook/assets/image (1576).png" alt=""><figcaption></figcaption></figure>

#### Replicate Log

Refer to these logs to verify the exclusions and ensure smooth operations during Replicate processes.
