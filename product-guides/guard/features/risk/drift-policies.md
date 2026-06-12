# Drift Policies

### Overview

**Drift Policies** in AutoRABIT Guard help you monitor meaningful changes in your Salesforce security posture over time. Instead of manually checking whether risk, user activity, or connected app behavior has changed, you can create policies that compare the latest Guard snapshot against previous historical data and notify the right users when drift is detected.

Use Drift Policies to track changes across:

* **API Security**, such as overpermissive or unverified connected apps.
* **Risk Assessment**, such as newly introduced manual or auto-resolvable risks.
* **User Activity Monitoring**, such as spikes in password changes, inactive users, or unfrozen accounts.

<figure><img src="../../../../.gitbook/assets/image (2535).png" alt=""><figcaption></figcaption></figure>

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
7. Save the policy.

When a policy is created, Guard evaluates it during the next daily drift evaluation run after the relevant daily snapshots are available.

### Create a drift policy from a template

Use templates when you want to monitor a common drift scenario quickly.

1. Go to **Risk > Drift Policies**.
2. Click **Create policy**.
3. Select **From template**.
4. Choose a template.
5. Enter a policy name.
6. Select one or more Salesforce orgs.
7. Configure notification settings.
8. Save the policy.

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
10. Save the policy.

For percentage-based conditions, enter the threshold percentage that must be exceeded before the policy triggers. For example, a condition such as “password changes increase by more than 25%” only triggers when the change between the two most recent snapshots exceeds that threshold.

### Manage Drift Policies

The Drift Policies page shows the policies configured in Guard. From this page, you can review policy statuses and take action when needed.

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

<figure><img src="../../../../.gitbook/assets/image (2537).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2538).png" alt=""><figcaption></figcaption></figure>

### How Drift Policies are evaluated

Guard evaluates Drift Policies using the same historical data used by Risk Assessment, User Activity Monitoring, and API Security.

Policies are evaluated once per day after daily snapshots are available. When a new policy is created, its first evaluation happens during the next daily run, not immediately upon saving.

If historical data is missing for any selected org or source, Guard displays a Data Unavailable status. This can happen if a source has never run, is not licensed, or has a gap in snapshot history.

### Email notifications

You can enable email notifications for a Drift Policy so selected users are notified when the policy triggers.

When email notifications are enabled:

* The **Send notification to** field is required.
* Multiple recipients can be added.
* Notifications include key context such as the policy name, org identifier, source area, and relevant links back to Guard where available.

<figure><img src="../../../../.gitbook/assets/image (2539).png" alt=""><figcaption></figcaption></figure>

### Troubleshooting

#### The policy does not trigger immediately after creation

New Drift Policies are evaluated during the next daily run after snapshots are available. They do not run immediately when saved.

#### A policy shows No data

Guard could not find the required historical data for one or more selected orgs or sources. Confirm that the relevant Guard source has run successfully and that the org is licensed for that source.

#### The Save button is disabled

Check that all required fields are complete. A policy must include at least one selected org. If email notifications are enabled, at least one eligible notification recipient is required.

#### A disabled policy is not triggering

Disabled policies do not evaluate, trigger, or send email notifications. Enable the policy to resume monitoring.
