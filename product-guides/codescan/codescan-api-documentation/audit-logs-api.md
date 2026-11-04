# Audit Logs API

#### Introduction / Overview <a href="#introduction-overview" id="introduction-overview"></a>

The **Audit Logs API** provides a structured way to retrieve audit log records for a given organization. It is designed to help administrators **track and review actions performed within the system** by capturing detailed event data.

This API returns audit events based on **filter criteria provided in the request body**, allowing users to narrow down results using:

* Organization identifier (organizationKey)
* User who performed the action (userLogin)
* Audit category (category)
* Operation performed (operation)
* Event timestamp (createdAt)D
* Trigger source (userTriggered)x\`

Each audit log entry includes:

* The **user or system** that initiated the action
* The **type of operation performed**
* The **category of the event**
* The **timestamp of occurrence**
* The **resulting value or change (**&#x6E;ewValu&#x65;**)**

The API supports **pagination via query parameters**, enabling efficient retrieval of large audit datasets.

#### Permissions Required <a href="#permissions-required" id="permissions-required"></a>

Access to this API is restricted to:

* **Organization Admin**
* **Super Admin**

#### Endpoint Details <a href="#endpoint-details" id="endpoint-details"></a>

* **HTTP Method:** POST
* **URL:** \<CODESCAN\_DOMAIN\_URL>/\_codescan/audit/logs?p=\<PAGE\_NUMBER>\&ps=\<PAGE\_SIZE>

***

#### Request Body <a href="#request-body" id="request-body"></a>

{% code lineNumbers="true" %}
```
{
  "organizationKey": "<ORG_KEY>",
  "userLogin": "<USER_LOGIN>",
  "category": "<CATEGORY>",
  "operation": "<OPERATION>",
  "createdAt": "<DATE>",
  "userTriggered": <BOOLEAN>
}

```
{% endcode %}

#### Request Field Details <a href="#request-field-details" id="request-field-details"></a>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th width="172"></th></tr></thead><tbody><tr><td><strong>Field</strong></td><td><strong>Type</strong></td><td><strong>Required</strong></td><td><strong>Description</strong></td><td><strong>Possible Values</strong></td></tr><tr><td><code>organizationKey</code></td><td>string</td><td>Yes</td><td>Organization key</td><td>—</td></tr><tr><td><code>userLogin</code></td><td>string</td><td>No</td><td>Login of user who triggered the action</td><td>—</td></tr><tr><td><code>category</code></td><td>string</td><td>No</td><td>Audit log category</td><td>PROJECT, USER_TOKEN, GROUP_PERMISSION, PERMISSION_TEMPLATE, PLUGIN, PROPERTY, QUALITY_GATE, QUALITY_PROFILE, USER, USER_GROUP, USER_PERMISSION</td></tr><tr><td><code>operation</code></td><td>enum</td><td>No</td><td>Operation performed</td><td>ADD, ADD_CHARACTERISTIC, ADD_EDITOR, ADD_GROUP, ADD_USER, DEACTIVATE, DELETE, DELETE_EDITOR, DELETE_GROUP, DELETE_USER, COMPONENT_KEY_UPDATE, COMPONENT_KEY_BRANCH_UPDATE, SET, SET_LICENSE, UPDATE, UPDATE_CHARACTERISTIC, UPDATE_COMPONENT_VISIBILITY</td></tr><tr><td><code>createdAt</code></td><td>string</td><td>No</td><td>Creation date or datetime of the audit event</td><td>Format: yyyy-MM-dd or yyyy-MM-dd'T'HH:mm:ssZExample: 2017-10-19 or 2017-10-19T13:00:00+0200</td></tr><tr><td><code>userTriggered</code></td><td>boolean</td><td>No</td><td>Whether the event was triggered by a user action</td><td>true, false</td></tr><tr><td><code>p</code></td><td>integer</td><td>No</td><td>The results page number.</td><td>1</td></tr><tr><td><code>ps</code></td><td>integer</td><td>No</td><td>The amount of results on each page.  Max is 500</td><td>500</td></tr></tbody></table>

#### Example Request <a href="#example-request" id="example-request"></a>

{% code lineNumbers="true" %}
```
POST https://app.codescan.io/_codescan/audit/logs?p=1&ps=10
```
{% endcode %}

{% code lineNumbers="true" %}
```
{
  "organizationKey": "org1",
  "userLogin": "652d14eeedabb7xxxxxd",
  "category": "PROJECT",
  "operation": "UPDATE",
  "createdAt": "2025-07-14",
  "userTriggered": true
}
```
{% endcode %}

#### Example Response <a href="#example-response" id="example-response"></a>

{% code lineNumbers="true" %}
```
{
  "content": [
    {
      "organizationUuid": "org-uuid-123",
      "userLogin": "jdoe",
      "userUuid": "user-uuid-456",
      "category": "PROJECT",
      "operation": "UPDATE",
      "newValue": "<changed value>",
      "createdAt": "2025-07-14T09:00:12.314+00:00",
      "userTriggered": true
    }
  ],
  "pageable": {
    "pageNumber": 0,
    "pageSize": 100
  },
  "totalElements": 1,
  "totalPages": 1,
  "first": true,
  "last": true,
  "empty": false
}
```
{% endcode %}

#### Response Field Details <a href="#response-field-details" id="response-field-details"></a>

**Audit Log Entry** (`content`)

| Field              | Description                                          |
| ------------------ | ---------------------------------------------------- |
| `organizationUuid` | Unique identifier of the organization                |
| `userLogin`        | Login of the user who performed the action           |
| `userUuid`         | Unique identifier of the user                        |
| `category`         | Audit log category                                   |
| `operation`        | Operation performed                                  |
| `newValue`         | Updated value or details of the change (JSON string) |
| `createdAt`        | Timestamp of the audit event                         |
| `userTriggered`    | Indicates whether the action was triggered by a user |

**Example: Project Analysis Event**

{% code lineNumbers="true" %}
```
{
  "category": "PROJECT_ANALYSIS",
  "operation": "ADD",
  "userLogin": "System",
  "userTriggered": false,
  "newValue": {
    "projectKey": "prod-project",
    "projectName": "prod-project",
    "jobId": "aefe9a9e-d8cf-4faa-811b-7ebc4ab8a0ca",
    "ncloc": "335"
  }
}

```
{% endcode %}

***

**Example: Group permission Assignment**

{% code lineNumbers="true" %}
```
{
  "category": "GROUP_PERMISSION",
  "operation": "ADD",
  "userLogin": "thammisetti-vanaja-priya79347",
  "userTriggered": true,
  "newValue": {
    "permission": "codeviewer",
    "groupName": "Members",
    "componentKey": "prod-project",
    "permissionTemplateName": "Default template",
    "qualifier": "project"
  }
}

```
{% endcode %}

<br>
