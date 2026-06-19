# Handling Deletions or Destructive Changes

{% hint style="info" %}
The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### About Destructive Changes <a href="#destructive-changes" id="destructive-changes"></a>

“Destructive Changes” allows users to remove metadata components from a target Salesforce org as part of the deployment process. This includes deleting components such as classes, fields, objects, or other configurations that are no longer required.

Example: A custom field created during development is no longer needed in Production. Instead of manually deleting it, the user includes it as a destructive change during deployment, ensuring it is removed in a controlled and trackable manner.

This option is useful in the following scenarios:

* Removing unused or deprecated metadata components.
* Cleaning up technical debt in the org.
* Aligning target org with source by deleting extra components.
* Reducing deployment errors caused by obsolete configurations.
* Maintaining a clean and optimized Salesforce environment.

#### Types of Destructive Changes <a href="#types-of-destructive-changes" id="types-of-destructive-changes"></a>

1. **Post-Destructive Changes**: Deletes unwanted metadata components from the destination org after a successful deployment.
2.  **Pre-Destructive Changes**: Deletes unwanted metadata components from the destination org before the deployment begins.



Example:\
If an old custom field needs to be removed and a new field is being deployed as a replacement, you may use **Pre-Destructive Changes** to remove the old field before deploying the new metadata.\
If certain components should only be removed after ensuring the new deployment is successful, you can use **Post-Destructive Changes**, so the deletion occurs only after successful completion of the deployment.

### Deploying Destructive Changes <a href="#deploying-destructive-changes" id="deploying-destructive-changes"></a>

After selecting the list of components to be deployed to the target Salesforce org, go to the **`Destructive Members`** tab.

<figure><img src="../../../../.gitbook/assets/Destructive Changes2.png" alt=""><figcaption></figcaption></figure>

You’ll see the list of metadata components in your target org but not in your source under the **`Post-Destructive Changes`** tab. Select the checkbox next to a component you want to delete, and that component will be deleted when you deploy.

You can also delete some undesired components from your target org by going to **`Modify`** and selecting the components and their destructive natures.

<figure><img src="../../../../.gitbook/assets/Destructive changes1.png" alt=""><figcaption></figcaption></figure>

Use the **`Clear All`** button to clear all the components you've opted for destructive changes (pre- and post-destructive). The **`Reset`** button resets the entire components selection except for the auto-populated components.&#x20;

Similar to standard deployments, test level and validation behaviors are also applied to destructive deployments.

When you deploy destructive changes to production, ARM will do compilation checks to ensure that any other metadata components do not reference the classes being deleted. Code coverage requirement is also enforced as usual.

Finally, the components assigned for destructive changes will be deleted from the target environment when you deploy.

### Destructive Changes on a Custom Object <a href="#destructive-changes-on-a-custom-object" id="destructive-changes-on-a-custom-object"></a>

When you select a custom object for the destructive changes, the following files will be deleted from your target org:

* The custom object file will be deleted.
* The translation file(s) will be deleted.
* The layout file(s) will be deleted.
* The workflow file(s) will be deleted.
* The sharing rule, matching rule, assignment rule, auto-response rule, and escalation rule file(s) will be deleted.
* The trigger file(s) will be deleted.
* The object permissions in profiles and permission sets will be deleted.
* The field permissions in profiles and permission sets will be deleted.

If you need to delete the files mentioned above from your source org, you need to delete them manually.

### Destructive Changes on a Custom Field <a href="#destructive-changes-on-a-custom-field" id="destructive-changes-on-a-custom-field"></a>

When you select a custom field for the destructive changes, the following files will be deleted from your target org:

* The custom field will be deleted from the object and removed from the associated page layouts, reports, record types, and list views.
* The field permissions in profiles and permission sets will be deleted.
