---
hidden: true
noIndex: true
---

# AutoRABIT Vault App Installation and Configuration Guide

**PURPOSE:** This guide walks administrators through installing the AutoRABIT Salesforce package, configuring the Salesforce OAuth settings required by the connector, authorizing inbound and outbound connections, enabling licensed products, assigning the AutoRABIT Vault permission set, and completing product-side Salesforce org registration for AutoRABIT Vault.

### Process at a Glance

<table><thead><tr><th valign="top">1 Install</th><th valign="top">2 Configure Salesforce</th><th valign="top">3 Authorize Connector</th><th valign="top">4 Register Org</th></tr></thead><tbody><tr><td valign="top">AppExchange / AgentExchange</td><td valign="top">OAuth &#x26; External Client App</td><td valign="top">Inbound + outbound</td><td valign="top">Product visibility + permissions</td></tr></tbody></table>

## 1.  Before You Begin

Confirm the target Salesforce environment and the user accounts that will be used before starting the installation. This avoids installing into the wrong org or authorizing the connector with an unintended user.

* Choose the installation target: Production/Developer Org or Sandbox.
* Use a Salesforce account with sufficient access to install the package and update Setup settings.
* Identify the Salesforce user that will act as the AutoRABIT integration user.
* Before inbound authorization, make sure the integration user has the AutoRABIT Setup User permission set.
* Confirm that the customer has a valid AutoRABIT Vault license enabled.

{% hint style="warning" %}
**ENVIRONMENT CHOICE** The AppExchange flow is different for Production/Developer organizations and Sandboxes. Follow only the path that matches the org you are configuring.
{% endhint %}

## 2.  Locate the AutoRABIT Package

#### 1.  Open Salesforce AppExchange / AgentExchange

Open the Salesforce marketplace in a browser. Sign in if prompted.

<figure><img src="../../../.gitbook/assets/image (2993).png" alt=""><figcaption><p align="center"><em>Figure 1. Salesforce AppExchange / AgentExchange landing page.</em></p></figcaption></figure>

#### 2.  Search for AutoRABIT

Use the marketplace search field and search for “AutoRABIT.”

<figure><img src="../../../.gitbook/assets/image (2994).png" alt=""><figcaption><p><em>Figure 2. Searching the marketplace for AutoRABIT.</em></p></figcaption></figure>

#### 3.  Open the AutoRABIT listing

Select the AutoRABIT Salesforce DevOps Platform listing from the search results.<br>

<figure><img src="../../../.gitbook/assets/image (2995).png" alt=""><figcaption><p><em>Figure 3. AutoRABIT listing in the marketplace search results.</em></p></figcaption></figure>

## 3.  Install in a Production or Developer Org

#### 1.  Select Get It Now

From the AutoRABIT listing, choose “Get It Now” to begin the production/developer installation flow.

<figure><img src="../../../.gitbook/assets/image (2996).png" alt=""><figcaption><p><em>Figure 4. “Get It Now” on the AutoRABIT listing.</em></p></figcaption></figure>

#### 2.  Authenticate to Salesforce

Log in with the Salesforce credentials associated with the target Production/Developer org.

<figure><img src="../../../.gitbook/assets/image (2997).png" alt=""><figcaption><p>Figure 5. Salesforce sign-in prompt launched from the marketplace.</p></figcaption></figure>

#### 3.  Use the correct Salesforce or business identity

If Salesforce requests account identification, use the Salesforce or business email tied to the intended org.

<figure><img src="../../../.gitbook/assets/image (2998).png" alt=""><figcaption><p>Figure 6. Salesforce account identification screen.</p></figcaption></figure>

#### 4.  Select the target org

Choose the Production/Developer organization where the package should be installed. Verify the org before proceeding.

<figure><img src="../../../.gitbook/assets/image (2999).png" alt=""><figcaption><p>Figure 7. Selecting the Production/Developer organization.</p></figcaption></figure>

#### 5.  Accept the marketplace terms and confirm installation

Review the installation details, accept the Salesforce AppExchange terms and conditions, and select “Confirm and Install.” Salesforce then redirects you to the package installation page in the selected org.

<figure><img src="../../../.gitbook/assets/image (3000).png" alt=""><figcaption><p><em>Figure 8. Confirm Installation Details and “Confirm and Install.”</em></p></figcaption></figure>

## 4.  Install in a Sandbox

#### 1.  Select Try It

For a Sandbox installation, use the “Try It” option on the AutoRABIT listing instead of “Get It Now.”

<figure><img src="../../../.gitbook/assets/image (3001).png" alt=""><figcaption><p>Figure 9. “Try It” option for the Sandbox installation path.</p></figcaption></figure>

#### 2.  Continue to installation

On the trial setup page, confirm the information shown and select “Continue to Installation.”

<figure><img src="../../../.gitbook/assets/image (3002).png" alt=""><figcaption><p align="center"><em>Figure 10. Sandbox trial setup and “Continue to Installation.”</em></p></figcaption></figure>

#### 3.  Log in and install

Select “Log In & Install,” then authenticate to the Sandbox in which the package will be installed.

<figure><img src="../../../.gitbook/assets/image (3003).png" alt=""><figcaption><p>Figure 11. “Log In &#x26; Install” for the Sandbox installation.</p></figcaption></figure>

#### 4.  Install for Admins Only

