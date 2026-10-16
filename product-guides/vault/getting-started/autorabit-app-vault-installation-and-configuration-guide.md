# AutoRABIT Vault - App Installation and Configuration Guide

Salesforce UI Compatibility Notice


The AutoRABIT package is a Second-Generation Managed Package (2GP) designed for Salesforce administrators to perform a one-time setup operation. It is supported exclusively in Salesforce Lightning Experience and is not compatible with Salesforce Classic.

Please ensure that your Salesforce org is using Lightning Experience before proceeding with the AutoRABIT package installation and configuration. Customers using Salesforce Classic must switch to Lightning Experience to complete the setup, as supporting Salesforce Classic is not technically feasible for this 2GP package.

{% hint style="info" %}
**PURPOSE:** This guide walks administrators through installing the AutoRABIT Salesforce package, configuring the Salesforce OAuth settings required by the connector, authorizing inbound and outbound connections, enabling licensed products, assigning the AutoRABIT Vault permission set, and completing product-side Salesforce org registration for AutoRABIT Vault.
{% endhint %}

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

In Setup, search for and open “Session Settings.” Under “Session Settings,” make sure both of the following are disabled in the org:

* Lock sessions to the IP address from which they originated
* Lock sessions to the domain in which they were first used

<figure><img src="../../../.gitbook/assets/image (3046).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../.gitbook/assets/image (3019).png" alt=""><figcaption><p><em>Figure 26. Configuration card in AutoRABIT Connector</em></p></figcaption></figure>

#### 3.  Authorize the inbound connection

The System Connections page contains two authorization areas. Start with Inbound Connection and click “Authorize.” The Salesforce user that completes this authorization becomes the AutoRABIT integration user for the connection.

<figure><img src="../../../.gitbook/assets/image (3020).png" alt=""><figcaption><p><em>Figure 27. Inbound Connection authorization in AutoRABIT Connector</em></p></figcaption></figure>

{% hint style="danger" %}
INTEGRATION USER REQUIREMENT If the currently signed-in Salesforce user is not the intended integration user, use the “Not you?” option on the Salesforce authorization screen and sign in as the correct user. The user completing this authorization must have the “AutoRABIT Setup User” permission set.
{% endhint %}

{% hint style="warning" %}
NON-ADMINISTRATOR PROFILE REQUIREMENT If the Salesforce user connecting the org to the AutoRABIT product is not a System Administrator, their profile must also include the following permissions: API Enabled, Modify Metadata Through Metadata API Functions, and Customize Application.
{% endhint %}

#### 4.  Allow access

Review the Salesforce authorization request for AutoRABIT Connector and click “Allow” when the displayed user is the intended integration user.

<figure><img src="../../../.gitbook/assets/image (3021).png" alt=""><figcaption><p><em>Figure 28. Salesforce “Allow Access?” authorization screen.</em></p></figcaption></figure>

&#x20;

## 7.  Configure and Authorize the Outbound Connection

After inbound authorization succeeds, complete the Outbound Connection. The connector requires three values from AutoRABIT Vault: Subdomain, Client ID, and Client Secret.

<figure><img src="../../../.gitbook/assets/image (3022).png" alt=""><figcaption><p><em>Figure 29. Outbound Connection fields in AutoRABIT Connector</em></p></figcaption></figure>

#### 1. Sign in to the AutoRABIT product

Open AutoRABIT Vault and sign in with your AutoRABIT account.

{% hint style="warning" %}
CREDENTIAL HANDLING Client Secret values are sensitive. Copy them only into the intended connector field and avoid placing them in tickets, chat messages, or documentation.
{% endhint %}

### 7.1  AutoRABIT Vault – Register a Salesforce Org

AutoRABIT Vault manages Salesforce org registration from a single Salesforce Orgs List page, whether this is the first org being registered or an additional one.

**1. Open Salesforce Orgs and click Register New Org**

In AutoRABIT Vault, go to Setup → Salesforce Orgs List, then click “+ Register New Org.” The Add New Org dialog opens, with a dropdown to select an already-authorized Salesforce org, a Salesforce Version selector, and an expandable “Authorize Org with AutoRABIT Connector” section.

<figure><img src="../../../.gitbook/assets/image (3023).png" alt=""><figcaption><p><em>Figure 30. Add New Org dialog in AutoRABIT Vault, with “Authorize Org with AutoRABIT Connector” collapse</em></p></figcaption></figure>

**2. Select an already-authorized org, if available**

If the org you want to add already appears in the “Select Salesforce ORGs” dropdown, choose it, confirm the “Salesforce Version” field matches your org's release, and skip to step 4.

**3. If the org isn’t listed, get the connector values from AutoRABIT Vault**

Click “Authorize Org with AutoRABIT Connector” to expand it. This reveals the Subdomain, Client ID, and Client Secret for the org you want to connect.

