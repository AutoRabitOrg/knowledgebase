# Login Settings

* Available from IZ Suite Server **26.3.1**.
* In a multi-tenant installation each tenant has its own **`Login Settings`**

**`Login Settings`** controls what happens when a user signs in through single sign-on for the first time, and how long a session stays valid.



1. Navigate to **`Global Settings`** → **`Settings`**.
2. Search for **`Login Settings`** and click the **`Edit`** action.
3. Update the values described below and click **`Save`**.



| Key                           | Default | Description                                                                                                                                                                                                                                                            |
| ----------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Auto Create New User`**    | `false` | When `true`, a user who authenticates successfully with **`Signin with CloudHub`**, **`Signin with Google`** or **`Microsoft Azure`** but does not yet exist in IZ Suite is created automatically. Does not apply to **`Signin with IZ Token`** or to security tokens. |
| **`Assign Roles`**            | empty   | Comma-separated ids of the roles granted to automatically created users. **Required when auto-create is enabled**: if it is empty, no user is created and the sign-in is rejected.                                                                                     |
| **`Session Timeout Seconds`** | `3600`  | Lifetime of a signed-in session in seconds. After this period the user must sign in again. Must be a positive whole number; invalid values fall back to one hour.                                                                                                      |
| **`Max Cache Entries`**       | `500`   | Reserved for future use.                                                                                                                                                                                                                                               |



### Automatic User Creation <a href="#automatic-user-creation" id="automatic-user-creation"></a>

Without automatic creation, every user must be invited first (see [Invite User](organization/invite-user.md)); a user who signs in through SSO without an invitation is rejected.

With automatic creation:

1. The user signs in with one of the enabled single sign-on options.
2. IZ Suite looks for an enabled user with the same email address (case-insensitive).
3. If none exists, the user is created with the name and email from the identity provider and the roles listed in **`Assign Roles`** are granted.
4. The user is signed in immediately.

#### Finding Role Ids <a href="#finding-role-ids" id="finding-role-ids"></a>

1. Navigate to **`Organization`** → **`Roles`**.
2. Enable the **`Id`** column from the column settings.
3. Copy the ids of the roles to grant, for example a viewer role scoped to the organization new users should see, and enter them separated by commas in **`Assign Roles`**.



* Grant only the minimum roles needed. Anyone who can authenticate with the configured identity provider will receive these roles on first sign-in. Restrict the identity provider application to the intended users or groups (for example **`Who can use this application`** in an Anypoint Connected App, or user assignment in Microsoft Entra ID).
* Users created automatically appear under **`Organization`** → **`Users`** like invited users and can have roles, permissions and organizations adjusted afterwards



### Session Timeout <a href="#session-timeout" id="session-timeout"></a>

**`Session Timeout Seconds`** applies to sessions created after the setting is saved. Existing sessions keep the lifetime they were issued with. Security tokens generated under **`Organization`** → **`Tokens`** and agent sessions are not affected by this setting.

**`Sign Out`** ends the session immediately, regardless of the remaining lifetime.