When the Salesforce package installation screen opens, select “Install for Admins Only,” then click “Install.” This is the installation scope shown in the source procedure.

<figure><img src="../../../.gitbook/assets/image (3004).png" alt=""><figcaption><p>Figure 12. Package installation scope set to “Install for Admins Only.”</p></figcaption></figure>

#### 5.  Approve required third-party access

Salesforce may request approval for access to login.salesforce.com and test.salesforce.com. Select the option to grant access to these third-party sites, then click “Continue.”

<figure><img src="../../../.gitbook/assets/image (3005).png" alt=""><figcaption><p><em>Figure 13. Approve Third-Party Access prompt.</em></p></figcaption></figure>

{% hint style="info" %}
**WHY THIS IS REQUIRED** The package requires these Salesforce endpoints so the AutoRABIT applications can complete the authentication and connectivity flow shown in this procedure.
{% endhint %}

#### 6.  Wait for package installation to complete

Do not begin post-install configuration until Salesforce confirms the package has finished installing.

<figure><img src="../../../.gitbook/assets/image (3006).png" alt=""><figcaption><p>Figure 14. Salesforce package installation in progress.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3007).png" alt=""><figcaption><p><em>Figure 15. Salesforce may send an email if the package installation takes longer than expected.</em></p></figcaption></figure>

{% hint style="warning" %}
LONG-RUNNING INSTALLATION If Salesforce reports that the package is taking a long time to install, wait for either the completion screen or the Salesforce completion email before continuing.
{% endhint %}

## 5. Configure Salesforce OAuth and External Client App Settings

After the package is installed, configure the Salesforce OAuth settings required by the AutoRABIT Connector.

#### 1.  Open OAuth and OpenID Connect Settings

In Salesforce Setup, search for and open “OAuth and OpenID Connect Settings.”

<figure><img src="../../../.gitbook/assets/image (3008).png" alt=""><figcaption><p><em>Figure 16. Salesforce Setup navigation to OAuth and OpenID Connect Settings.</em></p></figcaption></figure>

#### 2.  Enable the required OAuth settings

Verify that both of the following settings are enabled. If either is disabled, enable it:

* Allow Authorization Code and Credentials Flows
* Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows

<figure><img src="../../../.gitbook/assets/image (3009).png" alt=""><figcaption><p align="center"><em>Figure 17. Required OAuth settings in Salesforce Setup.</em></p></figcaption></figure>

#### 3.  Confirm the Salesforce warning

When Salesforce displays a warning about changing the setting, review it and click “OK” to continue.

<figure><img src="../../../.gitbook/assets/image (3010).png" alt=""><figcaption><p><em>Figure 18. Salesforce confirmation dialog when changing OAuth settings.</em></p></figcaption></figure>

#### 4.  Confirm Session Settings

In Setup, search for and open “Session Settings.” Under “Session Settings,” make sure “Lock sessions to the IP address from which they originated” is disabled in the org.

<figure><img src="../../../.gitbook/assets/image (3011).png" alt=""><figcaption><p><em>Figure 19. Session Settings: “Lock sessions to the IP address from which they originated” disabled.</em></p></figcaption></figure>

#### 5.  Open External Client App Manager

From Setup, open “External Client App Manager.”

<figure><img src="../../../.gitbook/assets/image (3013).png" alt=""><figcaption><p><em>Figure 20. External Client App Manager in Salesforce Setup.</em></p></figcaption></figure>

#### 6.  Open AutoRABIT Connector

Select only the external client app named “AutoRABIT Connector.” Do not select “AutoRABIT Connector (Dev).” The (Dev) External Client App (ECA) is reserved for debugging and troubleshooting purposes and must not be used for the standard AutoRABIT installation and configuration process.

<figure><img src="../../../.gitbook/assets/image (3014).png" alt=""><figcaption><p><em>Figure 21. Select the standard “AutoRABIT Connector” entry. Do not use “AutoRABIT Connector (Dev).”</em></p></figcaption></figure>

#### 7.  Edit Policies

On the AutoRABIT Connector page, open the Policies tab and click “Edit.”

<figure><img src="../../../.gitbook/assets/image (3015).png" alt=""><figcaption><p><em>Figure 22. Edit action on the AutoRABIT Connector Policies page.</em></p></figcaption></figure>

#### 8.  Expand OAuth Policies and enable guest-user credential flow

Expand “OAuth Policies,” enable “Enable Code and Credentials Flow for Guest Users,” and then save the changes.

<figure><img src="../../../.gitbook/assets/image (3016).png" alt=""><figcaption><p align="center"><em>Figure 23. OAuth Policies section before enabling the option.</em></p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3017).png" alt=""><figcaption><p><em>Figure 24. “Enable Code and Credentials Flow for Guest Users” enabled</em></p></figcaption></figure>

## 6. Open the AutoRABIT Connector and Authorize the Inbound Connection

#### 1.  Launch AutoRABIT Connector

Open the Salesforce App Launcher, search for “AutoRABIT Connector,” and launch the app.

<figure><img src="../../../.gitbook/assets/image (3018).png" alt=""><figcaption><p><em>Figure 25. AutoRABIT Connector in the Salesforce App Launcher.</em></p></figcaption></figure>

#### 2.  Open Configuration

From the AutoRABIT Connector home page, click the “Configuration” card.



