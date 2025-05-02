# Release Notes 25.2.3

## Release Notes 25.2.3

**Release Date:** **04 May 2025**

### **Overview** <a href="#overview" id="overview"></a>

This release of AutoRABIT ARM introduces key bug fixes and stability improvements to deployment label handling, CI job webhook executions, and user management across regions. Notably, a critical internal issue affecting metadata filtering during full deployments has been addressed. Additionally, issues related to saving users for countries without state-level details and CI job webhook failures have been resolved.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

**Issue with full Deployment - Previous Deployment Label type**\
A defect was identified when performing a full deployment using the “Previous Deployment Label” type, which inadvertently included all metadata members from the source organization, rather than only those associated with the selected label.
**Fix:** Updated deployment logic now ensures that only metadata within the selected label is included in the deployment.
**Impacted Modules:** Deployments

**Webhook Execution Failures in CI Jobs**\
Webhooks were not being executed during CI job runs due to limitations in DynamoDB.
**Fix:** Webhook invocation logic has been revamped to ensure reliable webhook execution in CI pipelines.
**Impacted Modules:** CI Jobs

**User Creation Failure – Countries Without States**\
An issue was reported where creating or editing users with countries that do not have states (e.g., Singapore, American Samoa, Andorra) failed to save the user details.**Fix:** Error handling and webhook invocation logic have been corrected to ensure reliable webhook execution in CI pipelines.
**Fix:** Validation logic has been updated to treat the state field as optional for applicable countries, ensuring successful user creation.
**Impacted Modules:** User Management
