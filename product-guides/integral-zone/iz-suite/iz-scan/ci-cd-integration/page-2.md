# Mule Coverage Reports

## Mule - Code Coverage Reports

{% hint style="warning" %}
* IZ Scan does not execute munit tests or produce coverage reports. Instead, it solely imports pre-generated reports in json format.
{% endhint %}

### How to generate coverage report

1. Coverage report should be configured in JSON format for IZ Scan to scan and upload the report. Refer [Maven Configuration for Coverage](https://docs.mulesoft.com/munit/latest/coverage-maven-concept)
2. Before scanning the project, make sure MUnit test cases are executed and coverage report is generated

### Coverage report upload

1. IZ Scan parses the JSON coverage report from default path **`target/site/munit/coverage/munit-coverage.json`**. No additional configuration parameters are required to enable scanning of coverage reports
2.  On successful analysis, coverage report will be uploaded to server with following statistics -

    1. Overall coverage percentage - Click on the actions and select **`Code Coverage Report`**&#x20;

    <figure><img src="../../../../../.gitbook/assets/iz_overall_code_coverage.png" alt="" width="563"><figcaption></figcaption></figure>



    b. File and flow level coverage percentage&#x20;



    <figure><img src="../../../../../.gitbook/assets/iz_file_flow_coverage (2).png" alt="" width="563"><figcaption></figcaption></figure>



&#x20;      c. Uncovered and covered lines&#x20;

<figure><img src="../../../../../.gitbook/assets/iz_line_coverage (1).png" alt="" width="563"><figcaption></figcaption></figure>

### See Also

* [Install IZ Scan for Cloud](using-iz-scan-cli.md)
* Install IZ Scan for Desktop
* Aborting Builds

