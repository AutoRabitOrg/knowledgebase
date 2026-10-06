# ARM Release Notes

<figure><img src="../../../.gitbook/assets/ARM_Banner_1920x1080.png" alt=""><figcaption></figcaption></figure>

## ARM **Release Notes 26.3.13**

**Release Date: 27 September 2026**

#### Salesforce Standard Authentication Retirement Notifications <a href="#salesforce-standard-authentication-retirement-notifications" id="salesforce-standard-authentication-retirement-notifications"></a>

Added notifications to help customers prepare for Salesforce’s retirement of username- and password-based **Standard authentication**.

Warnings are displayed for Salesforce orgs using Standard authentication in the following areas:

* Salesforce Org registration and configuration
* Environment Provisioning template execution
* CI Job, Deployment, and Environment Provisioning email notifications

The warning is not displayed for orgs using OAuth or OAuth via ECA. Customers can migrate existing Standard-authenticated orgs to **OAuth via ECA**, including orgs whose Standard connection has already stopped working, without affecting their existing mappings, CI Jobs, schedules, or permissions.

#### Salesforce API Version 68.0 Support – Phase 1 <a href="#salesforce-api-version-68.0-support-phase-1" id="salesforce-api-version-68.0-support-phase-1"></a>

Added ARM compatibility with Salesforce API version 68.0 across metadata retrieval, deployment, validation-only deployments, Org Compare, and EZ-Commit workflows. ARM continues to support Salesforce organizations running earlier API versions.

As part of Phase 1, added support for the following Agentforce metadata types:

* AiAgentDefinition
* AiAgentDefinitionVersion
* AiSurface
* AiResponseFormat
* AiTestingDefinition
* AgentPlatformSettings
* AgentforceForDevelopersSettings
* AgentforcePlatformTracingSettings
* BotEmailDefinition

These metadata types are supported across retrieval, commit, change detection, deployment, merge, and filtering workflows. Support for the remaining metadata types introduced with API version 68.0 is planned for the next release.

#### Cascading Selection for Custom Setting Data – Environment Provisioning <a href="#cascading-selection-for-custom-setting-data-environment-provisioning" id="cascading-selection-for-custom-setting-data-environment-provisioning"></a>

Enhanced Custom Setting selection while creating Environment Provisioning migration templates.

Selecting a Custom Setting now automatically selects all eligible fields. After retrieving records, selecting all records automatically selects every eligible field within those records. Selecting an individual record also selects its eligible fields.

Users can still refine the migration by deselecting individual records or fields. Existing behavior for mandatory, system, and non-editable fields remains unchanged. This enhancement applies to List and Hierarchy Custom Settings where applicable.

#### Target Branch Credentials for Pull Request Creation in EZ-Merge <a href="#target-branch-credentials-for-pull-request-creation-in-ez-merge" id="target-branch-credentials-for-pull-request-creation-in-ez-merge"></a>

Fixed an issue where the **Create Pull Request on Merged Changes** option used the credentials of the user who registered the repository instead of the credentials configured for the target branch.

With this fix, ARM uses the target branch credentials when creating the pull request. The help link for this option has also been updated to direct users to the relevant Knowledge Base article.

#### Merge Conflict Handling Improvements <a href="#merge-conflict-handling-improvements" id="merge-conflict-handling-improvements"></a>

Fixed an issue where attempting to download large conflicted Profile files could fail and invalidate the user session.

With this fix, the **Download Files** option is not displayed in Merge Request history when conflicts are present, preventing failed downloads and unexpected logout. An additional issue with the **Revert** action after selecting the source or destination version during conflict resolution has also been resolved.

#### SCA Run Options Fix in CI Jobs – New UI <a href="#sca-run-options-fix-in-ci-jobs-new-ui" id="sca-run-options-fix-in-ci-jobs-new-ui"></a>

Fixed an issue where the selected **Run on** option under **Run SCA Analysis** was not retained when reopening a CI Job in Edit mode.

Also fixed an issue where the applicable SCA run options and **Mark Build As Unstable If It Doesn’t Meet Below Criteria** setting were not displayed when SonarQube was selected.

With this fix, saved SCA options are displayed correctly, and the applicable SonarQube configuration options are available in the New UI.

***

## DataLoader + DataLoader Pro Release Notes **26.3.13**

**Release Date:** **27 September 2026**

#### Accurate Save Messaging for DataLoader Pro Jobs

When **Skip mappings** was selected while saving a DataLoader Pro job, the application could display an incorrect message. Save-message handling was corrected to accurately reflect the selected mapping behavior. The correction applies to new and existing jobs with single or multiple objects in both the existing and new interfaces.

#### Preserved Query Changes in Cloned DataLoader Extract Jobs

Changes made to a SOQL query while cloning a DataLoader Basic Extract Job were not retained, causing the cloned job to use the original query. Query-modification handling was corrected so the edited query is saved with the cloned job. The cloned job now executes using the updated query criteria in both the existing and new interfaces.

***

## ARM **Release Notes 26.3.12.1**

**Release Date: 23 Sep 2026**

#### GitLab OAuth Support for Repository Registration <a href="#gitlab-oauth-support-for-repository-registration" id="gitlab-oauth-support-for-repository-registration"></a>

Added **OAuth authentication support for GitLab repositories**, providing a secure alternative to Personal Access Token (PAT) and SSH authentication.

Users can now authorize ARM through GitLab OAuth and register GitLab repositories using the generated **Client ID and Client Secret**. ARM also supports re-authorization when OAuth access needs to be renewed or updated.

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/version-control/introduction-to-version-control/configure-gitlab-oauth-for-repository-registration-in-arm" %}

## ARM **Release Notes 26.3.12**

**Release Date: 20 Sep 2026**

#### Org Sync Performance and Stability Improvements

Improved **Org Sync performance and application stability** by allowing a maximum of **two Org Sync jobs to run at the same time**.

Any additional manual or scheduled Org Sync requests are automatically queued and will start once an active job is completed. The queued status is displayed in the **ARM UI** for better visibility.

#### Salesforce API 67 Settings Metadata Support

Added ARM support for the following **Settings metadata types introduced in Salesforce API version 67**:

* EmailAuthorizationSettings
* EnterpriseApiSettings
* EvidenceMgmtSettings
* IndustriesInsuranceSettings
* LaborCostOptimCrewMgmtSettings
* QualityManagementSettings
* ServiceIssueManagementSettings
* ServiceItsmChangeManagementSettings
* ThunderbirdVoiceSettings

These metadata types are now supported across applicable ARM workflows, including **retrieval, EZ-Commit change detection, constructive and destructive changes, and deployment**.

#### Installation Key Handling Fix in CI Jobs

Fixed an issue where the Installation Key could be incorrectly processed while saving or updating package installation CI Jobs, resulting in an **Invalid InstallationKey for SubscriberPackageVersion** error.

With this fix, the Installation Key is processed correctly when users enter or update the value, preventing the masked value from interfering with the newly entered key. This fix applies to **CI Job types 9 and 10** in both the **Old and New UIs**.

#### Installed Package Validation Fix in EZ-Commit and EZ-Merge

Fixed an issue where configurations containing only **InstalledPackage** metadata could fail during validation with a **Missing Active RSS Component** error, even though the same configuration could be deployed successfully.

With this fix, InstalledPackage metadata is handled correctly during validation deployments. The fix applies to **EZ-Commit and EZ-Merge** workflows for both **DX and non-DX repositories**.

#### CI Job Queue Processing Fix

Fixed an issue where validation and deployment CI Jobs could remain in the **Pending** state with a message indicating that another deployment to the same destination was in progress, even when no active job was running.

With this fix, ARM correctly identifies and clears inactive queue entries, allowing eligible CI Jobs to proceed automatically without manual intervention.

The fix applies to both **manually triggered and webhook-triggered CI Jobs**.

#### Dotfile Details Logout Fix in Commit History

Fixed an issue where expanding `.gitignore` or other dotfiles under **Commit History → File Changes** could unexpectedly redirect users to the login page.

With this fix, dotfile details are loaded correctly, allowing users to view the file changes without being unexpectedly logged out.

#### Duplicate Repository Name Validation

Fixed an issue where different users could register repositories using the same repository name with different repository URLs.

With this fix, ARM validates repository names across registered repositories. If the repository name is already in use, registration is prevented and an appropriate validation message is displayed.

#### Org Sync Schedule Email Field Fix – New UI

Fixed an issue where the **Email Notification** field was missing when configuring an Org Sync schedule in the **New UI**.

With this fix, the Email Notification field is restored and displayed as **mandatory**, consistent with the Old UI.

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

## ARM **Release Notes 26.3.11**

**Release Date: 13 Sep 2026**

#### Apache Tomcat 11.0.24 Upgrade – Enhancement

ARM now runs on **Apache Tomcat 11.0.24** on Shared, Dedicated, and On-Premises instances. This replaces **11.0.22** and includes Tomcat security and stability updates. Application startup and existing ARM workflows are unchanged.

#### Salesforce Org Delete After Clone Fix

Fixed an issue where a cloned Salesforce org could not be deleted if the org name contained a leading or trailing space. ARM showed **Salesforce org does not exist** even though the org was visible in the UI.

With this fix, org names are trimmed when registering or cloning. Cloned orgs can be deleted in both the Classic UI and the New UI. Re-authentication no longer clears the cloned flag or the original registration date.

#### EZ-Merge Validating Salesforce XML Log Fix

Fixed an issue where **EZ-Merge** showed **No log data available** during the **Validating Salesforce XML** stage when **Skip Flow/Layout/Profile/Perm.Set Access-Setting Duplicity Check** was enabled.

With this fix, that stage writes execution details to the process log in both the Classic UI and the New UI, for DX and Non-DX repositories.

#### EZ-Commit Folder Metadata Duplicate Member Fix

Fixed an issue where removing a folder-based metadata type and adding it again listed the same members twice. This affected folder types such as **ReportFolder**, **DashboardFolder**, **DocumentFolder**, and **EmailFolder**.

With this fix, removing the folder clears its members. Adding the same folder again lists each member only once in both the Classic UI and the New UI, for DX and Non-DX repositories.

#### CI Job Abort Cleanup Fix

Fixed an issue where aborting a CI Job from the UI could leave an unhandled interruption error in the agent log during job cleanup.

With this fix, abort completes for Version Control to Org and Org to Org CI Jobs without that agent error.

#### Scratch Org Create Button Fix – New UI

Fixed an issue in the New UI where **Create Scratch Org** stayed disabled on the last step of the Scratch Org flow when only the main user was present.

With this fix, the button is enabled for a single main user and for orgs with multiple permitted users.

#### SCA Job Name Validation Fix

Fixed an issue where an SCA job name that included **\\** or **;** could be saved, then failed on Run or Delete. A semicolon in the name could also end the user session.

With this fix, new SCA job names reject those characters. Existing jobs can still be run, scheduled, deleted, and viewed in logs and history.

#### Branching Baseline Revision Details Fix – New UI

Fixed an issue in the New UI where **Branching Baseline** Revision Details could fail to render the revision value.

With this fix, Revision Details open from a completed baseline row and show author, date, message, file count, and revision without an error.

***

## ARM **Release Notes 26.3.10**

**Release Date: 6 Sep 2026**

#### API 67 Metadata Types – Enhancement

ARM now supports the following Salesforce API 67 metadata types across commit, constructive changes, and deployment:

* AdminSuccessSettings
* AgentforceAccountManagementSettings
* AgenticCtxtDecorDefinition
* DataMaskPolicy
* DataMaskSettings

These types can be retrieved, compared, committed, and deployed when the org is on API 67.0 or later. Settings types can be updated but cannot be deleted, which matches Salesforce Metadata Coverage. Existing metadata types are unchanged.

#### Run Tests Based on Changes Deployment Log – Enhancement

When **Run Tests Based on Changes** is used, the deployment log previously showed only the final consolidated list of Apex test classes. It was not clear which classes came from the deployed Apex, dependency mapping, or default org test classes.

With this enhancement, the deployment log lists:

* Test classes identified from the Apex classes in the package
* Default Apex test classes configured on the Salesforce org
* The final consolidated list passed to Salesforce

This applies to Version Control to Org and Org to Org deployments in both the Classic UI and the New UI.

#### Data Retention Audit Cleanup Fix

Fixed issues where the daily Data Retention job did not delete eligible **Workspace Audit** and **Mailer Audit** records. The job could report success while old audit rows were left in place.

With this fix, ARM normalizes legacy audit values and completes Workspace Audit and Mailer Audit cleanup according to the configured retention period.

#### Release Label and High-Volume Page Load Fix

Fixed an issue where Release Labels and other high-volume pages could stop responding with a DynamoDB throughput error. Opening a label with a large number of revisions could leave the page stuck.

With this fix, ARM retries and handles temporary DynamoDB capacity limits so Release Labels, CI Jobs, Deployments, EZ-Commit, EZ-Merge, Feature Migration, Data Loader, and Administration pages can load and complete.

#### EZ-Commit Prompt Metadata File Diff Fix

Fixed an issue where EZ-Commit file diff failed for **Prompt** metadata destructive changes with no matching SFDX folder type. After the diff, Prompt could also show **No Modifications** because the file extension was incorrect.

With this fix, Prompt metadata is recognized in DX and Non-DX repositories. File diff and constructive and destructive commits complete, and Prompt files use the **.prompt-meta.xml** extension.

#### EZ-Commit Picklist Record Type Scope Fix

Fixed an issue where committing picklist changes on one object could show extra file changes on Record Types for other objects. Deactivating or activating picklist values on the selected object updated unrelated objects that shared similar picklist labels.

With this fix, EZ-Commit applies picklist and Record Type updates only to the selected object in both DX and Non-DX repositories.

#### Unused API Token Endpoint Removal

Removed an unused API endpoint that returned API token values in the HTTP response body.

Token creation and use in the application and the VS Code plugin are unchanged.

***

## DataLoader + DataLoader Pro Release Notes **26.3.10**

**Release Date:** **6 Sep 2026**

#### Correct Empty Relationship Fields in Data Loader Exports

Resolved an issue where empty User Role or Manager fields could incorrectly display the user’s name in exported CSV files. Data Loader now leaves these relationship fields blank when no value is available. The correction applies to normal and aggregate queries in both the existing and new interfaces.

***

## ARM **Release Notes 26.3.9.1**

**Release Date: 2 Sep 2026**

#### Salesforce Winter ’27 (API 68.0) Deploy Result Parsing Fix

Fixed an issue that caused EZ-Merge, deployments, and CI Jobs to fail after Salesforce upgraded sandboxes to Winter ’27 (API 68.0). When an Apex test level was selected, ARM could not parse the updated Metadata API deploy result and failed with "Cannot invoke "com.sforce.soap.metadata.DeployDetails.getComponentFailures()" because "deployDetails" is null". Validations that ran without a test level completed successfully, and the same deployment could succeed directly in Salesforce. ARM Salesforce libraries are now updated to API 68.0 so deploy results and test coverage responses parse correctly across all Apex test levels.

**Impacted Areas:**

* EZ-Merge
* Deployments
* CI Jobs
* Pre-Validated Commit
* Pre-Validated Merge
* Salesforce Code Coverage Reports

***

## ARM **Release Notes 26.3.9**

**Release Date: 30 Aug 2026**

#### Support Custom Package XML Filenames in Deployment – Enhancement

Custom Deployment previously required the uploaded Salesforce package manifest to be named exactly **package.xml**. Customers maintaining multiple manifests, such as `qa.xml`, `uat.xml`, or `production.xml`, had to rename the file before each deployment.

Custom Deployment now accepts any `.xml` filename that contains a valid Salesforce Package manifest, consistent with EZ-Commit. ARM validates the XML contents rather than the filename, processes accepted files internally as **package.xml**, and rejects non-package metadata files such as Profile or CustomObject XML. Existing deployments that use **package.xml** continue to work without change.

#### Extend Deployment Approval Auto-Reject Timeout to 7 Days – Enhancement

Pending L1 and L2 deployment approvals were automatically rejected after **3 days (72 hours)**, which did not always give approvers enough time to complete review.

Pending L1 and L2 approvals now remain active for **7 days (168 hours)** before auto-rejection. A notification email is sent **24 hours before auto-rejection** to the primary and secondary approvers and the deployment creator. The notification includes the deployment identifier, pending approval level, auto-rejection date and time, and the action required to avoid rejection. Approvals or rejections completed before the warning window do not trigger the reminder. Existing approval statuses, including **Auto Rejected**, are unchanged.

#### Display Actual Static Code Analysis Pass/Fail Result – Enhancement

ARM previously displayed a green tick when Static Code Analysis execution completed, even when the CodeScan or SonarQube Quality Gate had failed. This made it appear as though analysis had passed.

ARM now keeps the existing completion indicator and displays the actual Quality Gate result next to **Static Code Analysis** as **Analysis: PASS** or **Analysis: FAIL**. PASS and FAIL use the corresponding success and failure treatments. The result is shown only after the final outcome is received from CodeScan or SonarQube and applies to **Commit**, **Merge**, and **Quick Merge** in both the Classic UI and the New UI. This display applies to **CodeScan** and **SonarQube** only.

#### ECA Concurrent Session Lockout Fix

Fixed an issue where an ECA-enabled Salesforce org could be locked out with an **INVALID\_SESSION\_ID** error when a CI Job using **Deploy from Salesforce Org** and an **EZ-Commit** ran at the same time against the same source org. After the conflict, **Re-Authorize** did not reliably restore the org.

With this fix, ARM coordinates refresh-token rotation for the same org so concurrent CI Job and EZ-Commit operations can complete without invalidating each other’s session. Re-authorization restores org connectivity when needed, and single-operation workflows are unchanged.

#### OAuth and OAuth-with-ECA Registration and Re-Authorization Fix

Fixed issues where Salesforce org registration and re-authorization failed in several OAuth flows. OAuth to **OAuth-with-ECA** re-authorization did not complete, new OAuth registrations and re-authorization below API version 64 failed, and OAuth to OAuth-with-ECA re-authorization failed when **PKCE** was disabled.

With this fix, PKCE is supported for the standard OAuth flow as well as OAuth via ECA. Registration, re-authorization, token refresh, and test connection succeed with PKCE enabled or disabled, including when converting an existing org from OAuth to **OAuth via ECA**.

#### EZ-Merge Git Push Status Fix

Fixed an issue where **EZ-Merge** could be marked **Successful** when the remote Git push was rejected, for example by branch protection rules. The locally created commit revision was still shown as successful, and users had to inspect logs to discover that the push had failed.

With this fix, ARM validates the remote Git push result before marking the merge complete. If the push is rejected, the merge is marked **Failed**, the local commit revision is not shown as a successful revision, and the Git rejection error is displayed to the user. Merges that push successfully continue to be marked **Successful**.

#### Revision Number Display Fix in Commits, Merges, and CI Jobs

Fixed an issue where the full Git commit hash was displayed after merge conflict resolution, in merge notifications, in the EZ-Commit label section, and in CI Jobs.

With this fix, revision numbers are displayed as a **short SHA** across **Commit**, **Merge**, and **CI Job** views in both the Classic UI and the New UI.

#### Profile Compare Deploy View Fix

Fixed an issue in **Profile Compare** where **Deploy** and **Update and Deploy** applied permission changes to the target org, but the comparison grid did not refresh to show the post-deployment state. The grid could display stale or inverted source and target values.

With this fix, comparison data is refreshed after Deploy and Update and Deploy so the grid reflects the actual org state. Permissions continue to be applied only to the target org.

#### Vlocity Release Label Merge Board Type Fix

Fixed an issue where the **Board Type** field was not auto-populated during **Release Label Merge** for Vlocity release labels. The field remained blank and required manual input, unlike non-Vlocity release label merges.

With this fix, Board Type is automatically populated from the selected Vlocity release label and repository configuration for both release label and commit label merge workflows.

#### CI Job DynamoDB Throughput Error Fix

Fixed an issue where CI Jobs could fail during build processing with a DynamoDB throttling error indicating that throughput exceeded the current table or index capacity.

With this fix, CI Job processing handles this condition correctly so scheduled, webhook, pull request, and parallel CI Job executions can complete without this failure.

#### Quick Deploy After Validate Only Fix

Fixed an issue where **Quick Deploy** was unavailable after a successful **Validate Only** deployment to a Production org when the test level was set to **Salesforce Defaults**. In the Classic UI, the label name was disabled. In the New UI, a valid Asynchronous ID was not available for selection.

With this fix, Quick Deploy is available after a successful Validate Only deployment to Production when using Salesforce Defaults. The label name is populated and ARM-generated Asynchronous IDs are available. Quick Deploy remains unavailable after Validate Only on non-production orgs when Salesforce Defaults are used, which is expected.

#### Branching Baseline Commit Log Fix

Fixed an issue where initiating a **Branch Baseline** could fail with a UI exception while loading commit logs, including the message **Error parsing SCM commit log file**. Concurrent access to the commit log file could corrupt the file and block the baseline.

With this fix, ARM locks the commit log file during read and write operations and releases the lock when the operation completes. Branch Baseline can retrieve commit logs and proceed even when push protection is enabled or configuration files such as `.gitignore` and `package.xml` are missing from the branch.

***

## DataLoader + DataLoader Pro Release Notes **26.3.9**

**Release Date:** **30 Aug 2026**

#### Data Loader Pro Job Configuration Settings Not Retained <a href="#id-5.-data-loader-pro-job-configuration-settings-not-retained" id="id-5.-data-loader-pro-job-configuration-settings-not-retained"></a>

Resolved an issue where selected Data Loader Pro job settings were not retained during execution.

Options such as disabling workflows and validation rules and processing null values are now saved and applied correctly.

***

## ARM **Release Notes 26.3.8**

**Release Date: 23 Aug 2026**

#### Create Pull Request for Merged Changes in ez-Merge – New Enhancement (New UI) <a href="#create-pull-request-for-merged-changes-in-ez-merge-new-enhancement-new-ui" id="create-pull-request-for-merged-changes-in-ez-merge-new-enhancement-new-ui"></a>

Introduced the **Create Pull Request On Merged Changes** option in ez-Merge. When enabled, ARM applies the merged changes to a temporary branch, validates them, and creates a pull request targeting the selected destination branch instead of committing the changes directly.

The option is available only when **Pre-validation Merge** is configured and supports all pull-request-enabled repositories. Pull request details and the URL are available in the new **Pull Request Creation** process log.

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/version-control/ez-merge/create-pull-request-on-merged-changes-in-ez-merge" %}

#### Duplicate Picklist Member Selection Fix in EZ-Commit – New UI <a href="#duplicate-picklist-member-selection-fix-in-ez-commit-new-ui" id="duplicate-picklist-member-selection-fix-in-ez-commit-new-ui"></a>

Fixed an issue where a Custom Object already added as a Picklist member remained available in the dropdown and could be selected again without any feedback.

With this fix, previously added Custom Objects are no longer displayed in the dropdown, preventing duplicate selection and improving the metadata selection experience.

#### Branching Baseline Gitignore Handling Fix <a href="#branching-baseline-gitignore-handling-fix" id="branching-baseline-gitignore-handling-fix"></a>

Fixed an issue where the Branching Baseline process replaced the repository’s existing `.gitignore` file with a default version. This caused ignored files, such as `manifest/package.xml`, to be included and could trigger repository push-protection violations.

With this fix, ARM retains and applies the existing `.gitignore` file during the Branching Baseline process. The default `.gitignore` file is used only when one is not already available in the repository.

#### EZ-Commit File Diff Failure Fix – Old UI <a href="#ez-commit-file-diff-failure-fix-old-ui" id="ez-commit-file-diff-failure-fix-old-ui"></a>

Fixed an issue where Picklist metadata was incorrectly treated as a Custom Field when reusing a previously validated EZ-Commit label. This caused false deleted components and resulted in a file-diff failure.

With this fix, Picklist values are correctly processed as Picklist metadata, preventing false destructive entries and file-diff failures.

#### SonarQube SCA Execution with S3 Fix <a href="#sonarqube-sca-execution-with-s3-fix" id="sonarqube-sca-execution-with-s3-fix"></a>

Fixed an issue where SonarQube SCA executions failed when using S3 and incorrectly displayed the **Updating CodeScan Project** message.

With this fix, the S3-specific analysis path is restricted to CodeScan, ensuring SonarQube SCA executions are processed correctly.

#### Ignore Missing Visibility Setting Display Fix <a href="#ignore-missing-visibility-setting-display-fix" id="ignore-missing-visibility-setting-display-fix"></a>

Fixed an issue where the **Ignore Missing Visibility** setting was not displayed in the commit history details.

With this fix, the setting and its configured value are now visible under **More** on the Commit History Details page.

#### Standard Field Changes Detection Fix in EZ-Commit – New UI <a href="#standard-field-changes-detection-fix-in-ez-commit-new-ui" id="standard-field-changes-detection-fix-in-ez-commit-new-ui"></a>

Fixed an issue where changes to standard field permissions were not detected or displayed during comparison in EZ-Commit.

With this fix, standard field permission changes are correctly retrieved and displayed in the New UI.

#### Skipped Components Exclusion Fix <a href="#skipped-components-exclusion-fix" id="skipped-components-exclusion-fix"></a>

Fixed an issue where components configured as skipped were still included during repository-to-org deployments, even when **Do Not Include Skip Members During Deployment** was enabled.

With this fix, skipped components are correctly excluded from CI Job and Manual Deployment workflows for both DX and non-DX repositories.

#### Password Reset Screen Responsiveness Fix <a href="#password-reset-screen-responsiveness-fix" id="password-reset-screen-responsiveness-fix"></a>

Fixed an issue where the password reset screen became unresponsive when a Pendo survey appeared during login, preventing users from entering a new password.

With this fix, users can complete the password reset process without interference from Pendo notifications.

#### Support Contact Information on Password Reset – Enhancement <a href="#support-contact-information-on-password-reset-enhancement" id="support-contact-information-on-password-reset-enhancement"></a>

Added the AutoRABIT Support email address to the password reset message. Users who do not receive the reset email or continue experiencing login issues can now contact [**support@autorabit.com**](mailto:support@autorabit.com) directly for assistance.

#### CheckmarxOne Analysis Report Category Display Fix – New UI <a href="#checkmarxone-analysis-report-category-display-fix-new-ui" id="checkmarxone-analysis-report-category-display-fix-new-ui"></a>

Fixed an issue where the **Critical** category was missing from CheckmarxOne SCA analysis reports and appeared as an unlabeled column.

With this fix, all severity categories—Critical, High, Medium, Low, and Information—are displayed correctly.

#### AI Bundle Metadata Processing Fix <a href="#ai-bundle-metadata-processing-fix" id="ai-bundle-metadata-processing-fix"></a>

Fixed issues where **AiAuthoringBundle** and **GenAiPlannerBundle** metadata could be incorrectly included or processed during commit, CI Job, and deployment workflows.

With this fix, bundle metadata is handled correctly based on user selection, exclusion lists, and skipped members for both DX and non-DX repositories, preventing unintended deployment failures.

***

## DataLoader + DataLoader Pro Release Notes **26.3.8**

**Release Date:** **23 Aug 2026**

#### Data Loader Pro Org Re-Registration Consistency

Corrected inconsistent behavior between manual and scheduled executions after a Salesforce source org was re-registered with different name casing. The system now correctly identifies the source and destination orgs regardless of case sensitivity in the registration name.

***

## ARM **Release Notes 26.3.7**

**Release Date: 16 Aug 2026**

#### Vlocity CI Job Deployment Report Fix - New UI <a href="#vlocity-ci-job-deployment-report-fix-new-ui" id="vlocity-ci-job-deployment-report-fix-new-ui"></a>

Fixed an issue in the New UI where **Deployment Reports** for Vlocity CI Jobs displayed a **"Reports not available"**&#x6D;essage even when the deployment completed successfully. The CI Job deployment flow has been updated to capture and store Vlocity deployment results correctly, allowing users to view component-level deployment details directly from the CI Job History.

#### Vlocity Deployment Validation Flow Fix <a href="#vlocity-deployment-validation-flow-fix" id="vlocity-deployment-validation-flow-fix"></a>

Fixed an issue where **Vlocity deployments and Quick Merge workflows** could fail or remain stuck due to unsupported validation and Static Code Analysis (SCA) options being processed for Vlocity components.

The deployment configuration flow has been updated to correctly handle Vlocity deployments by hiding SCA, deployment validation, and their related configuration fields when they are not applicable. This ensures Vlocity deployment and Quick Merge workflows can be configured and processed without unintended validation failures.

#### Auto Populate Apex Test Classes Progress Status Fix <a href="#auto-populate-apex-test-classes-progress-status-fix" id="auto-populate-apex-test-classes-progress-status-fix"></a>

Fixed an issue where the **Auto Populate** progress status for default Apex test classes was incorrectly carried over when switching between Salesforce orgs. The loading and progress state is now handled independently for each selected org, allowing users to initiate Auto Populate for different Salesforce orgs without requiring a page refresh or waiting for another org's process to complete.

#### EZ-Commit Version Control Credential Handling Fix <a href="#ez-commit-version-control-credential-handling-fix" id="ez-commit-version-control-credential-handling-fix"></a>

Fixed an issue where **EZ-Commit** used the repository credentials configured under Admin settings instead of the logged-in user's profile-mapped Version Control credentials when **Salesforce Org Author** was set to **All** and **Skip Mappings** was disabled.

