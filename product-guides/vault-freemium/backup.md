# Backup

## Vault Backup Job Creation User Guide

_Create and start a backup job from an existing backup configuration_

## Purpose

Backup Job Creation allows a backup job to be started from the Backup module after the required Salesforce org, environment, and backup configuration are selected. The workflow opens the Start Backup dialog, confirms the backup details, starts the job, and displays the created backup record in the Backup Summary.

## Before Beginning

A source org and backup configuration must already be available. The Backup Jobs page uses the selected Salesforce Org, Environment, and Configurations values to display the related backup records and to start a new backup for the selected configuration.

![](<../../.gitbook/assets/Unknown image (247)>)

## Create a Backup Job

The Backup module opens on the Backup Jobs page. The page displays the selected Salesforce Org, Environment, and Configurations values at the top of the workspace. The Backup Summary table lists existing backup jobs for the selected configuration. When no backup has been created for the current selection, the table displays an empty state.

Selecting Backup Now opens the Start Backup dialog. Vault automatically generates a Backup Label and carries forward the selected configuration into the Configurations field. The dialog provides the review point before the backup job is started.

![](<../../.gitbook/assets/Unknown image (248)>)

The Configurations field supports selection or confirmation of the backup configuration that must be used for the job. After the configuration is selected, the Data section displays Full Backup as the backup type. The Exclude Deleted Records from Backups option remains available to control whether deleted records are excluded from the backup processing.

![](<../../.gitbook/assets/Unknown image (249)>)

## Start the Backup

Selecting Start Backup submits the backup request. During submission, the Start Backup button shows an in-progress state to indicate that Vault is processing the request and creating the backup job.

![](<../../.gitbook/assets/Unknown image (250)>)

After the request is accepted, Vault closes the dialog and displays a confirmation notification indicating that the backup has started. The Backup Summary refreshes with the created backup record. The record displays the backup label, configuration name, date and time, expiry date, duration, record count, API calls, data backup indicator, status, and available actions.

![](<../../.gitbook/assets/Unknown image (251)>)

## Result

The backup job is created for the selected configuration and becomes available in the Backup Summary. The status and supporting job details can be monitored from the same page, and the action icons provide access to the available job-level operations.

## Important Considerations

Backup jobs are created only for the currently selected Salesforce Org, Environment, and Configurations values.

The generated Backup Label can be reviewed before the job is started.

The Exclude Deleted Records from Backups option determines whether deleted records are excluded during backup processing.

The Backup Summary reflects the job after Vault accepts the backup request.
