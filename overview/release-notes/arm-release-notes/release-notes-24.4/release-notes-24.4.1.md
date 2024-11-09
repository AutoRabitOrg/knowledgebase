# Release Notes 24.4.1

## ARM Release Notes 24.4.1

**Release Date: 27 October 2024**

### Enhancements <a href="#enhancements" id="enhancements"></a>

**Manageable-State Selection for Branching Baseline**\
A new option has been added to select the Salesforce org's manageable state when initiating or re-running a branching baseline. This option is available only when the retrieval type is set to Salesforce, ensuring greater control over the data types included in the process.

1. **Consistent Manageable-State Dropdown Across Modules**\
   The manageable-state dropdown is now consistently available across several modules, streamlining the user experience. It can be found in the following areas:
   * Branching Baseline
   * CI Job (Org to Org deployment)
   * EZ Commit
   * My Account (Save Global Settings for Admins)
   * Static Code Analysis
   * Org Synchronization History
2. **Global Settings Migration for Manageable State**\
   Global settings for manageable state, previously configured in the "My Account → Admin" section, are now automatically retrieved and applied across relevant modules, ensuring consistency across the platform.
3. **Database Support for Manageable State**\
   The database schema has been updated to support the manageable-state dropdown in CI Job, EZ-Commit, and Branching Baseline modules. This ensures that user selections are properly saved and retrieved, maintaining data integrity across sessions.

**Conditional Abort Functionality for Branching Baseline**\
The "Abort" button is now only clickable when the branching baseline process is actively in progress. The abort functionality behaves as follows:

* If the process is in the retrieval stage, clicking "Abort" will stop the operation.
* If the process is in the committing stage, clicking "Abort" will cancel the process.
* If the revision has already been generated or committed, the "Abort" button will be disabled to prevent unnecessary actions.

1. **Enhancement: Updated Actions in Branching Baseline**\
   The actions available for each branching baseline iteration now include "Run," "Abort," and "Delete," providing clear and accessible options based on the process state.
2. **Enhancement: Combined Revision and Info Section in Iterations**\
   The "Revision" and "Info" columns in the branching baseline iterations section have been merged into a single "Revision Info" column. This section is now a clickable hyperlink, allowing users to view detailed information for each specific revision easily.

**Improved Abort Functionality with Interrupt Method (Internal)**\
The abort functionality has been enhanced across the application by implementing the recommended interrupt method, significantly improving reliability and preventing potential thread-related crashes. This update ensures a smoother and more stable abort process.

The enhanced abort functionality has been applied to the following areas:

* Admin
* CI Jobs
* Version Control Release Labels

Thorough internal QA checks have been performed to ensure the stability of this new approach.

**Enable the “Trigger Build On Commit” option when creating a CI Job**\
Users can now enable the “Trigger Build On Commit” option when creating a CI Job, allowing automated builds triggered directly by commits. Upon selecting this option, a webhook setup will become available, ensuring that every new change in the version control system triggers an update to the CI Job. Builds will only initiate for commits made in the feature templates folder.

### Support <a href="#support" id="support"></a>

**Accurate Merge Status Display**

Customers reported receiving expiry email notifications with a misleading status of "MERGED," even though the merge was still pending approval or awaiting changes to be committed. This confusion has been addressed by updating the merge status in the expiry email. Now, the system retrieves the status from the SCM History table, ensuring the actual state of the merge is reflected. Users will no longer see "MERGED" unless the merge has been fully completed, providing clearer communication on the status of their merges. Support Case #120537

**Profile Comparison Layout and Behavior Fixes**

The following issues in profile comparison have been resolved by adding the "Person Account" column dynamically when person accounts are enabled:

1. **Record Type Column Fix**: The Record Type section in new profile comparisons now displays only two columns, as expected. The third column, "Person Account Default," will only appear in the downloadable report if person accounts are enabled.
2. **Layout Fix**: The layout issue where five columns were displayed instead of six during profile comparisons has been addressed.
3. **Default and Visible Field Fix**: The issue where users could check 'Default' without checking 'Visible' and could not uncheck 'Default' once selected has been fixed.

These changes ensure a more accurate and dynamic display in profile comparisons, improving the overall user experience. Support Case #122267

**Select All Behavior Correction in Deployment Tab**

A UI bug in the Deployment tab has been fixed where unchecking a metadata member under the "All Metadata" tab did not update the "Select All" option as expected. The condition for deselecting "Select All" has been corrected based on metadata types in the front end, ensuring that when individual metadata members are unchecked, the "Select All" option now responds accurately and reflects the correct selection status. This fix improves the consistency and usability of the deployment process. Support Case #122601

**Apex Test Class Live Status Fix**

The issue where the Live status for the Apex Test Class was not populating under the SF Org Management section has been resolved. The fix involved changing the response data type from text to JSON, allowing the Live status to be fetched and displayed correctly for Apex Test Classes. This update ensures accurate status reporting for users. Support Case #122818

**Vlocity Deployment Failure Fix**

A code fix has been implemented to resolve the issue where Vlocity deployments were failing during VC incremental deployments. The failure occurred because the CI job picked a different dependency, specifically the _contentVersion_ dependency, which was not included in the release label deployment. The fix removes non-Vlocity components during CI deployments, ensuring that only relevant dependencies are picked, resulting in consistent and successful Vlocity deployments. Support Case #121492

