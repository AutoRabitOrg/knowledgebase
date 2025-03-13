# Release Notes 22.3

### New Features <a href="#new-features" id="new-features"></a>

#### 1. Comparison branches for Salesforce projects <a href="#1-comparison-branches-for-salesforce-projects" id="1-comparison-branches-for-salesforce-projects"></a>

Added the ability to add comparison branches to a Salesforce project in this release.

Key characteristics to look for:

* The comparison of issues
* The transfer of issue resolutions to the main branch of the Salesforce project.

For more information, see [Understanding branches for Salesforce project](https://knowledgebase.autorabit.com/codescan/docs/understanding-branches-for-salesforce-project).

#### 2. New nCino rules <a href="#2-new-ncino-rules" id="2-new-ncino-rules"></a>

Below are the nCino related rules added to the existing **Apex/Salesforce Metadata** rule sets and are tagged as **“ncino-goldstandard.”**

* **Process Builder Must Reference Product:** For general automation and validation best practices, associate actions in the system to a product line, product type, or product feature. Depending on how widespread the automation is, this ensures that follow-on phases for new lines of business have limited rework
* **Workflow Must Reference Product:** For general automation and validation best practices, associate actions in the system to a product line, product type, or product feature
* **Validation Rule Must Reference Product:** For general automation and validation best practices, associate actions in the system to a product line, product type, or product feature
* **System Bypass Logic - Workflow Rules:** This rule is required in custom workflow rules for integration users
* **System Bypass Logic - Validation Rules:** This rule is required in custom validation rules for integration users.

#### 3. Compute Engine parallel processing <a href="#3-compute-engine-parallel-processing" id="3-compute-engine-parallel-processing"></a>

This April's CodeScan cloud release includes the Compute Engine parallel processing capability. The key benefit is that it allows multiple analysis jobs to run in parallel in a fluid manner, reducing analysis job duration during peak usage and thereby improving user experience.

#### SonarQube compatible <a href="#sonarqube-compatible" id="sonarqube-compatible"></a>

CodeScan self-hosted is now compatible with **SonarQube™ 8.9** and **SonarJS 6.2+**. For more information, see [Installing CodeScan Self-Hosted](https://knowledgebase.autorabit.com/codescan/docs/codescan-self-hosted)

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### 1. Enhanced log report <a href="#1-enhanced-log-report" id="1-enhanced-log-report"></a>

The log report is now better than before. View your project analysis job's detailed log report, which includes the reasons for failed jobs.

#### 2. CodeScan integration with Github <a href="#2-codescan-integration-with-github" id="2-codescan-integration-with-github"></a>

In this release, the CodeScan integration with GitHub actions has been improved. When working on Github actions, the report generation feature has been included, which displays accurate findings based on analysis.

### Improvements <a href="#improvements" id="improvements"></a>

Minor performance, bug fixes, and security improvement can also be observed in the CodeScan portal.

### Bugs fixed <a href="#bugs-fixed" id="bugs-fixed"></a>

* Fixed a minor bug where the scheduled Salesforce jobs were not running in an instance because of several hardcoded values in the product sources.
* Fixed an issue where the project analysis job took a long time to accomplish and displayed the "Job took too long" error in some instances.
