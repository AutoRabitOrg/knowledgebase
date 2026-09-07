# Onboard Tenant

Before onboarding a tenant, make sure you have:



* A license key issued for the tenant. A license key can be applied to only one tenant.
* The email address of the person who will administer the tenant.
* DNS and TLS in place for the tenant hostname.
* The **`Manage Tenants`** permission on the platform tenant.



### Onboarding a Tenant <a href="#onboarding-a-tenant" id="onboarding-a-tenant"></a>

1. Sign in to the **platform tenant** and navigate to **`Manage Tenants`** → **`Tenants`**.
2. Click **`Onboard Tenant`**.
3. Enter the details:

| Field               | Required | Description                                                                                                                                                                                   |
| ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Slug`**          | Yes      | Short identifier used as the tenant's sign-in host, for example `acme` gives `acme.<your IZ Suite domain>`. Must be unique. Use lowercase letters and digits so that it is a valid DNS label. |
| **`Name`**          | Yes      | Display name of the tenant, for example `Acme Corporation`. Also used to name the tenant's first organization (`Acme Corporation Org`).                                                       |
| **`Admin Email`**   | Yes      | Email address of the tenant administrator. Recorded as the tenant's contact email.                                                                                                            |
| **`License Key`**   | Yes      | License key generated for this tenant with the applicable modules. Rejected if it is already applied to another tenant.                                                                       |
| **`Contact Name`**  | No       | Name of the tenant's contact person.                                                                                                                                                          |
| **`External Link`** | No       | A dedicated hostname for the tenant, for example `https://quality.acme.com`. Requests to this hostname resolve to the tenant.                                                                 |
| **`Description`**   | No       | Free-text description.                                                                                                                                                                        |

4. Click **`Provision`**.

Provisioning takes a few seconds. If the slug is already in use, or the license key is applied to another tenant, an error is shown and nothing is created.



### After Provisioning <a href="#after-provisioning" id="after-provisioning"></a>

A **`Tenant provisioned`** panel is displayed. Share its contents with the tenant administrator:

| Item              | Description                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`LOGIN URL`**   | The tenant's sign-in URL, `https://<slug>.<your IZ Suite domain>`.                                                                                                          |
| **`ADMIN EMAIL`** | The administrator's email address.                                                                                                                                          |
| **`LOGIN CODE`**  | A **one-time** code used with **`Signin with IZ Token`** on the tenant's login page. It is shown only once and cannot be retrieved later. Copy it before closing the panel. |

The panel also reports how many rows and tables were seeded into the new tenant.



Store the login code securely. If it is lost before the administrator's first sign-in, the tenant has to be deleted and onboarded again. After the first sign-in, generate an emergency administrator token under **`Organization`** → **`Tokens`** so that the tenant never depends on a single credential.



### First Steps for the Tenant Administrator <a href="#first-steps-for-the-tenant-administrator" id="first-steps-for-the-tenant-administrator"></a>

1. Open the **`LOGIN URL`**, click **`Signin with IZ Token`** and enter the **`LOGIN CODE`**.
2. Navigate to **`Global Settings`** → **`Settings`** and configure single sign-on (**`Anypoint Auth`**, **`Google Auth`** or **`Azure Auth`**) using redirect URIs on the tenant hostname.
3. Generate an emergency administrator token under **`Organization`** → **`Tokens`** and store it safely, then disable **`IZ Token Auth`** if your policy requires it.
4. Invite users or enable automatic user creation.
5. Configure agents, Connected Apps and schedules based on the requirement.



### Enabling Optional Modules <a href="#enabling-optional-modules" id="enabling-optional-modules"></a>



Optional modules such as **`Compliance`** are not part of the baseline copy. After onboarding, use **`Enable Modules`** on the tenant row to add them.
