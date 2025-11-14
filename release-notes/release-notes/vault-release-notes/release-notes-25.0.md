# Vault Release Notes 25.0

## Vault Release Notes 25.2.2 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 19 October 2025**

#### **Field-Level Comparison Filtering** <a href="#field-level-comparison-filtering" id="field-level-comparison-filtering"></a>

A new enhancement allows users to filter comparison results to include only specific fields during a Compare operation. This improvement helps isolate changes in critical fields while ignoring updates to non-essential system-generated fields, such as _Last\_Login_ timestamps in the User object.\
This enhancement provides faster, more accurate comparisons by reducing false positives and improving focus on relevant data changes.

#### **Azure Key Vault Integration for Secure Credential Handling** <a href="#azure-key-vault-integration-for-secure-credential-handling" id="azure-key-vault-integration-for-secure-credential-handling"></a>

Vault now integrates with Azure Key Vault to securely store and manage sensitive credentials such as Salesforce tokens, database passwords, and encryption keys.\
Secrets are no longer stored in application configs and can now be centrally controlled, rotated, and audited, ensuring stronger security and compliance.

#### **Salesforce API Upgrade for Upcoming Platform Releases** <a href="#salesforce-api-upgrade-for-upcoming-platform-releases" id="salesforce-api-upgrade-for-upcoming-platform-releases"></a>

Vault has been upgraded to use the latest Salesforce API versions (v63 & v64) to stay aligned with upcoming Spring ’25, Summer ’25, and Winter ’26 releases. All core integrations—SOAP, REST, Bulk, and Tooling APIs—are now updated to ensure compatibility, leverage new platform capabilities, and avoid feature disruptions.

#### **Enhanced MFA Security for JWT Authentication** <a href="#enhanced-mfa-security-for-jwt-authentication" id="enhanced-mfa-security-for-jwt-authentication"></a>

A fix has been implemented to enforce proper MFA validation during JWT-based login.\
Previously, users could authenticate without providing the required OTP when MFA was enabled.\
The updated flow now ensures OTP verification is mandatory, restoring full MFA security compliance.

#### **Stateless Session Management Enforcement** <a href="#stateless-session-management-enforcement" id="stateless-session-management-enforcement"></a>

Spring Security is now explicitly configured to use stateless session management, preventing unnecessary HTTP session creation in our JWT-based REST architecture.

#### **Fix for Backup Schedule Update Failure** <a href="#fix-for-backup-schedule-update-failure" id="fix-for-backup-schedule-update-failure"></a>

Resolved a _502 Bad Gateway_ error that occurred when updating scheduled backup configurations for the **GS Prod** org by optimizing the request payload during save operations.

#### **Security Vulnerability Patch Updates** <a href="#security-vulnerability-patch-updates" id="security-vulnerability-patch-updates"></a>

Addressed and upgraded identified vulnerability patches in the ARVault 25.2 release to ensure strengthened security and compliance.

## Vault Release Notes 25.2.1 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 29 October 2025**

#### **Replication Failure**

Fixed an issue that prevented replication jobs from executing successfully. Filters are now correctly copied to the new edit configuration folder during each configuration update.

#### **Live Data Masking Results Download**

Addressed a problem where Live Data Masking results could not be downloaded. Improved file transfer handling ensures large files are now processed and downloaded efficiently.

#### **Backup Failure Alerts**

Resolved an issue where alerts were not generated for failed backups. The system now correctly sends email notifications for scheduled job failures caused by invalid Salesforce credentials.

#### **Backup Job Execution**

Fixed an issue causing intermittent backup job failures. Code enhancements now ensure backup jobs run reliably without interruptions.

***

## Vault Release Notes 25.2.0 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 8 October 2025**

#### **Retry Failed Records**

You can now retry only the records that failed during processing, without reprocessing the entire job. This feature streamlines error handling and saves time by allowing exclusive focus on failed records.

<figure><img src="../../../.gitbook/assets/Retry - Failed Records - 0 (1).png" alt=""><figcaption></figcaption></figure>

#### **License and Usage Tracking**

Vault now provides visibility into actual license usage, storage consumption, and other key metrics compared to Salesforce subscription limits.

