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

| Item              | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| **`LOGIN URL`**   | The tenant's sign-in URL, `https://<slug>.<your IZ Suite domain>`. |
| **`ADMIN EMAIL`** | The administrator's email address.                                 |

The panel also reports how many rows and tables were seeded into the new tenant.



Share the temporary admin password with the administrator through a separate, secure channel. It is not shown again. The administrator signs in with the **`IZ User`** option using the admin email and this password, and must change it at the first sign-in. If it is lost, the administrator can use **`Forgot password?`** on the sign-in form, provided email is configured for the tenant.



{% hint style="info" %}
Up to 26.3.x the panel showed a one-time **`LOGIN CODE`** for **`Signin with IZ Token`**. From 26.4.1 the IZ Token sign-in is replaced by IZ User Auth (email and password).
{% endhint %}

### First Steps for the Tenant Administrator <a href="#first-steps-for-the-tenant-administrator" id="first-steps-for-the-tenant-administrator"></a>

1.
   1. Open the **`Login URL`**, click **`IZ User`**, sign in with the admin email and the temporary password, and set a new password.
   2. Navigate to **`Global Settings`** → **`Settings`** and configure single sign-on (**`Anypoint Auth`**, **`Google Auth`** or **`Azure Auth`**) using redirect URIs on the tenant hostname.
   3. Optionally review the password, lockout and MFA policy in **`Login Settings`**, and disable **`IZ User Auth`** if your policy requires single sign-on only. Licence administrators can still use the administrator sign-in URL; see [Sign-in and MFA](../sign-in-and-mfa.md).
   4. Invite users or enable automatic user creation.
   5. Configure agents, Connected Apps and schedules based on the requirement.



### Enabling Optional Modules <a href="#enabling-optional-modules" id="enabling-optional-modules"></a>



Optional modules such as **`Compliance`** are not part of the baseline copy. After onboarding, use **`Enable Modules`** on the tenant row to add them.
