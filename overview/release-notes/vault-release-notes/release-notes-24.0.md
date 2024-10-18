# Release Notes 24.0

## Vault 24.2.2 Release Notes

**Release Date: 18 October 2024**

* **UI Enhancements:** Improved UI for a smoother user experience in multiple areas.
* **Vault Connect Updates:** Now supports attachments with Salesforce External Objects, enabling a comprehensive view of archived data.
* **Organization Identification during Manual Backup Trigger:** Simplified identification of the Salesforce org initiating the backup, with clearer labels for a more streamlined and intuitive experience.

## Vault 24.2.1 Release Notes

**Release Date: 4 October 2024**

* **Improved Metadata Backups:** Enhancements have been made to metadata backups to better handle expected errors during retrieval from Salesforce.
* **FeedComment Restore/Replication:** Improved error handling ensures better support for FeedComment replication and restoration.
* **Improved Backup Performance**: Backup performance has been optimized for Salesforce environments with proxy settings enabled, resulting in faster backups.
* **Enhanced Support for Object Relationships in Restore/Replicate:** Relational integrity is now better maintained during restores and replications, even when object relationships in Salesforce do not follow standard naming conventions.
* **Improved Restore/Replicate Results**: The user experience for restore and replicate operations has been enhanced with an improved results presentation.
* **Log Enhancements**: Job logs have been upgraded to provide more detailed information about where time is being spent during job execution, improving transparency and troubleshooting.

## Vault 24.2 Release Notes

**Release Date: 24 Sep 2024**

#### **Overview**

AutoRABIT is thrilled to announce a series of significant enhancements to our platform. These updates are designed to elevate your experience, offering improved performance, enhanced security, and greater reliability. Below, you'll find detailed information on the key updates included in this release.

#### **Key Updates**

1. **Operating System Upgrade**
   * **Upgrade Details**: The platform's underlying operating system has been upgraded to the latest version.
   * **Benefits**:
     * **Enhanced Security**: The latest OS version includes critical security patches and updates to protect against vulnerabilities.
     * **Improved Performance**: Users will experience faster processing speeds and more efficient resource management.
2. **Core Libraries Upgrade**
   * **Upgrade Details**: We have upgraded the core libraries that support our platform's infrastructure.
   * **Benefits**:
     * **Boosted Security**: Updated libraries reduce the risk of security breaches by addressing known issues.
     * **Optimized Performance**: These upgrades enhance the overall performance, resulting in a smoother user experience.
3. **Database Version Upgrade**
   * **Upgrade Details**: The database powering our platform has been upgraded to a newer version.
   * **Benefits**:
     * **Smoother Operations**: The upgraded database improves transaction handling and data retrieval, leading to more reliable operations.
     * **Increased Reliability**: Users can expect reduced downtime and improved stability, ensuring a seamless experience.

### Vault v24.1.19

**3 July 2024**

1. **Enhanced Search Functionality:** Introduced “$” based search functionality to enable users to find precise results efficiently.
2. **Service Contracts & Price Book Fix:** Fixed an issue where restored service contracts and price book entries were not being recovered properly.
3. **Child Label Display Issue Resolved:** Resolved the problem of child labels displaying identical names across entries.
4. **Email Delivery for Deactivated Sub-users:** Corrected an issue where deactivated sub-users were still receiving emails.
5. **Case Object Relationship Fix:** Addressed a bug preventing relationships from being established with the Case object.
6. **Job Duration Display Fix:** Fixed the issue where job duration was inaccurately displayed as 1 second during processing.
7. **Special Character Handling:** Implemented a fix to properly handle and escape special characters.
8. **Salesforce Toggle State Issue:** Resolved an issue in which the “Auto-pick new objects and metadata in Salesforce” toggle appeared disabled, despite being enabled.

### Vault v24.1.18

**19 June 2024**

1. **Mail Notification Issue**: Scheduled job notifications were being sent to deactivated Admin users. This issue has been addressed.
2. **Duplicate Configuration Name Error**: When a duplicate name is entered in the connect section, an incorrect 500 internal server error was displayed.
3. **Updated Error Code**: The error code has been updated to correctly display a 400 series "Bad Request" status instead.

### Vault v24.1.17

**12 June 2024**

1. **Backend Failure Display Fix:** Failures were incorrectly shown due to users adding too many reference fields. The system now limits users to 40 reference fields.
2. **Custom Price Book Entry Automation:** Live replicate was failing to create entries in the standard price book, which is required by Salesforce. This process is now automated.
3. **Archival Report Expiration Fix:** Archival reports were not expiring after 7 days as intended. A fix ensures reports now expire 7 days after creation.
4. **Config ID Requirement:** The absence of a config ID in the script caused unintended actions for other clients. Config ID and client are now mandatory to prevent this.

