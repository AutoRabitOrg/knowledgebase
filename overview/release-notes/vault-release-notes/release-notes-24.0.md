# Release Notes 24.0

## Vault

### Release Notes 24.1.16

1. After completing the Restore/Replicate actions, the workflow rules are not enabled. According to the expected flow, the workflow rules should be enabled again after completing the Restore/Replicate.
2. A fix was provided as the config details the selected records IDs were not displayed as expected.
3. The field's names of the 'Unique Identifiers' were not displayed. Additional loggers were added, so that, if the fields were enabled, the same would be logged.
4. As the initial file size is 5MB, the file size is increased to 500MB on both the front and back end.
5. Even though the customer has selected 'serial mode', in the back-end logs, it is shown as parallel mode. A fix is provided to make sure the same serial mode is shown in the logs.
6. In addition to tracking the email activity, the email body is being printed in the logs. Based on the fix provided, the email body will not be printed in the logs.
7. The logs are updated to show detailed information on the reason for the log's failure.

### Release Notes 24.1.15

1. As a network error is being thrown, a thread pool is implemented.
2. Going forward, the files downloaded from the Archive module would be zipped for the download.
3. Going forward, the query column will be displayed at the criteria level only, not at the object level.
4. As the previously created asynchronous method is causing the error. Two methods each were created for each individual synchronous and asynchronous methods.

### Release Notes 24.1.14&#x20;

1. Parallel threading is enabled so that, with 5 threads active, each thread will pick up 5 million records whenever the records are identified. All five threads will process the records in parallel.&#x20;
2. Every time the 'ActivityMetrics' objects were to be selected, the customer can only select ActivityMetrics and ActivityMetricsRollup objects, the customer cannot select other objects.
3. The selection to be in effect, a query has to be entered using where condition
4. The reported issue has occurred as all the related records were auto-selected, even though the child's need not be selected for the selection made.
5. With the fix delivered:
   * If the parent object is selected, then the related child objects will also be processed
   * If the lookups are selected, then the related child's will not be processed.
6. Because of the circular references, the reported issue has occurred. A code fix was delivered to correct the issue.
7. As per the customer-set criteria, the customer should only receive the alerts when the criteria are met. A code fix was delivered to fix the issue.
8. As a column name has a typographic error, the same has been corrected
9. The customer has selected an object and set individual mappings for the fields to be moved to the target environment.

### Release Notes 24.1.13

1. A customer set an alert when a modification of 2,000 records occurs. Instead, customers are receiving alerts for a modification of only 15 records, for example. In the Vault application during the data replication, if a boolean value is empty in the source, then Vault tries to update the destination with a blank, which can result in an error. A code fix was provided so that, from now on, if a boolean is empty in the source, then the same field in the destination would be ignored, instead of updating the blanks.
2. In a ticket raised earlier on the same behavior of the issue, a customer suggested running the service reports in individual configurations and the rest of the objects in a separate column. In this instance, the knowledge article was not attached to the account and case. A code fix was provided to ensure the knowledge base article is associated with the respective account and case articles.&#x20;
3. To mitigate this issue with the 'Does not Contain' filter, double brackets were added to the code.
4. When a report is triggered while the apache drill is not available or down, then the following "Request Cannot Be Processed" is displayed to the user.
5. As the creation session information is not being tracked, a BUG is raised by the performance team. A fix was provided to address this issue; creation sessions are now being tracked properly.
6. As a lot of unnecessary information is being tracked in the logs, as per the fix provided, the unnecessary will not be processed going forward.
7. This is also related to "apache drill unavailability.'
8. The download link shared with the customer for downloading the archival records is not expiring even though the allotted time period has elapsed.
9. Replicate configuration details are still remaining even after the Orgs are deleted. As per the fix provided, going forward, the details will not remain in the system about the Orgs deleted.
10. When a lookup is selected, the related parents are not getting processed. With the fix provided, the related objects will be picked up automatically and processed.
11. The label "Replicate Label" was initially not displayed in the configuration details. After the code fix, the label is correctly displayed on the configuration details pop-up.

### Release Notes 24.1.12

1. A fix is provided to properly track and display the correct job processing time.
2. For more than one-minute records, it is becoming hard to download the record. Going forward, an email will be shared with the customer, with the link to download the report. The link will only be valid for 4 hours, and it will expire after 4 hours.
3. A code fix has been provided to track the user and sub user details in the logs.
4. The BUG was raised to identify the backup types that are null, all the backup types with null were identified. After the fix is implemented, no other backup types with null were left.
5. The fix is provided to display the latest alerts triggered on the top of the list.
6. A fix was provided to display the name of the user who has terminated the session.
7. The ADMIN name will be displayed on the log if the ADMIN terminates the session.
8. The Vault is following multiple notations to display the extension of the compressed file. So a fix is delivered to normalize the extensions across the application. Going forward, the file extension would be "gz"
9. Even though alerts were set if more than one record was deleted on an object, users were not receiving the alerts. A code fix was delivered to fix the reported issue.
10. The limit set on the filter is not visible once the user tries to edit the issue. On delivering the fix, the error was resolved.
11. Unless the child's are selected (explicitly), the child's should not be processed. In this scenario as the child's are processed automatically, a fix has been given to fix the issue.

