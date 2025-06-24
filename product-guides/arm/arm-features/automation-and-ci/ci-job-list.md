CI Job List
{% hint style="info" %}
For optimal viewing, set your browser zoom level to 80% in Chrome or Firefox.
{% endhint %}

The CI Job List screen displays all CI jobs created in ARM, listed in reverse chronological order — the most recent jobs appear at the top.

<figure><img src="../../../../.gitbook/assets/image (1179).png" alt="CI Job List UI"></figure>
Jobs that have been deployed display the icon
, while jobs that have only been validated display
.

Filtering Options
Use the filters to refine your search for specific CI jobs.

<figure><img src="../../../../.gitbook/assets/image (1182).png" alt="Filtering Options UI"></figure>
Group By: Select a specific job group from the dropdown or type the group name. Choose All Groups to view jobs from all groups.

Job Name: Search by typing or selecting a job name from the dropdown.

Last Modified Date Range: Filter jobs by modification date. Defaults to the last 7 days. Additional options include:

Last 14 days

Last 30 days

Last 24 hours

Custom Range: Specify your own date and time range.

<figure><img src="../../../../.gitbook/assets/image (1183).png" alt="Date Range Filter" width="563"></figure>
Advanced Filter Options
:

<figure><img src="../../../../.gitbook/assets/image (1185).png" alt="Filter Panel" width="401"></figure>
Job Source Type:

Sandbox: Choose the Source Org. Select All to include all orgs.

Version Control: Choose the Source Repository and Source Branch. Select All to include all repos and branches.

<figure><img src="../../../../.gitbook/assets/image (1186).png" alt="Source Type Filters" width="563"></figure>
Destination Org: Select a specific org or choose All to include jobs targeting any destination org.

Additional Options
<figure><img src="../../../../.gitbook/assets/image (1187).png" alt="CI Job Actions" width="550"></figure>
Info: View job metadata including source/destination orgs, repositories, branches, timestamps, etc.

Clone: Create a new job using details from an existing job.

Edit: Modify job details. If a job is in progress:

A prompt appears on saving.

Selecting YES aborts the current job, saves changes, and redirects to the CI Jobs Result page.

Selecting NO discards changes.

<figure><img src="../../../../.gitbook/assets/image (1188).png" alt="Edit Job Prompt" width="332"></figure>
For Vlocity (FlexCard/OmniScript) deployments:

The destination org must be registered with OAuth. If it's registered with Standard, re-register with OAuth or deployment will fail. The following log message appears:

To deploy compiled versions of OmniScript and FlexCards, Please re-register your destination org with OAuth and update the Local Compilation key in the My Account section

Enable Local Compilation and enter a valid Access Key under My Account:

Missing key:

Deployment will be performed without local compilation due to the absence of Access Key of Vlocity's Private NPM Repository

Invalid key:

Deployment is completed without local compilation due to the incorrect Access Key of Vlocity's Private NPM Repository

<figure><img src="../../../../.gitbook/assets/image (1189).png" alt="Local Compilation Config" width="452"></figure>
Activate/Deactivate: Temporarily disable jobs without deleting them. Reactivate when needed. This prevents unintended builds without loss of job data.

Delete: Permanently remove the job. This action is irreversible.

{% hint style="info" %}
Important Notes on Deactivated CI Jobs:

Scheduled builds will not run.

Configured hooks will not be processed.

Build and deploy queues will be cleared.

API-triggered builds are disabled.

Edit and Clone options are disabled.

If selected during post-deployment, deactivated jobs can affect parent CI job configuration.

Triggering new builds for deactivated jobs is not allowed.
{% endhint %}

