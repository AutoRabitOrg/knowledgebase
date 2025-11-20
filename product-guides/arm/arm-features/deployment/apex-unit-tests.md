# Apex Unit Tests

### What are Apex Unit Tests? <a href="#what-are-apex-unit-tests" id="what-are-apex-unit-tests"></a>

To facilitate the development of robust, error-free code, Apex supports the creation and execution of unit tests. Unit tests are class methods that verify whether a particular code is working correctly.

### What to Test in Apex? <a href="#what-to-test-in-apex" id="what-to-test-in-apex"></a>

Salesforce recommends the following components that need to be tested:

1. **Single Records:** This includes testing to verify that a single record produces the correct, expected result.
2. **Bulk Records:** Any apex code, whether a trigger, a class, or an extension, may be used for 1 to 200 records. We must test not only the single record case but the bulk cases as well.
3. **Positive scenarios:** This type of component testing expects a system to save a record without error.
4. **Negative scenarios:** This type of component testing expects a system to give an error.
5. **Restricted User:** Test whether users with restricted access to the objects used in the code see the expected behavior, i.e., whether they can run the code or receive error messages.

### Choose which Tests to Run <a href="#choose-which-tests-to-run" id="choose-which-tests-to-run"></a>

The following test options are available when you deploy or commit or use CI jobs:

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="418"><figcaption></figcaption></figure>

* **`No Test Run:`** No tests are run. This test level applies only to deployments to development environments like Sandbox, Developer Edition, or trial organizations. This test level is the default for development environments.
* **`Run Specified Tests:`** Only the tests that you specify are run. Provide the names of test classes in a comma-separated list.Make sure for the runTests parameter, and you're specifying the test class names separated by ",". The runTests parameter will be used only when the test level is set to **`Run Specified Tests`**.\
  Code coverage requirements differ from the default coverage requirements when using this test level. The executed tests must cover each class and trigger in the deployment package for a minimum of 75% code coverage. This coverage is computed for each class and trigger individually and differs from the overall coverage percentage.
* **`Run Local Tests:`** All tests in your organization are run, except the ones that originate from installed managed packages. This test level is the default for production deployments that include Apex classes or triggers.
* **`Run All Tests In Org:`** All tests are run. The tests include all tests in your organization, including tests of managed packages.
* **`Run Tests Based On Changes:`** This option will identify apex test classes from your source package in addition to the default configured apex classes and run the identified tests to the destination environment. Also, if you want to include the newly identified apex classes from the packages in your [default apex test class configuration](../../troubleshoot/how-tos/default-apex-class-configuration.md) list, please check the "**`Do you want us to update the test classes`**" checkbox.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="413"><figcaption></figcaption></figure>

{% hint style="info" %}
**Points to Note**:&#x20;

1. Only CI Jobs have the "**`Do you want us to update the test classes`**" checkbox enabled. This feature is yet to be implemented in other modules.
2. With our current "Run Tests Based on Changes" functionality, we still expect a test class for a wrapper class with appropriate code coverage, even if the wrapper class doesn't contain any executable code. Otherwise, we will encounter a code coverage error:

_Code Coverage Failures:_\
&#xNAN;_&#x43;lass: TransactionHistoryActionParameters -- Test coverage of selected Apex Class is 0%, at least 75% test coverage is required_\
&#xNAN;_\*\*\*\*\*\*\*\*\*\*\* DEPLOYMENT FAILED \*\*\*\*\*\*\*\*\*\*\*_
{% endhint %}

* **`User Salesforce Defaults:`** Keeps the default behavior for all tests. In the sandbox, no tests are executed. All local tests are executed in the production if they contain Apex classes or triggers. Local tests are all tests, except the ones that originate from managed packages. If your package doesn’t contain Apex components, no tests are run.

{% hint style="info" %}
**Point to Note**:

1. Please make sure to execute all apex tests before configuring this option. This allows you to configure the mapping between the main class and the test class.
2. If you have cleared the last run history in your destination org, you must again execute run all tests. If not done, the dependent test execution will fail.
3. If you have refreshed your sandbox, then again you are required to execute run all tests. If not done, the dependent test execution will fail.
4. If the test classes do not exist in the package, the test level is configured based on the Run local Tests.
{% endhint %}

### Where can I choose the Apex Tests level in ARM? <a href="#where-can-i-choose-the-apex-tests-level-in-arm" id="where-can-i-choose-the-apex-tests-level-in-arm"></a>

#### During EZ-Commit validation <a href="#during-ezcommit-validation" id="during-ezcommit-validation"></a>

In the **`Submit for Validation`** screen, select the **`Validate Deployment`** checkbox and choose an org to validate your commit. Next, choose the test level of validation from the **`Apex Test Level`** dropdown.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### During EZ-Merge Prevalidation <a href="#during-ezmerge-prevalidation" id="during-ezmerge-prevalidation"></a>

In the **`New Merge`** screen and under the **`Prevalidate Merge`** section, select the **`Validate Deployment`** checkbox and choose an org to validate your merge. Next, choose the test level of validation from the **`Apex Test Level`** dropdown.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="371"><figcaption></figcaption></figure>

#### During Deployment <a href="#during-deployment" id="during-deployment"></a>

In the **`Deployment Settings`** screen, you can choose the apex test level to validate the deployment.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### During Continuous Integration (CI) Jobs <a href="#during-continuous-integration-ci-jobs" id="during-continuous-integration-ci-jobs"></a>

You can set the apex test level when creating or editing a CI job in the **New/Edit CI job** screen under the **`Deploy`** section.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For more information on Apex unit tests, Refer to the [Salesforce Trailhead](https://trailhead.salesforce.com/en/modules/apex_testing/units/apex_testing_intro) module on Apex test level testing.
