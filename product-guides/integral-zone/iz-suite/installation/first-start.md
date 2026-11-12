---
description: >-
  Apply the licence, create the first administrator, sign in and finish the
  setup of a new IZ Suite installation.
---

# First Start

A new installation starts without a licence. The first person to open it applies the licence and becomes its first administrator.

{% hint style="warning" %}
Have ready:

* The licence key from AutoRABIT.
* The address users will open IZ Suite at, for example `https://izsuite.yourcompany.com`.
{% endhint %}

## Apply the Licence

1. Open IZ Suite in a browser. The sign-in card says **This workspace needs a license**.
2. Click **Apply license key**.
3.  On **Set up IZ Suite**, enter:

    | Field                                       | Description                                                                  |
    | ------------------------------------------- | ---------------------------------------------------------------------------- |
    | **License key**                             | The key from AutoRABIT.                                                      |
    | **Base URL**                                | The address users open IZ Suite at. Links in emails sent by IZ Suite use it. |
    | **Admin email**                             | The email of the first administrator.                                        |
    | **Admin password** and **Confirm password** | At least 12 characters, including a number and a special character.          |
4. Click **Apply license**. A **License applied** screen appears; click **Sign in** on it. Setup opens after you sign in.

Applying the licence also registers the built-in agent, so the agent of a [Proof of Concept Installation](proof-of-concept-installation.md) connects shortly after (it restarts on its own).

## Sign In

Sign in with the admin email and password you entered. See [Sign In](../getting-started/sign-in.md).

## Finish the Setup

1. Open [Setup](../administration/setup.md) from the sidebar. Its checklist follows your licence and the choices you make in it.
2. Check that the agent is connected in [Agents](../administration/global-settings/agents.md).
3. Optionally, turn on single sign-on; see [Single Sign-On](../supported-platforms/single-sign-on/).

## Next Steps

* [Setup](../administration/setup.md): connect your platforms and repositories.
* [Agents](../administration/global-settings/agents.md): confirm the agent is connected.
* [Upgrades](upgrades.md): keep the installation up to date.
