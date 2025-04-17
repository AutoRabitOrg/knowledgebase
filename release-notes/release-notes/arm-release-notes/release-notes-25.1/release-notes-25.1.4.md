# Release Notes 25.1.4

## ARM Release Notes 25.1.4

**Release Date: 17 April 2025**

## Overview <a href="#overview" id="overview"></a>

This release focuses on streamlining the deployment process and improving reliability across the platform. OmniStudio deployments now handle dependencies more intelligently with Max Depth -1, ensuring a smoother experience from retrieval to deployment. Conflict resolution has been made more precise, avoiding issues like content bleed between files, and users can now seamlessly retry failed merges without losing progress. Improvements to Org Sync and Admin settings make it easier to spot differences and manage roles in real time, while enhancements to file comparison and commit labeling bring greater clarity and control to the deployment workflow.

### **Bug Fixes and Improvements** <a href="#bug-fixes-and-improvements" id="bug-fixes-and-improvements"></a>

* **Max Depth -1 Support for OmniStudio Deployment**\
  Deployments using Max Depth -1 now correctly retrieve and include all dependent components such as IntegrationProcedure, DataRaptor, Document, and VlocityUiTemplate. The retrieved dependencies are now properly reflected in the UI and included in the deployment to the target org. _Impacted Modules: Deployment (org → org). Support Case: #130644_
* **Improved Conflict Resolution Accuracy**\
  Resolved an issue where content from previously resolved files was being incorrectly appended to other files during conflict resolution. This fix ensures each conflicted file is processed independently, preventing errors such as duplicate labels during deployment. _Impacted Modules: EZ-Merge → Conflicts. Support Case: #136544_
* **Retry Commit for EZ-Merge After Failure**\
  The "Retry Commit" option is now available when a merge fails due to incorrect or unmapped credentials. The system correctly updates the merge status to "CommitPending," enabling users to retry the commit. This fix applies to new merges created after this release. _Impacted Modules: EZ-Merge, Dry run merge. Support Case: #134433_
* **Enhancement: Accurate Filtering in Org Sync**\
  The 'Exists in Source Only' filter in Org Sync now accurately reflects the actual number of differing metadata groups. With this fix, both the group count and displayed results are consistent and reliable. _Impacted Modules: Org Sync. Support Case: #135738_
* **Immediate Visibility of 'Skip Org Mapping' Option**\
  The 'Skip Org Mapping' permission is now immediately visible in the Roles tab after enabling 'Skip Mappings' on a user’s profile. Previously, a page refresh was required for the option to appear. This enhancement ensures the setting is saved and reflected instantly without additional user actions. _Impacted Modules: Admin. Support Case: #135229_
* **Whitespace Differences in File Diff View**\
  The File Diff tab now displays whitespace-only changes when comparing Apex Class files. Previously undetected space differences are now identified and shown, ensuring accurate comparison between source and destination files. _Impacted Modules: Org Sync and Deployments._
* **Vlocity Commit Label Filtering**\
  Commit labels associated with Vlocity metadata can now be filtered correctly using the commit label name in the merge screen. Previously created labels without commit type are also supported following a back-end migration fix. _Impacted Modules: VC → Change labels → Commit labels._
* **Support for Initial Commit in Revision Range Deployment**\
  Salesforce metadata changes from the initial commit are now included in the retrieve metadata screen when selected as the "From Revision" in a revision range deployment. This ensures changes from both the initial and target revisions are accurately reflected and deployed. _Impacted Modules: Custom Deployments - Revision range, single revision._
