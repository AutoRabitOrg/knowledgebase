# Destructive Changes

{% hint style="info" %}
The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### About Destructive Changes <a href="#destructive-changes" id="destructive-changes"></a>

Removing dead code is an important software development aspect that is often neglected. In the world of Salesforce and Apex development, removing dead code promotes a cleaner code base, improves test coverage, and helps reduce deployment time. Unused code will slow you down in both the speed of your application and the speed of your developers in their ability to improve the application. Regularly cleaning up unused code is a good thing to do.

#### Types of Destructive Changes <a href="#types-of-destructive-changes" id="types-of-destructive-changes"></a>

1. **`Post Destructive Changes:`** The post Destructive Changes feature will delete the unwanted fields or metadata components from your destination Salesforce org when the deployment is successful.
2. **`Pre Destructive Changes:`** Pre Destructive Changes will delete unwanted fields or metadata components from your destination Salesforce org before the deployments begin.

### Deploying Destructive Changes <a href="#deploying-destructive-changes" id="deploying-destructive-changes"></a>

After selecting the list of components to be deployed to the target Salesforce org, go to the **`Destructive Items`** tab.

<figure><img src="../../../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

You’ll see the list of metadata components in your target org but not in your source under the **`Post-Destructive Changes`** tab. Select the checkbox next to a component you want to delete, and that component will be deleted when you deploy.

You can also delete some undesired components from your target org by going to **`Modify`** and selecting the components and their destructive natures.

<figure><img src="../../../../.gitbook/assets/image (66).png" alt="" width="485"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

Use the **`Clear All`** button to clear all the components you've opted for destructive changes (pre- and post-destructive). The **`Reset`** button resets the entire components selection except for the auto-populated components.&#x20;

Similar to standard deployments, test level and validation behaviors are also applied to destructive deployments.

When you deploy destructive changes to production, ARM will do compilation checks to ensure that any other metadata components do not reference the classes being deleted. Code coverage requirement is also enforced as usual.

Finally, the components assigned for destructive changes will be deleted from the target environment when you deploy.

### Destructive Changes on a Custom Object <a href="#destructive-changes-on-a-custom-object" id="destructive-changes-on-a-custom-object"></a>

When you select a custom object for the destructive changes, the following files will get deleted from your target org:

* The custom object file will be deleted.
* The translation file(s) will be deleted.
* The layout file(s) will be deleted.
* The workflow file(s) will be deleted.
* The sharing rule, matching rule, assignment rule, auto-response rule, and escalation rule file(s) will be deleted.
* The trigger file(s) will be deleted.
* The object permissions in profiles and permission sets will be deleted.
* The field permissions in profiles and permission sets will be deleted.

If you need to delete the files mentioned above from your source org, you need to get them deleted manually.

### Destructive Changes on a Custom Field <a href="#destructive-changes-on-a-custom-field" id="destructive-changes-on-a-custom-field"></a>

When you select a custom field for the destructive changes, the following files will get deleted from your target org:

* The custom field will be deleted from the object and removed from the associated page layouts, reports, record types, and list views.
* The field permissions in profiles and permission sets will be deleted.
