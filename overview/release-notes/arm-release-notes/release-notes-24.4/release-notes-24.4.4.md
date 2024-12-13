# Release Notes 24.4.4

## ARM Release Notes 24.4.4

**Release Date: 15 December 2024**

The following enhancements and support fixes have been implemented with this release to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Protection Against CSV Injection**

A security vulnerability related to CSV injection has been addressed, where malicious formulas embedded in CSV files could execute commands when opened in spreadsheet applications. User-generated data is now thoroughly sanitized, and special characters are escaped to prevent formula execution. This enhancement ensures that exported CSV files are safe to open, providing stronger protection against potential attacks. Impacted Modules: ORG SYNC HISTORY, USERS, CI JOB HISTORY, REPORTS, CI JOB LIST

#### **Unique Email Enforcement for User Registration**

An issue allowing multiple user accounts to be registered with the same email ID has been resolved, eliminating potential confusion and security risks. The registration process now includes strict validation checks to ensure each email address is linked to only one active account. Email verification has also been implemented to confirm ownership and prevent unauthorized registrations, improving data privacy and system integrity.

#### **TAF Sunset Feature Flag**

A feature flag has been introduced to support the gradual phase-out of TAF functionality in AutoRABIT. This flag allows controlled activation or deactivation of TAF at the customer account level, enabling a seamless transition without disrupting existing workflows. Automated testing and monitoring have been implemented to ensure functionality operates correctly and customer environments remain stable during the transition. Affected customers will be notified with detailed timelines, guidance, and alternative solutions to support their migration. Impacted Modules: TAF, CI Jobs, Reporting

#### **Asynchronous Deployment Processing**

The deployMetadata SOAP service within the Deployment module has been updated to run asynchronously in the background when initiating a Full Deployment. Previously, the service remained in a "pending" state until the deployment job completed. With this enhancement, the deployment process is more efficient, allowing the service to proceed without blocking user actions while the deployment completes in the background. Impacted Modules: Deployments.

#### **Enhanced Audit Log API for ELK Integration**

A new API endpoint has been introduced in the audit logs service to provide structured access to CEF audit logs. The API allows querying audit events based on a specified time range and maximum results, returning a detailed JSON response that includes event metadata, such as timestamps, event types, user actions, and outcomes. This enhancement replaces the previous plain-text log format with a structured and queryable system, enabling easier integration and analysis of audit data. Impacted Modules: API Audit Log Event.

#### **Fixed Redirect for Unsupported Types in Org Sync Report**

An issue in which clicking "HERE" in the Org Sync Report failed to redirect to the Unsupported Types Salesforce screen has been resolved. The href attribute spelling has been corrected, ensuring users are properly redirected to the relevant page for unsupported metadata types. This fix improves navigation and user experience within the Org Sync Report. Impacted Modules: Org Sync.

### Support <a href="#support" id="support"></a>

#### **Improved Stability for Commit and Merge Operations**

An issue causing failures in commit and merge operations due to corrupted global workspaces has been resolved. The global workspace handling mechanism has been enhanced to ensure stability, even when the OPTIMIZED\_WORKSPACE feature flag is disabled. This fix eliminates runtime exceptions during clone operations, improving the reliability of Ez-commit and Ez-merge processes. Impacted Modules: EZ-Commit, Ez-merge, Deployment & CI Jobs, Repo & branch registration. Support Case: #126078

#### **Accurate Reporting for CodeScan SCA with Large Number of Violations**

An issue where code scans with more than 500 violations displayed incorrect results in the UI and incomplete data in downloaded reports has been resolved. The fix ensures that all scanned violations are accurately reflected in the UI and included in the downloaded Excel files, providing a complete and reliable report for large code scans. Impacted Modules: CodeScan SCA execution Reports, CI Jobs , deployments , Commits and Merges. Support Case: #125928

#### **Improved Grouping for Salesforce Scanner Violations**

A mismatch issue between APEX PMD and Salesforce Scanner results has been resolved. Violations in bundle or static resource subfolders are now correctly grouped under their respective metadata types instead of being displayed as separate components. This fix ensures accurate and consistent results, improving the clarity of scanned violations across all file types, including .JS files. Impacted Modules: SCA Execution for both DX and NONDX. Support Case: #126561

#### **ToRevision Included in Scheduled CI Jobs**

An issue where the ToRevision parameter was missing in scheduled CI jobs has been resolved. This issue caused jobs to fail by incorrectly using the baseline revision instead of the incremental revision. The fix ensures that ToRevision is consistently included, enabling accurate and reliable execution of CI jobs. Impacted Modules: CI Jobs. Support Case: #125789

#### **Accurate Metadata Selection in AutoRABIT Build Deployments**

An issue where AutoRABIT Build deployments failed to pick all metadata components when certain components were excluded has been resolved. The deployment process now ensures that all remaining metadata is correctly included, even after exclusions. This fix addresses issues with missing datatable rows, ensuring complete and accurate metadata deployment. Impacted Modules: Deployments. Support Case: #122288

#### **Accurate Revision Handling in Incremental CI Jobs**

An issue where manually triggered incremental CI jobs skipped the previous revision has been resolved. The build process now ensures accurate handling of "From" and "To" revisions, preventing gaps in deployed commits. This enhancement guarantees that all relevant changes are included during incremental builds, maintaining consistency and reliability in deployment workflows. Impacted Modules: CI Jobs. Support Case: #126637

#### **Improved Handling of Managed Package Components in CI Jobs**

An issue causing CI job deployments to fail by including managed package components in destructive changes, despite the "Ignore Installed (Managed) Components" setting being enabled, has been resolved. Logic has been added to exclude installed components from destructive changes in both custom deployments and CI jobs. This enhancement ensures successful deployments without errors related to managed package components. Impacted Modules: CIJobs, Deployments \[DX , NON DX and Org to Org Deployments]. Support Case: #128016

#### **Resolved Deployment Error for DigitalExperienceBundle**

An issue during org-to-org deployments where DigitalExperienceBundle components were not found in the zipped directory, resulting in deployment failure, has been resolved. The logic handling Digital Experience bundles has been corrected to account for scenarios where excluded components exceed 50. This enhancement ensures successful deployments without errors related to missing DigitalExperienceBundle components. Impacted Modules: Custom Deployments with Digital Experience bundles. Support Case: #127472

#### **Accurate Package Version Updates in sfdx-project.json**

An issue where AutoRABIT failed to commit the latest package version to the `sfdx-project.json` file has been resolved. When a new package version is created, it is now correctly updated and committed in the `sfdx-project.json` file, ensuring consistency between the project configuration and the deployed package versions. Impacted Modules: CI Jobs. Support Case: #128347

&#x20;

&#x20;

&#x20;
