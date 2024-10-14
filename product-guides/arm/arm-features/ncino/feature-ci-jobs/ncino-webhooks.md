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

Refer to the following screenshot for making the selection:

**<----------------Place a screenshot of the selection to be made------------------>**

### Manually Creating Records <a href="#manually-creating-records" id="manually-creating-records"></a>

1. Provide your custom HEXID.
2. Reach out to AutoRABIT for the 'Feature Org ID.' AutoRABIT will provide the required “Org ID.”
3. Make the above-mentioned changes in the following:
   * manifest.yaml
   * project-def.json
   * dataset/\<HEXID>-Brands
4. Download the attached WebhookKnowBase-Branch-1 3.zip for reference on the structure of the file to be prepared.

