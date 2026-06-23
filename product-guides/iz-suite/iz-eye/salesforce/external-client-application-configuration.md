# External Client Application Configuration

## Configure External Client App

An External Client App in Salesforce is required to securely connect to Salesforce REST APIs because it establishes a trusted integration identity for IZ Suite within the Salesforce ecosystem. When IZ Suite scans Apex classes, triggers, and metadata through Salesforce APIs, it must authenticate using OAuth 2.0 rather than relying on individual user credentials.

Creating an External Client App defines the appropriate OAuth scopes, and allows administrators to control which users or system contexts can authorize the app. This ensures secure, token-based, and auditable access to Salesforce REST and Tooling APIs, enabling IZ Suite to perform automated code scanning and metadata analysis in a controlled, enterprise-compliant manner.

### Configuring the Client App in Salesforce

Follow the below steps to create a Bot User in Salesforce -

1. Navigate to **`Setup`** -> **`Users`** -> and click on **`New User`**
2. Enter the basic details
   1. **`First Name`** -
   2. **`Last Name`** -
   3. **`Email`** -
   4. **`Role`** - Nothing to be specified
   5. **`User License`** - Select Salesforce
   6. **`Profile`** - Select System Administrator
3. Save the User accepting the other default values

Follow the below steps to create Permission Set in Salesforce -

1. Navigate to **`Setup`** -> **`Users`** -> **`Permission Sets`** and click on **`New`**
2. Enter a name for the permission set and click on Save
3. Once the Permission Set is created in the **`Permission Set Overview`** -> **`System Permissions`**, click on Edit and choose the following permissions -
   1. **`API Enabled`**
   2. **`Author Apex`**
4. Click on Save
5. Once the Permission Set is saved, click on **`Manage Assignments`** -> **`Add Assignments`**
6. Select the new bot user created in the above step and assign the user.

Follow the below steps to create an External Client App in Salesforce -

1. Navigate to **`Setup`** -> **`Apps`** -> **`External Client Apps`** -> **`External Client App Manager`** and click on **`New External Client App`**
2. Enter the basic details and select **`Local`** distribution type
3. Under **`OAuth Settings`** enable OAuth
   1. **`Callback Url`** - https://login.salesforce.com
   2. Add **`Manage Users Data via APIs`** and **`Perform Requests at any time (refresh token, offline access)`** scopes
   3. Under **`Flow Enablement`** select **`JWT Bearer Workflow`**
   4. Generate the certificates using the below commands openssl genrsa -out server.key 2048 openssl req -new -x509 -key server.key -out server.crt -days 365
   5. Upload the public key (Eg: server.crt). Make sure the **`server.key`** is kept safe as we will need it while configuring the auth in IZ Suite.
4. Click on Create
5. Once the app is created, edit the app and update the following
   1. **`Permitted Users`** -> **`Admin Approved users are pre-authorized`**
   2. Under Select Profiles choose **`System Administrator`**
   3. Under Select Permission Sets choose the new Permission Set created in the above step
6. Save the settings

### Retrieve the External App’s Client ID

1. Navigate to **`Setup`** -> **`Apps`** -> **`External Client Apps`** -> **`External Client App Manager`** and click on the created client app
2. Click on **`Settings`** -> **`OAuth Settings`** -> **`Consumer Key and Secret`**&#x20;
3. The displayed **`Consumer Key`** is the Client Id, which will be used while configuring the Client app in IZ Suite

### Configuring the Client App details in IZ Suite

1. Navigate to main menu **`Organization`** -> **`My Organizations`** and click on **`Onboard Organization`**
2. Enter the following details -
   1. **`Organization Name`** - The name of the Organization. For example - **`IZ APAC`**
   2. **`Source`** - Choose **`Salesforce`** as source
3. Click on save.&#x20;
4. Once the Organization is created, click on the **`View Environments`** action item
5. Click on **`Create Environment`** to create a new environment
6. Enter the following details -
   1. **`Environment Name`** - The name of the Environment. For example - **`Sandbox`** or **`Production`**
   2. **`Is Production`** - Should be checked if the environment type is production
   3. **`Instance URL`** - Salesforce instance URL
   4. **`Client Id`** - Client Id retrieved from the Salesforce External Client App
   5. **`User Name`** - Name of the user assigned to the External Client App
   6. **`Private Key`** - Contents of the private key generated from the previous step. (Eg: Contents of server.key)&#x20;
7. Follow the same steps to add additional environments or organization

### Configuring Role for accessing IZ Eye

Once the environment is configured, create / edit a role add required permissions

1. Navigate to main menu **`Organization`** -> **`Roles`** and click on **`Create Role`**
2. Enter the following details
   1. Role Name - Name for the role Eg; IZ APAC IZ Eye Admin
   2. Permissions - Expand **`IZ Eye Salesforce`** and select the required permissions&#x20;
   3. Select the required organizations and environments to associate with the role&#x20;
3. Click on Submit

Once the role is configured, assign the same to users based on the requirement

1. Navigate to main menu **`Organization`** -> **`Users`** and click on **`Assign Roles to User`** action item
2. Click on the **`Unassigned`** tab and select the required roles
3. Click on save

### See Also

* Configure Code Scan Schedule
* Apex Classes & Triggers
