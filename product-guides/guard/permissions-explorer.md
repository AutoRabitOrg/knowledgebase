# Permissions Explorer

## Overview and How It Works

The Permissions Explorer feature in AutoRABIT Guard is designed to simplify Salesforce permissions analysis by categorizing permissions into familiar IT security categories. This enables security professionals to easily evaluate Salesforce-specific permissions in the context of their organization’s security policies and better understand “who can do what” within the Salesforce org.

## Features of Permissions Explorer

### Category-Based Permissions Classification

* Permissions are grouped into traditional IT security categories, such as data access, privilege escalation, and system modification. This categorization bridges the gap between Salesforce’s unique permissions structure and traditional security practices, making it easier to understand the implications of each permission.

### Org-Level Permissions Insights

* Select any Salesforce org and a specific set of permissions to analyze. The tool will immediately identify all users who have access to those permissions, helping you locate overprivileged accounts that might pose a security risk.

### Permissions Path Visualization

* For each permission, the Permissions Explorer displays a complete path of access, including:
  * Direct assignments through profiles and permission sets.
  * Indirect assignments through permission set groups.

### Interactive and Intuitive Interface

* The tool offers two viewing modes:
  * **Diagram View**: Provides a visual representation of permissions.
  * **Tree View**: Presents a more structured and organized layout.

Both formats provide clear, actionable insights into how permissions are assigned and who has access.

## How the Permissions Explorer Works

#### Step 1: Choose Your Salesforce Org

* From the dropdown menu, select the Salesforce org you want to analyze.

#### Step 2: Select Permissions to Inspect

* Choose one or more permissions from the predefined list to investigate. This list currently includes the most common Salesforce user permissions. If you need to inspect permissions not listed, please log a support ticket.

#### Step 3: View the Results

* The Permissions Explorer will display a list of users who match the selected permissions.
* Use Diagram View or Tree View to explore how each user gained access to the permissions, including any intermediate assignments (e.g., profiles, permission sets).

#### Step 4: Take Action

* Use the insights provided to adjust profiles and permission sets directly in Salesforce to reduce overprivileged access and enforce the principle of least privilege.

### How We Determine Which Users Have Selected Permissions

To find users with specific permissions, we run complex SOQL queries (Salesforce Object Query Language) to the Salesforce org.

The queries retrieve users who are active and not frozen. The results will only show users who have the selected permissions, including those granted via profiles, permission sets, or permission set groups.

### Which Permissions Can Be Inspected?

* The list of permissions available for analysis is predefined and includes the most common permissions. Some examples might include permissions like Modify All Data, Export Reports, and Author Apex.
* **Permissions not on the list**: Currently, customers cannot inspect permissions outside the predefined list. However, if there’s demand for a specific permission, AutoRABIT’s product team can consider adding it in future releases.

### Does Guard Support Permissions Granted via Profiles or Permission Sets?

* Yes! The Permissions Explorer displays permissions granted through the following mechanisms:
  * **Profiles**: Direct assignment of permissions to users via their profile.
  * **Permission Sets**: Additional permissions granted to users via permission sets.
  * **Permission Set Groups**: Permissions granted via group permission sets.

### Why Use the Permissions Explorer?

* **Identify Overprivileged Users**: Quickly locate users who have excessive or unnecessary permissions, helping to enforce the principle of least privilege.
* **Simplify Permission Audits**: Gain a clear understanding of who has access to critical permissions and how they were granted, making compliance audits more efficient.
* **Enhance Security Posture**: By classifying permissions into familiar security categories, security teams can more easily identify and mitigate potential risks, aligning Salesforce permissions with traditional security policies.

&#x20;

&#x20;
