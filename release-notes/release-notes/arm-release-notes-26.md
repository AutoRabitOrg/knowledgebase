---
hidden: true
---

# DataLoader + DataLoader Pro Release Notes

## DataLoader + DataLoader Pro Release Notes **26.3.13**

**Release Date:** **27 September 2026**

#### Accurate Save Messaging for DataLoader Pro Jobs

When **Skip mappings** was selected while saving a DataLoader Pro job, the application could display an incorrect message. Save-message handling was corrected to accurately reflect the selected mapping behavior. The correction applies to new and existing jobs with single or multiple objects in both the existing and new interfaces.

#### Preserved Query Changes in Cloned DataLoader Extract Jobs

Changes made to a SOQL query while cloning a DataLoader Basic Extract Job were not retained, causing the cloned job to use the original query. Query-modification handling was corrected so the edited query is saved with the cloned job. The cloned job now executes using the updated query criteria in both the existing and new interfaces.

***

## DataLoader + DataLoader Pro Release Notes **26.3.12**

**Release Date:** **20 Sep 2026**

#### Reliable Loading for Test Environment Jobs <a href="#id-4.-automatic-timeout-status-for-stalled-jobs" id="id-4.-automatic-timeout-status-for-stalled-jobs"></a>

Resolved an issue where editing a Test Environment job repeatedly requested Salesforce organization and object data, leaving the page stuck in a loading state. Job initialization now runs only once and prevents duplicate requests. Users can open and edit Test Environment jobs normally. Automatic Timeout Status for Stalled Jobs

Jobs that remain in progress for more than 24 hours are now automatically marked as **Timeout** when the status scheduler runs. This prevents outdated job statuses from remaining active indefinitely. The update applies across DataLoader Jobs, and Feature Management operations.

#### Correct Job Statuses Following Instance Restarts <a href="#id-6.-correct-job-statuses-following-instance-restarts" id="id-6.-correct-job-statuses-following-instance-restarts"></a>

Jobs interrupted by an instance restart no longer remain indefinitely in an **In Progress** state. Interrupted jobs are now marked as **Aborted** or **Failed**, preventing stale records from blocking later processing. The correction covers DataLoader Jobs, and Feature Management activities.

#### Automatic Recovery of Stalled nCino and DataLoader Jobs <a href="#id-7.-automatic-recovery-of-queued-ci-job-commits" id="id-7.-automatic-recovery-of-queued-ci-job-commits"></a>

DataLoader jobs could remain in an **In Progress** state when processing was interrupted or the status was not updated for more than 24 hours. Status-handling logic was corrected to move these stalled jobs to the appropriate terminal status. This prevents inactive jobs from appearing to run indefinitely and ensures that subsequent DataLoader processing can continue normally.

***

## DataLoader + DataLoader Pro Release Notes **26.3.10**

**Release Date:** **6 Sep 2026**

#### Correct Empty Relationship Fields in Data Loader Exports

Resolved an issue where empty User Role or Manager fields could incorrectly display the user’s name in exported CSV files. Data Loader now leaves these relationship fields blank when no value is available. The correction applies to normal and aggregate queries in both the existing and new interfaces.

***

## DataLoader + DataLoader Pro Release Notes **26.3.9**

**Release Date:** **30 Aug 2026**

#### Data Loader Pro Job Configuration Settings Not Retained <a href="#id-5.-data-loader-pro-job-configuration-settings-not-retained" id="id-5.-data-loader-pro-job-configuration-settings-not-retained"></a>

Resolved an issue where selected Data Loader Pro job settings were not retained during execution.

Options such as disabling workflows and validation rules and processing null values are now saved and applied correctly.

***

## DataLoader + DataLoader Pro Release Notes **26.3.8**

**Release Date:** **23 Aug 2026**

#### DataLoader Pro Org Re-Registration Consistency

