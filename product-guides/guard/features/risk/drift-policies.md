# Drift Policies

### Overview

**Drift Policies** in AutoRABIT Guard help you monitor meaningful changes in your Salesforce security posture over time. Instead of manually checking whether risk, user activity, or connected app behavior has changed, you can create policies that compare the latest Guard snapshot against previous historical data and notify the right users when drift is detected.

Use Drift Policies to track changes across:

* **API Security**, such as overpermissive or unverified connected apps.
* **Risk Assessment**, such as newly introduced manual or auto-resolvable risks.
* **User Activity Monitoring**, such as spikes in password changes, inactive users, or unfrozen accounts.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2Fd3wZRI8g2Pns6LAPOJ1S%2Fimage.png?alt=media&#x26;token=6b0339c8-94ba-4578-87b3-771965a56cd7" alt=""><figcaption></figcaption></figure>

### Key capabilities

#### Create policies from templates

Templates help you quickly monitor common drift scenarios without building conditions manually. Each template is designed around a high-signal security change, such as a new risky connected app or a sudden increase in inactive users.

Available templates include:

* **Overpermissive or unverified apps**
* **New risk exposure detected**
* **Spike in password changes**
* **Unexpected account reinstatement**
* **Unexpected rise in inactive accounts**

#### Create custom drift policies

Custom policies let you choose exactly which historical data points to monitor. You can create conditions across API Security, Risk Assessment, and User Activity Monitoring, then decide whether the policy should trigger on any change, an increase, a decrease, or a percentage-based change.

#### See immediate evaluation results

When immediate evaluation is enabled for a new policy, Guard evaluates the policy after it is saved and shows the result. The result tells you whether drift was detected, no matching change was found or there was not enough snapshot history for selected orgs or data sources.

If drift is detected, you can open the trigger details directly from the result. If evaluation cannot run for some orgs or data sources, the policy is still saved.

#### Monitor multiple orgs

A Drift Policy can be applied to one or more Salesforce orgs. Guard evaluates the selected policy conditions for each org included in the policy.

#### Receive email notifications

When notifications are enabled, Guard sends an email when a Drift Policy is triggered. Only Guard admins can configure email notifications.

#### Manage policies over time

You can enable, disable, edit, and delete Drift Policies as your monitoring needs change. Disabled policies do not trigger or send notifications.

### Getting started

1. In AutoRABIT Guard, open **Risk** from the primary navigation.
2. Select **Drift Policies**.
3. Click **Create policy**.
4. Choose whether to create the policy **From template** or **Custom**.
5. Select the Salesforce orgs the policy should monitor.
6. Configure the policy conditions and notification settings.
7. Choose whether to evaluate the policy immediately after saving.
8. Save the policy.

If immediate evaluation is enabled, Guard checks the policy after it is saved and opens a result dialog when the evaluation completes. Otherwise, the policy is evaluated during the next daily drift evaluation run after the relevant daily snapshots are available.

### Create a drift policy from a template

Use templates when you want to monitor a common drift scenario quickly.

1. Go to **Risk > Drift Policies**.
2. Click **Create policy**.
3. Select **From template**.
4. Choose a template.
5. Enter a policy name.
6. Select one or more Salesforce orgs.
7. Configure notification settings.
8. Choose whether to evaluate the policy immediately after saving.
9. Save the policy.

Guard adds the policy to the Drift Policies list with its name, selected orgs, and enabled status.

### Create a custom drift policy

Use a custom policy when you want more control over what Guard monitors.

1. Go to **Risk > Drift Policies**.
2. Click **Create policy**.
3. Select **Custom**.
4. Select one or more Salesforce orgs.
5. Choose the source area to monitor, such as **API Security**, **Risk Assessment**, or **User Activity Monitoring**.
6. Add one or more conditions.
7. Choose how conditions should be evaluated:
   * **Any change**
   * **Any increase**
   * **Any decrease**
   * **% increase**
   * **% decrease**
