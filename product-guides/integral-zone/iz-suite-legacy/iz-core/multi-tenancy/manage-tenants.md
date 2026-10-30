# Manage Tenants

* The **`Manage Tenants`** menu is available only on the **platform tenant** and only when the **`Multi Tenant`** license module is enabled.
* Users need the **`Manage Tenants`** permission



### Tenants <a href="#tenants" id="tenants"></a>

Navigate to **`Manage Tenants`** → **`Tenants`**.

| Column              | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| **`Slug`**          | Tenant identifier used as the sign-in subdomain.                                     |
| **`Name`**          | Display name.                                                                        |
| **`Login Link`**    | The tenant's login URL, `https://<slug>.<your IZ Suite domain>`. Opens in a new tab. |
| **`Contact Name`**  | Contact person. Hidden by default; enable it from the column settings.               |
| **`Contact Email`** | Contact email. Hidden by default.                                                    |
| **`External Link`** | Dedicated hostname of the tenant, if configured.                                     |
| **`Status`**        | **`ACTIVE`**, **`TRIAL`** or **`SUSPENDED`**.                                        |
| **`Created`**       | When the tenant was onboarded.                                                       |

Use **`Search slug / name`** to filter the list.



Toolbar actions:

* **`Onboard Tenant`** - Create a new tenant. See [Onboard Tenant](onboard-tenant.md).
* **`Update Global Settings`** - Push one setting value to several tenants. See below.
* **`Invalidate Tenant Cache`** - Refresh the hostname-to-tenant mapping on all server nodes. See below.

\
Row actions:

* **`Enable Modules`**
* **`Managed Settings`**
* **`Edit Tenant`**
* **`Delete Organizations`**
* **`Delete Tenant`**

For the platform tenant only **`Edit Tenant`** is available.



### Edit Tenant <a href="#edit-tenant" id="edit-tenant"></a>

1. Click **`Edit Tenant`** in the row's action menu.
2. Update the details:
   1. **`Slug`** - Changing the slug changes the login URL already shared with the tenant. See [Tenant URLs and Login](tenant-urls-and-login.md).
   2. **`Name`**
   3. **`Status`** - **`ACTIVE`**, **`SUSPENDED`** or **`TRIAL`**. The platform tenant must stay Active.
   4. **`Contact Name`**, **`Contact Email`**
   5. **`External Link`** - Dedicated hostname for the tenant.
   6. **`Description`**
3. Click **`Save`**.



Clearing an optional field removes the stored value. Changes to the slug or External Link take effect on all server nodes within about 15 seconds.



### Enable Modules <a href="#enable-modules" id="enable-modules"></a>

Optional modules are not part of the baseline that a new tenant receives.

1. Click **`Enable Modules`** on the tenant row.
2. Select the modules to enable. Modules that are already enabled are shown checked and cannot be disabled from this screen.
   * **`Compliance`** - Enables IZ Compliance for the tenant and copies the built-in standards, policy controls and default rule mappings into the tenant.
3. Click **`Submit`**.

The tenant's users see the module's menu after their next sign-in, provided the module is also part of the tenant's license.



### Managed Settings <a href="#managed-settings" id="managed-settings"></a>

Some global settings hold secrets or values that the platform operator may want to control on behalf of a tenant, for example AI provider keys or report storage credentials. **`Managed Settings`** decides, per tenant and per setting, who manages the values.



1. Click **`Managed Settings`** on the tenant row. The dialog **`Managed Settings - <slug>`** opens.
2. Each entry shows the setting name, a tag reading **`Tenant managed`** or **`We manage`**, and a switch:
   * Switch **on** (**`Tenant managed`**): the tenant supplies its own values. The listed keys are visible and editable in the tenant's **`Global Settings`** → **`Settings`**.
   * Switch **off** (**`We manage`**): the platform operator manages the values. Enter the keys under **`MASKED / HIDDEN KEYS`** as a comma-separated list, for example `AI_AGENT_API_KEY, VECTOR_DB_TOKEN`. Those keys are hidden from the tenant's settings screens and cannot be edited by the tenant.
3. Click **`Add Setting`** to add another setting by its name, for example `AI Agent Settings`, and configure it in the same way. Use the remove icon to drop an entry.
4. Click **`Save`**.



Default configuration of a new tenant:

| Setting                 | Mode           | Keys                                                                                                        |
| ----------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| **`AI Agent Settings`** | Tenant managed | `AI_AGENT_API_KEY`, `VECTOR_DB_TOKEN`, `AI_PROVIDER`, `AI_MODEL`, `VECTOR_DB_URL`, `VECTOR_DB_SEARCH_TOKEN` |
| **`Reporting Config`**  | Tenant managed | `PROVIDER`, `REGION`, `CLIENT_ID`, `CLIENT_SECRET`, `BUCKET_NAME`, `SECURE_VALUE_1`                         |
| **`Email Settings`**    | IZ Managed     | `Client Id`, `Client Secret`, `Refresh Token`, `Access URL`, `Host`, `Port`, `Is Secure`, `From Name`       |

Secure values are always masked for tenant users, whichever mode is selected.



### Update Global Settings



1. Click **`Update Global Settings`** in the toolbar.
2. Enter the details:
   1. **`Tenants`** - Select one or more tenants. Options are listed as `<slug> — <name>`.
   2. **`Setting Key`** - Name of the global setting, for example `AI Agent Settings`.
   3. **`Key`** - The entry inside the setting to change, for example `AI_MODEL`.
   4. **`Value`** - The new value.
3. Click **`Submit`**.

A report lists every selected tenant as **`Updated`** or **`Skipped`** with a reason.



### Delete Organizations <a href="#delete-organizations" id="delete-organizations"></a>

Removes organizations, and everything under them, from a tenant without deleting the tenant.



1. Click **`Delete Organizations`** in the row's action menu. The dialog **`Delete Organizations - <slug>`** lists the tenant's organizations as a tree with **`Name`**, **`Ext Id`**, **`Source`** and **`Created`**.
2. Select the organizations to delete. Selecting a parent selects its sub-organizations.
3. Click **`Delete Selected`** and confirm.



Deleting an organization is permanent. All of the organization's data (environments, applications, scans, jobs and permissions) is removed. Sub-organizations are deleted along with their parent.



### Delete Tenant <a href="#delete-tenant" id="delete-tenant"></a>

1. Click **`Delete Tenant`** in the row's action menu.
2. Confirm **`Delete Tenant <slug>`**.'

Deleting a tenant permanently removes all of its data: users, roles, tokens, organizations, applications, scans, schedules, settings, license and audit records. The tenant's license key becomes available for another tenant. The platform tenant cannot be deleted.



### Invalidate Tenant Cache <a href="#invalidate-tenant-cache" id="invalidate-tenant-cache"></a>



Server nodes cache the mapping from hostname to tenant. The cache is refreshed automatically when a tenant is edited; use this action if a hostname still resolves to the wrong tenant, for example after a DNS change.

1. Click **`Invalidate Tenant Cache`** in the toolbar.
2. Click **`Invalidate`**.

The mapping is rebuilt from the database on all server nodes within about 15 seconds.

\
<br>
