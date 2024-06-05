# Salesforce Enhanced Domains Issues

The Salesforce Enhanced Domains feature was able to be rolled out to Sandboxes on August 26th 2022 and will be generally available on September 9th for all environments.

If your CodeScan Cloud Salesforce project was linked to a Sandbox or Org that this feature is enabled in, you may be experiencing the error:

**Salesforce retured an unexpected result**

In this case, you will need to reattach your project analysis.

[CodeScan Cloud](https://www.codescan.io/products/cloud/) allows you to do this _without erasing_ the historical data present in your project.

To fix the above errors, first you need to delete the **Analysis Project**, to delete follow the steps below:

1. Go to your **Project** and navigate to the **Project Settings > Project Analysis** page.

<figure><img src="../../../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

2. Click on **Delete Analysis**.

<figure><img src="../../../../.gitbook/assets/image (441).png" alt=""><figcaption></figcaption></figure>

3. Make sure you do not have the "**Delete this project also?**" box checked. This will delete your history and is not reversible. Click **Delete Analysis**.

<figure><img src="../../../../.gitbook/assets/image (442).png" alt=""><figcaption></figcaption></figure>

4. Now use the **Attach Analysis Project** button at the top right of the screen to re-add the link.

<figure><img src="../../../../.gitbook/assets/image (443).png" alt=""><figcaption></figcaption></figure>

5. Configure the project and run the analysis.
