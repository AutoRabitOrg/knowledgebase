---
description: Salesforce Package Installation • OAuth Setup • Connector Registration • Vault
hidden: true
---

# AutoRABIT App Installation and Configuration Guide

{% hint style="info" %}
SALESFORCE UI COMPATIBILITY NOTICE The Autorabit package is a Second-Generation Managed Package (2GP) designed for Salesforce administrators to perform a one-time setup operation. It is supported exclusively in Salesforce Lightning Experience and is not compatible with Salesforce Classic. Please ensure that your Salesforce org is using Lightning Experience before proceeding with the Autorabit package installation and configuration. Customers using Salesforce Classic must switch to Lightning Experience to complete the setup, as supporting Salesforce Classic is not technically feasible for this 2GP package.
{% endhint %}

**PURPOSE** This guide walks administrators through installing the AutoRABIT Salesforce package, configuring the Salesforce OAuth settings required by the connector, authorizing inbound and outbound connections, enabling licensed products, assigning the AutoRABIT Vault permission set, and completing product-side Salesforce org registration for Vault.

Process at a Glance

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">1  Install</td><td valign="top">2  Configure Salesforce</td><td valign="top">3  Authorize Connector</td><td valign="top">4  Register Org</td></tr><tr><td valign="top">AppExchange / AgentExchange</td><td valign="top">OAuth &#x26; External Client App</td><td valign="top">Inbound + outbound</td><td valign="top">Product visibility + permissions</td></tr></tbody></table>

&#x20;

## 1. Before You Begin

Confirm the target Salesforce environment and the user accounts that will be used before starting the installation. This avoids installing into the wrong org or authorizing the connector with an unintended user.

●      Choose the installation target: Production/Developer Org or Sandbox.

●      Use a Salesforce account with sufficient access to install the package and update Setup settings.

●      Identify the Salesforce user that will act as the AutoRABIT integration user.

●      Decide which authentication flow you will use for the inbound connection (Client Credentials, Authorization Code and Credentials, or JWT Bearer) — this determines whether the integration user needs the AutoRABIT Setup User permission set or just their existing Profile added to Selected Profiles.

●      Confirm that the customer has a valid Vault license enabled.

ENVIRONMENT CHOICE The AppExchange flow is different for Production/Developer organizations and Sandboxes. Follow only the path that matches the org you are configuring.

## 2. Locate the AutoRABIT Package

1\. Open Salesforce AppExchange / AgentExchange

Open the Salesforce marketplace in a browser. Sign in if prompted.

<figure><img src="/broken/files/jImgXE3LB00ayfeW7cZ5" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce AppExchange / AgentExchange landing page.</em></p>

2\. Search for AutoRABIT

Use the marketplace search field and search for “AutoRABIT”.

<figure><img src="../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Searching the marketplace for AutoRABIT.</em></p>

3\. Open the AutoRABIT listing

Select the AutoRABIT Salesforce DevOps Platform listing from the search results.

<figure><img src="../../../../.gitbook/assets/image (171).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>AutoRABIT listing in the marketplace search results.</em></p>

## 3. Install in a Production or Developer Org

1\. Select Get It Now

From the AutoRABIT listing, choose “Get It Now” to begin the production/developer installation flow.

<figure><img src="../../../../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>“Get It Now” on the AutoRABIT listing.</em></p>

2\. Authenticate to Salesforce

Log in with the Salesforce credentials associated with the target Production/Developer org.

<figure><img src="../../../../.gitbook/assets/image (173).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce sign-in prompt launched from the marketplace.</em></p>

3\. Use the correct Salesforce or business identity

If Salesforce requests account identification, use the Salesforce or business email tied to the intended org.

<figure><img src="../../../../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce account identification screen.</em></p>

4\. Select the target org

Choose the Production/Developer organization where the package should be installed. Verify the org before proceeding.

<figure><img src="../../../../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Selecting the Production/Developer organization.</em></p>

5\. Accept the marketplace terms and confirm installation

Review the installation details, accept the Salesforce AppExchange terms and conditions, and select “Confirm and Install”. Salesforce then redirects you to the package installation page in the selected org.

<figure><img src="../../../../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Confirm Installation Details and “Confirm and Install”.</em></p>

## 4. Install in a Sandbox

1\. Select Try It

For a Sandbox installation, use the “Try It” option on the AutoRABIT listing instead of “Get It Now”.

<figure><img src="../../../../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>“Try It” option for the Sandbox installation path.</em></p>

2\. Continue to installation

On the trial setup page, confirm the information shown and select “Continue to Installation”.

<figure><img src="../../../../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Sandbox trial setup and “Continue to Installation”.</em></p>

3\. Log in and install

Select “Log In & Install”, then authenticate to the Sandbox in which the package will be installed.

