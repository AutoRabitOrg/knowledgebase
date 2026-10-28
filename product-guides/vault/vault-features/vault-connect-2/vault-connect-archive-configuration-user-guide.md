# Vault Connect Archive Configuration User Guide

## Vault Connect: Archive Configuration

### User Guide

This guide explains how to create and publish a Vault Connect configuration using archived data so that selected historical records can be available in Salesforce.

## Before you begin

* Sign in to AutoRABIT Vault and open Vault Connect > Configurations.
* Ensure that the intended Salesforce org and archive source configuration are available for selection.
* Confirm that an appropriate Vault connection and token status are displayed for the Salesforce org.

## Configuration workflow

The guided setup contains five stages: Select Org, Select Source, Select Snapshots, Select Objects, and Review & Publish. The screens below follow the sequence displayed in the application.

{% stepper %}
{% step %}
### Open Vault Connect

In the navigation pane, expand Vault Connect and select Configurations. Review the Vault Connect overview and the existing configuration information.

<figure><img src="../../../../.gitbook/assets/image (3271).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Open Vault Connect
{% endstep %}

{% step %}
### Start a new configuration

On the Configurations screen, select the action to create a configuration. The Create Vault Connect Configuration wizard opens.

<figure><img src="../../../../.gitbook/assets/image (3272).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Start a new configuration
{% endstep %}

{% step %}
### Select Org

Choose the Salesforce org in which the historical archive data should be accessible. Review the Org Name, Salesforce Org ID, Vault Connection, Existing Configurations, Token Status, and Last Updated columns. Select the org and click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (3273).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Step 1 — Select Org
{% endstep %}

{% step %}
### Select Source

Select a source archive configuration from the list. The selected Salesforce org appears at the top. Review Type, Schedule, Last Run, and Retention before clicking CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (3274).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Step 2 — Select Source

#### Adjust the source table columns

Select COLUMNS to open the column-selection dialog. Select the information that should be displayed in the list, then apply or confirm the selection using the dialog controls.

<figure><img src="../../../../.gitbook/assets/image (3275).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Adjust the source table columns

#### Filter the source list

Select FILTER BY to open the filter dialog. Choose a field and filter criterion to narrow the source configurations.

<figure><img src="../../../../.gitbook/assets/image (3276).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Filter the source list

#### Choose a filter field

Open the filter-field dropdown and select the desired field from the available options.

<figure><img src="../../../../.gitbook/assets/image (3277).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Choose a filter field

#### Choose a filter operator

Open the operator dropdown and choose the applicable comparison option for the selected field.

<figure><img src="../../../../.gitbook/assets/image (3278).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Choose a filter operator

#### Apply the source filter

Supply the required filter value, where applicable, and apply the filter. Select the intended source configuration and continue.

<figure><img src="../../../../.gitbook/assets/image (3279).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Apply the source filter
{% endstep %}

{% step %}
### Select Snapshots

Select one or more archive instances from the selected source configuration. Review Archive Name, Run Date, Type, Data Size, Records, and Expiry Date. Click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (3280).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Step 3 — Select Snapshots
{% endstep %}

{% step %}
### Select Objects

Review the objects found across the selected archive snapshots. Choose the objects that should be accessible from Salesforce.

<figure><img src="../../../../.gitbook/assets/image (3281).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Select Objects

#### Customize object table columns

Use COLUMNS to select the object details displayed in the table. Confirm the desired column selection.

<figure><img src="../../../../.gitbook/assets/image (3282).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Customize object table columns

#### Review selected object details

Review Object Label, API Name, Available In, Type, Data Size, Latest Snapshot, and Status. The Available In value indicates the number of selected snapshots containing the object.

<figure><img src="../../../../.gitbook/assets/image (3283).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Review selected object details

#### Filter the objects

Select FILTER BY to filter the object list using the available fields.

<figure><img src="../../../../.gitbook/assets/image (3284).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Filter the objects

#### Choose an object filter criterion

Select the field and comparison criterion in the filter dialog, then supply a value if required.

<figure><img src="../../../../.gitbook/assets/image (3285).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Choose an object filter criterion

#### Apply an object filter

Apply the configured object filter to narrow the displayed objects.

<figure><img src="../../../../.gitbook/assets/image (3286).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Apply an object filter

#### Finalize object selection

Select the required object checkboxes. Verify the selected-object count and click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (3287).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Finalize object selection
{% endstep %}

{% step %}
### Review & Publish

Review the Salesforce Org, Source Configuration, Selected Snapshots, and Selected Objects summary cards. Enter a required Configuration Name and, optionally, a Description. Review the Email Notifications recipient and the Automatically Include New Archive Jobs switch.

<figure><img src="../../../../.gitbook/assets/image (3288).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Step 5 — Review & Publish

#### Configure automatic inclusion

When Automatically Include New Archive Jobs is enabled, newly completed jobs from the selected source configuration are automatically included in this Vault Connect configuration. Leave it disabled when automatic inclusion is not required.

<figure><img src="../../../../.gitbook/assets/image (3289).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Configure automatic inclusion

#### Return to an earlier step

Use the Edit link on a summary card when a selected Salesforce org, source, snapshot, or object requires correction. The corresponding wizard step is displayed.

<figure><img src="../../../../.gitbook/assets/image (3290).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Return to an earlier step

#### Recheck review details

Return to Review & Publish after editing and verify that all summary cards reflect the intended selections.

<figure><img src="../../../../.gitbook/assets/image (3291).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Recheck review details

#### Enter publication details

Complete the required Configuration Name. Confirm the optional description, notification recipients, and automatic-inclusion setting.

<figure><img src="../../../../.gitbook/assets/image (3292).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Enter publication details

#### Publish the configuration

Select PUBLISH CONFIGURATIONS to submit the configuration for publication. The button is available when the required information has been entered. Use SAVE DRAFT to retain an unfinished configuration, BACK to revise selections, or CANCEL to exit the flow.

<figure><img src="../../../../.gitbook/assets/image (3293).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                             Publish the configuration
{% endstep %}
{% endstepper %}
