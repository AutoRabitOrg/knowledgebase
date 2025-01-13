# Release Notes 24.4

## nCino + Data Loader 24.4.5 Release Notes

**Release Date: 13 January 2025**

* **Group Jobs Stability:** Fixed an issue to ensure group jobs execute without failure.
* **Import Process Stability:** Resolved an issue to prevent failures during the import process.
* **Rollback Functionality:** Fixed the rollback functionality on the nCino UAT instance to ensure it works as expected.

## nCino + Data Loader 24.4.4 Release Notes

**Release Date: 13 December 2024**

* **Revision Range:** Improved the checkout logic for the revision range to enhance performance.
* **Fixed Query Logic:** Resolved an issue with adding conditions to queries.
* **Template Failure:** Fixed the issue causing failures in the "nCino Template."
* **Publish Icon:** Ensured the publish icon is visible for "nCino Customers" on the "Feature Template Manage" screen.

## nCino 24.4.3 Release Notes

**Release Date: 24 November 2024**

The following enhancements ensure compliance, improve flexibility, and streamline the user experience.&#x20;

* **CI Job Backup:** CI job rollback backups have been further streamlined and organized to ensure compliance standards are met.
* **nCino RBC Deployment Options:** Customers can now verify and configure the required `externalID` during RBC deployments, improving flexibility and control.
* **Trigger Build on Commit:** Scheduling conflicts are now resolved when the "Trigger Build on Commit" option is enabled, ensuring seamless automation.
* **nCino Step Logs**: nCino step logs have been enhanced to provide additional details, improving visibility and troubleshooting capabilities.

## nCino 24.4.2 Release Notes

**Release Date: 10 November 2024**

The following enhancements include an upgrade for version compatibility and fixes to improve user experience and streamline performance.

* **Salesforce Winter '62 Compatibility**: Upgraded nCino to support the latest Salesforce Winter '62 release.
* **RBC Fixes**: Resolved issues with RBC deployments and commits for improved reliability.
* **Feature Version Loading**: Fixed loading issues with the Feature Version page for a smoother experience.

## nCino & Data Loader Release Notes 24.4.1

**Release Date: 27 October 2024**

The following features, enhancements, and fixes have been implemented to improve user experience and streamline performance.

*   **Auto Trigger nCino Jobs**

    Enabling “Auto Trigger on Commit” in CI Jobs now automatically starts jobs with each new version control commit, streamlining workflows and eliminating manual triggers.
*   **Rollback Error**

    A rollback failed due to an issue with the selected baseline revision. Verify the baseline selection to proceed.
*   **OwnerID Record Error**

    The ID of the user who created the record will be retained in the destination records.
