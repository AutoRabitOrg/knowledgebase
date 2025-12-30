# Permissions Explorer

## Overview

The **Permission Explorer** feature provides deep visibility into Salesforce user access. It helps administrators quickly identify sensitive or overprivileged permissions and understand exactly how those permissions are granted. With two modes—**User Permissions** and **Object Access**—Permission Explorer makes it easier to strengthen security, maintain compliance, and prevent unauthorized access.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption><p>Permissions Explorer Home Page</p></figcaption></figure>

### Key Benefits

* **Identify Risky Access**: Detect users with sensitive or overly broad permissions.
* **Trace Permissions**: See where access comes from.
* **Explore Object Access**: Understand who can read, edit, create, or delete specific objects.
* **Predefined Templates**: Start quickly with built-in queries for common risk scenarios.
* **Compliance & Audit Support**: Demonstrate clear oversight of access control during audits.

## Modes of Permission Explorer

### 1. Explore User Permissions



*   **Quick Explorer**\
    Use predefined templates to answer critical questions such as:&#x20;

    * Who can access everything without restriction?
    * Who can deploy code directly to production?
    * Who can take over user accounts?
    * Who can grant elevated access to themselves or others?
    * Who can move large volumes of data in and out?
    * Who can weaken password policies?

    These templates accelerate common security investigations and reduce manual query building.

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Quick Explorer</p></figcaption></figure>

* **Saved Queries**\
  Any custom queries you’ve created are saved and easily accessible from the Permission Explorer homepage.
*   **Custom Explorer**\
    For deeper analysis, create your own queries by selecting permissions grouped into categories such as:

    * Access Control
    * Custom Code
    * Data Export / Data Input
    * Integration
    * Password Management
    * Super Admin Permissions (full permissions reserved for only a few trusted users)
    * User Management

    Once permissions are selected, the tool shows:

    * Which users hold the permissions
    * The **source of access** (profile or permission set)
    * A **User Detail Page** with account status, creator, and activity insights

### 2. Explore Object Access

This mode helps you evaluate **Object-level permissions** across your Salesforce orgs.

Steps:

1. Select a Salesforce org.
2. Choose **Standard** or **Custom** objects.
3. Select the type of access to check: **Read, Create, Edit,** and/or **Delete**.
4. Submit the query.

Results show:

* Which users have the selected access level.
* Why they have access (via profile or permission set).

This mode is especially useful for compliance checks and ensuring the proper protection of sensitive objects (such as customer data).

### Best Practices

* **Start with Quick Explorer**: Use templates to spot the most common and risky scenarios.
* **Audit Super Admins**: Regularly review who has full permissions and validate their necessity.
* **Save Custom Queries**: Build queries that align with your internal policies or compliance frameworks and revisit them regularly.
* **Review Object Access Quarterly**: Ensure sensitive custom objects aren’t unintentionally exposed.
* **Combine with User Activity Monitoring**: Use insights from Permission Explorer alongside activity data for a complete security picture.

## How We Determine Which Users Have Selected Permissions

To find users with specific permissions, we run complex SOQL queries (Salesforce Object Query Language) to the Salesforce org.

The queries retrieve users who are active and not frozen. The results will only show users who have the selected permissions, including those granted via profiles, permission sets, or permission set groups.

### Which Permissions Can Be Inspected?

* The list of permissions available for analysis is predefined and includes the most common permissions. Some examples might include permissions like Modify All Data, Export Reports, and Author Apex.
* **Permissions not on the list**: Currently, customers cannot inspect permissions outside the predefined list. However, if there’s demand for a specific permission, AutoRABIT’s product team can consider adding it in future releases.

### Why Use the Permissions Explorer?

* **Identify Overprivileged Users**: Quickly locate users who have excessive or unnecessary permissions, helping to enforce the principle of least privilege.
* **Simplify Permission Audits**: Gain a clear understanding of who has access to critical permissions and how they were granted, making compliance audits more efficient.
* **Enhance Security Posture**: By classifying permissions into familiar security categories, security teams can more easily identify and mitigate potential risks, aligning Salesforce permissions with traditional security policies.

### Example scenarios

1. **Security Audits**: Verify that only approved users have high-level permissions.
2. **Compliance Reviews**: Map permissions to regulatory requirements and flag risky access.
3. **Troubleshooting**: Investigate unexpected user activity by tracing their assigned permissions.
4. **Access Optimization**: Identify and reduce overprivileged accounts.



&#x20;