<figure><img src="../../../.gitbook/assets/image (3024).png" alt=""><figcaption><p><em>Figure 31. “Authorize Org with AutoRABIT Connector” panel showing the Subdomain, Client ID, and Client Secret to copy into Salesforce.</em></p></figcaption></figure>

**4. Enter those values in Salesforce and authorize**

Switch to the Salesforce tab with AutoRABIT Connector open (Configuration → System Connections → Outbound Connection, shown earlier in Section 7). Paste the Subdomain, Client ID, and Client Secret from AutoRABIT Vault into the matching fields, then click “Authorize.” Confirm the Outbound Connection changes to an authorized state before continuing.

<figure><img src="../../../.gitbook/assets/image (3025).png" alt=""><figcaption><p><em>Figure 32. Outbound Connection fields in Salesforce populated with the values copied from AutoRABIT Vault.</em></p></figcaption></figure>

## 8.  Enable Products and Assign Permissions

#### 1.  Open Products

After system connection registration is complete, close Configuration and open the “Products” card in AutoRABIT Connector.

<figure><img src="../../../.gitbook/assets/image (3026).png" alt=""><figcaption><p><em>Figure 33. Products card in AutoRABIT Connector</em></p></figcaption></figure>

#### 2.  Review product availability and toggles

For products with valid licenses, the connector displays an enable/disable toggle. Enabled products can see the registered Salesforce org in the related AutoRABIT application. If the toggle is off, that product cannot use the org in its configuration.

<figure><img src="../../../.gitbook/assets/image (3027).png" alt=""><figcaption><p><em>Figure 34. Example of a licensed product enabled with its toggle (a different AutoRABIT product is shown here as the illustrative example from the source procedure; AutoRABIT Vault's own toggle appears the same way when licensed).</em></p></figcaption></figure>

{% hint style="info" %}
DEFAULT BEHAVIOR After the org is registered, available licensed products are enabled by default in the flow shown. Turn off a product only when the org should not be exposed to that application.
{% endhint %}

#### 3.  Recognize products without a license

If there is no valid license for a product, the product page displays that no valid licenses are available instead of an active enablement toggle.

<figure><img src="../../../.gitbook/assets/image (3028).png" alt=""><figcaption><p><em>Figure 35. Example of a product with no valid licenses available (shown for a different product in the source procedure; this guide assumes AutoRABIT Vault itself is licensed).</em></p></figcaption></figure>

#### 4.  Open Licensing & Permissions

Return to the AutoRABIT Connector home page and click “Licensing & Permissions.”

<figure><img src="../../../.gitbook/assets/image (3029).png" alt=""><figcaption><p><em>Figure 36. Licensing &#x26; Permissions card.</em></p></figcaption></figure>

#### 5.  Assign the required permission sets

Review the listed AutoRABIT permission sets and assign the AutoRABIT Vault permission set to the authorized/integration user. The detailed steps for configuring this permission set are in section 8.1 below.

<figure><img src="../../../.gitbook/assets/image (3030).png" alt=""><figcaption><p><em>Figure 37. AutoRABIT permission sets available from Licensing &#x26; Permissions</em></p></figcaption></figure>

### 8.1  AutoRABIT Vault Permission Set

This section walks through configuring the AutoRABIT Vault permission set in Salesforce. Follow each step in order to grant the AutoRABIT Vault integration user the access it needs. The AutoRABIT Vault integration user requires View All Data, Modify All Data, Customize Application, and Query All Files to be enabled.

**1. Open Licensing & Permissions**

In Salesforce, open the AutoRABIT Connector app and click Licensing & Permissions.

<figure><img src="../../../.gitbook/assets/image (3031).png" alt=""><figcaption><p><em>Figure 38. AutoRABIT Connector home page, with Licensing &#x26; Permissions highlighted</em></p></figcaption></figure>

**2. Open Permission Sets**

Click Permission Sets.

<figure><img src="../../../.gitbook/assets/image (3032).png" alt=""><figcaption><p><em>Figure 39. Permission Sets option under Licensing &#x26; Permissions.</em></p></figcaption></figure>

**3. Select the AutoRABIT Vault Permission Set**

Click AutoRABIT Vault to open the permission set.

<figure><img src="../../../.gitbook/assets/image (3033).png" alt=""><figcaption><p><em>Figure 40. AutoRABIT Vault permission set in the Permission Sets list</em></p></figcaption></figure>

**4. Open System Permissions**

Click System Permissions. This section controls permissions to perform actions that apply across apps, such as “Modify All Data.”

<figure><img src="../../../.gitbook/assets/image (3034).png" alt=""><figcaption><p><em>Figure 41. System Permissions option on the AutoRABIT Vault permission set.</em></p></figcaption></figure>

**5. Enable editing**

Click Edit to make the permission list editable.

**6. Enable Customize Application**

Search for Customize Application and select its checkbox if it is not already selected.

<figure><img src="../../../.gitbook/assets/image (3035).png" alt=""><figcaption><p><em>Figure 42. Searching for and enabling Customize Application.</em></p></figcaption></figure>

**7. Enable View All Data**

Search for View All Data and select its checkbox if it is not already selected.

<figure><img src="../../../.gitbook/assets/image (3036).png" alt=""><figcaption><p><em>Figure 43. Searching for and enabling View All Data.</em></p></figcaption></figure>

**8. Enable Modify All Data**

Search for Modify All Data and select its checkbox if it is not already selected.

<figure><img src="../../../.gitbook/assets/image (3037).png" alt=""><figcaption><p><em>Figure 44. Searching for and enabling Modify All Data</em></p></figcaption></figure>

**9. Enable Query All Files**

Search for Query All Files and select its checkbox if it is not already selected.

<figure><img src="../../../.gitbook/assets/image (3038).png" alt=""><figcaption><p align="center"><em>Figure 45. Searching for and enabling Query All Files.</em></p></figcaption></figure>

**10.    Save the permission set**

After selecting all the required checkboxes, click Save at the top of the page.

**11.    Confirm the save**

In the Save Changes confirmation dialog box, click Save again to apply the changes. Depending on how the checkboxes were selected, this may appear as two separate confirmations: one covering Query All Files, and another covering View All Data, Modify All Data, and Customize Application.

<figure><img src="../../../.gitbook/assets/image (3039).png" alt=""><figcaption><p><em>Figure 46. Save Changes confirmation dialog covering the Query All Files permission</em></p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3040).png" alt=""><figcaption><p><em>Figure 47. Save Changes confirmation dialog covering View All Data, Modify All Data, and Customize Application.</em></p></figcaption></figure>

