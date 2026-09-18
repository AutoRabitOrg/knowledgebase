# Notification Center

## Overview

The Notification Center is your in-app inbox for Guard alerts. Notifications arrive when:

* An **Authorization Policy** you are subscribed to detects a deviation.
* A **Drift Policy** triggers after detecting a meaningful change in your security posture.
* A **Real-Time Change Notification** (Change Monitoring Policy) fires based on a rule you or your team configured.

Notifications appear on the bell icon in the Guard header. Clicking “See Inbox” takes you to your personal inbox.

<figure><img src="../../../.gitbook/assets/image (2857).png" alt=""><figcaption></figcaption></figure>

## Your Inbox

Notifications are sorted by the trigger date (most recent first).

Each notification shows:

* The **source feature** (for example: Authorization Policies, Drift Policies, Change Monitoring)
* The **Salesforce org** involved, where applicable
* The **time** the notification was generated

Clicking a notification takes you to the relevant policy in Guard where you can investigate further.

Guard Admins can see all notifications across the platform, not just those that they are assigned to. Select **All Notifications** in the toggle under the inbox to move to this view.

<figure><img src="../../../.gitbook/assets/image (2858).png" alt=""><figcaption></figcaption></figure>

## Archive

Notifications that are no longer needed can be archived. Archiving removes them from your main inbox without deleting them, so you can still refer back to them if needed.

To archive a notification, use the archive action on the notification item.

Archived notifications are accessible from the **Archive** tab in the notification panel.

## **Retention**

Notifications are kept for a total of 90 days before they are automatically removed.

## Notification Groups

Notification Groups let you define named sets of Guard users who should receive notifications from a particular source or policy. Instead of adding recipients one by one each time you create a policy, you create a group once and add it to the recipients list for any notification across Guard.

Only Admins can create, edit or delete Notification Groups.

<figure><img src="../../../.gitbook/assets/image (2859).png" alt=""><figcaption></figcaption></figure>

### **Create a notification group**

1. Open the Notification Settings from the bell icon at the top of the page.
2. Click **Create Notification Group**.
3. Enter a name for the group.
4. Add the Guard users who should be members.
5. Save.

The group is now available as a recipient option when configuring any policy notification.

<figure><img src="../../../.gitbook/assets/image (2860).png" alt=""><figcaption></figcaption></figure>

### **Edit and delete groups**

Open an existing group to rename it, add or remove members, or delete it. Deleting a group does not delete the policies that reference it, but may result in these policies having no recipients.

## Where Notifications Come From

The Notification Center currently receives in-app notifications from these Guard features:

| Source                                                                 | When a notification is sent                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------------- |
| Authorization Policies                                                 | A policy detects a user or permission set deviation           |
| Drift Policies                                                         | A daily evaluation finds drift above the configured threshold |
| Real-time Change Notifications (renamed to Change Monitoring Policies) | A monitored metadata change matches a configured rule         |

Each source controls who receives its notifications through the recipient settings in the policy rule. You can select individual Guard users or Notification Groups (or both) as recipients.

{% hint style="info" %}
If you were previously receiving email notifications from these features, those emails will continue as before. In-app notifications are delivered in addition to email.
{% endhint %}

## Role-Based Access

All Guard users can view notifications in their personal inbox and archive them.

Only **Admins** can create, edit and delete Notification Groups.
