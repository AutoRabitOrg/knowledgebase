---
hidden: true
---

# Add a Project to CodeScan from GitHub Enterprise

CodeScan supports the GitHub App authentication flow across all supported GitHub editions. This article covers the supported editions, the end-to-end first-time authentication flow, permission behavior, and known limitations.

## Supported GitHub Editions <a href="#supported-github-editions" id="supported-github-editions"></a>

| **GitHub Edition**                                                          | **Customer must create a GitHub App?** | **Authentication Flow**                                                                                                        |
| --------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **GitHub.com (Free / Pro / Team)**                                          | No                                     | GitHub App authorization and installation are managed by CodeScan.                                                             |
| [**GitHub.com**](http://github.com/) **(GitHub Enterprise Cloud) ( GHEC )** | No                                     | GitHub App authorization and installation are managed by CodeScan.                                                             |
| **GitHub Enterprise Server (GHES) — Self-Hosted**                           | Yes                                    | Customer creates and configures the GitHub App; GitHub App details to be added in ALM Connections Section by a CodeScan admin. |

{% hint style="info" %}
"GitHub Enterprise Cloud" is the SaaS offering hosted by GitHub.&#x20;

"GitHub Enterprise Server" is the on-premises / self-hosted appliance.&#x20;

The integration flow differs only for GitHub Enterprise Server (GHES).
{% endhint %}

## GitHub (Free / Pro / Team) & GitHub Enterprise Cloud Flow <a href="#github-free-pro-team-and-github-enterprise-cloud-flow" id="github-free-pro-team-and-github-enterprise-cloud-flow"></a>

#### First-Time Authentication Flow <a href="#first-time-authentication-flow" id="first-time-authentication-flow"></a>

When a user analyzes a GitHub repository for the first time:

1. The user selects GitHub as the source in CodeScan (Add Analysis Project → GitHub).
2. CodeScan redirects the user to GitHub.
3. GitHub displays the "Authorize & Install CodeScan GitHub App" screen, where the user picks the account or organization that owns the repositories they want to scan.
4. ![3pic.png](https://media-cdn.atlassian.com/file/6a667b10-9821-4bf9-a358-a5d7e8fcac3c/image/cdn?allowAnimated=true\&client=edba5115-c6ab-4222-8129-1768e20983cf\&collection=contentId-2562687035\&height=125\&max-age=2592000\&mode=full-fit\&source=mediaCard\&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlZGJhNTExNS1jNmFiLTQyMjItODEyOS0xNzY4ZTIwOTgzY2YiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0yNTYyNjg3MDM1IjpbInJlYWQiXX0sImV4cCI6MTc3OTk1OTQ5MiwibmJmIjoxNzc5OTU2NjEyLCJhYUlkIjoiNjJjZmUyY2VjNTM3ZjQ2MGQ0NDViOWNlIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL2FwcEFjY3JlZGl0ZWQiOmZhbHNlLCJhdXRoVHlwZSI6InNlc3Npb24ifQ.xwGEegy7legoPuTjwKQQ3xbNWFeHh853OK4he94cSPE\&width=760#media-blob-url=true\&id=6a667b10-9821-4bf9-a358-a5d7e8fcac3c\&clientId=edba5115-c6ab-4222-8129-1768e20983cf\&contextId=contentId-2562687035\&collection=contentId-2562687035)
5. The user authorizes and installs the CodeScan GitHub App on the chosen account or organization.
6. GitHub redirects the user back to CodeScan.
7. Repositories from the selected account / organization become available for analysis.

**Important — Choose the correct account or organization on first install.**

When GitHub shows the "Where do you want to install codescan github app?" screen, the account or organization you pick is the only one CodeScan binds to for the install.

Before clicking install, confirm where your repositories actually live (your personal GitHub account vs. a specific organization), and choose that target.

#### Organization Permission Behavior <a href="#organization-permission-behavior" id="organization-permission-behavior"></a>

**When the First User is an Organization Owner or Admin**

If the first user performing the analysis on an organization is a GitHub Organization Owner (or has app-install rights enabled by the owner):

* The GitHub App installation is approved instantly.
* Authentication completes successfully.
* Organization repositories become available immediately in CodeScan.

**When the First User is an Organization Member (Non-Owner)**

If the first user is only an organization member and does not have permission to install GitHub Apps:

1. On the install screen, GitHub presents a Request option instead of Install.
2. The user submits the installation request.
3. GitHub sends an email notification to the Organization Owner(s).
4. The Organization Owner must approve the request from either email or manually via\
   GitHub → Organization Settings → GitHub Apps → Pending requests.
5. After approval, the user retries the analysis flow once — authentication then completes automatically and the organization's repositories become available in CodeScan.

Note — Approval is required only once per organization. Once the CodeScan GitHub App is installed on an organization, subsequent users from that organization will not need any further approval — authentication becomes seamless for them.

***

#### GitHub Limitation — Repository Visibility for Repo Admins <a href="#github-limitation-repository-visibility-for-repo-admins" id="github-limitation-repository-visibility-for-repo-admins"></a>

By default this do apply — skip this section unless your organization has enabled the 'Allow repository admins to install GitHub Apps' setting.

For an organization member to scan a repository via CodeScan, they must have **repository admin access on GitHub**. This is a GitHub permission requirement.

If your GitHub organization has enabled\
Organization Settings → GitHub Apps → Allow repository admins to install GitHub Apps for their repositories,\
**Repository admins can directly install the CodeScan GitHub App** on the specific repositories they manage.



However, due to a GitHub limitation, repositories outside their admin scope are not visible during install and remain inaccessible until the Organization Owner explicitly grants access.



&#x20;

**Resolution**

Ask the Organization Owner to open Organization Settings → GitHub Apps → CodeScan → Configure, set Repository access to All repositories (or Only select repositories with the missing repos explicitly added), then click Save.

#### Pending Approval / Rejected Scenarios <a href="#pending-approval-rejected-scenarios" id="pending-approval-rejected-scenarios"></a>

If a user retries the GitHub authentication flow while their installation request is still awaiting approval (or has been rejected), Github displays the following message :

![2pic.png](https://media-cdn.atlassian.com/file/08259316-336f-47cc-acd2-f2411aafd69e/image/cdn?allowAnimated=true\&client=edba5115-c6ab-4222-8129-1768e20983cf\&collection=contentId-2562687035\&height=125\&max-age=2592000\&mode=full-fit\&source=mediaCard\&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlZGJhNTExNS1jNmFiLTQyMjItODEyOS0xNzY4ZTIwOTgzY2YiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0yNTYyNjg3MDM1IjpbInJlYWQiXX0sImV4cCI6MTc3OTk1OTQ5MiwibmJmIjoxNzc5OTU2NjEyLCJhYUlkIjoiNjJjZmUyY2VjNTM3ZjQ2MGQ0NDViOWNlIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL2FwcEFjY3JlZGl0ZWQiOmZhbHNlLCJhdXRoVHlwZSI6InNlc3Npb24ifQ.xwGEegy7legoPuTjwKQQ3xbNWFeHh853OK4he94cSPE\&width=760#media-blob-url=true\&id=08259316-336f-47cc-acd2-f2411aafd69e\&clientId=edba5115-c6ab-4222-8129-1768e20983cf\&contextId=contentId-2562687035\&collection=contentId-2562687035)

"What this means:" : Your installation request has already been submitted and is waiting for your organization owner's approval. Because you are a member of the organization (not an owner), the request was emailed to the owner. To follow up, contact the owner and ask them to approve it under **GitHub → Organization Settings → GitHub Apps → Pending requests**. Once approved, return here and click **Add Analysis Project** again.

This message can appear when:

* The Organization Owner has not yet approved the pending request.
* The user retries authentication before approval is granted.
* The Organization Owner has rejected the installation request.

***

## GitHub Enterprise Server (Self-Hosted) Flow (GHES) <a href="#github-enterprise-server-self-hosted-flow-ghes" id="github-enterprise-server-self-hosted-flow-ghes"></a>

For GitHub Enterprise Server (GHES) deployments, the customer creates and owns the GitHub App on their GHES instance, and connects it to CodeScan via an ALM Connection.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before integrating, ensure the following:

* Create a dedicated GitHub App on your GHES instance.
* Configure the GitHub App with the required permissions, events, and callback URL (see below).

#### Setup Process <a href="#setup-process" id="setup-process"></a>

1. **Create the GitHub App on GHES.** On your GHES instance, go to Settings → Developer settings → GitHub Apps → New GitHub App, and create the App with the permissions listed in the documentation: [GitHub Authentication using GitHub Apps (CodeScan) | AutoRABIT Knowledge Base](https://knowledgebase.autorabit.com/product-guides/codescan/getting-started/using-codescan/adding-projects-to-codescan/enterprise-git-connections/github-authentication-using-oauth-codescan)
2. **Add the ALM Connection in CodeScan.** Navigate to CodeScan → Administration → ALM Integrations → GitHub Enterprise Server → Add Connection, and paste in the App ID, Client ID, Client Secret from the GitHub App you created in Step 1, along with your GHES base URL.
3. **Authenticate and analyze repositories.** Users in your GHES organizations can now run Add Analysis Project → GitHub and follow the same authentication flow described for GitHub Enterprise Cloud above.

&#x20;

***

## FAQ <a href="#faq" id="faq"></a>

**Q: I already installed the CodeScan GitHub App on one GitHub organization (or personal account) through the CodeScan UI. How do I install it on another organization or personal account?**

**A: The CodeScan UI only walks you through the GitHub App installation for one account or organization at a time — whichever you select on the first install screen. If you need to add CodeScan to a different GitHub organization or personal account, you cannot do it from the CodeScan UI again. Instead, follow the steps in the section below ("How to Install the CodeScan GitHub App on Another GitHub Org or Personal Account") to install the app directly from GitHub using your install link.**

### How to Install the CodeScan GitHub App on Another GitHub Org or Personal Account <a href="#how-to-install-the-codescan-github-app-on-another-github-org-or-personal-account" id="how-to-install-the-codescan-github-app-on-another-github-org-or-personal-account"></a>

![3pic.png](https://media-cdn.atlassian.com/file/6a667b10-9821-4bf9-a358-a5d7e8fcac3c/image/cdn?allowAnimated=true\&client=edba5115-c6ab-4222-8129-1768e20983cf\&collection=contentId-2562687035\&height=125\&max-age=2592000\&mode=full-fit\&source=mediaCard\&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlZGJhNTExNS1jNmFiLTQyMjItODEyOS0xNzY4ZTIwOTgzY2YiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0yNTYyNjg3MDM1IjpbInJlYWQiXX0sImV4cCI6MTc3OTk1OTQ5MiwibmJmIjoxNzc5OTU2NjEyLCJhYUlkIjoiNjJjZmUyY2VjNTM3ZjQ2MGQ0NDViOWNlIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL2FwcEFjY3JlZGl0ZWQiOmZhbHNlLCJhdXRoVHlwZSI6InNlc3Npb24ifQ.xwGEegy7legoPuTjwKQQ3xbNWFeHh853OK4he94cSPE\&width=760#media-blob-url=true\&id=6a667b10-9821-4bf9-a358-a5d7e8fcac3c\&clientId=edba5115-c6ab-4222-8129-1768e20983cf\&contextId=contentId-2562687035\&collection=contentId-2562687035)

1. Step 1: Find Your Install Link

Take your CodeScan URL → replace every dot (.) with a dash (-) → put it after [https://github.com/apps/](https://github.com/apps/)

Examples:

| **CodeScan URL**                                                     | **GitHub App Install Link**                                                                                  |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [app.codescan.io](http://app.codescan.io/)                           | [https://github.com/apps/app-codescan-io](https://github.com/apps/app-codescan-io)                           |
| [app-eu.codescan.io](http://app-eu.codescan.io/)                     | [https://github.com/apps/app-eu-codescan-io](https://github.com/apps/app-eu-codescan-io)                     |
| [bank-codescan.autorabit.com](http://penfed-codescan.autorabit.com/) | [https://github.com/apps/bank-codescan-autorabit-com](https://github.com/apps/penfed-codescan-autorabit-com) |

2. Step 2: Open the Link
3. Choose the org / account for Installation
4. Step 3: Choose Repo Access

* **All repositories (recommended) — covers future repos automatically.**
* Only select repositories — you'll have to come back and add every new repo manually.

Pick All repositories if you want new repos to be scanned by CodeScan without extra work.

4. Step 4: Click Install

* Owner: The app installs right away. In CodeScan, click Add Analysis Project to begin scanning.
* Member (non-owner): GitHub will show that an installation request was submitted. See the steps below for approval.
* Ask your organization owner to approve via the email notification or manually at GitHub Org → Settings → GitHub Apps → Pending requests → Approve (set access to All repositories if desired), then retry Add Analysis Project.

5. Step 5: After Install — Verify

Go to GitHub → Settings → GitHub Apps → CodeScan → Configure and confirm your repositories are listed.\
Switch to All repositories to have CodeScan automatically include any new repositories you create later.