{% hint style="info" %}
ALTERNATIVE: OBJECT-BY-OBJECT PERMISSIONS If you do not want to grant all View All Data and Modify All Data permissions at once, you can go back to step 4 and, instead of System Permissions, open Object Settings. From there, grant the required permissions object by object, based on your specific needs.
{% endhint %}

{% hint style="info" %}
**NOTE** : Unlike ARM and Guard, the AutoRABIT Vault permission set does not require the Manage Users permission. AutoRABIT Vault's integration user instead requires an additional permission not needed by the other products: Query All Files, alongside View All Data, Modify All Data, and Customize Application.
{% endhint %}

## 9.  Complete Salesforce Org Registration in AutoRABIT Vault

After the Salesforce-side registration and permissions are complete, return to the same Add New Org dialog in AutoRABIT Vault to finish linking the org.

#### 1.  Refresh and select the newly authorized Salesforce org

If the org isn’t already shown, click “Refresh” next to “Select Salesforce ORGs.” Confirm the “Salesforce Version” field, then choose the newly authorized org from the dropdown.

<figure><img src="../../../.gitbook/assets/image (3041).png" alt=""><figcaption><p><em>Figure 48. “Select Salesforce ORGs” dropdown in AutoRABIT Vault, showing Salesforce orgs available to select.</em></p></figcaption></figure>

#### 2.  Add the org

With the correct org selected, click “Add Org” to complete the registration.

#### 3.  Confirm the org was added

The newly registered org now appears in the Salesforce Orgs List.

<figure><img src="../../../.gitbook/assets/image (3042).png" alt=""><figcaption><p><em>Figure 49. Salesforce Orgs List in AutoRABIT Vault, showing the newly registered org.</em></p></figcaption></figure>

{% hint style="info" %}
CROSS-PRODUCT BEHAVIOR Once the Salesforce org has been configured for one AutoRABIT product, any other AutoRABIT application that has a valid license and is enabled for the org should display that org without repeating the connector configuration steps.
{% endhint %}

## 10.  Completion Checklist

Before handing the configuration over for use, verify each item below.

* AutoRABIT package installation completed successfully in the intended Salesforce org.
* Required OAuth settings are enabled in Salesforce Setup.
* “Lock sessions to the IP address from which they originated” is disabled in Session Settings.
* AutoRABIT Connector OAuth Policy is saved with Code and Credentials Flow for Guest Users enabled.
* The standard “AutoRABIT Connector” ECA is selected; “AutoRABIT Connector (Dev)” is not used for normal configuration.
* &#x20;Inbound Connection is authorized with the intended integration user.
* The integration user has the AutoRABIT Setup User permission set.
* Outbound Connection contains the correct Subdomain, Client ID, and Client Secret and shows as authorized.
* AutoRABIT Vault is enabled in the Products area.
* The AutoRABIT Vault permission set is configured and assigned to the authorized user.
* The Salesforce org appears in AutoRABIT Vault after Refresh.
* The org was successfully added to the AutoRABIT Vault product configuration.

{% hint style="warning" %}
IF SOMETHING DOES NOT APPEAR Recheck the package installation status, OAuth settings, connector authorization state, product license availability, the product enablement toggle, and the permission sets assigned to the integration user. The product-side org list may also need to be refreshed after Salesforce-side changes.
{% endhint %}
