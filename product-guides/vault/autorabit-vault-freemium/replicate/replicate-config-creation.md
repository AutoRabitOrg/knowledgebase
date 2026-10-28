# Replicate Config Creation

## AutoRABIT Vault Replicate Configuration User Guide

_Create and manage Salesforce data replication configurations_

This guide explains how to create a Replicate configuration in AutoRABIT Vault, select the source backup and objects to include, define field matching rules, review replication settings, and manage saved configurations. A Replicate configuration copies supported data from a selected backup to the target Salesforce organization according to the choices made during setup.

Before you begin, ensure that the required source backup has completed successfully and that the appropriate source and target Salesforce organizations are available to your Vault user account.

## Workflow overview

| **Stage**               | **What you do**                                                           |
| ----------------------- | ------------------------------------------------------------------------- |
| 1. Choose Backup        | Select the backup that supplies the source data.                          |
| 2. Object selection     | Choose the backed-up objects and optionally narrow the data with filters. |
| 3. Field matching       | Map source and target records by using matching rules.                    |
| 4. Review and replicate | Confirm the configuration and choose the available replication options.   |

## Open Replicate Config

From the left navigation, select **Replicate**. The **Replicate Config** page lists existing configurations and provides their source and destination context, modified date, and actions. Select **Create New Replicate Config** to begin.

<figure><img src="../../../../.gitbook/assets/image (3066).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Config landing page_

<figure><img src="../../../../.gitbook/assets/image (3067).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Create New Replicate Config action_

## Create a Replicate configuration

{% stepper %}
{% step %}
### Choose a backup

The first stage displays available backups. Select the backup that contains the data to replicate, then select **Next**. The selected backup becomes the source for the remaining configuration steps.

<figure><img src="../../../../.gitbook/assets/image (3068).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose Backup stage_

<figure><img src="../../../../.gitbook/assets/image (3069).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Selected backup_
{% endstep %}

{% step %}
### Select objects and define source data

In **Object Selection**, choose the objects to include. Use the available object controls to expand the selection and inspect fields. Where provided, configure object-level criteria before proceeding. The chosen objects form the scope of the replicate configuration.

<figure><img src="../../../../.gitbook/assets/image (3071).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Object Selection stage_

<figure><img src="../../../../.gitbook/assets/image (3072).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Object selection with available controls_

<figure><img src="../../../../.gitbook/assets/image (3073).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose objects dialog_

<figure><img src="../../../../.gitbook/assets/image (3074).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Select an object from the object list_

<figure><img src="../../../../.gitbook/assets/image (3075).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Object fields and selection controls_

<figure><img src="../../../../.gitbook/assets/image (3076).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Edit an object selection_

<figure><img src="../../../../.gitbook/assets/image (3077).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Selected fields dialog_

<figure><img src="../../../../.gitbook/assets/image (3078).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Review selected fields_

<figure><img src="../../../../.gitbook/assets/image (3079).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Object Selection ready to proceed_
{% endstep %}

{% step %}
### Define matching rules

In **Field Matching**, define how Vault identifies the corresponding destination record for each selected object. Matching rules help retain the relationship between source data and data already present in the destination organization. Select **Add Matching Rule** for the required object, then choose the source field, match operator, and matching target field.

<figure><img src="../../../../.gitbook/assets/image (3080).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Field Matching stage_

<figure><img src="../../../../.gitbook/assets/image (3081).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Add Matching Rule dialog_

<figure><img src="../../../../.gitbook/assets/image (3082).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose the source object_

<figure><img src="../../../../.gitbook/assets/image (3083).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose the source field_

<figure><img src="../../../../.gitbook/assets/image (3084).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose a matching operator_

<figure><img src="../../../../.gitbook/assets/image (3085).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Choose the destination field_

<figure><img src="../../../../.gitbook/assets/image (3086).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Select source fields for matching_

<figure><img src="../../../../.gitbook/assets/image (3087).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Select destination fields for matching_

<figure><img src="../../../../.gitbook/assets/image (3088).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Save the matching rule_

<figure><img src="../../../../.gitbook/assets/image (3089).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Matching rule shown in Field Matching_

<figure><img src="../../../../.gitbook/assets/image (3090).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Matching warning and acknowledgement_
{% endstep %}

{% step %}
### Review replication settings

The **Review and Replicate** stage summarizes the selected source and target context, the configured object matching, and the available replication settings. Review each setting before starting the replication. If the warning message is displayed, read and acknowledge it before continuing.

<figure><img src="../../../../.gitbook/assets/image (3091).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Review and Replicate stage_

<figure><img src="../../../../.gitbook/assets/image (3092).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replication warning_

<figure><img src="../../../../.gitbook/assets/image (3093).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Summary dialog_

<figure><img src="../../../../.gitbook/assets/image (3094).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Summary settings_
{% endstep %}
{% endstepper %}

## Manage saved Replicate configurations

After saving, the **Replicate Config** page displays the configuration in the list. Use the actions provided for each row to view its configuration details, make changes, or remove the configuration when it is no longer required. Confirm a deletion only when the configuration should no longer be available.

<figure><img src="../../../../.gitbook/assets/image (3095).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Saved Replicate Config list_

<figure><img src="../../../../.gitbook/assets/image (3096).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Config information_

<figure><img src="../../../../.gitbook/assets/image (3097).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Matching Rule Details_

<figure><img src="../../../../.gitbook/assets/image (3098).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Configuration list with actions_

<figure><img src="../../../../.gitbook/assets/image (3099).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Saved configuration confirmation_

<figure><img src="../../../../.gitbook/assets/image (3100).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Config details_

<figure><img src="../../../../.gitbook/assets/image (3101).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Additional configuration details_

<figure><img src="../../../../.gitbook/assets/image (3102).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Delete Replicate Config confirmation_

<figure><img src="../../../../.gitbook/assets/image (3103).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Configuration deleted confirmation_

<figure><img src="../../../../.gitbook/assets/image (3104).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Configuration action menu_

<figure><img src="../../../../.gitbook/assets/image (3105).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Edit Replicate Config - Choose Backup_

<figure><img src="../../../../.gitbook/assets/image (3106).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Config list after update_

<figure><img src="../../../../.gitbook/assets/image (3107).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Delete warning acknowledgement_

<figure><img src="../../../../.gitbook/assets/image (3108).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Summary before replication_

<figure><img src="../../../../.gitbook/assets/image (3109).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                   _Replicate Summary confirmation_

## Best practices

* Use a recent, successfully completed backup so the source data is current and complete.
* Select only the objects and fields required for the intended replication to keep the configuration focused and easier to validate.
* Use stable, unique fields for matching wherever possible, and review matching rules carefully before replication.
* Review the Replicate Summary and all enabled settings before initiating the operation.
* Use configuration details to validate saved rules before reusing a configuration for another replication.
