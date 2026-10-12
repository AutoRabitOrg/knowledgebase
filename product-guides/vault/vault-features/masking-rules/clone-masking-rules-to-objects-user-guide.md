# Clone Masking Rules to Objects User Guide

**AutoRABIT Vault User Guide**

This guide explains how to clone existing masking rules to fields on one or more destination objects, review the rules that Vault will create, start the cloning operation, and monitor or retry the resulting bulk clone jobs.

## How rule consolidation works

Vault creates cloned rules by destination object and compatible field type. Within a destination object, selected fields with the same field type are combined under one cloned rule. The resulting rule retains the masking style and masking value of the selected source rule.

| **Observed selection**                  | **Result**               | **Interpretation**                                                                                         |
| --------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| 6 picklist fields on AccountTeamMember  | 1 rule masks 6 fields    | All six fields share the picklist type and are combined into one rule.                                     |
| 133 fields across 5 destination objects | 12 rules mask 133 fields | Vault counts each distinct compatible field type within each destination object as a separate cloned rule. |

{% hint style="info" %}
**Important:** The number of rules that will be created is not the same as the number of selected fields. It is the sum of applicable field-type groups across the selected destination objects.
{% endhint %}

## Before you begin

* Confirm that the required source masking rules exist in the selected Salesforce org.
* Identify the destination objects and fields to which the rules must be cloned.
* Ensure each destination field has the same field type as the selected source rule.
* Review fields marked as already having masking configured; these fields are not available for a new cloned assignment in the observed flow.

## Open the clone workflow

{% stepper %}
{% step %}
### Open Bulk Clone Rules

From the left navigation, expand Masking and select Bulk Clone Rules.
{% endstep %}

{% step %}
### Select the Salesforce org

Select the Salesforce org and select Apply.
{% endstep %}

{% step %}
### Open Clone to Object

Select Clone to Obj to open the Clone Masking Rules to Objects workflow.

<figure><img src="../../../../.gitbook/assets/image (2904).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk Clone Rules page and Clone to Obj action**
{% endstep %}
{% endstepper %}

## Select source masking rules

The Select Rules step lists available masking rules from the selected source org.

{% stepper %}
{% step %}
### Locate the source rule

Use the object filter or search controls to locate the required source rule.
{% endstep %}

{% step %}
### Select a masking rule

Select a masking rule. Only one rule for each field type can be selected.
{% endstep %}

{% step %}
### Continue

Review the selected-rule count and select Continue.

<figure><img src="../../../../.gitbook/assets/image (2905).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Available source masking rules**

<figure><img src="../../../../.gitbook/assets/image (2906).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **One source masking rule selected**
{% endstep %}
{% endstepper %}

## Add destination objects

The Destination Objects step is used to select target objects and configure compatible fields for each object.

{% stepper %}
{% step %}
### Add an object

Select Add Object.
{% endstep %}

{% step %}
### Select destination objects

Search for or select the required destination objects.
{% endstep %}

{% step %}
### Add selected objects

Select Add to include the objects in the destination configuration.

<figure><img src="../../../../.gitbook/assets/image (2907).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Destination Objects step before objects are added**

<figure><img src="../../../../.gitbook/assets/image (2908).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Object Selection dialog**

<figure><img src="../../../../.gitbook/assets/image (2909).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Destination object search and available objects**

<figure><img src="../../../../.gitbook/assets/image (2910).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Two destination objects selected**

<figure><img src="../../../../.gitbook/assets/image (2911).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Maximum of five destination objects selected**
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Observed limit:** The interface allows up to five destination objects in one clone operation. To choose another object after reaching the limit, unselect an existing object first.
{% endhint %}

## Select compatible destination fields

Select each destination object tab and choose the fields that must receive the cloned rule. Vault applies a source rule only to destination fields of the same field type and displays a clone preview for the active object.

{% stepper %}
{% step %}
### Open a destination object

Open a destination object tab.
{% endstep %}

{% step %}
### Select eligible fields

Select one or more eligible fields. Fields that already have masking configured are identified in the field list.
{% endstep %}

{% step %}
### Configure remaining objects

Repeat the selection for each destination object.
{% endstep %}

{% step %}
### Confirm configured objects

Confirm that the configured-object count reflects every intended destination object.

<figure><img src="../../../../.gitbook/assets/image (2912).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Configured destination objects and object-level clone preview**

<figure><img src="../../../../.gitbook/assets/image (2913).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Fields with existing masking and required field selection**

<figure><img src="../../../../.gitbook/assets/image (2914).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Case preview showing field groups and cloned rule names**
{% endstep %}
{% endstepper %}

## Understand the object-level readiness summary

