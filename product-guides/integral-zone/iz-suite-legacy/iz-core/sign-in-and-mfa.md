# Sign-in and MFA

{% hint style="warning" %}


* Available from IZ Suite Server **26.4.1**.
* In a multi-tenant installation every setting on this page is configured per tenant.
{% endhint %}

From 26.4.1 the **`IZ Token`** web login is replaced by **IZ User Auth**: users sign in to the web application with their email address and a password. Single sign-on through **`Anypoint Auth`**, **`Google Auth`** and **`Azure Auth`** is unchanged, and security tokens generated under **`Organization`** → **`Tokens`** continue to authenticate the IZ Scan CLI, IDE plug-ins and MCP clients. Security tokens can no longer be used to sign in to the web application.

The sign-in option is the **`IZ User Auth`** setting under **`Global Settings`** → **`Settings`** (previously **`IZ Token Auth`**). It is renamed automatically during the upgrade and keeps its **`Is Enabled`** value. On the login page it is shown as **`IZ User`** under **`Sign-in with`**



#### Signing In <a href="#signing-in" id="signing-in"></a>

1. Open the IZ Suite login page and click **`IZ User`**.
2. Enter your **`Email`** and **`Password`** and click **`Sign in`**.
3. If multi-factor authentication is enabled for your tenant, enter the code from your authenticator app.

A wrong email or password is reported as **Invalid email or password**, without saying which of the two was wrong.



**Upgrading from IZ Token Sign-in**

A user who signed in with **`IZ Token`** before the upgrade signs in once more with **`IZ User`**, entering their email address and their **old IZ token as the password**. They are then taken to **`Set a new password`**; once it is saved, the old token no longer works. Users who cannot do this can use **`Forgot password?`**, or an administrator can use **`Set Temporary Password`**.



#### Password Policy <a href="#password-policy" id="password-policy"></a>

| Rule             | Value                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Minimum length   | 12 characters                                                                                             |
| Required content | At least one number and one special character                                                             |
| Storage          | Passwords are stored as salted one-way hashes and cannot be retrieved by anyone, including administrators |
| Maximum age      | **`IZ User Auth Password Max Age`** in Login Settings, 90 days by default                                 |

When a password is older than the maximum age, or when an administrator has set a temporary password, the user is taken to **`Set a new password`** after signing in and must choose a new password before continuing.



#### Account Lockout <a href="#account-lockout" id="account-lockout"></a>

\
After **`Max Failed Login Attempts`** consecutive wrong passwords (5 by default) the account is locked for **`Account Lockout Minutes`** (15 by default). While it is locked, sign-in is refused with **Account locked until \<time>**, even with the right password. Wrong multi-factor codes count towards the same limit. A successful sign-in resets the counter.

Both values are configured in Login Settings.

#### Forgot Password <a href="#forgot-password" id="forgot-password"></a>

1. On the **`IZ User`** sign-in form, click **`Forgot password?`**.
2. Enter your email address and click **`Send reset link`**.
3. Open the link in the email, enter the new password twice and click **`Reset password`**.
4. Click **`Back to sign in`** and sign in with the new password.



* The link is valid for **30 minutes** and can be used **once**. Using a link, or changing the password in any other way, also invalidates every earlier link sent to the same user.
* For privacy, the page always confirms that a link is on its way, whether or not the address belongs to a user.
* Reset emails are sent only when **`IZ User Auth`** is enabled and **`Email Settings`** are configured. The link points to the instance URL configured in the **`Server Base Url`** setting.



#### Invitations <a href="#invitations" id="invitations"></a>

When a user is invited and **`IZ User Auth`** is enabled, the user receives an invitation email with a **`Set your password`** link. The link is valid for **7 days** and can be used once. After setting a password the user signs in with **`IZ User`**.

A user whose link has expired can request a new one with **`Forgot password?`**.



#### Multi-Factor Authentication <a href="#multi-factor-authentication" id="multi-factor-authentication"></a>

\
Multi-factor authentication (MFA) is switched on per tenant with the **`MFA Enabled`** entry of (`false` by default). It applies to **`IZ User`** sign-in; users who sign in through single sign-on use the MFA of their identity provider.



**Enrolling an Authenticator**

\
The first time a user signs in after MFA is enabled:<br>

1. The **`Set up your authenticator`** screen shows a QR code and a manual key.
2. Scan the QR code with Google Authenticator, Microsoft Authenticator, 1Password or any other TOTP authenticator app, or enter the manual key.
3. Enter the 6-digit code shown by the app and click **`Verify`**.
4. The **`Save your recovery codes`** screen shows 8 one-time recovery codes. Copy them to a safe place: they are shown only once. Click **`I have saved them, continue`**.



**Signing In with MFA**

\
After entering the email and password, enter the 6-digit code from the authenticator app. If the device is lost, click **`Lost your authenticator? Use a recovery code`** and enter one of the recovery codes. Each recovery code works only once.

The code must be entered within five minutes of the password step; otherwise the message **MFA session expired, sign in again** is shown.



#### Administrator Actions <a href="#administrator-actions" id="administrator-actions"></a>

Under **`Organization`** → **`Users`**, the actions menu of a user offers:

| Action                       | Effect                                                                                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Set Temporary Password`** | Sets a password for the user, following the password policy. The user must change it at their next sign-in.                                    |
| **`Reset MFA`**              | Removes the user's authenticator and recovery codes, for example after a lost device. The user sets up an authenticator again at next sign-in. |

Both actions require the **`Generate Security Token For Another User`** permission and are not offered for security token rows.

