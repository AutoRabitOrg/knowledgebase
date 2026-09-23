# Transaction Security Policies

{% hint style="info" %}
Salesforce Event Monitoring add-on is required to use this feature. Speak to us about enabling Transaction Security Policies in your Guard instance.
{% endhint %}

{% hint style="warning" %}
You must grant the Guard user in Salesforce additional permissions to use this feature - **Modify Transaction Security Policy** and **Transaction Security Exempt**.
{% endhint %}

#### Overview

Transaction Security Policies let you detect and respond to suspicious login and API activity in your Salesforce orgs in real time. Instead of finding out after the fact that an account was accessed from an unexpected location, that sensitive data was exported, or that an unapproved app queried your org, you can have Guard automatically block the action or alert the right people the moment it happens.

Guard creates and manages the underlying Salesforce Transaction Security Policies for you.

#### Key Capabilities

**Detect suspicious activity in real time**

Evaluate login and API events against your policy conditions as they happen. When an event matches, the configured action fires immediately.

**Four policy templates**

* **Detect Large PII Exports:** Flags or blocks API and report exports of more than 2,000 Lead or Contact rows, to reduce the risk of mass exfiltration of sensitive records.
* **Impossible Travel:** Flags or blocks a login when the same user appears from two geographically distant locations within a short window. The same user logging in from, for example, London and then from Singapore forty minutes later is a strong signal of credential theft or account takeover.
* **Legacy Device Access:** Flags or blocks logins from vulnerable or outdated operating systems and devices that expand your attack surface (Android and IOS).
* **Unapproved App Access:** Monitors and blocks API query calls from connected apps that are not on your trusted-app list, so unapproved integrations cannot quietly read org data.

**Choose your response**

For each policy you decide what happens when a condition triggers:

* **Block and notify:** The Salesforce session is terminated. The user sees an access-denied message. Guard sends a notification to configured recipients.
* **Notify only:** The session proceeds. Guard sends a notification to your configured recipients so someone can investigate as a first step. Use this action during an initial rollout period to understand how often the policy fires, before switching to Block.

Notifications can be sent to individual Guard users or to a notification group.

<figure><img src="../../../../.gitbook/assets/image (2864).png" alt=""><figcaption></figcaption></figure>

**Monitor multiple orgs**

A single policy can be easily applied to multiple connected Salesforce orgs, in the same step.

#### Before you start

For each org that you want to apply Transaction Security Policies to, the Salesforce Event Monitoring license must be in place.&#x20;

**Salesforce org requirements**

Each Salesforce org must have one of the following:

* An active Salesforce Shield permission set licence
* An active Salesforce Event Monitoring permission set licence
* An active Event Monitoring Analytics Apps permission set licence
* Or be a Developer Edition org (these include the required Event Monitoring capability without a separate licence row)

If none of these apply, Guard shows the org as not eligible when you create a policy, and deployment is skipped for that org.

**Guard user permissions**

It is essential to ensure these permissions are given to the Guard integration user before attempting to use Transaction Security Policies in Guard:

1. **Modify Transaction Security Policy**
2. **Transaction Security Exempt**&#x20;

The latter is required to ensure Guard is not blocked by the Unapproved App Access Transaction Security Policy.

**What Guard enables on activation**

When you create and activate a policy, Guard turns on Salesforce Event Monitoring (real-time event streaming and storage) in the selected orgs so events can be evaluated and stored. You confirm this in Guard before a policy is saved.

#### Getting started

**Navigation path**

`Guard → Risk → Transaction Security Policies`

<figure><img src="../../../../.gitbook/assets/image (2861).png" alt=""><figcaption></figcaption></figure>

1. In Guard, open **Risk** from the primary navigation.
2. Select **Transaction Security Policies**.

<figure><img src="../../../../.gitbook/assets/image (2865).png" alt=""><figcaption></figcaption></figure>

3. Click **Create policy**.
4. Choose a policy template: **Detect Large PII Exports**, **Impossible Travel**, **Legacy Device Access**, or **Unapproved App Access**.
5. Enter a name for the policy.
6. Select the Salesforce orgs the policy should apply to.
7. Configure any template-specific options
   * For Unapproved App Access, choose the trusted connected apps
   * For Impossible Travel, add in any whitelisted IP addresses that apply
8. Set the action: **Block** or **Notify**.
9. Add the recipients who should receive the alert.
10. Save the policy.

Guard creates the corresponding Salesforce Transaction Security Policy in each selected org. The policy is active immediately after saving.

