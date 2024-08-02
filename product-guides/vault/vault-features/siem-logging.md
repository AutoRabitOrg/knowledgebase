# SIEM Logs

## SIEM Logging – Event Logs <a href="#introduction" id="introduction"></a>

### Introduction <a href="#introduction" id="introduction"></a>

Security Information and Event Management (SIEM) system logs allow you to record and transport event data.&#x20;

### How to Access SIEM Logs <a href="#how-to-access-cef-logs" id="how-to-access-cef-logs"></a>

Users have the option to download logs from the UI. Access logs using the steps below.

* Click on "Profiles" to access the "Session Information."

<figure><img src="../../../.gitbook/assets/image (644).png" alt=""><figcaption></figcaption></figure>

* Click on the “Session Information” tab to access the “Activity” button.

<figure><img src="../../../.gitbook/assets/image (645).png" alt=""><figcaption></figcaption></figure>

* Click on the “Activity Log” to access user activity.
* On “Activity Logs”, click on the “Download” dropdown to access the available options.

<figure><img src="../../../.gitbook/assets/image (646).png" alt=""><figcaption></figcaption></figure>

* Click any of the options available to download the logs.

***

### APIs <a href="#apis" id="apis"></a>

The following APIs are available for SIEM logs.

**View or Download Event Logs as a Single File:**

Use the API below to view or download event logs as a single file. Ensure you minimize the date range if a large amount of data is present within the given date range. You can use the date parameters to manipulate the response per the requirement and increment the data accordingly to fetch the next set of records.

> `GET: {{url}}/ARVault/eventlogs?from=2023-10-09&to=2023-10-10`

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

* The `from` and `to` parameters are optional.
* If the `to` parameter is not provided, it downloads the logs up to the current date. If the `from` parameter is not provided, it will download the logs from today up to the current time.
* If the `from` value is greater than the `to` value, the API will consider the `from` value as the `to` value and vice versa.
* If you request a file with the same `from` and `to` parameters, it will download the log file for that day.
* The API will prepare a single user file for the given date range without loading the files into Java memory.
* It will save the consolidated file in the file system.
* If the user is an admin, it will consolidate all user logs for that organization within the date range.

***

**To download the zip:**

Two APIs are involved: one to prepare the zip file and the other to download the zip file. Details are given below:

1. `GET: {{url}}/ARVault/eventlogs/prepare-zip?from=2023-10-09&to=2023-10-10`

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**Output:** A temporary token for the file, which is valid for a minute.

* The API works in the same manner as described above, with the same from and to parameter validation and process.&#x20;
* It will prepare a consolidated zip file for the user.&#x20;
* File names are the user's email for that day, with special characters in the email replaced by '\_'.&#x20;
* It returns a temporary token cached for the file for a minute.

2. `GET: {{url}}/ARVault/eventlogs/download/code/{token}`

* The token is mandatory and should be sent as input to the API.
* If the token is invalid/expired, the API will respond with a forbidden message.
* If the token is valid, it will download the zip file, and the token cannot be used again.

***

**To download the consolidated file:**

Two APIs are involved: one to prepare the consolidated file and the other to download the zip file. Details are given below:

> 1. `GET: {{url}}/ARVault/eventlogs/prepare-log?from=2023-10-09&to=2023-10-10`

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

**Output:** A temporary token for the file, which is valid for a minute.

* The API works in the same manner as described above, with the same validation and process.
* It will prepare a consolidated file for the user. All validations are the same as the above API.
* It returns a temporary token cached for the file for a minute.

2. GET: \{{url\}}/ARVault/eventlogs/download/code/{token}

* The token is mandatory and should be sent as input to the API.
* If the token is invalid/expired, the API will respond with a forbidden message.
* If the token is valid, it will download the consolidated log file.



### SIEM Log Structure <a href="#cef-log-structure" id="cef-log-structure"></a>

**The following is the structure of the log.**

Date (ISO Format) SIEM:Version|Device Vendor|Device Product|Device Version|Thread Id|Name|Severity|Extension

**Example:**\
2024-06-17T06:37:44.145Z CEF:0|AutoRabit|Vault|23.2|http-nio-8081-exec-1|ArchivalReport|Low|sessionId=\<sessionid> username=example@example.com customerId=\<customer id> action=\<user loggedin> ip=0:0:0:0:0:0:0:1 userAgent=Chrome

The following table describes the fields of the SIEM log structure.

