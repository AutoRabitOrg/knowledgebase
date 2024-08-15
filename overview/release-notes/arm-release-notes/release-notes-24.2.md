# Release Notes 24.2

## Release 24.2 <a href="#improved-reporting-features-and-enhancements" id="improved-reporting-features-and-enhancements"></a>

**Release Date: 25 August 2024**

**Improved Reporting Features and Enhancements**

### **New Features**

* The new merge report is now included in the downloaded reports.
* Failure/Autoreject reasons have been added to the reports for emerge, commits, deployment, and CI build jobs, ensuring that if any jobs fail, the reason is included in the reports.

### **Enhancements**

* Extra fields have been correctly added to the current report.
* The name of "Latest Reports" has been changed to "Refresh Reports View."
* Users are now restricted from downloading more than six months of data.
* Post-download, headers, alignment, and naming conventions in Excel have been checked for readability and usability.

1. **Exclude Metadata in the Branching Baseline**\
   Users can now customize their baselines by excluding specific metadata. When selecting the "New Branching Baseline" option, a pop-up appears with available fields. A new "Exclude Metadata" checkbox allows users to choose what metadata to include or exclude from a scrollable or searchable list, with individual checkboxes for each item. Options to "Check All" or "Uncheck All" are available in both sections. Once selections are made, users can click "OK" and then "Run" to execute the process.
2. **Detailed Status Messages for Branching Baseline Process**\
   To improve transparency and usability, the branching baseline process now provides specific status messages for different failure scenarios. If some metadata members fail to commit, the status will display as "Partial Success" or "Failed." Users can download the files of the failed batch metadata XML files for better feasibility and view failure reasons, reducing troubleshooting time and improving overall efficiency.
3. **Updated UI and Pagination**\
   The UI for EZ-commit, deployments, and commit template screens has been updated with pagination for metadata-type tables. Users can now adjust the number of entries displayed per page.

**Pagination Availability:**

* **VC Commit:** Components selection screen.
* **Commit Template:** Components selection screen.
* **Deployments:** Retrieval screen and "Additional Metadata" section.

### Improvements <a href="#improvements" id="improvements"></a>

1. In this release, we revolutionized the system by converting all JSP pages into a RESTful API, enhancing modularity, scalability, and interoperability.
2. SOAP to REST services were upgraded.
3. Third-party libraries were upgraded.
