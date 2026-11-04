# Authorization Policies

## Overview

The Authorization Policies feature in AutoRABIT Guard offers a powerful, automated mechanism to enforce governance and security in your Salesforce org. Unlike Salesforce’s native functionality, Guard Authorization Policies allow you to define strict rules, such as permission set allow lists, to ensure only authorized users can access sensitive permissions.

Guard monitors your org in real time, detects violations, and can immediately act by reverting changes or notifying admins.&#x20;

## Key Features

### Permission Set Allow List Authorization Policies

Permission Set Allow List Authorization Policies allow you to limit who can be assigned specific permission sets. For example, you can define an Authorization Policy that ensures only certain users are allowed to have a permission set that provides access to critical data.

* **Prevent unauthorized access:** Prevent unauthorized users from being granted permissions that expose sensitive data.
* **Ensure compliance**: Enforce strict Authorization Policies for who can access certain permissions, ensuring compliance with both internal and external regulatory standards.

### Real-Time Monitoring and Enforcement

Guard continuously scans your Salesforce org every five minutes to detect violations in real time.

* **Continuous Monitoring:** Guard scans your org every five minutes, identifying and responding to Authorization Policy violations quickly.
* **Violation Actions:** When an Authorization Policy violation is detected, Guard can:
  * Revert Changes Immediately: Automatically remove unauthorized permission sets, reverting the change to a compliant state.
  * Notify Admins: Alert admins via email to manually review and resolve the violation.

### Flexible Authorization Policy Configuration

Guard allows you to easily configure Authorization Policies that fit your specific needs.

* **Criteria:** Select the permission sets and users involved. Use criteria groups to create flexible rules that suit you.
* **Remediation Actions:** Define how violations should be handled, whether by automatically reverting the change or notifying admins.&#x20;
* **Notifications:** You can specify which email addresses will receive notifications, and use Notification Groups to send an email to a team or set of stakeholders who should review the policy breach.&#x20;

### Detailed Violation Notifications

When Guard detects an Authorization Policy violation, you receive detailed alerts that give you the information necessary to quickly resolve the issue.

* The alert will include:
  * The permission set involved in the violation.
  * The user assigned the permission set.
  * The action taken, whether the permission set was reverted, or the admin was notified.

### Scalable Governance Framework

Guard’s Authorization Policies are just the beginning. The platform is designed to scale with your organization’s needs and will soon include other capabilities, such as password and governance rules.

* Future releases will expand the types of Authorization Policies available, offering even more granular control over your org’s security and compliance.

## Why Authorization Policies Matter

### Enforce Governance with Automation

Guard automates the enforcement of access rules, ensuring that your org remains compliant without manual oversight. This eliminates the risk of human error and guarantees consistent application of security Authorization Policies.

* Automation means fewer missed violations, less time spent managing security, and more time spent focusing on other business-critical tasks.

### Protect Sensitive Data

By controlling who has access to what permissions, Guard ensures that unauthorized users do not gain access to sensitive business data, such as financial, medical, or proprietary information.

* Enforcing permission set Authorization Policies helps prevent data breaches and keeps sensitive information secure.

### Maintain Compliance

Guard helps your organization meet both internal governance standards and external regulatory requirements by ensuring real-time enforcement of your Authorization Policies.

* Guard ensures compliance with both industry standards (e.g., HIPAA, SOX) and your organization’s internal security Authorization Policies.

### Boost Efficiency

Guard’s Authorization Policies can automatically revert violations or send actionable alerts for manual review, saving your team time and effort.

* Authorization Policies reduce the burden of constant manual oversight, giving your team time to focus on more strategic tasks.

## How It Works

### Create an Authorization Policy

To create an Authorization Policy, go to the Authorization Policies section in AutoRABIT Guard and click "Create Authorization Policy":

