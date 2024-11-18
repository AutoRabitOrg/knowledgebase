# Release Notes 24.4.3

## ARM Release Notes 24.4.3

**Release Date: 24 November 2024**

The following enhancements and support fixes have been implemented with this release to improve features and functionality and streamline the user experience.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### **Special Character Support in Commit Comments**

The EZ-Commit workflow now supports special characters in commit comments, including German characters (ä, ö, ü) and punctuation marks (colon \[:], semicolon \[;], slash \[/]). These characters are correctly displayed in commit messages, and the commit process completes without errors when they are used. Impacted Module: EZ-Commit.

#### **Duplicate Detection for Layout Metadata Subnodes**

The system now supports duplicate detection for all subnodes in Layout metadata, ensuring consistent layout configurations and preventing errors during deployment. Duplicate detection functionality has been extended to include the following subnodes:

* **Header**
* **RelatedLists**
* **Sections**
* **QuickActionList**
* **RelatedContent**
* **EmailDefault**
* **MiniLayout**
* **PlatformActionList**

Users will be prompted with clear, actionable messages when duplicates are detected in any of these subnodes, allowing them to resolve issues efficiently. This enhancement builds on existing duplicate detection for `<layoutItems>`, `<layoutColumns>`, and `<layoutSections>`. Impacted Module: Back End.

### Support <a href="#support" id="support"></a>

#### **Digital Experience Metadata Type Improvements**

#### **Accurate Metadata Selection in Profile Deployment**

When deploying a profile via the CI Job build, only the selected profile is now included in the deployment. The issue in which Digital Experience metadata was incorrectly included has been resolved, ensuring that deployments contain only the metadata explicitly chosen by the user. Impacted Modules: Every module that uses Digital Experience Bundle Metadata type. Support Case: #124246

#### **Delete Support for DigitalExperience Metadata**

Users can now delete DigitalExperience metadata in the EZ-Commit module. Additionally, support for managing DigitalExperience metadata has been extended across all modules. Impacted Modules: EZ-Merge, Custom Deployment, CI Jobs, Prevalidation Deployments, and Release Labels. Support Case: #123845

#### **Reliable Re-deployment Using Git Tags**

Re-deployment operations using Git tags now function without errors. The issue has been resolved in which components failed during re-deployment with an error message related to missing objects in the package. Users can successfully re-deploy components for the same tag label as expected. Impacted Modules: Tag deployments in custom deployments. Support Case: #124672

#### **Subscription Extension via Super Admin**

Super Admin users can now successfully extend subscription counts for active accounts. The issue causing an empty notification pop-up when attempting to increase subscriptions has been resolved. Impacted Module: SuperAdmin - Extend Customer tab. Found in QA.

#### **Improved CI Job Status Synchronization with AccelQ**

The integration between ARM and AccelQ has been enhanced to provide accurate and timely updates for CI job statuses and results. Key improvements include:

1. **Dynamic Polling Mechanism**:
   * The system now dynamically adjusts polling intervals for monitoring CI jobs triggered in AccelQ.
   * Once a job's status changes to "Scheduled," a scheduler will poll every 5 minutes to track the job's status.
2. **Targeted Job Monitoring**:
   * The polling mechanism focuses only on the specific AccelQ job related to the triggered CI build, ensuring efficient tracking and updates.
3. **Status Updates**:
   * CI job results in ARM now correctly reflect the actual job status and results from AccelQ upon completion.
4. **Abort Functionality**:
   * Aborting a CI job in ARM now terminates the execution in AccelQ, eliminating the need for manual intervention in AccelQ.

These updates ensure improved synchronization and user experience for ARM-AccelQ integrations. Impacted Module: CI Jobs. Support Case: #124660

#### **Vlocity Deployment Visibility in Deployment History**

The Vlocity deployment process has been updated to address issues with visibility and interaction:

1. **Deployment History Display**:
   * Vlocity deployments now appear correctly in the deployment history, ensuring users can track and review their deployments without issues.
2. **UI Interaction Fix**:
   * Resolved the issue where Vlocity components failed to expand when toggled. Users can now expand and view Vlocity components seamlessly in the deployment history UI.

These improvements enhance the usability and reliability of Vlocity deployments in ARM. Impacted Module: Vlocity Deployments. Support Case: #124417

#### **Accurate Notifications for Scheduled Code Coverage Report Changes**

The notification system for scheduled code coverage reports has been improved to accurately reflect changes in settings.

1. **Test-Level Changes**:
   * When the test level is altered for a scheduled code coverage report (e.g., weekly schedule), the notification now correctly indicates the change instead of displaying "no changes detected."
2. **Other Configuration Changes**:
   * Modifications to parameters such as test classes or email lists also trigger accurate and relevant notifications.

This enhancement eliminates misleading messages, ensuring that users receive correct feedback on configuration updates. Impacted Module: Admin-Code coverage report → Reports. Support Case: #125964

#### **Stability Improvements for Commit and Merge Operations**

The commit and merge processes have been enhanced to prevent failures caused by corrupted global workspaces. The issue occurring when the **OPTIMIZED\_WORKSPACES** feature flag was disabled has been resolved by updating the global workspace checkout mechanism to ensure stability, enabling seamless and error-free operations. Impacted Modules: EZ-Commit, EZ-Merge, Deployment & CI Jobs, Repo & branch registration. Support Case #126078

#### **Automatic Mapping of JIRA Credentials**

The JIRA credentials mapping process has been improved to eliminate the need for manual workarounds. Credentials using application tokens are now automatically populated in the ALM Mapping section of the profile, without requiring modifications to the default credentials in the ALM Management admin section. This enhancement simplifies the mapping process and ensures seamless integration with JIRA. Impacted Modules: VC Repos, Modularization, EZ-Commit, My Account, SF Org Management. Support Case #124949

#### **Improved Handling of Empty Metadata in Release Label Deployment**

The release label deployment process has been enhanced to prevent failures caused by empty metadata. When no deployable changes exist and the package.xml is empty, the system now accurately reflects the absence of metadata in both the UI and back end, ensuring consistency and preventing deployment errors. Impacted Module: Release Labels. Support Case #126720

#### **Notification Emails for New User Creation**

The issue in which notification emails were not being sent to new users upon creation in ARM has been resolved. New users now receive a notification email in their mailbox immediately after being created by an admin, ensuring consistent communication and a smoother onboarding process. Support Case #126197\
\
\




&#x20;
