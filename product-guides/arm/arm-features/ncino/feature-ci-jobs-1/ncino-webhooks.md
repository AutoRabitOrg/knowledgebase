# nCino Webhooks

## Webhooks for Auto Triggering nCino CI Jobs <a href="#title-text" id="title-text"></a>

Refer to [Webhooks](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks) for configuration details. Currently, nCino supports the following webhooks:

1. Webhook for GitHub
2. Webhook for GitHub Enterprise
3. Webhook for Microsoft Azure
4. Webhook for GitLab
5. Webhook for Bitbucket
6. Webhook for Bitbucket Enterprise
7. Webhook for Visual Studio GIT
8. Webhook for Visual Studio GIT Enterprise

For the above-mentioned repositories, if you select **“Trigger Build on Auto-Commit,”** the job will be triggered automatically for every new commit to the branch.

{% hint style="warning" %}
**Important Note**: If you’re committing both _nCino Record-Based Config_ files and _Salesforce Metadata_ files to the same branch—even though they’re in separate folders—AutoRABIT may encounter an issue with certain Git-based version control systems. Specifically, AutoRABIT is unable to determine which folder's contents have changed, leading to unnecessary build triggers that won't pick up any changes if they are in an irrelevant folder when the 'Build on commit' option is enabled.
{% endhint %}

### Configuring the CI Job for Trigger Build on Commit <a href="#manually-creating-records" id="manually-creating-records"></a>

1. Toggle the slider in the highlighted selection to enable 'Trigger Build on Commit' for the respective job.

<figure><img src="../../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Observe the copy symbol beside the URL. Use the highlighted URL as 'payload URL' in the configuration settings of the webhook. Refer to the following page for help configuring the [webhook](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks).
3. Once a job is created with the 'Trigger Build on Commit' setting enabled, then every commit into the respective repository and branch will auto-trigger a run in the application.

### Using Supported Deployment Types

For the _Revision Range_ deployment type, the `TriggerBuildOnCommit` option is **not supported**, which is expected behavior. When using a defined "From" and "To" revision, the system has no new revisions to detect or upon which to trigger builds. As a result, `TriggerBuildOnCommit` functionality does not apply to Revision Range deployments.

**Supported Deployment Types for** `TriggerBuildOnCommit`

The `TriggerBuildOnCommit` option is available for the following deployment types only:

1. **Version Control with Baseline Revision**: Suitable for deployments requiring specific baseline comparison.
2. **Entire Branch**: Triggers on new commits to the entire branch, allowing continuous integration.
3. **Version Control using Salesforce**: Integrates directly with version control but uses Salesforce to detect and trigger builds on commits.

If your deployment uses _Revision Range_, `TriggerBuildOnCommit` will not apply. If triggering builds on commits is required for your workflow, consider using one of the supported deployment types listed above.

### Manually Committing Templates <a href="#manually-creating-records" id="manually-creating-records"></a>

To manually commit the template data into your version control system (outside of AutoRABIT), follow the steps below:

#### **Information to collect before committing:** <a href="#information-to-collect-before-committing" id="information-to-collect-before-committing"></a>

* **HEXID**: A random 8-character alphanumeric string, for example: 10cPkE0E
* **Feature-Org-Id**: Provided by AutoRABIT upon request, for example: rJA5XMqsT71C6AwhaA7jyHznMxXvpRSM

#### Steps to Commit New Templates: <a href="#steps-to-commit-new-templates" id="steps-to-commit-new-templates"></a>

1. Add the HEXID and Feature-Org-Id details in the following files (refer to the attached sample file for guidance):
   * `feature-templates/nCino/config/manifest.yaml`
   * `feature-templates/nCino/config/project-def.json`
2. Create a feature folder named using the format `hexId-featureName` and include all relevant details such as filters, data, object sets, buckets, object relationships, and user IDs.
3. Ensure all information follows the folder structure of the reference folder.
4. Add `ar-config/project-def.json` file at root folder as in the attached reference.

#### Steps to Modify Existing Templates: <a href="#steps-to-modify-existing-templates" id="steps-to-modify-existing-templates"></a>

1. For any record additions, deletions, or updates, make the necessary changes under:
   * `feature-templates/nCino/dataset/hexId-FeatureName/data`
2. To modify object filters, make adjustments under:
   * `feature-templates/nCino/dataset/hexId-FeatureName/filters`

{% hint style="info" %}
Note:

* In the case of GitHub and GitLab, the jobs will only trigger if the commit has any changes related to “feature-templates.”
* For any version control types other than GitHub and GitLab, the CI Jobs will trigger for every commit regardless of data changes.
{% endhint %}

