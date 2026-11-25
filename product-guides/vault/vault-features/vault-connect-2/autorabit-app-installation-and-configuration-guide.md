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

<p align="center"></p>

<p align="center"><em>Figure 1. Salesforce AppExchange / AgentExchange landing page.</em></p>

2\. Search for AutoRABIT

Use the marketplace search field and search for “AutoRABIT”.

<p align="center"></p>

<p align="center"><em>Figure 2. Searching the marketplace for AutoRABIT.</em></p>

3\. Open the AutoRABIT listing

Select the AutoRABIT Salesforce DevOps Platform listing from the search results.

<p align="center"></p>

<p align="center"><em>Figure 3. AutoRABIT listing in the marketplace search results.</em></p>

## 3. Install in a Production or Developer Org

1\. Select Get It Now

From the AutoRABIT listing, choose “Get It Now” to begin the production/developer installation flow.

<p align="center"></p>

<p align="center"><em>Figure 4. “Get It Now” on the AutoRABIT listing.</em></p>

2\. Authenticate to Salesforce

Log in with the Salesforce credentials associated with the target Production/Developer org.

<p align="center"></p>

<p align="center"><em>Figure 5. Salesforce sign-in prompt launched from the marketplace.</em></p>

3\. Use the correct Salesforce or business identity

If Salesforce requests account identification, use the Salesforce or business email tied to the intended org.

<p align="center"></p>

<p align="center"><em>Figure 6. Salesforce account identification screen.</em></p>

4\. Select the target org

Choose the Production/Developer organization where the package should be installed. Verify the org before proceeding.

<p align="center"></p>

<p align="center"><em>Figure 7. Selecting the Production/Developer organization.</em></p>

5\. Accept the marketplace terms and confirm installation

Review the installation details, accept the Salesforce AppExchange terms and conditions, and select “Confirm and Install”. Salesforce then redirects you to the package installation page in the selected org.

<p align="center"></p>

<p align="center"><em>Figure 8. Confirm Installation Details and “Confirm and Install”.</em></p>

## 4. Install in a Sandbox

1\. Select Try It

For a Sandbox installation, use the “Try It” option on the AutoRABIT listing instead of “Get It Now”.

<p align="center"></p>

<p align="center"><em>Figure 9. “Try It” option for the Sandbox installation path.</em></p>

2\. Continue to installation

On the trial setup page, confirm the information shown and select “Continue to Installation”.

<p align="center"></p>

<p align="center"><em>Figure 10. Sandbox trial setup and “Continue to Installation”.</em></p>

3\. Log in and install

Select “Log In & Install”, then authenticate to the Sandbox in which the package will be installed.

<p align="center"></p>

<p align="center"><em>Figure 11. “Log In &#x26; Install” for the Sandbox installation.</em></p>

4\. Install for Admins Only

When the Salesforce package installation screen opens, select “Install for Admins Only”, then click “Install”. This is the installation scope shown in the source procedure.

<p align="center"></p>

<p align="center"><em>Figure 12. Package installation scope set to “Install for Admins Only”.</em></p>

5\. Approve required third-party access

Salesforce may request approval for access to login.salesforce.com and test.salesforce.com. Select the option to grant access to these third-party sites, then click “Continue”.

<p align="center"></p>

<p align="center"><em>Figure 13. Approve Third-Party Access prompt.</em></p>

WHY THIS IS REQUIRED The package requires these Salesforce endpoints so the AutoRABIT applications can complete the authentication and connectivity flow shown in this procedure.

6\. Wait for package installation to complete

Do not begin post-install configuration until Salesforce confirms the package has finished installing.

<p align="center"></p>

<p align="center"><em>Figure 14. Salesforce package installation in progress.</em></p>

<p align="center"></p>

<p align="center"><em>Figure 15. Salesforce may send an email if the package installation takes longer than expected.</em></p>

LONG-RUNNING INSTALLATION If Salesforce reports that the package is taking a long time to install, wait for either the completion screen or the Salesforce completion email before continuing.

## 5. Configure Salesforce OAuth and External Client App Settings
