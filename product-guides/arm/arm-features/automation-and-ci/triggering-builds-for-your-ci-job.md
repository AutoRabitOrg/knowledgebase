# Triggering Builds for your CI Job

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

The following articles talk about how to trigger a new build for your CI Job that you've created in AutoRABIT.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* The users must have permission to access the **CI Job Results** page in order to trigger a build.&#x20;
* The account owner or admin can assign the required permission to the users by visiting the **Admin > Roles** tab and create a role with the above-mentioned permission enabled.

### Trigger a new Build <a href="#trigger-a-new-build" id="trigger-a-new-build"></a>

1. Go to the **CI Job Results** screen.
2.  This screen will list all the CI Jobs for which the builds have already been triggered.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624787687123.png" alt="" width="563"><figcaption></figcaption></figure>

The CI Jobs deployed will have ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624787522949.png)symbols next to them and the one with only validated CI Jobs will have ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624787497205.png)symbols next to it.

1. Select your **CI job** in the **Select Job** dropdown. The dropdown here allows switching between the CI Jobs available.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619434914138.png" alt="" width="375"><figcaption></figcaption></figure>

1.  If there are no builds triggered yet, you get the notification as, **"No builds found for this job. Please trigger a new build for results."** Click on **Build Now**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619432044022.png" alt="" width="563"><figcaption></figcaption></figure>
2. If the builds already exist and you wish to trigger another one, you can do so using the **Build Now** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1624788002638.png" alt="" width="563"><figcaption></figcaption></figure>

The new build screen differs based on how your CI job is configured (with or without ALM configuration).

#### 1. ALM configured CI Job <a href="#id-1-alm-configured-ci-job" id="id-1-alm-configured-ci-job"></a>

For CI jobs configured with ALM details, the following screens are displayed and you can find the ALM work item details configured to the source Version control branch here.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619434360884.png" alt="" width="563"><figcaption></figcaption></figure>

1.  **Commit:** The ALM work items that are configured while committing to the selected source branch and meet the CI Job configuration will get fetched. All the available work item types, their status, and ALM data are displayed as per the workflow defined in the ALM system.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619434532945.png" alt="" width="563"><figcaption></figcaption></figure>
2.  **Merge:** The ALM work items configured while merging to the selected source branch and meet the CI Job configuration will get fetched will get displayed.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619434584201.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. **For ALM Label Type as Commit**: When you pick a work item in the dropdown, the result will show all commits regardless of the status configured.
2. If the user does not specify any label, all the **committed** and **merged work item** revisions will be packaged based on the CI job configuration. This scenario applies to scheduled CI jobs too.
{% endhint %}

#### 2. Without ALM configured CI Job <a href="#id-2-without-alm-configured-ci-job" id="id-2-without-alm-configured-ci-job"></a>

For the CI jobs configured without ALM, the below screen will be displayed.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1619434684534.png" alt="" width="563"><figcaption></figcaption></figure>

1. Under the **Build** inputs, enter the **title** of the build and add **comments** if any
2. Choose the **Deployment Type** i.e., **Deploy** (deploy the changes to the destination org/branch) or **Validate only** (validating before deploying the changes to the destination org).
3. Additional options:
   1. **Run Code Coverage On Destination:** This option is visible only if the user has been enabled to run the apex text class when configuring their CI Job. This option generates the code coverage report which provides information about the apex tests that are run, the classes that are covered, and the assertions that have failed and provide a percentage of the code that is covered by the test execution.
   2. **Enable Rollback For Deployment:** This option will enable the rollback function when running the deployment. This option will also be visible if the user has selected the **Rollback** option in the **Deploy** section while configuring their CI Job.
   3. **Ignore Warnings:** This checkbox allows the metadata members to deploy even if warnings are encountered.
4. Add any additional information in the **Notes** section. However, this is optional.
5. Click on **Trigger Build**. It validates the user credentials and upon successful validations, the build gets triggered.

{% hint style="info" %}
**Important Notes:**

* **Trigger Build** does not run the test cases for **Validate only** deployment type.
* It's best not to edit the CI jobs while the build progresses, which may lead to the failure of the job. Abort the build process if required to edit the CI jobs.
{% endhint %}

1. You'll be redirected to the [CI Job Results](ci-job-history.md) page where you can view the detailed report for your build triggered.

### For the following events in Pull request, AutoRABIT will initiate the build:

```
GITHUB_ACTIONS_TOPROCEED = "opened,edited,synchronize"
```

**Here is the validation detail:**

When you edit the pull request and commit the change, the CI job is triggered as expected.

When you edit the pull request, it's marked as edited. Upon committing the pull request, it synchronizes and pushes as expected.

**Refer to the screenshot below for webhook delivery:**

<figure><img src="../../../../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

**The screenshot below refers to webhook configuration settings:**

<figure><img src="../../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>