EZ-Commit now consistently uses the credentials mapped to the user performing the commit, ensuring repository permissions and branch protection rules are correctly enforced for both **Direct** and **Pre-Validated** commits.

#### Rollback Button State Fix - New UI <a href="#rollback-button-state-fix-new-ui" id="rollback-button-state-fix-new-ui"></a>

Fixed an issue in the New UI where the **Rollback** button remained enabled even after a rollback completed successfully. The Deployment History screen now disables the Rollback button while rollback is in progress and hides it once the rollback has completed successfully.

#### Weekly Reports Data Consistency Fix <a href="#weekly-reports-data-consistency-fix" id="weekly-reports-data-consistency-fix"></a>

Fixed an issue where data generated from the **Weekly Reports** module did not match the corresponding build information displayed in **CI Job History**. The filtering logic in both the UI and back end has been corrected to ensure reports display accurate and consistent CI Job build data across both the **Classic** and **New UI**.

#### CI Job Apex PMD SCA Criteria Status Fix <a href="#ci-job-apex-pmd-sca-criteria-status-fix" id="ci-job-apex-pmd-sca-criteria-status-fix"></a>

Fixed an issue where **CI Jobs** configured with **Apex PMD SCA criteria** could be incorrectly marked as unstable during execution. The SCA criteria processing and logging have been corrected to ensure the build status accurately reflects the Apex PMD analysis results.

#### EZ-Commit ALM Mapping Fix - Classic UI <a href="#ez-commit-alm-mapping-fix-classic-ui" id="ez-commit-alm-mapping-fix-classic-ui"></a>

Fixed an issue in the Classic UI where **ALM Work Item** details were not correctly populated and configured during EZ-Commit when using a Scratch Org with **Skip Mappings** disabled. The EZ-Commit selection flow now ensures ALM work items are fully loaded before resolving their statuses, allowing the mapped work item, current status, and available status options to be populated and function correctly. This provides consistent ALM mapping behavior across the Classic and New UI.

***

## DataLoader + DataLoader Pro Release Notes **26.3.7**

**Release Date:** **16 Aug 2026**

#### **Summary Side Panel Alignment Fix**

The Summary side pop-up in Dataloader Pro and DL Config now displays content with proper left alignment. This reduces unused blank space, improves readability, and helps prevent long values from appearing clipped at the right edge.

***

## ARM **Release Notes 26.3.6**

**Release Date: 9 Aug 2026**

#### Azure DevOps SSO Enhancement New UI <a href="#azure-devops-sso-enhancement" id="azure-devops-sso-enhancement"></a>

Enhanced Azure DevOps Single Sign-On (SSO) to support authentication using **Microsoft Entra Tenant ID** and **Object ID**, providing greater flexibility in user identity mapping. Administrators can now configure these identifiers for users, enabling successful SSO authentication even when the Identity Provider (IDP) username differs from the ARM username. If the Tenant ID and Object ID are not configured or do not match, ARM automatically falls back to the existing username-based validation, ensuring backward compatibility with current SSO configurations.

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/integration-and-plugins/sso/sso-with-microsoft-azure-ad" %}

#### Org-to-Org CI Job Incremental Build Fix <a href="#org-to-org-ci-job-incremental-build-fix" id="org-to-org-ci-job-incremental-build-fix"></a>

Fixed an issue in **Org-to-Org CI Jobs** where destructive change tracking did not behave correctly for unpackaged deployments. The destructive change processing has been improved to correctly maintain the destructive baseline, ensuring deleted components are tracked consistently across deployment cycles while preserving the expected behavior for incremental builds.

#### External Credential File Diff Fix <a href="#external-credential-file-diff-fix" id="external-credential-file-diff-fix"></a>

Fixed an issue where deleting **External Credential** metadata in DX repositories caused file diff generation to fail during EZ-Commit with a **"No enum constant"** error. ARM now correctly recognizes External Credential metadata during deletion workflows, enabling successful file diff generation for both direct and pre-validation commit operations.

#### Scratch Org Azure Boards Mapping Fix - New UI <a href="#scratch-org-azure-boards-mapping-fix-new-ui" id="scratch-org-azure-boards-mapping-fix-new-ui"></a>

Fixed an issue in the New UI where the **Team Name** field was not displayed during Scratch Org creation when configuring **Azure Boards** ALM mappings. The ALM mapping workflow has been updated to correctly display the required Team Name field, allowing users to complete Scratch Org creation without additional manual configuration.

#### Deployment Destructive Changes Pagination Fix <a href="#deployment-destructive-changes-pagination-fix" id="deployment-destructive-changes-pagination-fix"></a>

Fixed an issue where the **Destructive Changes** selection list did not display all available components during deployments, making it difficult to select destructive changes. The pagination logic has been improved to dynamically track the total number of filtered records, ensuring all matching components are displayed correctly during browsing and search.

#### Profile Rollback Permission Restoration Fix <a href="#profile-rollback-permission-restoration-fix" id="profile-rollback-permission-restoration-fix"></a>

Enhanced the rollback process for **Profile** metadata to correctly restore **Object** and **Field** permissions to their original state. ARM now preserves the pre-deployment permission state, including cases where no permissions previously existed, ensuring newly added permissions are properly removed during rollback for both **Deployments** and **CI Jobs**.

#### Search & Substitute XPath Handling Fix <a href="#search-and-substitute-xpath-handling-fix" id="search-and-substitute-xpath-handling-fix"></a>

Fixed an issue where **Search & Substitute** rules failed to replace values containing special characters, such as single quotes, in Custom Metadata fields. The XPath parsing logic has been corrected to properly handle these values, ensuring substitutions are applied successfully during deployment instead of being silently skipped.

#### Custom Field Translation Deletion Fix <a href="#custom-field-translation-deletion-fix" id="custom-field-translation-deletion-fix"></a>

Fixed an issue where deleting a **Custom Field** through EZ-Commit did not remove its associated **Field Translation** metadata from the repository. ARM now automatically deletes the related field translations when a destructive commit is performed for Custom Fields, ensuring translation metadata remains synchronized with the deleted field in both DX and non-DX repositories.

#### Ignore Missing Visibility Settings Fix <a href="#ignore-missing-visibility-settings-fix" id="ignore-missing-visibility-settings-fix"></a>

Fixed an issue in **CI Jobs** where enabling **Ignore Missing Visibility Settings, If Package Contains Profiles or Permission Sets** incorrectly removed valid Permission Set tab visibility entries during deployment. The backend logic has been updated to remove only references to metadata that are unavailable in the target org, preserving existing valid visibility settings and preventing unintended changes to Permission Sets.

#### EZ-Commit Object Selection Fix - New UI <a href="#ez-commit-object-selection-fix-new-ui" id="ez-commit-object-selection-fix-new-ui"></a>

Fixed an issue in the New UI where duplicate object names could appear in the **EZ-Commit** object selection picklist, preventing users from accessing the required fields. The object filtering logic has been updated to correctly handle object prefixes, ensuring object names are displayed uniquely and the appropriate fields are available for selection.

#### Deployment Timeout Status Fix <a href="#deployment-timeout-status-fix" id="deployment-timeout-status-fix"></a>

Fixed an issue where long-running **Quick Deploy** operations with a large number of components could be incorrectly marked as **Timed Out** in ARM, even though the deployment completed successfully in Salesforce. The deployment status handling has been improved to prevent active deployments from being incorrectly classified as timed out while background processing is still in progress, ensuring the deployment status accurately reflects the final outcome.

#### Automatic Cleanup of Deactivated Picklist Value References <a href="#automatic-cleanup-of-deactivated-picklist-value-references" id="automatic-cleanup-of-deactivated-picklist-value-references"></a>

Introduced an enhancement that automatically removes references to **deactivated picklist values** from affected **Record Types** during metadata processing. When a picklist value is deactivated, ARM identifies all Record Types belonging to the same object, removes only the invalid picklist value references, and automatically includes the updated Record Types in the generated deployment or commit package. This ensures metadata consistency across branches and deployments while preserving all other Record Type configurations and unrelated metadata.

{% embed url="https://knowledgebase.autorabit.com/fundamentals/faq/automatic-cleanup-of-deactivated-picklist-values" %}

***

## DataLoader + DataLoader Pro Release Notes **26.3.6**

**Release Date:** **09 Aug 2026**

#### External ID Mapping Persistence

Addressed a DataLoader issue reported through Support Case, where saved custom **External ID** field mappings reverted after a browser refresh. The mapping now persists as expected, helping users retain intended source-to-destination field relationships across sessions.

***

## ARM **Release Notes 26.3.5**

**Release Date: 2 Aug 2026**

#### Profile Rollback Restoration Improvement <a href="#profile-rollback-restoration-improvement" id="profile-rollback-restoration-improvement"></a>

Enhanced the rollback process for **Profile** metadata to ensure profile permissions are restored correctly after a rollback operation. ARM now creates a more complete Profile backup by including the required dependent metadata, enabling Salesforce to accurately restore Profile permissions during rollback for both **CI Jobs** and **Deployments**.

#### GitLab Cloud Pull Request Support <a href="#gitlab-cloud-pull-request-support" id="gitlab-cloud-pull-request-support"></a>

Added support for creating **GitLab Cloud Pull Requests** directly from ARM, allowing users to create Pull Requests without leaving the application. ARM validates the selected repository and branches before creating the Pull Request and displays the Pull Request number and URL upon successful creation, providing a streamlined and integrated GitLab Cloud workflow. Refer to the documentation on External Pull Requests [here](https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/version-control/external-pull-request).&#x20;

#### Dependent CI Job Execution Fix <a href="#dependent-ci-job-execution-fix" id="dependent-ci-job-execution-fix"></a>

Fixed an issue where a **Child CI Job** triggered automatically after a successful **Parent CI Job** deployment could fail during the build phase without displaying an error. The post-deployment execution flow has been improved to handle deployment status correctly, ensuring dependent Child CI Jobs execute reliably when triggered from Parent CI Jobs.

#### Salesforce Org Registration API <a href="#salesforce-org-registration-api" id="salesforce-org-registration-api"></a>

