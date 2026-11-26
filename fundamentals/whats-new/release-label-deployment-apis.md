# Release Label Deployment APIs

### **Overview**

ARM introduces Deployment APIs to initiate and monitor Salesforce deployments using existing Release Labels through external tools and CI/CD pipelines.

These APIs enable users to automate Salesforce org promotion without manually initiating deployments from the ARM UI.

### **Supported APIs**

| Method | Endpoint                 | Description                                                          |
| ------ | ------------------------ | -------------------------------------------------------------------- |
| POST   | `/deployments/v1/deploy` | Initiate a deployment or validation using an existing Release Label. |
| GET    | `/deployments/v1/name`   | Retrieve deployment status and execution details.                    |

### **Prerequisites**

* A valid ARM API token and appropriate permissions.
* An existing Release Label in ARM.
* A registered destination Salesforce org.
* ARM instance base URL.

### **1. Initiate Deployment**

The POST API allows users to deploy or validate an existing Release Label against a registered Salesforce org.

**Endpoint:**

```
POST {{baseUrl}}/deployments/v1/deploy
```

#### **Request Parameters**

| Parameter            | Type    | Required | Description                                             |
| -------------------- | ------- | -------- | ------------------------------------------------------- |
| `releaseLabelName`   | String  | Yes      | Name of the existing Release Label.                     |
| `destinationOrgName` | String  | Yes      | Name of the registered destination Salesforce org.      |
| `deploymentLabel`    | String  | Yes      | Deployment name used for tracking.                      |
| `validateOnly`       | Boolean | No       | Set to `true` for validation only. Defaults to `false`. |

#### **Sample Request – Deployment**

The following request initiates an actual deployment using an existing Release Label.

```
{
  "releaseLabelName": "Release_26.4.9",
  "destinationOrgName": "Production",
  "deploymentLabel": "Production_Deployment_01"
}
```

#### **Sample Request – Validation Only**

Set `validateOnly` to `true` to validate the Release Label without deploying changes to the destination org.

```
{
  "releaseLabelName": "Release_26.4.9",
  "destinationOrgName": "Production",
  "deploymentLabel": "Production_Validation_01",
  "validateOnly": true
}
```

#### **Additional Deployment Options**

The API also supports the following optional deployment configurations:

| Parameter                         | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| `testLevel`                       | Specifies the Salesforce test execution level.      |
| `skipWarnings`                    | Skips deployment warnings.                          |
| `takeBackup`                      | Takes a backup before deployment.                   |
| `ignoreMissingVisibilitySettings` | Ignores missing visibility settings.                |
| `removeLoginIpRanges`             | Removes login IP ranges.                            |
| `removeSystemAndUserPermissions`  | Removes system and user permissions.                |
| `skipMembers`                     | Skips members according to ARM deployment settings. |
| `skipDestructiveChanges`          | Skips destructive changes.                          |
| `ignoreInstalledComponents`       | Ignores installed components.                       |
| `note`                            | Adds deployment notes.                              |

When optional parameters are omitted, ARM applies its existing deployment defaults.

#### **Sample Request – All Deployment Options**

```
{
  "releaseLabelName": "Release_26.4.9",
  "destinationOrgName": "Production",
  "deploymentLabel": "Production_Validation_02",
  "validateOnly": true,
  "testLevel": "RunLocalTests",
  "skipWarnings": true,
  "takeBackup": true,
  "ignoreMissingVisibilitySettings": true,
  "removeLoginIpRanges": true,
  "removeSystemAndUserPermissions": true,
  "skipMembers": true,
  "skipDestructiveChanges": true,
  "ignoreInstalledComponents": true,
  "note": "Production release validation"
}
```

### **2. Retrieve Deployment Status**

The GET API allows users to monitor the progress of a deployment initiated through the POST API.

**Endpoint:**

```
GET {{baseUrl}}/deployments/v1/name
```

Using the deployment name, users can retrieve:

* Current deployment status.
* Deployment execution results.
* Failure details, when available.

External tools and CI/CD pipelines can periodically invoke this API to monitor deployment progress until completion.

### **3. View Deployment History**

Deployments initiated through the API are recorded in ARM Deployment History.

1. Log in to ARM.
2. Navigate to **Deployments → Deployment History**.
3. Locate the deployment using the specified deployment label.
4. Review the execution status, logs, and deployment results._y._

### **Important Considerations**

* The Release Label must already exist(artifact generated) in ARM.
* The destination Salesforce org must be registered in ARM.
* Both APIs require valid ARM API authentication and authorization.
* Setting `validateOnly` to `true` performs validation without deploying changes.
* Existing Release Label artifacts are reused without recreating them.
* API-triggered deployments follow the same deployment processing logic as the ARM UI.

### **Benefits**

* Automated Salesforce org promotion.
* Seamless integration with external CI/CD pipelines.
* Reduced manual intervention.
* Reusability of existing Release Labels.
* Centralized deployment tracking through ARM Deployment History.
