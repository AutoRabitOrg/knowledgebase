# Add a Project to CodeScan from GitHub Enterprise

CodeScan supports the GitHub App authentication flow across all supported GitHub editions. This article covers the supported editions, the end-to-end authentication flow, and known limitations.

## Supported GitHub Editions <a href="#supported-github-editions" id="supported-github-editions"></a>

<table data-header-hidden><thead><tr><th></th><th></th><th width="210.609375"></th><th></th></tr></thead><tbody><tr><td><strong>GitHub Edition</strong></td><td><strong>Should GitHub App be created manually?</strong></td><td><strong>Authentication Flow</strong></td><td><strong>Guide</strong></td></tr><tr><td><strong>GitHub.com (Free / Pro / Team)</strong></td><td>No</td><td>GitHub App authorization and installation are managed by CodeScan.</td><td><a href="https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/add-a-project-to-codescan-from-github">Follow these steps</a></td></tr><tr><td><strong>GitHub.com (GitHub Enterprise Cloud) (GHEC)</strong></td><td>No</td><td>GitHub App authorization and installation are managed by CodeScan.</td><td><a href="https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/add-a-project-to-codescan-from-github-enterprise#github-free-pro-team-and-github-enterprise-cloud-flow">Follow these steps</a></td></tr><tr><td><strong>GitHub Enterprise Server (GHES) — Self-Hosted</strong></td><td>Yes</td><td>User should create and configure the GitHub App; GitHub App details to be added in ALM Connections by a CodeScan Admin.</td><td><a href="https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/add-a-project-to-codescan-from-github-enterprise#github-enterprise-server-self-hosted-flow-ghes">Follow these steps</a></td></tr></tbody></table>

{% hint style="info" %}
"GitHub Enterprise Cloud" is the SaaS offering hosted by GitHub.

"GitHub Enterprise Server" is the on-premises / self-hosted appliance.
{% endhint %}

## GitHub Enterprise Cloud Flow <a href="#github-free-pro-team-and-github-enterprise-cloud-flow" id="github-free-pro-team-and-github-enterprise-cloud-flow"></a>

### Step-by-Step guide <a href="#first-time-authentication-flow" id="first-time-authentication-flow"></a>

When attaching a GitHub repository to an analysis project for the first time:

1. Select GitHub as the source in CodeScan (Add Analysis Project → GitHub):

<figure><img src="../../../../../.gitbook/assets/image (2523).png" alt=""><figcaption></figcaption></figure>

2. CodeScan will redirect the user back to GitHub.
3. On the "Authorize & Install CodeScan GitHub App" screen, pick the account or organization that owns the repository:

<figure><img src="../../../../../.gitbook/assets/image (2528).png" alt="" width="375"><figcaption></figcaption></figure>

3. This authorizes and installs the CodeScan GitHub App on the chosen account or organization.
4. GitHub will redirect the user back to CodeScan.
5. Repositories from the selected account/organization are now available for analysis.

{% hint style="info" %}
Please make sure to choose the correct account or organization on the first install.
{% endhint %}

### Organization Permission Behavior <a href="#organization-permission-behavior" id="organization-permission-behavior"></a>

Based on the user's permissions, there are two possible scenarios.

#### **Scenario 1: You're an Organization Owner/Admin**

If the user attaching the analysis is a CodeScan Admin + GitHub Organization Owner (or has app-install rights enabled by the owner):

* The GitHub App installation is approved instantly.
* Authentication completes successfully.
* Organization repositories become available in CodeScan immediately after authorization.

#### **Scenario 2: You're an Organization Member (Non-Owner)**

If the user attaching the analysis is an organization member and does not have permission to install GitHub Apps:

1. On the install screen, GitHub offers a Request option instead of Install.
2. The user submits the installation request.
3. GitHub sends an email notification to the Organization Owner(s).
4. The Organization Owner must approve the request from either email or manually via\
   GitHub → Organization Settings → GitHub Apps → Pending requests.
5. After approval, the user should attempt to attach the project again. The authentication completes automatically then and the organization's repositories become available in CodeScan.

{% hint style="info" %}
Approval is required only once per organization. Once the CodeScan GitHub App is installed on an organization, subsequent users from that organization will not need any further approval; authentication is seamless for them.
{% endhint %}

#### Pending Approval / Rejected Scenarios <a href="#pending-approval-rejected-scenarios" id="pending-approval-rejected-scenarios"></a>

If a user retries the GitHub authentication flow while their installation request is still awaiting approval (or has been rejected), the following message will be displayed:

<figure><img src="../../../../../.gitbook/assets/image (2529).png" alt="" width="375"><figcaption></figcaption></figure>

This means that your installation request has already been submitted and is waiting for your organization's owner approval. Because you are a member of the organization (not an owner), the request was sent.

To follow up, you can connect with the owner of your organization and ask them to approve it under **GitHub → Organization Settings → GitHub Apps → Pending requests**. Once approved, return to CodeScan and click **Add Analysis Project** again. You should be able to connect project successfully now.

This message appears when:

* The Organization Owner has not yet approved the pending request.
* The user retries authentication before approval is granted.
* The Organization Owner has rejected the installation request.

