# Release Notes 24.4.4

## ARM Release Notes 24.4.4

**Release Date: 15 December 2024**

With this release, we have implemented the following enhancements and support fixes to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **TAF Sunset Feature Flag**

We introduced a feature flag to support the gradual phase-out of TAF functionality in AutoRABIT. This flag allows controlled activation or deactivation of TAF at the customer account level, enabling a seamless transition without disrupting existing workflows. Automated testing and monitoring have been implemented to ensure functionality operates correctly and customer environments remain stable during the transition. Affected customers will be notified with detailed timelines, guidance, and alternative solutions to support their migration. Impacted Modules: TAF, CI Jobs, Reporting

#### **Protection Against CSV Injection**

We strengthened protection against the potential for a security vulnerability related to CSV injection, where malicious formulas embedded in CSV files could execute commands when opened in spreadsheet applications. User-generated data is now thoroughly sanitized, and special characters are omitted to prevent formula execution. This enhancement ensures that exported CSV files are safe to open, enhancing security against attempted cyberattacks. Impacted Modules: Org Sync History, Users, CI Job History, Reports, CI Job List

#### **Unique Email Enforcement for User Registration**

We eliminated the possibility for users to register using multiple email accounts for the same email ID, preventing potential confusion and security risks. The registration process now includes strict validation checks to ensure each email address is linked to only one active account. Email verification has also been implemented to confirm ownership and prevent unauthorized registrations, improving data privacy and system integrity.

#### **Asynchronous Deployment Processing**

We implemented an update to the deployMetadata SOAP service within the Deployment module, which now enables the process to run asynchronously in the background when initiating a Full Deployment. Previously, the service remained in a "pending" state until the deployment job completed. With this enhancement, the deployment process is more efficient, allowing the service to proceed without blocking user actions while the deployment completes in the background. Impacted Module: Deployments

#### ARM API Integration with Supported SIEM Systems

AutoRABIT introduced a new API endpoint in the audit logs service to provide structured access to CEF audit logs. The API allows querying audit events based on a specified time range and maximum results, returning a detailed JSON response that includes event metadata, such as timestamps, event types, user actions, and outcomes. This enhancement replaces the previous plain-text log format with a structured system with query capabilities, enabling easier integration and analysis of audit data. Impacted Module: API Audit Log Event

#### **Fixed Redirect for Unsupported Types in Org Sync Report**

We corrected an issue in which clicking "Here" in the Org Sync Report failed to redirect to the Unsupported Types Salesforce screen. The href attribute spelling has been corrected, ensuring users are properly redirected to the relevant page for unsupported metadata types. This fix improves navigation and user experience within the Org Sync Report. Impacted Module: Org Sync

### Support <a href="#support" id="support"></a>

#### **Improved Stability for Commit and Merge Operations**

We resolved an issue causing failures in commit and merge operations due to corrupted global workspaces. The global workspace handling mechanism has been enhanced to ensure stability, even when the OPTIMIZED\_WORKSPACE feature flag is disabled. This fix eliminates runtime exceptions during clone operations, improving the reliability of EZ-Commit and EZ-Merge processes. Impacted Modules: EZ-Commit, EZ-Merge, Deployment & CI Jobs, Repo & Branch Registration. Support Case: #126078

#### **Accurate Reporting for a CodeScan SCA with a Large Number of Violations**

We corrected an error occurring in which a CodeScan code analysis with more than 500 violations displayed incorrect results in the UI and incomplete data in downloaded reports. The fix ensures that all scanned violations are accurately reflected in the UI and included in the downloaded Excel files, providing a complete and reliable report for large code scans. Impacted Modules: CodeScan SCA Execution Reports, CI Jobs, Deployments, Commits, and Merges. Support Case: #125928

#### **Improved Grouping for Salesforce Scanner Violations**

We resolved a mismatch issue between Apex PMD and Salesforce Scanner results. Violations in bundle or static resource subfolders are now correctly grouped under their respective metadata types instead of being displayed as separate components. This fix ensures accurate and consistent results, improving the clarity of scanned violations across all file types, including .JS files. Impacted Modules: SCA Execution for both DX and Non-DX. Support Case: #126561

#### **ToRevision Included in Scheduled CI Jobs**

We fixed an issue in which the ToRevision parameter was missing in scheduled CI jobs. This issue caused jobs to fail by incorrectly using the baseline revision instead of the incremental revision. The fix ensures that ToRevision is consistently included, enabling accurate and reliable execution of CI jobs. Impacted Module: CI Jobs. Support Case: #125789

#### **Accurate Metadata Selection in AutoRABIT Build Deployments**

We resolved an issue in which AutoRABIT Build deployments failed to pick all metadata components when certain components were excluded. The deployment process now ensures that all remaining metadata is correctly included, even after exclusions. This fix addresses issues with missing data-table rows, ensuring complete and accurate metadata deployment. Impacted Module: Deployments. Support Case: #122288

#### **Accurate Revision Handling in Incremental CI Jobs**

We corrected an issue in which manually triggered incremental CI jobs were skipping the previous revision. The build process now ensures accurate handling of "From" and "To" revisions, preventing gaps in deployed commits. This enhancement guarantees that all relevant changes are included during incremental builds, maintaining consistency and reliability in deployment workflows. Impacted Module: CI Jobs. Support Case: #126637

#### **Improved Handling of Managed Package Components in CI Jobs**

We have resolved an issue causing CI job deployments to fail by including managed package components in destructive changes, despite the "Ignore Installed (Managed) Components" setting being enabled. Logic has been added to exclude installed components from destructive changes in both custom deployments and CI jobs. This enhancement ensures successful deployments without errors related to managed package components. Impacted Modules: CI Jobs, Deployments \[DX, Non-DX, and Org-to-Org Deployments]. Support Case: #128016

#### **Resolved Deployment Error for DigitalExperienceBundle**

We corrected an issue during org-to-org deployments in which DigitalExperienceBundle components were not found in the zipped directory, resulting in deployment failure. The logic handling Digital Experience bundles has been corrected to account for scenarios where excluded components exceed 50. This enhancement ensures successful deployments are completed without errors related to missing DigitalExperienceBundle components. Impacted Module: Custom Deployments with Digital Experience bundles. Support Case: #127472

#### **Accurate Package Version Updates in sfdx-project.json**

We resolved an issue where AutoRABIT failed to commit the latest package version to the `sfdx-project.json` file. When a new package version is created, it is now correctly updated and committed in the `sfdx-project.json` file, ensuring consistency between the project configuration and the deployed package versions. Impacted Module: CI Jobs. Support Case: #128347

## ARM Release Notes 24.4.4.1

**Release Date: 22 December 2024**

Patch to fix bugs in the nCino Query Validation module.&#x20;

&#x20;

&#x20;
