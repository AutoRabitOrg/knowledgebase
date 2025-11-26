# Run Test Automation Scripts

{% hint style="info" %}
**Important Note**: The **CI JOBS** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Run your automated test cases independently of the build or deployment outcome, targeting any Salesforce Org. Tests may include Selenium scripts (Maven/non-Maven) stored in your Version Control System. You can also integrate external test automation tools like Provar and AccelQ.

## Procedure <a href="#procedure" id="procedure"></a>

1. Log in to your AutoRABIT account.
2. From the top navigation, go to **Create New > New CI Job**.
3. Select the tile: **Run Test Automation Scripts**.
4. Provide a descriptive name in the **Job Name** field.
5. Add a brief **description** for the CI job.
6. Select or create a **Group** to help organize your CI jobs.

The interface is split into sections, detailed below.

### Tests <a href="#tests" id="tests"></a>

Choose how to fetch the test cases:

* **Version Control**
* **AccelQ** (requires plugin)
* **Provar** (requires plugin)

#### Version Control

Configure tests committed to a VCS branch.

Steps:

1. Choose **Repository Type**, **Repository**, and **Branch**.
2. Select test execution mode:
   * **Selenium Maven**: Provide **Test Case Root Path** and **Goals**
   * **Selenium Non-Maven**: Specify **Execution Type** and **Test Case Root Path**

Options:

* **Run Test Even When Deployment Fails**
* **Test Browsers**

#### AccelQ

Steps:

1. Choose **AccelQ** as the fetch type.
2. Provide your **Project Name** and **Test Job Name**
3. Set any required **parameters**

> Refer to AccelQ's **AUTH PROPERTIES** for Project Name and the **Job** section for Test Job Name.

#### Provar

Steps:

1. Select **Repository** and **Branch**
2. Enter:
   * **Test Cases Root Path** (up to `.testproject`)
   * **Test Cases Execution Path** (e.g., `tests/sample`)

Options:

* **Stop Deployment if Test Cases Fail to Compile**
* **Run Test Even When Deployment Fails**
* **Test Browsers**

### Choose Target <a href="#choose-target" id="choose-target"></a>

Select the Salesforce Org where test cases will run. This org will be pre-authenticated if using Provar.

### Schedule <a href="#schedule" id="schedule"></a>

Configure when the job should run:

* **Daily**: Runs daily at set time
* **Weekly**: Runs weekly on selected days
* **No Schedule**: Save job to run manually

> For credential usage info in CI jobs, refer to [this FAQ](../../../troubleshoot/arm-faqs/ci-jobs.md).

### What Next? <a href="#what-next" id="what-next"></a>

Once setup is complete, you'll be redirected to the [CI Job Results](/broken/pages/empQ5i682Aq3NuuUalqa) page where you can trigger a build for this CI job.
