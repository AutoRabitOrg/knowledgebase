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

## Register an ALM <a href="#registering-an-alm" id="registering-an-alm"></a>

1. Log in to ARM as an administrator.
2. Navigate to **Admin › ALM Mgmt**.
3.  Click **Register ALM**.\


    <figure><img src="../../../.gitbook/assets/image (1869).png" alt=""><figcaption></figcaption></figure>
4.  Fill the form:

    1. **ALM Name** – friendly label.
    2. **ALM Type** – choose the platform.\
       ![](<../../../.gitbook/assets/image (1870).png>)



## Field Mapping for Work Item Updates in Salesforce

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
