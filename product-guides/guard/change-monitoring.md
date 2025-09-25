# Change Monitoring

## Overview

Change Monitoring in AutoRABIT Guard provides an enhanced, comprehensive Audit trail for your Salesforce org. Built on top of Salesforce’s native Setup Audit Trail, Change Monitoring significantly improves visibility and accountability for changes made in the production environment. Whether changes occur directly in Salesforce, through AutoRABIT deployments, or via other methods, Change Monitoring captures them, organizes them, and presents them in an accessible and actionable way.

With Change Monitoring, you can ensure complete visibility into every change made in your Salesforce org, making it an invaluable tool for security, governance, and compliance.

## Features of Change Monitoring

### Executive View

The Executive View in Change Monitoring provides a high-level dashboard for at-a-glance viewing:

* Summarizes all changes made in the last 7 days, categorized by type (e.g., custom code, configuration changes).
* Offers a quick snapshot of recent activity—ideal for executives and managers who need to monitor trends without delving into the details.&#x20;
* Ensures teams can quickly identify high-level patterns and address critical areas as needed.

### Detail View

For a more granular analysis, the Detail View presents a table of all changes with advanced filtering capabilities. It includes important metadata such as:

* **Changed at**: Timestamp of the change.
* **Metadata Type**: Type of Salesforce component affected (e.g., Apex class, custom object).
* **Record Name**: The specific item that was changed.
* **Change Type**: Indicates whether the change was an addition, modification, or deletion.
* **Changed By**: The user responsible for the change.
* **Change Category**: Groups changes into logical categories (e.g., back-end code, security).

This level of detail enables users to fully investigate specific changes and identify patterns or issues in their Salesforce org.

### Smart Filtering

Smart Filtering allows users to filter changes by:

* **Who**: Identify and track which users made changes.
* **When**: Focus on changes within a specific date or time range.
* **What Type**: Narrow down metadata changes by component, like Apex classes, flows, or profiles.

This feature helps teams quickly pinpoint the exact changes they need to focus on, whether it's for audits, troubleshooting, or general monitoring.

### Enhanced Visibility

Change Monitoring provides enhanced visibility into changes from multiple sources, including:

* Direct edits in production.
* Changes deployed via AutoRABIT.
* Other deployment or modification methods.

This ensures that every change, regardless of its origin, is captured and tracked with full context, allowing teams to investigate unexpected or unauthorized changes quickly.

## Benefits of Change Monitoring

### Complete Audit Trail

* Gain full visibility into every modification in your org, ensuring transparency and accountability.

### Streamlined Investigations

* Use advanced filters to quickly pinpoint specific changes, saving time during audits or troubleshooting sessions.

### Improved Governance

* Ensure compliance with internal policies and external regulations by keeping a detailed log of all modifications made in your org.

### Enhanced Collaboration

* Help developers, admins, and security teams stay aligned by providing a single source of truth for all changes.

## How Change Monitoring Works

Change Monitoring builds upon the Salesforce Setup Audit Trail by using the Tooling API to retrieve the full log, which contains up to six months of historical data. However, where Salesforce's native audit trail offers only basic information, Change Monitoring enriches this data to provide deeper insights.

### Tracking Changes

Change Monitoring tracks changes using the SetupAuditTrail object and retrieves all relevant data available via this API. The data is processed to convert simple string representations of changes into more complex, structured objects.

For example, the Salesforce raw data for a change might look like this:

* Salesforce Raw Event: "Changed permission set Admin : Account Perms: AccountOwnership Apex class access was enabled."

Change Monitoring enhances this raw event into a detailed object like this:

