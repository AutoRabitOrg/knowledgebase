# General Questions and Answers

#### 1. What is Vault™? <a href="#1-what-is-vault-tm" id="1-what-is-vault-tm"></a>

Vault™ is our cloud-based Salesforce backup tool for reliable and secure backups of your organization’s essential data. Vault supplies off-platform backup, restoration, and recovery of Salesforce data and metadata. With our data backup for Salesforce, you can protect your Salesforce data while remaining compliant.

#### 2. Why do I need a Salesforce backup solution? <a href="#2-why-do-i-need-a-salesforce-backup-solution" id="2-why-do-i-need-a-salesforce-backup-solution"></a>

Your organization may experience several scenarios resulting in a Salesforce data loss. A backup of your data and metadata sets is essential to the recovery process. Some reasons your company would need a Salesforce backup can include:

* **Analyzing data off the platform:** Backups deliver a copy of your Salesforce data outside the platform. Your organization can use this copy to run a thorough analysis using tools not included in the Salesforce dashboard.
* **Reducing the risk of bulk data imports and updates:** Salesforce includes tools such as Data Loader to import and update thousands of records instantly. If completed incorrectly, this action can accidentally remove or alter these records, which would be cumbersome to correct manually. Your organization could use the Salesforce backup to repopulate the platform with the correct data.
* **Undoing an error:** Your employees may accidentally edit or delete values in Salesforce or change workflows and APEX script deployments. Your system may not recognize these errors immediately, but AutoRABIT Vault can undo this critical error and migrate the correct data back to Salesforce.

#### 3. What are the benefits of Salesforce data backup service? <a href="#3-what-are-the-benefits-of-salesforce-data-backup-service" id="3-what-are-the-benefits-of-salesforce-data-backup-service"></a>

With the thousands of changes made in the Salesforce database daily, regular and reliable backups are critical for the Salesforce environment. The advantages of Salesforce backup and restore include:

* **Restore lost data:** Rogue automation, user error, and mass data editing can accidentally delete or overwrite critical data. With Vault, you can restore your backup files to save your data and metadata. You can also send this data back to your Salesforce orgs.
* **Enhance data protection:** The automated backup schedule improves data security by regularly saving data off-platform. Your company will have reliable backup data sets to rely on if the original source is compromised.
* **Save version data:** With Salesforce data backup and restore from Vault, your organization won’t need to keep track of data changes or find them in exported files. You can save only the newest changes instead of the entire file, which protects the bulk of your data sets.
* **Detect and prevent data errors:** Vault capabilities, such as Compare, identify problems in the data and metadata structures, so you can verify that the most recent data is saved and protected.
* **Comply with industry regulations:** Our Salesforce data recovery manager allows your company to meet policy requirements for IT governance without sacrificing your data restoration needs. You can meet compliance regulations while backing up and recovering data at your ideal frequency.
* **Eliminate manual backup:** Manual efforts to back up Salesforce data and metadata can be lengthy. Automatic backup from Vault eliminates the need to manage the backup process by completing it automatically.

#### 4. Data vs. Metadata <a href="#4-data-vs-metadata" id="4-data-vs-metadata"></a>

* **Data** relates to the records that a business relies on, e.g. users, Accounts, Contacts, etc.
* **Metadata** is the data that describes data, the way that records behave and the “look and feel” of your Salesforce org.

#### 5. Does Vault support Multi-Factor Authentication (MFA)? <a href="#5-does-vault-supports-multi-factor-authentication-mfa" id="5-does-vault-supports-multi-factor-authentication-mfa"></a>

Vault supports Multi-Factor Authentication (MFA).

Multi-factor authentication (MFA) is a powerful, secure authentication method with two steps (or factors) to prove users’ identities when they log in. The first factor is information known to users, like usernames and passwords. The second is a verification method the user has in their possession, like an authenticator app or a security key. So multi-factor authorization makes it a lot harder for fraudsters to get access to your Vault data.

#### 6. How do I enable Multi-Factor Authentication (MFA) for my account? <a href="#6-how-to-enabe-multi-factor-authentication-mfa-for-my-account" id="6-how-to-enabe-multi-factor-authentication-mfa-for-my-account"></a>

As an administrator of your account, you can enable multi-factor authentication (MFA) for every account member (global level) or at the user level.

* Enabling MFA in your account at a global level affects all members of the account. This means that the users must enroll for MFA at their next login.
* Enabling MFA does not affect users already logged in, as the enforcement of MFA on the account takes effect only at new logins.
* Enabling MFA will mandate users to register their mobile devices for generating and validating tokens using authenticator apps like Google Authenticator or Salesforce Authenticator app.\
  [Learn more-->](https://knowledgebase.autorabit.com/vault/docs/set-up-multifactor-authentication-for-vault)

#### 7. How do I create a new user in my account? <a href="#7-how-to-create-a-new-user-in-my-account" id="7-how-to-create-a-new-user-in-my-account"></a>

You can create a new user with just a few clicks. It’s as simple as entering the first, middle, and last names and an email address, then selecting a role, Salesforce orgs (if required), and designation. After you invite users, they receive a confirmation email with a link to create their login password.

You will find the **`Add User`** option under **Manage Users > Users** tab.

You need **Administrator privileges** to add user accounts.

#### 8. Where can I find my Vault subscription details? <a href="#8-where-can-i-find-my-vault-subscription-details" id="8-where-can-i-find-my-vault-subscription-details"></a>

At the time of registering an account with Vault, our team will share a license key to your registered email address. You will need to add the license key under the **Settings > Licenses** tab to fetch the following details:

* **Number of Users:** Total number of users who can log into the Vault account.
* **Number of Orgs:** Total number of Salesforce orgs that can register with Vault.
* **Number of Threads for Orgs:** Total number of parallel queries that can be performed on the Salesforce environment.
* **Number of Configs for Org:** Total number of backup or archive configurations that you can have inside Vault.

#### 9. Admin vs Super Admin users <a href="#9-admin-vs-super-admin-users" id="9-admin-vs-super-admin-users"></a>

* **Admin:** The first user to log into the Vault application is the **admin** user _(also called administrator, org administrator, or, main user)_. The admin is the most authoritative user with many privileges, such as adding users, changing user passwords, deleting users, and configuring the Vault environment.
* **Super Admin:** Super admin users are on our end; they grant the client admin's request for initial access to the Vault application, then create and share the license key with the client.

#### 10. What is the Salesforce Bulk API version supported by Vault? <a href="#10-what-is-the-salesforce-bulk-api-version-supported-by-vault" id="10-what-is-the-salesforce-bulk-api-version-supported-by-vault"></a>

Bulk API version **1.0** is currently supported by Vault.
