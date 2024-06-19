# Page 1

## Introduction <a href="#introduction" id="introduction"></a>

#### CEF logs is a standardized log management system developed to record and transport event data.  <a href="#cef-logs-is-a-standardized-log-management-system-developed-to-record-and-transport-the-event-data" id="cef-logs-is-a-standardized-log-management-system-developed-to-record-and-transport-the-event-data"></a>

## How To Access CEF Logs <a href="#how-to-access-cef-logs" id="how-to-access-cef-logs"></a>

* An option is provided to download logs from the UI.

<figure><img src="../../../../.gitbook/assets/image (568).png" alt=""><figcaption></figcaption></figure>

***

### APIs <a href="#apis" id="apis"></a>

The following are the APIs available for the CEF logs.

**To View or Download Event Logs as a Single File:**

To view or download event logs as a single file, use the API below. Ensure you minimize the date range if a large amount of data is present within the given date range. You can use the date parameters to manipulate the response as per the requirement and increment the data accordingly to fetch the next set of records.

> `GET: {{url}}/ARVault/eventlogs?from=2023-10-09&to=2023-10-10`

`Headers:` \
`Authorization: Bearer <AccessToken>` \
`Cookies: ARVault=<ARVault>` \


`The values for <AccessToken> and <ARVault> can be retrieved from the login API response:` \
\
`<AccessToken> is found in the response body of the login API. <ARVault> is found in the response headers of the login API.`

* The `from` and `to` parameters are optional.
* If the `to` parameter is not provided, it downloads the logs up to the current date. If the `from` parameter is not provided, it will download the logs from today up to the current time.
* If the `from` value is greater than the `to` value, the API will consider the `from` value as the `to` value and vice versa.
* If you request a file with the same `from` and `to` parameters, it will download the log file for that day.
* The API will prepare a single file for the user for the given date range without loading the files into Java memory.
* It will save the consolidated file in the file system.
* If the user is an admin, it will consolidate all user logs for that organization within the date range.

***

**To download the zip:**

Two APIs are involved: one to prepare the zip file and the other to download the zip file. Details are given below:

1. `GET: {{url}}/ARVault/eventlogs/prepare-zip?from=2023-10-09&to=2023-10-10`
2. `Headers:`&#x20;
3. `Authorization: Bearer <AccessToken>`&#x20;
4. `Cookies: ARVault=<ARVault>`&#x20;
5.
6. `The values for <AccessToken> and <ARVault> can be retrieved from the login API response:`&#x20;
7.
8.  `<AccessToken> is found in the response body of the login API.` \
    `<ARVault> is found in the response headers of the login API.`

    \
    **Output:** A temporary token for the file, which is valid for a minute.

    * The API works in the same manner as described above, with the same `from` and `to` parameter validation and process.
    * It will prepare a consolidated zip file for the user.
    * Files will be named by the user's email for that day, with special characters in the email replaced by '\_'.
    * It returns a temporary token cached for the file for a minute.
9. `GET: {{url}}/ARVault/eventlogs/download/code/{token}`
   * The token is mandatory and should be sent as input to the API.
   * If the token is invalid/expired, the API will respond with a forbidden message.
   * If the token is valid, it will download the zip file, and the token cannot be used again.

***

**To download the consolidated file:**

Two APIs are involved: one to prepare the consolidated file and the other to download the zip file. Details are given below:

1. GET: [\{{url\}}/ARVault/eventlogs/](http://localhost:8080/ARVault/eventlogs?from=2023-10-09\&to2023-10-10)download/code/{token}
   * The token is mandatory and should be sent as input to the API.
   * If the token is invalid/expired, the API will respond with a forbidden message.
   * If the token is valid, it will download the consolidated log file.
2. `<AccessToken> is found in the response body of the login API.` \
   `<ARVault> is found in the response headers of the login API.`
   * **Output:** A temporary token for the file, which is valid for a minute.
   * The API works in the same manner as described above, with the same validation and process.
   * It will prepare a consolidated file for the user. All validations are the same as the above API.
   * It returns a temporary token cached for the file for a minute.
3.
4. `The values for <AccessToken> and <ARVault> can be retrieved from the login API response:`&#x20;
5.
6. `Cookies: ARVault=<ARVault>`&#x20;
7. `Authorization: Bearer <AccessToken>`&#x20;
8. `Headers:`&#x20;
9. `GET: {{url}}/ARVault/eventlogs/prepare-log?from=2023-10-09&to=2023-10-10`

&#x20;

### CEF Log Structure <a href="#cef-log-structure" id="cef-log-structure"></a>

**The following is the structure of the log.**

Date(ISO Format) CEF:Version|Device Vendor|Device Product|Device Version|Thread Id|Name|Severity|Extension

**Example:**\
2024-06-17T06:37:44.145Z CEF:0|AutoRabit|Vault|23.2|http-nio-8081-exec-1|ArchivalReport|Low|sessionId=\<sessionid> [username=example@example.com](mailto:username=asha@wish.com) customerId=\<customer id> action=\<user loggedin> ip=0:0:0:0:0:0:0:1 userAgent=Chrome

The following table describes the fields of the CEF log structure.

<table><thead><tr><th width="97">SL.No</th><th width="208">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>1</strong></td><td><strong>Date(ISO Format) CEF</strong></td><td>This field describes the date on which the log is created</td></tr><tr><td><strong>2</strong></td><td><strong>Version</strong></td><td>This defines the version of the CEF log</td></tr><tr><td><strong>3</strong></td><td><strong>Device Vendor</strong></td><td>This field denotes the vendor who is providing the</td></tr><tr><td><strong>4</strong></td><td><strong>Device Product</strong></td><td>This denotes which product of the CEF logs</td></tr><tr><td><strong>5</strong></td><td><strong>Device Version</strong></td><td>This denotes the product version</td></tr><tr><td><strong>6</strong></td><td><strong>Thread Id</strong></td><td>This is the ID from the server for a request</td></tr><tr><td><strong>7</strong></td><td><strong>Name</strong></td><td>This denotes the module of the product is being accessed</td></tr><tr><td><strong>8</strong></td><td><strong>Severity</strong></td><td>This denotes the severity of the event logged</td></tr><tr><td><strong>9</strong></td><td><strong>Extension</strong></td><td>This provides additional information on the event logged</td></tr></tbody></table>

&#x20;
