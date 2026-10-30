# SSO with Okta

Use this guide when your organisation authenticates Guard users through Okta with SAML 2.0.

### Before you start

You need:

* Okta administrator access
* From us:
  * Single sign-on URL (Reply URL / ACS URL)
  * Audience URI (SP Entity ID)

### Step 1: Create the SAML application

1. Sign in to the Okta Admin Console.
2. Go to Applications → Applications → Create App Integration.
3. Choose SAML 2.0 → Next.
4. Enter an app name (such as `Guard` )→ Next.

### Step 2: Enter the Guard SAML values

On the Configure SAML tab:

| Field                       | Value                                           |
| --------------------------- | ----------------------------------------------- |
| Single sign-on URL          | The Single sign-on URL                          |
| Audience URI (SP Entity ID) | The Audience URI                                |
| Name ID format              | EmailAddress (recommended)                      |
| Application username        | Email (recommended, so it matches Guard logins) |

Leave other defaults. Continue to the feedback step and finish creating the app.

### Step 3: Configure attribute statements

In the SAML app, open Sign On (or edit SAML settings) and add attribute statements so Guard receives profile data on login.

| Name        | Name format | Value                                                        | Purpose                        |
| ----------- | ----------- | ------------------------------------------------------------ | ------------------------------ |
| `firstName` | Unspecified | `user.firstName`                                             | First name                     |
| `lastName`  | Unspecified | `user.lastName`                                              | Last name                      |
| `email`     | Unspecified | `user.email`                                                 | Email                          |
| `username`  | Unspecified | `user.email` (or the attribute that matches the Guard login) | Username match / account merge |

If your Okta org already uses different attribute names, keep them consistent and tell us the exact names so Keycloak mappers can be aligned.

For admin elevation, also release a role or group attribute that we can map to `TENANT-MANAGER`. Common options:

Option A – group attribute

| Name   | Name format | Filter / value                                                                            |
| ------ | ----------- | ----------------------------------------------------------------------------------------- |
| `role` | Unspecified | Filter groups that contain `TENANT-MANAGER`, or send the group name that Support will map |

Option B – custom user attribute

Create a user profile attribute (for example `guardRole`) and set it to `TENANT-MANAGER` for admins. Release it as a SAML attribute named `role`.

Agree the exact attribute name and value with us before go-live. The value we map is `TENANT-MANAGER`.

### Step 4: Assign people and groups

1. Open the Guard app → Assignments.
2. Assign every person or group that should use Guard.
3. Make sure Guard admins are in the admin group or have the custom attribute that releases `TENANT-MANAGER`.
4. Everyone else receives standard Guard user access after we finish Keycloak mapping.

### Step 5: Download IdP metadata and send it to us

1. Open the app → Sign On.
2. In SAML Signing Certificates, open Actions for the active certificate.
3. Choose View IdP metadata.
4. Save the page as an `.xml` file (in Firefox choose All files if needed).

Reply to us with:

* The IdP metadata XML file
* The attribute statement names you configured (`firstName`, `lastName`, `email`, `username`, `role` or equivalent)
* How admins are identified (group name or custom attribute value `TENANT-MANAGER`)
* Confirmation that Application username / username attribute matches existing Guard logins (usually email)
* Your preferred button label on the Guard login page

We will complete the Keycloak side and confirm when you can proceed with testing.

### Step 6: Test

1. Sign out of Guard.
2. Open the Guard login page and choose the SSO option for your organisation.
3. Sign in with an Okta test user.
4. Confirm:
   * A standard user lands with normal Guard access
   * An admin still has admin access after SSO
   * Existing Guard users are matched to their previous accounts

### Optional: assertion encryption

Some organisations require encrypted SAML assertions. If you need this:

1. Ask us for an encryption certificate.
2. In Okta, edit the SAML app → Show advanced settings → set assertion encryption to encrypted and upload the certificate.
3. Re-test login after we confirm Keycloak is ready for encrypted assertions.

### Troubleshooting

| Symptom                                                  | What to check                                                                                               |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| User reaches Guard as the wrong person / opaque username | Application username or `username` attribute does not match Guard login. Prefer email.                      |
| Admin loses admin rights after next SSO login            | `TENANT-MANAGER` is not present in the SAML assertion, or the attribute name does not match what we mapped. |
| First or last name blank in Guard                        | `firstName` / `lastName` attribute statements missing or named differently than we expected.                |
| Login fails after URL change                             | Single sign-on URL / Audience URI in Okta no longer match our Keycloak values. Ask us before changing them. |

***

<br>
