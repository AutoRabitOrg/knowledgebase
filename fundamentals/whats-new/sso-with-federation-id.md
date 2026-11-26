# SSO with Federation ID

### **Overview**

ARM supports **Federation ID-based authentication** for SAML Single Sign-On (SSO), allowing administrators to identify users through a unique identifier, such as an employee ID, without relying on their ARM username or email address.

When Federation ID is selected, ARM matches the **Subject (NameID)** received in the SAML assertion against the Federation ID configured in the ARM user record.

**Availability:** New UI only.

### **Prerequisites**

* Administrator access to ARM.
* Administrator access to the identity provider (IdP), such as Microsoft Entra ID.
* A unique identifier for each user.
* Identity provider metadata XML file.

### **Configuring SSO with Federation ID**

#### **Step 1: Configure the Identity Provider**

The following steps use Microsoft Entra ID as an example.

1. Navigate to **Microsoft Entra ID → Enterprise Applications**.
2. Create or select the ARM application.
3. Navigate to **Single sign-on** and select **SAML**.
4. Under **Basic SAML Configuration**, configure the following details:

| Field                  | Value                     |
| ---------------------- | ------------------------- |
| Identifier (Entity ID) | `<ARM URL>/saml/metadata` |
| Reply URL (ACS URL)    | `<ARM URL>/saml/SSO`      |

5. Under **Attributes & Claims**, edit the **Unique User Identifier (Name ID)**.
6. Configure the following fields:

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| Name identifier format | Persistent                                        |
| Source                 | Attribute                                         |
| Source attribute       | Attribute containing the user's unique identifier |

7. Save the configuration.
8. Download the **Federation Metadata XML** file under **SAML Certificates**.
9. Assign the required users or groups to the application.

#### **Step 2: Configure Federation ID for ARM Users**

1. Log in to ARM as an administrator.
2. Navigate to **Settings → Users**.
3. Create a new user or edit an existing user.
4. Enter the unique identifier in the **Federation ID** field.
5. Click **Save**.

Ensure that the Federation ID exactly matches the value sent by the identity provider in the SAML Subject.

#### **Step 3: Configure SSO in ARM**

1. Navigate to **Settings → My Account → SSO Configuration**.
2. Enter the SSO **Domain**.
3. Upload the identity provider metadata XML file under **IDP metadata file**.
4. From the **Identify users by** dropdown, select one of the following options:

| Option             | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| Username           | Identifies users using their ARM username.                            |
| Federation ID      | Identifies users using their configured Federation ID.                |
| Microsoft Entra ID | Identifies users using their Microsoft Entra Tenant ID and Object ID. |

5. Select **Federation ID**.
6. Click **Save**.

#### **Step 4: Log in using SSO**

1. Navigate to the ARM login page.
2. Click **Login with SSO**.
3. Enter the configured SSO domain.
4. Click **Continue with SSO**.
5. Complete authentication with the identity provider.

ARM validates the Federation ID received in the SAML assertion and signs in the corresponding user.

### **Important Considerations**

* Federation ID must be unique within the ARM organization.
* Federation ID matching is case-sensitive.
* Federation ID supports a maximum of 512 characters.
* Only administrators can configure or modify Federation IDs.
* Assign Federation IDs to all SSO users before enabling Federation ID-based authentication.
* Existing SSO configurations continue to work without requiring any changes.
* Username and password authentication remains available for super administrators when **Enforce SSO** is disabled.

### **Troubleshooting**

| Issue                                   | Resolution                                                                                           |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Federation ID already exists            | Enter a unique Federation ID for the user.                                                           |
| SSO sign-in fails                       | Verify that the Federation ID matches the SAML Subject (NameID) received from the identity provider. |
| SSO domain is not configured            | Verify the configured domain and uploaded IdP metadata file.                                         |
| User is not assigned to the application | Assign the user to the application in the identity provider.                                         |
| Reply URL mismatch                      | Verify the Reply URL configured in the identity provider.                                            |
