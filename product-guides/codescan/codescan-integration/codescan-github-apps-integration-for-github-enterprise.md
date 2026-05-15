---
hidden: true
---

# CodeScan GitHub Apps Integration for GitHub Enterprise

This page provides a customer-facing overview of CodeScan GitHub Apps Integration for GitHub Enterprise and explains how to set up and configure the integration.



**Prerequisites:**

_Creating the github app:_

[GitHub Apps overview - GitHub Docs](https://docs.github.com/en/apps/overview)

1. While creating the github app, make sure the check box (Request user authorization during installation) is checked under callback URL:

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

This allows the user to install the github app and authorize using the github app at the same time.

2. Set callback url as `/_codescan/oauth2/authorize`
3. Set _**Repository**_ permissions:
   1. Content: read only
   2. Metadata(mandatory) : read only
   3. webhooks: Read and write
4. After creating the Github app, the client id, client secret and github app name env variables must be set in the task definition with the following keys:
   1. GITHUB\_APP\_KEY
   2. GITHUB\_APP\_SECRET
   3. GITHUB\_APP\_NAME\
      These are used to fetch the app installation token/access token that’ll be used to make github API requests and refresh the token.

**User Flow:**

1. User clicks on the github icon.
2. User is redirected to\
   `/_codescan/github/authorize`
   1. Backend generates GitHub App installation URL with extra state parameter “accessType”= “github\_app”
   2. Browser redirects to Github Apps Installation page
3. GitHub redirects to callback URL: `/_codescan/oauth2/authorize`
   1. `code` is received in params
   2. Call is made to `/_codescan/integrations/authorize` with `code`. This code is used to fetch installation access token for the first time.
4. Fetching installation access token
   1. If accessType in parameter == “github\_app”, backend makes request to `https://github.com/login/oauth/access_token` with `code`, GITHUB\_APP\_KEY and GITHUB\_APP\_SECRET to get installation access token and refresh token. This access token expires in **8 hours.**
   2. If accessType is not github\_app, the flow continues the same and they GITHUB\_KEY and GITHUB\_SECRET env variables are used.
   3. The installation access token is stored in projectEncConfig as usual.

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

1. API call is made to get repo list with the access token.
2. User selects repository
3. Create and update project api is called with accessType=github\_app
4. Store accessType=github\_app in ProjectConfig
5. Connection complete - CodeScan works normally

**Refresh token logic:**

1. If projectConfig.accessType==github\_app use the refresh token logic in all other cases use the existing flow.
2. The refresh token API can be called whenever the token is close to expiry(follow bitbucketHandler.java logic). At every API call to githubApps it can be checked if token is expired/close to expiry.

**Questions:**

How are multiple projects and concurrent analysis runs handled across same or different CodeScan orgs?

1. Since, to run an analysis and to make Github API requests, we require:
   1. Active Installation Access token(project level)
   2. Client ID(instance level)
   3. Client Secret(instance level)

Hence, concurrent analysis of different projects will run without any issues.

2. How is authentication type (GitHub App) represented and differentiated?
3. By Storing accessType=oauth/github\_app in ProjectConfig

## **Github Enterprise integration:** <a href="#github-enterprise-integration" id="github-enterprise-integration"></a>

The Github Apps enterprise flow remains the same as the Github apps Cloud except for a few key changes.

1. If for an existing Github Enterprise connection, the accessType is not github\_app, then continue with the older Github Oauth flow else use the new Github Apps flow.
2. Store accessType=github\_app

## &#x20;GitHub App for Enterprise Setup (CodeScan) <a href="#github-app-for-enterprise-setup-codescan" id="github-app-for-enterprise-setup-codescan"></a>

### &#x20;Step 1: Copy & Paste This URL <a href="#step-1-copy-and-paste-this-url" id="step-1-copy-and-paste-this-url"></a>

While being logged in as the admin in the GitHub Enterprise Server, use this link to create a GitHub app:

{% code lineNumbers="true" %}
```
https://YOUR_GHES_HOSTNAME/settings/apps/new?name=codescan-enterprise-app&description=GitHub App for CodeScan integration&url=https://autorabit.com&callback_urls[]=https://YOUR_PUBLIC_BASE/_codescan/oauth2/authorize&request_oauth_on_install=true&public=true&contents=read&metadata=read&repository_hooks=write&setup_on_update=true&webhook_active=false
```
{% endcode %}

### &#x20;What You Need to Change <a href="#what-you-need-to-change" id="what-you-need-to-change"></a>

Before pressing Enter, replace only these two values:

* `YOUR_GHES_HOSTNAME` → Your GitHub Enterprise Server URL\
  &#xNAN;_(Example:_ [_github.company.com_](http://github.company.com/)_)_
* `YOUR_PUBLIC_BASE` → URL of the CodeScan instance\
  &#xNAN;_(Example:_ [_app.codescan.io_](https://app.codescan.io/)_)_

### &#x20;Important <a href="#important" id="important"></a>

* App name must remain exactly: **codescan-enterprise-app** (do not modify)

### &#x20;Step 2: Create the App <a href="#step-2-create-the-app" id="step-2-create-the-app"></a>

* Open the updated URL
* Keep the app **Public** by enabling “Any account”:

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

* Click **Create GitHub App**

### Step 3: Copy Credentials <a href="#step-3-copy-credentials" id="step-3-copy-credentials"></a>

After creation, copy:

* **App ID**
* **Client ID**
* **Client Secret**\
  \
  Paste these details in the ALM connections page in CodeScan and create a new ALM connection

### &#x20;Done <a href="#done" id="done"></a>

Your GitHub App is ready for CodeScan integration.