<figure><img src="../../../.gitbook/assets/License &#x26; Subscription Tracking - 2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/License &#x26; Subscription Tracking - 3.png" alt=""><figcaption></figcaption></figure>

#### Restoring List View <a href="#restoring-list-view" id="restoring-list-view"></a>

Resolved an issue where list view restoration could fail. The restore process now includes all required dependencies to ensure successful recovery.

#### **Automated Encryption and Security Keys Rotation**

Introduced automation to handle Key-rotation activities, ensuring smoother key transitions and uninterrupted system operations. This enhancement strengthens security, reduces downtime, and minimizes the risk of errors.

#### **Platform Upgrades**

Upgraded underlying platform components to enhance security, improve performance, and ensure compatibility with the latest standards.

***

## Vault Release Notes 25.1.9 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 24 September 2025**

#### **Metadata Backup** <a href="#metadata-backup" id="metadata-backup"></a>

A fix has been implemented to ensure that certain metadata types are processed correctly. Previously, additional prefixes in metadata items during retrieval caused processing failures, which have now been resolved.

#### **Accurate Alerts Information** <a href="#accurate-alerts-information" id="accurate-alerts-information"></a>

Additional information has been added to ensure that email alerts include relevant information that helps users with easier understanding of the source of alert.

***

## Vault Release Notes 25.1.8 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 3 September 2025**

#### **Alerts** <a href="#alerts" id="alerts"></a>

Fixed an issue that occasionally prevented some alerts from appearing. The Alerts section now consistently displays the full list of alerts.

#### **Backup Schedule** <a href="#backup-schedule" id="backup-schedule"></a>

Resolved an issue that impacted backup scheduling. Backup schedules now display accurately and run as expected.

#### **Archive Processing** <a href="#archive-processing" id="archive-processing"></a>

Addressed an issue related to a legacy dependency. Archive processing is now fully reliable and unaffected by this component.

#### **Archive Job Processing – ContentVersion Handling** <a href="#archive-job-processing-contentversion-handling" id="archive-job-processing-contentversion-handling"></a>

Fixed an issue that caused inconsistencies when handling ContentVersion records during deletion. Archive job processing now works correctly and without discrepancies.

#### **Archive Job Processing – Memory Handling** <a href="#archive-job-processing-memory-handling" id="archive-job-processing-memory-handling"></a>

Improved memory management during archive job execution. Archive jobs now run reliably without failures related to memory usage.

***

## Vault Release Notes 25.1.7 <a href="#heading-title-text" id="heading-title-text"></a>

**Release Date: 20 August 2025**

#### **Enhanced Job Timeout Handling**

Improved the job termination logic to ensure jobs end gracefully when timeouts occur, preventing partial processing and maintaining system stability.

#### **Synthetic Backups Stability**

Implemented a fix to prevent timeouts during data processing in synthetic backups, ensuring uninterrupted and reliable execution.

#### **Archive Records Processing Fix**

Resolved an error in archive record processing to guarantee that all records are handled accurately without failures.

#### **Replication Jobs Diagnostics**

Added additional logging to replication jobs, enabling more precise identification of root causes for quicker resolution of issues.

***

## Vault Release Notes 25.1.6

**Release Date: 13 August 2025**

#### **Improved Naming Convention** <a href="#improvised-naming-convention" id="improvised-naming-convention"></a>

The column headers in the **Archive Summary** screen have been updated to improve readability and ensure better understanding of the data presented.

#### **Vault Connect – Backup as a Source** <a href="#vault-connect-backup-as-a-source" id="vault-connect-backup-as-a-source"></a>

1.  A new capability has been added to **Vault Connect**, enabling backups to be selected as a source in the configuration.

    <figure><img src="../../../.gitbook/assets/image (1892).png" alt=""><figcaption></figcaption></figure>
2.  This enhancement empowers customers to strengthen their business continuity strategies by seamlessly leveraging backup data during critical scenarios.

    <figure><img src="../../../.gitbook/assets/image (1893).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (1894).png" alt=""><figcaption></figcaption></figure>

#### **Improved Email Message Handling** <a href="#improved-email-message-handling" id="improved-email-message-handling"></a>