## GitHub Enterprise Server (Self-Hosted) Flow (GHES) <a href="#github-enterprise-server-self-hosted-flow-ghes" id="github-enterprise-server-self-hosted-flow-ghes"></a>

For GitHub Enterprise Server (GHES), a GitHub App should be created on the GHES instance and connected to CodeScan via an ALM Connections.

### Step-by-Step guide <a href="#setup-process" id="setup-process"></a>

Before attaching a project in CodeScan, you should:

* Create a dedicated GitHub App on your GHES instance.
* Configure the GitHub App with the required permissions, events, and callback URL

1. **Creating the GitHub App on GHES.**

On your GHES instance, navigate to Settings → Developer settings → GitHub Apps → New GitHub App, and create the App with the permissions listed here:

[GitHub Authentication using GitHub Apps (CodeScan) | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/enterprise-git-connections/github-authentication-using-oauth-codescan)

2. **Add the ALM Connection in CodeScan.**

Navigate to CodeScan → Administration → ALM Integrations → GitHub Enterprise Server → Add Connection, and paste in the App ID, Client ID, Client Secret from the GitHub App you created in Step 1, along with your GHES base URL.

3. **Authenticate and analyze repositories.**

Users in your GHES organizations can now navigate to **Add Analysis Project** → **GitHub** and follow the same authentication flow described for GitHub Enterprise Cloud above.

## Known limitations <a href="#faq" id="faq"></a>

### Repository Visibility limitation <a href="#github-limitation-repository-visibility-for-repo-admins" id="github-limitation-repository-visibility-for-repo-admins"></a>

{% hint style="info" %}
This section can be skipped unless your organization has enabled the 'Allow repository admins to install GitHub Apps' setting.
{% endhint %}

For an organization member to attach a GitHub analysis project, they must have repository admin access on GitHub. This is a GitHub permission requirement.

If your GitHub organization has enabled **Allow repository admins to install GitHub Apps** **for their repositories**, Repository admins can directly install the CodeScan GitHub App on the specific repositories they manage.

<figure><img src="../../../../../.gitbook/assets/image (2524).png" alt=""><figcaption></figcaption></figure>

However, due to a GitHub limitation, repositories outside their administration are not visible during install and remain inaccessible until the Organization Owner explicitly grants access.

<figure><img src="../../../../../.gitbook/assets/image (2532).png" alt="" width="375"><figcaption></figcaption></figure>

## FAQ <a href="#faq" id="faq"></a>

Q: I already installed the CodeScan GitHub App on one GitHub organization (or personal account) through the CodeScan UI. How do I install it on another organization or personal account?

A: The CodeScan UI only walks you through the GitHub App installation for one account or organization at a time — whichever you select on the first install screen. If you need to add CodeScan to a different GitHub organization or personal account, you cannot do it from the CodeScan UI again. Instead, follow the steps in the section below ("How to Install the CodeScan GitHub App on Another GitHub Org or Personal Account") to install the app directly from GitHub using your install link.

### How to Install the CodeScan GitHub App on Another GitHub Org or Personal Account <a href="#how-to-install-the-codescan-github-app-on-another-github-org-or-personal-account" id="how-to-install-the-codescan-github-app-on-another-github-org-or-personal-account"></a>

<figure><img src="../../../../../.gitbook/assets/image (2559).png" alt=""><figcaption></figcaption></figure>

1. **Step 1: Find Your Install Link**

Take your CodeScan URL → replace every dot (.) with a dash (-) → put it after [https://github.com/apps/](https://github.com/apps/)

Examples:

| **CodeScan URL**                                                     | **GitHub App Install Link**                                                                                  |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [app.codescan.io](http://app.codescan.io/)                           | [https://github.com/apps/app-codescan-io](https://github.com/apps/app-codescan-io)                           |
| [app-eu.codescan.io](http://app-eu.codescan.io/)                     | [https://github.com/apps/app-eu-codescan-io](https://github.com/apps/app-eu-codescan-io)                     |
| [bank-codescan.autorabit.com](http://penfed-codescan.autorabit.com/) | [https://github.com/apps/bank-codescan-autorabit-com](https://github.com/apps/penfed-codescan-autorabit-com) |

2. **Step 2: Open the Link**
3. **Step 3: Choose the org / account for Installation**
4.  **Step 4: Choose Repo Access**

    * **All repositories (recommended) — covers future repos automatically.**
    * Only select repositories — you'll have to come back and add every new repo manually.

    Pick All repositories if you want new repos to be scanned by CodeScan without extra work.
5. **Step 5: Click Install**
   1. Owner: The app installs right away. In CodeScan, click Add Analysis Project to begin scanning.
   2. Member (non-owner): GitHub will show that an installation request was submitted. See the steps below for approval.
   3. Ask your organization owner to approve via the email notification or manually at GitHub Org → Settings → GitHub Apps → Pending requests → Approve (set access to All repositories if desired), then retry Add Analysis Project.
6. **Step 6: After Install — Verify**

Go to GitHub → Settings → GitHub Apps → CodeScan → Configure and confirm your repositories are listed.\
Switch to All repositories to have CodeScan automatically include any new repositories you create later.
