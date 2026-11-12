# IZ User

**IZ User** is IZ Suite's own sign-in: people sign in with their email address and a password. It is on by default, next to any single sign-on option you add. People get an IZ User account when you invite them in [Users](../../administration/organizations/users.md).

<figure><img src="../../../../../.gitbook/assets/.gitbookassetssign-in-form (1).png" alt="Sign in to IZ Suite form with Email and Password fields"><figcaption><p>The IZ User sign-in form</p></figcaption></figure>

On the sign-in page, people click **IZ User** under **Sign in with**, enter their **Email** and **Password**, and click **Sign in**. **Forgot password?** sends a reset link. See [Sign In](../../getting-started/sign-in.md).

## Turn Off Password Sign-In

When everyone signs in with single sign-on, you can turn off email-and-password sign-in:

1. Sign in to IZ Suite with single sign-on yourself. This keeps you from being locked out.
2. Open **Administration** → **Setup**, click **Review** on **Let people sign in with single sign-on**, and switch **Password sign-in** off.

With password sign-in off, the **IZ User** option leaves the sign-in page and password reset emails are not sent. Switch it on again at any time.

## Two-Factor Authentication and Sign-In Limits

The **Login Settings** setting controls two-factor authentication and the sign-in limits for email-and-password sign-in. Change it under **Administration** → **Global Settings** → **Settings**.

| Key                               | Default | Description                                                                                                                                                                                                                         |
| --------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MFA Enabled**                   | `false` | When `true`, people who sign in with their email and password must also enter a code from an authenticator app. People without an authenticator set one up at their next sign-in (see [Sign In](../../getting-started/sign-in.md)). |
| **Max Failed Login Attempts**     | `5`     | Wrong passwords or codes in a row after which the account is locked.                                                                                                                                                                |
| **Account Lockout Minutes**       | `15`    | How long a locked account stays locked.                                                                                                                                                                                             |
| **IZ User Auth Password Max Age** | `90`    | Days after which a password must be changed at the next sign-in.                                                                                                                                                                    |
| **Session Timeout Seconds**       | `3600`  | How long a signed-in session lasts, for every sign-in option.                                                                                                                                                                       |

When someone loses their authenticator and their recovery codes, use **Reset MFA** on their row in [Users](../../administration/organizations/users.md). They set up an authenticator again at their next sign-in.

## Next Steps

* [Single Sign-On](./): the sign-in options and who gets in on first sign-in.
* [Anypoint Platform](anypoint-platform.md): let people sign in with their Anypoint account.
* [Azure](azure.md): let people sign in with their Microsoft account.
* [Users](../../administration/organizations/users.md): invite people, reset two-factor authentication and set temporary passwords.