<figure><img src="../../../../.gitbook/assets/image (181).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>“Log In &#x26; Install” for the Sandbox installation.</em></p>

4\. Install for Admins Only

When the Salesforce package installation screen opens, select “Install for Admins Only”, then click “Install”. This is the installation scope shown in the source procedure.

<figure><img src="../../../../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Package installation scope set to “Install for Admins Only”.</em></p>

5\. Approve required third-party access

Salesforce may request approval for access to login.salesforce.com and test.salesforce.com. Select the option to grant access to these third-party sites, then click “Continue”.

<figure><img src="../../../../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Approve Third-Party Access prompt.</em></p>

{% hint style="info" %}
**WHY THIS IS REQUIRED** The package requires these Salesforce endpoints so the AutoRABIT applications can complete the authentication and connectivity flow shown in this procedure.
{% endhint %}

6\. Wait for package installation to complete

Do not begin post-install configuration until Salesforce confirms the package has finished installing.

<figure><img src="../../../../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Figure 14. Salesforce package installation in progress.</em></p>

<figure><img src="../../../../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

<p align="center">              <em>Salesforce may send an email if the package installation takes longer than expected.</em></p>

{% hint style="info" %}
LONG-RUNNING INSTALLATION If Salesforce reports that the package is taking a long time to install, wait for either the completion screen or the Salesforce completion email before continuing.
{% endhint %}

## 5. Configure Salesforce OAuth and External Client App Settings

After the package is installed, configure the Salesforce OAuth settings required by the AutoRABIT Connector.

1\. Open OAuth and OpenID Connect Settings

In Salesforce Setup, search for and open “OAuth and OpenID Connect Settings”.

<figure><img src="../../../../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce Setup navigation to OAuth and OpenID Connect Settings.</em></p>

2\. Enable the required OAuth settings

Verify that both of the following settings are enabled. If either is disabled, enable it:

●      Allow Authorization Code and Credentials Flows

●      Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows

<figure><img src="../../../../.gitbook/assets/image (205).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Required OAuth settings in Salesforce Setup.</em></p>

3\. Confirm the Salesforce warning

When Salesforce displays a warning about changing the setting, review it and click “OK” to continue.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce confirmation dialog when changing OAuth settings.</em></p>

4\. Confirm Session Settings

In Setup, search for and open “Session Settings”. Under “Session Settings”, make sure both of the following are disabled in the org:

●      Lock sessions to the IP address from which they originated

●      Lock sessions to the domain in which they were first used

<figure><img src="../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Session Settings: both “Lock sessions to the IP address from which they originated” and “Lock sessions to the domain in which they were first used” disabled.</em></p>

{% hint style="info" %}
**WHY THIS IS REQUIRED** Leaving either setting enabled can cause the AutoRABIT Connector's authorization or ongoing API calls to be rejected if Salesforce detects a change in originating IP address or domain, since the integration doesn't always run from a single fixed location.
{% endhint %}

## 6. Configure and Authorize the Outbound Connection

Before you can select and authorize an inbound connection flow (Section 7), complete the Outbound Connection. The connector requires three values from Vault: Subdomain, Client ID, and Client Secret.

1\. Open Configuration

From the AutoRABIT Connector home page, click the “Configuration” card, then open “System Connections”. The Outbound Connection fields are shown first — the Inbound Connection section and the flow selection stay locked until the Outbound Connection is authorized.

<figure><img src="../../../../.gitbook/assets/image (233).png" alt=""><figcaption></figcaption></figure>

<p align="center">         <em>System Connections with the Outbound Connection fields blank and the Inbound Connection section locked.</em></p>

2\. Sign in to the AutoRABIT product

Open Vault and sign in with your AutoRABIT account.

{% hint style="info" %}
**CREDENTIAL HANDLING** Client Secret values are sensitive. Copy them only into the intended connector field and avoid placing them in tickets, chat messages, or documentation.
{% endhint %}

6.1 Vault – Register a Salesforce Org

Vault manages Salesforce org registration from a single Salesforce Orgs List page, whether this is the first org being registered or an additional one.

1\. Open Salesforce Orgs and click Register New Org

In Vault, go to Setup → Salesforce Orgs List, then click “+ Register New Org”. The Add New Org dialog opens, with a dropdown to select an already-authorized Salesforce org, a Salesforce Version selector, and an expandable “Authorize Org with AutoRABIT Connector” section.

<figure><img src="../../../../.gitbook/assets/image (239).png" alt=""><figcaption></figcaption></figure>

<p align="center">          <em>Add New Org dialog in AutoRABIT Vault, with “Authorize Org with AutoRABIT Connector” collapsed.</em></p>

2\. Select an already-authorized org, if available

