---
hidden: true
---

# ECA User Guide

## Introduction

Salesforce has introduced the **External Client App (ECA)** framework as the new standard for managing OAuth-based integrations. This framework replaces the legacy **Connected App** model for newly created integrations and provides a more secure and structured way to configure external applications that access Salesforce resources.

To align with Salesforce’s updated authentication framework, Vault now supports integration using **External Client Apps**. This approach ensures compatibility with Salesforce’s latest OAuth standards while maintaining secure access between Vault and Salesforce environments.

This guide explains how to register a Salesforce organization in Vault using the **External Client App (ECA)** configuration and authorize Vault to access Salesforce through OAuth.

## Overview

Registering a Salesforce organization in Vault involves configuring an OAuth connection using a **Salesforce External Client App**. This process establishes a secure authorization flow that allows Vault to interact with Salesforce APIs.

The setup process includes the following stages:

1. **Registering the Salesforce organization in Vault** by providing environment details.
2. **Creating an External Client App in Salesforce** to enable OAuth authentication.
3. **Configuring required OAuth scopes and callback settings** within Salesforce.
4. **Providing the Client ID and Client Secret in Vault**.
5. **Authorizing Vault to access Salesforce** through the OAuth authorization process.
6. **Validating the connection** and completing the org registration.

Once the setup is complete, the Salesforce organization becomes available in Vault and can be used for operations such as **Backup, Compare, Search & Compare, Restore, Replication, and Data Masking**.

## Step-By-Step Guide: Registering a Source Salesforce Org in Vault

### Navigate to the Salesforce Orgs Setup Page

On the **Vault Setup** page, the **Salesforce Orgs List** displays all registered Salesforce environments.

To register a new Salesforce organization:

1. Click **REGISTER NEW ORG**.

![](<../../../../.gitbook/assets/Unknown image (28) (1)>)

This action opens the **Source Org Integration** setup wizard.

### Configure Environment Details

The **Source Org Integration** wizard begins with **Environment Details**.This step captures the basic configuration required to connect the Salesforce environment.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (25) (1) (1)>)

Configure the following fields:

* **Environment Type** – Select the appropriate environment:
  * **Salesforce** – Standard Salesforce organization.
  * **nCino** – nCino environment running on Salesforce.
* **Salesforce API Version** – Select the API version used for integration.
* **Org Title** – Enter a recognizable name for the organization.This name helps identify the org within Vault.
* **User Name** – Enter the Salesforce username used for authentication.

### Select Salesforce Environment Type

After entering the username, select the type of Salesforce environment.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (26) (1) (1)>)

Available options include:

* **Production** – Used for live Salesforce environments.
* **Sandbox** – Used for development or testing environments.

Once the environment type is selected, provide the **Salesforce Login URL**.

This field supports both:

* Default Salesforce login URLs
* Custom **My Domain** login URLs

If Salesforce enforces **My Domain**, the login URL must match the configured domain.

Click **Continue** to proceed.

### Create the Salesforce External Client App

The next step guides the creation of a **Salesforce External Client App** required for OAuth authentication.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (27) (1) (1)>)

Vault displays the configuration steps that must be completed in Salesforce.

Complete the following actions in Salesforce:

1. Navigate to **Setup → App Manager**.
2. Click **New External Client App**.
3. Enable **OAuth Plugin**.
4. Select **Authorization Code (Web Server) Flow**.
5. Disable the **PKCE security option**.
6. Add the **Callback URL** provided in Vault.

After completing the configuration in Salesforce, return to Vault.

Important Note: After creating the ECA in Salesforce, there may be a replication delay on the Salesforce side. If you encounter the error error=invalid\_client\_id\&error\_description=client%20identifier%20invalid while attempting to connect or register the org, please wait 30 minutes, and try again to allow the Salesforce configuration to sync completely.

Click **I've completed the setup** to continue.

### Configure OAuth Scopes

