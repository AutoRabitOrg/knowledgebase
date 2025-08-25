# Enabling GitHub Checks

### About GitHub Status Checks <a href="#about-github-status-checks" id="about-github-status-checks"></a>

GitHub status checks are an excellent way to track and control the [CI/CD](../../../arm/troubleshoot/best-practices/branching-strategy-and-ci-cd-pipeline.md) status of your projects. AutoRABIT will send status checks for the pull requests to your GitHub repo and allows you to control when pull requests can be merged based on the results of the CI job. AutoRABIT reports the status of workflows and all corresponding jobs under the **Checks** tab on GitHub.

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Requirement <a href="#requirement" id="requirement"></a>

GitHub repositories registered in AutoRABIT should have the pull request feature enabled. \[[Learn More](../../../arm/arm-features/version-control/external-pull-request/)]

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Protected Branches <a href="#protected-branches" id="protected-branches"></a>

Protected Branches are a feature in [GitHub](../../../arm/arm-features/automation-and-ci/webhooks/configure-a-webhook-in-github.md) which lets you block merging pull requests into specific branches unless status checks have passed.&#x20;

If you’re a repository owner, you can update your repositories using protected branches to use status checks per the following:

1. Go to your repository’s **Settings** page.
2. In the left-hand menu, click **Branches**.&#x20;
3. Under **Branch protection rules** either click **Edit** for a rule that you would like to change or click **Add rule** at the top to create a new rule.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. If adding a new rule, enter the desired branch name in the **Branch name pattern** field.
5. Scroll down to the second box - **Require status checks to pass before merging**.&#x20;

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. From the build status checks in the last week of your repository, select one of them.
7. Click **Create**.

### To enable GitHub Checks <a href="#to-enable-github-checks" id="to-enable-github-checks"></a>

{% hint style="info" %}
The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

Enable the checkbox: **Status Check API** for your GitHub Repo under the **Build** section while creating a new CI job.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Whenever the job runs, AutoRABIT will automatically post the build status back to GitHub, referencing the relevant git commit and the outcome of the job (success or failure).

If a user selects CI deployment job (build and deploy), status check API is updated in the final step, i.e.,  after the build is successful and the deployment is completed.

If a user selects CI job to build only, status check API is updated after the build is completed.

### PR Validation

GitHub Status Checks API works on the Commit revision number but not on the Pull Request. It is to use the REST API to allow external services to mark commits with an error, failure, pending, or success state, which is then reflected in Pull Requests involving those commits.

**Let’s take an example:**&#x20;

Let's consider three branches: A, B, and C.

1. If Branch B is configured in the CI job with status check API
2. Suppose we have created the Pull request between branch A and branch B. -> above created CI job is triggered automatically on revision number 1234567, which is the latest revision of branch A.
3. Status Check API is triggered on CI job build revision number 1234567, which means this revision is available in branch A. So, two Pull requests contain the same source branch, and that’s the reason it is showing in multiple pull requests.

### Troubleshooting required status checks <a href="#troubleshooting-required-status-checks" id="troubleshooting-required-status-checks"></a>

1. After you enable the required status checks, your branch may need to be up-to-date with the base branch before merging. This ensures that your branch has been tested with the latest code from the base branch. If your branch is out of date, you'll need to merge the base branch into your branch.
2. The results of the deployment status in Github and the AutoRABIT application can sometimes be conflicting. While the deployment is still in progress in AutoRABIT, the status will be updated earlier on Github. This is due to the post-deployment activities being performed in AutoRABIT.

### Status Check API Functionality Documentation

This outlines the functionality of the Status Check API based on the different statuses of CI Jobs. The Status Check API triggers different responses depending on the current status of the CI Job, as detailed below.

* Status check API is triggered as "Pending" if the CI job status is "In progress".
* Status check API is triggered as "Success" if the cijob status is "Completed," "Partial”
* Status check API is triggered as "Error" if the cijob status is "Aborted".
* Status check API is triggered as "Failure" if the job status is "Failed" or "Unstable."
* If the CI Job status shows as "No Modifications" then the Status Check API should not get triggered at all.
