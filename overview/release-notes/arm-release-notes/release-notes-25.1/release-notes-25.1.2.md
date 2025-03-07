# Release Notes 25.1.2

## ARM Release Notes 25.1.2

**Release Date: 09 March 2025**

This release introduces **Checkmarx One Integration**, enabling users to perform security scans within ARM using Checkmarx One alongside existing Static Code Analysis tools.

Additionally, we have addressed multiple bug fixes and enhancements, including improved support for **PLATFORMEVENTCHANNELMEMBER** in destructive commits, enhanced **merge conflict detection for layouts**, and more reliable **duplicate resolution for profiles**. Security and stability improvements include **fully hiding API tokens after creation**, ensuring **correct project mapping for CodeScan in CI jobs**, and providing **consistent permission set deployments in Commit Label deployments**.

### New Feature

*   **Checkmarx One Integration**

    Users can now integrate Checkmarx One as a Static Code Analysis tool within ARM. This allows security scans to be performed using Checkmarx One alongside other existing tools, providing a scalable and fully managed security solution for cloud-native and DevOps teams.

### Bug Fixes and Improvements

*   **Improved Support for PLATFORMEVENTCHANNELMEMBER in Destructive Commits**

    ARM supports the destructive commit of **PLATFORMEVENTCHANNELMEMBER** metadata, ensuring seamless deletion and replacement of platform events without file diff errors. _Impacted Modules: Destructive changes, VC, Deployments, CI Jobs. Support Case #131023_
*   **Enhanced Merge Conflict Detection for Layouts**

    ARM reliably detects merge conflicts for layout metadata, including files with special characters in their names, ensuring a smoother and more accurate merge process. _Impacted Module: EZ-Merge. Support Case: #130985_
*   **Improved Duplicate Resolution for Profiles**

    ARM ensures stable conflict resolution for profiles by preventing errors caused by commented code on a new line. Users can click on files in the resolve duplicate screen without encountering IndexOutOfBounds exceptions. _Impacted Module: EZ-Merge duplicates resolution scenario. Support Case #130975_
*   **Improved Security for API Tokens**

    API tokens are now fully hidden after their initial creation and display, ensuring they are no longer exposed in network requests. This enhances security by preventing unauthorized access through browser developer tools. _Impacted Module: API Token creation._ _Support Case #131377_
*   **Correct Project Mapping for CodeScan in CI Jobs**

    ARM ensures that CodeScan projects are correctly linked to the scanned Salesforce org in CI jobs. The mapping issue causing a null project name has been resolved, ensuring accurate project creation and association. _Impacted Module: CI Job Build Logs. Support Case: #132391_
*   **Improved Commit Label Deployment for Permission Sets**

    ARM ensures consistent and accurate deployment of permission sets during Commit Label deployments. The **Ignore Missing Visibility** setting behaves as expected, and redeployments correctly generate a new deployment package instead of reusing the initial one. _Impacted Module: Commit Label. Support Case: #131711_

## nCino + Data Loader Improvements

**Release Date: 9 March 2025**

See the Release Notes for [nCino + Data Loader](https://knowledgebase.autorabit.com/overview/release-notes/ncino-release-notes/release-notes-25.1#ncino--data-loader-25.1.2-release-notes) improvements.
