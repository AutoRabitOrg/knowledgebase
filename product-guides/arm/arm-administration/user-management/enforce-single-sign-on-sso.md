# Enforce Single Sign-On (SSO)

Enforcing **Single Sign-On (SSO)** guarantees that every team member authenticates through your identity provider (IdP), enhancing security and simplifying password policies. Administrators can enable or selectively override SSO as needed.

---

## Enforce SSO for All Users

1. Open **My Account**.  
2. In **SSO Configuration**, tick **Disable login with AutoRABIT credentials**.  
3. Click **Save**.

From now on, all users must log in via SSO. Org Administrators can still sign in with either SSO **or** their AutoRABIT username/password—useful for IdP outages.

---

### Override SSO for Specific Users <a href="#how-to-override-single-signon-sso" id="how-to-override-single-signon-sso"></a>

An Org Admin can exempt individuals (e.g., contractors) from SSO without disabling it globally.

1. Go to **Admin › Users**.  
2. Select the user(s) you want to exempt.  
3. Untick the **Enforce SSO** checkbox next to their names.  
4. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image.gif" alt="Unchecking Enforce SSO for selected users"></figure>

{% hint style="info" %}
* Enabling **Disable login with AutoRABIT credentials** auto-checks **Enforce SSO** for every user.  
* You can override on a per-user basis at any time.
{% endhint %}