Corrected inconsistent behavior between manual and scheduled executions after a Salesforce source org was re-registered with different name casing. The system now correctly identifies the source and destination orgs regardless of case sensitivity in the registration name.

***

## DataLoader + DataLoader Pro Release Notes **26.3.7**

**Release Date:** **16 Aug 2026**

#### **Summary Side Panel Alignment Fix**

The Summary side pop-up in Dataloader Pro and DL Config now displays content with proper left alignment. This reduces unused blank space, improves readability, and helps prevent long values from appearing clipped at the right edge.

***

## DataLoader + DataLoader Pro Release Notes **26.3.6**

**Release Date:** **09 Aug 2026**

#### External ID Mapping Persistence

Addressed a DataLoader issue reported through Support Case, where saved custom **External ID** field mappings reverted after a browser refresh. The mapping now persists as expected, helping users retain intended source-to-destination field relationships across sessions.

***

## DataLoader + DataLoader Pro Release Notes **26.3.5**

**Release Date:** **02 Aug 2026**

#### DataLoader Pro Job Visibility for Subusers (DevHub Orgs) <a href="#dataloader-pro-job-visibility-for-subusers-devhub-orgs" id="dataloader-pro-job-visibility-for-subusers-devhub-orgs"></a>

Fixed an issue where Dataloader Pro jobs created by a subuser were not visible to the same subuser who created them. Jobs now correctly appear for both the creator (subuser) and admin users, ensuring consistent ownership-based visibility.

***

## DataLoader + DataLoader Pro Release Notes **26.3.2**

**Release Date:** **12 July 2026**

#### Knowledge KAV language filter not auto-populating in New UI <a href="#dt-13616-knowledge-kav-language-filter-not-auto-populating-in-new-ui" id="dt-13616-knowledge-kav-language-filter-not-auto-populating-in-new-ui"></a>

Fixed an issue in the New UI where the **Language** filter on the Knowledge KAV object did not prefill with the existing language value. The filter behavior now matches the Old UI.

***

## DataLoader & DataLoader Pro Release Notes **26.3.1**

**Release Date:** **05 June 2026**

#### Query Editor Workflow for Dynamic and Custom Queries – DL & DL PRO

The Query Editor in DataLoader Basic and DataLoader Pro now supports two modes: **Query Builder Mode** (build queries using field selections, filters, and order-by options) and **Manual Query Edit Mode** (edit queries directly in the text editor). Users can seamlessly switch between modes with clear confirmation prompts, and the system correctly manages state transitions to prevent conflicts between manual edits and dynamic query generation.

***

## DataLoader Pro Release Notes **26.2.11**

**Release Date:** **14 June 2026**

#### DL Data Retention Policy Fix <a href="#dt-13273-ncino-and-dl-data-retention-policy-fix" id="dt-13273-ncino-and-dl-data-retention-policy-fix"></a>

Fixed missing components in the data retention policy for "DL & DL PRO". Single DataLoader bulk file deletion was not being executed, and "DL & DL PRO" S3 backup deletions were targeting the wrong bucket. ARM data retention settings now apply to "DL & DL PRO" by default without requiring a separate checkbox.

#### DataLoader Pro Query Failure on Knowledge\_\_kav Object <a href="#dt-13345-dataloader-pro-query-failure-on-knowledge__kav-object-support-case-234338" id="dt-13345-dataloader-pro-query-failure-on-knowledge__kav-object-support-case-234338"></a>

Fixed an issue where DataLoader Pro jobs failed when a custom query was applied to the `Knowledge__kav` object. The error occurred because the system incorrectly appended a `WHERE` clause to queries that already contained filtering conditions (e.g., `LIMIT`), resulting in a syntax error. Query construction logic has been corrected to handle Knowledge objects properly.

***

## DataLoader Pro Release Notes **26.2.7**

**Release Date:** **17 May 2026**

#### **ZIP File Attachments Not Migrating via Data Loader Pro**

