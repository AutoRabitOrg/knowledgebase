# ALM Management

{% hint style="info" %}
**Important Note:** The actions described here are available **only to Org Administrators**. General ARM users cannot access ALM Management.
{% endhint %}

## Why Integrate an ALM? <a href="#overview" id="overview"></a>

AutoRABIT can connect to popular **Application Lifecycle Management (ALM)** platforms—Jira, Azure DevOps, IBM RTC, CA Agile Central (Rally), and VersionOne—to:

* Surface active and inactive sprints in one place.
* Sync work-item status automatically during merges, commits, and CI jobs.
* Enforce release governance with smart-commit patterns and webhook automation.

The **ALM Management** page (added in ARM 21.6) lives under **Admin** and lets you register new ALM connections, set integration rules, and manage repository mappings.

***

## Registering an ALM <a href="#registering-an-alm" id="registering-an-alm"></a>

1. Log in to ARM as an admin.
2. Navigate to **`Admin > ALM Mgmt`**.
3. Click **`Register ALM`** on the **`ALM Mgmt.`** screen.

<figure><img src="../../../.gitbook/assets/image (739).png" alt=""><figcaption></figcaption></figure>

4. Configure the following settings:
   1.  For **`IBMRTC`**, **`CA Agile Central`**, **`VersionOne`**, and **`Azure DevOps:`**

       * **`ALM Name:`** Enter a **name** for your ALM connection.
       * **`ALM Type:`** Select the **ALM type**.
       * **`ALM URL:`** Add the **ALM server URL**.
       * **`Credentials:`** Specify your credentials. Refer to the [Credential Manager](../troubleshoot/how-tos/create-users-credentials.md) section for more info on creating and storing your credential inside ARM.

       <figure><img src="../../../.gitbook/assets/image (740).png" alt="" width="414"><figcaption></figcaption></figure>
   2.  For **`JIRA:`**&#x20;

       <figure><img src="../../../.gitbook/assets/image (742).png" alt="" width="414"><figcaption></figcaption></figure>

       * **`ALM Name:`** Enter a name for your ALM connection.
       * **`ALM Type:`** Select **`JIRA`**.
       * **`Access Type:`**&#x53;elect one of the following:
         * **`Standard:`** Add the **`ALM URL`** and specify your **`Credentials`**.
         * **`OAuth:`** Select the access type as **`OAuth`**, and click on **`Validate & Save`**. You will be redirected to the ALM's website to authenticate your credentials and grant permission.

{% hint style="info" %}
**Important Notes:**

* Jira OAuth access type is currently supported for **Cloud versions** only.
* OAuth access type will only be available while registering ALM if the credentials have been successfully registered in the **ALM Settings** section. For more information on registering Jira OAuth credentials, click [here](user-management/manage-users-account-settings.md).

![](<../../../.gitbook/assets/image (744).png>)

* The **Access Token** expires in one hour. The **Refresh Token** expires every **90 days**.
{% endhint %}

5. Click on **`Test Connection`** to authenticate your credentials.
6. Click **`Save`**.

{% hint style="info" %}
NOTE: An "Authentication Failed" error may occur when selecting an ALM on the EZ-Commit screen. VPN connectivity appears to be the source of intermittent ALM connectivity issues; the ALM is incorrectly configured. To correct this issue:

* On the My Account screen, look for the ALM configuration.
* To reauthenticate your ALM configuration, click the Test Connection icon to verify your credentials.

If the steps above do not work, create a new credential and link it to your ALM account.
{% endhint %}

7. Once your [ALM](../arm-features/version-control/change-labels/alm-labels.md) is registered successfully, you can view it in the **`ALM List`** menu.
8. Use the **`AR Comments`** toggle button to turn off the Jira comments from AR. By default, the Jira comments are ON for newly registered and existing ALMs.
9. Use the **`Access Type`** drop-down list to switch between **`Standard`** and **`OAuth`**. Click on **`Re-Authenticate`** if your credentials have expired. This is only applicable to Jira ALMs.

{% hint style="info" %}
**Limitation:** Jira OAuth access type is currently supported for **Cloud versions** only. This function is on-demand, so if you'd want to make it available for your organization, please contact our experts at [support@autorabit.com](mailto:support@autorabit.com).
{% endhint %}

## Integration Settings <a href="#integration-settings" id="integration-settings"></a>

By default, we do not display the work items from the inactive sprints; however, if you want to view the hidden items, you can do so from this section.

1. Select the following checkbox to view the work items from the inactive sprints: **`Display work items from inactive sprints (we recommend setting up global filter criteria if are enabling this)`**
2. **`Enable global filter criteria on work items`**: This checkbox allows you to specify filter criteria.
   * You can select which fields are displayed by selecting the necessary column/field. However, you can refine the list of work items displayed by configuring a worklist filter.
   * Repeat these steps for each field if you want to set filter criteria.
3. Click **`Save Settings`**.

<figure><img src="../../../.gitbook/assets/image (745).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To remove a field's filter criteria, click on the ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-QT6MJ131.png) icon to the right of the rule.
{% endhint %}

***

## Registering an ALM - Saas Toolkit <a href="#registering-an-alm" id="registering-an-alm"></a>