**Board Type Selection Fix in Release Label Merge**

An issue where the board type was automatically changing from Vlocity to Salesforce during release label merges has been resolved. The problem occurred because the board type was not being explicitly set to Vlocity during the merge operation, causing Salesforce to be selected by default. This fix ensures that the correct board type, Vlocity, is maintained during the merge process. Support Case #123577

**Unrelated Changes in EZ-Merges Fix**

A fix has been implemented to address the issue of unrelated changes being pulled into EZ-Merges. To prevent this, the system now cross-checks the remote head revision against the local revision before allocating the workspace, ensuring the workspace is properly synced with the remote repository.

Additionally, loggers have been added to track and identify the root cause should this issue recur in the future. These updates ensure a more reliable and controlled merge process, reducing the chance of unintended changes being included in EZ-Merges. Support Case #122348

**Manual Deployment Destructive Changes Fix**

An issue was identified during manual deployments using AutoRABIT Build, where clearing all pre-destructive changes did not exclude them as expected. This occurred when deploying via the _Metadata.zip_ option in non-DX custom deployments, where destructive changes were still included despite being deselected.

A code fix has been implemented to ensure that when pre-destructive changes are cleared during deployment, they are properly excluded from the process. This update ensures that all selected components are correctly deployed, without any unwanted destructive changes being included. Support Case #122288

**Review Artifact Screen Icon Display Fix**

An issue on the Review Artifact screen where icons were not displaying correctly during keyword searches (Ctrl + F) has been resolved. Users previously saw only box icons, leading to confusion about the functions of each icon.

The fix involved correcting the file path for font icons and updating the CSS to ensure proper loading. Icons now display correctly, providing clear visual guidance for each action on the screen. Support Case #123456

**NamedCredential Search and Substitute Fix**

An issue was identified where the "Search and Substitute" feature was not working for the _NamedCredential_ metadata type. The problem occurred because the metadata type was misspelled as "NamedCrendential" in the configuration file.

The root cause has been addressed by correcting the spelling of "NamedCredential" in the JSON file that maintains supported metadata types and their subnodes. Support Case #124120

**Deactivated User Deletion Error Fix**

An issue where an error pop-up appeared when attempting to delete deactivated users has been resolved. While the user was successfully deleted after a page refresh, the error caused confusion.

The fix involved correctly reading the JWT token during the deletion process, ensuring that inactive users can now be deleted without triggering an error message. This update streamlines the user deletion process and eliminates unnecessary pop-ups. Support Case #123900

**Validation Job NullPointerException Fix**

An issue causing validation CI jobs to fail with a `java.lang.NullPointerException` has been identified. The problem occurred intermittently when the customer changed the baseline revision, with the workaround only providing temporary relief.

A fix has been implemented to address the root cause of the null pointer error. This ensures that validation jobs now run consistently without failure, eliminating the need for manual interventions or workarounds. Support Case #124232

**Workspace Error in EZ-Commit Delete Tab Fix**

An issue where users encountered a "Workspace does not exist" error in the Delete tab of EZ-Commit has been resolved. The error occurred because the system did not check whether the workspace was optimized before throwing a custom exception when the workspace was not locked.

A fix has been implemented by adding a condition to ignore optimized workspaces when checking for locks. This ensures that users no longer see the error pop-up when navigating to the Delete tab in EZ-Commit, improving the overall functionality. Support Case #124537

### Improvements <a href="#improvements" id="improvements"></a>

**Optimized Selective Deployments**\
Selective deployments have been optimized to utilize pre-prepared artifacts, eliminating the need for additional Git operations. This enhancement allows users to perform component selection directly on the pre-prepared artifact, ensuring faster deployment times and reducing the risk of errors associated with manual Git interactions.

**Lazy Loading for EZ Commit Data Tables**\
The EZ Commit process now includes lazy loading for metadata components when using the Auto Draft functionality. Initially, only necessary data is loaded, with additional data fetched as the user scrolls or navigates through the table. This ensures a more efficient and responsive experience.

**Lazy Loading in Package Manifest and Commit Template** \
Lazy loading has also been implemented in the Package Manifest and Commit Template screens and the Selected and Deleted tabs, enhancing performance and responsiveness across these areas.

A visual indicator has been added during the loading process, ensuring users are informed while additional data loads, without any noticeable delays or interruptions to the user experience.

**Third-Party Library Upgrades** \
Third-party libraries have been upgraded in the following repositories to ensure compatibility, security, and performance improvements:

1. Rabit Dependencies

{% file src="../../../../.gitbook/assets/Rabit_Dependencies_24.10.22.txt" %}

2. AutoRABIT Dependencies

{% file src="../../../../.gitbook/assets/AutoRABIT_Dependencies_24.10.22.txt" %}

3. AR Agent Dependencies

{% file src="../../../../.gitbook/assets/AR_Agent_Dependencies_24.10.22.txt" %}

By streamlining the selective deployment process, this improvement enhances efficiency and contributes to a more reliable release management workflow.

These updates bring the latest enhancements and fixes from external libraries, improving overall stability across the platform.

&#x20;
