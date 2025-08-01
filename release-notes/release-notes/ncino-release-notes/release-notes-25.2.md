# Release Notes 25.2

### nCino + DL - 25.2.12 Release Notes

**Release Date: 06 July, 2025**

**Job Comment Retention**

An issue where the _Job Label_ would overwrite the existing _Job Comment_ during job edits has been resolved. The comment field will now retain its original value unless explicitly modified by the user.

**RBC Deployment Templates Accuracy**

The logic for handling RBC Deployment Templates has been refined. The system now correctly accounts for omitted templates and accurately calculates the count of selected templates, ensuring consistent and reliable template tracking.

**Rollback Execution Stability**

Enhancements have been made to ensure that rollback operations, even when triggered on the _nth_ iteration, execute seamlessly without disruptions.

**Version Control CI Jobs Ordering**

The display order of CI Jobs under Version Control has been improved. Jobs are now consistently sorted by their _Modified Date_, ensuring that the most recently updated jobs appear at the top of the list.

**Selected Templates Preservation**

In the CI Job configuration, the order of templates within the _Selected Templates_ section is now preserved as per the user’s arrangement. This ensures better clarity and user-defined control over template sequences.

**Triggered Date Population**

A fix has been applied to ensure that the _Triggered Date_ field is correctly populated whenever a job is initiated. This resolves earlier inconsistencies and supports accurate build history tracking.

### nCino + DL - 25.2.11 Release Notes

**Release Date:** 29 June 2025

**CI Job Failure**\
Resolved an issue causing CI job failures due to improperly rendered template objects. The fix ensures templates are now rendered correctly, allowing jobs to execute successfully.

**CI Job Baseline Revision**\
Implemented a fix to ensure the rollback mechanism for CI job baseline revisions functions as expected, maintaining consistency and stability during version changes.

### nCino + DL - 25.2.9 Release Notes <a href="#title-text" id="title-text"></a>

**Release Date:** 15 June 2025

**DL Job Execution Stability**

A fix has been implemented to ensure that DL job executions complete without errors, improving overall job reliability and system stability.

#### Post-Deployment Status Tracking <a href="#post-deployment-status-tracking" id="post-deployment-status-tracking"></a>

Enhanced the tracking mechanism to accurately reflect both **cumulative** and **individual statuses** of deployment jobs, including those targeting **post-deployment ORGs**.

#### Salesforce API Upgrade <a href="#salesforce-api-upgrade" id="salesforce-api-upgrade"></a>

Upgraded the Salesforce integration to use the **latest API version 64**, ensuring continued compatibility and access to the newest platform features.

#### Trigger Build on Commit <a href="#trigger-build-on-commit" id="trigger-build-on-commit"></a>

Resolved an issue where builds were not reliably triggered upon commit. The trigger-build-on-commit functionality now operates **seamlessly and consistently**.

### **nCino + DataLoader 25.2.8 Release Notes**

**Release Date:** 08 June 2025

**Validation Rules Activation**\
Resolved an issue where enabling validation rules was not functioning consistently.

**Rollback Object Configuration**\
Fixed a bug to ensure object configuration data is loaded without discrepancies during rollback.

**Job Group Cloning**\
Addressed issues to ensure job group cloning now completes reliably.

**CI Job Baseline Revision**\
Corrected an error encountered during CI Job baseline revision selection.

### nCino + DataLoader 25.2.7 Release Notes

**Release Date**: 01 June, 2025

**API Refactoring**

Refactored core APIs to align with industry best practices, enhancing performance, scalability, and maintainability across the platform.

**User Permissions**

Standardized user permission handling across both nCino and DataLoader. Users now have access strictly based on their assigned roles and permissions, ensuring better access control and security.

**DL PRO Job Execution Notifications**

Enhanced job execution flow so users will now receive notifications only upon completion of DL PRO jobs, reducing noise and improving clarity in system alerts.

**DL PRO Filters Persistence**

Addressed an issue where filters were reset after being edited. Filters now persist correctly post-edit, ensuring a seamless user experience during job configuration.

**DL PRO Job Execution Stability**

Resolved an IndexOutOfBoundsException occurring during DL PRO job execution. The fix ensures more stable and error-free job runs moving forward.

### nCino + DataLoader 25.2.6 Release Notes

**Release Date**: 25 May, 2025

**Fix on Rollback**

A comprehensive fix has been applied to ensure rollback functions correctly across all scenarios without failure.

**CI Job Code Fix**

Resolved discrepancies in CI job execution. All triggered actions are now accurately reflected, ensuring reliable and traceable job status.

***

### nCino + DataLoader 25.2.5 Release Notes

**Release Date**: 18 May, 2025

**Post-Deploy ORGs Selection**

* Introduced a validation that prevents selecting post-deployment ORGs unless the main ORG is selected, enhancing deployment integrity.
* Fixed an issue where rollbacks for parallelly triggered ORGs did not behave as intended.
* Resolved a bug ensuring post-deployment ORG statuses are now independently tracked and are not tied to the destination ORG’s status.

**CI Job Fixes**

* Addressed an issue where failed CI jobs remained stuck in the queue.
* Applied a fix to prevent CI jobs from staying queued for extended periods, ensuring timely job execution.

***

### nCino + DataLoader 25.2.4 Release Notes

**Release Date**: 10 May, 2025

**Rollback Behavior Improved**

Rollback operations now skip any undeployed changes introduced after deployment edits, ensuring only successfully deployed components are eligible for rollback.

***

### nCino + DataLoader 25.2.3 Release Notes

**Release Date**: 4 May, 2025

**Post-Deployment ORG Rollback**

Users can now select specific ORGs used during post-deployment for targeted rollback actions.

**Individual Template Rollback**

Introduced support for rolling back individual templates, giving users finer control during remediation.

***

### nCino + DataLoader 25.2.2 Release Notes

**Release Date:** 27 April, 2025

**Data Transfer Fix**

Resolved an issue causing data transfer failures. Uploaded files are now reliably processed without interruption.

***

### nCino + DataLoader 25.2.1 Release Notes

**Release Date:** 20 April, 2025

**Template Creation Fix**

Implemented a fix to ensure template creation with multiple buckets is stable and error-free.

**CI Job Execution Fix**

Resolved an issue causing CI jobs to fail. Jobs now execute successfully under all expected conditions.