If the org you want to add already appears in the “Select Salesforce ORGs” dropdown, choose it, confirm the “Salesforce Version” field matches your org's release, and skip to step 4.

3\. If the org isn’t listed, get the connector values from Vault

Click “Authorize Org with AutoRABIT Connector” to expand it. This reveals the Subdomain, Client ID, and Client Secret for the org you want to connect.

<figure><img src="../../../../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

<p align="center">             <em>“Authorize Org with AutoRABIT Connector” panel showing the Subdomain, Client ID, and Client Secret to copy into Salesforce.</em></p>

4\. Enter those values in Salesforce and authorize

Switch to the Salesforce tab with AutoRABIT Connector open (Configuration → System Connections → Outbound Connection, shown earlier in Section 6). Paste the Subdomain, Client ID, and Client Secret from Vault into the matching fields, then click “Authorize”. Confirm the Outbound Connection changes to an authorized state before continuing.

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

<p align="center">    <em>Outbound Connection fields in Salesforce populated with the values copied from Vault.</em></p>

{% hint style="info" %}
OUTBOUND CONNECTION COMPLETE With the Outbound Connection authorized, continue to Section 7 to select and authorize your inbound connection flow.
{% endhint %}

## 7. Choose an Authentication Flow and Authorize the Inbound Connection

AutoRABIT Connector supports three ways to authorize the inbound connection between AutoRABIT and Salesforce: Client Credentials Flow, Authorization Code and Credentials Flow, and JWT Bearer Flow — listed here in the same left-to-right order they appear in System Connections. The flow toggles below only become available once the Outbound Connection (Section 6) is authorized. Complete the steps below to select a flow, then follow only the subsection for the flow you chose.

1\. Choose a connection flow

With the Outbound Connection authorized, open “System Connections” if it isn’t already. Under “Select the connection flow to use with this org,” toggle on the flow you want to use. Only one flow can be active at a time, and the Inbound Connection section changes to match the flow you select.

<figure><img src="../../../../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

<p align="center">       <em>System Connections with the Outbound Connection authorized and no authentication flow selected yet.</em></p>

{% hint style="info" %}
CHOOSING A FLOW

**Client Credentials Flow** — a non-interactive, application-level flow. AutoRABIT authenticates using a pre-configured integration user with no sign-in prompt. Review the security note in that section below before using it.

**Authorization Code and Credentials Flow** — the default, interactive flow. A real Salesforce user signs in and approves access. Best when a person will complete setup and authorization should be tied to that person's login.

**JWT Bearer Flow** — a non-interactive flow where AutoRABIT authenticates as a specific Salesforce user you choose, using a signed token instead of a login screen.
{% endhint %}

2\. Open External Client App Manager

From Setup, open “External Client App Manager”. The External Client App (ECA) itself — selecting the right entry, editing its policies, and enabling the correct flow — is configured per authentication flow in the subsections below.

<figure><img src="../../../../.gitbook/assets/image (320).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>External Client App Manager in Salesforce Setup.</em></p>

7.1  Client Credentials Flow

Use this flow only when you specifically need a non-interactive, application-level connection. Read the security note below before enabling it.

{% hint style="info" %}
WHERE DO THE CLIENT ID AND CLIENT SECRET COME FROM? These values are entered in the Outbound Connection, completed in Section 6 above. Refer to Section 6 if you still need to obtain and enter them before continuing here.
{% endhint %}

1\. Enable the flow on the External Client App

In Setup, open External Client App Manager and select the standard “AutoRABIT Connector” entry (not “AutoRABIT Connector (Dev)”).

<figure><img src="../../../../.gitbook/assets/image (322).png" alt=""><figcaption></figcaption></figure>

<p align="center">       <em>Select the standard “AutoRABIT Connector” entry. Do not use “AutoRABIT Connector (Dev)”.</em></p>

2\. Open OAuth Policies and locate Client Credentials Flow

Open the Policies tab, click Edit, expand “OAuth Policies”, and scroll to “OAuth Flows and External Client App Enhancements”. Before you check anything, both flow checkboxes are off.

<figure><img src="../../../../.gitbook/assets/image (325).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>“OAuth Flows and External Client App Enhancements” before Client Credentials Flow is enabled.</em></p>

3\. Check Enable Client Credentials Flow and set the Run As user

Check “Enable Client Credentials Flow”. A “Run As (Username)” field appears below it — enter the username of the Salesforce user whose permissions this connection should use.

<figure><img src="../../../../.gitbook/assets/image (326).png" alt=""><figcaption></figcaption></figure>

<p align="center">    <em>“Enable Client Credentials Flow” checked, with a Run As (Username) value entered.</em></p>

{% hint style="info" %}
SECURITY CONSIDERATION Client Credentials Flow uses application-level credentials with no interactive login or MFA challenge for each token request. Any access granted through this flow is tied entirely to the permissions of the Run As user, so choose that user carefully and confirm this trade-off is acceptable for your org before enabling it, especially in production.
{% endhint %}

