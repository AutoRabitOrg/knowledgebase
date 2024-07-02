# AccelQ

### AccelQ: Overview

With every release, AutoRABIT is looking to improve its application quality, achieve in-sprint automation to align with continuous delivery.&#x20;

AccelQ's Quality Driven Development (QDD) implements an innovative Agile Quality Life Cycle approach, integrating the usual test silos into an end-to-end automated process. AccelQ is built on a cognitive core engine bringing the power of predictive analytics in scenario design, autonomics in test automation, and adaptive change management in traceability.

### Integrating AccelQ as a Plugin into AutoRABIT

To integrate AccelQ as a plugin with AutoRABIT, it does require some steps in AutoRABIT to get it configured. The below section will help you out to get AccelQ configured in AutoRABIT in easy steps.

{% hint style="info" %}
**Important Note:** AccelQ status polds only for 10 minutes.
{% endhint %}

#### Step 1: Store your user's AccelQ credential in AutoRABIT

This is an initial step where the user's AccelQ credential such as username and password is stored in AutoRABIT.

1. Log in to your AutoRABIT account.
2. Go to the **Credentials** tab.
3. Click on **Create Credential** button from the right navigation bar.

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

4. On the next pop-up screen, give a **credential name**.
5. Choose the **Credential Type** as **"User name with Password."**
6. Enter your username and **AccelQ API token** in the **Password** field.
7. Please double-check that you use your AccelQ username instead of the email address that you use to log in to AccelQ.
8. Click **Save**.

<figure><img src="../../../.gitbook/assets/image (9).png" alt="" width="416"><figcaption></figcaption></figure>

#### Step 2: Integrate AccelQ with AutoRABIT

1. Go to the **My Account** page.
2. In the **Plugins** section, select **AccelQ** under **Test Types**.

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

3.  Fill in the below details to integrate AccelQ:

    * **URL:** Enter the AccelQ registered endpoint URL. For ex- poc.accelq.io
    * **Tenant Code:** Enter the Tenant code received from AccelQ. If you're not aware of this, you can retrieve your Tenant code from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ.

    <figure><img src="../../../.gitbook/assets/image (11).png" alt="" width="563"><figcaption></figcaption></figure>

    * **Select Credential:** Select the user's credential registered as mentioned in Step 1.

    <figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
4. Once you're done filling the AccelQ fields, click on **Save** to complete the integration process.&#x20;

### Adding AccelQ configuration in CI Job

1. Go to the **New CI Job** screen.

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

2.  Select any one of the below criteria for your CI job:

    * Deploy from Salesforce Org
    * Deploy from Version Control
    * Deploy from Salesforce Org with a Version Control backup
    * Deploy SFDX source from Version Control
    * Run Test Automation Scripts
    * Install an Unlocked Package from a Version Control Branch

    <figure><img src="../../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
3. Give the job a descriptive name in the **CI Job Name** field.
4. Go to the **Test** section. Here you will need to select _AccelQ_ to run the functional test cases to test the functionality of the code being deployed to production.
5. Select **Fetch Test Cases From** as **AccelQ**.

<figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

6.  Enter your **Project Name** and the **Test Job Name.**

    * You can find your project name from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ. Similarly, the test job name will be available in the Job section on AccelQ.

    <figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
7. Set the **parameter(s)** for your AccelQ test cases as shown below.

<figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

8. Click **Save**.
9. So, once the configured CI job is run and the build is triggered, AccelQ will review the code changes and functional review information can be found in the **CI Job Result** under the **Functional Tests** section. Here, you can find the status of the functional test done along with other details such as the number of components that successfully got reviewed, the number of components failed to review, components that are about to get reviewed or are in the queue.

<figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

10. To view the detailed success or failure report, click on the link available under Functional Tests.

    * **Success Report:**

    <figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

    * **Failure Report:**

    <figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
11. Click on **Error Details** for each test case being reviewed to view the error report.

<figure><img src="../../../.gitbook/assets/image (23).png" alt="" width="454"><figcaption></figcaption></figure>

### Adding AccelQ configuration in the 'Deployment Setting' screen

1. In the **Deployment Setting** screen, while performing a new deployment, you need to select **AccelQ** to fetch the test cases.

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

2.  Enter your **Project Name** and the **Test Job Name**.

    <figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="419"><figcaption></figcaption></figure>

    * You can find your project name from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ.

    <figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

    * Similarly, the test job name will be available in the Job section on AccelQ.

    <figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>
3. Click **Save**.
4. When the deployment is executed, you can find the AccelQ test cases report in the **Deployment History** screen.Click on the **Test Results** button for the detailed AccelQ report.

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>
