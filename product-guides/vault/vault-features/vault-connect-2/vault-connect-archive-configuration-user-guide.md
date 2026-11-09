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

<figure><img src="../../../../.gitbook/assets/image (5563).png" alt=""><figcaption></figcaption></figure>

Open Vault Connect
{% endstep %}

{% step %}
### Start a new configuration

On the Configurations screen, select the action to create a configuration. The Create Vault Connect Configuration wizard opens.

<figure><img src="../../../../.gitbook/assets/image (5564).png" alt=""><figcaption></figcaption></figure>

Start a new configuration
{% endstep %}

{% step %}
### Select Org

Choose the Salesforce org in which the historical archive data should be accessible. Review the Org Name, Salesforce Org ID, Vault Connection, Existing Configurations, Token Status, and Last Updated columns. Select the org and click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (5565).png" alt=""><figcaption></figcaption></figure>

Step 1 — Select Org
{% endstep %}

{% step %}
### Select Source

Select a source archive configuration from the list. The selected Salesforce org appears at the top. Review Type, Schedule, Last Run, and Retention before clicking CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (5566).png" alt=""><figcaption></figcaption></figure>

Step 2 — Select Source

#### Adjust the source table columns

Select COLUMNS to open the column-selection dialog. Select the information that should be displayed in the list, then apply or confirm the selection using the dialog controls.

<figure><img src="../../../../.gitbook/assets/image (5567).png" alt=""><figcaption></figcaption></figure>

Adjust the source table columns

#### Filter the source list

Select FILTER BY to open the filter dialog. Choose a field and filter criterion to narrow the source configurations.

<figure><img src="../../../../.gitbook/assets/image (5568).png" alt=""><figcaption></figcaption></figure>

Filter the source list

#### Choose a filter field

Open the filter-field dropdown and select the desired field from the available options.

<figure><img src="../../../../.gitbook/assets/image (5568).png" alt=""><figcaption></figcaption></figure>

Choose a filter field

#### Choose a filter operator

Open the operator dropdown and choose the applicable comparison option for the selected field.

<figure><img src="../../../../.gitbook/assets/image (5570).png" alt=""><figcaption></figcaption></figure>

Choose a filter operator

#### Apply the source filter

Supply the required filter value, where applicable, and apply the filter. Select the intended source configuration and continue.

<figure><img src="../../../../.gitbook/assets/image (5571).png" alt=""><figcaption></figcaption></figure>

Apply the source filter
{% endstep %}

{% step %}
### Select Snapshots

Select one or more archive instances from the selected source configuration. Review Archive Name, Run Date, Type, Data Size, Records, and Expiry Date. Click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (5572).png" alt=""><figcaption></figcaption></figure>

Step 3 — Select Snapshots
{% endstep %}

{% step %}
### Select Objects

Review the objects found across the selected archive snapshots. Choose the objects that should be accessible from Salesforce.

<figure><img src="../../../../.gitbook/assets/image (5573).png" alt=""><figcaption></figcaption></figure>

Select Objects

#### Customize object table columns

Use COLUMNS to select the object details displayed in the table. Confirm the desired column selection.

<figure><img src="../../../../.gitbook/assets/image (5574).png" alt=""><figcaption></figcaption></figure>

Customize object table columns

#### Review selected object details

Review Object Label, API Name, Available In, Type, Data Size, Latest Snapshot, and Status. The Available In value indicates the number of selected snapshots containing the object.

<figure><img src="../../../../.gitbook/assets/image (5575).png" alt=""><figcaption></figcaption></figure>

Review selected object details

#### Filter the objects

Select FILTER BY to filter the object list using the available fields.

<figure><img src="../../../../.gitbook/assets/image (5576).png" alt=""><figcaption></figcaption></figure>

Filter the objects

#### Choose an object filter criterion

Select the field and comparison criterion in the filter dialog, then supply a value if required.

<figure><img src="../../../../.gitbook/assets/image (5577).png" alt=""><figcaption></figcaption></figure>

Choose an object filter criterion

#### Apply an object filter

Apply the configured object filter to narrow the displayed objects.

<figure><img src="../../../../.gitbook/assets/image (5578).png" alt=""><figcaption></figcaption></figure>

Apply an object filter

#### Finalize object selection

Select the required object checkboxes. Verify the selected-object count and click CONTINUE.

<figure><img src="../../../../.gitbook/assets/image (5579).png" alt=""><figcaption></figcaption></figure>

Finalize object selection
{% endstep %}

{% step %}
### Review & Publish

Review the Salesforce Org, Source Configuration, Selected Snapshots, and Selected Objects summary cards. Enter a required Configuration Name and, optionally, a Description. Review the Email Notifications recipient and the Automatically Include New Archive Jobs switch.

<figure><img src="../../../../.gitbook/assets/image (5580).png" alt=""><figcaption></figcaption></figure>

Step 5 — Review & Publish

#### Configure automatic inclusion

When Automatically Include New Archive Jobs is enabled, newly completed jobs from the selected source configuration are automatically included in this Vault Connect configuration. Leave it disabled when automatic inclusion is not required.

<figure><img src="../../../../.gitbook/assets/image (5581).png" alt=""><figcaption></figcaption></figure>

Configure automatic inclusion

#### Return to an earlier step

Use the Edit link on a summary card when a selected Salesforce org, source, snapshot, or object requires correction. The corresponding wizard step is displayed.

<figure><img src="../../../../.gitbook/assets/image (5582).png" alt=""><figcaption></figcaption></figure>

Return to an earlier step

#### Recheck review details

Return to Review & Publish after editing and verify that all summary cards reflect the intended selections.

<figure><img src="../../../../.gitbook/assets/image (5583).png" alt=""><figcaption></figcaption></figure>

Recheck review details

#### Enter publication details

Complete the required Configuration Name. Confirm the optional description, notification recipients, and automatic-inclusion setting.

<figure><img src="../../../../.gitbook/assets/image (5584).png" alt=""><figcaption></figcaption></figure>

Enter publication details

#### Publish the configuration

Select PUBLISH CONFIGURATIONS to submit the configuration for publication. The button is available when the required information has been entered. Use SAVE DRAFT to retain an unfinished configuration, BACK to revise selections, or CANCEL to exit the flow.

<figure><img src="../../../../.gitbook/assets/image (5585).png" alt=""><figcaption></figcaption></figure>

Publish the configuration
{% endstep %}
{% endstepper %}