### Vault v 24.1.16

**29 May 2024**

1. **Workflow Rule Reenablement After Restore/Replicate:** After completing the Restore or Replicate actions, the workflow rules are not being reenabled. The expected behavior is that these rules should automatically be reenabled once the Restore or Replicate process is completed.
2. **Config Details Display Fix:** A fix has been implemented to address an issue where the configuration details of the selected record IDs were not being displayed as expected.
3. **Logging for 'Unique Identifiers' Field Names:** The field names of the 'Unique Identifiers' were not being displayed. To resolve this, additional logging has been added. Now, if these fields are enabled, they will be logged accordingly.
4. **File Size Limit Increase:** The initial file size limit was set to 5MB. This limit has now been increased to 500MB, applicable to both the front end and backend.
5. **Serial Mode Logging Issue:** Even though customers selected 'serial mode,' the backend logs incorrectly showed it as 'parallel mode.' A fix has been implemented to ensure that the logs correctly reflect the selected serial mode.
6. **Email Body Logging Issue:** Previously, the email body was being printed in the logs along with email activity tracking. A fix has been applied to prevent the email body from being logged.
7. **Enhanced Log Failure Details:** The logs have been updated to provide more detailed information regarding the reasons for log failures.

### Vault 24.1.15

**22 May 2024**

1. **Thread Pool Implementation for Network Error:** Due to recurring network errors, a thread pool has been implemented to manage tasks more efficiently.
2. **Archive Module File Downloads:** Moving forward, all files downloaded from the Archive module will be automatically zipped before download.
3. **Query Column Display Adjustment:** The query column will now only be displayed at the criteria level, not at the object level, ensuring a more streamlined view.
4. **Separation of Synchronous and Asynchronous Methods:** The previously created asynchronous method was causing errors. To address this, separate methods have been developed for both synchronous and asynchronous operations.

### Vault 24.1.14

**15 May 2024**

1. **Parallel Threading for Record Processing**: Parallel threading has been enabled with 5 active threads. Each thread will handle 5 million records whenever records are identified, processing them in parallel.
2. **Restricted Object Selection for ActivityMetrics**: Customers can now only select ActivityMetrics and ActivityMetricsRollup objects when working with 'ActivityMetrics'. To enforce this selection, a query with a WHERE condition must be entered.
3. **Fix for Auto-Selection of Related Records**: The reported issue occurred because all related records were auto-selected, even when child records did not need to be included. Now, if the parent object is selected, related child objects will also be processed. If only lookups are selected, the related child objects will not be processed.
4. **Fix for Circular References**: A reported issue occurred due to circular references. A code fix has been delivered to resolve this problem.
5. **Alert Criteria Issue**: Customers should only receive alerts when the specified criteria are met. However, an issue was causing random alerts to be sent. A code fix has been implemented to ensure alerts are only triggered when criteria are met.
6. **Typographic Error in Column Name**: A typographic error in a column name was identified and corrected.
7. **Field Mapping for Target Environment:** The customer selected an object and set individual mappings for fields to be moved to the target environment.

### Vault v24.1.13&#x20;

**08 May 2024**

1. **Alert Condition Misconfiguration:** The customer set a condition to receive alerts for modifications of 2,000 records, but instead, they are receiving alerts for modifications of just 15 records. This issue is being addressed.
2. **Data Replication Boolean Handling:** During data replication, if a Boolean value is empty in the source, the application attempts to update the destination with a blank value, which can cause errors. A code fix now ensures that if a Boolean value is empty in the source, the corresponding field in the destination will be ignored instead of being updated with a blank.
3. **Service Report Suggestion:** In response to an earlier ticket about the same issue, the customer was advised to run service reports individually for each configuration and to handle the remaining objects in a separate column.
4. **Knowledge Article Attachment Fix:** The knowledge article was not being attached to the corresponding account and case. A code fix has been implemented to ensure that the KB article is properly associated with the relevant account and case.
5. **'Does Not Contain' Filter Issue:** To address an issue with the 'Does Not Contain' filter, double brackets have been added to the code to improve its functionality.
6. **Error Message for Apache Drill Unavailability:** When a report is triggered and the Apache Drill service is down, users receive a "Request Cannot Be Processed" error message. This behavior is now documented and understood.
7. **Session Information Tracking Bug:** A bug was reported by the performance team because session creation information was not being tracked. A fix has been provided, and now session creation is tracked correctly.
8. **Logging Excess Information:** Logs were capturing unnecessary information. A code fix has been applied to prevent unnecessary data from being processed in the logs moving forward.
9. **Apache Drill Unavailability:** This issue is related to the unavailability of Apache Drill, and it has been addressed with the appropriate fixes.
10. **Non-Expiring Download Links:** The download links shared with customers for downloading archival records were not expiring after the designated four-hour period. This issue has been resolved to ensure the links expire as expected.
11. **Persistent Replicate Configuration Details:** Even after deleting Orgs, replicate configuration details still remained in the system. A fix has been implemented so that these details will no longer remain in the system after Orgs are deleted.
12. **Lookup-Related Parent Processing:** When a lookup was selected, related parent objects were not being processed. The fix now ensures that related objects are automatically picked up and processed accordingly.
13. **Replicate Label Display Issue:** The label "Replicate Label" was not being displayed in the configuration details. A code fix has corrected this, and the label now appears correctly in the configuration details pop-up.