For AccountTeamMember, all six selected fields are picklist fields. Because they share the same compatible field type, Vault groups them under one cloned substitution rule.

<figure><img src="../../../../.gitbook/assets/image (2915).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Six selected picklist fields on AccountTeamMember**

<figure><img src="../../../../.gitbook/assets/image (2916).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **One cloned rule configured to mask six AccountTeamMember fields**

**Displayed summary:** Ready to clone: 1 rule will be created, masking 6 fields on AccountTeamMember.

## Review the complete clone summary

Select Continue to open Summary. Review the source org, selected masking rules, destination objects, field-to-rule mappings, masking styles, source objects, and clone eligibility before starting the operation.

{% stepper %}
{% step %}
### Confirm source rules

Confirm that each selected source rule shows the expected field type, masking style, and Cloneable status.
{% endstep %}

{% step %}
### Review destination objects

Review each destination object and its selected field count.
{% endstep %}

{% step %}
### Verify rule mappings

Verify the source-to-cloned rule names and the masking style assigned to each field.
{% endstep %}

{% step %}
### Start cloning

Review the final Ready to clone summary and select Clone.

<figure><img src="../../../../.gitbook/assets/image (2917).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Summary with source rules, destination objects, and clone preview**

<figure><img src="../../../../.gitbook/assets/image (2918).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Summary mappings for Case, Opportunity, and Account**

<figure><img src="../../../../.gitbook/assets/image (2919).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Summary mappings for Account and AccountTeamMember**

<figure><img src="../../../../.gitbook/assets/image (2920).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Final readiness summary across five destination objects**
{% endstep %}
{% endstepper %}

**Displayed summary:** Ready to clone: 12 rules will be created, masking 133 fields across 5 objects.

## Start and monitor the clone operation

After Clone is selected, Vault confirms that the operation was initiated and directs the user to Masking > Bulk Clone Rules. A separate job is created for each destination object.

<figure><img src="../../../../.gitbook/assets/image (2921).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Clone operation initiated successfully**

<figure><img src="../../../../.gitbook/assets/image (2922).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk clone jobs created for the destination objects**

<figure><img src="../../../../.gitbook/assets/image (2923).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk Clone Rules list with destination-specific jobs**

<figure><img src="../../../../.gitbook/assets/image (2924).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Job statuses and actions**

<figure><img src="../../../../.gitbook/assets/image (2925).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Available action for an unsuccessful bulk clone job**

## Retry an unsuccessful job

If a destination-specific bulk clone job does not complete successfully, use the Retry action for that job.

{% stepper %}
{% step %}
### Locate the unsuccessful job

Locate the unsuccessful job in Bulk Clone Rules.
{% endstep %}

{% step %}
### Retry the job

Select the Retry action and confirm the operation when prompted.
{% endstep %}

{% step %}
### Monitor the retry

Verify the confirmation message and monitor the updated Last Run Date, status, and retry result.

<figure><img src="../../../../.gitbook/assets/image (2926).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Retry initiated for the selected bulk clone job**

<figure><img src="../../../../.gitbook/assets/image (2927).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk clone job list after retry**
{% endstep %}
{% endstepper %}

## Review bulk clone job details

Use the job information action to review the bulk job ID, operation type, destination, overall status, retry count, and field-level outcomes. The details identify the source and cloned rule, object, masking style, masking value, and remarks for each field.

<figure><img src="../../../../.gitbook/assets/image (2928).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk clone job information**

<figure><img src="../../../../.gitbook/assets/image (2929).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Partially failed job with field-level remarks**

<figure><img src="../../../../.gitbook/assets/image (2930).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Bulk Clone Rules list after job-detail review**

<figure><img src="../../../../.gitbook/assets/image (2931).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Detailed field mappings and masking values**

<figure><img src="../../../../.gitbook/assets/image (2932).png" alt=""><figcaption></figcaption></figure>

&#x20;                                            **Additional field-level job information**

## Interpret job results

| **Result**            | **Recommended review**                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Successfully cloned   | Confirm that the expected cloned rule and masking style are shown for the field.                                                                              |
| Partially Failed      | Review Remarks to identify failed fields, correct the reported configuration issue, and retry the destination-specific job.                                   |
| Invalid masking value | Verify that the source masking value is valid for the corresponding destination field. Picklist values must be valid for the destination field configuration. |

## Key points

* Only one source masking rule can be selected for each field type.
* A source rule can be applied only to destination fields with the same field type.
* Within one destination object, compatible fields of the same type are combined into one cloned rule.
* The same cloned rule can therefore mask multiple fields on that destination object.
* The total rule count is calculated across the field-type groups of all selected destination objects.
* Each destination object is tracked through its own bulk clone job, allowing object-specific monitoring and retry.