1. Choose whether to create an Authorization Policy based on permissions _or_ permission sets.
2. Provide a descriptive name for the Authorization Policy, such as "Authorization Policy for Admin Permissions."
3. Choose the Authorization Type:
   1. Based on criteria. (You'll set-up the criteria on the next page).
   2. Specific users. Use this option if you already know who or what you want to monitor.&#x20;
4. Select the Salesforce org from the drop-down list. This is where the policy will be applied.
5. Now configure your policy.&#x20;
   1. Select the permissions or permission sets you want to monitor. You can select multiple from the drop-down list.
   2. If you chose "Specific users" as the authorization type, now select the users that are _allowed_ to access the permissions. The policy will then be applied to all other users in the org.
   3. If you're using criteria, now set how you'd like to choose the users _allowed_ to access the selected permissions.
      1. You can do this based on one or more of Profile, Role, Company Name, Email Domain and License Type.&#x20;
      2. Add a field to set another AND criteria.
      3. And a group to create a stacked set of criterion, where OR is between each group. You can only stack to one level (i.e. you can't have a group within a group).&#x20;
      4. Select the Operator NOT IN when building complex sets of criterion, to exclude the entered values from the policy.&#x20;
6. Now set the remediation action.
   1. Auto-Revert and Notify: Violations trigger an automatic revert, as well as a notification.
   2. Notify only: A notification is sent to the users specified, for manual remediation.
7. Email Notifications: Specify the Guard users who should receive violation alerts.&#x20;

### Activate and Monitor

* Save and Activate: After configuring the Authorization Policies, save it and activate it.
* Real-Time Monitoring: Guard will continuously monitor your Salesforce org every five minutes, ensuring that any violations are detected and acted upon in real time.

## How Authorization Policy Violations Are Detected and Handled

Guard’s Authorization Policy detection relies heavily on the Change Monitoring capability, which tracks changes in your Salesforce org. When an Authorization Policy is violated, Guard parses these changes to determine if they violate the defined rules.

## **Parsing Events: How Changes Are Monitored**

Guard is built on top of Change Monitoring, which uses Salesforce’s SetupAuditTrail to track changes. When a change occurs that might violate an Authorization Policy, Guard parses the event details to determine whether the violation is valid. Let’s look at an example of how this works:

1. Change Event Detection: A change occurs, such as the assignment of a permission set to a user:
   1. Event: "Permission set Nebula Logger: Admin assigned to user Authorization Policy user (UserID: \[005Wy000000uRLh])"
2. Before and After Values: Guard detects and extracts the before and after values from the event. In this case:
   1. Before Value: The user did not have the permission set assigned.
   2. After Value: The permission set is now assigned to the user.
3. Event Parsing: Guard uses this information to determine the permission set involved ("Nebula Logger: Admin") and the user assigned to it (\[005Wy000000uRLh]).
4. Authorization Policy Comparison: Guard then checks whether this event violates any existing Authorization Policies:
   1. If there is a Permission Set Allow List Authorization Policy for "Nebula Logger: Admin," Guard checks whether the user is on the allow list.
   2. If the user is not on the allow list, the event is flagged as a violation.
5. Reverting the Offending Change: If the violation is detected, Guard automatically reverts the change (i.e., removes the unauthorized permission set from the user), ensuring compliance.
6. Email Alerts: If the Authorization Policy is configured to notify admins instead of automatically reverting the change, an email alert is triggered, providing admins with all relevant details.

## Handling Special Cases

Some Authorization Policies, such as those based on specific permissions (e.g., only user A, B, and C can have the "Modify All Data" permission), require additional logic to determine whether a violation has occurred.

For example:

* Guard tracks permission set assignments and checks if specific permissions (like "Author Apex") are granted to users.
* If an Authorization Policy specifies that only certain users can have a permission set that grants "Author Apex," Guard will remove the permission set from any user not on the allow list.

Currently, Guard does not handle edge cases where permission sets are modified after being assigned. For example, if a user already has a permission set and it is modified to include a new permission, Guard will not automatically remove the permission set until the assignment itself is changed. This limitation will be addressed in future releases.

&#x20;
