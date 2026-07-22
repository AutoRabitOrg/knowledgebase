# Synthetic\_Data\_Generator - Masking\_Rules

The Masking Rules module centralizes the creation and management of masking rules for a selected Salesforce org. A masking rule defines the object, field type, masking style, selected fields, and replacement behavior used to protect sensitive values.

This guide explains how a Synthetic Data masking rule is created from the standalone Masking Rules module.

## Open the Masking Rules Module

The Masking Rules page displays the selected Salesforce org and the available rule management options. The grid lists existing masking rules with columns such as Rule Name, Type Of The Rule, Object, Field Type, Masking Style, Selected Fields, Created Date, Modified Date, and Actions. When no rules are available, the page displays No Masking Rules.

The Salesforce org is selected from Salesforce Orgs. The required rule can then be created by selecting NEW MASKING RULE.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-07-14 at 2.06.52 AM.png" alt=""><figcaption></figcaption></figure>

## Start a New Masking Rule

Selecting NEW MASKING RULE opens the Masking Rule dialog. The dialog displays the selected Salesforce Org and provides the required fields for rule creation.

Rule Name is mandatory. The field supports alphanumerics, hyphen, underscore, and spaces. If the rule name does not follow the allowed format, a validation message is shown and the rule cannot be saved until the value is corrected.

SAVE remains inactive until the mandatory configuration is completed. CANCEL closes the dialog without saving the rule.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-07-14 at 2.01.43 AM.png" alt=""><figcaption></figcaption></figure>

## Define the Rule Scope

The rule scope is defined by selecting the Salesforce object and the field type. The Select Object list displays the available objects for the selected Salesforce org. After an object is selected, Field Type is used to narrow the field list to the required type of field.

![](<../../../../.gitbook/assets/Unknown image (377)>)

![](<../../../../.gitbook/assets/Unknown image (378)>)

![](<../../../../.gitbook/assets/Unknown image (379)>)

## Select the Synthetic Data Masking Style

Masking Style is set to Synthetic Data. This masking style replaces selected field values with generated synthetic values that align with the selected masking strategy.

![](<../../../../.gitbook/assets/Unknown image (380)>)

## Select Fields and Configure Masking Strategy

After the object, field type, and masking style are selected, the matching fields are listed in the table. The Search field can be used to narrow the list. The list can be scrolled to review and select the required number of fields.

Each selected field displays configuration options for Masking Strategy and Sample Value. The Masking Strategy value can be changed as needed for each field. The generated sample value provides a preview of the replacement format that will be used for the selected strategy.

Generate Sample Value can be used to shuffle through generated sample values. The value can be regenerated until an acceptable sample appears for the selected field.

![](<../../../../.gitbook/assets/Unknown image (381)>)

![](<../../../../.gitbook/assets/Unknown image (382)>)

![](<../../../../.gitbook/assets/Unknown image (383)>)

![](<../../../../.gitbook/assets/Unknown image (384)>)

![](<../../../../.gitbook/assets/Unknown image (385)>)

![](<../../../../.gitbook/assets/Unknown image (386)>)

## Save the Rule

After the required fields are selected and their masking strategy values are configured, SAVE becomes available. Selecting SAVE creates the masking rule for the selected Salesforce org.

The rule is then available from the Masking Rules page and can be reviewed or managed from the rule grid.

![](<../../../../.gitbook/assets/Unknown image (387)>)

## Configuration Summary

| **Configuration area**    | **Purpose**                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------- |
| **Salesforce Orgs**       | Identifies the Salesforce org where the masking rule is created.                      |
| **Rule Name**             | Defines the masking rule name and must follow the allowed character format.           |
| **Select Object**         | Determines the Salesforce object whose fields are available for masking.              |
| **Field Type**            | Filters the available fields by the selected field type.                              |
| **Masking Style**         | Uses Synthetic Data to replace selected field values with generated synthetic values. |
| **Masking Strategy**      | Defines the type of synthetic value generated for each selected field.                |
| **Generate Sample Value** | Regenerates the sample value until a suitable preview value appears.                  |
| **SAVE**                  | Creates the masking rule after the mandatory configuration is complete.               |
