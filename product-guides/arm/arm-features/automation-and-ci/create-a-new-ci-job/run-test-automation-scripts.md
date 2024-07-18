# Run Test Automation Scripts

{% hint style="info" %}
**Important Note**: The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your chrome/firefox browser.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Load your test cases irrespective of the build or deployment got failed and fire them on a Salesforce Org of your choice. These tests can be in form of Selenium scripts (Maven/ non-Maven) hosted on the ARM test repository (TAF) or in your Version Control System. You can even invoke integrations to other Test Automation products such as Provar, AccelQ using this option.&#x20;

## Procedure <a href="#procedure" id="procedure"></a>

1. Login to your AutoRABIT account.
2. From the top navigation pane, navigate to **Create New > New CI Job**.

<figure><img src="../../../../../.gitbook/assets/image (58) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Choose the tile: **Run Test Automation Scripts**

<figure><img src="../../../../../.gitbook/assets/image (59) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, give the job a descriptive name in the **Job Name** field.
5. Add a brief **description** of the current CI job.
6. To group your CI job for easier identification, choose the group from the dropdown. You can create a new group using the **"+"** symbol and assign your current and further CI jobs to such a group.
7. Here, the user interface is separated into different sections, we will cover each one of them separately.

### Tests <a href="#tests" id="tests"></a>

Before proceeding with the CI Job operation, you may like to run the functional test cases in order to test the functionality of the code being deployed to the Destination Environment. Therefore, select the manner in which you like to fetch the test cases.

There are different ways to fetch the Test cases:

* TAF Labels
* Version Control
* AccelQ (if AccelQ plugin is installed in AutoRABIT)
* Provar (if Provar plugin is installed in AutoRABIT)

<figure><img src="../../../../../.gitbook/assets/image (60) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1.  **TAF Labels:** The test labels that are present in the AutoRABIT TAF module get displayed. Select the test cases as per your requirement.

    * **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    * **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    * **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (61) (1) (1) (1).png" alt="" width="379"><figcaption></figcaption></figure>
2.  **Version Control:** The test cases committed to a branch in version control are displayed.

    * Select the **Version Control Repository** type.
    * Select the **Repository** and the **Branch**.&#x20;
    * Select the way you would like to run your test cases, i.e., TAF, Selenium Maven, or Selenium Non-Maven.
      1. For the **Selenium Maven** test type, you need to enter the test case root path in the **Test Case Root Path** field. Also, specify the goals.
      2. For the **Selenium Non-Maven** test type, you need to choose the **Execution Type**, and enter the test case root path in the **Test Case Root Path** field.

    **Additional options:**

    1. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. In the recent release, the user will be able to proceed with the test even if the deployment gets failed.
    2. **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (62) (1) (1) (1).png" alt="" width="547"><figcaption></figcaption></figure>
3. **AccelQ:** Select the Fetch Test Cases as **'AccelQ'**.  Enter your **Project Name** and the **Test Job Name** and set the **parameter(s)** for your AccelQ test.

<figure><img src="../../../../../.gitbook/assets/image (63) (1) (1) (1).png" alt="" width="467"><figcaption></figcaption></figure>

If you're not aware of where to find your **Project Name** and **Test Job name** in AccelQ, you can find your Project name from the **"AUTH PROPERTIES"** section in the User's Profile card on AccelQ. Similarly, the Test Job name will be available in the Job section on AccelQ.

<figure><img src="../../../../../.gitbook/assets/image (64) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (65) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4.  **Provar:** Select Fetch Test Cases From as **'Provar'**.

    * Select your **Version Control Repository** and the **Branch** and provide the **provar test cases path**.
    * **Test Cases Root Path**: Enter the test case root path till the **.testproject** file
    * **Test Cases Execution Path:** Enter the test cases execution path here. **Ex:** tests/sample and if not specified, all the test cases from the **'tests'** folder will get executed.

    **Additional options:**

    1. **Stop Deployment if Test cases fail to compile:** This prevents the deployment to proceed if any errors/warnings occur during running the test cases.
    2. **Run Test even when the Deployment fails:** Till now, the user was able to run the test module (Selenium, Provar, or AccelQ) only if the deploy stage is successful. This leads to failure of the deployment of the test cases fail in the 'test' stage. With the 19.3 release, the user will be able to proceed with the test even if the deployment gets failed.
    3. **Test Browsers:** Cross-browser compatibility testing needs to be performed to ensure if the rendering of data is correct across multiple browsers. Select the browser in which you would like to run the test cases.

    <figure><img src="../../../../../.gitbook/assets/image (66) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Choose Target <a href="#choose-target" id="choose-target"></a>

In this section, select the Salesforce Org where the automated test cases will execute. If you are running a Provar Test script, the selected Salesforce Org will be used for pre-authentication.

<figure><img src="../../../../../.gitbook/assets/image (67) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Schedule  <a href="#schedule" id="schedule"></a>

Allows you to schedule the process at which it must run.

1. **Daily:** The process will run every day at the scheduled time or time interval set.
2. **Weekly:** The process will run weekly on the scheduled day and time.&#x20;
3. **No schedule:** The process will only get saved, and you can run it when required.&#x20;

For more information on **Credential Usage** for different types of CI jobs, refer [HERE](../../../../../fundamentals/faq/ci-jobs.md).

### What Next? <a href="#what-next" id="what-next"></a>

Once you filled in all the details for your CI job, you will be redirected to the [CI Job Results](../../ncino/feature-ci-jobs/ci-job-results.md) page where you can trigger a build for your CI job.
