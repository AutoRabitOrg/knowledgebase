# CI Job Rollback

{% hint style="info" %}
For the best experience, set your browser zoom to **80%** in Chrome or Firefox.
{% endhint %}

The **Rollback** feature enables you to revert a deployment if issues are detected post-deployment or if unintended changes were introduced.

---

### How to Roll Back a Deployment <a href="#how-to-roll-back-a-deployment" id="how-to-roll-back-a-deployment"></a>

This section explains how to roll back a deployment in your CI jobs. The goal is to restore a previous release or deployment state.

---

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

- The **Rollback** checkbox must be selected when creating the CI job.

---

#### Steps <a href="#steps" id="steps"></a>

1. Navigate to the **CI Job Results** screen.
2. Select the deployment label you want to roll back.
3. Click the **Rollback** icon: ![](<../../../../.gitbook/assets/image (1200).png>)

   <figure><img src="../../../../.gitbook/assets/image (1201).png" alt="Rollback Icon Location"></figure>

4. Under **API Supported > Constructive Changes**, you’ll see the list of metadata components from the original deployment. All are selected by default.

   <figure><img src="../../../../.gitbook/assets/image (1202).png" alt="Constructive Changes Selection" width="526"></figure>

   <figure><img src="../../../../.gitbook/assets/image (1203).png" alt="Rollback Metadata Overview"></figure>

5. In **Choose your Pre/Post Destructive Changes**, you can mark metadata present in the destination but absent in the source for deletion. These deletions are logged in the **Rollback Iteration Log**.

   <figure><img src="../../../../.gitbook/assets/image (1204).png" alt="Destructive Changes Selection"></figure>

6. Choose a method for destructive changes:
   - **Post Destructive Changes**: Deletes components *after* deployment.
   - **Pre-Destructive Changes**: Deletes components *before* deployment starts.

{% hint style="info" %}
**Note:** For active **Flow** metadata, you must include the version number. See [FlowDefinition documentation](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowdefinition.htm) for details.
{% endhint %}

7. The **API Un-Supported** section lists metadata types unsupported by the API. You can manually include these as pre or post-destructive changes.

   <figure><img src="../../../../.gitbook/assets/image (1205).png" alt="Unsupported API Components"></figure>

{% hint style="info" %}
**Caution:** Avoid using unsupported API components in rollback, as they may cause rollback failures.
{% endhint %}

---

### Additional Deployment Options

Available configuration options before rollback:

- **Validate Only**: Run a dry-run validation without performing the actual rollback.
- **Deploy Purge on Delete**: Permanently deletes components instead of moving them to the Salesforce Recycle Bin.
- **Ignore Warnings**: Continues rollback even if warnings are encountered.

<figure><img src="../../../../.gitbook/assets/image (1206).png" alt="Additional Rollback Options"></figure>

---

### Apex Test Level

Select an **Apex Test Level** to validate your rollback deployment.

- For details, see [Apex Unit Tests](https://knowledgebase.autorabit.com/arm/docs/apex-unit-tests).

<figure><img src="../../../../.gitbook/assets/image (1207).png" alt="Apex Test Level Selection"></figure>

---

### Final Step

9. Click **Rollback** to initiate the process.
10. Once completed, the rollback appears in the **CI Job Results** screen, tagged accordingly. From there, you can:
   - View rollback reports
   - Download the rollback package
   - Re-deploy the rollback if needed