4\. Save

Click “Save” and confirm the success message before moving on.

<figure><img src="../../../../.gitbook/assets/image (327).png" alt=""><figcaption></figcaption></figure>

<p align="center">            <em>External client app saved with Client Credentials Flow enabled and a Run As user configured.</em></p>

5\. Turn on the flow in System Connections

Return to the AutoRABIT Connector app, open Configuration → System Connections, and toggle “Client Credentials Flow” on.

<figure><img src="../../../../.gitbook/assets/image (328).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Client Credentials Flow selected in System Connections.</em></p>

6\. Accept and authorize

Check “I understand that Client Credentials uses application-level credentials without interactive user authentication for each token request, and accept the associated security considerations,” then click “Authorize”. Because this flow is non-interactive, the connection is authorized immediately with no sign-in prompt.

<figure><img src="../../../../.gitbook/assets/image (331).png" alt=""><figcaption></figcaption></figure>

&#x20;                                   _Inbound connection authorized under Client Credentials Flow._

7.2  Authorization Code and Credentials Flow

This is the flow most orgs already use, and matches the default behavior of the AutoRABIT Connector. Before you can turn this flow on in System Connections, the AutoRABIT Connector External Client App (ECA) must have Guest User access enabled. Complete the ECA setup steps below first, then continue to the System Connections steps that follow.

{% hint style="info" %}
WHERE DO THE CLIENT ID AND CLIENT SECRET COME FROM? These values are entered in the Outbound Connection, completed in Section 6 above. Refer to Section 6 if you still need to obtain and enter them before continuing here.
{% endhint %}

1\. Open the AutoRABIT Connector External Client App

In Setup, open External Client App Manager, select the standard “AutoRABIT Connector” entry (not “AutoRABIT Connector (Dev)”), open the Policies tab, and click “Edit”.

<figure><img src="../../../../.gitbook/assets/image (346).png" alt=""><figcaption></figcaption></figure>

<p align="center">        <em>Select the standard “AutoRABIT Connector” entry. Do not use “AutoRABIT Connector (Dev)”.</em></p>

2\. Enable Code and Credentials Flow for Guest Users

Expand “OAuth Policies” and scroll to “OAuth Flows and External Client App Enhancements.” Check “Enable Code and Credentials Flow for Guest Users.” Leave “Enable Client Credentials Flow” unchecked — this app's Selected Permission Sets and Permitted Users (set to “Admin approved users are pre-authorized”) are already correct and do not need to change for this flow.

<figure><img src="../../../../.gitbook/assets/image (358).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>“Enable Code and Credentials Flow for Guest Users” unchecked, before it is enabled.</em></p>

<figure><img src="../../../../.gitbook/assets/image (362).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>“Enable Code and Credentials Flow for Guest Users” checked.</em></p>

3\. Save

Click “Save” on the External Client App policies page and confirm the success message before moving on.

<figure><img src="../../../../.gitbook/assets/image (424).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>External client app saved with Code and Credentials Flow for Guest Users enabled.</em></p>

4\. Select the flow

Return to the AutoRABIT Connector app and open Configuration → System Connections. Toggle “Authorization Code and Credentials Flow” on. The Inbound Connection section shows a single “Authorize” button.

<figure><img src="../../../../.gitbook/assets/image (428).png" alt=""><figcaption></figcaption></figure>

<p align="center">         <em>Authorization Code and Credentials Flow selected, inbound connection not yet authorized.</em></p>

5\. Authorize and sign in

Click “Authorize”. Salesforce opens the familiar “Allow Access?” consent screen. Review the requested permissions and the signed-in user shown, then click “Allow”.

<figure><img src="../../../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Salesforce “Allow Access?” authorization screen.</em></p>

{% hint style="info" %}
<mark style="color:$warning;">**INTEGRATION USER REQUIREMENT**</mark> <mark style="color:$warning;background-color:orange;">I</mark><mark style="color:$warning;background-color:orange;">f the currently signed-in Salesforce user is not the intended integration user, use the “Not you?” option on the authorization screen and sign in as the correct user. The user completing this authorization must have the “AutoRABIT Setup User” permission set.</mark>
{% endhint %}

6\. Confirm the connection

After you click Allow, Salesforce returns you to System Connections and Inbound Connection shows “Authorized as: \<username>” with Deauthorize and Re-authorize options.

<figure><img src="../../../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Inbound connection authorized under Authorization Code and Credentials Flow.</em></p>

7.3  JWT Bearer Flow

