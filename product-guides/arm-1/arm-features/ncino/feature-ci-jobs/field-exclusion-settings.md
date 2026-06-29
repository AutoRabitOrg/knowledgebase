# Field Exclusion Settings

**Configure Excluded Fields in CI Jobs**

Excluded fields control which object fields are omitted from deployment processing for a CI job. This guide explains how field exclusions are reviewed during CI job setup, how predefined audit field exclusions appear in the workflow, and where the same exclusions are confirmed after build execution.

## Before starting

The CI job is already in progress and the workflow is on the Destination step. Source type and Source are complete, Deploy to is enabled, and the destination organization is selected. Commit settings are available when Commit to is enabled.

* A Destination org is selected.
* Commit settings are configured when the CI job also commits changes.
* A template or source configuration is selected for the CI job.
* The object mapping table displays the objects included in the selected configuration.

![](<../../../../../.gitbook/assets/Unknown image (192)>)

## Review excluded fields for an object

In the Destination step, the Excluded fields column provides access to object-level field exclusion settings. Opening Exclude fields for an object displays the Field Exclusion Settings panel.

![](<../../../../../.gitbook/assets/Unknown image (193)>)

The panel opens in All Fields view and indicates the number of fields currently excluded for the selected object. Excluded fields are selected in the list. Audit fields such as CreatedDate, CreatedById, LastModifiedDate, LastModifiedById, SystemModstamp, LastActivityDate, LastViewedDate, and LastReferencedDate are excluded by default.

**Note:** Audit fields are excluded by default to maintain data integrity and comply with organizational policies. These excluded fields may appear in downloaded results, but those are not considered for deployment.

## Filter the field list

The Field Exclusion Settings panel includes a list filter for switching between field views. The available views are Show all fields, Show only excluded fields, and Show only mandatory fields.

![](<../../../../../.gitbook/assets/Unknown image (194)>)

Field list view options.

1. Show all fields keeps the complete field list visible.
2. Show only excluded fields narrows the panel to the fields currently excluded from deployment processing.
3. Show only mandatory fields checks for mandatory fields in the selected object context.

When Show only excluded fields is selected, the panel changes to Only Excluded Fields and lists the fields currently excluded for the selected object.

![](<../../../../../.gitbook/assets/Unknown image (195)>)

When Show only mandatory fields is selected, the panel changes to Only Mandatory Fields. In this flow, the list returns No fields found.

![](<../../../../../.gitbook/assets/Unknown image (196)>)

## Return to the destination mapping

After the field review is complete, the Destination step remains the working context for the CI job. The mapping table continues to show external ID mappings, sorting criteria, applied filters, and excluded fields for each object.

![](<../../../../../.gitbook/assets/Unknown image (197)>)

The Applied filters indicator opens the filter configured for the selected object. The filter confirms the record-selection criteria configured for the selected object.

![](<../../../../../.gitbook/assets/Unknown image (198)>)

## Confirm excluded fields in Preview

The Preview step consolidates the CI job configuration before execution. Source details, Destination details, Job settings, and object mappings appear in a single review page.

![](<../../../../../.gitbook/assets/Unknown image (199)>)

The Applied filters column confirms the configured object filter, and the Excluded fields column remains available for final review. Opening Excluded fields from Preview displays the exclusion details in read-only mode.

![](<../../../../../.gitbook/assets/Unknown image (200)>)

![](<../../../../../.gitbook/assets/Unknown image (201)>)

Field Exclusion Settings (Readonly) confirms that the same audit fields are excluded for the selected object. The read-only state supports review without changing the finalized Preview configuration.

## Review excluded fields after the CI job runs

After the CI job runs, CI Job History provides status and result details for each build. The Actions menu includes Build results, which opens the build output for the selected job.

![](<../../../../../.gitbook/assets/Unknown image (202)>)

Feature details summarizes the selected build. The result includes Build status, Deploy status, retrieved counts, success counts, and failed counts for each object.

![](<../../../../../.gitbook/assets/Unknown image (203)>)

The object-level result details include a Successful records summary and an Excluded fields section. The summary shows the final record-processing outcome for the object. The Excluded fields section lists the fields that are not considered for deployment.

![](<../../../../../.gitbook/assets/Unknown image (204)>)
