# Release Notes 25.0

## Vault Release Notes 25.1

**Release Date: 11 June 2025**

* **Vault Compare Enhancements**: Enhanced the user experience with easier navigation to specific fields and more intuitive change review capabilities.&#x20;
* **Enhanced Scheduler Architecture**: Improved tracking and queuing of jobs for more efficient and reliable execution.
* **Additional Validations During Cloning of Replicate Jobs**: Introduced environment validation checks to alert users of any missing metadata before initiating the cloning process of replicate jobs.
* **Synthetic Backup**: Full backups now utilize delta changes from the previous successful full backup, significantly reducing backup duration.
* **Improved Salesforce Session Management**: Improved session management to prevent inactivity during long-running jobs and enhanced API call tracking for greater accuracy.
* **Scheduler Distribution**: Moved the scheduler to an external server to better manage processing load distribution.
* **Performance Enhancements**: Optimized data retrieval logic to improve performance across backup and archival operations.
* **Replicate & Restore Performance**: Optimized the data loading process, significantly improving replicate and restore performance.
* **Restore Logic Update:** Refined logic to more effectively prevent duplicate record creation, ensuring more reliable and consistent restore operations.
* Salesforce Winter ’25 Upgrade: Upgraded the Salesforce integration to support the latest Winter ’25 API version.
* **S3 Policy Management**: Improved S3 configuration checks to surface errors early during Vault account setup.
* **Tomcat Upgrade**: Upgraded Tomcat version 10 to 11 for improved security, performance, and standards compliance.
* **Vault Data Masking**: Improved pattern recognition in specific data types to ensure accurate masking while preserving the original format required for valid data representation.
* **Restore UI Label Updates**: Updated restore flow labels:
  * “Restore Now” is renamed to “Create Restore Job”
  * “Trigger Restore” is renamed to “Review and Restore”
  * “Selected Data to Restore” popup is renamed to “Restore Summary”
* **Big Objects Support**: Implemented support for backing up Big Objects.
* **Knowledge Article Replication**: Enhanced owner ID handling to prevent errors caused by owner mismatches, ensuring smooth and accurate replication of knowledge articles.
