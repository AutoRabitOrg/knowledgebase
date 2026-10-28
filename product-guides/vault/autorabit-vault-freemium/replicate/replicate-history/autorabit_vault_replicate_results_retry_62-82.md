# AutoRABIT\_Vault\_Replicate\_Results\_Retry\_62 82

AutoRABIT Vault - Replication Information, Results, and Retry

**Continuation of: AutoRABIT Vault - Replicate History and Job Monitoring**

This guide continues from the Replicate History job-monitoring workflow. With Replicate History open and the relevant job identified, the next actions are to review replication information and results, inspect masking details, and retry replication when required. It can also be followed independently from Replicate > History.

## Continuing from job monitoring

From Replicate > History, locate the replication entry reviewed in the preceding guide. The Actions and Status column provides access to replication information, summaries, detailed logs, and retry actions.

## Opening replication information

Select Info for the required entry. The Replicate Info window opens with the Info tab, displaying the replication label and the configuration options used for the execution.

## Reviewing included object information

Switch to the Data tab in Replicate Info to review the selected objects, record counts, child-object inclusion, and applicable object-level details.

## Opening the replication summary

Return to Replicate History and select Summary for the required job.

## Reviewing object-level results

In Replicate Summary, review the objects and their Success and Failure counts. Use the Download results action when the generated result file is required.

## Opening masking information

Select View masking info in Replicate Summary for an object that provides masking information.

## Reviewing masking rules

In Masking Info, inspect the masking rule name, rule type, field type, and masking style for the relevant object.

## Filtering the summary

Use the available summary filter to narrow the view to Successful Objects or Failed Objects.

## Opening detailed logs from History

Select Detailed Logs from the relevant history row to review the execution messages without navigating through the other summary screens.

## Inspecting execution messages

Review the chronological entries in Detailed Logs. Select Download Full Log when a local copy of these messages is required.

## Starting a replication retry

Return to the Replicate History table. Select Retry for the required job to open the retry configuration.

## Reviewing retry settings

In Retry Replicate Summary, confirm the destination org and replication label. Review the available Salesforce automation switches and other execution options before proceeding.

## Submitting the retry

Enter or review the retry batch size and the available execution settings. Select Replicate Now to start the replication retry.

## Confirming that replication starts

Return to Replicate History and review the status indicator for the newly started execution.

## Monitoring retry progress

Use the status and actions for the retry job to track execution. Open the job details when more detailed progress information is required.

## Reopening the replication summary

Select the relevant replication entry or Summary action to inspect the results after the retry operation.

## Downloading summary results

In Replicate Summary, review the updated Success and Failure counts and select Download results to obtain the available output.

## Opening updated masking information

Select View masking info from the replication summary to inspect the masking rules associated with the job.

## Viewing a masking rule

In Masking Info, select View for the required masking rule to open its field-level details.

## Reviewing masking-rule details

Review the field names and their masking styles in Masking Rule Details. Close the dialog to return to the masking-rule list.

## Customizing history columns

Return to Replicate History and open Columns. Select or clear the available column checkboxes to control which information appears in the history table.

## Completing the review

The Replicate History table remains the entry point for reviewing job statuses, returning to logs and summaries, or monitoring a subsequent retry.
