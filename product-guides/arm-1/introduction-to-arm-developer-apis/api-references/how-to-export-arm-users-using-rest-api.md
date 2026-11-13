# How to Export ARM Users Using REST API

### Overview

AutoRABIT ARM provides a REST API that allows administrators to retrieve user information based on their account status. This API helps administrators automate user reporting, license management, and auditing without manually exporting user information from the ARM interface.

The API supports retrieving **All, Active, or Inactive users** and allows the results to be downloaded in Excel format.

### Prerequisites

Before using the API, ensure that:

* You have access to AutoRABIT ARM.
* You have the required permissions to retrieve user information.
* You have generated a valid **API Token** in ARM.
* You have an API testing tool such as Postman or cURL.

### Step 1: Generate an API Token in ARM

1. Log in to your AutoRABIT ARM account.
2. Navigate to the API Token management section.
3. Create a new token with the **API** token type.
4. Copy the generated token and store it securely.

**Note:** The API token is required to authenticate requests. Do not share your token with unauthorized users.

### Step 2: Configure the API Request

Open Postman or your preferred API client and configure the request using the following details.

**HTTP Method:** `GET`

**API Endpoint:**

```http
GET https://<your-arm-domain>/api/usermanagement-api/export-users?status=all
```

Replace `<your-arm-domain>` with your ARM instance domain.

#### Request Headers

Navigate to the **Headers** tab in Postman and provide the following values:

| Key    | Value              |
| ------ | ------------------ |
| token  | Your ARM API Token |
| Accept | application/json   |

**Note:** This API uses the GET method, so no request body is required.

### Step 3: Select the User Status

The API supports three status options to retrieve users.

| Status     | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| `all`      | Retrieves all ARM users, regardless of their account status. |
| `active`   | Retrieves only Active ARM users.                             |
| `inactive` | Retrieves only Inactive ARM users.                           |

#### Option 1: Retrieve All Users

To retrieve all users, use:

```http
GET https://<your-arm-domain>/api/usermanagement-api/export-users?status=all
```

This retrieves both Active and Inactive users.

#### Option 2: Retrieve Active Users

To retrieve only Active users, use:

```http
GET https://<your-arm-domain>/api/usermanagement-api/export-users?status=active
```

This retrieves users whose accounts are currently Active in ARM.

#### Option 3: Retrieve Inactive Users

To retrieve only Inactive users, use:

```http
GET https://<your-arm-domain>/api/usermanagement-api/export-users?status=inactive
```

This retrieves users whose accounts are currently Inactive in ARM.

### Step 4: Execute the API Request

1. Open Postman.
2. Select **GET** as the request method.
3. Enter the API endpoint with the required `status` parameter.
4. Navigate to the **Headers** tab.
5. Enter your ARM API Token in the `token` header.
6. Set the `Accept` header to `application/json`.
7. Click **Send**.

ARM processes the request and returns the user information based on the selected status.

### Step 5: Download the User Information in Excel Format

The API also supports exporting the retrieved user information in Excel format.

1. Execute the API request with the required user status.
2. Once the request completes successfully, use the download or save-response option available in your API client.
3. Save the exported user information in Excel format.
4. Open the downloaded file to review the user details.

The exported information can be used for user inventory reporting, license reconciliation, and auditing.

**Note:** The exact download procedure depends on the response format returned by your ARM instance and the API client being used.

### Step 6: Sample cURL Request

You can execute the same API using cURL.

**Retrieve All Users**

```bash
curl --location 'https://<your-arm-domain>/api/usermanagement-api/export-users?status=all' \
--header 'token: <YOUR_ARM_API_TOKEN>' \
--header 'Accept: application/json'
```

**Retrieve Active Users**

```bash
curl --location 'https://<your-arm-domain>/api/usermanagement-api/export-users?status=active' \
--header 'token: <YOUR_ARM_API_TOKEN>' \
--header 'Accept: application/json'
```

**Retrieve Inactive Users**

```bash
curl --location 'https://<your-arm-domain>/api/usermanagement-api/export-users?status=inactive' \
--header 'token: <YOUR_ARM_API_TOKEN>' \
--header 'Accept: application/json'
```

Replace `<YOUR_ARM_API_TOKEN>` with the API Token generated in ARM.

### Troubleshooting

| Issue                       | Recommended Action                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------------------- |
| Unauthorized request        | Verify that the API Token is valid and has the required permissions.                               |
| Invalid status parameter    | Ensure the status value is `all`, `active`, or `inactive`.                                         |
| No users returned           | Verify that users exist for the selected status.                                                   |
| API request fails           | Verify the ARM instance URL, network connectivity, and request headers.                            |
| Unable to download the file | Verify the API response format and use the appropriate save or download option in your API client. |

### Summary

The **Export ARM Users API** enables administrators to retrieve user information programmatically without manually exporting records from the ARM interface.

By using the `status` parameter, administrators can retrieve All, Active, or Inactive users and use the exported information for reporting, auditing, license management, and other administrative activities.
