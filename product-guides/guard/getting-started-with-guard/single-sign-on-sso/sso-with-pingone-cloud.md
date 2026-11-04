# SSO with PingOne Cloud

Use this guide when your organisation authenticates Guard users through PingOne Cloud with SAML 2.0.

### Before you start

You need:

* PingOne administrator access to the environment that holds your users
* From us:
  * Single sign-on URL (also called the ACS URL or Reply URL)
  * Entity ID (also called the Audience URI or SP Entity ID)

### Step 1: Create the SAML application

1. Sign in to the PingOne admin console.
2. Go to Applications → Applications.
3. Select the + icon to add an application.
4. Enter an application name such as `Guard` and, if you want one, a short description.
5. Choose SAML Application and select Configure.
6. If PingOne asks how to provide the service provider details, choose Manually Enter.

### Step 2: Enter the Guard SAML values

Enter these values:

| Field     | Value                  |
| --------- | ---------------------- |
| ACS URL   | The Single sign-on URL |
| Entity ID | The Entity ID          |

Leave the other settings at their PingOne defaults. In particular, keep the default signing key and keep responses or assertions signed. PingOne cannot connect to Guard until Keycloak has been configured with this application, so do not test the connection yet.

Save the application.

### Step 3: Configure attribute mappings

Open the Guard application and go to Attribute Mappings. PingOne always sends a subject value, called `saml_subject`, which Guard uses to match the user. Map it to the value that matches the existing Guard login, usually the email address.

Add the following mappings so Guard receives profile data on login.

| SAML attribute name | PingOne attribute                                             | Purpose                        |
| ------------------- | ------------------------------------------------------------- | ------------------------------ |
| `saml_subject`      | Email Address (or Username if that matches the Guard login)   | Username match / account merge |
| `firstName`         | Given Name                                                    | First name                     |
| `lastName`          | Family Name                                                   | Last name                      |
| `email`             | Email Address                                                 | Email                          |
| `username`          | Email Address (or the attribute that matches the Guard login) | Username match / account merge |

{% hint style="warning" %}
The subject and `username` values must match the existing Guard login where users already have accounts. If they do not match, Guard may create a second account for the same person. Tell us which value you have used so we can align the Keycloak mappers.
{% endhint %}

If PingOne shows different attribute names in your environment, keep them consistent and tell us the exact names you have used.

For admin access, also release an attribute that we can map to `TENANT-MANAGER`. The simplest option in PingOne is a group attribute:

| SAML attribute name | PingOne attribute | Purpose                                                   |
| ------------------- | ----------------- | --------------------------------------------------------- |
| `role`              | Group Names       | Sends the names of the PingOne groups the user belongs to |

Create a PingOne group for Guard admins, for example `Guard Admins`, and tell us the group name. We will map that group to `TENANT-MANAGER` in Keycloak.

Agree the exact attribute name and group name with us before go-live. A role assigned only inside Keycloak or Guard does not stick across SSO logins, because the PingOne assertion is checked on every login.

### Step 4: Assign users and groups

1. Open the Guard application and go to Access.
2. Add every user or group that should access Guard. Users need to exist in the PingOne environment and be enabled for the application before they can sign in.
3. Make sure Guard admins belong to the admin group in Step 3.
4. Everyone else receives standard Guard user access (after we finish the Keycloak mapping).

### Step 5: Download the IdP metadata and send it to us

1. Open the Guard application and go to Configuration.
2. Download the metadata file using Download Metadata, or copy the metadata URL if your version of PingOne shows one instead.
3. Keep a note of the signing certificate. You do not normally need to send it separately, because it is included in the metadata.

Reply to us with:

* The IdP metadata XML file, or the metadata URL
* The attribute names you configured (`saml_subject`, `firstName`, `lastName`, `email`, `username` and `role`, or your equivalents)
* The name of the PingOne group that identifies Guard admins
* Confirmation that the subject and `username` values match existing Guard logins (usually email)
* Your preferred button label on the Guard login page (for example `Contoso SSO`)

We will then complete the Keycloak side and confirm when you can proceed with testing.

### Step 6: Test

1. Sign out of Guard.
2. Open the Guard login page and choose the SSO option for your organisation.
3. Sign in with a PingOne test user.
4. Confirm:
   * A standard user lands with normal Guard access
   * An admin still has admin access after SSO
   * Existing Guard users are matched to their previous accounts (no unexpected duplicates)

### Optional: assertion encryption

Some organisations require encrypted SAML assertions. If you need this:

1. Ask us for an encryption certificate.
2. In PingOne, open the Guard application and edit the SAML configuration to encrypt the assertion, then upload the certificate.
3. Re-test login after we confirm Keycloak is ready for encrypted assertions.

### Troubleshooting

| Symptom                                                           | What to check                                                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| User reaches Guard as the wrong person or with an opaque username | `saml_subject` or the `username` attribute does not match the Guard login. Prefer email and check the mapping in Step 3. |
| Admin loses admin rights after the next SSO login                 | The admin is not in the PingOne admin group, or the `role` attribute is not being sent.                                  |
| First or last name is blank in Guard                              | The `firstName` or `lastName` mapping is missing, or it is named differently from what we mapped.                        |
| Login fails after a URL change                                    | The ACS URL or Entity ID in PingOne no longer matches the values we configured. Ask us before changing them.             |
| User is told they cannot access the application in PingOne        | The user has not been given access to the Guard application. Check Step 4.                                               |