`{`\
&#x20; `"detail": "Changed permission set Admin : Account Perms: AccountOwnership Apex class access was enabled",`\
&#x20; `"login": "`[`uat@pablogonzalez.io`](mailto:uat@pablogonzalez.io)`",`\
&#x20; `"auditTrailId": "0YmWy000004AydKKAS",`\
&#x20; `"date": "2024-10-10T09:30:47.000+0000",`\
&#x20; `"error": "",`\
&#x20; `"eventKey": "SetupEntityAccessAudit_PermissionSet_ApexClass_Enabled",`\
&#x20; `"recordName": "Admin_Account_Perms",`\
&#x20; `"propertyModified": "classAccesses",`\
&#x20; `"subPropertyModified": "AccountOwnership",`\
&#x20; `"beforeValue": "disabled",`\
&#x20; `"afterValue": "enabled",`\
&#x20; `"changeCategory": "Attribute-Based Access Control (ABAC)",`\
&#x20; `"recordId": "0PSWy000000TnN7OAK",`\
&#x20; `"metadataType": "PermissionSet",`\
&#x20; `"operationType": "MODIFIED",`\
&#x20; `"isMetadata": true,`\
&#x20; `"riskLevel": "High Risk"`\
`}`\


This enriched event provides:

* **Context**: Who made the change, when it was made, and which component was affected.
* **Detailed Impact**: What specifically was modified, e.g., access permissions, profile settings.
* **Risk Level**: An assigned risk level, which categorizes the change by its security impact.

### Event Parsing and Categorization

When a change is captured, it undergoes transformation:

* Regex-based parsing of raw data.
* Real-time Salesforce queries to gather additional metadata details.
* Categorization based on predefined change types, e.g., profile modifications, security changes.

This detailed parsing and categorization process allows teams to perform a deep analysis of changes that could have security implications.

### Tracking Supported Events

* Change Monitoring enhances and tracks events related to various Salesforce components. Currently, the following metadata types are supported:

\[

&#x20; 'GlobalValueSet',

&#x20; 'QueueRoutingConfig',

&#x20; 'StaticResource',

&#x20; 'ApexPage',

&#x20; 'CustomTab',

&#x20; 'CompactLayout',

&#x20; 'Group',

&#x20; 'WorkflowTask',

&#x20; 'WorkflowRule',

&#x20; 'WorkflowAlert',

&#x20; 'ApprovalProcess',

&#x20; 'PasswordPolicy',

&#x20; 'DataCategoryAccess',

&#x20; 'SharingGuestRule',

&#x20; 'SharingCriteriaRule',

&#x20; 'SharingOwnerRule',

&#x20; 'Role',

&#x20; 'WebLink',

&#x20; 'CustomPermission',

&#x20; 'PermissionSet',

&#x20; 'QuickAction',

&#x20; 'RecordType',

&#x20; 'Queue',

&#x20; 'WorkflowFieldUpdate',

&#x20; 'FlexiPage',

&#x20; 'FieldSet',

&#x20; 'CustomObject',

&#x20; 'ValidationRule',

&#x20; 'LightningComponentBundle',

&#x20; 'Profile',

&#x20; 'AuraDefinitionBundle',

&#x20; 'CustomMetadata',

&#x20; 'User',

&#x20; 'PermissionSetAssignment',

&#x20; 'ProfileSessionSetting',

&#x20; 'CustomField',

&#x20; 'ApexClass',

&#x20; 'ApexTrigger',

&#x20; 'Flow',

&#x20; 'Layout',

&#x20; 'ProfilePasswordPolicy',

&#x20; 'ExternalCredential',

&#x20; 'RemoteSiteSetting',

&#x20; 'NamedCredential',

&#x20; 'AuthProvider',

&#x20; 'ExternalDataSource'

]

**Not All Events Are Parsed**: While Change Monitoring tracks a wide variety of changes, only certain events are parsed into rich objects. Others are logged and stored but not parsed into detailed objects. Users can view these unparsed events in the “Other” tab.

### Data Retention and Refresh

* **Data Retention**: Change Monitoring can store up to one year of historical data, far more than the six-month limit imposed by Salesforce's native audit trail.
* **Refresh Rate**: The audit trail is refreshed every five minutes, meaning changes made in Salesforce are captured in near real time. Users can also manually trigger a refresh.

&#x20;
