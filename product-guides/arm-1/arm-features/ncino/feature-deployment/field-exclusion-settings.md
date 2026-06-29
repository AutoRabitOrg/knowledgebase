# Field Exclusion Settings

**Configure Excluded Fields in Deployment**

Excluded fields control which object fields are omitted from deployment processing. This guide explains how field exclusions are reviewed during Deployment setup, how predefined audit field exclusions appear in the workflow, and how the same exclusions are confirmed before deployment execution.

## Before starting

The deployment workflow is already in progress and the Destination step is active. Source type and Source are complete, Deploy to is enabled, and the destination organization is selected. Commit settings are available when Commit to is enabled.

* A Destination org is selected.
* Commit settings are configured when the deployment also commits changes.
* A template or source configuration is selected for the deployment.
* The object mapping table displays the objects included in the selected configuration.

![](<../../../../../.gitbook/assets/Unknown image (183)>)

## Review the applied filter

The Applied filters column provides access to the filter configured for an object mapping. Opening the filter displays the configured record-selection criteria for the selected object.

![](<../../../../../.gitbook/assets/Unknown image (184)>)

After the filter is reviewed, the workflow returns to the Destination step. The object mapping table remains available for reviewing external ID mappings, sorting criteria, applied filters, and excluded fields.

![](<../../../../../.gitbook/assets/Unknown image (185)>)

## Review excluded fields for an object

In the Excluded fields column, opening Exclude fields displays the Field Exclusion Settings panel for the selected object.

![](<../../../../../.gitbook/assets/Unknown image (186)>)

The panel opens in All Fields view and indicates the number of fields currently excluded for the selected object. Excluded fields are selected in the list. Audit fields such as CreatedDate, CreatedById, LastModifiedDate, LastModifiedById, SystemModstamp, LastViewedDate, and LastReferencedDate are excluded by default.

\*\*Note:\*\*Audit fields are excluded by default to maintain data integrity and comply with organizational policies. These excluded fields may appear in downloaded results, but those are not considered for deployment.

## Filter the field list

The Field Exclusion Settings panel includes a list filter for switching between field views. The available views are Show all fields, Show only excluded fields, and Show only mandatory fields.

![](<../../../../../.gitbook/assets/Unknown image (187)>)

**Field list view options:**

1. Show all fields keeps the complete field list visible.
2. Show only excluded fields narrows the panel to the fields currently excluded from deployment processing.
3. Show only mandatory fields checks for mandatory fields in the selected object context.

When Show only mandatory fields is selected and no matching fields are available, the panel displays No fields found. Returning to All Fields restores the complete field list for review.

![](<../../../../../.gitbook/assets/Unknown image (188)>)

![](<../../../../../.gitbook/assets/Unknown image (189)>)

## Confirm excluded fields in Preview

The Preview step consolidates the deployment configuration before execution. Source details, Destination details, Job settings, and object mappings appear in a single review page.

![](<../../../../../.gitbook/assets/Unknown image (190)>)

The Applied filters column confirms the configured object filter, and the Excluded fields column remains available for final review. Opening Excluded fields from Preview displays the exclusion details in read-only mode.

![](<../../../../../.gitbook/assets/Unknown image (191)>)

Field Exclusion Settings (Readonly) confirms that the same audit fields are excluded for the selected object. The read-only state supports review without changing the finalized Preview configuration.