JWT Bearer Flow authorizes AutoRABIT to act as a specific Salesforce user without an interactive sign-in. Before you can turn this flow on in System Connections, the AutoRABIT Connector External Client App (ECA) itself must be configured to permit it. Complete the ECA setup steps below first, then continue to the System Connections steps that follow.

{% hint style="info" %}
<mark style="color:blue;">**WHERE DO THE CLIENT ID AND CLIENT SECRET COME FROM?**</mark> These values are entered in the Outbound Connection, completed in Section 6 above. Refer to Section 6 if you still need to obtain and enter them before continuing here.
{% endhint %}

{% hint style="info" %}
<mark style="color:red;">**PREREQUISITE**</mark> Before continuing, identify the Salesforce user you intend to use as the integration user for this connection — the user AutoRABIT will authenticate as under this flow. You will need to know that user's Profile before configuring the External Client App below, and you will use that same username later when completing Inbound Connection.
{% endhint %}

1\. Create a Remote Site Setting for the AutoRABIT product

JWT Bearer Flow requires Salesforce to allow an outbound callout to the AutoRABIT product’s domain before the flow can be used. Client Credentials Flow and Authorization Code and Credentials Flow do not need this step — complete it only when you are setting up JWT Bearer Flow, before the steps below.

In Salesforce Setup, use the Quick Find box to search for “Remote Site Settings,” open it, and click “New Remote Site”.

<figure><img src="../../../../.gitbook/assets/image (442).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Quick Find box in Salesforce Setup showing “Remote Site Settings.”</em></p>

<figure><img src="../../../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Blank “New Remote Site” page.</em></p>

Enter a Remote Site Name of your choosing (for example, “AUTHUB”) and a Remote Site URL built from three parts: the prefix https://, the AutoRABIT product’s Subdomain, and the suffix .autorabit.com — for example, https://{subdomain}.autorabit.com.

The Subdomain portion of that URL is the same Subdomain value shown on Vault’s “Add New Org” / “Register New Org” screen (see Section 6 above, where this same value was copied into the Outbound Connection fields).

<figure><img src="../../../../.gitbook/assets/image (457).png" alt=""><figcaption></figcaption></figure>

<p align="center">       <em>Vault’s Subdomain value, also used earlier to populate the Outbound Connection in Section 6.</em></p>

<figure><img src="../../../../.gitbook/assets/image (477).png" alt=""><figcaption></figcaption></figure>

<p align="center">   <em>Remote Site Name and Remote Site URL entered, ready to save.</em></p>

Click “Save”.

<figure><img src="../../../../.gitbook/assets/image (503).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Remote Site Setting saved.</em></p>

{% hint style="info" %}
<mark style="color:blue;">REMOTE SITE SETTING COMPLETE</mark> With the Remote Site Setting saved, Salesforce will allow the outbound callout to the AutoRABIT product’s domain needed for JWT Bearer Flow. Continue with the External Client App configuration below.
{% endhint %}

2\. Open the AutoRABIT Connector External Client App

In Setup, open External Client App Manager, select the standard “AutoRABIT Connector” entry (not “AutoRABIT Connector (Dev)”), open the Policies tab, and click “Edit”.

<figure><img src="../../../../.gitbook/assets/image (504).png" alt=""><figcaption></figcaption></figure>

<p align="center">       <em>Select the standard “AutoRABIT Connector” entry. Do not use “AutoRABIT Connector (Dev)”.</em></p>

3\. Review the current OAuth Policies state

Expand “OAuth Policies.” If you configured Client Credentials Flow earlier (see 7.1), “Enable Client Credentials Flow” is still checked here and “Permitted Users” is still set to “All users can self-authorize.” The steps below update both of these for JWT Bearer Flow.

<figure><img src="../../../../.gitbook/assets/image (505).png" alt=""><figcaption></figcaption></figure>

<p align="center">         <em>Current OAuth Policies state before JWT Bearer Flow setup: Client Credentials Flow still enabled, Permitted Users dropdown open.</em></p>

4\. Confirm Permitted Users under Plugin Policies

Under “Plugin Policies,” set “Permitted Users” to “Admin approved users are pre-authorized.”

<figure><img src="../../../../.gitbook/assets/image (506).png" alt=""><figcaption></figcaption></figure>

<p align="center">      <em>Plugin Policies with Permitted Users set to “Admin approved users are pre-authorized,” shown here before the OAuth flow checkboxes below are disabled.</em></p>

5\. Confirm the integration user's Profile

Before selecting anything on the External Client App's policies page, confirm which Profile is assigned to the Salesforce user you intend to authenticate as under this flow. In Setup, open Users, open that user's detail page, and note the value in the Profile field. You will select this same profile in the next step.

<figure><img src="../../../../.gitbook/assets/image (507).png" alt=""><figcaption></figcaption></figure>

<p align="center">     <em>Salesforce user detail page confirming the integration user's Profile — here, “TEST Team” has the “Standard User” profile.</em></p>

