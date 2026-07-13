# Restore

## AutoRABIT Vault **Restore Job User Guide**

Restore data from a selected backup using EZ Restore or Selective Restore

## Purpose

The Restore workflow supports restoration of backed-up Salesforce data from a selected backup source. The flow begins by retrieving available backup records for a Salesforce org, then continues through either EZ Restore for a complete restore or Selective Restore for object-level, record-level, and field-level control.

The restore process also provides review controls, Salesforce automation options, progress tracking, and job-level results after the restore job is submitted.

**Guide scope:** This guide covers restore job creation from Backup as the restore source, including EZ Restore, Selective Restore, restore review, job submission, and restore history tracking.

## Open Restore and Retrieve Backup Details

The workflow starts from the Restore module. The Salesforce Orgs and Restore Source fields define the context for the restore list. When no restore jobs are available for the selected criteria, the list displays a No Data state while still keeping restore creation actions available.

![](<../../.gitbook/assets/Unknown image (12)>)

After selecting the Salesforce org, restore source, and configuration, Get Details retrieves the available backup records. The backup list displays the label, configuration, date and time, expiry date, record count, type, and status. A backup record is selected before starting a restore action.

![](<../../.gitbook/assets/Unknown image (1) (1)>)

## Start an EZ Restore

EZ Restore is used when the selected backup needs to be restored without manually refining objects, records, or fields. Before the restore summary opens, AutoRABIT Vault presents restore considerations that may affect job execution. These include Salesforce automation behavior, metadata size limits, inactive owners, and dependency requirements. Got It confirms the message and continues the restore flow.

![](<../../.gitbook/assets/Unknown image (2) (1)>)

The Restore Summary opens with the generated restore label, batch size, email notification recipient, and Salesforce Automations controls. The summary also lists the selected data scope. Automation options allow restore execution to disable or adjust selected Salesforce behaviors during processing, such as workflows, validation rules, triggers, flows, and Bulk API serial mode. Restore Now submits the job.

![](<../../.gitbook/assets/Unknown image (3) (1)>)

After submission, AutoRABIT Vault starts creating the restore job and displays a processing state. The restore action remains in progress until the job record is created and made available in the restore history list.

![](<../../.gitbook/assets/Unknown image (4) (1)>)

Once the restore job is created, AutoRABIT Vault displays a confirmation message. OK closes the message and returns to the restore list.

![](<../../.gitbook/assets/Unknown image (5) (1)>)

## Monitor the Restore Job

The restore history list shows the submitted restore job with its label, date and time, duration, success records, failed records, status, and available actions. While the job is running, the status indicator shows progress, and the action area provides job-level options such as summary or log access when available.

![](<../../.gitbook/assets/Unknown image (6) (1)>)

As processing continues, the status and action indicators update on the same restore history list. The page can be refreshed to check the latest job state.

![](<../../.gitbook/assets/Unknown image (7) (1)>)

When the job completes, the restore history shows the final duration, successful record count, failed record count, and completed status. The completed job remains available for review through the actions column.

![](<../../.gitbook/assets/Unknown image (8) (1)>)

## Start a Selective Restore

Selective Restore begins from the same backup retrieval flow. The backup record is selected, and Selective Restore opens the data selection workflow for controlled restore execution. This option supports a narrower restore scope by object, related objects, records, and fields.

![](<../../.gitbook/assets/Unknown image (9) (1)>)

The Data step lists the objects available in the selected backup. The Objects with records toggle limits the list to objects that contain backed-up records. The object row provides controls for schema review, child object inclusion, common child object selection, records, selection criteria, and selected fields. Review and Restore becomes available after the required restore scope is selected.

![](<../../.gitbook/assets/Unknown image (10) (1)>)

## Review Object Relationships

The schema view presents the selected object and its related objects. Search Objects helps locate related objects, and Search Direction controls whether parent, child, or both relationship directions are shown. Related objects can be expanded and selected as needed before saving the relationship selection.

![](<../../.gitbook/assets/Unknown image (11) (1)>)

Include All Child Objects marks child object inclusion for the selected object. The Common Child Objects control identifies child objects that can be included as part of the restore scope. These relationship controls help ensure dependent data is available when the restore job runs.

![](<../../.gitbook/assets/Unknown image (12) (1)>)

## Refine Records and Fields

The Records option opens the record selection scope for the selected object. When All is selected, all available records for the object are included in the restore scope. This keeps the object restore broad while still allowing the overall job to remain selective.

![](<../../.gitbook/assets/Unknown image (13)>)

The record selection dialog lists records for the selected object and provides filtering controls. Columns, operator, search text, file-based input, pagination, and view controls support narrowing the record set. Apply saves the selected record scope, and Cancel exits without applying changes.

![](<../../.gitbook/assets/Unknown image (14)>)

The Selected Fields option controls which fields are restored for the selected object. When All is selected, all available fields are included in the restore scope.

![](<../../.gitbook/assets/Unknown image (15)>)

The field mapping dialog lists source fields and corresponding mapping fields. Field selections can be searched, reset, adjusted, and applied. Required identity fields remain protected where applicable.

![](<../../.gitbook/assets/Unknown image (16)>)

## Review and Create the Selective Restore Job

After object, relationship, record, and field selections are finalized, Review and Restore opens the final restore submission flow. AutoRABIT Vault again displays restore considerations before the summary step. The message reinforces validation, automation, size limit, inactive owner, and dependency considerations that may affect restore success.

![](<../../.gitbook/assets/Unknown image (17)>)

![](<../../.gitbook/assets/Unknown image (18)>)

The Restore Summary confirms the selected restore scope, generated restore label, batch size, email notification recipient, and Salesforce Automations settings. The Data section summarizes the selected object and indicates whether all fields and records are included. Restore Now submits the selective restore job.

![](<../../.gitbook/assets/Unknown image (19)>)

AutoRABIT Vault confirms successful restore job creation after submission. The confirmation message closes with OK and returns to the restore history list.

![](<../../.gitbook/assets/Unknown image (20)>)

The restore history list shows the latest restore jobs and their processing outcomes. Completed rows display duration, success records, failed records, status, and job actions for follow-up review.

![](<../../.gitbook/assets/Unknown image (21)>)

## Result

At the end of the workflow, AutoRABIT Vault creates a restore job from the selected backup source. EZ Restore restores the selected backup using the full available scope, while Selective Restore creates a controlled restore job based on object, relationship, record, and field selections. The restore history provides visibility into progress, completion status, record counts, failures, and job-level actions.
