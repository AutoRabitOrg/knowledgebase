# Retrieval APIs

### API Specification <a href="#api-specification" id="api-specification"></a>

* **Request Endpoint**: `https://<domain>auditlogs.autorabit.com/logs/audit_logs`\
  &#xNAN;_&#x46;or example: https://testauditlogs.autorabit.com/logs/audit\_logs_
* **Request Type**: `GET`
* **Request Query String Parameters**:
  * **startTime**=**YYYY-MM-DDThh:mm:ss** (this is optional; if not specified, the current day will be presumed)\
    &#xNAN;_&#x46;or example: 2021-03-14T1000:00_
  * **maxResults**=**1000** (optional, default value is 1000)
  * **eventType**=**event1, event2** (this is optional, however, if not specified it will load all the events)\
    &#xNAN;_&#x46;or example: eventType=DEPLOYMENT, DATALOADERPRO will load events for DEPLOYMENT and DATALOADERPRO respectively._
* **Request Headers**:
  * **Content-Type**: application/json
  * **Authorization**: Your Bearer token

### Obtaining Your Access Token <a href="#obtaining-your-access-token" id="obtaining-your-access-token"></a>

To interact with API, you need to have a unique, personal access token. This will be used to authenticate yourself within the API. Please contact the AutoRABIT Team to update the following properties in the **config** file once the API token gets generated:

`/home/ubuntu/.rabit/auditlogs/auditConfig.json`

To generate your access token, you should:

1. Log in to the AutoRABIT account.
2. Hover your mouse over the **Admin** module and select the option: **API Tokens**
3. Click on the **Create API Token** button to generate a new token.
4. Enter the **API Token Name** on the next screen.
5. Click **Create**. Note down your newly generated token - you are going to need it soon.

{% hint style="info" %}
**Point to Note:**

For security reasons, it is not possible to view the token after closing the creation dialog. If necessary, create a new token. Max of **10 tokens** are permitted for each user license. You should store the token securely, as for any password.
{% endhint %}

### Sample Request <a href="#sample-request" id="sample-request"></a>

```
curl --location --request GET 'https://previewauditlogs.autorabit.com/logs/audit_logs?startTime=2021-3-14T00:10:00&maxResults=1000&eventType ' \

--header 'Content-Type: application/json' \

--header 'Authorization: Bearer token' \

--data-raw ''

```

### Sample Response <a href="#sample-response" id="sample-response"></a>

```
[
    "2021-03-14 07:34:36 CEF:1.0|AutoRABIT|AutoRABIT|20.2|LOGIN|admin|Low|arLName=saikumar.preview@autorabit.com arLType=UWP arBrowserType=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 msg=Success reason=Login Success start=Mar 14 2021 07:34:36 UTC",
    
    "2021-03-14 07:39:33 CEF:1.0|AutoRABIT|AutoRABIT|20.2|DATALOADERPRO|dataloaderpro|Low|deviceProcessName=ce0f03bf-c17f-431e-9771-90bae5ba5c66 arActor=saikumar.k@autorabit.com arStatus=NA arSSFOrgName=NA arDSFOrgName=NA arObject= NA arSOQLQuery=NA arSFAPIVersion=NA arExternalId=NA arIUTF8=NA arBulkAPI= NA arInsertNulls=NA arVRImpact=NA arWRImpact=NA arDMLType=NA arRSucessCount=NA arRFailureCount=NA arObject=NA arCategory=null arBatchSize=null arSrcUserSuffix=null arDestUserSuffix=null arScheduleTime=null arScheduleTimeInterval=null arScheduleDays=null arScheduleType=null arPrcoessId=ce0f03bf-c17f-431e-9771-90bae5ba5c66 arParents=null arChilds=null arIgnoreCommunityUsers=null arIsAccountIncluded=nullarIsMaskingEnabled=null arScheduleFromDate=null arScheduleToDate=null arScheduleRuns=null arAutoFilter=null arMinMulRef=null arIsIncremental=null arStartDate=null arMaskingField=null arMaskingName=null arMaskingType=null arMaskingStyle=null arVRName=null arWFName=null arVRId=null arWFId=null arObjectType=null msg=Dataloader pro job:ce0f03bf-c17f-431e-9771-90bae5ba5c66 schedule has been deleted successfully. start=NA end=NA suser=NA duser=NA",
]

```

### Sample Response (for invalid API Token) <a href="#sample-response-for-invalid-api-token" id="sample-response-for-invalid-api-token"></a>

```
{
    "timestamp": "2021-03-16T17:22:14.786+00:00",
    
    "status": 401,
    
    "error": "Unauthorized",
    
    "message": "",
    
    "path": "/logs/audit_logs"
}
```

## Audit Logs Retrieval API Guide

This guide provides information on how to use the Audit Logs Retrieval API to view and download audit logs. The API offers endpoints for retrieving audit log data and downloading it in a ZIP file format. Follow the instructions below to integrate and use these APIs in your application.

### Viewing Audit Logs

#### Endpoint

`GET <https://<domain>>/logs/audit_logs`

**Example:**

`<https://testauditlogs.autorabit.com/logs/audit_logs>`

#### Query String Parameters

1. `startTime` (optional): The start time for the audit logs in ISO 8601 format (YYYY-MM-DDThh:mm:ss). If not specified, the current day's logs are presumed.
   * **Example:** `2021-03-14T10:00:00`
2. `maxResults` (optional): The maximum number of results to return. Default value is 1000.
   * **Example:** `maxResults=1000`
3. `eventType` (optional): A comma-separated list of event types to filter the logs. If not specified, all event types are loaded.
   * **Example:** `eventType=DEPLOYMENT,DATALOADERPRO`

#### Example Request

`GET <https://testauditlogs.autorabit.com/logs/audit_logs?startTime=2021-03-14T10:00:00&maxResults=500&eventType=DEPLOYMENT,DATALOADERPRO>`

#### Response

The response will contain the audit logs based on the specified parameters.

### Downloading Audit Logs

#### Endpoint

`GET {domain}/logs/audit_logs/download`

#### Parameters

* `startTime` (required): The start date for the audit logs in ISO 8601 format.
* `endTime` (optional): The end date for the audit logs in ISO 8601 format. If not specified, the logs are provided until the current day, provided the duration is within 90 days from the `startTime`.

#### Example Request Using Curl

`curl --location '<https://<domain>>/logs/audit_logs/download?startTime=2021-03-14T10:00:00&endTime=2021-03-20T10:00:00' \ --header 'Content-Type: application/json' \ --header 'Authorization: Bearer <bearer token>'`

#### Notes:

* If only the `startTime` is provided, logs are retrieved up to the current day.
* The date range (from `startTime` to `endTime` or the current day) must be within 90 days.
* The downloaded logs are provided in a ZIP file.

#### Example Download Request

`GET <https://<domain>>/logs/audit_logs/download?startTime=2021-03-14T10:00:00&endTime=2021-03-20T10:00:00`

The logs between March 14, 2021, and March 20, 2021, will be downloaded in a ZIP file.

### Authorization

All requests to the API endpoints must include an `Authorization` header with a valid Bearer token.

**Example:**

`--header 'Authorization: Bearer <bearer token>'`

Ensure your Bearer token is kept secure and is valid for accessing the API.
