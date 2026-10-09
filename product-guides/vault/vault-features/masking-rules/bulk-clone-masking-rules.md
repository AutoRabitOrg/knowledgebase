# Bulk Clone Masking Rules

### Bulk Clone Rules User Guide

This guide describes how masking rules are cloned from a source Salesforce org to one or more target orgs from the Bulk Clone Rules page. It also explains how to monitor the generated jobs and review rule-level results.

## Overview

The Clone to Org workflow uses a three-step wizard. Masking rules are selected first, target orgs are selected next, and the combined selection is reviewed before the clone begins. A separate bulk job is created for each target org.

## Prerequisites

* The source Salesforce org is configured and available in Vault.
* The required masking rules exist in the source org.
* Each target Salesforce org is configured and accessible.
* Appropriate access to Masking and Bulk Clone Rules is available.

## Open Bulk Clone Rules

{% stepper %}
{% step %}
### Open the Bulk Clone Rules page

From the navigation pane, expand Masking and select Bulk Clone Rules.
{% endstep %}

{% step %}
### Select the source org

Select the source Salesforce org from the Salesforce Orgs list, and then click Apply. The page displays the bulk clone jobs associated with the selected source org.
{% endstep %}

{% step %}
### Start the workflow

Click Clone to Org to open the Clone Masking Rules to ORGs wizard.

<figure><img src="../../../../.gitbook/assets/image (2892).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Bulk Clone Rules page with the source org and Clone to Org action
{% endstep %}
{% endstepper %}

## Select Masking Rules

{% stepper %}
{% step %}
### Review the available rules

On the Select Rules step, review the masking rules from the selected source org. All rules are selected by default. The list identifies the rule name, object, field type, masking style, and source org.
{% endstep %}

{% step %}
### Choose the rules to clone

Keep the required checkboxes selected and clear the checkboxes for rules that must not be cloned. Use Search to locate a specific rule. The selected-rule count updates below the list.
{% endstep %}

{% step %}
### Continue to target selection

Click Continue after the required masking rules are selected.

<figure><img src="../../../../.gitbook/assets/image (2893).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Select Rules step with all masking rules selected by default

<figure><img src="../../../../.gitbook/assets/image (2894).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Select Rules step with two masking rules selected
{% endstep %}
{% endstepper %}

## Select Target Orgs

{% stepper %}
{% step %}
### Review the available target orgs

On the Target orgs step, review the Salesforce orgs available as clone destinations. All target orgs are selected by default.
{% endstep %}

{% step %}
### Choose the target orgs

Keep the required target-org checkboxes selected and clear the remaining checkboxes. Select All toggles the complete list. Use Search to locate a specific org.
{% endstep %}

{% step %}
### Continue to the summary

Click Continue after one or more target orgs are selected. Click Back to revise the rule selection or Cancel to exit the workflow.

<figure><img src="../../../../.gitbook/assets/image (2895).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Target orgs step with all available orgs selected

<figure><img src="../../../../.gitbook/assets/image (2896).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Target orgs step with two orgs selected
{% endstep %}
{% endstepper %}

## Review and Start the Clone

{% stepper %}
{% step %}
### Verify the summary

On the Summary step, verify the source org, target orgs, selected masking rules, objects, field types, masking styles, and selected fields.

Each selected rule is validated against each target org during processing. A rule and target-org combination is skipped when the required object or field is missing or when the rule already exists. Skipped combinations are reported in Job History.
{% endstep %}

{% step %}
### Initiate the clone

Click Clone to create the bulk clone jobs. Click Back to revise the target org selection or Cancel to exit without starting the clone.

<figure><img src="../../../../.gitbook/assets/image (2898).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Summary step showing the source org, target orgs, and selected rules
{% endstep %}

{% step %}
### Acknowledge the confirmation

When the success message appears, click OK. The message confirms that cloning has started and may require time to complete.

<figure><img src="../../../../.gitbook/assets/image (2899).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Cloning initiated confirmation message
{% endstep %}
{% endstepper %}

## Monitor Bulk Clone Jobs

{% stepper %}
{% step %}
### Review the generated jobs

Return to the Bulk Clone Rules page. A separate row appears for each target org. Review the Job ID, Destination, Created By, Created Date, Last Run Date, Last Run By, Duration, and Status columns.

Use Refresh to retrieve the latest job status. Search, Filter By Type, Columns, pagination controls, and the items-per-page setting refine the displayed job list.

<figure><img src="../../../../.gitbook/assets/image (2900).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Bulk Clone Rules page with jobs created for the selected target orgs
{% endstep %}
{% endstepper %}

## Review Job Details

{% stepper %}
{% step %}
### Open the job information

In the Info column, select the information icon for the required job. The Bulk Clone Job Info window displays the Bulk Job ID, job type, destination, overall status, and retry count.
{% endstep %}

{% step %}
### Review rule-level results

Review each rule row to confirm the object, field type, masking style, masking value, selected fields, status, and remarks. A Partially Failed status indicates that at least one rule failed while another rule completed successfully.

<figure><img src="../../../../.gitbook/assets/image (2901).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Bulk Clone Job Info with rule-level status and remarks
{% endstep %}
{% endstepper %}

## Use Job Actions

The Actions column provides controls for the jobs displayed on the Bulk Clone Rules page. Select the applicable action to open job information, review job output, or run the supported job operation.

<figure><img src="../../../../.gitbook/assets/image (2902).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Bulk Clone Rules job list and available actions

Some job-information views display only rule configuration details. In this view, compare the source and cloned rule names, object, field type, masking style, masking value, and selected fields.

<figure><img src="../../../../.gitbook/assets/image (2903).png" alt=""><figcaption></figcaption></figure>

&#x20;                      Bulk Clone Job Info showing rule configuration details

## Status Interpretation

| **Status**          | **Meaning**                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Successfully cloned | The masking rule is created in the target org.                                                                       |
| Failed              | The rule is not cloned. Review Remarks for the cause, such as an existing rule name.                                 |
| Partially Failed    | The job contains both successful and failed rule results.                                                            |
| Skipped             | The rule does not apply to the target org because a required object or field is missing, or the rule already exists. |

## Result

The selected masking rules are processed for every selected target org. Each target org receives an individual bulk clone job, and rule-level outcomes remain available from Job History for verification and troubleshooting.
