# Automate Branch Creation, Metadata Commit, and Pull Requests Using ARM APIs

### Overview

AutoRABIT ARM provides API support to automate branch creation, Salesforce metadata retrieval, committing metadata changes, and creating Pull Requests.

Users can initiate the workflow through a POST API request and monitor the execution status of individual operations using a GET API request.

This functionality supports both new and existing branches.

### Step 1: Generate an API Token

1. Log in to AutoRABIT ARM.
2. Navigate to **Settings → API Token Manager**.
3. Click **Create API Token**.
4. Enter the token details.
5. Select **API** as the token type.
6. Generate and securely copy the token.

<figure><img src="../../../../.gitbook/assets/image (164).png" alt=""><figcaption></figcaption></figure>

Use this token to authenticate the POST and GET requests.

### Step 2: Configure the POST API

The POST API initiates the workflow to create or select a branch, retrieve Salesforce metadata, commit changes, and create a Pull Request.

**Method:** `POST`

**Endpoint:**

```
POST https://<ARM_BASE_URL>/api/vc/v1/branch-pr
```

Replace `<ARM_BASE_URL>` with your ARM instance hostname.

For example, the screenshots show the following SIT environment endpoint:

```
POST https://arm-sit.autorabit.com/api/vc/v1/branch-pr
```

#### Request Headers

| Header         | Value                   |
| -------------- | ----------------------- |
| `token`        | Generated ARM API token |
| `Accept`       | `application/json`      |
| `Content-Type` | `application/json`      |

#### Sample Request Body

Navigate to **Body → raw → JSON** in Postman.

```
{
  "packageManifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Package xmlns=\"http://soap.sforce.com/2006/04/metadata\"><types><members>AccountController</members><members>AccountControllerTest</members><name>ApexClass</name></types><types><members>AccountTrigger</members><name>ApexTrigger</name></types><types><members>Account.Customer_Tier__c</members><name>CustomField</name></types><types><members>accountSummary</members><name>LightningComponentBundle</name></types><version>62.0</version></Package>",
  "orgName": "100GB-SANDBOX",
  "repoName": "Thiru GitHub OAuth",
  "baseBranch": "main",
  "branchName": "feature/test-branch-pr",
  "jiraKey": "",
  "commitMessage": "Test1",
  "prTitle": "Test PR1",
  "prDescription": "Test PR",
  "useExistingBranch": false
}
```

#### Request Parameters

| Parameter           | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `packageManifest`   | Salesforce metadata components to retrieve, defined using Package XML |
| `orgName`           | Salesforce Org name registered in ARM                                 |
| `repoName`          | Repository name registered in ARM                                     |
| `baseBranch`        | Base branch used to create the new branch and target the Pull Request |
| `branchName`        | New or existing branch name                                           |
| `jiraKey`           | Optional Jira issue key                                               |
| `commitMessage`     | Commit message for the retrieved metadata                             |
| `prTitle`           | Pull Request title                                                    |
| `prDescription`     | Pull Request description                                              |
| `useExistingBranch` | Determines whether to create a new branch or use an existing one      |

#### Using a New or Existing Branch

**Create a new branch**

```
"useExistingBranch": false
```

When set to `false`, ARM creates a new branch from the specified base branch. If no branch name is supplied, ARM can generate one automatically, as demonstrated in the minimal-request example.

**Use an existing branch**

```
"useExistingBranch": true
```

When set to `true`, ARM uses the specified existing branch rather than creating a new one.

The remaining workflow retrieves the metadata, commits the changes, and creates a Pull Request.

### Step 3: Execute the POST Request

Once the request headers and body are configured, click **Send**.

#### Successful Response

**HTTP Status: `202 Accepted`**

```
{
  "requestId": "<REQUEST_ID>",
  "status": "QUEUED"
}
```

The API returns a unique Request ID.

The `QUEUED` status indicates that the request has been accepted and is awaiting processing.

**Important:** A `202 Accepted` response does not mean that the Pull Request has already been created.

Use the returned Request ID to monitor execution through the GET API.

### Step 4: Configure the GET API to Track Execution Status

The GET API retrieves the execution status of the workflow initiated by the POST request.

**Method:** `GET`

**Endpoint:**

```
GET https://<ARM_BASE_URL>/api/vc/v1/branch-pr/<REQUEST_ID>
```

For the SIT environment:

