
# ALM Management

{% hint style="info" %}
**Important Note:** The actions described here are available **only to Org Administrators**. General users cannot access ALM Management.
{% endhint %}

## Why Integrate an ALM? <a href="#overview" id="overview"></a>

AutoRABIT can connect to popular **Application Lifecycle Management (ALM)** platforms—Jira, Azure DevOps, IBM RTC, CA Agile Central (Rally), and VersionOne—to:

* Surface active and inactive sprints in one place.  
* Sync work-item status automatically during merges, commits, and CI jobs.  
* Enforce release governance with smart-commit patterns and webhook automation.

The **ALM Management** page (added in ARM 21.6) lives under **Admin** and lets you register new ALM connections, set integration rules, and manage repository mappings.

---

## Register an ALM <a href="#registering-an-alm" id="registering-an-alm"></a>

1. Log in to ARM as an administrator.  
2. Navigate to **Admin › ALM Mgmt**.  
3. Click **Register ALM**.

   <figure><img src="../../../.gitbook/assets/image (739).png" alt="Register ALM button on the ALM Mgmt screen"></figure>

4. Fill the form:

   ### IBM RTC, CA Agile Central, VersionOne, or Azure DevOps

   <figure><img src="../../../.gitbook/assets/image (740).png" alt="ALM registration form for Azure DevOps" width="414"></figure>

   * **ALM Name** – friendly label.  
   * **ALM Type** – choose the platform.  
   * **ALM URL** – base server URL.  
   * **Credentials** – select stored credentials (see [Credential Manager](../troubleshoot/how-tos/create-users-credentials.md)).

   ### Jira

   <figure><img src="../../../.gitbook/assets/image (742).png" alt="Jira registration with Standard and OAuth access types" width="414"></figure>

   * **ALM Name** – friendly label.  
   * **ALM Type** – *Jira*.  
   * **Access Type** –  
     * **Standard** – enter **ALM URL** and credentials.  
     * **OAuth** – pick **OAuth**, click **Validate & Save**, and grant access in the Jira pop-up.

   {% hint style="info" %}
   * Jira **OAuth** is supported for **Cloud** editions only.  
   * OAuth appears only after you register Jira OAuth credentials in **ALM Settings**. Learn how [here](user-management/manage-users-account-settings.md).  
   * **Access Token** expires after 1 hour; **Refresh Token** after 90 days.

   <figure><img src="../../../.gitbook/assets/image (744).png" alt="Jira OAuth token details"></figure>
   {% endhint %}

5. Click **Test Connection** to verify access, then **Save**.

   {% hint style="info" %}
   **Troubleshooting Authentication**  
   An *Authentication Failed* error on the EZ-Commit screen often stems from VPN issues or outdated credentials.  
   1. Go to **My Account › ALM Configuration**.  
   2. Click **Test Connection** to re-authenticate.  
   3. If it still fails, create a new credential and relink the ALM.
   {% endhint %}

6. The new ALM appears in the **ALM List**.

   * Toggle **AR Comments** to disable AutoRABIT-generated comments in Jira.  
   * For Jira, you can switch **Access Type** between *Standard* and *OAuth* and click **Re-Authenticate** when tokens expire.

{% hint style="info" %}
**Limitation:** Jira OAuth is Cloud-only and enabled on request. Contact **support@autorabit.com** if you need it.
{% endhint %}

---

## Integration Settings <a href="#integration-settings" id="integration-settings"></a>

Configure how work items are shown and filtered:

1. **Display work items from inactive sprints** – include backlog items.  
2. **Enable global filter criteria on work items** – add column filters as needed.  
3. Click **Save Settings**.

<figure><img src="../../../.gitbook/assets/image (745).png" alt="Integration Settings panel"></figure>

{% hint style="info" %}
To remove a field’s filter, click the trash-can icon next to the rule.
{% endhint %}

---

## Smart Commits <a href="#smart-commits" id="smart-commits"></a>

Define the pattern AutoRABIT uses to parse work-item references in commit messages—for example:

```

git commit -m "\[PROJECT-123] add README"

```

<figure><img src="../../../.gitbook/assets/image (746).png" alt="Smart Commits pattern settings" width="488"></figure>

* **Enable auto update on webhook** – reveals a webhook URL you can add to your VCS so external commits update the ALM automatically. See setup guides [here](../arm-features/automation-and-ci/webhooks/).  
* Optionally **sync external smart commits** made outside AutoRABIT.

---

## Repository Mappings <a href="#repository-mappings" id="repository-mappings"></a>

Repository mappings let AutoRABIT update ALM work-item status after a successful merge.

{% hint style="info" %}
* A mapping is **required** for smart-commit syncing.  
* Status changes apply **only** to merges performed through merge requests.

<figure><img src="../../../.gitbook/assets/image (747).png" alt="Repository Mappings table"></figure>
{% endhint %}

1. Choose the version-control **Repository**.  
2. Select the **Source Branch** (click *Register here* if it’s missing).  
3. Pick the **ALM Project**.  
4. In **ALM Work Item Status**, define:  
   * **Work Item Type**  
   * Current status  
   * Target status after merge

   <figure><img src="../../../.gitbook/assets/image (748).png" alt="ALM status mapping dialog" width="379"></figure>

5. Click **Save**.

{% hint style="info" %}
Branches and repos you **can’t** access won’t appear in the dropdowns.
{% endhint %}

6. Suppress ALM email noise by listing addresses in **Notify exception status updates to**.

<figure><img src="../../../.gitbook/assets/image (749).png" alt="Notify exception status updates field"></figure>
