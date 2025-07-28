# JIRA

### JIRA: Overview <a href="#jira-overview" id="jira-overview"></a>

ARM-JIRA integration automatically posts updates to Jira tickets when you run validations and deployments, with a link back to the full report in ARM. It makes tracking the status of your user stories and support tickets faster and easier. Tasks can be organized by project, allowing an organization to track issues within projects transparently.

**To put it simply:** JIRA allows you to track any kind of unit of work (be it an issue, bug, story, project task, etc.) through a predefined workflow. However, in order to integrate JIRA as a plugin with ARM, it does require some steps in ARM to get it configured. The below section will help you out to get JIRA configured in ARM in easy steps.

Point to Note: **Jira OAuth** access type is currently supported for **Cloud versions** only. This function is on-demand, so if you'd want to make it available for your organization, please get in touch with our experts at [support@autorabit.com](mailto:support@autorabit.com).

### Integrate JIRA with ARM <a href="#integrate-jira-with-arm" id="integrate-jira-with-arm"></a>

#### Step 1: Store your user's JIRA credential in ARM <a href="#step-1-store-your-users-jira-credential-in-arm" id="step-1-store-your-users-jira-credential-in-arm"></a>

This is an initial step where the user's JIRA credential, such as username and password, is stored in ARM.

1. Log in to your ARM account.
2. Hover your mouse over the **Admin** module and click on the **Credentials** tab.

<figure><img src="../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="353"><figcaption></figcaption></figure>

3. Next, click on **Create Credential** from the right navigation bar.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next pop-up screen, give a **Credential name**.
5. Choose the **Credential Type** as '**User name with Password.'**
6. Enter your JIRA **username** and **password;** we will store this encrypted.
7. Please double-check that you use your JIRA username instead of the email address that you use to log in to JIRA.
8. Click **Save**.

<figure><img src="../../../.gitbook/assets/image (25) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="416"><figcaption></figcaption></figure>

{% hint style="warning" %}
**Troubleshooting:**

While registering JIRA with ARM, JIRA fails to connect and results in **"Authentication Failure,"** please use the below steps to re-authenticate the JIRA.

1. Use the **"https://id.atlassian.com/manage/api-tokens"** link to generate a new API token.
2. Click on **"Create API Token,"** provide the label name and click on **Create**.
3. The token gets created. You will be able to see the **"Your new API token"** popup; click on the **"Copy to Clipboard."**
4. Use the copied token as a password for creating/updating the credential in ARM.
5. Once updated, please use the same credential to authenticate the JIRA.
{% endhint %}

#### Step 2: Integrate JIRA with ARM <a href="#step-2-integrate-jira-with-arm" id="step-2-integrate-jira-with-arm"></a>

1. If you're logged out from your account, log in again into ARM with your credentials.
2. Go to **Admin > My Account** section.
3. Click on **New ALM System** under the **ALM Management** section.

<figure><img src="../../../.gitbook/assets/image (26) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Select **ALM type** as '**JIRA'** from the drop-down.

<figure><img src="../../../.gitbook/assets/image (27) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="379"><figcaption></figcaption></figure>

