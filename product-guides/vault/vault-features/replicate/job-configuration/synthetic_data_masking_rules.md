# Synthetic\_Data\_Masking\_Rules

_Creating synthetic data masking rules during Replicate Config creation_

## Overview

The Replicate Config workflow includes a Masking Rules step where job-level masking rules are configured before the replicate configuration is finalized. These rules define how selected fields are transformed during replication so sensitive or business-specific values can be replaced with generated sample data.

When a field is included in both a job-level masking rule and an organization-level masking rule, the job-level masking rule takes priority for the replicate job.

| **Area**              | **Behavior**                                                                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Masking Strategy      | The value in the Masking Strategy field can be changed for each selected field. This allows different generator strategies to be applied field by field.       |
| Generate Sample Value | The Generate Sample Value icon refreshes the displayed sample value. The value can be regenerated until the generated sample is suitable for the masking rule. |
| Field selection       | The field list can be scrolled, and the required number of fields can be selected from the available records before saving the masking rule.                   |
| Save behavior         | SAVE becomes available after the required masking rule details and field selections are completed.                                                             |

## Accessing the Masking Rules step

In Replicate Config, the flow progresses from Choose Backup to Select Components and then opens the Masking Rules step. The page displays the selected source and destination org context, a Filter option, the Columns selector, and the masking rule grid. The grid is empty until a rule is added.

The NEW MASKING RULE action starts the masking rule creation flow for the current replicate configuration.

![](<../../../../../.gitbook/assets/Unknown image (333)>)

The same step remains available with navigation controls such as BACK and NEXT. After masking rules are completed, NEXT continues the replicate configuration flow to Config Details.

![](<../../../../../.gitbook/assets/Unknown image (334)>)

## Starting a new masking rule

Selecting NEW MASKING RULE opens the Masking Rule dialog. The dialog captures the Rule Name, Select Object, Field Type, and Masking Style. The field grid remains empty until the required selections are completed.

Rule Name is mandatory. When the entered value does not meet the allowed format, the validation message indicates that alphanumerics, hyphen, underscore, and spaces are allowed.

![](<../../../../../.gitbook/assets/Unknown image (335)>)

The Add to Org masking rules list option is available at the bottom of the dialog. When selected, the rule is also added to the organization-level masking rules list for reuse, subject to the available configuration behavior.

![](<../../../../../.gitbook/assets/Unknown image (336)>)

## Selecting object and field type

The Select Object dropdown lists the objects available for the selected Salesforce org context. After an object is selected, Field Type is used to narrow the available fields to the required type.

![](<../../../../../.gitbook/assets/Unknown image (337)>)

The Field Type dropdown displays the supported field categories. Selecting a field type controls which fields appear in the grid and which masking styles are applicable for the rule.

![](<../../../../../.gitbook/assets/Unknown image (338)>)

## Choosing the masking style

Masking Style defines how the selected fields are transformed. In this flow, Synthetic Data is selected to generate replacement values that match the configured strategy for each field.

![](<../../../../../.gitbook/assets/Unknown image (339)>)

After the object, field type, and masking style are selected, AutoRABIT Vault loads the matching field list. The grid displays each eligible field with Check, Field Name, Masking Strategy, Sample Value, and the Generate Sample Value icon.

![](<../../../../../.gitbook/assets/Unknown image (340)>)

## Selecting fields and updating masking strategies

The required fields are selected using the checkboxes in the Check column. The field list can be scrolled to review additional fields and select the required number of fields for the masking rule.

![](<../../../../../.gitbook/assets/Unknown image (341)>)

Each selected field has its own Masking Strategy value. The value appearing under Masking Strategy can be changed field by field from the dropdown. Available strategies depend on the selected field type and masking style. The View More option exposes additional strategy values when the list contains more options than initially displayed.

![](<../../../../../.gitbook/assets/Unknown image (342)>)

## Generating and reviewing sample values

The Sample Value column shows the generated value for the selected strategy. The Generate Sample Value icon refreshes the displayed sample value for the corresponding field. This allows the generated output to be shuffled until the sample value is acceptable for the masking rule.

![](<../../../../../.gitbook/assets/Unknown image (343)>)

After a sample value is regenerated, the row displays the updated output while preserving the selected field and masking strategy. This review can be repeated before saving the rule.

![](<../../../../../.gitbook/assets/Unknown image (344)>)

## Saving the masking rule

After the required fields are selected and the masking strategies are reviewed, SAVE stores the masking rule for the replicate configuration. CANCEL closes the dialog without saving changes.

If Add to Org masking rules list is selected before saving, the masking rule is also added to the organization-level masking rules list. If it is not selected, the rule remains part of the current job-level replicate configuration only.

![](<../../../../../.gitbook/assets/Unknown image (345)>)

## Result

The masking rule is available in the Masking Rules step for the replicate configuration. The configuration can then continue to Config Details and proceed with the remaining replicate setup. During execution, the selected fields use the configured masking strategies and generated values according to the saved rule.
