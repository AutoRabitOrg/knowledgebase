# Notification Center

## Overview

The Notification Center is your in-app inbox for Guard alerts. Notifications arrive when:

* An **Authorization Policy** you are subscribed to detects a deviation.
* A **Drift Policy** triggers after detecting a meaningful change in your security posture.
* A **Real-Time Change Notification** (Change Monitoring Policy) fires based on a rule you or your team configured.

Notifications appear on the bell icon in the Guard header. Clicking “See Inbox” takes you to your personal inbox.

<figure><img src="../../../.gitbook/assets/image (5205).png" alt=""><figcaption></figcaption></figure>

## Your Inbox

Notifications are sorted by the trigger date (most recent first).

Each notification shows:

* The **source feature** (for example: Authorization Policies, Drift Policies, Change Monitoring)
* The **Salesforce org** involved, where applicable
* The **time** the notification was generated

Click the notification name to open its notification detail page.

Guard Admins can see all notifications across the platform, not just those that they are assigned to. Select **All Notifications** in the toggle under the inbox to move to this view.

<figure><img src="../../../.gitbook/assets/image (5206).png" alt=""><figcaption></figcaption></figure>

## Notification detail page

Every notification has its own detail page in Guard. It shows:

* What changed: the field, the before value and the after value.&#x20;
* Changed by: the Salesforce user who made the change
* Policy name and policy type
* The affected org
* The timestamp

You can reach the detail page from the inbox, the notification bell or the View details link in a notification email.

Standard Guard users also see a link to the policy that raised the notification. Notification users do not see the policy link, the navigation or any action controls.

If a notification has expired or been deleted, Guard shows a message that it is no longer available. If you open a notification you were not sent, Guard shows an access denied message.

## Notification emails

By default, notification emails do not include the details of the change. Each email contains a subject that names the policy and org, and a View details link. Recipients sign in to Guard to see the full detail.

This keeps security data inside Guard. Admins and tenant managers can choose to include the detail in emails instead (see below).

When AI notification summaries are turned on, the AI summary appears near the top of the email, directly under the org name and policy type.

### Turn notification detail on or off

Only Admins can see and change this setting. It applies to the whole tenant.

1. Open the Notification Centre from the bell icon at the top of the page.
2. Go to Notification Settings.
3. Find the notification detail toggle.
4. Turn it on to include detail in notifications, or off to send the "View details" link only.
5. If you are turning it on, read the warning and select **Accept** to confirm.

The toggle is off by default.

{% hint style="warning" %}
When notification detail is on, security data leaves Guard. It may be forwarded or stored by anyone who can read the inbox or channel the notification is sent to.
{% endhint %}

When the toggle is on, notifications include:

* What changed, with before and after values
* Changed by
* Policy name and policy type
* The affected org
* The timestamp
* The AI summary, if AI notification summaries are turned on
* A link to view details in Guard

The change applies to notifications sent from then on. Every change to the toggle is recorded in the audit log, with who changed it and when.

### Personal data in notifications

When detail is included in a notification, Guard masks anything that could be personal data. This includes names, email addresses, usernames, phone numbers and IP addresses, wherever they appear. Masked values keep just enough to recognise them, for example `j***@acme.com` or `J*** S***`.

AI summaries are written so that they do not include personal data.

The notification detail page inside Guard shows the full, unmasked values. Use the View details link if you need them.

## AI notification summaries

AI notification summaries give a short, plain-language explanation of each notification. They are turned on or off by a tenant manager in [Feature Controls](../getting-started-with-guard/feature-controls.md), not in Notification Settings.

Each summary uses 1 AI credit. You can see how many credits summaries have used on the AI Credit Usage page, listed as Notification Summary.

## Notification users

Notification users are people who need to receive Guard notifications but do not need access to the rest of Guard. For example, a security lead or an app owner who only needs to know when something changes.

Notification users:

* Appear in policy recipient lists alongside Guard users and Notification Groups
* Receive notification emails for the policies they are added to
* Can open the notification detail page for notifications sent to them
* Cannot see or use any other part of Guard

If a notification user signs in without a notification link, or tries to open another part of Guard, they see a Notification access only page. It explains that their account can only view notification details and asks them to open a notification email and select View details.&#x20;

To create notification users, see [User Management](../getting-started-with-guard/user-management.md).

## Archive

Notifications that are no longer needed can be archived. Archiving removes them from your main inbox without deleting them, so you can still refer back to them if needed.

To archive a notification, use the archive action on the notification item.

Archived notifications are accessible from the **Archive** tab in the notification panel.

## **Retention**

Notifications are kept for a total of 90 days before they are automatically removed.

## Notification Groups

Notification Groups let you define named sets of Guard users who should receive notifications from a particular source or policy. Instead of adding recipients one by one each time you create a policy, you create a group once and add it to the recipients list for any notification across Guard.

Only Admins can create, edit or delete Notification Groups.

<figure><img src="../../../.gitbook/assets/image (5207).png" alt=""><figcaption></figcaption></figure>

### **Create a notification group**

1. Open the Notification Settings from the bell icon at the top of the page.
2. Click **Create Notification Group**.
3. Enter a name for the group.
4. Add the Guard users who should be members.
5. Save.

The group is now available as a recipient option when configuring any policy notification.

<figure><img src="../../../.gitbook/assets/image (5208).png" alt=""><figcaption></figcaption></figure>

### **Edit and delete groups**

Open an existing group to rename it, add or remove members, or delete it. Deleting a group does not delete the policies that reference it, but may result in these policies having no recipients.

## Where Notifications Come From

The Notification Center currently receives in-app notifications from these Guard features:

| Source                                                                 | When a notification is sent                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------------- |
| Authorization Policies                                                 | A policy detects a user or permission set deviation           |
| Drift Policies                                                         | A daily evaluation finds drift above the configured threshold |
| Real-time Change Notifications (renamed to Change Monitoring Policies) | A monitored metadata change matches a configured rule         |

Each source controls who receives its notifications through the recipient settings in the policy rule. You can select individual Guard users, notification users or Notification Groups as recipients.

{% hint style="info" %}
In-app notifications are delivered in addition to email.
{% endhint %}

## Role-Based Access

| Action                                                           | Admin | Guard User | Notification user |
| ---------------------------------------------------------------- | ----- | ---------- | ----------------- |
| View their own inbox and archive notifications                   | ✅     | ✅          | ❌                 |
| Open the notification detail page for notifications sent to them | ✅     | ✅          | ✅                 |
| Create, edit and delete Notification Groups                      | ✅     | ❌          | ❌                 |
| Turn notification detail on or off                               | ✅     | ❌          | ❌                 |
| Create notification users                                        | ✅     | ❌          | ❌                 |