During **email message restoration**, the system now ensures that audit fields are preserved accurately, avoiding unintended updates and maintaining metadata integrity.

#### **Event Logs Enhancements** <a href="#event-logs-enhancements" id="event-logs-enhancements"></a>

Improvements have been made to the **event logging mechanism**, including:

* Consolidation of daily logs
* Enhanced tracking of activities performed by anonymous users for improved auditability and compliance.

#### **Vault Compare Performance Optimization** <a href="#vault-compare-performance-optimization" id="vault-compare-performance-optimization"></a>

The **Vault Compare** operation has been optimized to provide a faster and more seamless user experience during large-scale data comparisons.

#### **Improved Salesforce Org Identification** <a href="#improved-salesforce-org-identification" id="improved-salesforce-org-identification"></a>

Enhancements have been made to the logic that fetches **Salesforce Org details**, ensuring more accurate identification of the Salesforce environment connected to Vault.

***

## Vault Release Notes 25.1.5

**Release Notes: 21 July 2025**

#### Live Data Masking <a href="#live-data-masking" id="live-data-masking"></a>

**New Feature:** Live Data Masking enables Salesforce administrators to protect sensitive information (such as PII) within a live production org without the need to replicate the full dataset. This targeted masking approach allows admins to:

<figure><img src="../../../.gitbook/assets/1 - Live Masking.png" alt=""><figcaption></figcaption></figure>

* Selectively mask specific fields across chosen objects

<figure><img src="../../../.gitbook/assets/2 - Live Masking.png" alt=""><figcaption></figcaption></figure>

* Minimize operational overhead by avoiding bulk data processing

<figure><img src="../../../.gitbook/assets/12 - Live Masking copy.png" alt=""><figcaption></figcaption></figure>

* Ensure only necessary data is altered, maintaining data integrity elsewhere

This enhancement provides a more efficient and secure way to manage data privacy in real-time environments.

#### **Editable Org Configuration**

A new provision allows seamless editing of Salesforce org configurations within Vault. This feature simplifies compliance-driven credential updates by enabling users to re-authenticate Salesforce orgs with updated login credentials directly from the Vault interface.

#### **Selected Object Processing**

The fix ensures that only the explicitly selected child objects are processed during archival/hierarchical backup operations, providing more control and reducing unintended data processing.

#### **Consistent Verbiage Across UI**

Column labels and field names across the application interface have been standardized. This update ensures improved clarity and a more consistent user experience throughout Vault.

#### **Email Message Field Handling**

A fix is implemented to prevent special fields—such as audit fields—from being inadvertently updated during email data operations, preserving the integrity of email-related metadata.

***

## Vault Release Notes 25.1.4

**Release Notes:** **16 July 2025**

*   **Flexible Scheduling Enhancements**

    The scheduling functionality has been enhanced to support a wider range of intervals, providing greater flexibility in configuring backup and automation schedules.
*   **Deleted Records Handling**

    A new option has been introduced to **exclude records in the Recycle Bin** from processing. This helps streamline operations and focus only on active data.
* **GDPR Compliance for Deleted Records**
* A fix has been implemented to ensure that **opted-out deleted records** are no longer visible in Vault, aligning with GDPR compliance and privacy expectations.

***

## Vault Release Notes 25.1.3

**Release Notes: 9 July 2025**

*   **Archival Job Enhancement**

    Previously, the archival job retained additional information even after the configured data retention period had expired. This behavior has now been updated: expired data is fully cleared, ensuring more efficient resource utilization and improved system performance.
*   **Backup Job Reliability Improvement**

    Resolved an issue where backup jobs processing millions of records would experience timeouts, leading to excessive and unproductive retries without successfully retrieving data. The underlying cause has been addressed to ensure more stable and efficient backup operations at scale.
*   **Optimized Metadata Handling in Restore**

    The system's capability to process metadata has been improved by increasing the number of files it can handle concurrently. This ensures smoother and more efficient metadata restore operations.

***

## Vault Release Notes 25.1.2

**Release Date: 02 July 2025**

