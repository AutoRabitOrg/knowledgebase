# Find\_Replace\_Masking\_Rule

**Find & Replace Masking Rule**

AutoRABIT Vault Replicate - User Guide

This guide explains how a Find & Replace masking rule is created during Replicate Config. The flow supports masking by searching for either a regular expression or a specific value, and replacing the matched value with either a fixed replacement or generated synthetic data.

The masking rule is configured from the Masking Rules step of Replicate Config. After the rule is saved, it is available for the current replicate configuration and can optionally be added to the destination org masking rules list for reuse.

| **Area**             | **Purpose**                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Find**             | Accepts either a regular expression or a specific value that AutoRABIT Vault searches for within the selected fields. |
| **Replace With**     | Defines whether the matched value is replaced with a Specific Value or Synthetic Data.                                |
| **Replace Value**    | Appears for Specific Value replacement and stores the value that replaces every match.                                |
| **Masking Strategy** | Appears for Synthetic Data replacement and controls the type of generated sample value.                               |
| **Sample Value**     | Displays a generated value based on the selected masking strategy. The generate icon refreshes the sample value.      |

\*\*Note:\*\*When job-level and organization-level masking rules use the same field, the job-level masking rule takes priority.

### Open the Masking Rules step

During Replicate Config, the flow reaches the Masking Rules step after the backup and component selections are completed. The page lists existing masking rules, shows the source and destination org context, and provides the New Masking Rule action. If no rules exist, AutoRABIT Vault displays the No Masking Rules empty state.

![](<../../../../../.gitbook/assets/Unknown image (346)>)

### Start a new masking rule

Selecting New Masking Rule opens the Masking Rule panel. The rule setup begins with Rule Name, Select Object, Field Type, and Masking Style. Rule Name is mandatory and accepts alphanumeric characters, spaces, hyphen, and underscore. AutoRABIT Vault displays a validation message when unsupported characters are entered.

![](<../../../../../.gitbook/assets/Unknown image (347)>)

The selected Salesforce org is shown at the top of the panel to keep the masking configuration tied to the destination context. Select Object provides a searchable object list, and the required object is selected before field-level configuration begins.

![](<../../../../../.gitbook/assets/Unknown image (348)>)

### Choose the field type and masking style

After the object is selected, Field Type filters the available fields by their Salesforce data type. Selecting the required field type narrows the field list and helps apply masking only to compatible fields.

![](<../../../../../.gitbook/assets/Unknown image (349)>)

Masking Style defines how the selected fields are masked. For this flow, Find & Replace is selected. This enables AutoRABIT Vault to search for a value or pattern inside the selected fields and replace the matching content.

![](<../../../../../.gitbook/assets/Unknown image (350)>)

### Define the value or pattern to find

When Find & Replace is selected, AutoRABIT Vault displays Find, Replace With, and Replace Value fields. The Find field accepts either a regular expression or a specific value. A regular expression can be used to identify a pattern across records, while a specific value can be used to target an exact value for replacement.

![](<../../../../../.gitbook/assets/Unknown image (351)>)

In a regular expression based setup, the pattern is entered directly in Find. AutoRABIT Vault uses this value to identify matching content within the selected fields during masking.

![](<../../../../../.gitbook/assets/Unknown image (352)>)

### Select the replacement method

Replace With controls how matched values are replaced. Specific Value replaces every match with a fixed value provided in Replace Value. Synthetic Data replaces matched values with generated data based on the masking strategy selected for each field.

![](<../../../../../.gitbook/assets/Unknown image (353)>)

When Specific Value is selected, Replace Value becomes the required replacement input. The rule can then be applied to one or more selected fields. Save becomes available after the required rule details and at least one field selection are completed.

![](<../../../../../.gitbook/assets/Unknown image (354)>)

![](<../../../../../.gitbook/assets/Unknown image (355)>)

### Use synthetic data as the replacement

When Replace With is set to Synthetic Data, AutoRABIT Vault displays the Masking Strategy and Sample Value columns in the field list. Each selected field can use an appropriate masking strategy, and AutoRABIT Vault displays a sample value generated from that strategy.

![](<../../../../../.gitbook/assets/Unknown image (356)>)

The Sample Value information icon explains that the displayed value is generated using the selected masking strategy. This helps validate the expected output format before the masking rule is saved.

![](<../../../../../.gitbook/assets/Unknown image (357)>)

The Masking Strategy value can be changed for each applicable field. The available strategy list provides compatible strategy options, and View More expands the list when additional strategies are available.

![](<../../../../../.gitbook/assets/Unknown image (358)>)

The generate icon refreshes the sample value for the corresponding field. The icon can be used repeatedly until the displayed sample value is suitable for the masking requirement.

![](<../../../../../.gitbook/assets/Unknown image (359)>)

### Mask a specific value

The same Find & Replace flow also supports exact value replacement. A specific value is entered in Find, Specific Value is selected under Replace With, and the desired masked output is entered in Replace Value. The required field is then selected from the field list.

![](<../../../../../.gitbook/assets/Unknown image (360)>)

### Save the masking rule

After the rule details are completed and the required fields are selected, Save stores the masking rule. The Add to Org Masking Rules List option can be selected when the rule also needs to be added to the destination org masking rules list for reuse.

### Result

The Find & Replace masking rule is saved with the selected object, field type, masking style, find condition, replacement method, and selected fields. During replicate processing, AutoRABIT Vault searches the selected fields for the configured regular expression or specific value and masks the matching content using the selected replacement method.