```
GET https://arm-sit.autorabit.com/api/vc/v1/branch-pr/<REQUEST_ID>
```

Replace `<REQUEST_ID>` with the Request ID returned by the POST request.

#### Request Headers

| Header   | Value                   |
| -------- | ----------------------- |
| `token`  | Generated ARM API token |
| `Accept` | `application/json`      |

Click **Send** to retrieve the execution status.

#### Sample Successful GET Response

**HTTP Status: `200 OK`**

```
{
  "requestId": "<REQUEST_ID>",
  "status": "COMPLETED",
  "currentStep": null,
  "steps": [
    {
      "name": "CREATE_BRANCH",
      "status": "SUCCESS",
      "message": "Branch created from 'main'."
    },
    {
      "name": "RETRIEVE_METADATA",
      "status": "SUCCESS",
      "message": "Metadata retrieved from Salesforce Org."
    },
    {
      "name": "COMMIT",
      "status": "SUCCESS",
      "message": "Changes committed successfully."
    },
    {
      "name": "UPDATE_JIRA",
      "status": "SKIPPED",
      "message": "No jiraKey supplied."
    },
    {
      "name": "CREATE_PULL_REQUEST",
      "status": "SUCCESS",
      "message": "Pull request created: <PULL_REQUEST_URL>"
    }
  ]
}
```

_This is a simplified example based on the completed response shown in the screenshots. Identifiers and repository-specific details have been replaced with placeholders._

#### Understanding the Response

| Field         | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `requestId`   | Unique identifier for the submitted request                          |
| `status`      | Overall workflow status                                              |
| `currentStep` | Currently executing operation, or `null` when no operation is active |
| `steps`       | Individual operations and their execution results                    |
| `name`        | Name of the operation                                                |
| `message`     | Additional details about the operation                               |

#### Workflow Operations

| Operation             | Description                                        |
| --------------------- | -------------------------------------------------- |
| `CREATE_BRANCH`       | Creates a new branch or selects an existing branch |
| `RETRIEVE_METADATA`   | Retrieves metadata from the Salesforce Org         |
| `COMMIT`              | Commits retrieved metadata to the selected branch  |
| `UPDATE_JIRA`         | Updates Jira when applicable                       |
| `CREATE_PULL_REQUEST` | Creates a Pull Request against the target branch   |

If the request is still processing, execute the GET API again to retrieve the latest status.

### Step 5: Verify the Pull Request

Once the workflow status is `COMPLETED` and the Pull Request creation step is successful, users can access the created Pull Request.

#### Option 1: API Response

The GET response includes the Pull Request URL in the `CREATE_PULL_REQUEST` step message.

#### Option 2: AutoRABIT ARM

1. Log in to ARM.
2. Navigate to **Version Control → External Pull Requests**.
3. Select the corresponding repository.
4. Locate the newly created Pull Request.
5. Open the Pull Request to review the committed changes.

#### Option 3: Git Repository

Open the configured Git repository and navigate to the Pull Requests section to review the newly created Pull Request.

### API Error Handling

The API returns validation errors when request details are invalid or the requested operation cannot be performed.

#### Example 1: Repository Not Found

**HTTP Status: `400 Bad Request`**

```
{
  "error": "Repository 'my-repo' was not found."
}
```

Verify that `repoName` matches the repository registered in ARM.

#### Example 2: Branch Already Exists

**HTTP Status: `400 Bad Request`**

```
{
  "error": "Branch '<BRANCH_NAME>' already exists in repository '<REPOSITORY_NAME>'."
}
```

This error can occur when the API attempts to create a branch that already exists.

To resolve the issue, specify a different branch name or set `useExistingBranch` to `true` when you intend to reuse an existing branch.

### Important Notes

* The API token must be generated using the **API** token type.
* The Salesforce Org and repository must be registered in ARM.
* The Package Manifest must contain valid Salesforce metadata.
* The POST API initiates the workflow asynchronously.
* The GET API can be used to monitor each operation.
* The Jira update step can be skipped when no Jira key is provided.
* A completed workflow can be verified through the GET response, ARM, or the Git repository.
* Never expose actual API tokens or sensitive request information in publicly shared documentation.

### Conclusion

The ARM Branch and Pull Request APIs simplify Salesforce development workflows by automating branch creation, metadata retrieval, commits, and Pull Request creation.

With support for new and existing branches, users can integrate these APIs into their development processes while monitoring individual operations through the GET status API.