### Vault v24.1.12&#x20;

**24 Apr 2024**

1. **Job Processing Time Tracking Fix:** A fix has been implemented to accurately track and display the correct job processing time.
2. **Record Download Improvement:** For records taking more than a minute to download, it was becoming difficult for customers to access them. Going forward, customers will receive an email with a link to download the report. This link will be valid for 4 hours and will expire afterward.
3. **User and Sub-User Tracking in Logs:** A code fix has been provided to track and log both user and sub-user details more effectively.
4. **Null Backup Types Issue:** A bug was raised to identify backup types that were null. All null backup types were identified, and after the fix was implemented, no null backup types remained.
5. **Alert Display Order Fix:** A fix has been provided to ensure that the most recent alerts are displayed at the top of the list.
6. **Session Termination Logging Fix:** A fix was provided to display the name of the user who terminated a session. If an Admin terminates the session, the Admin's name will now be displayed in the log.
7. **File Extension Normalization:** The Vault was using multiple notations for compressed file extensions. A fix has been delivered to standardize these extensions across the application, and moving forward, the file extension will consistently be ".gz".
8. **Alert Delivery Issue:** Alerts were supposed to be sent to the intended user when more than one record was deleted from a set object. However, users were not receiving these alerts. A code fix has been implemented to resolve this issue.
9. **Filter Limit Visibility Issue:** The limit set on the filter was not visible when users tried to edit it. This issue has been resolved with the latest fix.
10. **Child Record Processing Fix:** Child records should not be processed unless explicitly selected. In scenarios where child records were being processed automatically, a fix has been applied to correct this behavior.

### Vault v24.1.11

**03 Apr 2024**

1. **Scheduled vs. Actual Job Date Mismatch:** A fix has been provided to resolve the mismatch between the scheduled dates and the actual dates when jobs are run.
2. **Filter Modification Issue in Queries:** When filters are modified in a query, the changes were not being reflected. A fix has been implemented to ensure that filter modifications are properly applied in the query.
3. **Removal of Mobile Number Field:** The mobile number field has been removed from the user profile sections.

### Vault v 24.1.10

**27 Mar 2024**

1. **nCino Person Accounts Data Issue:** A data issue in nCino person accounts has been identified and fixed.
2. **Disabled Rules and Triggers Functionality Fix:** There was an issue where the disabled rules and triggers functionality was not working as expected. A fix has been implemented to resolve this.
3. **Optimized Destination ID Verification:** A fix has been made to ensure that only the backup IDs in the destination are verified, rather than checking all destination IDs.
4. **MAPDB Implementation Flag:** A new flag has been added to the database to ensure the proper functioning of the MAPDB implementation.
5. **Archival Job Restore Improvement:** Steps have been taken to ensure that deleted entities are not incorrectly shown during the archival job restore process.
6. **Username and Refresh ID Logging:** The username and refresh ID have been added to the logs to ensure that users receive accurate error messages and notifications.
7. **Customer ID Replacement:** The customer ID has been replaced with the bucket name to ensure that the appropriate folder is created.
8. **Thread Writing Conflict Resolution:** Previously, multiple threads were writing into a single file, causing some threads to move into a wait state. A fix has been implemented so that each thread writes to its own file, with all files being merged at the end.
9. **Admin Session Visibility Update:** Admin users were unable to see other users' sessions. New updates have been made to address this issue.

### Vault v 24.1.9

**23 Mar 2024**

