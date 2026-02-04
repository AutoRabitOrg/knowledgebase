# Start a CI Build Automatically or Manually

{% hint style="info" %}
The **CI Jobs** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The following articles describe how to trigger a new build for your CI Job created in AutoRABIT.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* Users must have permission to access the **CI Job Results** page.
* The account owner or admin can assign this permission under **Admin > Roles** by enabling the required permission in the role configuration.

***

### Trigger a new Build <a href="#trigger-a-new-build" id="trigger-a-new-build"></a>

1. Navigate to the **CI Job Results** screen.
2. This screen lists all CI Jobs for which builds have been triggered.

<figure><img src="../../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

1. Jobs with deployments display the icon: ![](<../../../../.gitbook/assets/image (1141).png>), while validated-only jobs show: ![](<../../../../.gitbook/assets/image (1142).png>)
2. Use the **Select Job** dropdown to choose your CI job.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

1. If no builds exist yet, you'll see:\
   &#xNAN;**"No builds found for this job. Please trigger a new build for results."**\
   Click **Build Now**.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. If previous builds exist, click **Build Now** to trigger a new build.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. The build initiation screen will differ depending on whether your CI Job is configured with ALM.

***

**ALM-configured CI Job**

ALM-integrated CI Jobs display ALM work item information from the source version control branch.

<figure><img src="../../../../.gitbook/assets/image (1146).png" alt="ALM integration panel showing work items"><figcaption></figcaption></figure>

* **Commit**: Displays work items committed to the source branch.

<figure><img src="../../../../.gitbook/assets/image (1147).png" alt="ALM work items from commits" width="513"><figcaption></figcaption></figure>

* **Merge**: Displays work items merged into the source branch.

<figure><img src="../../../../.gitbook/assets/image (1148).png" alt="ALM work items from merges" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. **ALM Label Type: Commit:** If a label is selected, results show all commits regardless of status.
2. If no label is selected, all committed and merged revisions matching the CI Job configuration will be packaged. This applies to scheduled CI Jobs as well.
{% endhint %}

***

**Without ALM-configured CI Job**

CI Jobs without ALM integration show the following build input screen:

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Enter a **Title** and optional **Comments**
* Choose **Deployment Type**:
  * **Deploy**: Executes a full deployment to destination org or branch.
  * **Validate only**: Runs validations without deployment.

**Additional Options:**

1. **Run Code Coverage On Destination**
   * Enabled if test execution is configured in the CI Job.
   * Generates Apex test coverage reports.
2. **Enable Rollback For Deployment**
   * Enabled if **Rollback** was selected in the CI Job's **Deploy** section.
3. **Ignore Warnings**
   * Allows deployment to continue despite warnings.

* Use the **Notes** field to enter optional information.
* Click **Trigger Build** to validate and execute the build.

{% hint style="info" %}
**Important Notes:**

* The **Validate only** deployment type does not run test cases.
* Avoid editing CI Jobs while a build is in progress to prevent job failure. Abort the build if edits are necessary.
{% endhint %}

8. Upon triggering, you will be redirected to the [CI Job Results](../../../arm/arm-features/automation-and-ci/ci-job-history.md) page, where build reports are available.

***

### For the following Pull Request events, AutoRABIT triggers a build:

**Validation Details:**

* Editing and committing a pull request triggers the CI job as expected.
* When a pull request is edited, GitHub marks it accordingly, and AutoRABIT builds are triggered upon commit synchronization.

**Webhook Delivery Screenshot:**

<figure><img src="../../../../.gitbook/assets/image (1150).png" alt="Webhook event delivery log from GitHub"><figcaption></figcaption></figure>

**Webhook Configuration Screenshot:**

<figure><img src="../../../../.gitbook/assets/image (1151).png" alt="Webhook settings for GitHub repository integration"><figcaption></figcaption></figure>
