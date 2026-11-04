# Replicate History

## AutoRABIT Vault - Replicate History and Job Monitoring

Replicate History provides access to the execution status, object activity, and detailed logs for replication jobs. This guide covers reviewing and monitoring replication from the history table.

{% stepper %}
{% step %}
### Opening Replicate History

Navigate to Replicate > History to review replication jobs. The history table identifies the source and destination orgs, configuration, record counts, and available job actions.

<figure><img src="../../../../.gitbook/assets/image (5458).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Reviewing the job list

Locate the required replication entry using the job label and configuration name. Review Success Records, Failure Records, and the indicators under Actions and Status.

<figure><img src="../../../../.gitbook/assets/image (5459).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Identifying the job status

Review the status indicator in the selected row before opening job details. The indicator reflects the current execution state.

<figure><img src="../../../../.gitbook/assets/image (5460).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Monitoring a running job

Select the job details action to open Job Details. The execution timeline indicates the current stage, while the record metrics and object progress provide a detailed view of processing.

<figure><img src="../../../../.gitbook/assets/image (5461).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Reviewing completed execution

For a completed job, review the completed stages and final metrics in Job Details. A completed status can still contain failed records, which are identified separately.

<figure><img src="../../../../.gitbook/assets/image (5462).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Recognizing subsequent job activity

Return to Replicate History after initiating another replication. A notification confirms that the configuration is saved and replication is started.

<figure><img src="../../../../.gitbook/assets/image (5463).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Monitoring the new execution

Review the status indicator of the newly started replication in the history table. Open the corresponding job to inspect its progress.

<figure><img src="../../../../.gitbook/assets/image (5464).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Checking progress from History

Use the job status and action icons in Replicate History to identify active processing and to open additional information.

<figure><img src="../../../../.gitbook/assets/image (5465).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Inspecting an active replication

In Job Details, review the highlighted execution stage and the duration. The object-level progress bar indicates processing progress for the listed object.

<figure><img src="../../../../.gitbook/assets/image (5466).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Identifying failed execution

Review the failure indicator in Replicate History. A failed job can be opened to examine the objects and records associated with the failure.

<figure><img src="../../../../.gitbook/assets/image (5467).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Filtering failed objects

Open Job Details and select the Failed Objects count to restrict the object list to objects reporting failures.

<figure><img src="../../../../.gitbook/assets/image (5468).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Clearing the object filter

Clear the failed-object filter to return to the full object list and resume review of the job execution details.

<figure><img src="../../../../.gitbook/assets/image (5469).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Expanding object activity

Expand the relevant object entry under Live Activity to inspect the individual execution events associated with that object.

<figure><img src="../../../../.gitbook/assets/image (5470).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Collapsing object activity

Collapse the activity entry after reviewing the event details to return to the concise object summary.

<figure><img src="../../../../.gitbook/assets/image (5471).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Searching job activity

Use the search control within Job Details to locate relevant activity or object information. Choose the applicable search option when available.

<figure><img src="../../../../.gitbook/assets/image (5472).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Reviewing the filtered results

Inspect the resulting object or activity list to identify the execution information associated with the search.

<figure><img src="../../../../.gitbook/assets/image (5473).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Opening detailed logs

Switch from Live Activity to Detailed Logs to review the chronological execution messages for the selected replication job.

<figure><img src="../../../../.gitbook/assets/image (5474).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Downloading job logs

Select Download Full Log from Detailed Logs when a copy of the execution messages is required for further review.

<figure><img src="../../../../.gitbook/assets/image (5475).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Returning to available job actions

Close Job Details to return to Replicate History. The row action icons provide access to additional information and follow-up operations, covered in the next guide.

<figure><img src="../../../../.gitbook/assets/image (5477).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Opening replication information

Select Info for the required entry. The Replicate Info window opens with the Info tab, displaying the replication label and the configuration options used for the execution.

<figure><img src="../../../../.gitbook/assets/image (5478).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reviewing included object information

Switch to the Data tab in Replicate Info to review the selected objects, record counts, child-object inclusion, and applicable object-level details.

<figure><img src="../../../../.gitbook/assets/image (5479).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Opening the replication summary

Return to Replicate History and select Summary for the required job.

<figure><img src="../../../../.gitbook/assets/image (5480).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reviewing object-level results

In Replicate Summary, review the objects and their Success and Failure counts. Use the Download results action when the generated result file is required.

<figure><img src="../../../../.gitbook/assets/image (5481).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Opening masking information

Select View masking info in Replicate Summary for an object that provides masking information.

<figure><img src="../../../../.gitbook/assets/image (5482).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reviewing masking rules

In Masking Info, inspect the masking rule name, rule type, field type, and masking style for the relevant object.

<figure><img src="../../../../.gitbook/assets/image (5483).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Filtering the summary

Use the available summary filter to narrow the view to Successful Objects or Failed Objects.

<figure><img src="../../../../.gitbook/assets/image (5484).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Opening detailed logs from History

Select Detailed Logs from the relevant history row to review the execution messages without navigating through the other summary screens.

<figure><img src="../../../../.gitbook/assets/image (5485).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Inspecting execution messages

Review the chronological entries in Detailed Logs. Select Download Full Log when a local copy of these messages is required.

<figure><img src="../../../../.gitbook/assets/image (5486).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Starting a replication retry

Return to the Replicate History table. Select Retry for the required job to open the retry configuration.

<figure><img src="../../../../.gitbook/assets/image (5487).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reviewing retry settings

In Retry Replicate Summary, confirm the destination org and replication label. Review the available Salesforce automation switches and other execution options before proceeding.

<figure><img src="../../../../.gitbook/assets/image (5488).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Submitting the retry

Enter or review the retry batch size and the available execution settings. Select Replicate Now to start the replication retry.

<figure><img src="../../../../.gitbook/assets/image (5489).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Confirming that replication starts

Return to Replicate History and review the status indicator for the newly started execution.

<figure><img src="../../../../.gitbook/assets/image (5490).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Monitoring retry progress

Use the status and actions for the retry job to track execution. Open the job details when more detailed progress information is required.

<figure><img src="../../../../.gitbook/assets/image (5491).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reopening the replication summary

Select the relevant replication entry or Summary action to inspect the results after the retry operation.

<figure><img src="../../../../.gitbook/assets/image (5492).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Downloading summary results

In Replicate Summary, review the updated Success and Failure counts and select Download results to obtain the available output.

<figure><img src="../../../../.gitbook/assets/image (5493).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Opening updated masking information

Select View masking info from the replication summary to inspect the masking rules associated with the job.

<figure><img src="../../../../.gitbook/assets/image (5494).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Viewing a masking rule

In Masking Info, select View for the required masking rule to open its field-level details.

<figure><img src="../../../../.gitbook/assets/image (5495).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Reviewing masking-rule details

Review the field names and their masking styles in Masking Rule Details. Close the dialog to return to the masking-rule list.

<figure><img src="../../../../.gitbook/assets/image (5496).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Customizing history columns

Return to Replicate History and open Columns. Select or clear the available column checkboxes to control which information appears in the history table.

<figure><img src="../../../../.gitbook/assets/image (5497).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
## Completing the review

The Replicate History table remains the entry point for reviewing job statuses, returning to logs and summaries, or monitoring a subsequent retry.
{% endstep %}
{% endstepper %}
