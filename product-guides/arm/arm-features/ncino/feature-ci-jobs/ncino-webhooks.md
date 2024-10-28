# nCino Webhooks

## Webhook for Auto Triggering nCino CI Jobs <a href="#title-text" id="title-text"></a>

Refer to [Webhooks](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks) for configuration details. Currently, nCino supports the following webhooks:

1. Webhook for Git
2. Webhook for Git Enterprise
3. Webhook for Microsoft Azure
4. Webhook for GitLab
5. Webhook for Bitbucket
6. Webhook for Bitbucket Enterprise
7. Webhook for Visual Studio GIT
8. Webhook for Visual Studio GIT Enterprise

For the above-mentioned repositories, if the user selects **“Trigger Build on Auto-Commit,”** the job will be triggered automatically for every new commit to the branch.

{% hint style="warning" %}
**Important Note**: Note: If you’re committing both _nCino Record-Based Config_ files and _Salesforce Metadata_ files to the same branch—even though they’re in separate folders—AutoRABIT may encounter an issue with certain Git-based version control systems. Specifically, AutoRABIT is unable to determine which folder's content has changed, leading to unnecessary build triggers that won't pick any changes if changes are in an irrelevant folder when the 'Build on commit' option is enabled.
{% endhint %}

### Manually Creating Records <a href="#manually-creating-records" id="manually-creating-records"></a>

1. Provide your custom HEXID.
2. Reach out to AutoRABIT for the 'Feature Org ID.' AutoRABIT will provide the required “Org ID.”
3. Make the above-mentioned changes in the following:
   * manifest.yaml
   * project-def.json
   * dataset/\<HEXID>-Brands
4. Download the attached WebhookKnowBase-Branch-1 3.zip for reference on the structure of the file to be prepared.

