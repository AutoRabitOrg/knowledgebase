# Find\_Replace - Masking\_Rules

The Masking Rules module centralizes the creation and management of masking rules for a selected Salesforce org. A masking rule defines the object, field type, masking style, selected fields, and replacement behavior used to protect sensitive values.

This guide explains how a Find & Replace masking rule is created from the standalone Masking Rules module.

## Open the Masking Rules Module

The Masking Rules page displays the selected Salesforce org and the available rule management options. The grid lists existing masking rules with columns such as Rule Name, Type Of The Rule, Object, Field Type, Masking Style, Selected Fields, Created Date, Modified Date, and Actions. When no rules are available, the page displays No Masking Rules.

The Salesforce org is selected from Salesforce Orgs. The required rule can then be created by selecting NEW MASKING RULE.

<figure><img src="../../../../.gitbook/assets/image (2666).png" alt=""><figcaption></figcaption></figure>

## Start a New Masking Rule

Selecting NEW MASKING RULE opens the Masking Rule dialog. The dialog displays the selected Salesforce Org and provides the required fields for rule creation.

Rule Name is mandatory. The field supports alphanumerics, hyphen, underscore, and spaces. If the rule name does not follow the allowed format, a validation message is shown and the rule cannot be saved until the value is corrected.

SAVE remains inactive until the mandatory configuration is completed. CANCEL closes the dialog without saving the rule.

<figure><img src="../../../../.gitbook/assets/Screenshot 2026-07-14 at 2.01.43 AM.png" alt=""><figcaption></figcaption></figure>

## Define the Rule Scope

The rule scope is defined by selecting the Salesforce object and the field type. Select Object displays the available objects for the selected Salesforce org. Field Type narrows the field list to the required type of field.

![](<../../../../.gitbook/assets/Unknown image (363)>)

![](<../../../../.gitbook/assets/Unknown image (364)>)

## Select Find & Replace as the Masking Style

Masking Style is set to Find & Replace. This masking style searches selected fields for a configured value or pattern and replaces the matching values based on the selected replacement option.

![](<../../../../.gitbook/assets/Unknown image (365)>)

## Configure the Find and Replacement Values

The Find field accepts either a regular expression or a specific value. This value is used to search across the selected fields and identify the values that must be masked.

After the Find value is entered, Replace With determines how the matched values are replaced. The replacement option can be set to Specific Value or Synthetic Data.

* Specific Value replaces each matched value with the replacement value entered in the rule.
* Synthetic Data replaces each matched value with generated synthetic data based on the configured replacement behavior.

![](<../../../../.gitbook/assets/Unknown image (366)>)

![](<../../../../.gitbook/assets/Unknown image (367)>)

![](<../../../../.gitbook/assets/Unknown image (368)>)

![](<../../../../.gitbook/assets/Unknown image (369)>)

![](<../../../../.gitbook/assets/Unknown image (370)>)

## Select Fields and Review Sample Values

After the rule criteria are configured, the matching fields are displayed in the table. The Search field can be used to narrow the list. The field list can be scrolled to review and select the required number of fields.

Selected fields display the masking strategy and sample value columns. The sample value indicates how the matched data will be replaced when the rule is applied.

![](<../../../../.gitbook/assets/Unknown image (371)>)

![](<../../../../.gitbook/assets/Unknown image (372)>)

![](<../../../../.gitbook/assets/Unknown image (373)>)

![](<../../../../.gitbook/assets/Unknown image (374)>)

![](<../../../../.gitbook/assets/Unknown image (375)>)

## Save the Rule

After the Find value, Replace With option, replacement details, and selected fields are complete, SAVE becomes available. Selecting SAVE creates the Find & Replace masking rule for the selected Salesforce org.

The rule is then available from the Masking Rules page and can be reviewed or managed from the rule grid.

![](<../../../../.gitbook/assets/Unknown image (376)>)

## Configuration Summary

| **Configuration area** | **Purpose**                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **Salesforce Orgs**    | Identifies the Salesforce org where the masking rule is created.                        |
| **Rule Name**          | Defines the masking rule name and must follow the allowed character format.             |
| **Select Object**      | Determines the Salesforce object whose fields are available for masking.                |
| **Field Type**         | Filters the available fields by the selected field type.                                |
| **Masking Style**      | Uses Find & Replace to locate and replace values that match the configured Find value.  |
| **Find**               | Accepts either a regular expression or a specific value to identify values for masking. |
| **Replace With**       | Supports Specific Value or Synthetic Data as the replacement method.                    |
| **SAVE**               | Creates the masking rule after the mandatory configuration is complete.                 |
