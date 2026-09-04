# AutoRABIT App Installation and Configuration Guide



{% hint style="info" %}
This guide is intended for the Salesforce administrator responsible for installing and configuring AutoRABIT in your organization. It walks you through package installation, required Salesforce OAuth settings, AutoRABIT Connector authorization, product enablement, permission assignment, and final Salesforce org registration in your licensed AutoRABIT products.&#x20;
{% endhint %}

## Process at a Glance

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Step 1:  Install</td><td valign="top">Step 2:  Configure Salesforce</td><td valign="top">Step 3:  Authorize Connector</td><td valign="top">Step 4:  Register Org</td></tr><tr><td valign="top">AppExchange / AgentExchange</td><td valign="top">OAuth &#x26; External Client App</td><td valign="top">Inbound + outbound</td><td valign="top">Product visibility + permissions</td></tr></tbody></table>

## Before You Begin

Before you begin, confirm which Salesforce org you are configuring and which Salesforce account will be used as the AutoRABIT integration user. Completing these checks first helps prevent installing the package in the wrong environment or authorizing the connector with the wrong account.

·   Choose the installation target: Production/Developer Org or Sandbox.

·   Use a Salesforce account with sufficient access to install the package and update Setup settings.

·   Identify the Salesforce user that will act as the AutoRABIT integration user.

·   Before inbound authorization, make sure the integration user has the AutoRABIT Setup User permission set.

·   Confirm that your organization has active licenses for the AutoRABIT products you plan to connect.

{% hint style="info" %}
**Environment choice**

The AppExchange flow is different for Production/Developer organizations and Sandboxes. Follow only the path that matches the org you are configuring.
{% endhint %}

## Locate the AutoRABIT Package

1\. Open Salesforce AppExchange / AgentExchange

Open the Salesforce marketplace in a browser. Sign in if prompted.

<figure><img src="../../../.gitbook/assets/image (2809).png" alt=""><figcaption></figcaption></figure>

2\. Search for AutoRABIT

Use the marketplace search field and search for “AutoRABIT”.

<figure><img src="../../../.gitbook/assets/image (2810).png" alt=""><figcaption></figcaption></figure>

3\. Open the AutoRABIT listing

Select the AutoRABIT Salesforce DevOps Platform listing from the search results.

<figure><img src="../../../.gitbook/assets/image (2811).png" alt=""><figcaption></figcaption></figure>

## Install in a Production or Developer Org

1\. Select Get It Now

From the AutoRABIT listing, choose “Get It Now” to begin the production/developer installation flow.

<figure><img src="../../../.gitbook/assets/image (2812).png" alt=""><figcaption></figcaption></figure>

2\. Authenticate to Salesforce

Log in with the Salesforce credentials associated with your target Production/Developer org.

<figure><img src="../../../.gitbook/assets/image (2813).png" alt=""><figcaption></figcaption></figure>

3\. Use the correct Salesforce or business identity

If Salesforce requests account identification, use the Salesforce or business email tied to the intended org.

<figure><img src="../../../.gitbook/assets/image (2814).png" alt=""><figcaption></figcaption></figure>

4\. Select the target org

Choose the Production/Developer organization where you want the package installed. Verify the org before proceeding.

<figure><img src="../../../.gitbook/assets/image (2815).png" alt=""><figcaption></figcaption></figure>

5\. Accept the marketplace terms and confirm installation

Review the installation details, accept the Salesforce AppExchange terms and conditions, and select “Confirm and Install”. Salesforce then redirects you to the package installation page in the selected org.

<figure><img src="../../../.gitbook/assets/image (2816).png" alt=""><figcaption></figcaption></figure>

## Install in a Sandbox

1\. Select Try It

For a Sandbox installation, use the “Try It” option on the AutoRABIT listing instead of “Get It Now”.

<figure><img src="../../../.gitbook/assets/image (2817).png" alt=""><figcaption></figcaption></figure>

2\. Continue to installation

On the trial setup page, confirm the information shown and select “Continue to Installation”.

<figure><img src="../../../.gitbook/assets/image (2818).png" alt=""><figcaption></figcaption></figure>

3\. Log in and install

Select “Log In & Install”, then authenticate to the Sandbox in which the package will be installed.

<figure><img src="../../../.gitbook/assets/image (2819).png" alt=""><figcaption></figcaption></figure>

4\. Install for Admins Only

When the Salesforce package installation screen opens, select “Install for Admins Only”, then click “Install”. This is the installation scope shown in the source procedure.

<figure><img src="../../../.gitbook/assets/image (2820).png" alt=""><figcaption></figcaption></figure>

5\. Approve required third-party access

Salesforce may request approval for access to login.salesforce.com and test.salesforce.com. Select the option to grant access to these third-party sites, then click “Continue”.

<figure><img src="../../../.gitbook/assets/image (2821).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Why this is required**

The package requires these Salesforce endpoints so your AutoRABIT applications can complete the authentication and connectivity flow shown in this procedure.
{% endhint %}

6\. Wait for package installation to complete

Do not begin post-install configuration until Salesforce confirms the package has finished installing.