Add the required OAuth scopes in the Salesforce External Client App.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (28) (1) (1)>)

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (29) (1)>)

The following scopes must be enabled:

* **Access the identity URL service (id, profile, email, address, phone)**
* **Manage user data via APIs (api)**
* **Manage user data via Web browsers (web)**
* **Full access (full)**
* **Perform requests at any time (refresh\_token, offline\_access)**

Ensure the **Callback URL (Redirect URI)** matches exactly with the value provided in Vault.

Any mismatch will result in connection failure.

### Enter OAuth Credentials

After completing the Salesforce External Client App configuration, provide the OAuth credentials in Vault.

Important Note: After creating the ECA in Salesforce, there may be a replication delay on the Salesforce side. If you encounter the error error=invalid\_client\_id\&error\_description=client%20identifier%20invalid while attempting to connect or register the org, please wait 30 minutes, and try again to allow the Salesforce configuration to sync completely.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (30) (1)>)

Enter the following details:

* **Client ID** – The Consumer Key generated from the Salesforce External Client App.
* **Client Secret** – The Consumer Secret generated from the Salesforce External Client App.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (31) (1)>)

These values are available in Salesforce under the External Client App configuration.

#### Where to Find the Credentials in Salesforce

1. Navigate to **Setup → App Manager**.
2. Locate the created **External Client App**.
3. Open the dropdown menu and select **View**.
4. Click **Manage Consumer Details**.
5. Copy the **Consumer Key (Client ID)** and **Consumer Secret (Client Secret)**.

Paste these values into the corresponding fields in Vault.

Click **Continue** to proceed to the authorization step.

### Authorize Vault to Access Salesforce

The **Connect to Salesforce** step initiates the OAuth authorization process.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (32) (1)>)

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (33) (1)>)

Vault displays the connection details for verification:

* **Org Title** – The name assigned during configuration.
* **Type** – The selected Salesforce environment (Production or Sandbox).
* **Login URL** – The Salesforce login endpoint used for authentication.

This step establishes a secure connection between Vault and the Salesforce organization.

Click **Connect to Salesforce** to begin the authorization process.

### Complete Salesforce Authorization

After clicking **Connect to Salesforce**, the following process occurs:

1. The browser redirects to the Salesforce login page.

![A screenshot of a web page AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (10) (1) (1) (1)>)

1. Authentication occurs using the provided Salesforce credentials.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (11) (1) (1) (1)>)

1. Salesforce displays the permissions requested by Vault.

![A screenshot of a computer error message AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (12) (1) (1) (1)>) ![A screenshot of a computer screen AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (13) (1) (1)>)

1. Select **Allow** to grant the required access.
2. After authorization, Salesforce redirects back to Vault automatically.

Vault then completes the validation and confirms the connection.

### Validation and Setup Completion

After the authorization process is completed, Vault validates the Salesforce connection and displays a **Connection Successful** confirmation.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (14) (1) (1)>)

The **Validation & Confirmation** step displays the environment details of the connected Salesforce org, including:

* **Org Title** – The name assigned during org registration.
* **Salesforce Org ID** – The unique identifier of the Salesforce environment.
* **Instance URL** – The Salesforce instance endpoint used for API communication.
* **Login URL** – The login endpoint used for authentication.

This confirmation indicates that the Salesforce organization has been successfully connected to Vault.

### Test the API Connection

To verify that Vault can communicate with the Salesforce environment, perform an API connectivity test.

1. In the **Test Your Connection** section, click **Test API Connection**.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (15) (1) (1)>)

### Verify the API Connection Status

If the connection test succeeds, Vault displays a confirmation message indicating that the API communication is working correctly.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (16) (1) (1)>)

A notification message appears confirming that the **API connection test was successful**.

This validation ensures that Vault can securely interact with the Salesforce environment using the configured OAuth credentials.

### Complete the Org Registration

After the connection test is successful:

1. Click **Finish**.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (17) (1) (1)>)

