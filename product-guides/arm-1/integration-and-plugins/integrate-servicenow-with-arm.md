# ServiceNow

## Step 1: Store Your ServiceNow Credentials in ARM

1. Log in to your ARM account.
2. Navigate to the **Admin** module and click the **Credentials** tab.

\
&#x20;<img src="../../../.gitbook/assets/image (2887).png" alt="" data-size="original">



3. Click **Create Credential** from the right navigation.

<figure><img src="../../../.gitbook/assets/image (2515).png" alt=""><figcaption></figcaption></figure>

4. In the popup:

* Enter a **Credential Name**
* Set **Credential Type** to _User name with Password_
* Input your **ServiceNow username** and **password**
* Ensure you're using your **username**, not your login email

5. Click **Save**

<figure><img src="../../../.gitbook/assets/image (2516).png" alt=""><figcaption></figcaption></figure>

***

## Step 2: Integrate ServiceNow with ARM

1. Log in to ARM (if not already logged in).
2. Go to **Admin > My Account**
3. Click **New ALM System** under the **ALM Management** section
4.  Set **ALM Type** as **SERVICENOW**\
    \
    <br>

    <figure><img src="../../../.gitbook/assets/image (2517).png" alt=""><figcaption></figcaption></figure>
5. Enter:
   * A **Label Name**
   * Your ServiceNow **subdomain URL** (e.g., `https://[subdomain].service-now.com`)
   * The **credentials** stored in Step 1
6. Click **Test Connection** to validate
7. Click **Save** to complete the integration

> Once integrated, you can log bugs/issues to ServiceNow directly from ARM.

{% hint style="danger" %}
**Note:** ServiceNow OAuth integration is supported only for **Cloud versions**. Contact **support@autorabit.com** to enable this feature.
{% endhint %}

***

## Configuring ServiceNow Work Items in ARM

### EZ-Commit Integration

1. In the **EZ-Commit** screen under **Post Commit**:
   * Check **Update ALM Workitem Status**
   * Select:
     * **ALM Type:** SERVICENOW
     * **ALM Label, Project, Sprint,** and **Work Item**
     * **Status** to be updated

<figure><img src="../../../.gitbook/assets/Screenshot 2026-09-30 at 3.27.36 PM.png" alt=""><figcaption></figcaption></figure>

2. Upon commit, work item status will be reflected in ServiceNow.

***

### CI Job Integration

#### Applicable to:

* Package from Version Control
* Deploy from Version Control
* Deploy from SFDX branch to Salesforce Org
* Install Unlocked Package from VCS

1.  In **Build** section of CI Job creation:

    * Check **Map ALM Project (Ex: ServiceNow)**

    <figure><img src="../../../.gitbook/assets/image (2889).png" alt=""><figcaption></figcaption></figure>
2. Go to **ALM** section:

* Set:
  * **ALM Type:** SERVICENOW
  * **Label** and **Projects**

<figure><img src="../../../.gitbook/assets/Screenshot 2026-09-30 at 3.30.10 PM.png" alt=""><figcaption></figcaption></figure>

3. Choose:

* One or all **Active Sprints**

<figure><img src="../../../.gitbook/assets/Screenshot 2026-09-30 at 3.32.57 PM.png" alt=""><figcaption></figcaption></figure>

4. Select:

* **Work Item Type** (or all)

<figure><img src="../../../.gitbook/assets/Screenshot 2026-09-30 at 3.34.59 PM.png" alt=""><figcaption></figcaption></figure>

5. Update the **Status** for selected work item types

<figure><img src="../../../.gitbook/assets/Screenshot 2026-09-30 at 3.36.20 PM.png" alt=""><figcaption></figcaption></figure>
