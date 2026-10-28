# Restore User Guide

## AutoRABIT Vault Restore Job User Guide

Restore data from a selected backup using EZ Restore or Selective Restore

## Purpose

The Restore workflow supports restoration of backed-up Salesforce data from a selected backup source. The flow begins by retrieving available backup records for a Salesforce org, then continues through either EZ Restore for a complete restore or Selective Restore for object-level, record-level, and field-level control.

The restore process also provides review controls, Salesforce automation options, progress tracking, and job-level results after the restore job is submitted.

{% stepper %}
{% step %}
### Open Restore Jobs

Select Restore from the left navigation.

Review the Salesforce Org and Backup configuration displayed above the Restore Jobs table.

Select Create Restore Job to begin a restore.

<figure><img src="../../../.gitbook/assets/image (3158).png" alt=""><figcaption></figcaption></figure>

&#x20;                              _Restore Jobs page when no restore jobs are available_

<figure><img src="../../../.gitbook/assets/image (3159).png" alt=""><figcaption></figcaption></figure>

&#x20;                              _Restore Jobs page with existing restore jobs_
{% endstep %}

{% step %}
## Create a restore job

Selecting Create Restore Job opens the restore configuration flow. Available backup configurations and backup jobs are loaded for the selected Salesforce Org.

<figure><img src="../../../.gitbook/assets/image (3160).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore configuration loading_
{% endstep %}

{% step %}
### Select backup data

Selecting Create Restore Job opens the restore configuration flow. Available backup configurations and backup jobs are loaded for the selected Salesforce Org.

Select the required Backup configuration entries.

Review the available backup jobs in the table.

Select one or more backup jobs for the restore.

The backup list displays the backup Label, Job Info, Date/Time, Expiry Date, Records, and Status. Restore actions remain unavailable until at least one backup job is selected.

<figure><img src="../../../.gitbook/assets/image (3161).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Available backup jobs before selection_

<figure><img src="../../../.gitbook/assets/image (3162).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Selected backup jobs with restore actions enabled_
{% endstep %}

{% step %}
### Start an EZ Restore

EZ Restore applies the selected backup data through a streamlined restore configuration. Select EZ Restore after the required backup jobs are selected.

A warning appears before the restore settings are displayed. Review the conditions that can affect restore processing, then select Got it to continue.

{% hint style="warning" %}
* Active triggers, process builders, workflows, flows, and validation rules can contribute to restore failures.
* Salesforce limits the maximum uncompressed metadata size per job to 500 MB. An appropriate batch size is required when metadata exceeds the limit.
* Inactive owners in Salesforce can contribute to restore failures.
* Missing dependencies, including required fields, can contribute to restore failures. Required dependencies should be included in the restore job.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (3163).png" alt=""><figcaption></figcaption></figure>

&#x20;                                      _Restore warning displayed before EZ Restore configuration_
{% endstep %}

{% step %}
### Configure the Restore Summary

The Restore Summary displays the destination Org Name and provides the restore label, batch size, Salesforce automation controls, and processing options.

Review or update the Restore Label.

Enter the Batch Size. The displayed maximum is 9999.

Enable the required Salesforce Automations controls.

Enable the required processing options.

Select Restore Now to submit the restore job.

#### Available restore options

| **Option**                      | **Purpose shown in the restore configuration**                           |
| ------------------------------- | ------------------------------------------------------------------------ |
| Disable workflows               | Controls workflow execution during the restore.                          |
| Disable triggers                | Controls trigger execution during the restore.                           |
| Disable flows                   | Controls flow execution during the restore.                              |
| Disable validation rules        | Controls validation-rule execution during the restore.                   |
| Ignore failed records           | Allows restore processing to continue when records fail.                 |
| Override data with blank values | Allows blank values from the restore data to replace destination values. |
| Enable serial mode for Bulk API | Runs Bulk API processing in serial mode when enabled.                    |

<figure><img src="../../../.gitbook/assets/image (3164).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore Summary before submission_

<figure><img src="../../../.gitbook/assets/image (3165).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore submission in progress_
{% endstep %}

{% step %}
### Monitor restore execution

After submission, the restore job appears in Restore Jobs. The Actions and Status area reflects the current job state and provides access to job details.

<figure><img src="../../../.gitbook/assets/image (3166).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore job added to the Restore Jobs table_

<figure><img src="../../../.gitbook/assets/image (3167).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore job processing status_

#### Review Job Details

Open the job details to track the restore stages and record-level progress. The execution flow moves through Connecting to Salesforce, Selecting objects & records, Restoring records to Salesforce, Processing related records, and Restore complete.

Live Activity displays Successful Objects, Failed Objects, Duration, Successful Records, and Failed Records. Object progress appears below the summary metrics.

<figure><img src="../../../.gitbook/assets/image (3168).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Job Details during restore processing_

<figure><img src="../../../.gitbook/assets/image (3169).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Job Details after successful completion_
{% endstep %}
{% endstepper %}

## Review job status and available actions

The Restore Jobs table retains completed and failed restore jobs. Success and failure indicators appear in Actions and Status together with actions for further review. A retry action is available for a failed restore job where shown.

<figure><img src="../../../.gitbook/assets/image (3170).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore Jobs table showing completed and failed results_

<figure><img src="../../../.gitbook/assets/image (3171).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Completed Job Details and Live Activity_

### View Restore Info

Select the Info action to review the configuration saved with the restore job.

<figure><img src="../../../.gitbook/assets/image (3172).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Info action in the Restore Jobs table_

Restore Info displays the backup labels and restore settings, including validation rules, workflows, triggers, flows, Bulk API mode, failed-record handling, duplicate-record handling, blank-value handling, and email notifications.

<figure><img src="../../../.gitbook/assets/image (3173).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore Info details_

## Review the Restore Summary

Select the Summary action to review object-level restore results. The summary shows Success and Failure counts for each object, together with Download and Error columns.

<figure><img src="../../../.gitbook/assets/image (3174).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Summary action in the Restore Jobs table_

<figure><img src="../../../.gitbook/assets/image (3175).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Object-level Restore Summary_

### Review Detailed Logs

Select Detailed Logs to open the completed job directly on the Detailed Logs tab. The log view supports log search and provides Download full log for offline review.

<figure><img src="../../../.gitbook/assets/image (3176).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Detailed Logs action in the Restore Jobs table_

<figure><img src="../../../.gitbook/assets/image (3177).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Detailed Logs for a completed restore job_

## Identify restore jobs

When a restore label is truncated in the table, hover over the label to display the complete value. The full label helps distinguish restore runs with similar prefixes.

<figure><img src="../../../.gitbook/assets/image (3178).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Complete restore label displayed from a truncated table value_

### Reopen object results

The Summary action remains available after completion and can be reopened to review object-level success and failure results or access the available download.

<figure><img src="../../../.gitbook/assets/image (3179).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                    _Restore Summary reopened from the Restore Jobs table_

## Completion checks

* Confirm that the restore job reaches Restore complete.
* Review Successful Records and Failed Records in Job Details.
* Open Restore Summary when object-level results require review.
* Open Detailed Logs when execution details or error investigation is required.