Resolved an issue where ZIP file attachments associated with HTML Report object records were not being migrated from Production to sandbox environments using Data Loader Pro. PDF and other attachment types migrated correctly, but ZIP files were silently skipped. All attachment types now migrate as expected.

***

## DataLoader Pro Release Notes **26.2.5** <a href="#release-notes-26.2.3" id="release-notes-26.2.3"></a>

**Release Date:** **03 May 2026**

**DataLoader Pro Job Result Inaccessible**\
Resolved an issue where result files from completed DataLoader Pro jobs were not accessible. Users can now successfully view and download job results as expected.

***

## DataLoader Release Notes 26.2.4

**Release Date: 26 April 2026**

**Data Retention Policy for nCino & DataLoader** — Admins can now enable automatic cleanup of unused jobs (DataLoader processes, Feature Deployments, CI Job histories, etc.) via a configurable retention policy under My Account.

***

## DataLoader Release Notes 26.2.3

**Release Date: 26 April 2026**

**Dataloader Extract Job not returning all field columns**&#x20;

* When using a DataLoader Extract job with a WHERE IN clause, the downloaded file did not include all field columns from the query. Removing the WHERE IN clause returned all columns correctly. Fixed to ensure all queried fields are present in the extracted output, regardless of clause type.

***

## DataLoader Pro Release Notes 26.2.1 <a href="#release-notes-version-26.1.12" id="release-notes-version-26.1.12"></a>

**Release Date:** **05 April 2026**

**New UI: DataLoader Pro CSV validation incorrect**

Fixed DataLoader Pro in the new UI so invalid CSV input is correctly validated and flagged.

***

## DataLoader Release Notes 26.2.1

**Release Date:** **05 April 2026**

**DataLoader Basic job stuck / Salesforce error during extract**

Fixed an issue where DataLoader Basic extract jobs showed a stuck status and unexpected Salesforce errors during execution.

**Fields and query not loading when editing extract job**

Fixed DataLoader extract job editing so fields and the saved query now load correctly.

***

## DataLoader Pro Release Notes 26.1.13 <a href="#release-notes-version-26.1.12" id="release-notes-version-26.1.12"></a>

**Release Date:** **29 March 2026**

**DataLoader Pro - Pagination Issue in DataLoader Pro (New UI)**

Resolved an issue where pagination did not function correctly after fetching objects in DataLoader Pro job configuration. Pagination now works as expected when navigating through master objects.

***

## DataLoader Release Notes 26.1.13 <a href="#release-notes-version-26.1.12" id="release-notes-version-26.1.12"></a>

**Release Date:** **29 March 2026**

**DataLoader Basic** - **Concurrent Job Validation in Data Loader Basic (New UI)**

Fixed an issue where multiple jobs could be triggered for the same org without proper validation. The system now correctly prevents concurrent job execution and displays an appropriate error message when a job is already in progress.

***

## Data Loader Pro Release Notes 26.1.12 <a href="#release-notes-version-26.1.11" id="release-notes-version-26.1.11"></a>

**Release Date: 22 March 2026**

**Flexible Result File Downloads**\
Users can now download Dataloader Pro job results in their preferred file format, making it easier to consume and share output data. This enhancement allows teams to align exports with their reporting standards or downstream tools without needing manual conversions after download.

**Default Columns in Dataloader UI**\
Default column configurations have been introduced and corrected across Dataloader Basic and Pro screens. Previously, no default view options were applied, forcing users to manually adjust columns each time they accessed a screen. With this fix, users now see a sensible default column set, improving usability and reducing setup time for common workflows.

**Correct Status for Aborted DL Pro Jobs**\
Aborted DL Pro jobs from the old UI now show an accurate status instead of incorrectly appearing as “Failed” in both the old and new interfaces. This fix improves the reliability of job status reporting, enabling teams to distinguish between genuine failures and intentional aborts, and to analyze actual failure trends more accurately.

***

## DataLoader Release Notes 26.1.12 <a href="#release-notes-version-26.1.11" id="release-notes-version-26.1.11"></a>