8. Choose whether multiple conditions should use **AND** or **OR** logic.
9. Configure notification settings.
10. Choose whether to evaluate the policy immediately after saving.
11. Save the policy.

For percentage-based conditions, enter the threshold percentage that must be exceeded before the policy triggers. For example, a condition such as “password changes increase by more than 25%” only triggers when the change between the two most recent snapshots exceeds that threshold.

### Manage Drift Policies

The Drift Policies page shows the policies configured in Guard. From this page, you can review policy statuses and take action when needed.

By default, the newest policies appear first. You can change the sort order from the column headers.

The list includes key policy details such as:

* Policy name
* Selected orgs
* Source or domain
* Enabled status
* Number of times triggered
* Last triggered date, or **Never** if the policy has not triggered

### View Drift Policy details

Open a policy to review its configuration and trigger history. The detail page helps you understand what the policy monitors, which orgs it applies to, and when it last detected drift.

Policy details include:

* Policy name
* Selected orgs
* Source area (Domain)
* Notification recipients
* Trigger history

You can take action by:

* **Enable** a policy to begin evaluation.
* **Disable** a policy to stop it from triggering or sending emails.
* **Edit** a policy to update org selection, custom conditions, or email settings.
* **Delete** a policy when it is no longer needed.

Deleting a policy requires confirmation before the policy is removed.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FCfLKx8G3U7yyDZtCFW8P%2Fimage.png?alt=media&#x26;token=d0ce922a-b16d-4519-978a-7b54c1f97ad0" alt=""><figcaption></figcaption></figure>

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FQeZXOLlsApSmemDcD8Xw%2Fimage.png?alt=media&#x26;token=9d2b30a1-d7ff-43b9-9ada-06694cdeba03" alt=""><figcaption></figcaption></figure>

### How Drift Policies are evaluated

Guard evaluates Drift Policies using the same historical data used by Risk Assessment, User Activity Monitoring, and API Security.

Policies are evaluated once per day after daily snapshots are available. A new policy can also be evaluated immediately after saving when immediate evaluation is enabled.

Immediate evaluation compares the latest available snapshots. The result can show:

* Drift detected
* No drift detected
* Evaluation could not run because there is not enough snapshot history
* A mixed result where some orgs or data sources could be checked and others could not

If historical data is missing for any selected org or source, Guard displays a Data Unavailable status. This can happen if a source has never run, is not licensed, or has a gap in snapshot history.

### Email notifications

You can enable email notifications for a Drift Policy so selected users are notified when the policy triggers.

When email notifications are enabled:

* The **Send notification to** field is required.
* Multiple recipients can be added.
* Notifications include key context such as the policy name, org identifier, source area, and relevant links back to Guard where available.

<figure><img src="https://1912836914-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F9vAxMuDrkUkB4OXlH9CL%2Fuploads%2FldRg3gnhFktLLTcZTswT%2Fimage.png?alt=media&#x26;token=b20fe9a7-aa52-4b21-9266-06fe6a789b6a" alt=""><figcaption></figcaption></figure>

### Troubleshooting

#### The policy does not show an immediate result after creation

Confirm that immediate evaluation was enabled before saving the policy. If it was not enabled, Guard evaluates the policy during the next daily run after snapshots are available.

If immediate evaluation was enabled but some orgs or data sources could not be checked, review the result dialog. Guard may need at least two snapshots before it can compare changes.

#### A policy shows No data

Guard could not find the required historical data for one or more selected orgs or sources. Confirm that the relevant Guard source has run successfully and that the org is licensed for that source.

#### The Save button is disabled

Check that all required fields are complete. A policy must include at least one selected org. If email notifications are enabled, at least one eligible notification recipient is required.

#### A disabled policy is not triggering

Disabled policies do not evaluate, trigger, or send email notifications. Enable the policy to resume monitoring.
