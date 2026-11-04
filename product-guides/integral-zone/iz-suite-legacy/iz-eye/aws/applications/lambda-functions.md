---
description: AWS Lambda
---

# Lambda Functions

{% hint style="info" %}
o start scanning the functions, a schedule with the **`AWS Lambda Analysis`** job type has to be created - [Schedule Configuration](../schedule-configuration.md)
{% endhint %}

#### What Is Scanned <a href="#what-is-scanned" id="what-is-scanned"></a>

A Lambda scan has two passes, and both report into the same application:

| Pass              | What is read                                                                                                                                                                                                                                                                                                              | Rules                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Configuration** | The function's configuration and tags (`lambda-function-definition.json`), its resource-based policy (`lambda-policy.json`), function URLs (`lambda-url-configs.json`), event source mappings (`lambda-event-source-mappings.json`) and its execution role with its inline and attached policies (`lambda-iam-role.json`) | AWS Lambda rule pack                              |
| **Code**          | The files of the deployment package, for functions on a Python runtime                                                                                                                                                                                                                                                    | Python rules of the active Python quality profile |

* Functions packaged as a **container image** have no downloadable package and are configuration-scanned only.
* Functions on other runtimes (for example Node.js or Java) are configuration-scanned only. Java code is scanned from the source repository with IZ Scan, not from the deployed function.
* If the deployment package cannot be downloaded, the configuration findings are still published and the job log says why the code pass was skipped.
* If the access key cannot read IAM, the scan runs without `lambda-iam-role.json` and the IAM rules are not evaluated.
* Many Lambda rules include an auto-fix suggestion.

#### To view all the functions <a href="#to-view-all-the-functions" id="to-view-all-the-functions"></a>

1. Navigate to **`IZ Eye`** -> **`AWS`** -> **`AWS Lambda`**. Overview includes -
   1. **`Name`** - Name of the Lambda function
   2. **`Organization`** - The AWS account to which the function belongs
   3. **`Environment`** - The region to which the function belongs
2. Click on the **`Plus`** icon to view the details
3. Summary details include -
   1. **`Total Issues`** - Configuration and code issues found by the latest scan
   2. **`Status`** - State of the function reported by AWS, for example **`Active`**
   3. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues. Configuration issues are reported against the `lambda-*.json` documents, code issues against the Python source files. See [Application Issues](../../application-issues.md).
   3. **`View Metrics`** - Includes the function's runtime and its relationships: the queues, topics, event buses, state machines, secrets, tables, databases and APIs it is connected to.

<br>