6\. Move that Profile into Selected Profiles

Under “App Policies,” find “Select Profiles.” In the Available Profiles list, select the profile you confirmed for the integration user in the previous step (“Standard User” in this example) and move it into Selected Profiles. Leave “Select Permission Sets” empty — no permission set needs to be assigned on this page for JWT Bearer Flow.

<figure><img src="../../../../.gitbook/assets/image (529).png" alt=""><figcaption></figcaption></figure>

<p align="center">    <em>Select Profiles: the integration user's profile selected in Available Profiles, ready to move. Select Permission Sets is left empty.</em></p>

<figure><img src="../../../../.gitbook/assets/image (532).png" alt=""><figcaption></figcaption></figure>

<p align="center">  <em>The profile moved into Selected Profiles. Select Permission Sets remains empty.</em></p>

{% hint style="info" %}
<mark style="color:blue;">**WHY PROFILES, NOT A PERMISSION SET JWT**</mark> Bearer Flow authenticates as a specific Salesforce user and relies on that user's own Profile and permissions. Adding the integration user's Profile to Selected Profiles is what authorizes the External Client App to act on behalf of that user; no separate permission set assignment is required on this page for this flow.
{% endhint %}

7\. Disable the other OAuth flows for this app

Still under “OAuth Policies,” scroll to “OAuth Flows and External Client App Enhancements.” Make sure “Enable Client Credentials Flow” is unchecked, and uncheck “Enable Code and Credentials Flow for Guest Users” if it is turned on. Both checkboxes must be off before you save, so that JWT Bearer Flow is the only inbound flow this External Client App allows.

<figure><img src="../../../../.gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

<p align="center">    <em>“Enable Client Credentials Flow” and “Enable Code and Credentials Flow for Guest Users” both unchecked. (Cropped to the OAuth Flows section; Select Profiles/Select Permission Sets are unchanged from the previous step.)</em></p>

{% hint style="info" %}
WHY THIS MATTERS Leaving another flow enabled on the External Client App alongside JWT Bearer Flow widens how this app can be authorized beyond the single pre-authorized user you intend. Disabling the other flows keeps JWT Bearer Flow as the only way this app can be used for the inbound connection.
{% endhint %}

8\. Save

Click “Save” on the External Client App policies page and confirm the success message before moving on.

<figure><img src="../../../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<p align="center">     <em>External Client App saved with Permitted Users and flow settings in place. (Cropped to the OAuth Flows section; Select Profiles is unchanged from the previous step.)</em></p>

9\. Select the flow in System Connections

Return to the AutoRABIT Connector app and open Configuration → System Connections. Toggle “JWT Bearer Flow” on. The Inbound Connection section asks for a Salesforce username instead of showing a consent screen.

10\. Choose the Salesforce user

In the Username field, search for and select the SAME Salesforce user whose Profile you added to Selected Profiles in step 6.

<figure><img src="../../../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

<p align="center">  <em>Searching for and selecting the integration user under JWT Bearer Flow — the same user (“TEST Team”) whose profile was added to Selected Profiles.</em></p>

{% hint style="info" %}
<mark style="color:blue;">ABOUT THIS FLOW JWT</mark> Bearer Flow lets AutoRABIT authenticate as the selected Salesforce user without an interactive login, using a signed token in place of a username/password prompt or an OAuth consent screen. AutoRABIT Connector manages the certificate and key pair used to sign these tokens, so no separate certificate upload is required on this screen.
{% endhint %}

11\. Authorize

Click “Authorize”. The connection is established immediately, using the selected user's permissions.

<figure><img src="../../../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Inbound connection authorized under JWT Bearer Flow.</em></p>

{% hint style="info" %}
<mark style="color:$warning;">NON-ADMINISTRATOR PROFILE REQUIREMENT</mark> If the Salesforce user connecting the org to the AutoRABIT product is not a System Administrator, their profile must also include the following permissions: API Enabled, Modify Metadata Through Metadata API Functions, and Customize Application. This applies regardless of which authentication flow above you used.
{% endhint %}

## 8. Enable Products and Assign Permissions

1\. Open Products

After system connection registration is complete, close Configuration and open the “Products” card in AutoRABIT Connector.

<figure><img src="../../../../.gitbook/assets/image (569).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Products card in AutoRABIT Connector.</em></p>

2\. Review product availability and toggles

For products with valid licenses, the connector displays an enable/disable toggle. Enabled products can see the registered Salesforce org in the related AutoRABIT application. If the toggle is off, that product cannot use the org in its configuration.

<figure><img src="../../../../.gitbook/assets/image (571).png" alt=""><figcaption></figcaption></figure>

