# Reattaching Bitbucket Projects

At AutoRABIT, we have made some changes to make our Bitbucket project webhooks more secure. To take advantage of this change, Bitbucket projects that were created in CodeScan need to be reattached.

[CodeScan Cloud](https://www.codescan.io/products/cloud/) allows you to do this _without erasing_ the historical data present in your project. It will only reconnect the CodeScan project with the Bitbucket repository.

{% hint style="info" %}
This only affects projects created in CodeScan with our internal integration.

This **DOES NOT** include:

* Projects created from Bitbucket pipelines
* Projects being cloned from Bitbucket and scanned from a separate CI platform
{% endhint %}

Follow these steps to reattach your project analysis:

1. Open your Bitbucket **project.**
2. Navigate to the **Project Settings > Project Analysis** page.

<figure><img src="../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

3. Click on **Delete Analysis**.

<figure><img src="../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

4. Make sure you do not have the "**Delete this project also?**" box checked. This will delete your history and is not reversible. Click **Delete Analysis**.

<figure><img src="../../../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

5. Now use the **Attach Analysis Project** button at the top right of the screen to re-add the link.

<figure><img src="../../../../.gitbook/assets/image (447).png" alt=""><figcaption></figcaption></figure>

6. You will now see a new popup window. Select the required option from the options given (e.g., Bitbucket).

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. Once you select **Bitbucket**, it will redirect you to the **Bitbucket login page**. Validate your credentials and click on **Login**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>



8. Choose your **repository**.&#x20;
9. Make sure you select the checkbox under **Check Pull Requests**.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

10. Once you fill out all the details in the popup window, select **Add and Run Now**.
11. This triggers the project analysis along with the project being added under your CodeScan organization.
