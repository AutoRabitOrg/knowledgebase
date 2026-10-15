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