Vault completes the org registration process and closes the **Source Org Integration** wizard.

The newly connected Salesforce organization now appears in the **Salesforce Orgs List** within the **Setup** section and is available for Vault operations such as **Backup, Compare, Search & Compare, Restore, Replication, and Masking**.

### Confirm Successful Org Registration

After clicking **Finish**, Vault displays a confirmation message indicating that the Salesforce organization has been successfully registered.

![](<../../../../.gitbook/assets/Unknown image (18) (1) (1)>)

This confirmation verifies that the integration process has completed successfully and the Salesforce environment is now available for Vault operations.

Click **OK** to close the confirmation message.

### Verify the Registered Salesforce Org

After the confirmation message is closed, the **Salesforce Orgs List** page displays the newly registered organization.

![](<../../../../.gitbook/assets/Unknown image (19) (1) (1)>)

The list provides key details for each connected environment, including:

* **Org Title**
* **Org ID**
* **Environment Type**
* **Username**
* **Last Updated Time**
* **Authentication Type**
* **Instance URL**

The newly added organization now appears in this list and is ready to be used within Vault.

### Re-authenticate an Existing Org (If Required)

If authentication credentials expire or require renewal, the Salesforce organization can be re-authenticated directly from the **Salesforce Orgs List**.

![](<../../../../.gitbook/assets/Unknown image (19) (1) (1)>)

To re-authenticate an organization:

1. Locate the required org in the **Salesforce Orgs List**.
2. Navigate to the **Actions** column.
3. Click the **Re-authenticate** icon.

Vault redirects to the Salesforce login page to complete the authentication process.

### Authenticate Through Salesforce Login

When the **Re-authenticate** action is initiated, the Salesforce login screen appears.

![](<../../../../.gitbook/assets/Unknown image (20) (1) (1)>)

Enter the following credentials:

* **Username**
* **Password**

Click **Log In** to authenticate the connection.

After successful authentication, Vault restores the secure connection with the Salesforce environment.

### Access Additional Org Actions

After the Salesforce org is successfully registered, additional management options are available for the connected org.

1. Navigate to **Setup**.
2. Locate the required org in the **Salesforce Orgs List**.
3. In the **Actions** column, click the **More actions (⋮)** icon.

![A list of numbers and numbers AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (21) (1) (1)>)

A menu appears displaying additional management options for the selected Salesforce org.

### View Org Configurations

The **More actions** menu provides multiple options for managing the registered Salesforce org.

![A list of numbers and numbers AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (22) (1) (1)>)

To view the configurations associated with the org:

1. Click **View Configs**.

Vault opens the configuration view for the selected Salesforce org, allowing management of backup and archive configurations.

### View Backup Configurations

The **Configs** page displays the configurations created for the selected Salesforce org.

This page includes the following sections:

* **Configs Tab** – Displays configuration settings associated with the org.
* **Backup** – Lists backup configurations created for the org.
* **Archive** – Displays archive configurations, if configured.

The **Backup** section provides details such as:

* **Backup Config Name**
* **Config Type**
* **Frequency**
* **Schedule Time**
* **Backup Config Details**
* **Actions**
* **Last Backup Status**

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (23) (1) (1)>)

From this page, new configurations can be created using:

* **Add Backup Config** – Create a new backup configuration.
* **Add Archive Config** – Create a new archive configuration.

The **Back to Orgs List** option allows navigation back to the **Salesforce Orgs List** page.

### Open the Salesforce Org Edit Option

Vault allows updating the configuration details of a registered Salesforce org.

1. Navigate to **Setup**.
2. Locate the required org in the **Salesforce Orgs List**.
3. In the **Actions** column, click the **More actions (⋮)** icon.
4. Select **Edit Salesforce Org**.

![A list of data on a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (66)>)

Vault opens the **Environment Details** window for the selected Salesforce environment.

### Update Salesforce Org Configuration

