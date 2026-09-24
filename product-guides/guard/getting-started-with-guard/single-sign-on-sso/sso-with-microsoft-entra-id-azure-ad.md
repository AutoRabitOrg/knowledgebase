# SSO with Microsoft Entra ID (Azure AD)

Use this guide when your organization authenticates Guard users through Microsoft Entra ID with SAML 2.0.

Guard SSO is configured by AutoRABIT Support in Keycloak. You set up the Entra application and send us the federation metadata.

### Before you start

You need:

* Administrator access to Microsoft Entra ID
* Submit a Support ticket with us by emailing support@autorabit.com&#x20;
* Support will send you:
  * Reply URL (also called Redirect URI or ACS URL)
  * Identifier (Service Provider Entity ID)

### Step 1: Create the enterprise application

1. Sign in to the [Microsoft Entra admin centre](https://entra.microsoft.com/).
2. Go to Identity → Applications → Enterprise applications.
3. Select New application → Create your own application.
4. Enter a name such as `Guard` . Choose "Integrate any other application you don’t find in the gallery (Non-gallery)" and create the app.
5. Open the app and select Single sign-on → SAML.

### Step 2: Enter the Guard SAML values

In Basic SAML Configuration, edit and set:

| Field                                      | Value                                         |
| ------------------------------------------ | --------------------------------------------- |
| Identifier (Entity ID)                     | The Identifier from Support                   |
| Reply URL (Assertion Consumer Service URL) | The Reply URL from Support                    |
| Sign on URL (optional)                     | Your Guard login URL, if Support provides one |

Save the configuration.

### Step 3: Configure claims (attributes)

In Attributes & Claims, make sure these claims are released. Guard maps them on login.

| Claim name                                                           | Source attribute                                          | Purpose                        |
| -------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------ |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`    | `user.givenname`                                          | First name                     |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`      | `user.surname`                                            | Last name                      |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | `user.mail`                                               | Email                          |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`         | Prefer the same value as the Guard username (often email) | Username match / account merge |

{% hint style="warning" %}
The username claim must match the existing Guard login where users already have accounts. If Entra sends email as the unique login instead of Name, tell Support so they can map the email claim as username.
{% endhint %}

### Step 4: Create the admin app role

Guard admins must receive the role claim `TENANT-MANAGER` from Entra. A role assigned only inside Keycloak or Guard does not stick across SSO logins.

1. Open App registrations and select the same Guard application (or the linked app registration).
2. Go to App roles → Create app role.
3. Set:
   * Display name: `TENANT-MANAGER`
   * Allowed member types: Users/Groups
   * Value: `TENANT-MANAGER`
   * Description: Guard tenant administrator
   * Enable the role
4. Save.

Also confirm the SAML token includes the role claim:

`http://schemas.microsoft.com/ws/2008/06/identity/claims/role`

### Step 5: Assign users and groups

1. In the enterprise application, open Users and groups.
2. Assign every user or group that should access Guard.
3. For Guard admins, assign them the TENANT-MANAGER app role.
4. Everyone else can be assigned without that role. They receive standard Guard user access after Support finishes Keycloak mapping.

### Step 6: Download federation metadata and send it to Support

1. In Single sign-on → SAML, under SAML Certificates, download Federation Metadata XML.
2. Reply on the Support ticket with:
   * The Federation Metadata XML file
   * Confirmation of which users or groups are Guard admins (`TENANT-MANAGER`)
   * Confirmation that the username claim matches existing Guard logins (usually email)
   * Your preferred button label on the Guard login page (for example `Contoso SSO`)

Support completes the Keycloak side and confirms when you can test.

### Step 7: Test

1. Sign out of Guard.
2. Open the Guard login page and choose the SSO option for your organization.
3. Sign in with an Entra test user.
4. Confirm:
   * A standard user lands with normal Guard access
   * An admin still has admin access after SSO
   * Existing Guard users are matched to their previous accounts (no unexpected duplicates)

Only after testing should you ask Support to enable Only SSO Authentication for the tenant.

### Troubleshooting

| Problem                                                  | What to check                                                                                                       |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| User reaches Guard as the wrong person / opaque username | Username claim does not match Guard login. Align Name/email claim with Support.                                     |
| Admin loses admin rights after next SSO login            | `TENANT-MANAGER` app role missing in Entra, or role claim not released.                                             |
| Login fails after Redirect URI change                    | Reply URL / Identifier in Entra no longer match the values Support configured. Raise a ticket before changing them. |

<br>