**Release Date: 22 March 2026**

**Accurate Count(id) in DL Basic Extract**\
The Count(id) column now correctly displays record counts in the new UI for DL Basic Extract jobs. Earlier, the column appeared empty in the new UI while still showing values in the old UI, leading to confusion and forcing users to cross-check between interfaces. The fix aligns both UIs so users can confidently rely on the new interface for record counts.

**Accurate Count(id) in DL Basic Extract**\
The Count(id) column now correctly displays record counts in the new UI for DL Basic Extract jobs. Earlier, the column appeared empty in the new UI while still showing values in the old UI, leading to confusion and forcing users to cross-check between interfaces. The fix aligns both UIs so users can confidently rely on the new interface for record counts.

***

## DataLoader Pro Release Notes 26.1.11&#x20;

**Release Date: 15 March 2026**

**DL Pro – Corrected Record Count Display for Objects with Similar Names**

An issue was resolved where the **success count and error count** were displayed incorrectly in the **DL Pro results table** when multiple objects had the same name but different prefixes. The system now correctly distinguishes between such objects, ensuring that **success, error, and extracted record counts** are displayed accurately in the DataLoader parent and child relations result table.

***

## DataLoader Release Notes 26.1.11&#x20;

**Release Date: 15 March 2026**

**Deployment from Deployment History Fix**

An issue was resolved where deploying a dataset directly from the **Deployment History** screen resulted in the error _“Unable to fetch feature deployment iteration objects.”_ This has been fixed, and datasets can now be deployed successfully from the **Deployment History** view as expected.

**Relational Compare Fix in Deploy using Template**

An issue was resolved where performing a **relational compare** during **Deploy using Template** failed with the error _“Cannot retrieve data from Salesforce with the unique identifier.”_ This occurred when parent records were not fetched during the relational compare process. The issue has been fixed, and relational compare now retrieves data correctly and proceeds without errors.

**Aggregate Query Handling Improvement**

An issue was addressed in **DataLoader** where running aggregate SOQL queries resulted in the error _“Field must be grouped or aggregated.”_ Query validation and extract operations have been improved to correctly support relational field extraction when using **GROUP BY** and **ORDER BY** clauses, ensuring aggregate queries execute successfully.

***

## DataLoader Pro Release Notes 26.1.10&#x20;

**Release Date: 08 March 2026**

#### Processing Rule Migration – Parent-Child Relationship Fix

Resolved an issue where **Processing Rule child records were not created during sandbox migration**, causing all rules to be imported as parent records.

The migration logic has been updated to correctly handle **self-referential parent-child relationships**, ensuring that both parent and associated child rules are migrated as expected.

***

## DataLoader Pro Release Notes 26.1.9&#x20;

**Release Date: 01 March 2026**

#### Hierarchical Object Handling – Parent Resolution Consistency

Enhanced object hierarchy handling to ensure consistent behavior between job configuration and execution.

Previously, in cases where an object (e.g., **Loan**) functioned both as a child (in the UI) and as a parent (in the hierarchy), additional parent objects were fetched during execution even if they were not selected during job creation.

With this fix, only the objects selected during configuration will be processed during execution, unless mandatory parent dependencies are explicitly required.

***

## DataLoader Pro Release Notes 26.1.6

**Release Date:** **08 February 2026**

#### Improved Filtered Data Migration <a href="#dl-pro-improved-filtered-data-migration" id="dl-pro-improved-filtered-data-migration"></a>

Resolved an issue where data migrations could fail when filters were applied to master objects. The system now ensures that all required related records are included automatically, preventing migration failures due to missing references.

#### Selective Deployment – Improved Log Visibility <a href="#selective-deployment-improved-log-visibility" id="selective-deployment-improved-log-visibility"></a>

Fixed an issue where data retrieval logs were not visible during selective deployments. Logs are now displayed correctly and only when applicable, providing clearer visibility into deployment progress.

