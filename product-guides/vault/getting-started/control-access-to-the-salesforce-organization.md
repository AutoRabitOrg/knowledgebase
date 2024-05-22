# Control Access to the Salesforce Organization

The org administrator can restrict their users to access only those Salesforce orgs which has been authorized to them. Users will be able to perform Vault operations in their Salesforce org based on their org access, such as backup, restore, replicate, comparison, and archival.

The **Enable org. access control** toggle in the **Manage Users** page is switched on by default. This indicates that the admin has the org access control permission and can specify which users have access to which Salesforce org(s) in the Vault account. If the toggle is turned off, all users in the Vault account will have access to all registered orgs.

<figure><img src="../../../.gitbook/assets/image (86) (1).png" alt=""><figcaption></figcaption></figure>

#### Enable org. access control is turned 'On' <a href="#enable-org-access-control-is-turned-on" id="enable-org-access-control-is-turned-on"></a>

1. On the **Add User** screen, the **Salesforce Orgs** field is enabled; the org admin must select Salesforce orgs when registering a new user with the Vault account.
2. Users will have access to the Salesforce orgs that the org admin has enabled.
3. Users can only perform Vault operations in Salesforce orgs to which they have been granted access.

#### Enable org. access control is turned 'Off' <a href="#enable-org-access-control-is-turned-off" id="enable-org-access-control-is-turned-off"></a>

1. All users in the Vault account will have access to all registered Salesforce orgs.
2. User will have privilege to choose orgs whether or not registered by him to carry out the Vault operation.
3. The **Salesforce Orgs List** shows all of the registered orgs that have been added to the Vault account to date.