1. Log in to ARM as an administrator.
2. Navigate to **Admin › ALM Mgmt**.
3.  Click **Register ALM**.\


    <figure><img src="../../../.gitbook/assets/image (1869).png" alt=""><figcaption></figcaption></figure>
4.  Fill the form:

    1. **ALM Name** – friendly label.
    2. **ALM Type** – choose the platform.\
       ![](<../../../.gitbook/assets/image (1870).png>)



**Field Mapping for Work Item Updates in Salesforce**

To enable AutoRABIT to update your Work Items (e.g., User Stories or Bugs) based on commit actions, please configure the following fields from your registered Salesforce Org:\
![](<../../../.gitbook/assets/image (1872).png>)\


c. Salesforce Org\
Select the Salesforce Org from your list of registered orgs where the work item updates should be applied.

d. Custom Object / Work Item Type\
Choose the Custom Object that represents your Work Items (e.g., User\_Story\_\_c, Bug\_\_c). This is where the Work Item ID will be updated.

e. Title Field\
Map the field that represents the project or feature to which the Work Item belongs. This is usually a custom text field like Project\_\_c.

f. Assignee Field\
Select the custom field that stores the user assigned to the Work Item. This allows AutoRABIT to track ownership of the User Story or Bug.

g. Status Field\
Choose the custom field that reflects the current status of the Work Item (e.g., New, In Progress, Ready for QA, Closed). This field can be updated automatically based on the commit action.

h. Comment Field\
Select the custom field where commit-related comments should be posted. The system will populate this with detailed commit information after the action is performed.\
\
**1. Select Post Commit Action**\
\
Under the Post Commit section, select:

**2. Update ALM Work Item Status**

**Configure ALM Fields**\
Fill in the required fields to ensure the correct ALM Work Item is updated post-commit:

**ALM Type**: Choose the integrated ALM tool (e.g., Salesforce).

* ALM Label: Select the applicable label for this commit operation.
* ALM Project: Pick the project or module name (e.g., User Story, Bug).
* ALM Work item: Select the Work Item ID you wish to update.
* ALM Work Item Status: Choose the new status you want to set (e.g., To Do, In Progress, Done).
*   Current Status: Shows the status of the item (e.g., In Testing).\


    <figure><img src="../../../.gitbook/assets/image (1873).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1874).png" alt=""><figcaption></figcaption></figure>

**Complete the Commit**\
Click Commit after configuring all required fields. The system will:

* Perform the commit action.
* Post-commit, automatically update the ALM Work Item to the new selected status.
* Add relevant commit information to the comment field (if configured), including metadata, user, and validation results.

&#x20;

**Sample Outcome Post Commit Comment Format:**\
\
The selected Work Item will reflect the updated status in your ALM tool and include commit metadata like:

\[Message] \[a00dL00001DYPnCQAX]# Saas tool Integration-2&#x20;

\[Repository] bhanu-github-cloud&#x20;

\[Branch] 18235\_test&#x20;

\[Revision] 3637289&#x20;

\[Committed by] bhanuprakash.yempati@autorabit.com&#x20;

\[Committed metadata members] {Apex Class=\[A000, A0000]}&#x20;

\[Pre-validation Results]&#x20;

&#x20; Label Name = a00dl00001dypncqax.20250702204545047&#x20;

&#x20; Apex Test Results = NA&#x20;

&#x20; Static Analysis = NA&#x20;

&#x20; Deployment Org = NA&#x20;

&#x20; Overall Validate Deployment Status = NA&#x20;

&#x20; Approved By = bhanuprakash.yempati@autorabit.com&#x20;

***

## Smart Commits <a href="#smart-commits" id="smart-commits"></a>

Define the pattern AutoRABIT uses to parse work-item references in commit messages—for example:

```

git commit -m "\[PROJECT-123] add README"

```

<figure><img src="../../../.gitbook/assets/image (746).png" alt="Smart Commits pattern settings" width="488"><figcaption></figcaption></figure>

* **Enable auto update on webhook** – reveals a webhook URL you can add to your VCS so external commits update the ALM automatically. See setup guides [here](../arm-features/automation-and-ci/webhooks/).
* Optionally **sync external smart commits** made outside AutoRABIT.

***

## Repository Mappings <a href="#repository-mappings" id="repository-mappings"></a>

Repository mappings let AutoRABIT update ALM work-item status after a successful merge.

{% hint style="info" %}
* A mapping is **required** for smart-commit syncing.
* Status changes apply **only** to merges performed through merge requests.

<img src="../../../.gitbook/assets/image (747).png" alt="" data-size="original">
{% endhint %}

1. Choose the version-control **Repository**.
2. Select the **Source Branch** (click _Register here_ if it’s missing).
3. Pick the **ALM Project**.
4.  In **ALM Work Item Status**, define:

    * **Work Item Type**
    * Current status
    * Target status after merge

    <figure><img src="../../../.gitbook/assets/image (748).png" alt="ALM status mapping dialog" width="379"><figcaption></figcaption></figure>
5. Click **Save**.

{% hint style="info" %}
Branches and repos you **can’t** access won’t appear in the dropdowns.
{% endhint %}

6. Suppress ALM email noise by listing addresses in **Notify exception status updates to**.

<figure><img src="../../../.gitbook/assets/image (749).png" alt="Notify exception status updates field"><figcaption></figcaption></figure>