***

## DataLoader Pro Release Notes 26.1.4

**Release Date:** **25 January 2026**

#### DataLoader Pro – FeedItem & ContentDocumentLink Status Handling <a href="#dl-pro-feeditem-and-contentdocumentlink-status-handling" id="dl-pro-feeditem-and-contentdocumentlink-status-handling"></a>

Improved DataLoader Pro job execution for Account migrations by correctly handling field mappings for objects processed via **Bulk API v1**, ensuring accurate status reporting for related objects such as **FeedItem** and **ContentDocumentLink**.

#### DataLoader Pro – Parent Record Handling with Filters <a href="#dl-pro-parent-record-handling-with-filters" id="dl-pro-parent-record-handling-with-filters"></a>

Enhanced DataLoader Pro data retrieval logic to ensure that when filters are applied, **all related parent records (including self-referenced and multi-level parents)** are automatically identified and migrated up to the top level, preventing partial data migration when filters are used.

#### DataLoader Pro – Batch Size Handling for Screen Section Objects <a href="#dl-pro-batch-size-handling-for-screen-section-objects" id="dl-pro-batch-size-handling-for-screen-section-objects"></a>

Fixed an issue where DataLoader Pro jobs completed with a “No Records” status when a batch size was specified for Screen Section objects by improving handling of recursive processing scenarios.

***

## DataLoader Release Notes 26.1.4

**Release Date:** **25 January 2026**

#### DataLoader Extract – Limit Not Applied <a href="#data-loader-extract-limit-not-applied" id="data-loader-extract-limit-not-applied"></a>

Fixed an issue where the **Limit** specified in the Extract Job configuration pop-up was not being honored during execution, causing all records to be extracted instead of the defined subset.

#### DataLoader – Insert Operation Stability

Fixed an issue where DataLoader insert jobs failed without producing success or error records by handling duplicate column generation during CSV preparation for lookup-mapped fields.

***

## DataLoader Pro Release Notes 26.1.3

**Release Date**: **18 January 2026**

#### **DataLoader - Validation and Workflow Rules Visibility Fix**

Resolved an issue where **Validation Rules and Workflow Rules** were not displayed in the Data Loader job pop-up when disabled during Insert, Update, or Upsert operations.

#### **DataLoader - Test Environment Dropdown Fix** <a href="#data-loader-test-environment-dropdown-fix" id="data-loader-test-environment-dropdown-fix"></a>

Fixed an issue where the **“All Groups”** dropdown remained disabled after creating a Data Loader job in the Test environment and required a manual page refresh. The dropdown is now enabled immediately, improving usability.

#### **DataLoader Pro - Custom Mapping Fix** <a href="#dl-pro-data-loader-pro-custom-mapping-fix" id="dl-pro-data-loader-pro-custom-mapping-fix"></a>

Resolved an issue where **Data Loader Pro jobs** failed when custom object mappings were selected. The issue has been fixed to ensure successful job execution with custom mappings.

#### DataLoader Pro - **Group Job Clone Filter Restoration Fix**

Resolved an issue where **object filters were not restored when cloning group jobs** in Data Loader Pro. Filters are now correctly retained and displayed after cloning.

#### **DataLoader Pro - Upsert Fix for Knowledge Objects** <a href="#data-loader-pro-upsert-fix-for-knowledge-objects" id="data-loader-pro-upsert-fix-for-knowledge-objects"></a>

Resolved an issue where **Data Loader Pro upsert jobs** processed zero records despite valid source data being present. The issue was fixed by correctly handling **external ID fields for Knowledge (KAV) objects**.

#### **DataLoader Pro - Skip Object Selection UI Fix** <a href="#skip-object-selection-ui-fix" id="skip-object-selection-ui-fix"></a>

Resolved an issue where the **Skip** checkbox was not reflected in the UI after an ancestor object was skipped. The selection state is now correctly saved and displayed.
