# Single Sign-On

People can sign in to IZ Suite with their MuleSoft Anypoint or Microsoft Azure account instead of an email and password. You register an app with the identity provider, save its details in Setup, and choose whether IZ Suite creates an account for people who sign in for the first time.

The single sign-on step appears in Setup when your licence covers MuleSoft Anypoint or Azure and that platform is ticked under **What do you use?** in Setup. Each provider card follows the same rule.

{% hint style="warning" %}
You need a role that can change global settings to set up single sign-on. Turning on **Create people on first sign-in** also needs a role that can assign roles.
{% endhint %}

## How Single Sign-On Works

1. On the sign-in page, the person clicks the identity provider's option under **Sign in with**.
2. The identity provider asks them to sign in and returns them to IZ Suite's redirect URL.
3. IZ Suite looks for an enabled person with the same email address.
4. If there is one, they are signed in. If there is none, they are created with the roles you chose, but only when **Create people on first sign-in** is on; otherwise the sign-in is refused.

Two-factor authentication for single sign-on is handled by the identity provider. IZ Suite's own two-factor authentication applies to email-and-password sign-in only.

## Sign-In Options

| Option                    | People sign in with                                          | Page                                      |
| ------------------------- | ------------------------------------------------------------ | ----------------------------------------- |
| [**IZ User**](iz-user.md) | Their email address and an IZ Suite password. On by default. | IZ User                                   |
| **MuleSoft Anypoint**     | Their Anypoint Platform account.                             | [Anypoint Platform](anypoint-platform.md) |
| **Microsoft Azure**       | Their Microsoft Entra ID (Azure) work account.               | [Azure](azure.md)                         |

All options are set up in one Setup drawer: open **Administration** → **Setup** and click **Set up** (or **Review**) on **Let people sign in with single sign-on**. Each provider has its own card and saves on its own.

<figure><img src="../../../../../.gitbook/assets/v2-plat-sso (1).png" alt="Let people sign in with single sign-on drawer with the MuleSoft Anypoint and Microsoft Azure sign-in cards, redirect URLs, switches and client details"><figcaption></figcaption></figure>

## Create People on First Sign-In

By default, only people you invited can sign in with single sign-on. To let anyone who can sign in at the identity provider in:

1. In the same drawer, turn on **Create people on first sign-in**.
2. Under **Roles for new people**, choose at least one role. Every person created this way gets all of these roles.
3. Click **Save**.

People created this way appear under [Users](../../administration/organizations/users.md) like invited people, and you can change their roles later.

{% hint style="danger" %}
Anyone who can sign in through the identity provider gets these roles. Keep the roles narrow, and restrict the app to the intended people at the provider (for example **Who can use this application?** in Anypoint, or user assignment in Microsoft Entra ID).
{% endhint %}

## Next Steps

* [IZ User](iz-user.md): email-and-password sign-in, two-factor authentication and lockouts.
* [Anypoint Platform](anypoint-platform.md): set up Anypoint sign-in.
* [Azure](azure.md): set up Microsoft Azure sign-in.
* [Sign In](../../getting-started/sign-in.md): what people see when they sign in.
* [Users](../../administration/organizations/users.md): invite people, reset two-factor authentication and set temporary passwords.
* [Setup](../../administration/setup.md): the other platform steps.
* [Supported Platforms](../): back to the platform overview.