<p align="center">     <em>Example of a licensed product enabled with its toggle (a different AutoRABIT product is shown here as the illustrative example from the source procedure; Vault's own toggle appears the same way when licensed).</em></p>

{% hint style="info" %}
**DEFAULT BEHAVIOR** After the org is registered, available licensed products are enabled by default in the flow shown. Turn off a product only when the org should not be exposed to that application.
{% endhint %}

3\. Recognize products without a license

If there is no valid license for a product, the product page displays that no valid licenses are available instead of an active enablement toggle.

<figure><img src="../../../../.gitbook/assets/image (599).png" alt=""><figcaption></figcaption></figure>

<p align="center">      <em>Example of a product with no valid licenses available (shown for a different product in the source procedure; this guide assumes Vault itself is licensed).</em></p>

4\. Open Licensing & Permissions

Return to the AutoRABIT Connector home page and click “Licensing & Permissions”.

<figure><img src="../../../../.gitbook/assets/image (601).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Licensing &#x26; Permissions card.</em></p>

5\. Deploy the product permission sets

Click “Permission Sets” under Licensing & Permissions. Only the base permission sets may be listed at first — if the permission set for your product isn’t shown yet, click “Deploy Permission Sets” in the top right.

<figure><img src="../../../../.gitbook/assets/image (602).png" alt=""><figcaption></figcaption></figure>

<p align="center">        <em>Permission Sets tab under Licensing &#x26; Permissions, with “Deploy Permission Sets” highlighted. Only the base permission sets are listed before deployment.</em></p>

Salesforce confirms that the deployment has started. This deploys the permission sets for every licensed AutoRABIT product (ARM, CodeScan, Guard, and Vault) to this org — it can take a few minutes to complete.

<figure><img src="../../../../.gitbook/assets/image (603).png" alt=""><figcaption></figcaption></figure>

<p align="center">          <em>Confirmation that permission set deployment has started, after clicking “Deploy Permission Sets”.</em></p>

{% hint style="info" %}
WAIT FOR DEPLOYMENT TO FINISH Give the deployment a few minutes, then refresh the Permission Sets page before continuing. The permission set for your product isn’t available to assign until the deployment completes.
{% endhint %}

6\. Assign the required permission sets

Review the listed AutoRABIT permission sets and assign the AutoRABIT Vault permission set to the authorized/integration user. The detailed steps for configuring this permission set are in section 8.1 below.

<figure><img src="../../../../.gitbook/assets/image (604).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>AutoRABIT permission sets available from Licensing &#x26; Permissions.</em></p>

8.1 AutoRABIT Vault Permission Set

This section walks through configuring the AutoRABIT Vault permission set in Salesforce. Follow each step in order to grant the AutoRABIT Vault integration user the access it needs. The AutoRABIT Vault integration user requires View All Data, Modify All Data, Customize Application, and Query All Files to be enabled.

1\. Open Licensing & Permissions

In Salesforce, open the AutoRABIT Connector app and click Licensing & Permissions.

<figure><img src="../../../../.gitbook/assets/image (611).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>AutoRABIT Connector home page, with Licensing &#x26; Permissions highlighted.</em></p>

2\. Open Permission Sets

Click Permission Sets.

<figure><img src="../../../../.gitbook/assets/image (612).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Permission Sets option under Licensing &#x26; Permissions.</em></p>

3\. Select the AutoRABIT Vault Permission Set

Click AutoRABIT Vault to open the permission set.

<figure><img src="../../../../.gitbook/assets/image (613).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>AutoRABIT Vault permission set in the Permission Sets list.</em></p>

4\. Open System Permissions

Click System Permissions. This section controls permissions to perform actions that apply across apps, such as “Modify All Data.”

<figure><img src="../../../../.gitbook/assets/image (614).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>System Permissions option on the AutoRABIT Vault permission set.</em></p>

5\. Enable editing

Click Edit to make the permission list editable.

6\. Enable Customize Application

Search for Customize Application and select its checkbox if it is not already selected.

<figure><img src="../../../../.gitbook/assets/image (616).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Searching for and enabling Customize Application.</em></p>

7\. Enable View All Data

Search for View All Data and select its checkbox if it is not already selected.

<figure><img src="../../../../.gitbook/assets/image (617).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Searching for and enabling View All Data.</em></p>

8\. Enable Modify All Data

Search for Modify All Data and select its checkbox if it is not already selected.

<figure><img src="../../../../.gitbook/assets/image (618).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Searching for and enabling Modify All Data.</em></p>

9\. Save the permission set

After selecting all three checkboxes, click Save at the top of the page.

10\. Confirm the save

In the Save Changes confirmation dialog box, click Save again to apply the changes. This confirms View All Data, Modify All Data, and Customize Application under System Permissions.

<figure><img src="../../../../.gitbook/assets/image (619).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Save Changes confirmation dialog covering View All Data, Modify All Data, and Customize Application, under System Permissions.</em></p>

11\. Open App Permissions

Query All Files is listed on a separate page from the three permissions above. Click “Permission Set Overview” at the top of the page, then select App Permissions from the dropdown, under Apps.

<figure><img src="../../../../.gitbook/assets/image (620).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Permission Set Overview dropdown, with App Permissions highlighted under Apps.</em></p>

12\. Enable editing

Click Edit to make the permission list editable.

13\. Enable Query All Files

Search for Query All Files and select its checkbox if it is not already selected. It is listed under the Content category.

<figure><img src="../../../../.gitbook/assets/image (626).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>Searching for and enabling Query All Files, under App Permissions.</em></p>

14\. Save the permission set

Click Save at the top of the page.

15\. Confirm the save

In the Save Changes confirmation dialog box, click Save again to apply the changes. This confirms Query All Files under App Permissions.

<figure><img src="../../../../.gitbook/assets/image (627).png" alt=""><figcaption></figcaption></figure>

<p align="center">         <em>Save Changes confirmation dialog covering the Query All Files permission, under App Permissions.</em></p>

{% hint style="info" %}
<mark style="color:blue;">**ALTERNATIVE: OBJECT-BY-OBJECT PERMISSIONS**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">If you do not want to grant all View All Data and Modify All Data permissions at once, you can go back to step 4 and, instead of System Permissions, open Object Settings. From there, grant the required permissions object by object, based on your specific needs.</mark>

<mark style="color:blue;">NOTE Unlike ARM and Guard, the AutoRABIT Vault permission set does not require the Manage Users permission. Vault's integration user instead requires an additional permission not needed by the other products: Query All Files, alongside View All Data, Modify All Data, and Customize Application. Query All Files is configured separately because Salesforce lists it under App Permissions rather than System Permissions.</mark>
{% endhint %}

## 9. Complete Salesforce Org Registration in Vault

After the Salesforce-side registration and permissions are complete, return to the same Add New Org dialog in Vault to finish linking the org.

1\. Refresh and select the newly authorized Salesforce org

If the org isn’t already shown, click “Refresh” next to “Select Salesforce ORGs”. Confirm the “Salesforce Version” field, then choose the newly authorized org from the dropdown.

<figure><img src="../../../../.gitbook/assets/image (643).png" alt=""><figcaption></figcaption></figure>

<p align="center"> <em>“Select Salesforce ORGs” dropdown in Vault, showing Salesforce orgs available to select.</em></p>

2\. Add the org

With the correct org selected, click “Add Org” to complete the registration.

3\. Confirm the org was added

The newly registered org now appears in the Salesforce Orgs List.

<figure><img src="../../../../.gitbook/assets/image (644).png" alt=""><figcaption></figcaption></figure>

<p align="center"><em>Salesforce Orgs List in AutoRABIT Vault, showing the newly registered org.</em></p>

{% hint style="info" %}
<mark style="color:blue;">**CROSS-PRODUCT BEHAVIOR**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">Once the Salesforce org has been configured for one AutoRABIT product, any other AutoRABIT application that has a valid license and is enabled for the org should display that org without repeating the connector configuration steps.</mark>
{% endhint %}

## 10. Completion Checklist

Before handing the configuration over for use, verify each item below.

☐ AutoRABIT package installation completed successfully in the intended Salesforce org.

☐ Required OAuth settings are enabled in Salesforce Setup.

☐ “Lock sessions to the IP address from which they originated” and “Lock sessions to the domain in which they were first used” are both disabled in Session Settings.

☐ The standard “AutoRABIT Connector” ECA is selected; “AutoRABIT Connector (Dev)” is not used for normal configuration.

☐ An inbound connection flow has been chosen (Client Credentials, Authorization Code and Credentials, or JWT Bearer) and shows as authorized in System Connections.

☐ For Client Credentials or Authorization Code and Credentials Flow: the integration user has the AutoRABIT Setup User permission set. For JWT Bearer Flow: the integration user's Profile has been added to the External Client App's Selected Profiles.

☐ Outbound Connection contains the correct Subdomain, Client ID, and Client Secret and shows as authorized.

☐ Vault is enabled in the Products area.

☐ The AutoRABIT Vault permission set is configured and assigned to the authorized user.

☐ The Salesforce org appears in Vault after Refresh.

☐ The org was successfully added to the Vault product configuration.

{% hint style="info" %}
<mark style="color:yellow;">**IF SOMETHING DOES NOT APPEAR**</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">Recheck the package installation status, OAuth settings, connector authorization state, product license availability, the product enablement toggle, and the permission sets assigned to the integration user. The product-side org list may also need to be refreshed after Salesforce-side changes.</mark>
{% endhint %}