*   **New Archive Enhancement: Disable Automation Rules**

    Vault now allows users to **disable Salesforce automation rules during the archiving process**. This improvement helps ensure a smoother and more reliable archival experience by preventing interference from active automation rules. As a result, users can expect **fewer errors** and **increased stability** during archival operations.
*   **Selective Record Download for Backups and Archives**

    Users can now **filter and download specific records** from a backup or archive, enabling targeted data access without the need to browse through the entire dataset. The downloaded files are easily compatible with common tools like **Excel**, allowing for **quick and convenient analysis** of only the required information.
*   **Improved Export Stability for Large Datasets in Compare Module**

    A fix has been deployed to enhance the **reliability and performance** of the **export functionality** in the Compare module. Users can now expect a **smoother experience** when exporting large datasets, especially during **bulk compare operations**.
*   **Enhanced Event Logging for Improved Traceability and Integration**

    The event logging system has been upgraded to provide **greater detail and reliability**, enabling **seamless analysis and traceability** of system activities. Logs are now more easily **integrated with tools like Splunk**, streamlining monitoring and audit workflows.
*   **Schema View Usability Fix: Easy Copying of Object Names**

    A fix has been implemented to allow users to **easily copy object names** while viewing the schema. This enhancement improves **usability and efficiency**, making it more convenient to reference or reuse object names during configuration or documentation tasks.

***

## Vault Release Notes 25.1.1

**Release Date: 18 June 2025**

* **Backup Optimization:** Streamlined the object processing logic within the backup module to improve performance and reliability.
* **Dynamic Pagination for Replication Config**: Introduced dynamic pagination during replication config creation, ensuring better scalability and responsiveness.
* **Improved Alert Search**: Optimized the search functionality in the Alerts section for quicker results and enhanced user experience.
* **Accurate Backup Duration Calculation**: Fixed an issue to ensure backup durations are now calculated and displayed correctly across all jobs.
* **Performance Improvement – Replicate Job Optimization**: Resolved a performance bottleneck in the replicate job process by identifying and addressing a delay issue. This enhancement improves execution speed and overall system efficiency.

***

## Vault Release Notes 25.1

**Release Date: 04 June 2025**

* **Vault Compare Enhancements**: Enhanced the user experience with easier navigation to specific fields and more intuitive change review capabilities.&#x20;
* **Enhanced Scheduler Architecture**: Improved tracking and queuing of jobs for more efficient and reliable execution.
* **Additional Validations During Cloning of Replicate Jobs**: Introduced environment validation checks to alert users of any missing metadata before initiating the cloning process of replicate jobs.
* **Synthetic Backup**: Full backups now utilize delta changes from the previous successful full backup, significantly reducing backup duration.
* **Improved Salesforce Session Management**: Improved session management to prevent inactivity during long-running jobs and enhanced API call tracking for greater accuracy.
* **Scheduler Distribution**: Moved the scheduler to an external server to better manage processing load distribution.
* **Performance Enhancements**: Optimized data retrieval logic to improve performance across backup and archival operations.
* **Replicate & Restore Performance**: Optimized the data loading process, significantly improving replicate and restore performance.
* **Restore Logic Update:** Refined logic to more effectively prevent duplicate record creation, ensuring more reliable and consistent restore operations.
* **Salesforce Winter ’25 Upgrade:** Upgraded the Salesforce integration to support the latest Winter ’25 API version.
* **S3 Policy Management**: Improved S3 configuration checks to surface errors early during Vault account setup.
* **Tomcat Upgrade**: Upgraded Tomcat version 10 to 11 for improved security, performance, and standards compliance.
* **Vault Data Masking**: Improved pattern recognition in specific data types to ensure accurate masking while preserving the original format required for valid data representation.
* **Restore UI Label Updates**: Updated restore flow labels:
  * “Restore Now” is renamed to “Create Restore Job”
  * “Trigger Restore” is renamed to “Review and Restore”
  * “Selected Data to Restore” popup is renamed to “Restore Summary”
* **Big Objects Support**: Implemented support for backing up Big Objects.
* **Knowledge Article Replication**: Enhanced owner ID handling to prevent errors caused by owner mismatches, ensuring smooth and accurate replication of knowledge articles.