<figure><img src="../../../.gitbook/assets/image (2822).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2823).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;**Long-running installation**

If Salesforce reports that the package is taking a long time to install, wait for either the completion screen or the Salesforce completion email before continuing.
{% endhint %}

## Configure Salesforce OAuth and External Client Settings

After the package is installed, configure the Salesforce OAuth settings required by the AutoRABIT Connector.

1\. Open OAuth and OpenID Connect Settings

In Salesforce Setup, search for and open “OAuth and OpenID Connect Settings”.

<figure><img src="../../../.gitbook/assets/image (2824).png" alt=""><figcaption></figcaption></figure>

2\. Enable the required OAuth settings

Verify that both of the following settings are enabled. If either is disabled, enable it:

·   Allow Authorization Code and Credentials Flows

·   Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows

<figure><img src="../../../.gitbook/assets/image (2825).png" alt=""><figcaption></figcaption></figure>

3\. Confirm the Salesforce warning

When Salesforce displays a warning about changing the setting, review it and click “OK” to continue with the configuration.

<figure><img src="../../../.gitbook/assets/image (2826).png" alt=""><figcaption></figcaption></figure>

4\. Open External Client App Manager

From Setup, open “External Client App Manager”.

<figure><img src="../../../.gitbook/assets/image (2827).png" alt=""><figcaption></figcaption></figure>

5\. Select AutoRABIT Connector

In External Client App Manager, select only the entry named “AutoRABIT Connector”. Do not select “AutoRABIT Connector (Dev)”. The (Dev) External Client App is reserved for AutoRABIT debugging and troubleshooting and is not part of the standard customer configuration.

<figure><img src="../../../.gitbook/assets/image (2828).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Connector selection**

Choose AutoRABIT Connector without “(Dev)”. AutoRABIT Connector (Dev) is for debugging purposes only and should not be configured by customer administrators during a normal installation.
{% endhint %}

6\. Edit Policies

On the AutoRABIT Connector page, open the Policies tab and click “Edit”.

<figure><img src="../../../.gitbook/assets/image (2829).png" alt=""><figcaption></figcaption></figure>

7\. Expand OAuth Policies and enable guest-user credential flow

Expand “OAuth Policies”, enable “Enable Code and Credentials Flow for Guest Users”, and then save the changes.

<figure><img src="../../../.gitbook/assets/image (2830).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2831).png" alt=""><figcaption></figcaption></figure>

## Open the AutoRABIT Connector and Authorize the Inbound Connection

1\. Launch AutoRABIT Connector

Open the Salesforce App Launcher, search for “AutoRABIT Connector”, and launch the app.

<figure><img src="../../../.gitbook/assets/image (2832).png" alt=""><figcaption></figcaption></figure>

2\. Open Configuration

From the AutoRABIT Connector home page, click the “Configuration” card.

<figure><img src="../../../.gitbook/assets/image (2833).png" alt=""><figcaption></figcaption></figure>

3\. Authorize the inbound connection

The System Connections page contains two authorization areas. Start with Inbound Connection and click “Authorize”. The Salesforce account that completes this authorization becomes the integration user AutoRABIT uses for this connection. Use a dedicated integration account when that is your standard practice.

<figure><img src="../../../.gitbook/assets/image (2834).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;**Integration User requirement**

If you are currently signed in as a different Salesforce user than the intended integration user, use the “Not you?” option on the Salesforce authorization screen and sign in as the correct user. The account completing this authorization must have the “AutoRABIT Setup User” permission set assigned before you continue.
{% endhint %}

4\. Allow access

Review the Salesforce authorization request carefully. Confirm the displayed Salesforce account is the integration user you intend to use, then click “Allow”.

<figure><img src="../../../.gitbook/assets/image (2835).png" alt="" width="267"><figcaption></figcaption></figure>

## Configure and Authorize the Outbound Connection

After the inbound connection is authorized successfully, configure the Outbound Connection. The connector requires three values from the applicable AutoRABIT product: Subdomain, Client ID, and Client Secret.

<figure><img src="../../../.gitbook/assets/image (2836).png" alt=""><figcaption></figcaption></figure>

1\. Sign in to the AutoRABIT product

Open the AutoRABIT product your organization is licensed to use and sign in with your AutoRABIT account.

<figure><img src="../../../.gitbook/assets/image (2837).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Credential handling**

Client Secret values are sensitive. Copy them only into the intended connector field and avoid placing them in tickets, chat messages, or documentation.
{% endhint %}

## Guard - first-time configuration

1\. Open the Guard onboarding flow

If this is the first time the product is being configured, the Guard welcome screen is displayed. Click “Get Started”.

<figure><img src="../../../.gitbook/assets/image (2838).png" alt=""><figcaption></figcaption></figure>

2\. Open the Salesforce org authorization details

Guard displays the information needed to authorize the org with AutoRABIT Connector.

<figure><img src="../../../.gitbook/assets/image (2839).png" alt=""><figcaption></figcaption></figure>

3\. Copy the three connector values into Salesforce

Return to AutoRABIT Connector in Salesforce and populate the Outbound Connection fields as follows:

·   Subdomain: copy the subdomain shown by the AutoRABIT product.