1. **nCino Person Accounts Data Fix:** An issue with the data in nCino person accounts has been identified and resolved.
2. **Disable Rules and Triggers Functionality Fix:** The functionality for disabling rules and triggers was not working as expected. A fix has been implemented to correct this issue.
3. **Optimized Backup ID Verification:** A fix has been applied to ensure that only the backup IDs in the destination are verified, instead of checking all destination IDs.
4. **MAPDB Implementation Flag:** A new flag has been added to the database to support the MAPDB implementation.
5. **Archival Job Restore Accuracy:** Steps have been taken to ensure that deleted entities are not incorrectly displayed during the archival job restore process.
6. **Enhanced Error/Notification Logging:** The username and refresh ID have been added to the system to ensure that users receive precise error messages and notifications.
7. **Customer ID Replacement with Bucket Name:** The customer ID has been replaced with the bucket name to ensure that the correct folder is created during the process.

### Vault v 24.1.8

**13 Mar 2024**

1. **Password Modification Tracking:** A provision has been added to the database to track when passwords were last modified.
2. **Blank Value Restoration:** A new feature has been added that allows the restoration of blank values from the source to the destination.
3. **Asset Attribute Backup Support:** A fix has been provided to ensure that the asset attribute is supported only during a full backup.
4. **Post-Org Refresh Data Operations:** A fix has been implemented to ensure that data operations continue seamlessly after an Org refresh is completed.
5. **Job Status Display Fix:** A fix has been rolled out to ensure that jobs display the correct status throughout their execution.
6. **Secure File Download via HTTPS:** A fix has been implemented to ensure that files are downloaded securely through HTTPS.
7. **Connect Config Deletion:** A fix has been provided to ensure that the connect configuration is properly deleted when required.
8. **Delete Flow Corrections:** Necessary corrections have been made to ensure that the delete flow operates correctly and as intended.

### Vault 24.1.7&#x20;

**28 Feb 2024**

AWS KMS support has been added for encryption and decryption to the ingestion service.

### Vault 24.1.6

**21 Feb 2024**

1. **Restore and Replicate Workflow Issues:** Issues related to disabling and enabling workflows through Salesforce Metadata APIs during restore and replicate operations have been addressed.
2. **Duplicate Parent IDs Restored:** A fix has been implemented to prevent the same parent IDs from being restored multiple times.
3. **Missing Records Information in Backup/Archive:** When users select more 'Excluded Fields' for backups, the records information was not being displayed. This issue has been resolved.
4. **Archive Job Failures with Filters:** Archive jobs were failing when filters were applied. A fix has been provided to resolve this issue.
5. **Encrypted Vault Connect Job Logs:** The downloaded file for Vault Connect job logs was displaying in encrypted mode. This issue has been corrected.
6. **Vault Connect UI Data Alignment:** The data alignment on the Vault Connect UI has been corrected as part of the recent fix deployment.

### Vault v24.1.5

**14 Feb 2024**

1. **Managed Package Query Issue:** When querying fields from managed packages, files related to those packages were not being retrieved. We have removed the triggers that were not retrieved from Salesforce, and going forward, only packages with available files will be processed.
2. **Archiving Deleted Records Count:** If a record was archived after being deleted, it was incorrectly counted in the success tally. This issue has been identified and addressed.
3. **Batch Processing Failure Count:** For data processed in batches, the failure count was previously calculated on a batch basis rather than as a consolidated total. This has been reviewed to ensure accurate reporting.
4. **Data Sorting Issue:** Data in Salesforce is stored in ascending order, but retrieving it in descending order was taking longer than expected, causing job delays. This issue has been identified as a cause of jobs getting stuck, and steps are being taken to address it.

### Vault v24.1.4

**07 Feb 2024**

1. **Attachment and Content Version Processing:** Previously, selecting both the attachment and content version led to errors. With the new fix, these records will now be processed without issues.
2. **Org Registration Error Messaging**: Users were encountering vague errors due to insufficient permissions during Org registration. The error message has been updated to provide clearer information.
3. **nCino Feature Visibility Issue**: Users couldn't view nCino features in Vault because property files were being read from the wrong location. This has been corrected.
4. **Email Trigger Update**: A fix has been implemented to allow users to change the recipient of triggered emails.
5. **Log Output Simplification**: Logs have been streamlined to print on a single line instead of across three lines.
6. **Null Pointer Exception Handling:** A fix has been provided to handle null pointer exceptions, ensuring successful records are processed without failure.

### Vault v24.1.3

**31 Jan 2024**