The **Environment Details** window allows modification of the registered Salesforce org configuration.

![](<../../../../.gitbook/assets/Unknown image (67)>) ![](<../../../../.gitbook/assets/Unknown image (68)>)

1. Update the required fields as needed:

* **Environment Type** – Select **Salesforce** or **nCino**.
* **Salesforce API Version** – Choose the API version used for integration.
* **Org Title** – Modify the display name for the org.
* **Org Type** – Select **Production** or **Sandbox**.
* **Salesforce Login URL** – Verify or update the login endpoint if a **My Domain** or custom login URL is used.

2. After reviewing the changes, click **Save** to apply the updated configuration.

Vault updates the Salesforce org details while maintaining the existing connection settings.

### Open Client Key Configuration

1. In the **Salesforce Orgs List**, locate the required org.
2. Click the **More Actions (⋮)** menu under the **Actions** column.
3. Select **Edit Client Keys**.

![](<../../../../.gitbook/assets/Unknown image (69)>)The **Edit Credentials** configuration wizard opens, allowing the External Client App credentials to be configured.

### Configure Salesforce External Client App

The first stage of the wizard provides guidance for creating an **External Client App** in Salesforce.

1. In the **Salesforce Admin Setup** section, follow the instructions to create an External Client App in Salesforce:

* Navigate to **Setup → App Manager**.
* Create a **New External Client App**.
* Enable the **OAuth Plugin**.
* Select **Authorization Code (Web Server) Flow**.
* Disable the **PKCE security option** if required.

![](<../../../../.gitbook/assets/Unknown image (70)>)

1. Copy the **Callback URL (Redirect URI)** displayed in Vault and add it to the External Client App configuration in Salesforce.

![](<../../../../.gitbook/assets/Unknown image (71)>)

1. Configure the following **OAuth scopes** in Salesforce:

* Access the identity URL service
* Manage user data via APIs
* Manage user data via Web browsers
* Full access
* Perform requests at any time (refresh\_token, offline\_access)

![](<../../../../.gitbook/assets/Unknown image (72)>)

1. Ensure that the **Redirect URI in Salesforce exactly matches the Callback URL displayed in Vault** to prevent connection failures.
2. After completing the Salesforce configuration, click **Next** to proceed.

### Step 31–32: Enter Client Credentials

1. In the **Edit Credentials** step, enter the following values from the Salesforce External Client App:

* **Client ID** – The Consumer Key generated in Salesforce.

![](<../../../../.gitbook/assets/Unknown image (73)>)

*
  * **Client Secret** – The Consumer Secret generated in Salesforce.

![](<../../../../.gitbook/assets/Unknown image (74)>)

1. These values can be retrieved in Salesforce by navigating to:**Setup → App Manager → External Client App → Manage Consumer Details**.
2. After entering the credentials, proceed to save and re-authenticate the connection.

Vault uses these credentials to securely establish OAuth authentication with the Salesforce org.

### Open Connect Configuration

1. In the **Salesforce Orgs List**, locate the required Salesforce org.
2. Click the **More Actions (⋮)** menu under the **Actions** column.
3. Select **Connect (Beta)**.

![](<../../../../.gitbook/assets/Unknown image (75)>)

The **Connect (Beta)** configuration page opens for the selected org.

### Access the Connect (Beta) Page

1. After selecting **Connect (Beta)**, the **Connect (Beta)** tab opens within the org configuration screen.

![A screenshot of a computer AI-generated content may be incorrect.](<../../../../.gitbook/assets/Unknown image (76)>)

1. This page displays all configured **Connect jobs** for the selected org.
2. The following options are available on this page:

* **Sync with Salesforce** – Synchronizes connect configurations with Salesforce.
* **Add Connect Config** – Creates a new Connect configuration.
* **Refresh** – Reloads the connect configuration list.

3. If no configurations exist, the page displays the message **“No Connects.”**
4. To create a new configuration, click **Add Connect Config**.
