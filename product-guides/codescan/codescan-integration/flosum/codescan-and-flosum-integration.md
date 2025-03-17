# CodeScan and Flosum Integration

## About Flosum <a href="#about-flosum" id="about-flosum"></a>

**Flosum** is a release management tool for the Salesforce platform. Flosum users can now integrate CodeScan in their deployments to achieve secure, error-free releases.

{% hint style="info" %}
**Note**: Flosum cannot be integrated with On-Premises/Self-Hosted versions of CodeScan.
{% endhint %}

## How to Integrate Flosum with CodeScan <a href="#how-to-integrate-flosum-with-codescan" id="how-to-integrate-flosum-with-codescan"></a>

1. **Install CodeScan.**&#x20;
   1. Obtain the CodeScan package URL from your Customer Success Manager.&#x20;
   2. Install the CodeScan package in your Flosum organization.&#x20;
   3. After installation, click on the app launcher and open Flosum-CodeScan.

<figure><img src="../../../../.gitbook/assets/image (509).png" alt=""><figcaption></figcaption></figure>

2.  **Authorize** CodeScan.

    *   Go to the **Authorization** tab in Flosum-CodeScan.\


        <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



    * Enter the following details to sync CodeScan with your Flosum organization.
      * **CodeScan URL**: Use the appropriate URL for your CodeScan instance:
        * **US** region: [_https://app.codescan.io_](https://app.codescan.io)
        * **EU** region: [_https://app-eu.codescan.io_](https://app-eu.codescan.io)
        * **AUS** region: [_https://app-aus.codescan.io_](https://app-aus.codescan.io)
      * **Organization Key**: Obtain this key from your hosted CodeScan instance.
      *   **Token**: Generate a token by navigating to **User > My Account > Security** in CodeScan. Set the token expiration or choose "no expiration."\


          <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **Flosum Branch Configuration**:
   1. On the **Branch Configuration** tab, choose the branch you want to scan.
      * Select all or specific component types from the six supported profiles:
        * Aura
        * Lightning
        * Apex Class
        * Apex Triggers
        * Apex Page
        * Component
      *   Check the boxes for the components you want to scan and click **Save**.\


          <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
4. **Finalize Setup**:&#x20;
   *   Log in to CodeScan and confirm that your branch is populated in the CodeScan server. \


       <figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
   *   Select the branch, click **Add Analysis Project**, and attach it as a webhook.\


       <figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

       <figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Initiating a Scan on the Flosum Branch

1. **Branch Sync**:
   * Add the **Branch Sync** lightning component to your branch's Lightning record page.
   *   Click the **Branch Sync** button to trigger the static code analysis.\


       <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2. **View Project Analysis**:
   *   Go to the **Project Analysis** page to see the analysis in progress.\


       <figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Your Flosum-CodeScan integration is complete!