Added a new API that enables Salesforce organizations to be registered in ARM using standard **Username**, **Password**, and **Security Token** authentication. The API supports secure, token-based access, allowing Salesforce Org registration to be automated and integrated with external provisioning and onboarding workflows without relying on the ARM user interface. Refer to the full list of API references [here](https://knowledgebase.autorabit.com/product-guides/arm-1/introduction-to-arm-developer-apis/api-references).&#x20;

#### CI Job Clone API <a href="#ci-job-clone-api" id="ci-job-clone-api"></a>

Added a new API that enables users to clone an existing **CI Job** in ARM, allowing CI Job configurations to be duplicated programmatically without using the ARM user interface. This simplifies the automation of CI/CD setup and integration with external systems. Refer to the full list of API references [here](https://knowledgebase.autorabit.com/product-guides/arm-1/introduction-to-arm-developer-apis/api-references).

#### CI Job Baseline Revision Pagination Fix <a href="#ci-job-baseline-revision-pagination-fix" id="ci-job-baseline-revision-pagination-fix"></a>

Fixed an issue where the **Baseline Revision** selection dialog retained the previously selected page after clicking **Get Latest Head** or **Get All Revisions**. The revision list now refreshes from the first page, ensuring users can immediately view the latest revisions and browse the complete revision list as expected.

***

## DataLoader + DataLoader Pro Release Notes **26.3.5**

**Release Date:** **02 Aug 2026**

#### DataLoader Pro Job Visibility for Subusers (DevHub Orgs) <a href="#dataloader-pro-job-visibility-for-subusers-devhub-orgs" id="dataloader-pro-job-visibility-for-subusers-devhub-orgs"></a>

Fixed an issue where Dataloader Pro jobs created by a subuser were not visible to the same subuser who created them. Jobs now correctly appear for both the creator (subuser) and admin users, ensuring consistent ownership-based visibility.

***

## ARM **Release Notes 26.3.4**

**Release Date: 26 July 2026**

#### Provar CI Job Execution Fix (New UI) <a href="#provar-ci-job-execution-fix-new-ui" id="provar-ci-job-execution-fix-new-ui"></a>

Fixed an issue where CI Jobs configured by selecting the **Provar Plugin** before entering Version Control details failed to execute due to missing credential and test file information. The configuration flow has been corrected so Provar jobs execute successfully regardless of the order in which the Provar and Version Control options are selected.

#### GitHub Enterprise Pull Request Webhook Fix <a href="#github-enterprise-pull-request-webhook-fix" id="github-enterprise-pull-request-webhook-fix"></a>

Fixed an issue where CI Jobs configured to trigger on Pull Request events in GitHub Enterprise were not starting automatically, even though the webhook payload was successfully received. The webhook processing logic has been updated to correctly identify the configured repository and process Pull Request events, ensuring CI Jobs are triggered as expected.

#### Deployment History Search Fix New UI <a href="#deployment-history-search-fix" id="deployment-history-search-fix"></a>

Fixed an issue where searching by **Deployment Label** in the Deployment History page did not return matching deployment records, even though the deployments were present in the history. The search logic has been updated to use the correct deployment label field, ensuring accurate results when searching by full or partial deployment label names.

#### Scratch Org ALM Mapping Validation Fix <a href="#scratch-org-alm-mapping-validation-fix" id="scratch-org-alm-mapping-validation-fix"></a>

Fixed an issue where creating a Scratch Org failed with the error **"Please fill in all required ALM mapping fields"** even when all required mappings were configured. The validation logic has been updated to correctly recognize ServiceNow ALM mappings, allowing users to proceed with Scratch Org creation successfully.

#### Org Synchronization Deployment Navigation Fix (New UI) <a href="#org-synchronization-deployment-navigation-fix-new-ui" id="org-synchronization-deployment-navigation-fix-new-ui"></a>

Fixed an issue where initiating an Org Synchronization deployment did not automatically redirect users to the Deployment History page. The navigation flow has been updated to redirect users after deployment initiation, and automatic log polling has been added so deployment progress and status are displayed without requiring manual page refreshes.

**Automatic OAuth Token Refresh and PKCE Support for External Connected Apps – Enhancement**

Enhanced Salesforce External Connected App authentication with automatic OAuth token refresh and support for **Proof Key for Code Exchange (PKCE)** for newly registered Salesforce organizations.

When an access token expires, ARM uses the stored refresh token to obtain a new access token and automatically retries the original Salesforce API request, eliminating the need for manual reauthorization. PKCE support further strengthens the security of the OAuth authorization flow.

#### AiAuthoringBundle Merge Validation Fix <a href="#aiauthoringbundle-merge-validation-fix" id="aiauthoringbundle-merge-validation-fix"></a>

Fixed an issue where EZ-Merge validation for **AiAuthoringBundle** metadata failed because the required `.bundle-meta.xml` file was not included in the deployment package during merge validation. ARM now automatically includes the corresponding bundle metadata file, ensuring successful validation and consistent behavior across subsequent versions of the same agent.

***

## ARM **Release Notes 26.3.3**

**Release Date: 19 July 2026**

#### Release Label Artifact Update Fix <a href="#release-label-artifact-update-fix" id="release-label-artifact-update-fix"></a>

Fixed an issue where updating an existing Release Label with a new revision did not regenerate the associated artifact correctly, resulting in missing delta files. ARM now regenerates the package manifest using the latest revision data whenever a Release Label is updated, ensuring the generated artifact accurately reflects all changes included in the updated Release Label.

#### Ignore Installed Components Information Update <a href="#ignore-installed-components-information-update" id="ignore-installed-components-information-update"></a>

Updated the **Ignore Installed Components** option across ARM to provide clearer guidance on its behavior. An informational message is now displayed wherever this option is available, helping users understand when installed components will be skipped during deployment and CI Job execution. This enhancement improves usability by setting the correct expectations before the operation is initiated.

#### Additional Vlocity DataPack Metadata Support <a href="#additional-vlocity-datapack-metadata-support" id="additional-vlocity-datapack-metadata-support"></a>

Added support for the following Vlocity DataPack metadata types in ARM:

* OfferMigrationPlan
* CpqConfigurationSetup
* IntegrationRetryPolicy
* String

These metadata types can now be retrieved through Vlocity commit workflows, committed to version control, and deployed between Salesforce orgs while preserving the required matching keys, parent-child relationships, and Global Key handling.

#### Financial Cloud Standard Value Set Support <a href="#financial-cloud-standard-value-set-support" id="financial-cloud-standard-value-set-support"></a>

Added support for additional Salesforce Financial Cloud Standard Value Sets to ensure standard picklist values are correctly retrieved during metadata operations. This enhancement improves compatibility with Salesforce Financial Cloud by enabling standard value sets to be included in EZ-Commit, Review Artifact creation, and selective deployment workflows.

#### Deployment History Visibility Fix <a href="#deployment-history-visibility-fix" id="deployment-history-visibility-fix"></a>

Fixed an issue where newly initiated deployments could temporarily disappear from the **Deployment History** page after clicking **Deploy**, requiring multiple page refreshes before becoming visible. The deployment processing flow has been updated to ensure deployment jobs are displayed immediately after they are initiated, providing a more consistent and reliable user experience.

#### Sharing Rule Destructive Change Detection Fix <a href="#sharing-rule-destructive-change-detection-fix" id="sharing-rule-destructive-change-detection-fix"></a>

Fixed an issue where deleted **Sharing Rule** metadata was not automatically detected as a destructive change during Version Control deployments. ARM now correctly identifies deleted Sharing Rule components and automatically includes them in the **Destructive Items** list, ensuring consistent destructive change handling across DX, Non-DX, and Release Label deployment workflows.

***

## ARM **Release Notes 26.3.2**

**Release Date: 12 July 2026**

#### Salesforce CLI Upgrade <a href="#salesforce-cli-upgrade" id="salesforce-cli-upgrade"></a>

Upgraded the bundled **Salesforce CLI (SF CLI)** from **v2.130.9** to **v2.140.6** to incorporate the latest Salesforce CLI enhancements, stability improvements, and bug fixes. This update improves compatibility with the latest Salesforce platform capabilities and ensures continued support for ARM operations that rely on the Salesforce CLI.

#### EZ-Merge Multi-Level Approval Fix - New UI <a href="#ez-merge-multi-level-approval-fix-new-ui" id="ez-merge-multi-level-approval-fix-new-ui"></a>

Fixed an issue in the New UI where EZ-Merge requests requiring multiple approval levels could complete after the first approval instead of progressing through the configured approval workflow. The approval flow has been corrected to properly process all configured approvers, ensuring merge requests follow the expected approval sequence before completion.

#### Subscription Management for All Customers <a href="#subscription-management-for-all-customers" id="subscription-management-for-all-customers"></a>

Enhanced **Subscription Management** to be available for all ARM customers, regardless of the number of purchased licenses. Customers with fewer than 20 licenses can now access subscription details, release allocated licenses, and manage license usage without requiring manual intervention for license downgrades. Team management remains unchanged for customers with 20 or more licenses, while the **Create Team** option is unavailable for customers with fewer than 20 licenses.

This enhancement simplifies license management and enables a smoother license downgrade process.

#### Vlocity Build Tool CLI Upgrade <a href="#vlocity-build-tool-cli-upgrade" id="vlocity-build-tool-cli-upgrade"></a>

Upgraded the bundled **Vlocity Build Tool (VBT) CLI** from **v1.17.20** to **v1.17.24** to include the latest fixes, stability improvements, and compatibility updates for Vlocity-related operations in ARM.

#### Compare Process Notification Improvement <a href="#compare-process-notification-improvement" id="compare-process-notification-improvement"></a>

Updated the Compare Changes workflow to display a clear warning message instead of an error when a compare or commit operation is already in progress in another browser tab or session. This provides a more accurate user experience and better communicates the operation status during concurrent Compare Changes activities.

#### External Client Application File Diff Fix <a href="#external-client-application-file-diff-fix" id="external-client-application-file-diff-fix"></a>

Fixed an issue where deleting an **External Client Application (ECA)** through EZ-Commit did not generate the expected file diff, causing the commit process to fail. Support for ECA metadata has been added to ensure file differences are generated correctly during both direct commits and pre-validation commit workflows involving metadata deletions.

#### EZ-Merge File Difference Consistency Fix <a href="#ez-merge-file-difference-consistency-fix" id="ez-merge-file-difference-consistency-fix"></a>

Fixed an issue where the file changes displayed during EZ-Merge did not match the changes shown during the corresponding EZ-Commit. The merge file comparison logic has been corrected to ensure the merge preview accurately reflects the committed changes, providing consistent and reliable file difference information during conflict resolution.

#### Provar Configuration Display Fix - New UI <a href="#provar-configuration-display-fix-new-ui" id="provar-configuration-display-fix-new-ui"></a>

Fixed an issue in the New UI where Provar configuration fields were not displayed after selecting **Provar** in the CI Job Tests screen. The configuration options now load correctly, allowing users to configure the required Provar settings, including Repository, Branch, Test Cases Root Path, and Test Cases Execution Path.

#### SonarQube Baseline Branch Support - New UI <a href="#sonarqube-baseline-branch-support-new-ui" id="sonarqube-baseline-branch-support-new-ui"></a>

Fixed multiple issues in the New UI where the **Baseline Branch** dropdown was not displayed for SonarQube Static Code Analysis. The Baseline Branch selection is now available and retained correctly across EZ-Merge, CI Job Edit, and SCA Label workflows, ensuring a consistent configuration experience with CodeScan.

#### Credential Creation Save Button Fix - Old UI

Fixed an issue in the Old UI where the **Save** button did not respond when creating a new credential due to a client-side loading error. The credential creation dialog now loads correctly, allowing users to save new credentials successfully.

#### Release Labels Loading Fix - New UI

Fixed an issue in the New UI where navigating directly to the **Release Labels** page from the left-side menu caused the page to remain in an infinite loading state. The navigation flow has been corrected to ensure the Release Labels page loads successfully when accessed directly.

#### **Package.xml Upload Fix (Old UI)**

Fixed an issue in the Classic (Old) UI where clicking **Select Package.xml** while creating a Custom Deployment from **Package.xml** did not respond or open the local file browser. The upload component has been corrected to initialize properly, allowing users to successfully select and upload **Package.xml** and ZIP deployment files during deployment creation. This issue was limited to the Classic UI and did not affect the New UI.

***

## DataLoader + DataLoader Pro Release Notes **26.3.2**

**Release Date:** **12 July 2026**

#### Knowledge KAV language filter not auto-populating in New UI <a href="#dt-13616-knowledge-kav-language-filter-not-auto-populating-in-new-ui" id="dt-13616-knowledge-kav-language-filter-not-auto-populating-in-new-ui"></a>

Fixed an issue in the New UI where the **Language** filter on the Knowledge KAV object did not prefill with the existing language value. The filter behavior now matches the Old UI.

***

## ARM **Release Notes 26.3.1.1**

**Release Date: 6 July 2026**

#### SSO Login Redirection Fix

Fixed an issue that prevented users from logging in through Single Sign-On (SSO) due to an overly restrictive Content Security Policy (CSP). The SSO redirection flow has been updated to allow successful authentication and seamless redirection to the configured identity provider.

**Impacted Areas:**

* SSO Authentication

***

## ARM **Release Notes 26.3.1**

**Release Date: 5 July 2026**

#### Backup-Enabled Validation Metadata Retrieval Fix <a href="#backup-enabled-validation-metadata-retrieval-fix" id="backup-enabled-validation-metadata-retrieval-fix"></a>

Fixed an issue where Validate Only deployments with Backup enabled could fail due to additional metadata retrieval during the backup flow. The backup metadata retrieval process has been improved to correctly handle validation scenarios and avoid unnecessary failures when deployment components are limited to selected metadata.

**Impacted Areas:**

* Deployment Module

#### Branch Unregistration Improvements <a href="#branch-unregistration-improvements" id="branch-unregistration-improvements"></a>

Improved the branch unregistration process to ensure branch-related records are cleaned up correctly during synchronization. The update enhances multi-branch unregistration handling, removes stale branch mapping data, and improves logging to provide more accurate status reporting and consistent behavior across branch synchronization workflows.

**Impacted Areas:**

* Version Control Repository Settings
* Sync Branches

#### Apache Tomcat 11.0.22 Upgrade <a href="#apache-tomcat-11.0.22-upgrade" id="apache-tomcat-11.0.22-upgrade"></a>

Upgraded Apache Tomcat from **11.0.21** to **11.0.22** across Shared, Dedicated, and On-Prem environments to incorporate the latest security fixes and stability improvements. This update enhances platform security while maintaining compatibility and consistent performance across all deployment models.

**Impacted Areas:**

* Shared Instances
* Dedicated Instances
* On-Prem Deployments

#### Permission Set Compare Changes Consistency Fix <a href="#permission-set-compare-changes-consistency-fix" id="permission-set-compare-changes-consistency-fix"></a>

Fixed an issue where the **Compare Changes** view did not match the actual changes committed to GitHub when using **Create/Append Revision to Existing Label** in EZ-Commit. Permission Set commit options are now applied consistently throughout the commit workflow, ensuring the Compare Changes view accurately reflects the final commit content.

**Impacted Areas:**

* EZ-Commit

#### CI Job File Changes Retention Fix <a href="#ci-job-file-changes-retention-fix" id="ci-job-file-changes-retention-fix"></a>

Fixed an issue where the **File Changes** tab in CI Job history could appear empty after historical CI Job data was cleaned up. The retention process has been updated to preserve the required file difference information, ensuring deployed file changes remain available for supported CI Job history records.

**Impacted Areas:**

* CI Jobs

#### Microsoft Teams Workflows Webhook Support <a href="#microsoft-teams-workflows-webhook-support" id="microsoft-teams-workflows-webhook-support"></a>

Added support for **Microsoft Teams Workflows** webhook URLs, enabling ARM notifications to continue working as Microsoft phases out traditional Incoming Webhooks. ARM can now deliver deployment and system notifications using the new Teams Workflows integration, helping customers transition seamlessly to Microsoft's supported notification model.

**Impacted Areas:**

* Notification Integrations

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/webhooks/teams-workflows" %}

***

## DataLoader & DataLoader Pro Release Notes **26.3.1**

**Release Date:** **05 June 2026**

#### Query Editor Workflow for Dynamic and Custom Queries – DL & DL PRO

The Query Editor in DataLoader Basic and DataLoader Pro now supports two modes: **Query Builder Mode** (build queries using field selections, filters, and order-by options) and **Manual Query Edit Mode** (edit queries directly in the text editor). Users can seamlessly switch between modes with clear confirmation prompts, and the system correctly manages state transitions to prevent conflicts between manual edits and dynamic query generation.

***

## ARM **Release Notes 26.2.13**

**Release Date: 28 June 2026**

#### Environment Provisioning History Performance Improvement

Improved the Environment Provisioning History screen performance by implementing backend pagination. This ensures history records load based on the selected page size, reducing load time during initial access and page refresh.

**Impacted Area:**

* Environment Provisioning History

#### CodeScan Project-Level Exclusions Support

Improved CodeScan integration to correctly honor project-level file exclusions configured in the CodeScan UI when no exclusions are defined in the ARM CodeScan plugin. ARM-defined exclusions continue to take precedence when explicitly configured, ensuring consistent and expected scan behavior across analysis workflows.

**Impacted Areas:**

* CodeScan Integration

#### Profile IP Ranges Handling Enhancement

Enhanced Profile IP Range handling to support consistent **Append**, **Replace All**, and **Remove IP Ranges** behavior across commit and deployment workflows. The **Replace All** option now ensures Profile IP ranges are fully synchronized from the source or branch metadata, aligning target org values with the selected deployment source while keeping other Profile metadata behavior unchanged.

**Impacted Areas:**

* Commit Workflows
* Deployments

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/getting-started-1/arm-administration/manage-users-account-settings/profile-ip-range-handling" %}

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm/arm-administration/profile-ip-range-handling" %}

#### GitHub Enterprise OAuth Validation

Improved repository registration by validating GitHub repository URLs before allowing OAuth authentication. OAuth registration is now restricted to GitHub Cloud repositories, and users attempting to register GitHub Enterprise repositories are prompted to use Username/PAT authentication instead, preventing unsupported configurations and subsequent branch operation failures.

**Impacted Area:**

* Repository Registration (New UI)
* GitHub OAuth Authentication

#### CI Job Repository Cloning Performance Improvement

Improved CI Job execution performance by resolving an issue that caused unnecessary repository cloning during Repo-to-Org workflows. Repository configuration handling has been enhanced to reuse existing repository data where applicable, reducing clone operations and improving overall CI Job execution time.

**Impacted Areas:**

* CI Jobs – Repo-to-Org (DX & Non-DX)
* Repository Cloning Performance

#### GitHub OAuth Branch Creation UI Improvement

Improved the EZ-Commit branch creation experience for GitHub OAuth repositories by hiding the **Credentials** selection when OAuth authentication is in use. This ensures the branch creation dialog displays only relevant options, providing a cleaner and more intuitive user experience.

**Impacted Area:**

* EZ-Commit Branch Creation
* GitHub OAuth Repository Integration (New UI)

#### Pre-Validation Commit SCA Date Filter Fix - New UI

Fixed an issue in the New UI where Pre-Validation Commit SCA did not correctly apply the selected date range due to a date format parsing error. The date selection handling has been updated so SCA analyzes only the components within the chosen date range.

**Impacted Area:**

* EZ-Commit → Pre-Validation Commit

***

## ARM **Release Notes 26.2.12**

**Release Date: 21 June 2026**

#### Merge Conflict Resolution Progress Indicator

Enhanced the merge conflict resolution workflow to provide better visibility and prevent duplicate actions during commit processing. A progress indicator is now displayed when conflict resolution commits and related background downloads are initiated, and user actions are properly synchronized to prevent multiple commit requests and UI exceptions.

**Impacted Area:**

* Version Control → Commit History → Conflict Resolution Workflow

#### AccelQ Error Details Display Fix

Fixed an issue where error details for failed AccelQ test cases were not displayed in the Old UI. Users can now view failure information, including error messages and test execution details, directly from the test report, providing consistent behavior across both Old and New UI experiences.

**Impacted Areas:**

* CI Jobs – Test Results
* Deployment Module – Test Results
* AccelQ Integration (Old UI)

#### Deployment Comparison Handling for Destructive Changes

Fixed an issue in the New UI where deployment comparisons could become unresponsive when only destructive changes were selected. Comparison handling has been improved to correctly process destructive metadata selections and prevent comparison workflows from getting stuck during metadata retrieval.

**Impacted Areas:**

* Org-to-Org Deployments
* Deployment Comparison (New UI)
* Destructive Change Processing

#### Register Branch Usability Improvements

Enhanced the Register Branch experience by enabling branch searches to be executed using the **Enter** key in the Branch Name Search field, providing a faster and more intuitive workflow. Additionally, the informational Note  message has been updated for improved clarity.

**Updated Note Message:**

* **Previous:** _Support to "src" as default folder is no more exists._
* **Updated:** _Support to "src" as default folder if no other folders exist._

**Impacted Areas:**

* Register Branch (Classic UI)
* User Interface Messaging

#### Deployment Compare Screen Validation Message Fix - New UI

Fixed an issue in the New UI where an incorrect destructive-change confirmation dialog was displayed on the Compare screen when no constructive members were selected. Users now receive an appropriate validation message prompting them to select at least one member before proceeding, ensuring a clearer and more consistent deployment experience.

**Impacted Areas:**

* Deployment Compare Screen (New UI)

#### Dataloader Post-Activity Status Handling Fix

Fixed an issue in CI Jobs where Dataloader post-activity processing could continue logging repeated status checks even after the Dataloader job had completed. Status handling has been improved to correctly recognize completion states and stop further polling, ensuring post-activity logs accurately reflect the final execution status.

**Impacted Area:**

* CI Jobs – Post Activities

#### CodeScan Report Synchronization Fix

Fixed an issue where ARM displayed incorrect CodeScan analysis results by retrieving report data from an unrelated scan instead of the executed analysis. Report retrieval logic has been updated to ensure ARM displays the correct violations and file counts, keeping SCA results synchronized with the corresponding CodeScan execution.

**Impacted Areas:**

* Static Code Analysis (SCA) Reports

***

## ARM **Release Notes 26.2.11**

**Release Date: 14 June 2026**

#### Parallel Processor Execution Fix <a href="#parallel-processor-execution-fix" id="parallel-processor-execution-fix"></a>

Fixed an issue in CI Jobs where Parallel Processor executions could fail to trigger external automation workflows due to backend request handling inconsistencies. The execution logic has been updated to ensure parallel processor requests are processed correctly, improving the reliability of post-deployment automation integrations.

**Impacted Areas:**

* CI Jobs
* Parallel Processor Integration
* Post-Deployment Automation Workflows

#### Branching Baseline Deletion Control Improvement <a href="#branching-baseline-deletion-control-improvement" id="branching-baseline-deletion-control-improvement"></a>

Improved Branching Baseline handling by restricting deletion actions when an abort operation is already in progress. This prevents users from performing conflicting actions on baseline iterations and helps maintain consistent baseline processing behavior.

**Impacted Area:**

* Settings → Branching Baseline Module

#### Connected App Search & Substitute Support <a href="#connected-app-search-and-substitute-support" id="connected-app-search-and-substitute-support"></a>

Enhanced Search & Substitute to support `ConnectedApp` metadata, allowing users to dynamically replace Connected App configuration values during Commit, CI Job, and Deployment execution.

This enhancement helps manage environment-specific Connected App configurations without manual XML updates.

**Impacted Areas:**

* Search & Substitute

#### Permission Set Agent Access Support <a href="#permission-set-agent-access-support" id="permission-set-agent-access-support"></a>

Added support for the `<agentAccesses>` node in Salesforce Permission Sets to ensure agent access configurations are correctly retained during metadata operations. Previously, these entries were retrieved successfully but were excluded during commit processing. With this enhancement, agent access configurations are now preserved across version control and deployment workflows.

**Impacted Areas:**

* Version Control
* Deployments

#### Package.xml Custom Object Retrieval Fix <a href="#package.xml-custom-object-retrieval-fix" id="package.xml-custom-object-retrieval-fix"></a>

Fixed an issue in EZ-Commit where certain metadata components, including Custom Objects, could be skipped when retrieving components using an uploaded `package.xml`. The package.xml retrieval logic has been improved to ensure valid metadata components are retained and displayed correctly in the Added/Modified Metadata Components tab.

**Impacted Area:**

* EZ-Commit using `package.xml`

#### Merge Approval Link Fix - New UI <a href="#merge-approval-link-fix-new-ui" id="merge-approval-link-fix-new-ui"></a>

Fixed an issue in the New UI where approvers saw an “Unknown Error” after clicking the approval link from an EZ-Merge email notification. The approval link now redirects correctly to the Merge Label approval pop-up, allowing users to review and approve merge requests as expected.

**Impacted Area:**

* EZ-Merge Approval Workflow (New UI)

#### Branch Permission Inheritance for Commit Visibility <a href="#branch-permission-inheritance-for-commit-visibility" id="branch-permission-inheritance-for-commit-visibility"></a>

Fixed an issue where commit labels created by sub-users were not visible to Custom Admins when branches were created through the EZ-Commit workflow. Branch permissions are now automatically inherited and synchronized during branch creation, ensuring authorized users can view and approve commits without requiring manual branch access assignment.

**Impacted Areas:**

* EZ-Commit Branch Creation
* Commit Label Visibility

#### Commit Label Visibility for Custom Admins <a href="#commit-label-visibility-for-custom-admins" id="commit-label-visibility-for-custom-admins"></a>

Fixed an issue where Custom Admins could not view or approve commit labels created by sub-users when branches were created through the EZ-Commit workflow. Branch permissions are now automatically inherited from the parent branch and synchronized during branch creation, ensuring commit labels remain visible and accessible to authorized approvers.

**Impacted Areas:**

* EZ-Commit Branch Creation
* Commit Label Visibility

***

## DataLoader Pro Release Notes **26.2.11**

**Release Date:** **14 June 2026**

#### DL Data Retention Policy Fix <a href="#dt-13273-ncino-and-dl-data-retention-policy-fix" id="dt-13273-ncino-and-dl-data-retention-policy-fix"></a>

Fixed missing components in the data retention policy for "DL & DL PRO". Single DataLoader bulk file deletion was not being executed, and "DL & DL PRO" S3 backup deletions were targeting the wrong bucket. ARM data retention settings now apply to "DL & DL PRO" by default without requiring a separate checkbox.

#### DataLoader Pro Query Failure on Knowledge\_\_kav Object <a href="#dt-13345-dataloader-pro-query-failure-on-knowledge__kav-object-support-case-234338" id="dt-13345-dataloader-pro-query-failure-on-knowledge__kav-object-support-case-234338"></a>

Fixed an issue where DataLoader Pro jobs failed when a custom query was applied to the `Knowledge__kav` object. The error occurred because the system incorrectly appended a `WHERE` clause to queries that already contained filtering conditions (e.g., `LIMIT`), resulting in a syntax error. Query construction logic has been corrected to handle Knowledge objects properly.

***

## ARM **Release Notes 26.2.10**

**Release Date: 7 June 2026**

#### Support for Salesforce Run Relevant Tests in Deployments (New Enhancement) <a href="#support-for-salesforce-run-relevant-tests-in-deployments-new-enhancement" id="support-for-salesforce-run-relevant-tests-in-deployments-new-enhancement"></a>

AutoRABIT now supports Salesforce’s **Run Relevant Tests** test level for deployment validations and deployments. This option executes only the Apex tests identified by Salesforce as impacted by the changes being deployed, helping reduce deployment time and improve CI/CD efficiency while maintaining required test coverage. Support is available across validation, deployment, and Quick Deploy workflows.

#### Salesforce Summer ’26 (API Version 67) Support (New) <a href="#salesforce-summer-26-api-version-67-support-new" id="salesforce-summer-26-api-version-67-support-new"></a>

AutoRABIT now supports **Salesforce API Version 67**, enabling compatibility with the latest Salesforce Summer ’26 release. This update includes support for newly introduced metadata types such as **FlowValueMap, EmailAuthorizationSettings, InsPlcyLimitConsumptionRule, and OrchestrationPlanCtxMapping**, along with support for Salesforce metadata enhancements in Queue, DataSrcDataModelFieldMap, Network, InvocableActionExtension, and Flow.

#### EZ-Commit Performance Improvements for Large Salesforce Schemas <a href="#ez-commit-performance-improvements-for-large-salesforce-schemas" id="ez-commit-performance-improvements-for-large-salesforce-schemas"></a>

Enhanced EZ-Commit performance for Salesforce orgs containing large volumes of custom fields and metadata components. Optimizations to schema processing and change detection improve component loading, retrieval responsiveness, and overall user experience across EZ-Commit, AutoDraft, and Package Manifest workflows.

#### My Profile – VC Mappings Performance Improvements <a href="#my-profile-vc-mappings-performance-improvements" id="my-profile-vc-mappings-performance-improvements"></a>

Improved performance of the **My Profile → VC Mappings** page for environments with a large number of branches. Backend pagination and loading optimizations reduce page load times and improve responsiveness when viewing and managing version control mappings.

#### EZ-Commit User Experience Improvements <a href="#ez-commit-user-experience-improvements" id="ez-commit-user-experience-improvements"></a>

Enhanced the EZ-Commit save experience by improving validation feedback for required fields. Mandatory fields are now clearly highlighted when left unselected, helping users identify missing information more quickly and reducing submission errors.

***

## ARM **Release Notes 26.2.9**

**Release Date: 31 May 2026**

#### Bitbucket Token Authentication & Email Support Update <a href="#bitbucket-token-authentication-and-email-support-update" id="bitbucket-token-authentication-and-email-support-update"></a>

**Effective Date: 9 June 2026**

To align with Bitbucket's deprecation of App Passwords, ARM now supports Token-based authentication for Bitbucket integrations and introduces an optional **Email Address** field for Bitbucket credentials. The email address is used for Bitbucket API operations such as Pull Request creation, while Git operations (Clone, Fetch, Push) continue to work using Token or SSH authentication.

Existing App Password credentials will continue to function until Bitbucket's deprecation date. Customers are encouraged to migrate to Token-based authentication and update their Bitbucket credentials with an email address to ensure uninterrupted API functionality.

**Action Required:**\
Review and update your Bitbucket credentials to use Token authentication and provide an email address for API-based operations.

For complete details, configuration steps, and migration guidance, please refer to the documentation link below:

**Documentation:**

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm-1/getting-started-1/registration/version-control-repository/bitbucket/configuring-bitbucket-token-authentication-and-email-support" %}

{% embed url="https://knowledgebase.autorabit.com/product-guides/arm/registration/version-control-repository/bitbucket/configuring-bitbucket-token-authentication-and-email-support" %}

#### Pin/Favorite CI Jobs for Quick Access - New UI <a href="#pin-favorite-ci-jobs-for-quick-access-new-ui" id="pin-favorite-ci-jobs-for-quick-access-new-ui"></a>

Introduced the ability to pin or favorite CI Jobs in the New UI, allowing users to quickly access frequently used jobs without searching through the full job list. Pinned jobs are displayed in a dedicated section at the top of the CI Job List and are maintained individually for each user.

**Impacted Area:**

* CI Jobs List (New UI)

#### SiteDotCom Metadata Retrieval Fix <a href="#sitedotcom-metadata-retrieval-fix" id="sitedotcom-metadata-retrieval-fix"></a>

Fixed an issue where `SiteDotComSite` metadata changes were not included in Single Revision Deployments and Release Labels when only the `.site` file was modified. Metadata processing has been improved to correctly retain and retrieve associated SiteDotCom components, ensuring changes are accurately captured across deployment workflows.

**Impacted Areas:**

* Single Revision Deployment
* Revision Range Deployment
* Release Labels
* Org-to-Org Deployments
* CI Jobs (DX & Non-DX)
* SiteDotCom Metadata Processing

#### SonarQube Analysis Result Synchronization Fix <a href="#sonarqube-analysis-result-synchronization-fix" id="sonarqube-analysis-result-synchronization-fix"></a>

Fixed an issue where SonarQube violations were not displayed in the ARM Analysis Dashboard despite being available in SonarQube. The result retrieval process has been updated to correctly fetch and synchronize SonarQube scan results, ensuring accurate visibility of violations within ARM.

**Impacted Areas:**

* EZ-Commit
* EZ-Merge
* Static Code Analysis (SCA)
* CI Jobs using SonarQube Integration

***

## ARM **Release Notes 26.2.8.1**

**Release Date: 27 May 2026**

#### Conflict File Truncation Fix <a href="#conflict-file-truncation-fix" id="conflict-file-truncation-fix"></a>

Fixed an issue in EZ-Merge where conflicted files could become truncated during conflict resolution, causing merge failures for certain profile files. The file copy handling has been improved to ensure complete file content is preserved during conflict processing.

**Impacted Areas:**

* EZ-Merge

#### Multiple Branch Mapping Retention Fix <a href="#multiple-branch-mapping-retention-fix" id="multiple-branch-mapping-retention-fix"></a>

Fixed an issue in My Version Control Mappings where selecting and saving a new branch caused previously mapped branches to become unselected. The credential update logic has been improved to retain mappings for existing branches while updating credentials only for the selected branch.

**Impacted Areas:**

* My Version Control Mappings
* Branch Creation
* Branch Registration
* Credential Mapping Workflows

***

## ARM **Release Notes 26.2.8**

**Release Date: 24 May 2026**

#### **Improvements to Log Viewer Experience - New UI** <a href="#improvements-to-log-viewer-experience" id="improvements-to-log-viewer-experience"></a>

We’ve enhanced the log viewing experience across multiple ARM modules to improve usability and performance.

**What’s Improved**

* Removed unwanted auto-scroll behavior for completed jobs and logs
* Users can now freely interact with the page without UI locking
* Added quick navigation buttons to:
  * Scroll to Top
  * Scroll to Bottom
* Added Full-Screen mode for easier log analysis
* Improved live log streaming and polling for running jobs
* Enhanced handling of large logs for smoother scrolling and improved responsiveness

**Impacted Areas**

CI Jobs, Deployment, Dataloader, Reports, SFDX, Admin Settings, and Version Control.

#### **Improvements to EZ-Commit Destructive Changes Handling** <a href="#improvements-to-ez-commit-destructive-changes-handling" id="improvements-to-ez-commit-destructive-changes-handling"></a>

Enhanced the handling and display of deleted metadata changes in EZ-Commit for improved consistency and accuracy.

**What’s Improved**

* Added support for displaying `Action = D` for deleted metadata changes in the Old UI
* Improved consistency between the Old UI and New UI for destructive changes handling
* Updated deleted changes behavior during the `package.xml` upload flow:
  * `Modified By` and `Modified Date` fields will now remain empty for destructive changes to avoid misleading information

**Impacted Areas**

EZ-Commit – Deleted Metadata Changes Handling (Destructive Changes)

***

## ARM **Release Notes 26.2.7**

**Release Date:** **17 May 2026**

#### Report Folder Selection Handling <a href="#report-folder-selection-handling" id="report-folder-selection-handling"></a>

Improved metadata filtering in VC-EZ-Commit to correctly recognize nested Report folders from `package.xml` uploads, even when a corresponding metadata file is not present. This ensures complete folder hierarchies are properly detected and displayed during metadata selection.

**Impacted Area:** VC-EZ-Commit

#### Azure Logic App Audit Log API Compatibility <a href="#azure-logic-app-audit-log-api-compatibility" id="azure-logic-app-audit-log-api-compatibility"></a>

Enhanced the Audit Logs service to improve compatibility with Azure Logic Apps by removing mandatory header validation for GET requests. This resolves issues where audit log API calls were failing due to automatically stripped `Content-Type` headers in Azure Logic App integrations.

**Impacted Area:** Audit Logs Service

#### Branch Credential Mapping Improvement <a href="#branch-credential-mapping-improvement" id="branch-credential-mapping-improvement"></a>

Improved branch credential mapping in ARM Version Control to ensure branches created through the EZ-Commit workflow are correctly associated with the user-selected credentials. This resolves issues where feature branches created by sub-users were not searchable during PR creation workflows.

**Impacted Areas:**

* EZ-Commit
* Pull Request Workflow
* Branch Registration & Credential Mapping
* Version Control Repository Integration

#### Enhanced Pagination Support - New UI <a href="#enhanced-pagination-support-new-ui" id="enhanced-pagination-support-new-ui"></a>

Improved pagination options across deployment reporting screens by adding support for viewing up to 100 records per page. This enhancement helps users review large datasets more efficiently within Deployment History, Release Labels, and related deployment report views.

**Impacted Areas:**

* Deployment History
* Release Labels

#### Active CI Job Filtering in Permissions - New UI <a href="#active-ci-job-filtering-in-permissions-new-ui" id="active-ci-job-filtering-in-permissions-new-ui"></a>

Updated the New UI permissions workflow to display only active CI jobs during user permission assignment, aligning the behavior with the Old UI experience. This prevents inactive jobs from appearing in CI job selection lists across permission management screens.

**Impacted Areas:**

* Users & Permissions

#### AiAuthoringBundle Metadata Support <a href="#aiauthoringbundle-metadata-support" id="aiauthoringbundle-metadata-support"></a>

Added support for the `AiAuthoringBundle` metadata type across ARM metadata operations, enabling proper handling during deployments, exclusions, skip-member configurations, and CI job processing. This resolves issues where deployments involving `AiAuthoringBundle` components were failing or not being recognized correctly.

**Impacted Areas:**

* CI Jobs
* Deployment Module
* Version Control

***

## DataLoader Pro Release Notes **26.2.7**

**Release Date:** **17 May 2026**

#### **ZIP File Attachments Not Migrating via Data Loader Pro**

Resolved an issue where ZIP file attachments associated with HTML Report object records were not being migrated from Production to sandbox environments using Data Loader Pro. PDF and other attachment types migrated correctly, but ZIP files were silently skipped. All attachment types now migrate as expected.

***

## ARM **Release Notes 26.2.6.1** <a href="#release-notes-26.2.6.1" id="release-notes-26.2.6.1"></a>

**Release Date: 13 May 2026**

#### Deployment and Validation Status Reporting Failure for Salesforce Summer ’26 Sandboxes <a href="#deployment-and-validation-status-reporting-failure-for-salesforce-summer-26-sandboxes" id="deployment-and-validation-status-reporting-failure-for-salesforce-summer-26-sandboxes"></a>

Resolved an issue where Merge/Commit validations and deployments were incorrectly reported as failed in ARM for Salesforce Sandbox/Production environments upgraded to Salesforce Summer ’26 (API version 67).

Customers experienced the following error in ARM UI popup messages and logs when using any Test Level option:

* Run Local Tests
* Run All Tests
* Run Specified Tests
* Use Salesforce Default

`com.sforce.ws.ConnectionException: unable to find end tag at: START_TAG seen ...`

**Resolution**

Upgraded Salesforce Metadata API libraries to version 67 to support Salesforce Summer ’26 API response changes and ensure accurate deployment and validation status reporting.

***

## **ARM Release Notes 26.2.6**

**Release Date: 10 May 2026**

#### Testim Integration with ARM CI Jobs – New UI

Testim is now integrated with ARM CI Jobs to enable automated testing, rollback handling, and improved deployment visibility.

* Enabled execution of Testim tests (Suite, Label, Plan) within CI Jobs
* Added automatic test execution during CI runs
* Introduced rollback on failure based on test results
* Added email notifications with test results, job details, and rollback status
* Provided execution logs and results in CI Job history

More Information: https://knowledgebase.autorabit.com/product-guides/arm-1/integration-and-plugins/testim

***

#### Date Filter UX Improvements – New UI

Enhancements to the date filter improve usability and accuracy in the New UI.

* Calendar now opens only for Custom Range selection
* Predefined ranges apply instantly without requiring Apply
* Fixed incorrect month display and removed future month visibility

***

#### SCM Authentication Improvements for Branch Registration

Improvements to repository credential handling ensure consistent authentication during branch registration.

* Save button enabled only when changes are made
* Validates last modified user’s credentials during branch registration
* Automatically falls back to repository-level credentials if validation fails

***

#### CI Job History – Job Name Visibility Enhancements – New UI

Enhancements improve visibility and readability of CI job names.

* Job Name column is now resizable in CI List and Job History pages
* Improved handling of long job names to reduce truncation

***

#### EZ Commit Label Validation Fix – New UI

Resolved inconsistency in label validation between New UI and Old UI.

* Updated validation logic to support special characters
* Fixed regex for allowed and invalid characters
* Labels with characters like -, ., +, \[ ] are now accepted

***

#### Run Specified Tests – Multiple Test Input Fix – New UI

Resolved issue with handling multiple test class inputs during deployments.

* Restored support for comma-separated test classes
* Supports input via comma, Enter key, and pasted values
* Each test class is correctly parsed as an individual entry

***

#### Commit Fetching Fix for SFDX Repositories

Resolved issue where commits were not fetched for SFDX repositories.

* Updated SSH-based logic to fetch revisions based on selected package directory
* Ensures commits are retrieved correctly when a package folder is selected

***

## ARM **Release Notes 26.2.5.1** <a href="#release-notes-26.2.6.1" id="release-notes-26.2.6.1"></a>

**Release Date: 13 May 2026**

#### Deployment and Validation Status Reporting Failure for Salesforce Summer ’26 Sandboxes <a href="#deployment-and-validation-status-reporting-failure-for-salesforce-summer-26-sandboxes" id="deployment-and-validation-status-reporting-failure-for-salesforce-summer-26-sandboxes"></a>

Resolved an issue where Merge/Commit validations and deployments were incorrectly reported as failed in ARM for Salesforce Sandbox/Production environments upgraded to Salesforce Summer ’26 (API version 67).

Customers experienced the following error in ARM UI popup messages and logs when using any Test Level option:

* Run Local Tests
* Run All Tests
* Run Specified Tests
* Use Salesforce Default

`com.sforce.ws.ConnectionException: unable to find end tag at: START_TAG seen ...`

**Resolution**

Upgraded Salesforce Metadata API libraries to version 67 to support Salesforce Summer ’26 API response changes and ensure accurate deployment and validation status reporting.

***

## ARM **Release Notes 26.2.5** <a href="#release-notes-26.2.5" id="release-notes-26.2.5"></a>

**Release Date: 3 May 2026**

#### **Configurable Deployment Behavior for Profile IP Ranges (Limited)** <a href="#id-1.-configurable-deployment-behavior-for-profile-ip-ranges-new-enhancement" id="id-1.-configurable-deployment-behavior-for-profile-ip-ranges-new-enhancement"></a>

Introduced a new configuration to control how Profile IP Ranges are handled during deployments. This feature is enabled via a **Feature Flag**, and the **Deployment Mode** options are visible only when the flag is turned ON.

**Deployment Mode Options:**

* **Append (Default):** Adds new IP ranges without removing existing ones in the target
* **Replace All:** Ensures the target matches the source/package by deploying only the IP ranges included and removing any others from the target

**Important Notes:**

* The **Replace All** option is fully supported for **Org-to-Org deployments**, where it aligns the target exactly with the source.
* For other deployment types (such as CI Jobs, Single Revision, Commit Label, and Revision Range), behavior depends on **package preparation**. Only the IP ranges included in the deployment package are applied, and any others **will be removed** from the target.
* Since these deployments follow a **delta-based mechanism**, users should carefully prepare packages when using **Replace All** to avoid unintended removal of IP ranges.

#### **BotOne V Metadata Upload – Full Path Exposure Fix (Support Case #213285)**

Fixed an issue where full file path details were exposed during metadata ZIP upload for the BotOne V type, posing a potential security concern.

This issue occurred due to missing bot metadata during Release Label package generation. The fix ensures that the required bot metadata is included, preventing path exposure and ensuring correct upload behavior.

**Impacted Areas:**\
Release Labels, DX Deployments, DX ZIP Deployment, CI Jobs (DX with Bot metadata)

#### **Independent Visibility for Permission Set Commit Options (Enhancement)**

Improved the EZ Commit experience by making Permission Set commit options visible independently in the Submit Validation panel. Previously, the **Remove user permissions** option was only shown when **Commit access settings for selected metadata** was enabled, causing confusion.

With this enhancement:

* Both options are now displayed by default when a Permission Set is selected.
* Users can choose either option independently or use both together, without any dependency between them.

**Impacted Areas:**\
Version Control – EZ Commit

#### **SonarQube New Code Identification Fix for PR Analysis (Support Case #204387)**

Fixed an issue where SonarQube analysis from ARM did not correctly identify new code for commits made to non-main branches without an associated Pull Request. Previously, such analyses were treated as standalone branches, leading to incorrect reporting.

With this fix, the selected baseline branch is now correctly used during Pull Request analysis. This ensures that changes are properly compared and reflected under **New Code** in SonarQube, improving accuracy and consistency in reporting.

**Impacted Areas:**\
EZ Commit, EZ Merge, SCA Reports, Deployments with SCA (SonarQube Integration)

#### **Stale Scheduled Job Execution Fix for ACCELQ Jobs (Support Case #222962)**

Fixed an issue where scheduled jobs were triggering even when they were not present, deleted, or not properly saved in the UI. This caused inconsistencies between the UI and scheduler, leading to repeated and unnecessary job executions.

With this fix, cleanup logic has been implemented to remove stale and orphaned scheduler (cron) entries for ACCELQ jobs. Jobs that are deleted or not properly configured are no longer triggered, ensuring alignment between the UI and scheduler state.

**Impacted Areas:**\
CI Jobs, Scheduler (ACCELQ Jobs), Deployment Execution

#### **Pattern-Based Substitution Support for Named Credentials (Enhancement)**

Enhanced the Search & Substitute feature to support pattern/wildcard-based substitution for Named Credential parameter values. Previously, only exact-match substitutions were supported, requiring multiple rules for similar URL patterns.

With this enhancement, a new subelement, **namedCredential.parameterValueMatchExpression**, allows users to define a single rule to handle multiple URL variations dynamically. This reduces duplication and simplifies maintenance by replacing only the matched portion while preserving the remaining value.

Existing exact-match behavior using **namedCredential.parameterValue** remains unchanged.

**Impacted Areas:**\
Admin – Search & Substitute, CI Jobs, Deployment Configuration

***

## DataLoader Pro Release Notes **26.2.5** <a href="#release-notes-26.2.3" id="release-notes-26.2.3"></a>

**Release Date:** **03 May 2026**

**DataLoader Pro Job Result Inaccessible**\
Resolved an issue where result files from completed DataLoader Pro jobs were not accessible. Users can now successfully view and download job results as expected.

***

## **ARM Release Notes 26.2.4** <a href="#release-notes-26.2.3" id="release-notes-26.2.3"></a>

**Release Date:** **26 April 2026**

#### **Accurate Error Message Display for Deployment Failures (Support Case #207169)** <a href="#accurate-error-message-display-for-deployment-failures-support-case-207169" id="accurate-error-message-display-for-deployment-failures-support-case-207169"></a>

Fixed an issue where incorrect or misleading error messages were displayed in the Deployment UI logs. In certain cases, users saw generic authentication-related errors, even when the actual failure was due to invalid deployment configurations (e.g., selecting “No Test Run” for Production deployments).

With this fix, the UI now reflects the correct backend error messages, providing clear and accurate insights into deployment failures. This helps users quickly identify and resolve issues.

**Impacted Areas:**\
Deployment, CI Jobs

#### **Template Sharing for Subusers – Environment Provisioning (Both UIs) - New Enhancement** <a href="#template-sharing-for-subusers-environment-provisioning-both-uis-new-enhancement" id="template-sharing-for-subusers-environment-provisioning-both-uis-new-enhancement"></a>

Introduced an enhancement to allow Subusers to share environment provisioning templates they have created. Previously, only Admin users could share templates.

With this update:

* Subusers can now share their own templates.
* Sharing remains restricted for templates created by other users.
* Admin users continue to have full sharing access across all templates.

This improvement reduces dependency on Admins and enables better collaboration.

**Impacted Areas:**\
Environment Provisioning (Template Management) – Old UI & New UI

#### **Multiple Diff View Support in EZ-Commit – New UI (Support Case #215475)** <a href="#multiple-diff-view-support-in-ezcommit-new-ui-support-case-215475" id="multiple-diff-view-support-in-ezcommit-new-ui-support-case-215475"></a>

Enhanced the EZ-Commit experience in the New UI to allow users to view multiple file diffs simultaneously. Previously, opening a diff would automatically close any previously opened diff, limiting comparison across components.

With this update, users can expand multiple diff sections at the same time, enabling easier side-by-side review and improved validation before committing.

**Impacted Areas:**\
EZ-Commit, CI Jobs, Deployments, Version Control, Merge Requests

#### **Baseline Revision Selection Display Fix – Classic UI (Support Case #211183)** <a href="#baseline-revision-selection-display-fix-classic-ui-support-case-211183" id="baseline-revision-selection-display-fix-classic-ui-support-case-211183"></a>

Fixed an issue in the Classic UI where the selected Baseline Revision was not visually reflected in the CI Job edit screen, even though it was correctly saved. This caused confusion and unnecessary validation errors.

With this fix, the selected revision is now properly highlighted, and users are automatically navigated to the relevant page. If no revision is selected, the default view is shown without disruption.

**Impacted Areas:**\
CI Jobs, Deployments, Merge Requests (Revision Selection Popup)

#### **Merge Conflict Email Notification Accuracy Fix (Support Case #210042)** <a href="#merge-conflict-email-notification-accuracy-fix-support-case-210042" id="merge-conflict-email-notification-accuracy-fix-support-case-210042"></a>

Fixed an issue where non-conflicting files were incorrectly listed under the “Conflicted Files” section in merge conflict email notifications.

With this fix, only the actual conflicting files are displayed in the “Conflicted Files” section, while successfully merged files are shown correctly under “Merged Files,” improving clarity and accuracy of notifications.

**Impacted Areas:**\
Version Control – EZ-Merge

#### **Apache Tomcat Upgrade for On-Prem Instances** <a href="#apache-tomcat-upgrade-for-on-prem-instances" id="apache-tomcat-upgrade-for-on-prem-instances"></a>

Upgraded Apache Tomcat from version 11.0.13 to 11.0.21 for all On-Prem deployments. This update ensures improved performance, enhanced security, and better stability of the ARM application environment.

**Impacted Areas:**\
On-Prem Installations

#### **Login Redirection Issue Fix – New UI (Support Case #214960,#222145,#218645)** <a href="#login-redirection-issue-fix-new-ui-support-case-214960" id="login-redirection-issue-fix-new-ui-support-case-214960"></a>

Fixed an issue where users were unable to log in correctly after enabling the New UI and were repeatedly redirected despite switching back to the Old UI.

This fix ensures stable login behavior by restoring failed script handling and improving error visibility, allowing users to successfully access the application across browsers.

**Impacted Areas:**\
Login, UI Navigation (Old UI & New UI)

#### **Faster Branch Creation Using GitHub API (Both UIs) - New Enhancement** <a href="#faster-branch-creation-using-github-api-both-uis-new-enhancement" id="faster-branch-creation-using-github-api-both-uis-new-enhancement"></a>

Introduced an enhancement to improve branch creation performance by creating branches instantly using the GitHub API. Previously, branch creation was delayed due to synchronous workspace copy and setup processes.

With this update:

* Branches are created immediately upon user action.
* Workspace checkout and related processes run asynchronously in the background.
* Users can access and start working on the branch without delay.
* The system falls back to the existing process if GitHub pull request support is not enabled.

This enhancement improves responsiveness and overall user experience.

**Impacted Areas:**\
Version Control, EZ-Commit (Old UI & New UI)

#### **CI Jobs List Auto-Refresh Fix After Activate/Deactivate (Support Case #217089 – New UI)** <a href="#ci-jobs-list-auto-refresh-fix-after-activate-deactivate-support-case-217089-new-ui" id="ci-jobs-list-auto-refresh-fix-after-activate-deactivate-support-case-217089-new-ui"></a>

Fixed an issue in the New UI where the CI Jobs list did not automatically refresh after activating or deactivating a job. Previously, although the change was successfully applied in the backend, the UI did not reflect the updated _Last Date Modified_ or reorder the job in the list until a manual refresh was performed.

With this fix, the CI Jobs list now refreshes automatically upon successful activation or deactivation. The _Last Date Modified_ timestamp is updated instantly, and the modified job is moved to the top of the list, ensuring consistency with the default sorting behavior.

**Impacted Areas:**\
CI Jobs – List Page (New UI)

#### **Users/Permissions Access Issue for Non-Admin Users (Support Case #216643 – New UI)** <a href="#users-permissions-access-issue-for-non-admin-users-support-case-216643-new-ui" id="users-permissions-access-issue-for-non-admin-users-support-case-216643-new-ui"></a>

Fixed an issue where non-admin users were unable to directly access the Users/Permissions section in the New UI despite having the required permissions. Access was only possible after navigating via the Old UI, leading to inconsistent behavior.

With this fix, routing logic now correctly validates user permissions, allowing direct access from the New UI and ensuring consistent behavior across both interfaces.

**Impacted Areas:**\
User Management – Navigation (Old UI & New UI)

#### **Apache Tomcat Upgrade to Version 11.0.21 (Shared & Dedicated Environments)** <a href="#apache-tomcat-upgrade-to-version-11.0.21-shared-and-dedicated-environments" id="apache-tomcat-upgrade-to-version-11.0.21-shared-and-dedicated-environments"></a>

Upgraded Apache Tomcat from version 11.0.13 to 11.0.21 across both Shared (SaaS) and Dedicated environments to address known security vulnerabilities and improve overall platform stability.

This upgrade ensures a secure and reliable runtime environment, with validation confirming compatibility across multi-tenant and customer-specific setups. Core functionalities, performance, and environment-specific configurations continue to operate as expected post-upgrade.

**Impacted Areas:**\
Platform Infrastructure – Shared (SaaS) & Dedicated Environments

#### **Salesforce CLI Upgrade to v2.130.9 (Support Case #219699)** <a href="#salesforce-cli-upgrade-to-v2.130.9-support-case-219699" id="salesforce-cli-upgrade-to-v2.130.9-support-case-219699"></a>

Upgraded the Salesforce CLI from version 2.125.2 to 2.130.9 across development and CI/CD environments to ensure compatibility with the latest Salesforce features, bug fixes, and security updates.

Post-upgrade validation confirmed that existing workflows—including deployments, org authentication, and package operations—continue to function as expected, with no impact on automation or pipelines.

**Impacted Areas:**\
Development Environments, CI/CD Pipelines, Deployment Workflows

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

## **ARM Release Notes 26.2.2**

**Release Date:** **12 April 2026**

#### **1. ARM Deployment: Improved Error Message Rendering (Support Case #206745 – New UI)**

Fixed an issue in the New UI where ARM did not correctly parse or escape `< >` characters in error messages returned from Salesforce during deployments. This caused error details to display incorrectly in the Failed Components section of the deployment report.

With this fix, error messages are now properly rendered, ensuring accurate and readable visibility into deployment failures.

**Impacted Areas:**\
Deployment Report (Failed Components Section)

***

#### **2. Permission Set XML Consistency for Data Cloud (Support Case #211123)**

Resolved an issue where Data Cloud-enabled Permission Sets showed inconsistencies between ARM IDE and Compare Files, due to the `<dataspaceScopes>` node missing in comparison results. This prevented users from committing changes successfully.

Support for the `dataspaceScopes` field has now been added, ensuring accurate metadata mapping when present in the Salesforce org. This enables seamless comparison, commit, and deployment of Permission Sets.

**Impacted Areas:**\
EZ Commit, Merge, Deployment, CI Jobs (DX and Non-DX)

***

#### **3. EZ Commit: Duplicate Component Selection Prevention (Support Case #212351 – New UI)**

Fixed an issue in the New UI where components selected under the Added/Modified Components tab in EZ-Commit (with Autodraft enabled) were not reflected in the All Metadata Components tab, allowing duplicate selections during commit.

With this fix, component selections are now synchronized across tabs, preventing duplicates and ensuring accurate commit lists.

**Impacted Areas:**\
EZ-Commit Flow

***

#### **4. CI & Selective Deployment: Consistent Component Evaluation (Support Case #210095)**

Addressed inconsistent behavior between CI Jobs and Selective Deployment when using the Ignore Installed Components option.

* In CI Jobs, component evaluation was correctly performed at the parent level, resulting in the expected “No local changes to deploy” message.
* In Selective Deployment, evaluation was limited to the child level, leading to incorrect deployment eligibility.

This fix aligns Selective Deployment logic with CI behavior, ensuring consistent and accurate component evaluation across deployment flows.

**Impacted Areas:**\
Org-to-Org Deployment, VC-to-Org Deployment (Workflow Metadata)

***

#### **5. Salesforce Org Registration via OAuth with ECA Fails with “Undefined Error” (Support Case #217635)**

Fixed an issue where users encountered an “undefined error” while registering a Salesforce Org in AR using OAuth via ECA. This issue was specific to version 26.2.1 and did not occur in earlier releases.

With this fix, the missing SfOrg ID is now properly added during new org registration, allowing Salesforce orgs to be registered successfully through OAuth with ECA.

**Impacted Areas:**\
Salesforce Org Registration, ECA OAuth Flow

***

#### **6. ALM Integration Enhancements (Salesforce)**

**Note:** These enhancements are available only in the New UI.

**Overview**

This release enhances AutoRABIT’s ALM integration by extending automatic Work Item status updates beyond commit operations. Updates are now supported across multiple modules, enabling consistent lifecycle tracking within Salesforce ALM.

**What’s New**

**Work Item Status Updates Across Modules**\
Work Item status updates are now supported in:

* EZ-Commit (existing support)
* Merge Requests (new UI)
* EZ-Merge (new UI)
* CI Jobs (new UI)

These enhancements enable automatic synchronization of Work Item statuses during key development activities such as commits, merges, and CI pipeline executions, improving traceability and process consistency.

***

## **ARM Release Notes 26.2.1** <a href="#release-notes-version-26.2.1" id="release-notes-version-26.2.1"></a>

**Release Date: 05 April 2026**

1. **Custom Setting Migration Template – Save Confirmation Pop-up Fix (New UI) \[SupportCase#205885]**\
   Fixed an issue where newly provisioned data values were not displayed in the Save confirmation pop-up while creating or editing a Custom Setting migration template in the New UI. This prevented users from verifying configuration details before saving.\
   This issue was limited to the New UI and did not impact the Old UI.\
   **Impacted Areas:**\
   Environment Provisioning, Custom Setting Migration Template (Save & Edit – New UI)<br>
2. **Quick Deploy Not Enabled for UseSalesforceDefaults – \[Support Case #203174]**\
   Fixed an issue where the Quick Deploy option was not available in CI jobs when using the UseSalesforceDefaults test level, even though it was supported and enabled in the Salesforce Production org.\
   This update ensures ARM behavior aligns with Salesforce by correctly enabling Quick Deploy based on the selected test level.\
   **Impacted Areas:**\
   CI Jobs (Org-to-Org, VC-to-Org Deployments)<br>
3. **CI Job Stuck in In-Progress State Blocking PR Validation Trigger – \[Support Case #201347]**\
   Fixed an issue where CI jobs remained in an In-progress state in the Job History UI even after successful validation. This prevented subsequent CI builds, including PR validation jobs, from triggering automatically.\
   The issue also caused abort actions from the UI to fail. With this fix, CI job statuses are now correctly updated upon completion, ensuring normal job execution flow.\
   **Impacted Areas:**\
   CI Jobs<br>
4. **AI Metadata Components Not Processed in Org-to-Org Deployments –  \[Support Case #201393]**\
   Fixed an issue where AI metadata components (GenAiFunction) were not properly processed during Org-to-Org deployments, causing compare operations to hang indefinitely and direct deployments to fail with a “No changes found” message.\
   This update ensures AI metadata components are correctly considered during deployment and comparison workflows, enabling successful execution.\
   **Impacted Areas:**\
   Deployments (Org-to-Org)<br>
5. **Release Label Not Fetching Latest HEAD Revisions –  \[Support Case #201799]**\
   Fixed an issue where merged revisions from pull requests were not being fetched during Release Label creation, even though they were present in the remote repository. This led to discrepancies where revisions were visible in EZ-Merge but missing in Release Label selection.\
   This update improves the revision-fetching logic to include all relevant folder-based and merged revisions, ensuring consistency across features.\
   **Impacted Areas:**\
   Release Labels, EZ-Merge, CI Job Configuration, Deployments (Single Revision & Range), nCino Flows<br>
6. **Commit History Date Format Inconsistency –  \[Support Case #209987]**\
   Fixed an issue where the commit history date format in the New UI differed from the Old UI. Previously, the New UI displayed dates in DD/MM/YY format, while the Old UI followed MM/DD/YY, leading to inconsistency.\
   This update standardizes the date format in the New UI to match the Old UI for a consistent user experience.\
   **Impacted Areas:**\
   Commit History, Version Control<br>
7. **Save Button Triggering Re-authentication in Salesforce Org Details –  \[Support Case #213381]**\
   Fixed an issue where clicking the Save button in the Salesforce Org Detail page incorrectly triggered the re-authentication flow, redirecting users to the Salesforce login page.\
   This update ensures that the Save action only updates org details within the application, while the Re-authenticate action correctly handles the login flow, maintaining clear separation of functionality.\
   **Impacted Areas:**\
   Settings → Salesforce Org<br>
8. **EZ Commit Pagination Infinite Loop in New UI –  \[Support Case #213239]**\
   Fixed an issue in the EZ Commit flow where the paginated component list entered an infinite loop when users rapidly navigated between pages after setting a higher pagination limit.\
   This update improves pagination handling to ensure smooth and stable navigation across component lists.\
   **Impacted Areas:**\
   Version Control (EZ Commit), Metadata Selection Pagination (New UI)<br>
9. **Unable to Add Users in New UI Due to Missing Mail Extension –  \[Support Case #214523]**\
   Fixed an issue where admins were unable to add new users in the New UI because the mail extension dropdown appeared empty, preventing user creation.\
   This update ensures the default domain is correctly handled and displayed, allowing admins to successfully add users.\
   **Impacted Areas:**\
   Admin → User Management (New UI)

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

## **ARM Release Notes 26.1.13**

**Release Date: 29 March 2026**

#### **Automatic Dependency Fetch for Data Cloud Data Kits (DX only) - New UI**

ARM now automatically retrieves all dependent metadata for a selected Salesforce Data Cloud Data Kit using connected org credentials. This eliminates the need to manually download and upload the package manifest (_package.xml_) during commit or deployment workflows.

This enhancement streamlines the process, reduces manual effort, and minimizes errors.

**Impacted Areas:**\
Data Cloud Deployments, Commit Workflow.

***

#### **Environment Provisioning – Post Deployment Behavior Fix -** #201758

Fixed issues with the Post Deployment step to ensure templates are included only when explicitly selected.

This update improves usability and ensures more reliable execution of provisioning steps.

**Impacted Areas:**\
Environment Provisioning, Migration Templates

#### **CodeScan Baseline Not Applied in EZ Commit – Fix - (**#199417,#204388,#204387)

Resolved an issue where the configured CodeScan baseline was not applied during **EZ Commit** or **EZ Merge** operations for mapped Salesforce orgs.

The system now correctly uses the defined baseline for analysis.

**Impacted Areas:**\
EZ Commit, EZ Merge, SCA Module

#### **OmniStudio Components Missing in CI Deployments – Fix -** #206010

Fixed an issue where OmniStudio components (such as **OmniScript** and **OmniDataTransform**) were excluded from CI deployments when listed under excluded metadata types.

Improved visibility helps identify such configurations and ensures accurate deployments.

**Impacted Areas:**\
CI Jobs, OmniStudio Deployments

#### **CI Jobs History – “More Info” Text Selection Fix -** #209352

Fixed a regression in the New UI where users were unable to select or copy text from the **More Info** popup in CI Jobs History.

Text selection and copying now work as expected.

**Impacted Areas:**\
CI Jobs History, More Info Popup (New UI)

#### **Missing Bot & GenAI Metadata in Deployments – Fix -** #209232

Fixed an issue where **GenAI** and **GenAI Planner Bundle** metadata were not included during deployments using Release Labels, even when selected.

Deployments now correctly include all selected metadata components.

**Impacted Areas:**\
Commits, Deployments

#### **Assessment Metadata Missing in Release Label Deployments – Fix -** #204091

Resolved an issue where **AssessmentQuestionSet** and **AssessmentQuestion** metadata were not included during Release Label deployments.

These components are now properly processed and deployed.

**Impacted Areas:**\
Deployments, CI Jobs

#### **LightningTypeBundle Metadata Not Detected in EZ Commit – Fix -** #210860

Fixed an issue where **LightningTypeBundle** metadata was not retrieved or displayed in **Review Artifacts** during EZ Commit, resulting in missing diffs.

The system now correctly detects and processes this metadata across workflows.

**Impacted Areas:**\
EZ Commit, EZ Merge, CI Jobs, Deployments

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

## ARM Release Notes 26.1.12 <a href="#release-notes-version-26.1.12" id="release-notes-version-26.1.12"></a>

**Release Date:** **22 March 2026**

#### **Code Coverage & Test Class Report Structure Enhancement (New Enhancement)** <a href="#code-coverage-and-test-class-report-structure-enhancement-new-enhancement" id="code-coverage-and-test-class-report-structure-enhancement-new-enhancement"></a>

Improved the structure of the **Code Coverage Report CSV** and **Test Class report** so that the test class name is now repeated on every row for each test method. This makes sorting, filtering, and analysis by class and method more reliable, especially for larger orgs.

**Impacted Areas**\
Code Coverage Report CSV\
Test Class Report

***

#### **Parallel Processor Support in CI Jobs – New UI** <a href="#parallel-processor-support-in-ci-jobs-new-ui" id="parallel-processor-support-in-ci-jobs-new-ui"></a>

The **Parallel Processor** configuration is now available in the **New UI** for CI Jobs. This feature allows users to configure **GET or POST requests** to be executed before or after a Salesforce deployment as part of the CI job execution.

This capability was previously available in the **Old UI** and has now been integrated into the **New UI** with the same functionality and behavior, ensuring feature parity across both interfaces.

**Impacted Areas**\
CI Jobs – New UI Configuration

***

#### **Scratch Org Deployment – Access Token Retrieval Fix** <a href="#scratch-org-deployment-access-token-retrieval-fix" id="scratch-org-deployment-access-token-retrieval-fix"></a>

Fixed an issue where **CI Job deployments from a Salesforce Org to a Scratch Org** could fail with a **400 Bad Request error** while attempting to fetch an access token using the stored refresh token. This occurred when the **destination org was registered using Standard authentication and had a different login URL than the source org** (for example, Production/Developer source org and Sandbox destination org).

The token retrieval logic has been updated to correctly handle such scenarios, preventing CI job failures during Scratch Org deployments.

**Impacted Areas**\
CI Jobs – Deploy from Salesforce Org to Scratch Org

***

#### **Dev Hub Selection Retention Fix – Create Unlocked Package Version and Install It to Salesforce (New UI)** <a href="#dev-hub-selection-retention-fix-create-unlocked-package-version-and-install-it-to-salesforce-new-ui" id="dev-hub-selection-retention-fix-create-unlocked-package-version-and-install-it-to-salesforce-new-ui"></a>

Fixed an issue in the **New UI** where the selected **Dev Hub** was not retained in the CI Job type **“Create Unlocked Package Version and Install It to Salesforce.”** After saving the job configuration and completing deployment, returning to the **Edit Deployment** screen showed the **Dev Hub** field as empty, even though a value had been previously selected.

The initialization logic has been corrected to ensure the saved **Dev Hub selection is retained and displayed properly** when reopening the job configuration.

**Impacted Areas**\
CI Job → Create Unlocked Package Version and Install It to Salesforce → Deployment Settings → Dev Hub Selection (New UI)

***

#### **ContentAsset Handling Fix – Release Label Artifacts** <a href="#contentasset-handling-fix-release-label-artifacts" id="contentasset-handling-fix-release-label-artifacts"></a>

Fixed an issue where **including a ContentAsset modification revision in a Release Label artifact** caused package generation to fail with an error indicating missing source files for the **ContentAsset** type.

The packaging logic has been updated to ensure that when a **ContentAsset** `.meta.xml` **file** is detected, the corresponding **binary asset file** is also included in the generated package if it exists in the repository. This prevents manifest generation failures and ensures ContentAssets are packaged correctly.

**Impacted Areas**\
Release Labels in Version Control (DX and Non-DX)\
Release Label Deployment and Merge (ContentAsset changes)

***

#### **CI Job Backup Failure Fix – Unsupported Metadata Type Handling** <a href="#ci-job-backup-failure-fix-unsupported-metadata-type-handling" id="ci-job-backup-failure-fix-unsupported-metadata-type-handling"></a>

Fixed an issue where **CI Jobs configured for Backup to Version Control** could fail with the error **“Missing metadata type definition in registry for id 'CustomObjectBinding'.”**

This occurred because Salesforce exposes the **CustomObjectBinding** metadata type during discovery, even though it is not currently supported for retrieval. The system previously attempted to include this metadata in retrieval batches, causing the job to fail.

The metadata type has now been **added to the exclusion map**, preventing retrieval attempts and allowing CI backup jobs to complete successfully.

**Impacted Areas**\
CI Jobs – Backup to Version Control

***

#### **1-Month Data Retention Policy Option** <a href="#id-1-month-data-retention-policy-option" id="id-1-month-data-retention-policy-option"></a>

ARM now supports a **1-Month retention policy** to provide greater flexibility in managing system data. Previously, retention policies were limited to **3 months, 6 months, and 12 months**.

With this enhancement, administrators can configure a **30-day retention period**, enabling automatic removal of data older than one month. This helps organizations better manage storage usage, improve system performance, and align with internal compliance or governance requirements.

Existing configurations using **3-month, 6-month, or 12-month** retention policies remain unchanged.

**Impacted Areas**\
Administration → Retention Policy Settings

***

#### **Multiple Approver Support for EZ-Merge – New UI** <a href="#multiple-approver-support-for-ez-merge-new-ui" id="multiple-approver-support-for-ez-merge-new-ui"></a>

Added support for selecting **multiple approvers in EZ-Merge** within the **New UI**. Previously, users were limited to selecting only a **single approver** when creating a merge request, unlike the Old UI which allowed multiple approvers.

This enhancement restores the ability to **select multiple approvers for merge approvals**, aligning the New UI behavior with the functionality available in the Old UI.

**Impacted Areas**\
EZ-Merge – New UI

***

#### **CI Job Configuration Save Fix – Install Package Job (New UI)** <a href="#ci-job-configuration-save-fix-install-package-job-new-ui" id="ci-job-configuration-save-fix-install-package-job-new-ui"></a>

Fixed an issue in the **New UI** where configuration changes were not saved correctly for the CI Job type **“Install an Unlocked or Managed Package from a Version Control Branch.”** In some cases, fields such as **Run Apex Compile, Security Type, and Upgrade Type** reverted to different values when switching between the New UI and Old UI.

The issue was caused by values not being properly retained in **disabled fields** during the save operation. This has been corrected to ensure the selected configuration values are saved and displayed accurately.

**Impacted Areas**\
CI Job → Edit Job → Deploy Page (New UI)

***

#### **Salesforce Spring ’26 (API 66) Metadata Support** <a href="#salesforce-spring-26-api-66-metadata-support" id="salesforce-spring-26-api-66-metadata-support"></a>

ARM now supports additional metadata types introduced with **Salesforce Spring ’26 (API 66)**. The following metadata types are now supported:

* AffinityScoreDefinition
* CleanDataService
* DuplicateRule
* ExtlClntAppCanvasSettings
* Flow sub-types (FlowSchedule, FlowScreenStyleSetting)
* GiftEntryGridTemplate

**Impacted Areas**\
Version Control\
Deployments\
CI Jobs

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

## ARM Release Notes 26.1.11 <a href="#release-notes-version-26.1.11" id="release-notes-version-26.1.11"></a>

**Release Date:** **15 March 2026**

#### Backup to Version Control – Credential Refresh Fix <a href="#backup-to-version-control-credential-refresh-fix" id="backup-to-version-control-credential-refresh-fix"></a>

Fixed an issue in **CI → Jobs → Backup to Version Control** where changing the selected repository or branch did not refresh the associated credentials. The system previously continued using credentials from the initial selection, which could lead to authentication failures or incorrect commit identities. The credential refresh logic has been corrected to ensure the appropriate credentials are loaded whenever the repository or branch selection changes.

**Impacted Areas**\
CI → Jobs → Backup to Version Control

***

#### EZ-Commit – Retrieval Logs Button Fix <a href="#ez-commit-retrieval-logs-button-fix" id="ez-commit-retrieval-logs-button-fix"></a>

Fixed an issue in **Version Control → EZ-Commit (Review Artifact screen)** where the **Retrieval Logs** button became unresponsive after the first click. Users can now open the logs panel multiple times without interruption, ensuring smooth review of retrieval logs during the commit process.

**Impacted Areas**\
EZ-Commit (Version Control) → Retrieval Logs Button

***

#### Mail Extension Placeholder & Validation Fix – New UI <a href="#mail-extension-placeholder-and-validation-fix-new-ui" id="mail-extension-placeholder-and-validation-fix-new-ui"></a>

Fixed an issue in the **New UI → My Account → Mail Extensions** where the placeholder text in the **Extension Name field** suggested using an “@” symbol even though the system does not allow it. The placeholder and validation message have been updated to display valid examples and ensure consistency with the accepted input format.

**Impacted Areas**\
New UI → My Account → Mail Extensions

***

#### Env Provisioning – Unsupported Metadata Template Execution Fix <a href="#env-provisioning-unsupported-metadata-template-execution-fix" id="env-provisioning-unsupported-metadata-template-execution-fix"></a>

Fixed an issue in **Env Provisioning** where executing the **“DisableTeams” template (Environment Provisioning Unsupported Metadata)** returned a **Succeeded** status, but the changes were not reflected in the target Salesforce Org. The template creation logic has been updated to ensure the configuration is properly processed so that all expected settings are applied after execution.

**Impacted Areas**\
Env Provisioning

***

#### Environment Provisioning History – Pagination Fix <a href="#environment-provisioning-history-pagination-fix" id="environment-provisioning-history-pagination-fix"></a>

Fixed an issue in the **Environment Provisioning History** page where the grid displayed only **10 records** even when a higher page size was selected. Pagination has been corrected to ensure the grid displays the number of records based on the selected page size.

**Impacted Areas**\
Environment Provisioning History Page

***

#### Environment Provisioning – Duplicate Template Name Validation <a href="#environment-provisioning-duplicate-template-name-validation" id="environment-provisioning-duplicate-template-name-validation"></a>

Fixed an issue in **New UI → Environment Provisioning → Templates** where the system allowed creation of templates with duplicate names without any validation. A validation check has been added to prevent duplicate template names and ensure users receive an appropriate error message when attempting to create one.

**Impacted Areas**\
Create New Environment Provisioning Template

***

#### #200317 – CI Jobs: Email Notification After Quick Deploy <a href="#id-200317-ci-jobs-email-notification-after-quick-deploy" id="id-200317-ci-jobs-email-notification-after-quick-deploy"></a>

Enhanced **CI Job notifications** to support sending report emails after **Quick Deploy** execution. Previously, email notifications were sent only after the **Validate** stage. With this update, users will also receive CI Job report emails once the **Quick Deploy** process is completed.

**Impacted Areas**\
CI Jobs with notification enabled and Quick Deploy applicable

***

#### #201002 – Revision Range Deployment Commit Selection Fix <a href="#id-201002-revision-range-deployment-commit-selection-fix" id="id-201002-revision-range-deployment-commit-selection-fix"></a>

Fixed an issue in **Deployment → Revision Range Deployments** where users were unable to select commits from the **first page of the “To” revision list** during a revision-range deployment. The UI logic has been corrected to allow proper selection of commits from the displayed list.

**Impacted Areas**\
Deployment → Revision Range Deployments

***

#### #198567 – Quick Merge Continue Button Fix (New UI) <a href="#id-198567-quick-merge-continue-button-fix-new-ui" id="id-198567-quick-merge-continue-button-fix-new-ui"></a>

Fixed an issue in **New UI → Version Control → Commit History** where the **Continue** button in **Quick Merge** was disabled immediately after performing a new **EZ-Commit**. Users can now proceed with Quick Merge without needing to exit and reopen the page.

**Impacted Areas**\
Version Control → Commit History → Quick Merge

***

#### #202013 – CheckmarxOne Project Creation During EZ-Merge <a href="#id-202013-checkmarxone-project-creation-during-ez-merge" id="id-202013-checkmarxone-project-creation-during-ez-merge"></a>

Resolved an issue where **AutoRABIT EZ-Merge operations with CheckmarxOne SCA validation** created a **new project in CheckmarxOne for every execution**. With the fix, scans executed during EZ-Merge will use a **single common project** instead of creating multiple projects.

To apply this behavior, enable the feature flag **ENABLE\_CHECKMARK\_COMMON\_PROJECT\_EZMERGE**, which ensures all EZ-Merge scans are executed under the project **“AR-Merge.”**

**Impacted Areas**\
EZ-Merge with CheckmarxOne SCA Validation

***

#### #203270 – CI Job Validate Only Execution Fix <a href="#id-203270-ci-job-validate-only-execution-fix" id="id-203270-ci-job-validate-only-execution-fix"></a>

Fixed an issue in **CI Jobs** where a queued job triggered with the **Validate Only** option executed as a **regular deployment**instead of validation. The issue occurred when multiple jobs were triggered and one entered the queue. The logic has been corrected to ensure queued jobs retain the **Validate Only** configuration and execute accordingly.

**Impacted Areas**\
CI Jobs with Deployment (Validate Only and Real Deployment) option

***

#### **GitHub OAuth Authentication Support for Repository Integration (New UI)**

Introduced OAuth-based authentication support for GitHub repository integration in ARM, alongside the existing Personal Access Token (PAT) method. Users can now select OAuth during repository registration, authorize access via GitHub, and securely connect repositories without manually managing tokens.

> **Note:** This feature is currently available only in the New UI.

For step-by-step guidance, refer to the documentation:<br>

[https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/version-control/introduction-to-version-control/oauth-support-for-github](https://knowledgebase.autorabit.com/product-guides/arm-1/arm-features/version-control/introduction-to-version-control/oauth-support-for-github)

**Impacted Areas:**\
Version Control → Repository Registration (GitHub OAuth)

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

## ARM Release Notes 26.1.10

**Release Date: 08 March 2026**

#### RecordType Picklist Values Detection Fix #190557

Resolved an issue where newly added `<picklistValues>` in **RecordType metadata** were not detected during **CI Job runs** or **Single Revision deployments** when the file contained a `<description>` node. The delta generation logic has been updated to ensure picklist value changes are correctly identified and included in deployment packages.

**Impacted Areas**\
Deployments, CI Jobs

***

## DataLoader Pro Release Notes 26.1.10&#x20;

**Release Date: 08 March 2026**

#### Processing Rule Migration – Parent-Child Relationship Fix

Resolved an issue where **Processing Rule child records were not created during sandbox migration**, causing all rules to be imported as parent records.

The migration logic has been updated to correctly handle **self-referential parent-child relationships**, ensuring that both parent and associated child rules are migrated as expected.

***

## ARM Release Notes 26.1.9

**Release Date: 01 March 2026**

This release includes usability improvements, UI consistency enhancements, deployment fixes, and expanded authentication support.

#### Merge Request – Delete Feature Branch Behavior Improvement

We’ve improved the behavior of the **“Delete Feature Branch”** option in Merge Requests to ensure a smoother and more predictable user experience.

#### What’s Improved

* The **Delete Feature Branch** button is automatically hidden after commit when _“Delete source branch”_ is selected.
* The button remains visible if the option is not selected.
* The button is temporarily disabled while deletion is in progress to prevent duplicate actions.

This enhancement prevents accidental multiple deletions and improves workflow clarity.

#### Clear AutorabitExtId – Status & Log Visibility Fix

Resolved icon visibility issues during the **Clear AutorabitExtId** operation in both Old UI and New UI.

### Improvements

* Status and Log icons no longer disappear during or after execution.
* Status now correctly updates to **Success** or **Failed** upon completion.
* Log access remains available after execution.
* In the New UI, the **Live Status Log** icon is visible during execution.

This ensures better execution tracking and improved transparency.

#### Static Resource Deletion Fix – CI Deployment

Addressed a CI deployment issue related to incomplete Static Resource deletions.

### Enhancement

* Static Resources are now fully removed during deletion.
* Prevents deployment errors caused by residual metadata.
* Ensures accurate manifest generation in CI jobs.

This improves deployment reliability and consistency.

#### Search Functionality Enhancement – Metadata Filters

Search functionality has been improved and aligned across Old UI and New UI.

#### Search Now Supports Filtering By:

* Metadata Member Name
* Modified By
* Modified Date

This resolves previous inconsistencies and ensures consistent filtering behavior across interfaces.

#### JIRA OAuth Redirection – 413 Error Fix

Resolved a **413 – Request Entity Too Large** error occurring during JIRA OAuth registration in the New UI.

OAuth registration now works seamlessly in both Old UI and New UI.

#### Salesforce Org Registration via OAuth – External Client App (ECA)

ARM now supports OAuth via External Client App (ECA) as a modern Salesforce authentication method.

#### What’s New

* New authentication option: OAuth via External Client App
* Secure OAuth authorization
* Encrypted token storage
* Token lifecycle management
* Re-authentication support with editable **Consumer ID** and **Consumer Key**
* Please use the link below for Step-by-Step guidance
* [https://knowledgebase.autorabit.com/product-guides/arm/registration/salesforce-org/register-salesforce-org-using-oauth-via-external-client-app-eca](https://knowledgebase.autorabit.com/product-guides/arm/registration/salesforce-org/register-salesforce-org-using-oauth-via-external-client-app-eca)

#### Migration Support

Existing Salesforce orgs using Standard or Connected App OAuth can migrate to ECA without:

* Creating a new org entry
* Losing pipelines, jobs, or configurations
* Affecting existing mappings

The authentication type and connection status update automatically upon successful migration.

This enhancement strengthens security and aligns with modern Salesforce authentication standards.

#### Salesforce Org Visibility After Permission Update (New UI)

Fixed an issue where updating User Permissions in the New UI caused the associated Salesforce Org to disappear from **My Profile → My Salesforce Orgs**.

The save logic has been corrected to ensure the Org association remains intact after permission updates.

***

## DataLoader Pro Release Notes 26.1.9&#x20;

**Release Date: 01 March 2026**

#### Hierarchical Object Handling – Parent Resolution Consistency

Enhanced object hierarchy handling to ensure consistent behavior between job configuration and execution.

Previously, in cases where an object (e.g., **Loan**) functioned both as a child (in the UI) and as a parent (in the hierarchy), additional parent objects were fetched during execution even if they were not selected during job creation.

With this fix, only the objects selected during configuration will be processed during execution, unless mandatory parent dependencies are explicitly required.

***

## ARM Release Notes 26.1.8 <a href="#release-notes-version-26.1.8" id="release-notes-version-26.1.8"></a>

**Release Date: 22 February 2026**

#### Test Mapping Management – Bulk Import/Export (New UI) <a href="#test-mapping-management-bulk-import-export-new-ui" id="test-mapping-management-bulk-import-export-new-ui"></a>

Enhanced Test Mapping management is now available in the new UI to simplify maintenance and reduce unnecessary test executions.

Users can now download existing test mappings, edit them offline, and re-upload via CSV for bulk updates. The uploaded file fully replaces the existing mapping set after confirmation. System validations ensure correct file format and structure before processing.

A backup of the previous file is automatically maintained (one version at a time) and can be downloaded if needed. The UI also displays last updated date and updated by details, with changes tracked in back-end tables.

**Note:** Only three columns are supported in import: Sno, Apex Test Class, and Apex Class/Trigger.

**Impacted Areas (DEV)**\
CI Jobs – Test Mapping Configuration (New UI)

**Functional Impact Areas (QA)**\
CI/CD – Run Tests Based on Changes\
Test Mapping Management (New UI Only)\*\*

#### Rollback Log – Org Name Display Fix <a href="#rollback-log-org-name-display-fix" id="rollback-log-org-name-display-fix"></a>

Fixed an issue where the **Org Name** was displayed as `null` on the Rollback Log page after executing a CI Job with rollback enabled.

The internal Org Name value was not populated during rollback execution, resulting in unclear log entries. Logging logic has been corrected to prevent null internal values from being displayed.

Additionally, unnecessary fields (`constructiveChanges`, `destructiveChangesPre`, `destructiveChangesPost`, `destructiveChanges`) were removed from rollback logging to avoid misleading entries.

**Impacted Areas (DEV)**\
Rollback Log Page

**Functional Impact Areas (QA)**\
CI Rollback

#### CI Job History – Pagination Missing for Sub-users <a href="#ci-job-history-pagination-missing-for-sub-users" id="ci-job-history-pagination-missing-for-sub-users"></a>

Fixed an issue where **Sub-users** could not see pagination controls on the **CI Job History** page. As a result, only the first **25** job records were shown and users could not navigate to additional history entries.

Sub-users can now view pagination (Next/Previous/page numbers) and access all available CI Job History records.

#### Sync Branch – Unregister Button Visibility Fix <a href="#sync-branch-unregister-button-visibility-fix" id="sync-branch-unregister-button-visibility-fix"></a>

Fixed a UI issue in the **Sync Branch** pop-up where the **Unregister** button was not visible when a large number of branches (100+) were listed. The modal did not provide scrolling, preventing users from accessing the action button.

A scrollable container has now been added to the branch list to ensure proper responsiveness. The Unregister button remains accessible regardless of the number of branches displayed or screen resolution.

**Impacted Areas (DEV)**\
Sync Branches Popup

**Functional Impact Areas (QA)**\
Sync Branches Popup

#### Report Deployment – Package Structure Fix- #193182 <a href="#report-deployment-package-structure-fix-193182" id="report-deployment-package-structure-fix-193182"></a>

Fixed an issue where Report deployments were failing with the error:\
_“An object '\<reportfolder/reportname>' of type Report was named in package.xml, but was not found in zipped directory.”_

The failure occurred due to additional child folder entries being incorrectly added to the generated `package.xml` during deployment. Package-generation logic has been corrected to include only the required Report folders and Report components, preventing mismatches between the package.xml and the zipped directory.

**Impacted Areas (DEV)**\
Deployments, CI Jobs (Org to Org, SCM Repo to Org), Commits including Reports

**Functional Impact Areas (QA)**\
Org to Org Deployment\
CI – Salesforce to Salesforce Deployment\
Repo to Org Deployment

#### ALM Integration (New UI) – Work Items Not Displaying - #198093 <a href="#alm-integration-new-ui-work-items-not-displaying-198093" id="alm-integration-new-ui-work-items-not-displaying-198093"></a>

Fixed an issue where work items were not displayed in the **ALM Integration (New UI)** for certain projects and sprint selections. The issue occurred due to the request payload using the project/sprint key instead of the required ID, resulting in empty responses.

The request handling has been updated to use the correct ID parameter, ensuring work items load properly for the selected project and sprint.

**Impacted Areas (DEV)**\
EZ-Merge – ALM Integration

**Functional Impact Areas (QA)**\
EZ-Merge – ALM Work Items (New UI)\*\*

#### Pagination Count & Record Display Fix <a href="#pagination-count-and-record-display-fix" id="pagination-count-and-record-display-fix"></a>

Fixed an issue where changing the pagination dropdown (e.g., 10 to 20 or 50 records) did not update the displayed results on the **CI Job History and Details** pages. The back-end logic has been corrected to properly apply the selected page size.

Also resolved pagination count mismatches observed in the following modules:

* Credential Page
* Commit History
* Branching Baseline
* CI Job Details

Pagination now correctly reflects the selected page size and displays accurate record counts across affected screens.

**Impacted Areas (DEV)**\
CI Job Details Page

**Functional Impact Areas (QA)**\
CI Job History and Related Modules

#### Default Apex Test Cases – Success Message Added <a href="#default-apex-test-cases-success-message-added" id="default-apex-test-cases-success-message-added"></a>

Fixed an issue where no confirmation message was shown after successfully downloading the **Default Apex Test Cases** file.

A success toast notification is now displayed once the export action completes, providing clear confirmation to the user.

**Impacted Areas (DEV)**\
Salesforce Org – Export (Default Apex Test Cases)

**Functional Impact Areas (QA)**\
UI/UX Validation – Toast Notifications & Front-End Response Handling

***

## ARM Release Notes 26.1.7

**Release Date: 15 February 2026**

#### Internal Cases <a href="#internal-cases" id="internal-cases"></a>

#### Smart Commit Pattern & Webhook Selection Not Persisting <a href="#smart-commit-pattern-and-webhook-selection-not-persisting" id="smart-commit-pattern-and-webhook-selection-not-persisting"></a>

Fixed an issue where the selected Smart Commit pattern and enabled Webhook settings under ALM Management were getting cleared after saving the Integration configuration.

The issue was caused by null values overwriting existing records in the database during update operations. The update logic has been modified to prevent null fields from overriding saved configurations, ensuring selections are retained correctly.

**Impacted Areas:** ALM Configuration Updation

#### Default Branch Not Updated After Deletion via Sync Branches <a href="#default-branch-not-updated-after-deletion-via-sync-branches" id="default-branch-not-updated-after-deletion-via-sync-branches"></a>

Fixed an issue where ARM did not automatically assign a new default branch after the existing default branch was deleted using the **Sync Branches** operation.

When the default branch was removed, the system failed to promote the last-used branch as the new default. The logic has been enhanced to detect deletion of the default branch and automatically update the last-used branch as the new default.

The implementation introduces a streamlined default-branch update flow (without unnecessary workspace creation) and consolidates common logic to avoid duplication.

**Impacted Areas:**\
Branch Management (Sync Branches), Branch Creation, Registration, Deletion, and Updation

#### Default Branch Not Reflected in UI After Sync (New UI) <a href="#default-branch-not-reflected-in-ui-after-sync-new-ui" id="default-branch-not-reflected-in-ui-after-sync-new-ui"></a>

Fixed an issue in the New UI where, after deleting the current default branch via the **Sync Branches** operation, the updated default branch was not immediately reflected in the UI. The system required a full page refresh for the new default branch to appear correctly.

The backend correctly promoted the next available branch as the default; however, the UI state was not refreshed automatically. The flow has been updated to call the repository details API after sync, ensuring the updated default branch is reflected instantly without requiring a manual refresh.

**Impacted Areas:**\
Sync Branches in VC Repositories

#### Time Zone Discrepancy in Default Date Range (New UI) <a href="#time-zone-discrepancy-in-default-date-range-new-ui" id="time-zone-discrepancy-in-default-date-range-new-ui"></a>

Fixed an issue in the New UI where the default calendar date range was calculated using the system time zone instead of the time zone configured in the user’s profile. This resulted in incorrect date ranges and missing recent entries across history-related screens.

The logic has been updated to apply the user-specific time zone when determining the default date range, aligning the New UI behavior with the Old UI.

**Impacted Areas:**\
Default date range handling in CI Jobs, Deployments, Dashboards, and Analytics

#### Repository Search Not Updating Branch Details Panel (New UI) <a href="#repository-search-not-updating-branch-details-panel" id="repository-search-not-updating-branch-details-panel"></a>

Fixed an issue where searching for a repository on the **Repositories** screen filtered the list correctly but did not update the right-hand **Branches** detail panel. The previously selected repository’s branch data remained visible, and the newly searched repository could not be selected to load its details.

The behavior has been corrected to reset the detail view after search and default to the first tab selection, ensuring that users can select a searched repository and immediately view the corresponding Branches data.

**Impacted Areas:**\
Search functionality in VC Repositories

#### Support Cases: <a href="#support-cases" id="support-cases"></a>

**Support Case: #186557**

#### Sandbox Mapping Failure in My Salesforce Orgs <a href="#sandbox-mapping-failure-in-my-salesforce-orgs" id="sandbox-mapping-failure-in-my-salesforce-orgs"></a>

Fixed an issue where mapping a specific sandbox under **Profile → My Salesforce Orgs** resulted in an error, even after re-registering the sandbox.

The issue was caused by a SOQL query length limit being exceeded (100,000 character limit) while retrieving Salesforce users for sandboxes with large user datasets.

The logic in `getSfUsers` has been enhanced to partition large SOQL queries into manageable chunks, ensuring successful user retrieval and sandbox mapping without errors.

**Impacted Areas:**\
Profile → My Salesforce Orgs (Sandbox User Mapping)\
Salesforce Integration – User Retrieval

**Support Case: #174294**

#### Reports with Subfolders Not Recognized in EZ Commit <a href="#reports-with-subfolders-not-recognized-in-ez-commit" id="reports-with-subfolders-not-recognized-in-ez-commit"></a>

Fixed an issue where Reports containing subfolders were not retrieved in **EZ Commit** when uploading a `package.xml`, although the same worked correctly in the Deployment module.

Enhanced metadata handling to correctly process members with subfolder paths ("/"), ensuring proper retrieval and commit of Report, Document, and EmailTemplate metadata in both DX and non-DX modes.

**Impacted Areas:** EZ Commit (Report, Document, EmailTemplate metadata – DX & Non-DX)

**Support Case: #186894**

#### Workflow Deletion – Destructive Merge Validation Failure <a href="#workflow-deletion-destructive-merge-validation-failure" id="workflow-deletion-destructive-merge-validation-failure"></a>

Fixed an issue where **Merge Validation** failed for revisions containing only destructive metadata (e.g., deleted Workflow components) when **Run Destructive = Enabled** and **Type = Post**.

Previously, the system generated the destructive XML only if at least one non-destructive component was present. As a result, revisions with only destructive members produced an empty `package.xml`, causing validation failure.

The logic has been updated to always process destructive components and generate the destructive XML package correctly, even when no non-destructive components are included.

**Impacted Areas:** EZ-Merge (Pre-Validation)

**Support Case: #189316**

#### Incorrect Storage Display in Super Admin Workspace Management <a href="#incorrect-storage-display-in-super-admin-workspace-management" id="incorrect-storage-display-in-super-admin-workspace-management"></a>

Fixed a UI issue where increasing workspace storage from the **Super Admin** account did not correctly update the displayed used and remaining storage values. The discrepancy was visible only in the Super Admin view, while registered user accounts displayed accurate values.

The calculation logic for available storage has been corrected in the Super Admin → Workspace Management UI to ensure accurate storage metrics are shown.

**Impacted Areas :** Super Admin → Workspace Management

**Support Case: #177966**

**CI Jobs – Parallel Processor Endpoint Handling**

Enhanced Parallel Processor configuration to support scenarios where the target API does not accept the default `/version/parallelexec` suffix appended at runtime.

A new internal flag (`AR_37880_PARALLEL_EXEC_ENDPOINT_IGNORE_LAST_SEGMENT`) allows trimming of the auto-appended version and `parallelexec` segments, enabling compatibility with custom API endpoint structures.

**Impacted Areas:** CI Jobs – Parallel Processor

***

## ARM Release Notes 26.1.6

**Release Date: 08 February 2026**

\
**Support Ticket: #186267**

**Reports – Code Coverage**

Fixed an issue where recent Salesforce Tooling API changes could result in inconsistent code coverage data, leading to failures during Code Coverage report generation.

The SOQL query used to retrieve coverage data has been updated, and additional validations have been added before processing the queried data to prevent unexpected errors and ensure reports run reliably.

**Impacted Areas:** Reports – Code Coverage

**Support Ticket: #187473**

**CI Job History**

Fixed an issue where changing the page size after applying a group filter could display CI jobs unrelated to the selected group.

The filtering logic has been improved to ensure group and other applied filters are retained correctly when the page size is changed, providing consistent and accurate CI job history results.

**Impacted Areas:** CI Job Results, CI Job History Page

***

## DataLoader Pro Release Notes 26.1.6

**Release Date:** **08 February 2026**

#### Improved Filtered Data Migration <a href="#dl-pro-improved-filtered-data-migration" id="dl-pro-improved-filtered-data-migration"></a>

Resolved an issue where data migrations could fail when filters were applied to master objects. The system now ensures that all required related records are included automatically, preventing migration failures due to missing references.

#### Selective Deployment – Improved Log Visibility <a href="#selective-deployment-improved-log-visibility" id="selective-deployment-improved-log-visibility"></a>

Fixed an issue where data retrieval logs were not visible during selective deployments. Logs are now displayed correctly and only when applicable, providing clearer visibility into deployment progress.

***

## ARM Release Notes 26.1.5

**Release Date: 01 February 2026**

**Refreshed UI** \
\
The refreshed ARM UI is now available to all customers on shared instances.

Customers on shared instances can access the refreshed UI immediately and switch between the existing UI and the refreshed UI at any time using the in-app toggle. Switching does not impact configuration, data, or any in-progress work.

For customers on dedicated instances, the refreshed UI can be enabled on request. Please contact AutoRABIT Support or your Customer Success Manager to schedule the upgrade.\
\
**Support Case: #182599**

**CI Job Not Updating Branch After Multiple Builds**

Fixed an issue where CI jobs continued to run successfully but stopped updating the target branch after multiple builds. The backend logic has been updated to correctly detect metadata changes and commit them to the branch, ensuring the repository stays in sync with the latest successful CI job execution.

This fix applies to CI jobs regardless of whether **“Check-out with user credentials and commit changes with the actual modified user credentials”** is enabled or disabled.

**Impacted Area:** Version Control → CI Jobs

**Support Case: #184383**

**Admin Visibility of DevHub-Enabled Salesforce Orgs**

Fixed an issue where Salesforce orgs registered with **DevHub enabled** were visible in **Admin → Salesforce Org Management** but not shown under **My Profile → My Salesforce Orgs** for other Admin users. Backend logic has been corrected to ensure that any org present in Salesforce Org Management is also visible in My Salesforce Orgs for **all Admin users**, regardless of DevHub configuration.

**Impacted Area:**\
Admin → Salesforce Org Management\
Profile → My Salesforce Orgs

***

## ARM Release Notes 26.1.4

**Release Date: 25 January 2026**\
\
**Refreshed UI – Phase 2 – Europe / Canada / Middle East Region**\
The refreshed ARM UI is now available to customers in the APAC region as part of a phased, region-based rollout. This update refreshes the UI layout only, with no changes to functionality or core workflows. Some UI elements have been repositioned to improve usability and consistency.

Customers can switch between the existing UI and the refreshed UI at any time using the provided toggle. No configuration, data, or in-progress work is lost when switching between experiences.

Availability will expand to additional regions in upcoming releases.\
\
**Support Case: 160127 :** Pagination added for Single Revision deployments\
The Single Revision deployment page could become unresponsive when handling a large number of revisions on a branch. Pagination has been introduced in the UI to efficiently manage large revision lists and prevent page freezes during deployments across CI Jobs and Deployments modules.\
\
**Support Case: 177903:** EZ-Merge reverse sync conflict resolution loop\
When performing a reverse sync using Entire Branch EZ-Merge with the conflict resolution strategy set to Source changes, AutoRABIT continued to prompt for manual conflict resolution and surfaced new conflicts repeatedly. This issue has been fixed to ensure conflicts are automatically resolved using source branch changes as expected, allowing the operation to complete successfully.\
\
**Support Case: 180026:** CI Job deployment fails with “no local changes to deploy”\
CI Jobs were unable to correctly determine whether a Matching Rule was installed or org-created because the NamespacePrefix was not being evaluated. The CI Jobs module has been updated to check NamespacePrefix and apply the same installed versus unmanaged filtering logic used in the Deployments module.\
\
**Support Case: 173748:** Branching Baseline status mismatch between UI and backend\
In Branching Baseline, the UI logs showed the process as completed while the backend status was failed, leading to confusing and unclear logs. This has been fixed to correctly surface backend failures in the UI and display clear error information.

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

## ARM Release Notes 26.1.3

**Release Date: 18 January 2026**

**Refreshed UI – APAC only**\
The refreshed ARM UI is now available to customers in the APAC region as part of a phased, region-based rollout. This update refreshes the UI layout only, with no changes to functionality or core workflows. Some UI elements have been repositioned to improve usability and consistency.

Customers can switch between the existing UI and the refreshed UI at any time using the provided toggle. No configuration, data, or in-progress work is lost when switching between experiences.

Availability will expand to additional regions in upcoming releases.\
\
\
**Support Case #178052 – Unable to View Compare Changes**\
Fixed an issue in **EZ-Commit** where users could not view **Compare Changes** on the review page during diff generation, resulting in an error.

A new backend API now clears any stuck _live status_ key from in-memory storage, preventing failures in the compare/diff flow.

**Impacted Area:** Version Control → EZ-Commit (Review → Compare Changes / Diff Generation)

**Support Case #175864 – Skip Org Mappings Missing During Role Creation**\
Fixed an issue where the **Skip Org Mappings** option was not visible during role creation or editing, even when it was expected to be configurable.

The visibility condition has been corrected to ensure the option is displayed appropriately based on configuration and not incorrectly hidden at the org level.

**Impacted Area:** Admin → Roles (Create / Edit Roles)

**Internal Case – Workspace Limit Error During Pre-validation Commit**\
Fixed an issue where **Pre-validation commits** in the ARM–SIT integration branch failed during the **Delta** step due to a workspace limit error.

Backend logic has been updated to avoid unnecessary workspace creation, allowing the pre-validation commit to complete successfully.

**Impacted Areas:**

* Version Control → EZ-Commits
* Version Control → Merges

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

***

## ARM Release Notes 26.1.2

**Release Date: 11 January 2026**

**Internal Case**\
An issue where adding a user to a team completed user creation but returned an API 404 error has been resolved. The user creation process now completes successfully without errors.

_Impacted Area:_\
Admin → Subscriptions → Team User Management

**Support Case: #173910**

Single Revision Merge now validates that the selected revision belongs to the chosen source branch. If a revision from a different branch is entered, the merge is blocked with a clear validation message.

_Impacted Area:_\
Version Control → EZ-Merge (Single Revision)

***

## ARM Release Notes 26.1.1

**Release Date: 4 January 2026**

**Support Case: #160652**

**Improved handling of Record Type picklist values in CI delta jobs:** CI jobs now more accurately process Record Type changes when delta is enabled. If picklist values are added or removed, only the actual differences are included in the build as expected. If a Record Type change does not involve picklist values (for example, updating only the description), the generated build file excludes picklist value tags. This prevents unintended dependency issues and ensures existing picklist values in the target org are not accidentally overwritten during deployment.

Impacted Areas: Commits, CI job and Deployments.

**Support Case: #173939**

**Improved commit stability during concurrent approvals:** Commits no longer fail when reviewers approve multiple commits at the same time. The commit processing logic has been updated to correctly handle queued commits, preventing unnecessary failures and eliminating the need for developers to recommit their changes when approvals occur concurrently.

Impacted Areas: Commits

**Support Case: #174471**

**Fixed deployment failures when using “Ignore missing visibility settings”:** Deployments using the _Ignore missing visibility settings_ option now work correctly for single-revision delta deployments. An issue where Profile metadata was not fully packaged—resulting in truncated files and deployment failures—has been resolved by improving the file copying mechanism used during deployment processing. This ensures Profile metadata is included correctly and deployments behave consistently with CI jobs.

Impacted Areas: Deployments

***



####

***

##

***

## **ARM Release Notes 22.1**

**Date of release:** _20 March 2022_\
**Article last updated:** _23 October 2022_

### New features <a href="#new-features" id="new-features"></a>

#### 1. Squash and merge <a href="#id-1-squash-and-merge" id="id-1-squash-and-merge"></a>

We have added the **Squash and Merge** feature in this release. Sometimes, when merging a long list of changes from a development branch into the master, it's helpful to squash those commits into one change for ease of review and declutter the repo's commit history. AutoRABIT offers an option to squash all commits in a merge request into one commit after the merge is approved and completed.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/squash%20and%20merge.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/ez-merge/squash-and-merge.md)

#### 2. SFDX- Import packages <a href="#id-2-sfdx-import-packages" id="id-2-sfdx-import-packages"></a>

**Packages**

The users could previously build a new package (unlocked or managed) and update the package's version in Salesforce DX. With this release, you may now import packages and update the version of packages created outside of AutoRABIT.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/import%20packages.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/import-an-unlocked-managed-package.md)

**Dev Hub management**

With this update, users will see all of the packages in their dev hub in the record view. You may expand each package to show the package's versions in order and package data such as version name, version number, ancestor version, ancestor dependencies, etc.

![Dev hub.gif](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/Dev%20hub.gif)

[**Read more →**](../../../product-guides/arm/registering-a-devhub.md)

#### 3. Step-based rollback <a href="#id-3-stepbased-rollback" id="id-3-stepbased-rollback"></a>

The option to list the API-supported and unsupported API components is added to the CI job/deployment rollback. If such components may be deployed to the target environment but do not have API support to delete them, ARM will display them individually as unsupported API types. Take, for example, **RecordType**.

The **RecordType** component may be deployed to the target environment, but it cannot be removed; instead, we need to connect to the target Salesforce environment to deactivate the component.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/step%20based%20rollback.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/automation-and-ci/ci-job-rollback.md)

***

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Checkmarx upgrade to v9.4.1 <a href="#id-1-checkmarx-upgrade-to-v941" id="id-1-checkmarx-upgrade-to-v941"></a>

Checkmarx has been updated to version **9.4.1**. Earlier, Checkmarx used a username/password-based authentication method. Now, the user will be able to use token-based authentication with the Checkmarx upgrade.

#### 2. Export all users <a href="#id-2-export-all-users" id="id-2-export-all-users"></a>

The **Export All Users** feature allows the org admins to export a CSV file of all the users currently in their account. We now have added the following fields to the existing CSV file:

* CreatedDate
* CreatedByName
* DeativatedDate
* LastLoginDate
* DeactivatedByName
* LastModifiedDate
*   LastModifiedByName.<br>

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/export%20all%20users.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-administration/user-management/users-roles-and-permissions.md)

#### 3. Pull request support for Azure cloud repositories <a href="#id-3-pull-request-support-for-azure-cloud-repositories" id="id-3-pull-request-support-for-azure-cloud-repositories"></a>

We have extended the support of having the pull request support in the CI Job for the Azure repository. This feature was previously available for Github cloud/Enterprise and Bitbucket cloud/Enterprise; however, we've added support for Azure cloud repositories (DX and non-DX repositories) with this release.

#### 4. Merge/commit approval eligibility <a href="#id-4-mergecommit-approval-eligibility" id="id-4-mergecommit-approval-eligibility"></a>

If you want to make sure one or more people approve every commit or merge, you can enforce this workflow by using merge/commit approvals. These approvals allow you to set the number of necessary approvals to approve every commit/ merge in a project.

The org admins' eligibility level has been enhanced with the ARM 22.1 version. If you're an administrator, you will have the privilege to approve self-merge even if the criteria to self-approve a merge is set to FALSE. This permission will be denied to all members of your team except the org admin. To put it another way, no criteria can restrict an org administrator from approving any EZ-commit/ EZ-Merge.<br>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/commit-merge%20approval.gif" alt=""><figcaption></figcaption></figure>

[**Read more →**](../../../product-guides/arm/arm-features/version-control/merge-approvals.md)

#### 5. CodeScan additional metadata support <a href="#id-5-codescan-additional-metadata-support" id="id-5-codescan-additional-metadata-support"></a>

We have enhanced the scope for analysis of what CodeScan does by adding support for additional metadata and rules. For our ARM users who want to incorporate the SCA tool into their subscriptions, CodeScan would be their first choice as it now supports more robust integrations.

Below is the list of CodeScan supported metadata types:

|                                   |                         |                         |
| --------------------------------- | ----------------------- | ----------------------- |
| Apex Triggers                     | Apex Classes            | Aura Definition Bundles |
| Lightning Component Bundles (LWC) | Visualforce Pages       | Custom Object           |
| Settings                          | Flows                   | Workflows               |
| Profiles                          | Sharing Rules           | Sharing Criteria Rules  |
| Sharing Owner Rules               | Sharing Territory Rules | Permission Sets         |

#### 6. SFDX CLI update <a href="#id-6-sfdx-cli-update" id="id-6-sfdx-cli-update"></a>

The SFDX CLI has been upgraded to the latest stable **7.134** version.

Key characteristics to look for:

* Single deployment request for constructive and destructive changes
* Quick deploy and rollbacks work for both constructive and destructive changes
* Package preparation has been improved.

***

### Improvements <a href="#improvements" id="improvements"></a>

* The jquery-UI version has been upgraded to **v1.13.0** to fix security issues. Upgrading to the most recent version of jquery makes our application more secure and potentially faster in script execution and loading.
* Minor performance, bug fixes, and security improvements can also be observed in the ARM portal.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 21 May 2023 <a href="#id-21-may-2023" id="id-21-may-2023"></a>

**(ARM v22.1.48)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where wrong **timezone** region was displaying for users ([#71553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111412006)).
* Fixed an issue where the **EZ-Commits report file** displayed the file count but not the components count ([#71538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111479094)).
* Fixed an issue where clone build jobs were taking between 10 and 25 minutes, which is much longer than expected ([#70227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000109182447)).
* Fixed an issue where CI job build failed to show changes in the org after deployment ([#70791](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110120443) and [#71956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111861212)).
* Fixed an issue where CI job to generate **Code Coverage Report** was not reflected in the org or in the e-mail notification ([#72042](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111983230)).
* Fixed an issue where merge status is displayed as completed but no revision is generated, and the merge is not available in the UAT branch ([#71266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000110960210)).
* Enhanced **DataLoader** by adding the ability to **field mapping** through the lookup fields ([#58480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095290579)).
* Fixed an issue with **DataLoader** where while running an **Extract** job on the **PUBLISHER** object, the job was failing with the following error `Publisher: column id is not supported in ORDER BY clause` ([#71303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111030174)).
* Enhanced the **nCino filter criteria** by adding the ability to search and filter labels using the whole or partial name ([#71826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000111666181)).
* Enhanced ARM by using known vulnerable components through the **DataTables 1.10.12** plugin for advanced data table functionalities such as sorting, filtering, pagination, and more. This allows users to easily display and manipulate large sets of data on their web pages in a user-friendly manner (internal ticket).
* Fixed an issue with **Prevalidation Merge** where users were unable to deploy the **ApexClass Tests** related to ApexClasses and Apex Triggers (internal ticket).
* Fixed a UI bug where the **date column** in the **EZ-Commit Weekly report** was displaying incorrect values (internal ticket).

#### 09 April 2023 <a href="#id-09-april-2023" id="id-09-april-2023"></a>

**(ARM v22.1.46)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **validation jobs** on **Pull Requests** weren't getting triggered ([#67538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106410313), [#67494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106382311), and [#67448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106353830)).
* Fixed an issue where Salesforce components were showing under the **Apex Test Success** tab in the **Deployment** module, which is not expected behavior ([#67537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253424)).
* Enhanced the **Branching Baseline** feature by allowing admin to define default baseline branches, making it easier for developers to choose the default branch for each project ([#63571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000102024066)).
* Fixed an issue where user was unable to register a branch even though **Test Connection** was successful ([#67023](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105968682)).
* Fixed an issue where ARM wasn't fetching the **ApexClass Tests** related to **ApexTriggers** upon selecting **Run Tests Based On Changes** option ([#67503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106378846)).
* Fixed an issue where **SCA Report** failed to run using **Codescan** plugin with the following Salesforce error: `An unexpected error occurred. Please include this ErrorId if you contact support: 384187622-16951 (-673032061)` ([#61676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099101151) and [#67675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604299)).
* Fixed an issue where triggered **CI jobs** were either failing due to an error **No Such File or Directory found**, or getting aborted automatically after some time and logs weren't printing at the back end ([#67549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106253579), [#66910](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106035058), [#67724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106597223), [#67720](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106570720), [#66881](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936162), and [#67667](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106604150)).
* Fixed an issue where triggered **CI jobs** were taking too long to build, and also slowing down ARM altogether ([#66846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105989569)).
* Fixed an issue where if the file name contained spaces, **Commit Validation** via **VS Code** plugin was unable to detect the file ([#63518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101868754)).
* Fixed an issue where **Search & Substitute** was not updating the value for a **custom label** in the SF org ([#66809](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000105936001)).
* Fixed an issue where there was a discrepancy between the changes captured in the ARM **Diff** and the repos in **BitBucket** ([#60596](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000097396243)).
* Fixed an issue where the SF org **URL** is not displaying the updated one under **Profile** ([#67718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106581101)).
* Fixed an issue with **nCino** where CI job filter changes on templates are not reflecting after saving ([#66956](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000106067470)).
* Fixed an issue with **Dataloader Pro** where user tried to migrate **Account Object Data** with **Attachments Object**, but the logs verify that there is a **Null Pointer Exception**. (internal ticket).
* Improved **nCino** by adding additional loggers for **Branching baseline** for user to view the status in the UI (internal ticket).
* Fixed an issue where user was unable to filter while trying to select a job which had spaces in the job name (internal ticket).

#### 25 December 2022 <a href="#id-25-december-2022" id="id-25-december-2022"></a>

**(ARM v22.1.38)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** jobs were failing due to incorrect files being copied from customer repository branch to Provar project directory ([#56662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091635358)).
* Fixed an issue where user triggered a **CI Job** but it deployed with many more components than expected ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where non-admin users were unable to select **Branch Type** while trying to create a **new branch** from **New EZ-Commit Branch** ([#57732](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000093556923)).
* Fixed an issue where **CI jobs** are failing intermittently with the following error: `Getting access token failed from refresh tokenHTTP/1.1 400 Bad Request` ([#57371](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880162)).
* Fixed an issue where user was trying to deploy only the **Documents** from the branch to Org, but deployment failed and **Asynch ID** is not generating ([#57263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092661381)).
* Fixed an issue where user was trying to deploy **login hours**. First they merged it to target branch, then once CI job triggers login hours are not getting deployed to target org ([#57359](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092880015)).
* Fixed multiple issues where user was having trouble creating **new package version** from **previous ancestor** version ([#55707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090251366)).
* Fixed an issue where **Merge** is **failing** with the following error: `failed to push some refs to 'https://github.com/salesforce-align/SFDX.git'` ([#55939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090999346)).
* Fixed an issue where the **Standard Field Account.name** is displayed in the deleted components list ([#57396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000092927781)).
* Fixed an issue where the **prevalidation commit** failed at **delta** stage ([#55763](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090435979)).
* Fixed an issue where user was unable to create **commit label** for the same repository second time, and branches were not displayed (internal ticket).

#### 11 December 2022 <a href="#id-11-december-2022" id="id-11-december-2022"></a>

**(ARM v22.1.37)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **SFI components** were not getting fetched in **Commit** and **Deployment** module ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue where multiple metadata types where not able to retrieve ([#56668](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000091694003)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where user performed a **merge** and sent it for **approval**, but it was not available under the **Commit history** tab ([#53759](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087839030)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was creating the **feature template** for some of the **nCino** objects but it was taking too long to **retrieve** the objects from **Source Org** ([#53915](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087934809)).
* Enhanced **nCino** to:
  * Modify **notification** messages for null checks on request parameters (internal ticket).
  * Display only **nCino** revisions for Version Control in nCino feature **deployment** (internal ticket).

#### 04 December 2022 <a href="#id-04-december-2022" id="id-04-december-2022"></a>

**(ARM v22.1.36)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Flexi pages** were not picked up in a **CI Job** even after the commit with same set of metadata was excluded by user ([#54518](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088461033)).
* Fixed an issue where **Abort** function to stop **Provar** jobs was not working as expected ([#55511](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090032787)).
* Fixed an issue where production backup **CI Job** was not picking all the changes, and when user modified the job configuration and retriggered the job, the application was throwing the following error `java.lang.NullPointerException: null` ([#55213](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089591408)).
* Fixed an issue where all **Slack Notifications** were selected by default and user was unable to unselect all at once ([#55817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090727146)).
* Fixed an issue where **SFI components** were not being fetched both in **Commit** and **Deployment** modules ([#55139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089491921)).
* Fixed an issue with **DataLoader Pro** where user selected a field as **External ID** in a job and saved it, but the saved entry was lost and user was unable to map it ([#55011](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089299148)).
* Fixed an issue where **Deployment validation** in **Prevalidation Commit** fails because profile validation automatically picks **User Permissions** even though **Remove User Permissions** option is selected ([#54941](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088985107)).
* Fixed an issue where user was performing a single **Merge** with only two approval process, but while selecting **SCA**, process is auto rejected ([#55671](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090263086)).
* Fixed an issue where **Commit Label** is not **Auto rejected** when the **validation criteria** is not met ([#55670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090311201)).
* Fixed an issue where **Release Label Merge** was failing and throwing the following error: `fatal: bad revision` ([#55000](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089278434)).
* Fixed an issue with **EZ-Commit** where user was unable to upload a **Custom YAML** file ([#55826](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090770005)).
* Fixed an issue where the **Vlocity Component** option under **Fetch Changes** is not populating for sub-users with roles that have all permissions and access ([#54962](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089032619)).
* Fixed an issue where **Commits** added from **non-nCino** **Repositories** were not cleared from the **Workspace** causing the Commit to either not be visible in the UI or it is added to the queue but not deployed to the **Destination Org** (internal ticket).
* Fixed an issue where user was performing a merge operation and validating the package on the **target org** but the validation was failing with multiple errors ([#55541](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090145025)).

#### 27 November 2022 <a href="#id-27-november-2022" id="id-27-november-2022"></a>

**(ARM v22.1.35)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was trying to migrate **Products**, **Pricebooks**, and its entries but the **Deploy** was failing for **Pricebook** and throwing the following error: `INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY: insufficient access rights on cross-reference id:--` ([#55263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089652641)).
* Fixed an issue with **nCino** where user was trying to create a custom feature template including **product objects** as well as **product line** but the deployment was failing with the following error: `Required fields are missing: [LLC_BI_Product_Line_c]` ([#51209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085641324)).
* Fixed an issue with **nCino** where **CI Job** was stuck in **Build Success** status ([#53605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087564091)).
* Fixed an issue where **CI Job** build was failing with a **NullPointerException** ([#55204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089616148)).
* Fixed an issue where the **Repository Branch** was unavailable to select to run the **Merge** process after selecting **On successful deployment** option ([#55537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090158003)).
* Fixed an issue where **Admin** was able to see the **Teams** field under **ALM Integration** but the same field was unavailable for sub-users ([#55153](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089465059)).
* Fixed an issue with **EZ-Commit** where user was trying to perform a **destructive commit** using **Autodraft** option, but was unable to select **deleted components** under the **Deleted** tab ([#55507](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089979335) and [#55651](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000090293003)).
* Fixed an issue where user was getting a **NullPointerException** when trying to resolve a **Merge conflict** ([#55137](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089410195)).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was able to create a **Delegated Group** but was unable to add a **Delegated Admin** user to the group using **Environment Provisioning** ([#55266](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089705014)).

#### 20 November 2022 <a href="#id-20-november-2022" id="id-20-november-2022"></a>

**(ARM v22.1.34)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing **Prevalidation Commit** but commits in the repository have different components than the ones shown in **Diff** before the commit ([#52307](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086491044)).
* Fixed an issue with **Install an Unlocked or Managed Package from a Version Control Branch** where CI job getting an exception and the build status was showing as successful but the **Scratch Org** was not being created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **CI Job** shows that the ALM status has been updated successfully but on **Azure ALM** it is not updated ([#54669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088657005)).
* Fixed an issue where **Test Automation CI Jobs** were failing due to **InitializeDriver** & **quit methods** ([#45878](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077372830)).
* Fixed a bug where user was able to access certain branches in the **Deployment** module to which he did not have access under **Profile Settings** ([#54879](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089011291)).
* Fixed an issue with **CI Jobs** where the build failed with **Checkout** conflict for an **.svg file** ([#54172](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088252005)).
* Fixed an issue with **nCino** where **Record Classification** and **Classification Objects** were missing in the template (internal ticket).
* Fixed an issue with **nCino** where user was creating a CI Job and observed that `Use UTF-8 file encoding for the file read and write operations` flag was displayed at the bottom below the **Commit Details** section (internal ticket).
* Fixed an issue with **nCino** where the **UTF-8 Encoding Flag** was not displayed in the pop-up during **Re-Deployments** (internal ticket).
* Fixed an issue where during an EZ-Commit, complete information about some of the members of WaveDataflow metadata type was not retreived from the Salesforce Org ([#49753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083936148)).
* Fixed an issue where **Quick Merge** was throwing the following error after clicking **Validate & Merge**: `Please Select Valid revision` ([#53932 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087946912)).
* Fixed an issue with **EZ-Commit** where **Autodraft** feature was taking too long and eventually failing when user was trying to retrieve components ([#48257](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082041269)).
* Fixed an issue where user was unable to add another branch to **Azure** in the **ALM MGMT Repository mappings** ([#55133](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000089433593)).
* Fixed an issue where the **Destructive** commit **Diff** was including more components than selected ([#54795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088780309)).
* Fixed an issue where a merge got stuck for a long time and the **Commit ID** was reflected in **BitBucket** but unavailable to select for release label deployment ([#52964](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087060140)).

#### 13 November 2022 <a href="#id-13-november-2022" id="id-13-november-2022"></a>

**(ARM v22.1.33)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was trying to create an **Extract** process in **DataLoader** but after validating the query the application was throwing an error: `not supported; requires @DynamoDBTyped or @DynamoDBTypeConverted` ([#54648](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088630160)).
* Fixed an issue with **CI Jobs** where **External Credential** metadata was not identified during **Deployment** ([#53939](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087955144)).
* Fixed a UI bug where user was performing an **org to org deployment** using **package.xml** file and the components were successfully deployed and also verified on Salesforce target, but the status on ARM was still **In-Progress** ([#50459 ](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375)and [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue with **DX CI Jobs** where user is not getting details of faulty commit revisions in the notification ([#54063](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088015242)).
* Fixed an issue with **Profile Manager** where the deployment is not showing any progress in the logger detail in front end. It was updated only after completion of the deployment job at backend ([#53706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704963)).
* Enhanced the **Conflict Resolution Log** by adding additional loggers like strategy chosen to resolve the conflict and which user did the resolution ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).
* Fixed a bug where **Merge Commit** validation was not considering special characters like %,#, etc. as a value and throwing the following error: `Merge comment should not contain an empty space` ([#54512](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088479003)).
* Fixed an issue where ARM was slowing at different phases in the **EZ-Commit** module ([#50503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084910726)).
* Fixed an issue where Git check response was not delivered for validation **CI Job** even though user has added the comment for a **Pull request** in the remote repository ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).

#### 06 November 2022 <a href="#id-06-november-2022" id="id-06-november-2022"></a>

**(ARM v22.1.32)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **DX CI Job** where user selected **Do Not Include Skip Members** but the respective mapper reports were not skipped (internal ticket).
* Fixed an issue where the **Deployment** module page was loading very slowly and then thrwing an error: `Page Unresponsive` ([#53675](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087704191)).
* Fixed the following issues in **CI** and **Reports** modules (internal ticket):
  * Build With **NULL ERROR** (issue exists both with Proxy and without Proxy)
  * SF Org Code coverage Execution is failing (issue exists both with Proxy and without Proxy)
  * Jenkins Build is updated with **FAILED** status even after it is successfully completed (issue exists only without Proxy)
  * Checkmarx text is not displaying the **Proxy Configuration** note (Only With Proxy)
* Fixed an issue with **QA Environments** where user was unable to create and delete the **SFDX module** because of the **Apache config CACHE** settings (internal ticket).
* Fixed an issue with the **Deployment** module where user initiated a **Deployment** without selecting the **Do not Include Skip Members** option, but this option was auto-enabled and skipped the member at the time of deployment ([#53747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087811296)).
* Fixed an issue with **Modularization** where user creating a module and selected the **Ignore installed components** check box but the installed components were not ignored causing the deployment to fail ([#53703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087755311)).
* Fixed an issue with **AccelQ Test Automation** where test case fails but the error details pop-up is not showing the details of the error that caused the failure ([#54224](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000088281589)).
* Fixed an issue where user is setting up the **Apex PMD rules** as **Priority 1** & **Priority 2** in the **CI Job** but the SCA Report is showing the **Priority 3, P4 & P5** which wasn't selected ([#54017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087969396)).
* Fixed an issue where the **Git** check response was not delivered for a validation **CI Job** ([#53036](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087171146)).
* Fixed an issue where the **Deleted Report** metadata components were not found in the **EZ-Commit** ([#53119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087247293)).
* Fixed an issue where user was trying to perform a **Quick Merge** but was getting an **Undefined** error for all labels (internal ticket).

#### 30 October 2022 <a href="#id-30-october-2022" id="id-30-october-2022"></a>

**(ARM v22.1.31)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where triggering a **CI Job** in **Objects** was resulting in an ambiguous error in the **CI Job Build** ([#53066](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087190013), [#52955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087099268), [#53631](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087579265)).
* Fixed an issue where all **CI Jobs** were failing and throwing the error: `Validation Checking failed Version Control Mappings not found for Repo: SA Repo and Branch: bugfix/Bugfix_PQT_Rel_Validation` ([#52945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087098136), [#52950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087101272), [#52757](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086925007)).
* Fixed a UI bug on the **CI Jobs** page for **Install an Unlocked or Managed Package from a Version Control Branch** type where old **Dev Hub**dropdown list was displayed in the **Deploy** section (internal ticket).
* Fixed an issue with **AccelQ** where running a test execution was successful even before the jobs were completed in AccelQ, but the status was always showing as **Not Run** instead of **Success** or **Failure** even if the jobs have been successfully completed ([#50181](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084509148)).
* Fixed a **Page Unresponsive** issue while creating a new **Release Label** by adding a feature to list limited results on each page ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where a merge got auto-approved and was in **Merged Not Commit** status ([#52398](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086586845), [#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed an issue where user created a **Release Label**, performed a **Merge** operation, committed changes to the target branch, and created two revisions in the **Github** branch.\
  But ARM was throwing an error while applying merge stage and only on the revision generated ([#51364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085859319)).
* Fixed an issue where **EZ-Commit** initiation was stuck with the error: `Unable to fetch Salesforce Org users. Reason: Invalid login: invalid user name or password or security token or api version or user locked out` ([#52550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086834002)).
* Fixed an issue where user was not able to select the orgs in the **EZ-Commit** drop down ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001), [#51219](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085620605)).
* Fixed an issue where **Page Size** value on the **Edit Release Label** screen is defaulting to the previous value instead of the set value (internal ticket).
* Fixed a UI bug where **OK Button** in **Automation** is not visible in the **Create Release Label** pop-up when opened in 100% zoom (internal ticket).

#### 23 October 2022 <a href="#id-23-october-2022" id="id-23-october-2022"></a>

**(ARM v22.1.30)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **CI Job** was successful but was including components from **GIT revisions** from old deleted branches ([#46983](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079512053)).
* Fixed an issue where user was performing a production deployment using CI job for an object, but it failed with the following error: `Cannot set sharingModel to ControlledByParent on a CustomObject without a MasterDetail relationship field` ([#48626](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082749181)).
* Fixed an issue where **CI Job** was getting an exception, **Build** status was showing as _successful_, but **Scratch Org** not getting created ([#50702](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085126029)).
* Fixed an issue where **Managed Package** was picking the wrong ancestor by adding a feature to manually select the preferred ancestor while creating a package version ([#48311](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223305)).
* Fixed an issue where user was adding **URLs** to the **Proxy Configuration Settings** but the **URL List** was not reflecting the same (internal ticket).
* Fixed an issue where **Custom Template Creation** failed and the **Logs** did not record the reason for failure ([#52147](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086277150)).
* Fixed an issue where the **Created By** value was not visible in **Dataloader**, **Dataloader Pro DL Config**, and the **TestEnv History** page (internal ticket).
* Fixed an issue where the **Comment Box** was not accepting more than **100 characters** while rejecting a **Commit**, but was working as expected while approving a commit ([#51384](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085891476)).
* Fixed an issue with **Apex Test Class Config.** in **SF MGMT ORG** where the **Fetch Current Set**, **Add Manually**, and **Auto Populate** options were throwing an error: `Error 200` ([#52408](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086578687), [#52328](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086485900)).
* Fixed an issue where user set **Commit validation Criteria** to **Auto reject after 7 days** but the older Pre-validation commits are not auto rejected after 7 days ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user cannot add **Skip** members manually and it is failing due to **special characters** being included ([#53139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087266642)).

#### 16 October 2022 <a href="#id-16-october-2022" id="id-16-october-2022"></a>

**(ARM v22.1.29)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where skipped members were present in many components but only **Report Metadata** was failing during **Deployment** ([#51040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085433814)).
* Fixed an issue where **CI Job** was getting stuck in **In Progress** status but the log showed that the deployment was successful ([#51140](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085583019)).
* Fixed an issue where GitHub login credentials were not working when user triggered a CI Job for the second time ([#50630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085136003)).
* Fixed an issue where CI Job has failed in the Salesforce org, but still stuck in **In Progress** status in ARM ([#50435](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084823763)).
* Fixed an issue where user raised a **Pull request** on a branch and was getting a webhook response, but CI Job build was not triggered ([#51592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085996953)).
* Fixed a UI bug where **Add to dashboard** button was unavailable for widgets ([#52333](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086514169)).
* Fixed an issue where a new database file is created and overwritten with an existing database file whenever the server was restarted (internal ticket).
* Fixed an issue where user was trying to resolve conflicts on **Merge Request Labels** created more than 7 days ago, but application was throwing an error: `undefined` (internal ticket).
* Fixed an issue where **Custom Email Template** was not working for **Email notifications** ([#47484](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080506162)).
* Fixed an issue where user was testing **SSH Connection** but the application was throwing an error: `invalid privateKey` ([#50940](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371198)).
* Fixed an issue with **nCino** where **UI Log** was not generated for failed CI Jobs ([#50442](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084795478)).
* Fixed an issue where **New EZ-Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue where **Audit Logs** were not generating via **Postman Services** ([#50221](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084545179)).
* Fixed an issue where **Commits** were getting stuck and throwing the following error: `No credential have been found with Name:git`, but was not reflecting in the UI log ([#51713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000086127001)).
* Fixed an issue with **Workspace Settings** where unused workspaces were not being cleared despite selecting **Clear all workspaces which are not used in last 7 days** ([#50164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084481079)).
* Fixed an issue where user was performing a **Prevalidation EZ-Commit** and found that some **Layout Assignments** were deleted though those layouts were not part of the commit ([#50945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085371456)).
* Fixed an issue with **nCino** where migration was failing due to errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).

#### 09 October 2022 <a href="#id-09-october-2022" id="id-09-october-2022"></a>

**(ARM v22.1.28)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with **nCino** where user was getting errors with **Standard Screen** and **UI Templates** ([#50432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084739297)).
* Fixed an issue where user noticed discrepancy in the **Conflict Resolution Log** ([#47559](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080771349)).

#### 02 October 2022 <a href="#id-02-october-2022" id="id-02-october-2022"></a>

**(ARM v22.1.27)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where components were successfully deployed, but deployment status was still showing **In-Progress** in ARM ([#50459](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084807375), [#51288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085799424)).
* Fixed an issue where CI Jobs were getting stuck and throwing the following error: `Too many open files` ([#44319](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001), [#49273](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074784001)).
* Fixed an issue where **email notification** wasn't sent for some of the **CI Jobs** ([#48028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081639899)).
* Fixed an issue where the Custom label and remote site setting URLs were not getting updated by ARM through **Environmental Provisioning** ([#49612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083684001)).
* Fixed an issue with **Vlocity** where selecting one component from a GIT repository was causing all the components from the category to get selected ([#49806](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084007005)).
* Fixed an issue with **ALM Mgmt.** where item status was not retrieved properly for **Merge Request**, but was working as expected for **EZ-Merge** ([#50628](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085133005)).
* Fixed a UI bug where **Release Labels** were showing duplicate **Time Stamps** ([#51205](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000085689003)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected after 7 days as the user had configured under **Commit Validation Criteria** ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).
* Fixed an issue where user was getting an error pop-up on the **Permissions** and the **SF ORG MGMNT** pages, and the SF org and VC repo mappings were lost in the profile section of a role ([#49108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083164265)).

#### 26 September 2022 <a href="#id-26-september-2022" id="id-26-september-2022"></a>

**(ARM v22.1.26)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Provar** test job was throwing an error while in queue ([#49797](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083986945)).
* Fixed an issue where scheduled auto-sync of external commits was not working (internal ticket).
* Fixed an issue with the **New EZ-Commit** screen where **ALM Types** are changing to old ALM type names after resaving details on the **ALM Management** screen (internal ticket).
* Fixed an issue with **Pre-validation merge** where the **Object** file content was empty in the **CodeScan Analysis SCA** report (internal ticket).
* Fixed an issue with **Branching Baseline** where some of the custom object metadata nodes were deleted from the repository ([#47239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080102001), [#47270](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080113166)).
* Fixed an issue with **EZ-Merge** where **Diff** was not being generated even though there were file changes between the source branch and the destination branch ([#50323](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084689471)).
* Fixed a UI bug in **DataLoader** where user was switching from **Graphical View** to **Grid View** but **Graphical View** options were still being displayed ([#50431](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084822478)).
* Fixed an issue with **nCino** where the **Insert/Update With Null Values** option was not getting updated for CI jobs ([#50259](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084641005)).
* Fixed an issue where users were unable to **re-authenticate** the **Salesforce Org** after refreshing their personal sandboxes ([#48533](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082553001)).
* Fixed an issue where **Environment Provisioning Template** was not functioning as expected for **Custom Labels** containing URL ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue with **EZ-Commit** where user was trying to deploy **Permission Sets** and **Profiles** together, and the pre-validation process was stuck in **In-Progress** status ([#49340](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083456001)).
* Fixed an issue where old **Commit Labels** were not getting auto-rejected as configured ([#49874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084033082)).

#### 19 September 2022 <a href="#id-19-september-2022" id="id-19-september-2022"></a>

**(ARM v22.1.25)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed multiple issues with **CodeScan<>ARM** Integration (internal ticket).
* Fixed an issue where **CI Jobs** and **Deployments** were both failing for **Reports** and **Dashboards** because the folder could not be found (internal ticket).
* Fixed an issue with **New Commit** screen where the **Select All** checkbox was getting unselected when navigating from the **DELETED** tab to the **ADDED/MODIFIED METADATA COMPONENTS** tab and back to the **DELETED** tab (internal ticket).
* Fixed an issue with **Version Control Prevalidation Commit** where for the selected **Custom Metadata** and **Permission Set**, **Diff** was being generated as expected but the **Deployment** was failing (internal ticket).
* Fixed an issue with **Version Control Prevalidation Merge** where SCA report was empty, and throwing the following error in the console: `Uncaught TypeError: Cannot read properties of undefined (reading 'length')` (internal ticket).
* Fixed an issue where user was unable to reset the AutoRABIT password, and was getting an error: `getAttribute: Session already invalidated` ([#50145](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084391472)).
* Fixed an issue where **CI Jobs** was not picking the right number of components unless the user cancelled the build and retriggered it ([#47164](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921675)),([#46981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079504156)).
* Fixed an issue where the user tried to merge to the Dev branch but the **CI Job** failed and was throwing a **Duplicate** error ([#49661](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083729177)).
* Fixed an issue where user was trying to install **Unlocked Package** via **CI Job** but it was failing and throwing the following error: `ERROR 178928269770891:275 - For input string: "0-2" java.lang.NumberFormatException: For input string: "0-2"` ([#50093](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000084341003)).
* Enhanced **Vlocity** loggers for **Branching Baseline** by displaying to the user **Status Count** of **Remaining**, **Success**, **Error** and **Ignored** (internal ticket).
* Fixed an issue where **Test Connection** was failing on the **Version Control Summary** page under the **Admin** module ([#49299](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083372346)).
* Fixed an issue with **Prevalidation Merge** by increasing the **SCA Response timeout** from **50 minutes** to **5 hours** ([#48613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082720068)).
* Fixed an issue where merging **Master Branch** with the **Production** branch was throwing the following error: `No merge head specified` ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed a bug where **New A-Z Merge** was throwing an error ([#46754](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079012711)).
* Fixed an issue with **Autorabit Commit Label** related to **Permission Sets Deployment** ([#48709](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082892203)).

#### 11 September 2022 <a href="#id-11-september-2022" id="id-11-september-2022"></a>

**(ARM v22.1.24)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was selecting a single package to import, but all available package versions were being imported ([#49426](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083542359)).
* Fixed an issue with **Profile Manager** where user was comparing a profile but the deployment was not starting ([#48620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082696017)).
* Fixed an issue where deploying components with profiles was not working as expected and throws the following error: `Duplicate layoutAssignment:PersonAccount (PersonAccount.Person_Prospect)` ([#49021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083082001)).
* Fixed an issue where custom metadata records were not being selected during deployment ([#49167](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083203846)).
* Fixed an issue in **Version Control Commit Labels** history where **Created By** and **Created Date** values were exchanged (internal ticket).
* Fixed an issue where user was getting an error while trying to deploy **Vlocity Metadata** using **CI Jobs** ([#47568](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080830005)).
* Fixed an issue where **Branching Baseline** was not retrieving **Workflow Metadata types** ([#49403](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083447017)).
* Fixed an issue where **Release Label** failed to load revisions from a particular branch and the browser was hanging and throwing an _Out of memory_ error ([#48563](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082627224)).
* Fixed an issue where **EZ-Commit** was not getting auto-rejected when **CodeScan** analysis failed, even though user select the option to run **Static Code Analysis** ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).
* Fixed an issue where merge was failing at the **Validate Deploy** step even before selecting the org to validate ([#49724](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083898393)).
* Fixed an issue where **Layout** was being removed from the **Diff** while deploying **Profile** changes with related **Layouts** and **RecordTypes** ([#48268](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082045983)).
* Fixed multiple issues with **CodeScan<>ARM** Integration ([#49605](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083671017)).

#### 04 September 2022 <a href="#id-04-september-2022" id="id-04-september-2022"></a>

**(ARM v22.1.23)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where user was performing a new deployment but getting an error when using the **Compare Orgs & Deploy** button ([#48707](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860460), [#48676](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860003), [#48737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082918005), [#48734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082914003)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.NullPointerException: null` ([#48706](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082860315)).
* Fixed an issue where few fields were not being analyzed in CodeScan SFDX. User was selecting Custom Fields, Apex Classes, and Record Types in E-Z Commit, but Static Code Analysis was only Apex Classes ([#48547](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082584398)).
* Fixed an issue where dashboards and reports were changing to **Destructive** and getting deleted ([#48119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081915009)).
* Fixed an issue where discrepancies for **Document**, **Assignment Rule** and **AutoResponseRule** metadata types content was observed in **package.xml** for SFDX and non-SFDX CI Jobs ([#47017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079534439)).
* Fixed an issue where the Dataloader Pro Jobsfailing and throws the following error: `java.lang.NullPointerException: null` ([#49170](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182317), [#49283](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083331025), [#49331](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083407003), [#49199](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000083182597)).
* Fixed an issue where nCino CI Jobs via RBC were failing during parallel deployment. Instead of falling in queue, the first job was failing while the other succeeded, and the user had to retrigger the failed job ([#47335](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080272507)).
* Fixed an issue where creating multiple deployment jobs from the same source org to the same destination org for different templates, the jobs were failing with **Null Pointer Exception** error (internal ticket).
* Fixed an issue with **DX Pre-validation merge** where **Destructive Deployment** for custom labels failed without any errors (internal ticket).

#### 28 August 2022 <a href="#id-28-august-2022" id="id-28-august-2022"></a>

**(ARM v22.1.22)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where **Unpackaged Packages Directory** folder was being created in the **Deployment Promotion** zip package when deploying **Static Resource Metadata type** using **Single revision DX Deployment** (internal ticket).
* Fixed an issue where after upgrading the AR instance, deployment jobs kept removing the custom metadata access on the **Permission Sets** ([#48296](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082147005)).
* Fixed an issue where **Org difference** jobs were running for more than 24 hours ([#48324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082223730)).
* Fixed an issue where Environment provisioning template was not working when trying to update custom label values that contain URL, and the incorrect value was being updated in the org ([#47892](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081421793)).
* Fixed an issue where choosing the **Select Manually** option while doing a commit was resulting in a blank screen for the **Deleted** tab (internal ticket).
* Fixed an issue where while doing Prevalidation commit in AR, **Commit Only Permissionsets For The Selected Metadata** functionality was not working properly for both DX and Non-DX cases (internal ticket).
* Fixed an issue in Dataloader where an **Undefined Error** was displayed when user was trying to create and save the **Screens Template** (internal ticket).
* Fixed an issue where user was trying to validate the commit using single revision, but was getting an **Empty Package** error even though there were changed files in the commit ([#47530](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080730150)).
* Fixed an issue where DataLoader Pro jobs were failing with an error **duplicate value found: SetupOwnerId duplicates value on record with id** for the custom setting **Multichannel\_Settings\_vod\_\_c**, even though there is no field mapped with name **SetupOwnerId** ([#48230](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081981779)).
* Fixed an issue where the **search** functionality was not working in Dataloader Configuration as well as Dataloader Test Environment Setup (internal ticket).
* Fixed an issue where EZ Commit Logs and Change Labels were not displaying for some of the commit labels ([#45364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076464250)).
* Fixed an issue where the user was not able to see the deployment report because the build was failing when only custom fields were being selected without the related object ([#45663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077048275)).
* Fixed an issue where merge request was being auto rejected if the selected approver was no longer with AR ([#48084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081784401)).
* Fixed a bug where user had enabled Squash and Merge while performing a new merge, but the Squash and Merge option was not displayed after the Merge Request was approved ([#48246](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082046388)).
* Fixed an issue in CI Jobs deployments where Bulk API option for **Attachments** was throwing an error (internal ticket).
* Fixed an issue where **nCino CI Jobs** were failing the first time and completing the second time successfully ([#46545](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644141)).

#### 21 August 2022 <a href="#id-21-august-2022" id="id-21-august-2022"></a>

**(ARM v22.1.21)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI job build was getting stuck in **In-progress** status ([#47934](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081483565)).
* Fixed an issue where **RunSpecifiedTest** level execution was failing with Test classes dependency errors ([#47666](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081029378)).
* Fixed an issue where DX CI Job build failed if document metaxml change commit revision includes in the build \[Including Email templates and Static Resources types] (internal ticket).
* Fixed an issue where entire branch merge was failing with multiple common ancestor errors ([#47334](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080237436)).
* Enhanced the Dataloader history screen (internal ticket):
  * Column mover added to table column alignment for text view.
  * Moved **Last Run** details to the **Date/Time** column.
* Fixed an issue where Standard fields are not retreiving when included in **package.xml**, and retrieving through **E-Z Commit (Package Manifest)** option ([#47961](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081505333)).
* Fixed an issue for the **nCino CI Jobs** were failing due to default selection of **AutorabitExtId\_\_c** in **Mappings** (internal ticket).
* Fixed an issue for the nCino Deployments where even if **LookupKey** is available, by default **Name** is selected in **External ID Mapping** (internal ticket).
* Fixed an issue for the nCino CI Jobs where **Attachments** were failing due to **External Mappings** not being set to the **NAME** field (internal ticket).
* Added the feature to dynamically handle the respective nCino Prefix rather than depending on the JSON file to identify the External Id field

#### 14 August 2022 <a href="#id-14-august-2022" id="id-14-august-2022"></a>

**(ARM v22.1.20)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushed with special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).

#### 07 August 2022 <a href="#id-07-august-2022" id="id-07-august-2022"></a>

**(ARM v22.1.19)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the package URL was not visible for the SFDX modules successfully configured in ARM (internal ticket).
* Fixed an issue where our internal team members got the undefined error while creating a new scratch org and selecting the module (internal ticket).
* Fixed an issue where after triggering the CI job, the **File Changes** and **Check-ins** results mismatched ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue where the package created to deploy ExperienceBundle misses some of the folder and metadata files contained in it ([#46692](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079024001)).
* Fixed the below deployment-related issues:
  * Unable to find commits that are part of a Release Label while performing a new deployment ([#47337](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080246444))
  * Unable to retrieve components from a Release Label during deployment ([#47534](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080713440))
  * Changes are not deployed to the destination org which are part of a Release Label ([#46908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079358877))
* Fixed an issue where the users while deploying a destructive XML file from one sandbox to another, is getting auto rejected ([#47714](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081149440), [#47747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081187577)).
* Fixed an issue where the deployment failed to initiate when search and substitute rules are selected ([#47802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000081320007)).
* Fixed an issue where the status log .csv files are inconsistent for deployment via CI jobs (internal ticket).
* Fixed an issue where the users were unable to process the migration of RBC object (nForce\_\_Views\_\_c) using the nCino CI jobs, feature template migration, or the Dataloader Pro jobs ([#47098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079761055)).
* Fixed an issue where while deploying a **nCino-User Interface** template, only partial records are deployed and no deployment logs are generated ([#47494](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080488668)).
* Fixed an issue where the users, while performing an EZ-Commit by enabling the run SCA option, the CodeScan analysis is getting failed, but EZ-Commit is not getting auto-rejected ([#47155](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079921059)).

#### 31 July 2022 <a href="#id-31-july-2022" id="id-31-july-2022"></a>

**(ARM v22.1.18)**\
This is a maintenance release. The following items were fixed and/or added:

* Upgraded the Spring and AWS libraries on ARM for addressing the Spring vulnerability ([#46970](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079471289)).
* Fixed an issue where the users were unable to login to ARM via SSO (internal ticket).
* Fixed an issue where the ARM is not able to fetch any component using the release label ([#46662](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078894834)).
* Fixed an issue where the baselining of branches has wiped out the records types for many records, and the users were forced to do manual changes to the Record types ([#42719](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072309163)).
* Fixed an issue where the ARM allows to associate only one branch to one package, and not able to build beta package versions from various branches. This is now fixed ([#46841](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262193)).
* Fixed an issue where the CI job, while deploying manage packages, is installing all the manage packages instead of installing a single package ([#46832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262054)).
* Fixed an issue where the links on the **CI Job log** screen are redirected to the user's login page instead of redirecting to user's Salesforce org screen ([#47151](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079912283)).
* Salesforce API version 55 (Beta support) is upgraded. The label is modified throughout ARM application to Salesforce API version 55.0 ([#47404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080386152)).
* Duplicate classes from the ARM repo has been removed (internal ticket).
* Fixed an issue with the **Profile Manager** where the user were unable to select the default app permission during the profile deployment ([#47462](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080494273)).
* Fixed an issue where the merge revisions were missing from the CI jobs ([#46862](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079287922)).
* Fixed an issue where the users were unable to commit **Vlocity card** from one org to another org in ARM ([#44938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075743019)).
* Fixed an issue where for both CI Jobs and Deloyments (Non-DX and DX), the deployment was getting failed with the below error although the **Ignore missing visibility settings** is checked: `permissionset error--- Error in field: customPermission not found` (internal ticket).
* Fixed an UI bug where while performing test connection for any successful Salesforce org registered, the messasge is displayed as **"Success"** instead of **"Testconnection was successful"** (internal ticket).
* Fixed an issue where the ALM integration was not working when the files are pushedwith special characters in their name ([#47414](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080454001)).
* Fixed an issue where the commit labels was getting auto-rejected while committing Profile FLS ([#46844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079276142)).
* Fixed an issue where the merge was getting failed with the following error: `Fetch operation is failed due to some runtime exceptions from Git` ([#46773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079094055)).
* Fixed an issue where the username and passwords fields were not editable for users registered in ARM with basic authentication ([#47099](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079788018)).

#### 24 July 2022 <a href="#id-24-july-2022" id="id-24-july-2022"></a>

**(ARM v22.1.17)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when user triggers a code coverage run in the production environment, the action takes more time than expected. Also, the total time taken for the task completion is shown inaccurate in the log report ([#44544](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040590), [#43527](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073512143)).
* Fixed an issue where the CI job was not working as expected and throws the following error: `java.lang.OutOfMemoryError: Java heap space` ([#47182](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988001), [#47190](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079988142), [#47209](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000080017264), [#47191](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079950166)).
* Fixed an issue where the **Rollback settings** were not getting saved in the **My Account** page (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue with the permissionsets where instead of delta changes, the Permissionset retrieving entire file from the branch and causing dependency issues ([#46846](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079262334)).
* Fixed an UI bug where the ARM application displays unwanted scrollbar when **"Exclude Installed (Managed) components"** is selected in the **My Account** page (internal ticket).
* Enhanced the ARM workspace feature to automatically unlock the workspace after sufficient time to run the workspace operations.
* Added the feature to set **Limit 0** option for the Dataloader Pro jobs. This limit will allow users to skip migrating child or Ancestors objects.
* Fixed an issue where while editing an existing nCino CI Job, the version control is not automatically choosing the previous repository set. This is causing the selected nCino Templates to reset ([#46952](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079432380)).
* Fixed an issue where the ALM labels were missing from the ALM Label lists page ([#44410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074860453)).
* Fixed an issue where the settings related with user permissions were erased ([#46472](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078507457)).
* Fixed an issue where the users when performed EZ-Commit using a package manifest file, doesn't include managed components that are in the **package.xml** file ([#47083](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079769291)).

#### 17 July 2022 <a href="#id-17-july-2022" id="id-17-july-2022"></a>

**(ARM v22.1.16)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the Execute Anonymous Apex metadata is not working as expected when configured as Environment Provisioning template ([#46817](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079248146)).
* Fixed a bug where our internal team were able to use the perform the prevalidation commit and direct commit without giving the prevalidation commit label name and without commit comment, which are mandatory fields (internal ticket).
* Fixed an issue where the ALM workitems are not retrieved in CI job through merge (internal ticket).
* Fixed a bug where our internal team were able to save the **Install an Unlocked or Managed Package from a Version Control Branch** CI job even though Installation key were not uploaded which is a mandatory field (internal ticket).
* **\[Enhancement]** Added the Salesforce versions information in the logs for all Dataloader related jobs activities.
* **\[Enhancement]** Added the ability to delete a commit before it is pushed to your remote repository so that you have a choice to redo incorrect commits/ merges.
* Fixed an issue where the merge prevalidations were auto rejected with status as **Approval Pending** ([#46665](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078888152), [#46864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079289063)).
* Fixed an issue where the **Delete Commit** button was not seen after approving an EZ-Commit label (internal ticket).
* Fixed an issue where the toggle button for the dashboard metadata type in the commit label screen is not working as expected (internal ticket).
* Fixed an issue for the nCino Feature Deployments where the users were getting audit field issue when trying to deploy with `Insert/Update with Null Values` option (internal ticket).
* Fixed an issue for the nCino CI jobs using Spreads Templates where the users were getting `NullPointerException` error when trying to deploy with `Insert/Update with Null Values` option (internal ticket).

#### 10 July 2022 <a href="#id-10-july-2022" id="id-10-july-2022"></a>

**(ARM v22.1.15)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users failed to enable the pull request support for their version control repositories ([#46336](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078290172)).
* Fixed an issue where the re-use previously validated commit label takes more time to load ([#46171](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077992017)).
* Fixed an issue where the constructive changes are picked in the CI build, although no constructive changes are in-between _From_ and _To_ revisions (internal ticket).
* Fixed a bug marked deployment as failed, whereas the log report says successful ([#46737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079038631)).
* Fixed an issue with the SFDX job, where for the Report metadata type, the rollback feature was working weirdly (internal ticket).
* Fixed a bug where the users could not edit/modify their CI jobs when the build was in progress ([#43538](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073573003)).
* Fixed an issue where entering the package installation key in `Install an Unlocked or Managed Package from Version Control Branch` CI Job gets altered when manually entered or pasted ([#46836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079265163)).
* Fixed an issue where the user could not run the static code scan report on GitHub with APEX PMD Lint Scanner metadata type ([#46781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000079122007)).
* Fixed an issue with the CodeScan analysis report that failed when running from ARM ([#44404](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074862389)).
* Fixed an issue where the user could not fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Enhanced the Dataloader Pro, where the attachments are now supported ([#41077](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299001)).
* Fixed a bug where editing the Dataloader job shows **"Job Group"** as _null_ or _empty_ (internal ticket).
* Vlocity has been upgraded to v1.15.5.
* Fixed an issue with the CI job where the version control using Salesforce with attachments was not picking the attachments during CI build (internal ticket).
* Fixed an issue with the EZ-Merge, where merging the main branch to the dev branch failed with a `No merge head specified` error ([#46594](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078825001)).
* Fixed an issue that throws `Schema as invalid` error while running the branching baseline operation ([#46593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078805109)).
* Fixed an issue where the merge failed using a single revision ([#46491](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078644005), [#45764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077211038)).
* Fixed an issue where our internal team members could not create a new role from the **Admin** section (internal ticket).
* Fixed a bug where the `Invalid Schema` error is seen for non-SFDX prevalidation merge (internal ticket).
* Fixed an EZ-Commit issue where additional permissions were removed from Profiles metadata type, which is not a part of the commit ([#44543](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075040441)).

#### 03 July 2022 <a href="#id-03-july-2022" id="id-03-july-2022"></a>

**(ARM v22.1.14)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the deployment via CI job picked unnecessary components for deletion ([#44204](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074533873)).
* Fixed the issue where the user when trying to delete a component in **Community** metadata type, deletes the whole Community rather than its components ([#43698](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073869007)).
* Fixed an issue where DevHub registration in ARM was failing ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed a bug where our internal team members were not able to view the Salesforce Org URLs in the **My Profile** section (internal ticket).
* Fixed an issue where the deployment using **Commit/Release Label** was not working ([#46419](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078496053)).
* Fixed an issue where the mapping more than one class to same test class is not recognized by ARM during commit/merge operation ([#46396](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078430859), [#45159](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076223139)).
* Fixed an issue where the CI job builds were failing because of missing revisions ([#45532](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076855001), [#46352](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078378003)).
* Fixed an issue where the **Compact Layout** were not getting deployed and throws undefined error([#46592](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078798022)).
* Fixed an issue where the ALM statuses were not updated/rolled back post CI job rollback completion ([#45945](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077581145)).
* Fixed an issue where the destructive changes were not working as expected for the CI jobs ([#46216](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049311)).
* Fixed an issue where the ARM failed to update the Audit fields when trying to run nCino feature deployment ([#46356](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078401001)).
* Fixed an issue where our internal team were not able to register their credentials on one of the ARM SAAS instances ([#46315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078239277)).
* Fixed an issue where prevalidation commits were getting failed due to credential issues. The following error was thrown `No credentials found` ([#46274](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078213003), [#46098](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077754153)).
* Fixed a bug where the deleted components were tagged as **UC (UnChanged)** instead of **D (Deleted)** in the EZ-Commit ([#46087](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077760173)).
* Fixed an issue where the metaXML file were not retrieved for the ContentAsset metadata type for the **SFDX "Entire Branch"** merge case (internal ticket).
* Fixed an issue where the deployment validation were failing for the prevaildation merge with the error: `No source backed components present in the package` (internal ticket).
* Fixed an issue where the merge using single revision (baseline revision) receives the metadata schema error ([#46570](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078699087)).
* Fixed an issue where the merges were getting failed and throws the `Schema is invalid for the file` error ([#45768](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077202614)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).

#### 26 June 2022 <a href="#id-26-june-2022" id="id-26-june-2022"></a>

**(ARM v22.1.13)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Spread Template** in the **nCino** module was not working as expected ([#45078](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076003188)).
* Fixed an issue where the user was getting `"field integrity exception: unknown (CreatedByID(0051X00000BbMIR) is not in org"` for the records that were available in the destination org.
* Fixed the issue where the **Disable Workflow** template in the **Environment Provisioning** module was not working as expected ([#46195](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078049157)).
* Fixed an issue where the creation of a scratch org were getting failed. The fix has been deployed to in this weekly release ([#46021](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690007)).
* Fixed an issue where the users were unable to use the **release label** for deployment ([#45415](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076584626)).
* Fixed an issue where the users were not able to register same DevHub with two different usernames ([#46208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078056108)).
* Fixed an issue where the CI Job was picking the deleted components from GitHub branch although the **Prepare Destructive Changes** checkbox was not selected. This caused the deployment to fail ([#42553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the users were not able to view their GitHub branches in the ARM application ([#46044](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077690473), [#46353](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078386013)).
* Fixed an issue where the CI Job for backing up from org to the version control branch was failing with null pointer exception error ([#45646](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072012015)).
* Fixed an issue where the **EZ-Commits**, when included **Profile**, was not working as expected ([#45902](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077441170)).
* Fixed an issue where the commits were getting stuck at the delta stage ([#45101](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076070023)).
* Fixed an issue where the Git tags were being added to the queue but not being processed (internal ticket).
* Fixed an isse where the delta was getting failed in the **EZ-Commit** flow (internal ticket).
* Fixed an issue where the Dalaloader Pro job is failing with `Required field missing on "nCino_Screen__c" object`, however the user were able to view the `Screen__c` object has a value in their source org ([#45139](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076158018)).
* Fixed an issue where the user were not able to save the Dataloader Pro jobs and throws the `JAVA.NullPointerException` error ([#46385](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078393786)).
* Fixed a bug where the users were not able to view the log reports after registering **Tags** via ARM (internal ticket).
* Fixed an issue where the tags creation got failed when the tag name contains **'error'** with custom API flow (internal ticket).

#### 19 June 2022 <a href="#id-19-june-2022" id="id-19-june-2022"></a>

**(ARM v22.1.12)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed a minor bug where the child members checkboxes remained checked even when the parent metadata type was unchecked (internal ticket).
* Fixed an issue where CI job build **ToRevision** number was mismatched in the **CI Job Results** and the **CI Build Info** page ([#45580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076910037)).
* Fixed an issue where the request parameters were empty in the **nCino Feature Commit History** screen ([#45855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077344165)).
* Fixed an issue where the users while accessing the commits older than 30 days, ARM throws `Request parameters are empty/null` error (internal ticket).
* Fixed an issue where the users when accessing the **Commit History** page throws `Invalid FilterExpression` error (internal ticket).
* Fixed an issue where the user were unable to fetch the latest CI job weekly reports ([#42587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072104139)).
* Fixed an issue where the **Diff report** in the **Merge Request** was not working as expected ([#45315](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076389550)).
* Fixed an issue where the user ran the branching baseline operation by excluding the Managed package components, however, the **Package.xml** file still had all the managed package components listed in it ([#45125](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076117289)).
* Fixed an issue where the code coverage report was being generated at a different time than what was scheduled ([#45703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077145009)).
* Fixed an issue where the exported users list contained inaccurate information ([#44782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075451374)).
* Fixed an issue where the TAF execution were getting failed (internal ticket).
* Fixed an issue where the **From Revision** was not visible when user access their CI job from **CI Job History** page (internal ticket).
* Fixed an issue that caused **Chrome** to crash anytime a user attempted to view the functional test results for the task of running a Selenium Maven test. The functional test results screen enters a continuous cycle of requests, which crashes the browser (internal ticket).
* Fixed an issue where the **skip members** feature of ARM was not working as expected (internal ticket).
* Fixed an issue where the user while performing **EZ-Commit** with SonarQube code analysis was getting failed with `Failed to run the sonar-scanner: null` error ([#46070](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077717988)).

#### 12 June 2022 <a href="#id-12-june-2022" id="id-12-june-2022"></a>

**(ARM v22.1.11)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 05 June 2022 <a href="#id-05-june-2022" id="id-05-june-2022"></a>

**(ARM v22.1.10)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).

#### 29 May 2022 <a href="#id-29-may-2022" id="id-29-may-2022"></a>

**(ARM v22.1.9)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the branching baseline feature for profile was not working as expected ([#44615](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075179971), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed an issue where the Dataloader Pro jobs were failing with no error message ([#44620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075206808), [#44264](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074669005)).
* Fixed the issue where the Dataloader Pro jobs was not working as expected ([#43966](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301291)).
* Fixed an issue where the users while performing org to org migration of nCino record based configurations, all the related items are getting carried over except the _notes_ and _attachment_ of the Credit Memo from source to the destination environment ([#40990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069124041))
* Fixed an issue where the Jenkins builds were failing during the CI/CD process (internal ticket).

#### 22 May 2022 <a href="#id-22-may-2022" id="id-22-may-2022"></a>

**(ARM v22.1.8)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 15 May 2022 <a href="#id-15-may-2022" id="id-15-may-2022"></a>

**(ARM v22.1.7)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).

#### 08 May 2022 <a href="#id-08-may-2022" id="id-08-may-2022"></a>

**(ARM v22.1.6)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 01 May 2022 <a href="#id-01-may-2022" id="id-01-may-2022"></a>

**(ARM v22.1.5)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the picklist values failed to retrieve while preparing the CI job build ([#44117](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074423001), [#44029](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074323857)).
* Fixed the issue for the SFDX jobs where the user permissions were picked up for the deployment even if the user opts for "**Remove User Permissions**" ([#44027](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074328464)).
* Fixed an issue where new tags gets automatically added for the sharing rules after the ARM 22.1 upgrade ([#44032](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074275828))
* Fixed an issue where the SFDX CI job picked up extra content for workflow and custom labels ([#44028](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074327108)).
* Fixed an issue with EZ-commit features where the metadata file was causing the JAXM marshall exception (invalid XML format) error ([#43864](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074126263), [#43513](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073481411)).
* Fixed an issue where the quick deployment functionality was not working as expected ([#42521](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071941125)).
* Fixed an issue where the users could not view the commits list to merge them into a release label ([#43718](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).
* Fixed an issue where the code coverage reports fail to include all the classes in the CSV file ([#42848](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072441595), [#39582](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066807003)).
* Fixed an issue where the commits triggered in ARM shows a different author in Azure DevOps ([#44225](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074591143), [#43503](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073518014)).
* Fixed a bug where selecting the "**Deployment**" icon after signing in to the ARM application caused the user to log off and on and return to the home page ([#44040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074301863)).
* Fixed a bug where the check-ins display the wrong number of files changed during commit ([#40119](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067784313)).
* Fixed an issue in the TAF module where nothing pops up when you click on the "**View Log**" button ([#42020](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071114057), [#40284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067992205)).
* Fixed an issue where the users while accessing the help center from ARM application, receiving the **({"result":"failure","cause":"E105 - Request Delayed"})** error ([#43579](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652168)).
* Fixed a bug where the commits was getting failed due to SCM (Software Configuration Management) authentication failure ([#42276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071577005)).
* Fixed a bug where the merge operations ran for more than 12 hours and later failed ([#38755](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065037173), [#42874](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072544001), [#38913](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065383003)).
* Fixed an issue where extra metadata members are picked up for the profile component during the EZ-Commit process ([#41361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069919263)).
* Fixed an issue where the users could not use commit template for the deployment ([#43995](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074325045), [#43586](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073635324), [#43905](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074163310), [#43407](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073339003)).

#### 24 April 2022 <a href="#id-24-april-2022" id="id-24-april-2022"></a>

**(ARM v22.1.4)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where performing a validation merge on the Azure repository branch creates the merge label and an external commit label with the same name and the same revision number ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).
* Fixed an issue where the package deployment job was not triggered automatically once the validation was successful ([#43779](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074011003), [#43789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074031001)).
* Fixed the issue where the **DiscoveryAIModel** metadata type was unsupported, which caused the CI jobs to fail ([#42981](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072630620)).
* Fixed an issue where the users were unable to fetch the standard fields from the custom objects ([#43378](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073288005))
* Fixed an issue where the ARM user interface gets distorted when the zoom is 100% ([#43735](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073906153)).
* Fixed an issue where the ALM workflow was mismatched ([#43775](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073985001)).
* Fixed **Spring4Shell vulnerability** by upgrading the Spring Boot version to 2.6.6 for the AR Agent ([#43584](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073648538)).
* Fixed an issue where the "**invalid session**" error occurs when the user tries to delete and resave the cloned CI job.
* Fixed an issue where the **Conflict Resolution** screen was not showing all the merge conflicts ([#43663](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073767313)).
* Fixed an issue where the CI job build status fails with "**java.util.ConcurrentModificationException**" error when running the nCino feature migration templates ([#40752](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068643005)).
* Fixed an issue with the Dataloader Pro job where the users, when trying to migrate the case object along with feed item & feed comment, the ARM application throws the "**invalid cross reference id**" error ([#43703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073896030)).
* Fixed an issue where the merge process, after being sucessful, did not display the code coverage report ([#42079](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071200468)).

#### 17 April 2022 <a href="#id-17-april-2022" id="id-17-april-2022"></a>

**(ARM v22.1.3)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue for the Chrome browser where the ApexPMD ruleset was not uploading incorrectly (under the **Plugins** section). For other browsers, it was working as expected ([#42954](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072670003)).
* Fixed the issue with the merge where the changes present in the source branches were not picked up, and therefore latest changes did not reflect on the destination branch ([#43553](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073610001), [#43598](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073662177), [#43595](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073653614), [#43593](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652863), [#43591](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073629096), [#43580](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073652300), [#43574](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073651134)).
* Fixed an issue where the Salesforce-DX deployment and rollback mismatches ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040))
* Added the criteria to trigger the callout URL post-deployment. If you set it to _success_, the callout URL is activated if the salesforce deployment is successful ([#38990](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065571472)).
* Enabled feature flag settings to select between classic ARM and Salesforce CLI process to generate package manifest.
* Fixed an issue where the commit validation is successful for an empty field, whereas the CI job fails ([#43324](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073218067)).
* Fixed an issue where the deleted metadata components were showing under the **"File Changes"** tab but did not appear under the **"Destructive Changes"** column while carrying out a manual deployment ([#41670](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070494027)).
* Fixed Dataloader Pro job issue where the job is completed successfully without loading all ancestors/master objects data to the destination environment ([#43276](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073123039)).
* Fixed branching baseline issue where all metadata from the production org were not copied to the version control repo/branch ([#42938](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072633029), [#42685](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072244001), [#42955](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072644308), [#42445](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071818001), [#43038](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072780490), [#42753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072314347), [#42242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000071424143), [#42766](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072375048), [#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* Fixed the below nCino issues:
  * Unable to proceed with feature deployment using an existing community feature migration template due to the following error: **"No External Id field exist in source org."** This is now fixed and working as expected ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
  * Non-template records were being picked up during nCino deployment.
  * Non-template records are fetched in the dataset.
  * Spread Statement Record failing with the error **“Missing Statement Types.”** This is now fixed.

#### 10 April 2022 <a href="#id-10-april-2022" id="id-10-april-2022"></a>

**(ARM v22.1.2)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **Abort** option was showing for completed CI jobs ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463), [#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed the issue where the SFDX deployment is getting failed even though the user uploaded the correct file.
* Fixed a bug where the static code analysis (SCA) status shows as **in progress** for a failed execution.
* Fixed an issue where deleting a custom field was affecting other custom objects where the globalpicklistvalue is shared by multiple objects ([#42782](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000072370556)).
* Fixed a bug where the users were not able to view specific values under the standard value sets in the **New EZ-Commit** screen ([#41773](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070686445)).
* Fixed a bug where the **New EZ-Commit > Deleted Component** tab throws a null error on expanding the metadata types.
* Fixed a bug where the deploying records via record based configurations (RBC) was throwing error: **"No external Id field exists in the source org"** ([#43263](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000073131047)).
* Fixed an issue where creating a new nCino feature migration template takes longer than expected ([#41855](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070869289)).
* Addressed out of memory (OOM) and other performance issues in this weekly release.

#### 03 April 2022 <a href="#id-03-april-2022" id="id-03-april-2022"></a>

**(ARM v22.1.1)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option where not working when users use the EZ commit/ Merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 March 2022 <a href="#id-27-march-2022" id="id-27-march-2022"></a>

**(ARM v22.1.0)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** in the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the exclude metadata types in the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).

***

## ARM Release Notes **21.6**

**Date of Release:** _**21 November 2021**_

**On this page:**

1. [New Features](./#new-features)
2. [Enhancements](./#enhancements)
3. [Improvements](./#improvements)
4. [Changelogs](./#changelogs)

### New Features <a href="#new-features" id="new-features"></a>

#### Pull Request Support for Azure DevOps <a href="#pull-request-support-for-azure-devops" id="pull-request-support-for-azure-devops"></a>

Pull request is a feature that allows you to review code and provide feedback before merging it into the master branch. Previously, we had GitHub and Bitbucket support. We've included support for Azure DevOps in this release. ([Learn More](../../../product-guides/arm/arm-features/version-control/external-pull-request/pull-request-support-for-azure-cloud.md))

* During **Ez-Commit** and new **Pull Requests**, you can now create a Pull Request in Azure with the assignee.
* You should be able to choose the repository, the base branch, and another branch to compare during the creation of a pull request.
* A link to the Azure DevOps application will be included in each pull request created in AutoRABIT. The pull request can also be approved directly from the AutoRABIT application.

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### Audit Log Report <a href="#audit-log-report" id="audit-log-report"></a>

AutoRABIT had an audit report feature that gave you a comprehensive view of your business operations by fostering a collaborative operational audit environment. In this release, we've made some enhancements and added a button called **"Audit Log Report"** on the CI job page, which allows you to generate a report in PDF format for a specific period.

* We've improved the **CI Job Result** screen by giving users the option to generate an Audit log report for internal auditing purposes. This is a report of CI jobs deployments and the commits associated with each deployment, including commit details such as Author, Commit Time Stamp, and so on.
* We changed the timestamp in the Audit log report from **12-Hour** format to **24-hour UTC** format by default to comply with ISO 8601 notation, which is a commonly recommended format for representing date and time.
* Added support for custom _“keynames”_, _“Salesforce Org type“_ and _“AR SF Org type”_ in the Audit trail report wherever Salesforce org name details are applicable.

#### **Salesforce CLI Upgrade** <a href="#salesforce-cli-upgrade" id="salesforce-cli-upgrade"></a>

Salesforce CLI is a command-line interface for working with your Salesforce org that makes development and build automation easier. It can be used to create and manage organizations, synchronize sources to and from organizations, create and install packages, and more. In this version of ARM, Salesforce-DX CLI is upgraded to the latest **7.129** version.

#### **Salesforce Winter (API 53) Support** <a href="#salesforce-winter-api-53-support" id="salesforce-winter-api-53-support"></a>

In order to keep our product up to date with the most recent Salesforce updates. AutoRABIT now supports the most recent **API version 53** in this release. Now our Salesforce developers will begin using API 53 on their Sandboxes for development. The most recent API version is intended for customizing the metadata model and developing tools to manage it.

### Improvements <a href="#improvements" id="improvements"></a>

#### Platform Improvements <a href="#platform-improvements" id="platform-improvements"></a>

* We've been working hard over the last few weeks to improve our platform's stability, performance, query optimizations, code smells, security vulnerabilities, and reliability. With this release, you will notice significant improvements in our application, such as faster page load times, improved performance, and faster search functionality, among other things.
* **JQuery Upgrade**: JQuery was updated from version **1.8.3** to version **3.6**. Upgrading to the most recent version of jQuery makes our application more secure, as well as potentially faster in terms of script execution and loading.

#### **UI Improvement** <a href="#ui-improvement" id="ui-improvement"></a>

Across the CI Job module, **"Load More"** buttons have been replaced with **"Previous"** and **"Next"** buttons. This new feature will allow our users to display 25, 50, 75, or 100 records on a single page and navigate between pages using the Previous and Next buttons. This feature was previously limited to the Version Control module, but it has recently been expanded to include the CI Job module as well.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 11 Mar 2022 <a href="#id-11-mar-2022" id="id-11-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to deploy release labels ([#40600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068395530)).
* Fixed the following SSO errors:
  * Unable to use SSO for AutoRABIT authentication ([#37767](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062637173)).
  * Unable to log in via SSO in the chrome and the firefox browser.
  * Fixed "**domain name does not exist**" error ([#41853](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070865403)).
* Fixed a bug where users were getting an undefined error for the standard templates while editing the CI job.
* Fixed an issue where the status of the AutoRABIT ExternalId field was showing as processing, but it was marked as completed in the log report ([#40669](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068569430)).
* Fixed a bug that restricted users from using Dataloader Pro's **Auditable Standard** field feature ([#40794](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068711163)).
* Fixed an issue where the users were unable to replace attachment records in the destination org.
* Fixed an issue where the attachments were not completely deployed in the target environment ([#41208](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069667003)).
* Fixed an issue where users were unable to deploy the nCino feature from org to org using the **nCino-Forms** **standard template** ([#38764](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065055277)).
* Fixed an issue where the users were unable to **stop/delete** the data loader running jobs ([#39556](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066791149)).
* Fixed an issue where the users when attempting to initiate the deployment, were failing with the **"Failed to initiate deployment request"** error ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to perform the branching baseline operation ([#41622](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070417055)).
* Fixed an issue where the users were not able to configure the approver's lists on the **New Merge Request** screen ([#41844](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070874003)).
* Fixed an issue where the users trying to revert a commit for a commit label was getting failed ([#39613](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066805855)).

#### 06 Mar 2022 <a href="#id-06-mar-2022" id="id-06-mar-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **skip members** feature was not working for the Version Control, Deployments, and CI Job module ([#41531](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221221)).
* Fixed an issue where the users were receiving layout permissions errors when using **Prevalidation Commit**.
* The SCA option was not working when users use the EZ-Commit/merge operation. The issue has now been fixed ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* Fixed an issue where the users were unable to generate the deployment report and received validations errors for the EZ-Merge operation ([#41639](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423671)).
* Fixed an issue where the users were unable to update any changes in the permission section.
* Fixed an issue where the non-licensed users were receiving the deployment email failure notification for the unsuccessful deployment ([#41705](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070543145)).
* Fixed an issue where the users were unable to use the nCino feature after the ARM was upgraded to v21.6 ([#41108](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069360251)).

#### 27 Feb 2022 <a href="#id-27-feb-2022" id="id-27-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to switch the tab from the **Test Coverage** to the **Class Coverage** on the **Apex test results** page ([#41455](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070062179)).
* Fixed an issue where the users were unable to save Salesforce settings in the **My Account** screen ([#41329](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069835104)).
* Fixed an issue where the users were not able to save the excluded metadata types on the **My Account** page ([#41529](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070221075)).
* Fixed an issue where the users were not able to create a new ALM project for the Azure repository ([#41554](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070326013), [#41630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070423082)).
* Fixed an issue where the users having difficulty with the **datamigration.properties** file while creating a new instance ([#41510](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070231024)).
* Fixed an issue where the users when trying to start a deployment, it was getting failed with the "**Failed to start deployment request** error" ([#40620](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068429999)).
* Fixed an issue where the users were unable to revert the commits using AutoRABIT ([#39957](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067378384)).
* Fixed an issue where the users were not able to use the "**Files Changed**" functionality on the **Merge Request History** page ([#41456](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000070069155)).
* Fixed an issue where the users were unable to delete the changes made in the version control branch via AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed a bug that prevented users from performing commit and merge operations in AutoRABIT ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where the external objects with lookup relationships were not getting displayed under the child objects in the Dataloader Pro ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed an issue where the users were unable to update the "**Validation checks**" status from the in-progress state to the completed state.
* Fixed an issue where changes from multiple package directories were not being retrieved without selecting a package directory.
* Fixed an issue where the users were unable to attach the CSV file while carrying out the CI deployment.
* Fixed an issue that caused users to receive an invalid session error when changing their password.

#### 20 Feb 2022 <a href="#id-20-feb-2022" id="id-20-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to see the commits ID in the release label ([#41284](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069797001)).
* Fixed an issue where the users were unable to view their permission details in the Users and Roles tab ([#41043](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069219179)).
* Fixed an issue where users were not able to delete the changes made in the source branch using AutoRABIT ([#39130](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065873001)).
* Fixed an issue where the branching baseline for a profile and branch to branch merge was not working ([#40836](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068737067)).
* There was an AutoRABIT performance issue that caused searching for revisions, validations, and commits to taking a long time. It has now been fixed ([#39129](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065834119)).
* Fixed an issue where users were not able to commit their changes to the branch ([#39269](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066103022)).
* When users attempted to update changes in the target org using the profile manager, the deployment getting failed. It has now been fixed ([#40599](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068421379)).
* Fixed an issue where users were unable to switch from a credential-based login to an SSO-based login ([#40871](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068784190)).
* AutoRABIT instances were not supporting the Salesforce API 54 version. It has now been fixed. ([#40921](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068957023)).
* When a user performs a pre-validation commit on the Azure repository branches, it creates a duplicate external commit with the same revision ID. This issue has now been fixed ([#39287](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141740)).

#### 13 Feb 2022 <a href="#id-13-feb-2022" id="id-13-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **"Group By"** functionality was not fetching the correct CI job results ([#38870](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069460109)).
* Fixed an issue where the deployment status of CI Job has failed in logs but the process is still in-progress stage ([#40805](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068697958)).
* Fixed an issue where the users were unable to use the SCA for LWC components unlike apex class, triggers, and aura bundle ([#39288](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141955)).
* When a pull request is in progress, the job is not triggered for additional changes committed before the work is completed. This is now fixed ([#38877](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065276358)).
* Fixed a bug where the users were facing challenges while merging the entire branch changes to the target environment ([#39451](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066611145)).
* Fixed an issue where the File Diff shows full component (especially Aura, LWC components) as a change instead of delta changes ([#39351](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066320276)).
* Fixed a bug where the sub-users without admin privileges were able to export and download the org users' data from **Admin > Users** section.
* Fixed an issue where the data loader pro throws the error **"Error creating output directory: configs"** while uploading data from one environment to another ([#40832](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068736307)).
* Fixed an issue where the external object-related lookups were unable to verify the relationship associated with the external objects in the destination org ([#41084](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069299165)).
* Fixed a minor user-interface bug where the users were unable to find the **Resolve Conflict button** to resolve the merges conflict. This is now resolved.

Limitations identified in this release:**RestrictionRule** metadata type is not supported for the SFDX deployment.

#### 06 Feb 2022 <a href="#id-06-feb-2022" id="id-06-feb-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed the below UI issues:
  * The **"Commit"** button was not available for the merge request label job. ([#38876](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065275014)).
  * For the entire deployment, the **"To Revision"** radio button was disabled, and users were unable to select revisions from the list provided.
  * Although the field **"Timezone"** was mandatory upon signup, the users were able to proceed without picking a timezone.
* Fixed an issue where the admin was unable to assign permissions to its sub-users. This is now working as expected ([#40017](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067565003)).
* Fixed an issue where the validation rule automation was not working for the **Environment Provisioning** module ([#41035](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069198519), ([#40991](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000069108736)).
* Fixed an issue where the data loader pro job is not able to load data for objects with fields exceeding limits([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the users were unable to register the existing branches to AutoRABIT ([#40894](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068809067)).
* Fixed an issue where the EZ-Merge was showing status as failed in the AutoRABIT application however, in the Salesforce environment the status shows as success ([#40673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068536502)).
* Fixed a bug where the users were unable to register a dev hub on the **SDFX > Hub Management** page.

#### 30 Jan 2022 <a href="#id-30-jan-2022" id="id-30-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 29 Jan 2022 <a href="#id-29-jan-2022" id="id-29-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 23 Jan 2022 <a href="#id-23-jan-2022" id="id-23-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to generate the code coverage log report from the **Report** Module ([#38717](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939344)).
* Fixed an issue where the users were unable to upload the package.xml file to resolve the merge conflict ([#39960](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067372236)).
* Fixed an issue where the users were able to commit the changes although the validation got failed. ([#38228](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775343)).
* Fixed an issue where the user was unable to perform the **Enable/Disable validation rule** on the Managed package object using the environment provisioning functionality ([#40297](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000068017532)).
* Fixed a bug where the user was unable to deploy the **Email Template** on their target environment ([#40241](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000067922013)).
* Fixed an issue where users were unable to upload/migrate the knowledge articles from one sandbox to another sandbox ([#37922](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063030291)).
* Fixed an issue where the users were facing the **"Null Pointer Exception"** error during the merge prevalidation process.
* Fixed an issue where If the users picked all the conflicted files during a merge request, they would receive an error message saying **"Please click on any conflicted file."**
* Fixed an issue where the users were unable to find the log report for the newly created branch in AutoRABIT.
* Fixed an issue where the users were unable to find out the work item statuses during the deployment process for the unlocked packages.
* **ALM Enhancements:**
  * Added a new section called **"ALM Management"** to the **Admin** module for merge requests
  * Detailed information on all of your ALM's active and inactive sprints.
  * Smart commits to reading the comment in a revision associated with your ALM story.
  * We have introduced the **ALM Details** section that lists the work items linked with the commits along with the existing and post-merge status.
  * Ability to keep the work item status without a change or update it during EZ-Commit.
  * You may now configure the job to pick up revisions based on your work item status while deploying from version control to a Salesforce org, allowing you to adjust the status even after a successful rollback.

#### 16 Jan 2022 <a href="#id-16-jan-2022" id="id-16-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the users were unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 09 Jan 2022 <a href="#id-09-jan-2022" id="id-09-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as their parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 02 Jan 2022 <a href="#id-02-jan-2022" id="id-02-jan-2022"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the CI Job builds are getting stuck and no log information was displayed ([#39052](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065705011), [#38992](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564443), [#39682](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066942137)).
* Fixed an issue where the conflicted files downloaded were incorrect during the merge process ([#39364](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066317317)).
* Fixed an issue where the aura components were not getting retrieved while carrying out the branching baseline operation ([#38610](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064710558)).
* Fixed a bug that restricted users from entering the credential name on the **"Create Credential"** screen because the field was disabled.
* Fixed a bug where the super administrator was getting an empty popup screen when navigating to the **Process Summary** page.
* Fixed an issue where the users were able to find the **Abort** option even when the CI Job had been completed successfully ([#38177](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063673463)).

#### 26 Dec 2021 <a href="#id-26-dec-2021" id="id-26-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **commit approvers** were not receiving email notifications due to the commit prevalidation being stuck in-progress. ([#38908](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065375104)).
* Fixed an issue where the users were not able to select the master branch as the parent branch while registering existing branches from the repository in AutoRABIT ([#39082](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065729137)).
* Fixed an issue where the users were receiving an error message saying **"Please select the date"** even though the date was selected when registering the SVN Branch.
* Fixed an issue where the destructive commit components were still displayed for deployment ([#38888](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065298351)).
* Fixed a bug where the access token is being printed along with the URL in the **Merge Log** report ([#39546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066761398)).
* Fixed an issue where when users expanded the metadata types on the **Profile Manager** screen, they were able to spot duplicate child components.
* Fixed an issue where the lookup field values were not picked up while creating the nCino feature migrating template ([#38868](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065239462)).
* Fixed a bug that displays the nCino-related CI Jobs on the ARM **CI Jobs Results** page.

#### 19 Dec 2021 <a href="#id-19-dec-2021" id="id-19-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user was unable to close the diff report file in the **Org Synchronization History** screen ([#39149](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065918101)).
* Fixed an issue for the SFDX CI Jobs where the metadata types were not excluded without the baseline revision.
* Fixed an issue where the release label deployment is adding unselected components in the deployment package ([#39239](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066031923)).
* Fixed a bug where the users were unable to delete unwanted Dataloader Pro jobs from AutoRABIT ([#38600](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064711105)).
* Fixed a bug where the parallel CI jobs are not working as expected ([#38803](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076930)).
* Fixed a bug where the users were unable to generate the code coverage log report from the **Report** module ([#38673](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064853195)).
* Fixed a bug where the search box doesn't work well with uppercase and lowercase in the commit label unlike the search in the dropdowns on the **Commit History** page ([#39286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000066141525)).
* Fixed an issue where the metadata types **"NavigationMenu"** and **"IframeWhiteListUrlSettings"** were included in the build view changes for both DX and non-DX CI Jobs, despite being excluded.

#### 12 Dec 2021 <a href="#id-12-dec-2021" id="id-12-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when the user is trying to perform pre-validation commit for report metadata, it is getting added under emailservice functions in diff report ([#37925](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063067009), [#38581](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064666105), [#38880](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065272149), [#38734](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064981980)).
* Fixed an issue where the case _entitlementProcess-meta.xml_ files were not picked up during deployment ([#39069](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065734191), [#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed an issue where the deployment report is getting failed while doing prevalidation merge with the report folder.
* Fixed an issue where users were unable to retrieve a package which has more than 1000 components ([#38737](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064985007)).
* Fixed a bug where a null pointer exception was thrown while loading in Dataloader Pro ([#38286](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063928003)).
* Fixed an issue where the entitlement process is getting removed from Package.xml ([#39097](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065777009)).
* Fixed an issue where the external commits did not show up on the release label ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed a bug that displays the wrong statuses in the test reports ([#39008](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065572975), [#38986](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065564303)).
* Fixed an issue where the code coverage percent is not available in the case of SFDX merge operation.
* Fixed an issue where the data loader pro jobs were not able to load data for objects with fields exceeding 800 ([#38790](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085228)).
* Fixed an issue where the code coverage percentage shows as 0 in the UI logs even after deployment validation is passed.
* Fixed a bug where the changes are being committed even after a failed validation.
* Fixed an issue where the package directory filter in the release labels is not working as expected.

#### 05 Dec 2021 <a href="#id-05-dec-2021" id="id-05-dec-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where when pre- and post-destructive changes were added to the process, it caused the deployment to fail ([#38330](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064040175), [#38721](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064967175)).
* Fixed a bug where for fewer CI jobs, the **Older** button was disabled. This has now been enabled and is working as expected ([#39050](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065702042)).
* Fixed an issue in the SFDX module that prevented commits from being executed using scratch org ([#38789](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065076258)).
* Fixed an issue where the external commits were not displayed when creating release labels or merging single revisions. This is now working as it should ([#38822](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065151262)).
* Fixed an issue where users were unable to run SCA within the reports module due to an error stating **"Invalid mapping credentials."** In addition, the number of issues indicated in the Ez-commit process does not match the CodeScan analysis ([#38917](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065373386)).
* Fixed a bug where single data loader jobs couldn't be edited and there was a mapped field cache issue ([#38753](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065026084)).
* Fixed an issue where the alm mapping details for the scratch org with alm configuration could not be found.
* While executing scratch org alm commit with skip mapping set to false, the current ALM work item status was reporting _"empty"_ results. This is now fixed.
* Fixed a bug that allowed users to save multiple criteria rows with the same priorities for ApexPMD.
* Fixed an issue where the repository filter on the _Commit History_ screen was reset to default after resolving a conflict.
* Fixed a bug where the failed component count position is wrong when the window is scrolled.

#### 28 Nov 2021 <a href="#id-28-nov-2021" id="id-28-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed nCino objects deployment issue during using nCino CI Jobs ([#39375](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058591003)).
* Fixed an issue where the custom object is being listed during CI Job operation but not during Ez-commit ([#38361](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064187022)).
* Fixed Ez-merge issue which shows different results in AutoRABIT when compared to the production environment ([#38831](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065181230)).
* Fixed an issue where the users were unable to extract deleted records and threw **"Malformed Query Fault"** error ([#38448](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064441154)).
* Fixed an issue where the pull request support with BitBucket was not working properly. This is now fixed ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed a bug in the merge request and pull request validation builds which were unable to list the changed components whereas the CI Job build was able to pick them up ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017), [38713](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064936484)).
* Fixed an issue where the org administrator was unable to assign hub level permissions to its sub-users ([#38898](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065336005)).
* Fixed wrong metadata identification for deletion issue ([#37703](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062453147)).
* Fixed an issue where the user was unable to update **"Configuration For recordTypes picklistValues"** ([#38901](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065355005)).
* Fixed API version error in the CI Job screen ([#36550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059178003)).
* Fixed CI build failing issue ([#38630](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064788278)).
* Fixed EZ-Commit issue where the file diff was throwing an error due to credential scope issue ([#38950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065446001), [38795](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065077341)).
* Fixed an issue where duplicate entries were seen while creating release labels ([#37300](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061440253)).
* Fixed a bug where the user was unable to click on the **OK** button on the **Merge Request History** screen ([#38781](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000065085003)).
* Fixed an issue where the **"include delete records"** checkbox is de-selected automatically during editing the data loader extract job.
* Fixed an issue where the scratch org permissions are not visible on **"hub level permissions"** and _"_**scratch org permissions"** screens.
* Fixed Ez-commit issue where a sub user with only one repository registered with AutoRABIT, is not able to find/select his repository in the **EZ-Commit** screen.
* Fixed an issue where the repository filter is reset to default during the conflict resolve flow.
* Fixed registering the branch issue when the branch registration crossed 100 limits in AutoRABIT.
* Fixed a bug where the parent checkbox in the download zip for CI Job is not working as expected.
* Fixed wave-dependent missing files from the package during the prevalidation merge operation.
* Fixed an issue where the non-SFDX CI job for WaveTemplates is showing no modifications when triggered.
* Fixed single data loader and data loader pro filter issues while carrying out the edit functionality.

#### 21 Nov 2021 <a href="#id-21-nov-2021" id="id-21-nov-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the quick deployment feature was not working as expected and was throwing **"Invalid Login"** error ([#37802](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062709159)).
* Fixed a bug where the merge request validation was getting failed ([#37095](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060661017)).
* Fixed an issue where the commit search was not working as expected in the **Version Control** module ([#36548](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059165111)).
* Fixed an issue where the users were facing invalid credentials issue while updating the src as metadata folder path in-branch settings **(Admin > VC' Repos)** ([#38727](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064939824)).
* Fixed an issue where the pull request support for BitBucket was not working properly as expected ([#38644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064828044)).
* Fixed an issue where the deployment shows failed status although there are no failures and the items did get moved to the destination org. This is now working as expected ([#37774](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062644015), [#38363](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064201151)).
* Fixed an issue where the user was not able to retrieve the metadata to deploy the changes using AutoRABIT's deployment feature.
* Fixed data loader pro issue which was throwing unknown error while migrating the data objects ([#38566](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064649001)).

***

## **ARM Release Notes 21.5**

**Date of Release: 29 August 2021**

**On this page:**

1. [Enhancements](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#enhancements)
2. [Changelogs](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#changelogs)

In keeping with our dedication to continual improvement, the **August-21 (AR 21.5)** release delivers a plethora of exciting upgrades and improvements to our AutoRABIT application.

### Enhancements <a href="#enhancements" id="enhancements"></a>

* **UI/UX Improvements:** Focused on application performance and user experience. Try it out for yourself and let us know how to feel:
  * **Page Navigation:** When working with several records, breaking data into multiple pages is always a good idea. You can now view 25, 50, 75, or 100 records on a single page, and use the **Previous** and **Next** buttons to switch to the previous or next page. This feature is now only available in the Version Control module, but it will be expanded to other modules in future releases.
  * **Never miss a required field:** You will be prompted to fill in all the required fields before you proceed. Follow the UI highlights to minimize rework.
* **Customize CI jobs for desired Salesforce API versions:** To support different Salesforce API versions for distinct Salesforce orgs instead of a global setup, we've added a new checkbox named **Salesforce API version** across the CI Job module. This will offer a granular facility in a CI job to select the required Salesforce API version.
* **Improved Audit Trail Report:** Additional data was added to the reports to support improved report analysis.
* **Performance Improvement:** Waiting is always boring- we have reduced that wait for you.
* **Salesforce CLI Upgrade-** Salesforce CLI upgraded to the latest stable **7.112** version.

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 14 November 2021 <a href="#id-14-november-2021" id="id-14-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed deployment issues
  * Fixed an issue where no metadata was found while validating the components from the master branch to the production environment ([#38612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064709627), [#38587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064645657), [#38571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639413), [#38537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064517581), [#38552](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064584042), [#38549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064544537))
  * Fixed revision based deployment issue ([#38386](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064283007))
  * Fixed an issue where the commit labels changes are not reflected in the release label ([#38569](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064646158))
  * Fixed an issue where the salesforce deployment from GIT to SFDC was not working ([#38558](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639001))
  * Fixed deployment issue where no components were being retrieved via _Single Revision_ or _Revision Range_ ([#38550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064581003), [#38546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064558188))
* Fixed a bug where the deployment CI Job occurs multiple times ([#37454](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061960003)).
* Fixed the search and substitute deletion rule issue ([#38410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064291165)).
* Fixed SFDX parent and child job triggered the issue.
* Fixed an issue where the review artifact with AutoDraft functionality was not working properly in the EZ-commit screen.

#### 07 November 2021 <a href="#id-07-november-2021" id="id-07-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141))
* Fixed SFDX deployment and rollback mismatches issue ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040)).
* Fixed a bug where when attempting to commit the deletion of 19 profiles, a Diff Report listing of 20 profiles was generated. ([#38303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063932311)).
* Fixed code coverage report discrepancy issue ([#36282](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058168335)).
* Fixed an issue where the wave template related dependent files were missing from the package \[CI, Deployment, VC].
* Fixed an issue where all existing credentials for version control mappings that were created using the **Profile** screen were reset.

#### 31 October 2021 <a href="#id-31-october-2021" id="id-31-october-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* The deleted sharing rules were not showing up in the EZ-Commit Deleted tab, which was fixed ([#37747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062586019))
* Fixed a bug where the older commits were not accessible for merge ([#38242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063785008)).
* Fixed an issue where when deploying a new custom object, an error _"Profile Search Layout: - System Administrator - not appropriate for object XXXXXX"_ was thrown ([#37897](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062972201)).
* Fixed a merge conflict issue([#37950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063128003)).
* Fixed a commit label issue ([#38275](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063874030)).
* Fixed an issue with SSO where users had to log in twice before being able to use the AutoRABIT application ([#36634](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059319963)).
* The issue with the SSO domain has been fixed ([#37232](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061168477)).
* Fixed data loader audit logs issue ([#37688](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062385762)).
* Fixed an issue where the users were unable to exclude _EmbeddedServiceLiveAgent_ from CI Job ([#38261](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063818321)).
* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141)).
* Fixed an issue where users were unable to compare profiles using the _Profile Manager_ feature in the _Deployment_ module ([#36978](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060367023)).
* In CI Jobs, a bug with the _"Group By"_ filter was fixed ([#38132](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063522197)).
* Fixed an issue where the community site was not getting deployed ([#38226](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775199)).
* Fixed a bug that caused metadata retrieval to fail with a **Null** error during revision range deployment.
* \[Profile Manager] Fixed an issue where the org compare feature would not work when three orgs were configured, resulting in a "Empty screen" error.
* \[Profile manager] Fixed an issue where after comparison, duplicate metadata entries and empty popups were displayed.
* \[nCino CI Jobs] Fixed an issue where the unwanted objects are displayed on editing the cloned CI Job.