### Release Notes 24.1.11

1. As there was a mismatch on the scheduled dates and the actual job running dates, a fix is provided
2. When the filters are being modified in a query, the change of filters are not reflecting in the query
3. The mobile number field is removed from the profile sections of the user

### Release Notes 24.1.10

1. As multiple threads were writing into one file, some other threads were moving into the wait state. Now, a fix is implemented to ensure each individual threads write into individual files and merging all the files at the end
2. As the admin users were not able to see others sessions new updates were made to the Vault application.

### Release Notes 24.1.9

1. As there was an issue with the data in the nCino person accounts, the issue is fixed
2. As the disable rules and triggers functionality is not working as expected. A fix is provided
3. A fix is done to ensure that instead of checking all the destination IDs only the backup IDs in the destination will be verified
4. A new flag is implemented in the DB so that the MAPDB implementation will work
5. Steps were taken to ensure that the entity deleted is not shown for incorrect reasons in the archival job restore function
6. The user name and refresh id is added to ensure exact error/notification will be shown to the user
7. Replace the customerid with the bucket name to ensure that the proper folder will be created

### Release Notes 24.1.8

1. A provision to track when the password was last modified is added in the DB
2. A provision to restore the blank values from the source to destination is added to Vault
3. A fix is provided to ensure that the asset attribute is only supported for full backup
4. A fix to ensure the data operations continues after the ORG refresh is done is implemented
5. A fix is rolled out to ensure that a proper status is shown on the jobs
6. A fix to ensure that the files are downloaded through https is implemented
7. A fix is provided to make sure that the connect config is gets deleted properly
8. To make sure the delete flow is properly in place the required corrections were made

### Release Notes 24.1.7

AWS KMS support is added for encryption and decryption to the ingestion service

### Release Notes 24.1.6

1. Restore and Replicate Issues - Workflow disable/enable through salesforce metadata APIs.
2. Same parent ids restored multiple times
3. Not showing records info in Backup/Archive if user selected more 'Excluded fields' for backups
4. Archive jobs getting failed when applying the filters
5. Vault connect job log downloaded file showing in encrypted mode.
6. Vault connect The data alignment on the UI is corrected as part of the fix deployed in this

### Release Notes 24.1.5

1. When we query the fields of the managed packages, we are not getting the files related to the managed packages
2. We have removed the triggers that were not retrieved from salesforce
3. So, we are no longer processing those packages, and, going forward we will process the packages that we get the files for"
4. If a record is tried to be archived after deleted, then that is posted in the success count
5. For the data processed in batches, the failure count is calculated in batches instead of consolidated amounts.
6. Data is stored in ascending order in the Salesforce
7. While the data is being retrieved, the data is being sort in descending order
8. Reordering the data into descending order is taking longer time than expected and is causing the job to get stuck.

### Release Notes 24.1.4

1. As of now, when the user selects the attachment and content version, it is failing
2. When the user selects only the attachment and content version the records should be processed without any error, as per the new fix"
3. During the ORG registration, the user is facing error because of lack of permissions:
4. In current scenario, the user is facing an error that doesn’t provide whole information
5. Now, the existing message is corrected to display a proper message to the user"
6. The user is not able to view the nCino features in the Vault application
7. The property files were read from a wrong location, it is corrected by directing to a correct location"
8. As the user is not able to change the user email to whom the email is to be triggered, a fix was provided for the same
9. The logs are modified to print in one single line instead of three different lines
10. As of now when the system encounters the null pointer exception the failure occurs. A fix was provided to handle the null pointer exceptions and process the successful records

### Release Notes 24.1.3

1. New Algorithm is set in place. Removed existing master map generation and all its dependencies and Queue is added. Initially in queue selected object well be added and later their children. Also, full object result from salesforce was being saved in-memory for that job.  Now instead of full object result, filtered result is being saved.
2. New restrictions were setup on id's fetching in parallel processing&#x20;
3. The APIs count displayed were not showing the consolidated count of the files fetched and records processed. The fix implemented will consider both and calculate.
4. During the restore of the common children, the check for notes was missing. The current implementation will set the check in place.
5. Bug was related to isDisableParentChildMapping flag as later on code is common children are there we were changing its value due to which flow was getting disturbed. Introduced a new flag with name disableParentChildMappingForCommonObjects.
6. As the restore and replicate are failing, a bug fix is rolled out to fix the reported issue.

### Release Notes 24.1.2

1. A syntactical error in the database was causing issues; a fix was provided.
2. The latest backup is taking more time mainly because the FeedItem and EmailMessages are taking more than 1 hour to process.&#x20;
3. A fix was provided for the clients to download files from the S3.
4. For Oauth authentication type, as the token became null, files were not being processed, and the restore was failing.
5. A new Boolean flag named "personAccountChecked' was added to ensure child files are processed.

### **Release Notes 24.1** <a href="#whats-new" id="whats-new"></a>

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
