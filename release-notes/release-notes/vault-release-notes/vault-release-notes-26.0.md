# Vault Release Notes 26.0

## Vault Release Notes 26.1.0

**Release Date:** March 4, 2026

**Search Across Backups and Archives**

Vault now enables advanced search across Backups and Archives within a selectable six-month time span using an intuitive query builder. Users can define specific criteria, execute the search configuration, and identify data from Archives & Backups.

<figure><img src="../../../.gitbook/assets/1 (4).png" alt=""><figcaption></figcaption></figure>

The feature allows comparison of selected snapshots to pinpoint changes across ORGs based on the defined criteria. Once differences are identified, the **Review and Restore** capability enables targeted data restoration, ensuring precise recovery of required records.

<figure><img src="../../../.gitbook/assets/2 (4).png" alt=""><figcaption></figcaption></figure>

This enhancement streamlines historical data analysis and controlled restoration from backups and archives.

<figure><img src="../../../.gitbook/assets/3 (5).png" alt=""><figcaption></figcaption></figure>

**Org Selection Persistence Improvement**

Resolved an issue where the selected Org was not retained after a browser refresh. The application now consistently preserves and displays the previously selected Org across all modules, ensuring a seamless user experience.

**Salesforce Org Registration – Enhanced to support External Client Apps**

Updated the Salesforce Org registration flow to use OAuth 2.0 aligned with Salesforce’s requirement to support OAuth flow through External Connected Apps. The enhanced guided setup enables secure onboarding of Production and Sandbox environments with real-time validation, encrypted credential storage, automatic token management, actionable error guidance, environment health visibility, and complete audit logging.

**Archive Job Processing Accuracy Improvement**

Resolved an issue where the Archive job for the Case object incorrectly returned a Success status despite unprocessed records. The job status now accurately reflects processing outcomes, ensuring all records are either successfully archived or explicitly marked as failed with proper visibility.

**Backup Job Log Loading Fix (QA)**

Resolved an issue where Backup Jobs failed with a “Failed to load backup log” error, preventing log details from being displayed. Backup execution and log retrieval now function correctly, ensuring proper job completion visibility.













