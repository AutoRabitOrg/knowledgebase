# GitHub Authentication using GitHub Apps (CodeScan)

{% hint style="info" %}
**This integration has recently switched from using OAuth 2.0 to GitHub Apps.** &#x20;

If you are currently using the OAuth version of this integration, you do not have to change anything. AutoRABIT will continue to support all current projects of this type. However, all future connections must be made with the GitHub Apps flow below.
{% endhint %}

Connecting AutoRABIT (CodeScan) to GitHub Enterprise requires a secure handshake based on the GitHub Apps Framework.

**Applies To**

* GitHub Enterprise Server (self-managed) deployments; not applicable to [GitHub](https://www.github.com/).

**Generate Client ID and Client Secret**

1. Log in to your GitHub Enterprise Server with an admin account.
2. To create a GitHub App, copy the URL below.  \
   `https://YOUR_GHES_HOSTNAME/settings/apps/new?name=codescan-enterprise-app&description=GitHub%20App%20for%20CodeScan%20integration&url=https://autorabit.com&callback_urls[]=https://YOUR_PUBLIC_BASE/_codescan/oauth2/authorize&request_oauth_on_install=true&public=true&contents=read&metadata=read&statuses=write&pull_requests=read&repository_hooks=write&setup_on_update=true&webhook_active=false`
3.  Edit the URL by replacing the following placeholders:

    * `YOUR_GHES_HOSTNAME` → Your GitHub Enterprise Server URL\
      &#xNAN;_(Example:_ [_github.company.com_](http://github.company.com/)_)_
    * `YOUR_PUBLIC_BASE` → URL of the CodeScan instance\
      &#xNAN;_(Example:_ [_app.codescan.io_](https://app.codescan.io/)_)_

    <i class="fa-message-exclamation">:message-exclamation:</i>  NOTE: App name must remain exactly: **codescan-enterprise-app** (do not modify this).
4. Paste the URL into your browser.
5.  Keep the app public by enabling **Any Account.**<br>

    <figure><img src="../../../../.gitbook/assets/image (2489).png" alt=""><figcaption></figcaption></figure>
6. Click **Create GitHub App**
7. After creation, copy the App ID, Client ID and Client Secret, and use our [ALM Configuration Article](configuring-and-managing-alm-integrations.md) to complete your setup.