#### Create a Detect Large PII Exports policy

Use this template when you want to stop or alert on large Lead or Contact exports through the API or reports.

<figure><img src="../../../../.gitbook/assets/image (2867).png" alt=""><figcaption></figcaption></figure>

The policy fires when more than 2,000 Lead or Contact rows are processed in a single API or report event. That threshold is fixed in the template. We recommend setting the action to **Block & Notify**.

#### Create an Impossible Travel policy

Use this template to catch sessions that originate from geographically impossible locations relative to a user’s previous login.

<figure><img src="../../../../.gitbook/assets/image (2868).png" alt=""><figcaption></figcaption></figure>

Guard looks at distinct source IPs for the same user within a short window. If more than one IP appears, the policy triggers. Recommended action is **Notify Only.**

{% hint style="info" %}
VPN usage and split-tunnelling can produce false positives, since a user’s apparent location may jump between the VPN exit point and their actual location. Review flagged sessions carefully before using the Block action in environments with broad VPN usage.
{% endhint %}

#### Create a Legacy Device Access policy

Use this template when you want to restrict or alert on logins from outdated or vulnerable devices and operating systems.

<figure><img src="../../../../.gitbook/assets/image (2869).png" alt=""><figcaption></figcaption></figure>

The policy evaluates the login platform. Logins from Android versions below 5, and iOS versions below 25, are flagged. Recommended action is **Block & Notify**.

#### Create an Unapproved App Access policy

{% hint style="danger" %}
Before using this policy, please ensure you have first given the Guard user **Transaction Security Exempt** as a permission in Salesforce. Otherwise, you could block Guard and loose functionality across the app.
{% endhint %}

Use this template to stop unapproved connected apps from running API query calls against your org.

<figure><img src="../../../../.gitbook/assets/image (2871).png" alt=""><figcaption></figcaption></figure>

When you create the policy, choose which of your connected apps are trusted. Any API query from an app that is not on that list triggers the policy. Other API operations are not evaluated. Recommended action is **Block & Notify**.

{% hint style="info" %}
Leave the trusted-app list empty only if you intend to flag every connected-app query.
{% endhint %}

#### Manage policies

The Transaction Security Policies list shows all your configured policies. From this page you can:

* See each policy’s name, type, orgs, active status and configured action.
* Open a policy to review its configuration and event history, make edits or disable it.
* Disabling a policy does not delete it.
* Edit a policy to change orgs, action or recipients.
* Delete a policy when it is no longer needed. Deleting requires confirmation and also removes the underlying Salesforce Transaction Security Policy from the connected orgs.

<figure><img src="../../../../.gitbook/assets/image (2872).png" alt=""><figcaption></figcaption></figure>

#### How Guard and Salesforce interact

Guard manages Transaction Security Policies through the Salesforce Metadata API. When you create or update a policy in Guard, it writes the corresponding configuration to Salesforce. When you delete a policy, the Salesforce policy is also removed.

Policy evaluation itself happens in Salesforce, not in Guard. Salesforce assesses each login event against the policy conditions in real time. When a condition matches, Salesforce applies the configured action (Block or Notify) and sends the result back to Guard so it can be recorded in the event history.

Because Salesforce handles evaluation, the speed and reliability of detection depends on Salesforce’s event processing. There is no additional polling delay introduced by Guard.

#### Roles and permissions

{% hint style="info" %}
Only Guard **Admins** can create, edit, enable, disable or delete Transaction Security Policies. Standard users and Support Engineers can view policies and event history, but cannot change them.
{% endhint %}

#### Troubleshooting

**A policy does not appear in the Salesforce Setup menu**

Guard creates the Salesforce Transaction Security Policy during the save operation. If the policy does not appear in Salesforce Setup within a few minutes, check that the connected org is still active in Guard and that the org connection has the required permissions.

**A Salesforce session was blocked for a legitimate user**

Disable the policy or switch the action to Notify while you investigate.

* **Impossible Travel** — check whether the user is on a VPN or proxy that makes their location appear to jump.
* **Legacy Device Access** — confirm the device or OS they used should still be allowed, or that the login platform string is what you expect.
* **Detect Large PII Exports** — confirm the export size and whether Lead or Contact data was intentionally included.
* **Unapproved App Access** — add the connected app to the trusted-app list if it is a known integration.

**The policy has never triggered despite expected activity**

Confirm the policy is enabled and that the selected orgs are the ones where the activity is occurring. Check Salesforce’s own Transaction Security event log to see whether the event was evaluated and what the outcome was.