5. Enter the **label name** of your own choice.
6. Enter your JIRA subdomain (e.g., _https://\[subdomain].atlassian.net_) in the **URL** field.
7. Select the same **user's credential** created in **Step 1**.
8. Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
9. Click **Save** and your Jira integration are ready.
10. Once you log in, JIRA is integrated with your ARM account, and you can start logging bugs and issues with just one click directly to JIRA.

{% hint style="danger" %}
**Limitation:**

**Jira OAuth** access type is currently supported for **Cloud versions** only. This function is on-demand, so if you'd want to make it available for your organization, please get in touch with our experts at [support@autorabit.com](mailto:support@autorabit.com).
{% endhint %}

### Steps to Configure OAuth in ARM

1. **Create an OAuth App in Atlassian**
   * Go to the Atlassian Developer Console and create a new **OAuth 2.0 (3LO)** app.
   * Enter the **callback URL** provided in ARM.
   * Copy the **Client ID** and **Client Secret**.
2. **Configure in AutoRABIT**
   * In ARM, go to **Admin > My Account**.
   * Scroll to **ALM Settings** and expand the **JIRA** section.
   * Enter the **Client ID**, **Client Secret**, and the **callback URL**.
   * Click **Test Credentials**, then **Save**.
3. **Authorize the Connection**
   * You’ll be redirected to JIRA to log in and approve access.
   * Once authorized, the connection is complete.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Mapping JIRA to Salesforce Org/ Version Control <a href="#mapping-jira-to-salesforce-org-version-control" id="mapping-jira-to-salesforce-org-version-control"></a>

Once you are done registering the plugins with ARM, make sure you map the JIRA ALM type with your required Salesforce Org/ Version Control. Mapping will help you manage a seamless and accurate Salesforce change management process directly from within your Jira projects and teams.&#x20;

1. Go to the **Salesforce Org Management(Admin > SF Org Mgmt.)** page.
2. Select the **Salesforce org** for which you like to map the JIRA as a plugin.
3. Under **Salesforce Org- Mappings** tab, choose **JIRA** as ALM type and click on **Mapping**.
4. Select the **label** and the **project**.
5. Click **Save Mappings**. The selected plugin will be mapped with your Salesforce Org.

<figure><img src="../../../.gitbook/assets/image (28) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuring JIRA Work items in ARM <a href="#configuring-jira-work-items-in-arm" id="configuring-jira-work-items-in-arm"></a>

You and your team members have a provision to perform actions on Jira issues or update the JIRA work items while running a commit or during a CI job.

#### In EZ-Commit <a href="#in-ezcommit" id="in-ezcommit"></a>

In the **EZ-Commit** screen and under the **Post Commit** section, you need to:

1. Select the checkbox: **Update ALM Workitem Status.**
2. Select the **ALM type** as **JIRA.**
3. Select the **ALM Label, project,** and the **sprint** for which the commit is planned.
4. Select the **work item** and the **status**.

<figure><img src="../../../.gitbook/assets/image (29) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Once the changes are committed to the version control system, the status of the ALM work item is updated and reflected in your ALM system.

#### In CI Job <a href="#in-ci-job" id="in-ci-job"></a>

{% hint style="info" %}
**Important Notes:**&#x20;

Configuring the Jira work items is applicable to the following CI jobs:

* Package from Version Control
* Deploy from Version Control
* Deploy from the SFDX branch to a Salesforce Org
* Install an Unlocked Package from Version Control Branch
{% endhint %}

1. Go to the **Build** section under the **New Create CI Job** screen.
2. Tick the **Map ALM Project (Ex: Jira)** checkbox.

<figure><img src="../../../.gitbook/assets/image (30) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="441"><figcaption></figcaption></figure>

3. Go to the **ALM** section. Here you can configure the work item type status in JIRA ALM to include in the build.
4. Select the **ALM type** as **JIRA.**
5. Select the **ALM Label** and its related **Projects**.

<figure><img src="../../../.gitbook/assets/image (31) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

6. The active sprint(s) for the above-selected Project will be available in the **Sprint** drop-down. ARM has given provisions for you to update multiple sprints related to tasks or bugs and update the status on the go when running the CI Job. You can select either one of the sprints or if you wish to update the status for all the sprints, leave it as default, i.e., keep **'All Active Sprints'** in the selected mode.

<figure><img src="../../../.gitbook/assets/image (32) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Select the **Work Item** type. Here you can select multiple work items that you like the update the status in your ALM. To use all the work item types, keep the **'All Work Item Type'** option selected by default.
8. Based on the above work item selected, you need to update the status for each work item type. See the screenshot attached.

<figure><img src="../../../.gitbook/assets/image (33) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
