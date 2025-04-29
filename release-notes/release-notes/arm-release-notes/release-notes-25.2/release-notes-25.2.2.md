# Release Notes 25.2.2

## Release Notes 25.2.2

**Release Date:** **27 April 2025**

### **Overview** <a href="#overview" id="overview"></a>

This release introduces significant enhancements to AutoRABIT’s ARM platform, focusing on enhanced metadata support, improved deployment accuracy, and optimized performance across CI workflows. Previously unsupported metadata types are now fully recognized in DX-based branching and deployment. Issues with redundant code coverage reports and performance bottlenecks in ALM item loading have been resolved. Significant improvements also include full profile permission coverage in EZ-Commit and enhanced metadata exclusion logic.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

**Support for New Metadata Types in DX Repo CI Deployments**\
Previously unsupported metadata types are now included in deployments created through DX repo-based branching. These include: `ApplicationSubtypeDefinition`, `BusinessProcessTypeDefinition`, `ConvIntelligenceSignalRule`, `ExplainabilityActionDefinition`, `ExpressionSetDefinitionVersion`, `ForecastingGroup`, and `PathAssistant`.\
**Impacted Modules:** CI Jobs (DX Branching & Deployments)

**Code Coverage Report Duplication Fixed**\
Resolved an issue where multiple code coverage reports were generated for the same sandbox. The back-end logic has been updated to ensure that only one report is created per sandbox.\
**Impacted Modules:** Code Coverage Reports

**Improved ALM Item Load Time in Commit/Merge Modules**\
Addressed severe performance lag when loading Azure ALM items after sprint selection. Switched to batch API calls for fetching work item data and states, reducing calls from thousands to single digits. Load time dropped from \~6 minutes to \~4 seconds for large sprints.\
**Impacted Modules:** Commit/Merge (ALM Integration with Azure)

**Full Profile Commit – Object Permissions & Tab Visibility Fixes**\
Fixed missing object permissions (Documents, Push Topics) and tab visibilities (Reports, Dashboards) in full profile commits during EZ-Commit. The package.xml generation logic now correctly includes all necessary metadata members.\
**Impacted Modules:** EZ-Commit, Profiles

**Metadata Exclusion Logic Improved – ExpressionSetDefinitionVersion**\
Corrected behavior in which `ExpressionSetDefinitionVersion` metadata was included in deployments, even when excluded. This enhancement enables precise control over metadata exclusions, particularly for workflows that require separate deployment flows (e.g., OmniStudio jobs).\
**Impacted Modules:** CI Jobs, Deployment

***

## nCino + Data Loader Release Notes 25.1.4

**Release Date: 27 April 2025**

Refer to the latest release notes published for nCino + Data Loader at [https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes](https://knowledgebase.autorabit.com/release-notes/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.4-release-notes).&#x20;