<table><thead><tr><th width="97">SL.No</th><th width="120">Field</th><th width="110">Data Type</th><th width="86" data-type="number">Length</th><th>Description</th></tr></thead><tbody><tr><td><strong>1</strong></td><td><strong>Date (ISO Format) SIEM</strong></td><td>Date Time</td><td>24</td><td>This field describes the date on which the log is created.</td></tr><tr><td><strong>2</strong></td><td><strong>CEF Version</strong></td><td>Number</td><td>2</td><td>This defines the version of the SIEM log.</td></tr><tr><td><strong>3</strong></td><td><strong>Device Vendor</strong></td><td>Text</td><td>9</td><td>This field denotes the vendor providing the device.</td></tr><tr><td><strong>4</strong></td><td><strong>Device Product</strong></td><td>Text</td><td>5</td><td>This denotes which product of the SIEM logs.</td></tr><tr><td><strong>5</strong></td><td><strong>Device Version</strong></td><td>Number</td><td>10</td><td>This denotes the product version.</td></tr><tr><td><strong>6</strong></td><td><strong>Thread Id</strong></td><td>Text</td><td>32</td><td>This is the ID from the server for a request.</td></tr><tr><td><strong>7</strong></td><td><strong>Name</strong></td><td>Text</td><td>256</td><td>This denotes the module of the product being accessed.</td></tr><tr><td><strong>8</strong></td><td><strong>Severity</strong></td><td>Text</td><td>10</td><td>This denotes the severity of the event logged.</td></tr><tr><td><strong>9</strong></td><td><strong>Extension</strong></td><td>Text</td><td>5120</td><td>This provides additional information on the event logged.</td></tr></tbody></table>

### &#x20;Custom Keys

The custom keys or extensions will have the following tracked in the event logs.

<table><thead><tr><th width="134">Key Name</th><th width="102">Key Type</th><th width="97">Module</th><th width="111">Data Type</th><th width="90">Length</th><th>Description</th></tr></thead><tbody><tr><td>SessionId</td><td>Custom</td><td>All</td><td>Text</td><td>32</td><td>Identifies the user login</td></tr><tr><td>User Name</td><td>Custom</td><td>All</td><td>Text</td><td>255</td><td>Identifies the Loggedin User</td></tr><tr><td>Action</td><td>Custom</td><td>All</td><td>Text</td><td>2048</td><td>Identifies the API call</td></tr><tr><td>IP</td><td>Custom</td><td>All</td><td>IP</td><td>39</td><td>Identifies the device address</td></tr><tr><td>User Agent</td><td>Custom</td><td>All</td><td>Text</td><td>32</td><td>Identifier the browser used by the customer</td></tr><tr><td>CustomerId</td><td>Custom</td><td>All</td><td>Text</td><td>255</td><td>Identifies the customer</td></tr><tr><td>Message</td><td>Custom</td><td>All</td><td>Text</td><td>2048</td><td>Audit Log message</td></tr></tbody></table>

### **Vault Event Type** <a href="#vault-event-type" id="vault-event-type"></a>

<table><thead><tr><th width="86">SI No</th><th width="231">Event Type</th><th width="153">Module</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>AnamolyDetails</td><td>Setup > Alerts</td><td>Event type to track the configured triggers activity in Vault</td></tr><tr><td>2</td><td>Archival</td><td>Archive</td><td>Event type to track the activity on the Archival module</td></tr><tr><td>3</td><td>ArchivalReport</td><td>Archive Reports</td><td>Event type to track the user activity on the Archive Reports module</td></tr><tr><td>4</td><td>ArchivalReportDownload</td><td>Archive Reports</td><td>Event type to track the user download on the reports module</td></tr><tr><td>5</td><td>ArchivalReportItem</td><td>Archive Reports</td><td>Event type to track the user activity on the Archival Report Items</td></tr><tr><td>6</td><td>ArchivalReportItemQuery</td><td>Archive Reports</td><td>Event type to track the user activity on the Archival Report Item Queries</td></tr><tr><td>7</td><td>ArchivalReportQuery</td><td>Archive Reports</td><td>Event type to track the user activity on the Archival Report Queries</td></tr><tr><td>8</td><td>AwsEnviReg</td><td>Settings</td><td>Event type for tracking the AWS storage registration</td></tr><tr><td>9</td><td>BakupSchedulesManage</td><td>Config</td><td>Event type for tracking all the user actions on the schedules</td></tr><tr><td>10</td><td>BlackList</td><td>GDPR</td><td>Event type to track the user activity on GDPR module</td></tr><tr><td>11</td><td>Customer</td><td>User Management</td><td>Event type to track the activity every time the user details are fetched</td></tr><tr><td>12</td><td>DataMasking</td><td>Replicate</td><td>Event type to track activity every time the data masking is performed</td></tr><tr><td>13</td><td>EventLog</td><td>CEF Logs</td><td>Event type to track the user activity when the CEF logs are downloaded by the user either from API or UI</td></tr><tr><td>14</td><td>FileDownload</td><td>File Downloads</td><td>Event type to track the UI file downloads</td></tr><tr><td>15</td><td>MultiFactorAuth</td><td>User Management</td><td>Event type to track the login and access of the user(s)</td></tr><tr><td>16</td><td>Proxy</td><td>Vault Settings</td><td>Event type to track the activity on the proxy settings page</td></tr><tr><td>17</td><td>Restore</td><td>Replicate Restore</td><td>Event type to track the user activity on the Replicate &#x26; Restore modules</td></tr><tr><td>18</td><td>Role</td><td>User Management</td><td>Event type to track the user activity every time the user role details are fetched</td></tr><tr><td>19</td><td>SalesforceFeatures</td><td>Setup > Config</td><td>Event type to track the nCino Features accessed by the Vault application</td></tr><tr><td>20</td><td>SforgBakupCfg</td><td>Setup > BackupConfig</td><td>Event type to track the activities performed on the backup config</td></tr><tr><td>21</td><td>SforgBakupStatus</td><td>Backup Restore Replicate</td><td>Event type to track the user activity on the Backup Restore Replicate module</td></tr><tr><td>22</td><td>SfOrgConnectConfig</td><td>Setup > Config</td><td>Event type to track the Vault connect configuration</td></tr><tr><td>23</td><td>SfOrgConnectSync</td><td>Setup > Config</td><td>Event type to track the user activity on the Vault Connect ‘Sync With Salesforce’</td></tr><tr><td>24</td><td>SforgEnviReg</td><td>Settings</td><td>Event type to track the storage registration in Vault</td></tr><tr><td>25</td><td>SforgUniqueFiledsConfig</td><td>Unique Identifiers</td><td>Event type to track the user activity on the Unique Identifiers tabs</td></tr><tr><td>26</td><td>SFReader</td><td>All Modules</td><td>Event type to track the activity every time the SFORG details are read</td></tr><tr><td>27</td><td>StartBackup</td><td>Backup &#x26; Archive</td><td>Event type to track the activity every time the “Backup &#x26; Archive” are triggered</td></tr><tr><td>28</td><td>User</td><td>User Management</td><td>Event type to track the activity on the user management</td></tr><tr><td>29</td><td>Zoho</td><td>Zoho Integration</td><td>Event type to track the user activity when the user accesses “Zoho”</td></tr></tbody></table>