1. **New Algorithm Implementation:** The existing master map generation and its dependencies have been removed. A queue system is added, where selected objects are processed first, followed by their children. Instead of saving the full object result from Salesforce in memory, only the filtered result is saved.
2. **Parallel Processing Restrictions:** New restrictions have been applied to limit ID fetching during parallel processing.
3. **API Count Fix:** The displayed API count now accurately reflects both the files fetched and records processed, providing a consolidated total.
4. **Restore Check for Common Children:** A missing check for notes during the restore of common children has been added in the current implementation.
5. **Parent-Child Mapping Bug Fix:** A bug related to the `isDisableParentChildMapping` flag, which was disrupting the flow, has been addressed by introducing a new flag, `disableParentChildMappingForCommonObjects`.
6. **Restore and Replicate Bug Fix:** A fix has been rolled out to resolve issues causing restore and replicate failures.

### Vault v24.1.2

**24 Jan 2024**

1. **DB Syntactical Error Fix:** A syntactical error in the database has been corrected.
2. **Backup Performance Issue:** The latest backup is taking longer, with FeedItem and EmailMessages processing for more than an hour.
3. **S3 File Download Fix:** A fix has been implemented to allow clients to download files from S3.
4. **OAuth Token Issue:** Restore failures were occurring because the OAuth token was null. This issue has been resolved.
5. **New Flag for Child File Processing:** A new Boolean flag, `personAccountChecked`, has been added to ensure child files are processed

***

## **Vault 24.1 Release Notes** <a href="#whats-new" id="whats-new"></a>

**Anticipated Release Date: 17 April 2024**

These release notes contain important information about **Vault® 24.1**.&#x20;

This release incorporates new features, enhancements, and resolved issues from all previous significant releases. If you're upgrading from an earlier version of Vault, check the release notes for any interim versions or details about additional improvements in this release over your current release.

**What’s new?**

**Exciting New Security Enhancements Await in Vault's Latest Release!**

Security is paramount, and we're thrilled to introduce a range of robust features designed to fortify your data protection strategies. Get ready to bolster your defenses and streamline your workflows with these groundbreaking additions:

**1. Elevated Security: Masking Rules at Org Level**\
Take control of your data security like never before. Now, you can define masking rules at the Salesforce org level, ensuring compliance with organizational policies and enabling seamless reusability across multiple jobs.

**2. Enhanced Security Monitoring: Seamless Viewing of Logs & Reporting on User Activity (SIEM)**\
Empower your enterprise security with enhanced user activity and application event logging. Logs are now provided in CEF format, enabling seamless integration with tools like Splunk for comprehensive analysis and continuous monitoring.

**3. Advanced Encryption: AWS KMS Support for Vault Connect**\
Securely access archived data from AWS KMS encrypted storage using your own key with Vault Connect. Enjoy peace of mind knowing your data is protected while viewing it directly in Salesforce through external objects.

**4. Supporting Vault with Azure Private Link**\
Experience seamless and secure access to BLOB storage from Azure VMs with support for Azure private link in the Vault application, eliminating the need for access keys.

Now, let's dive into additional enhancements aimed at optimizing your data management processes:

**5. Enhanced Vault Capabilities: Reusable Replicate Configurations**\
Say goodbye to repetitive setup tasks! With our enhanced Vault capabilities, you can now create reusable Replicate configurations, saving you valuable time and effort by efficiently rerunning configurations and generating multiple jobs as needed.

**6. Streamlined Workflow: Org-to-Org Cloning of Masking Rules**\
Simplify your data masking process with ease! Introducing the ability to clone masking rules directly from one Salesforce org to another, eliminating the hassle of defining rules from scratch for sandboxes and other Salesforce orgs with identical masking requirements.

**7. Enhanced Clarity: Naming Masking Rules**\
Bring clarity and organization to your masking rules by providing them with descriptive names of your choice. With this new feature, managing and identifying rules has never been easier.

**8. Real-Time Replication: Replicate with Salesforce Live Data**\
Experience the power of near real-time data replication with support for Salesforce Live Data sources. Seamlessly seed your org with actual data without relying solely on backups.

**9. Insightful Analytics: Drawing Metrics on Archived Data**\
Unlock valuable insights from your archived data with built-in reporting capabilities within the Vault application. Now, you can analyze metrics on up to 6 months' worth of archived data effortlessly.

**10. Simplified Data Management: Mapping Restricted Picklists & Record Types**\
Streamline your data management processes with automated mapping of restricted picklist values and record types between source and destination Orgs, eliminating the need for manual intervention.

**11. Preserved Data Integrity: Restore with Blank/Null Values**\
Ensure data integrity throughout the restoration process with the ability to seamlessly restore null or blank values from backups during rollback or replication.

**12. Improved Connectivity: Vault Connect - OData Connector V4.01 Support**\
Stay connected effortlessly with support for the OData connector V4.01, ensuring seamless connectivity and data exchange while bypassing callout limits.

Upgrade now and fortify your data defenses with Vault's latest release!