·   Client ID: copy the Client ID shown by the product.

·   Client Secret: copy the Client Secret shown by the product.

<figure><img src="../../../.gitbook/assets/image (2840).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2841).png" alt=""><figcaption></figcaption></figure>

4\. Authorize the outbound connection

After all three values are entered, click “Authorize”. Confirm that the outbound connection changes to an authorized state before moving on.

## Guard - adding another org later

1\. Open Salesforce Orgs

If Guard has already been configured previously, use the left navigation and open “Salesforce Orgs”.

<figure><img src="../../../.gitbook/assets/image (2842).png" alt=""><figcaption></figcaption></figure>

2\. Click Add New Org

On the Salesforce Orgs page, select “Add New Org”.

<figure><img src="../../../.gitbook/assets/image (2843).png" alt=""><figcaption></figcaption></figure>

3\. Copy the connector values

The Add New Org dialog displays the Subdomain, Client ID, and Client Secret. Copy these values into the corresponding Outbound Connection fields in Salesforce AutoRABIT Connector.

<figure><img src="../../../.gitbook/assets/image (2844).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2845).png" alt=""><figcaption></figcaption></figure>

4\. Authorize

Click “Authorize” in AutoRABIT Connector to complete the outbound connection.

{% hint style="info" %}
**Other Products**

The source procedure names CodeScan, Vault, and ARM as additional product paths but does not include separate screenshots for retrieving their connector values. Use the product-specific location that exposes the same Subdomain, Client ID, and Client Secret required by the Outbound Connection.
{% endhint %}

## Enable Products and Assign Permissions

1\. Open Products

After both system connections are authorized, close Configuration and open the “Products” card in AutoRABIT Connector.

<figure><img src="../../../.gitbook/assets/image (2846).png" alt=""><figcaption></figcaption></figure>

2\. Review product availability and toggles

For products your organization is licensed to use, the connector displays an enable/disable toggle. Enabled products can see the registered Salesforce org in the related AutoRABIT application. If the toggle is off, that product cannot use the org in its configuration.

<figure><img src="../../../.gitbook/assets/image (2847).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;**Default behavior**

After the org is registered, available licensed products are enabled by default in the flow shown. Turn off a product only when the org should not be exposed to that application.
{% endhint %}

3\. Recognize products without licenses

If your organization does not have an active license for a product, the product page displays that no valid licenses are available instead of an active enablement toggle.

<figure><img src="../../../.gitbook/assets/image (2848).png" alt=""><figcaption></figcaption></figure>

4\. Open Licensing & Permissions

Return to the AutoRABIT Connector home page and click “Licensing & Permissions”.

<figure><img src="../../../.gitbook/assets/image (2849).png" alt=""><figcaption></figcaption></figure>

5\. Assign the required permission sets

Review the listed AutoRABIT permission sets and assign the correct permissions to the authorized/integration user based on the products that will be used.

<figure><img src="../../../.gitbook/assets/image (2850).png" alt=""><figcaption></figcaption></figure>

## Complete Salesforce Org Registration in the AutoRABIT Product

1\. Refresh the product-side org list

After the Salesforce-side registration and permissions are complete, return to the AutoRABIT product and click “Refresh” in the Add New Org dialog.

<figure><img src="../../../.gitbook/assets/image (2851).png" alt=""><figcaption></figcaption></figure>

2\. Select the newly authorized Salesforce org

The newly registered Salesforce org should appear in the selection list. Choose it to create the product configuration.

<figure><img src="../../../.gitbook/assets/image (2852).png" alt=""><figcaption></figcaption></figure>

3\. Add the org

With the correct org selected, click “Add Org”.

<figure><img src="../../../.gitbook/assets/image (2853).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Cross-product behavior**

Once the Salesforce org has been configured for one AutoRABIT product, any other AutoRABIT product that your organization is licensed for and has enabled should display the same Salesforce org without repeating the connector configuration steps.
{% endhint %}

## Completion Checklist

Before you begin using the integration, verify each item below.

☐ AutoRABIT package installation completed successfully in the intended Salesforce org.

☐ Required OAuth settings are enabled in Salesforce Setup.

☐ The standard AutoRABIT Connector (without “Dev”) was selected in External Client App Manager.

☐ AutoRABIT Connector OAuth Policy is saved with Code and Credentials Flow for Guest Users enabled.

☐ Inbound Connection is authorized with the intended integration user.

☐ The integration user has the AutoRABIT Setup User permission set.

☐ Outbound Connection contains the correct Subdomain, Client ID, and Client Secret and shows as authorized.

☐ Required licensed products are enabled in the Products area.

☐ Required product permission sets are assigned to the authorized user.

☐ The Salesforce org appears in the AutoRABIT product after Refresh.

☐ The org was successfully added to the intended product configuration.

{% hint style="info" %}
**If something is missing**

Recheck the package installation status, OAuth settings, connector authorization state, product license availability, product enablement toggle, and permission sets assigned to the integration user. Refresh the product-side org list after Salesforce-side changes.&#x20;

If the configuration still does not complete, capture the screen or error message and contact AutoRABIT Support.
{% endhint %}
