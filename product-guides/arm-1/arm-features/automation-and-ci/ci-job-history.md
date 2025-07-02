# CI Job History

CI Job History

{% hint style="info" %}
For the best viewing experience, set your browser zoom level to 80% in Chrome or Firefox.
{% endhint %}

The CI Job History page allows you to:

Create a new CI job

Trigger a new build for an existing CI job

Access build and deployment details, SCA reports, and more

<figure><img src="../../../../.gitbook/assets/image (1152).png" alt="CI Job History UI"><figcaption></figcaption></figure>

Deployment Workspace On the right-hand side of the CI Job History page, the Deployment Workspace displays builds in the deployment queue and the reasons for their queue status.

<figure><img src="../../../../.gitbook/assets/image (1153).png" alt="Deployment Workspace"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1154).png" alt="Deployment Queue - Screenshot" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1155).png" alt="Deployment Queue Details"><figcaption></figcaption></figure>

Common Queue Messages and Required Actions: Parallel processing limit reached: Wait for current processes to complete.

Agent unavailable: Verify agent connectivity.

Deployment to same destination in progress: Wait for current deployment to finish.

Previous build in progress or queued: Wait until it completes or clears.

Build Details Each Build displays the following information:

<figure><img src="../../../../.gitbook/assets/image (1156).png" alt="Build Details Overview"><figcaption></figcaption></figure>

Build Label: Name of the build.

Build Date: Timestamp of when the build started.

Build Number: Listed in reverse chronological order.

Abort (in-progress only): Stop a running CI job deployment and test execution.

Build Information : View or download build details (ZIP format).

Build Status: Indicates if the build is successful, in progress, or failed. Build logs are downloadable.

Warnings, Changes, Check-ins, and SCA Hover over the icon in Build Details to access additional build data:

<figure><img src="../../../../.gitbook/assets/image (1159).png" alt="Hover Options Overview"><figcaption></figcaption></figure>

Warning Displays build-time warnings. If none, a "No Warnings Found" message appears.

Changes Metadata Changes: Lists all modified metadata in the build.

<figure><img src="../../../../.gitbook/assets/image (1160).png" alt="Metadata Changes Tab" width="563"><figcaption></figcaption></figure>

Destructive Changes: Shows components marked for deletion. (Learn More)

<figure><img src="../../../../.gitbook/assets/image (1161).png" alt="Destructive Changes Tab" width="563"><figcaption></figcaption></figure>

File Changes: Displays added/modified files with line-level diffs. Red = deleted, Green = added/updated.

<figure><img src="../../../../.gitbook/assets/image (1162).png" alt="File Changes Tab" width="563"><figcaption></figcaption></figure>

Individual file diffs are downloadable:

<figure><img src="../../../../.gitbook/assets/image (1163).png" alt="Download Diff Icon" width="347"><figcaption></figcaption></figure>

Check-ins Displays a summary of revisions included in the build:

<figure><img src="../../../../.gitbook/assets/image (1164).png" alt="Check-in Summary" width="563"><figcaption></figcaption></figure>

Important Notes: Diffs for large files may only be downloadable, not viewable in UI.

Excluded metadata and unrelated folders (in SFDX single-source builds) are not shown in File Changes.

Older builds may not display File Changes tab.

Recent builds include both File Changes and Check-ins.

For GIT, deltas use git diff. Lazy commits may cause discrepancies between Metadata Changes and Check-ins.

Builds between weekly GIT fixes may bind changes to a single HEAD revision.

Parent Revisions are blank for builds before 22.1.18-RELEASE.

Static Code Analysis (SCA) SCA is part of the secure development lifecycle, conducted during code review using tools like CodeScan, ApexPMD, and Checkmarx.

<figure><img src="../../../../.gitbook/assets/image (1165).png" alt="SCA Overview"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1166).png" alt="SCA Detail View" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1167).png" alt="Violation Highlights"><figcaption></figcaption></figure>

Click a file to view violations, and select a violation to jump to its corresponding line in the code preview panel.

Deployment Details

<figure><img src="../../../../.gitbook/assets/image (1168).png" alt="Deployment Details UI"><figcaption></figcaption></figure>

Deployment Status:

Icon Status ![](<../../../../.gitbook/assets/image (1169).png>) Validation successful ![](<../../../../.gitbook/assets/image (1170).png>) Validation failed Deployment successful Deployment failed

Deployment Log: View or download deployment log.

Quick Deploy: View or rerun quick deployment status.

Rollback:

Enabled by selecting Rollback when creating a CI job.

icon indicates validated rollback.

Re-run Rollback: Select metadata for rollback. Deleted components can be handled via destructive changes. Excluded metadata appears in the Rollback Log.

Deployment Reports Hover over the icon in Deployment Details to download:

Deployment Report:

Includes Dependency Analyzer for failed components.

Downloadable in Manifest (JSON) or XLS.

<figure><img src="../../../../.gitbook/assets/image (1175).png" alt="Dependency Analyzer"><figcaption></figcaption></figure>

Reports older than 30 days are unavailable.

Quick Deployment Report:

<figure><img src="../../../../.gitbook/assets/image (1176).png" alt="Quick Deployment Report"><figcaption></figcaption></figure>

Rollback History:

<figure><img src="../../../../.gitbook/assets/image (1177).png" alt="Rollback History"><figcaption></figcaption></figure>

Post Activities Displays post-deployment outcomes for various components:

Status CI Job Env Provisioning Data Loader Merge Jenkins Job Success Completed Success Completed Merged Success/Unstable Failed Not completed Not successful Not completed Not merged Other than Success/Unstable

Functional Tests View the percentage of test success/failure per build.

<figure><img src="../../../../.gitbook/assets/image (1178).png" alt="Functional Tests Summary"><figcaption></figcaption></figure>

Apex Tests (Coverage) View code coverage including test-executed classes, failed assertions, and overall coverage percentage.