### &#x20;Messages <a href="#messages" id="messages"></a>

Following are the audit log messages

* **Storage**
  * Storage configuration request has been submitted."
  * "Storage configuration update request has been submitted.”
* **User Management**
  * "User addition request has been submitted."
  * "User activation request has been submitted."
  * "Create password request has been submitted."
  * "Reset password request has been submitted."
  * "Change password request has been submitted."
  * "Delete user request has been submitted."
  * "Deactivate user request has been submitted."
  * "Create user request has been submitted."
  * "Update user request has been submitted."
  * "User profile update request has been submitted."
  * "User logged in with details: "
  * "User logged out with details: "
  * "Session terminated by: "
  * "User got blocked with details: "
  * "MFA verification code validated successfully for user."
  * "MFA is enabled for user."
  * "MFA is disabled for user."
  * "MFA is reset for user."
  * "MFA device is successfully registered by user.”
* **Setup**
  * "Backup schedule disable request has been submitted."
  * "Backup schedule enable request has been submitted.”
* **Customer Management**
  * "Customer activation request has been submitted."
  * "Customer deactivation request has been submitted."
  * "Customer deletion request has been submitted.”
  * "Enable/disable org access control request has been submitted."
* **Salesforce Operations**
  * "Salesforce org creation request has been submitted."
  * "Salesforce org update request has been submitted."
* **Vault Connect**
  * "Sforg Odata Connector Config creation/update request has been submitted."

**Backup**&#x20;

* "Backup configuration creation request has been submitted."
* "Backup configuration update request has been submitted."
* "Backup configuration delete request has been submitted."
* "Backup download operation has been initiated."
* "Backup has been downloaded."
* "Object has been downloaded from backup."
* "Backup has been initiated."
* "Stop backup process has been initiated."

**Restore**

* "Restore operation has been initiated.”
* "Restore deletion request has been submitted."
* **Hierarchial**
  * "Hierarchical backup process has been initiated."
  * "Hierarchical backup configuration creation request has been submitted."
  * "Hierarchical backup configuration update request has been submitted."
  * "Hierarchical backup configuration delete request has been submitted.”
  * "Stop hierarchical process has been initiated.”
  * "Hierarchical backup download operation has been initiated."
* **Archive**&#x20;
  * "Archive process has been initiated."
  * "Archive backup configuration creation request has been submitted."
  * "Archive backup configuration update request has been submitted."
  * "Archive backup delete request has been submitted."
  * "Stop archive process has been initiated."
  * "Archive download operation has been initiated."&#x20;
* **Replication**
  * "Replicate operation has been initiated."
  * "Replicate configuration creation request has been submitted."
  * "Replicate configuration update request has been submitted."
  * "Replicate deletion request has been submitted."
* **Alert rules**
  * "Create alert rule request has been submitted."
  * "Delete alert rule request has been submitted."
  * "Anomaly detection process has been initiated."
  * "Object has been downloaded for anomaly detection."
  * "All records have been downloaded for anomaly detection."
* **GDPR**
  * "Create GDPR request has been submitted."
  * "Delete GDPR request has been submitted."
  * "Object has been downloaded from GDPR."
  * "Upload search file for GDPR request has been initiated."

&#x20;
