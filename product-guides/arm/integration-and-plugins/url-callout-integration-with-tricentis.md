---
description: How AutoRABIT Uses the URL Callout to Integrate with Tricentis
---

# URL Callout Integration with Tricentis

Overview&#x20;

One of the key DevSecOps integrations available in ARM is Tricentis, a leading provider of continuous testing tools, to streamline the testing process in CI/CD pipelines. The integration between AutoRABIT and Tricentis is achieved through URL callouts, which allow these two platforms to communicate and trigger automated testing at various stages of the release process.&#x20;

This article will walk through how AutoRABIT leverages the URL callout to integrate with Tricentis, ensuring seamless automated testing as part of the release lifecycle.&#x20;

URL Callout in AutoRABIT&#x20;

In AutoRABIT, a URL callout is a configuration that allows AutoRABIT to send HTTP requests to external systems or services like Tricentis. This communication is initiated when specific conditions are met during the release or deployment process, typically when a new build is triggered or changes are ready to be tested.&#x20;

The callout allows AutoRABIT to:&#x20;

1. Trigger Automated Tests: When a new build or release package is ready, AutoRABIT sends a request to Tricentis to initiate the testing process.&#x20;
2. Pass Metadata and Configuration: Along with the trigger, the URL callout can pass essential information, such as the build version, specific test cases to run, and relevant metadata.&#x20;
3. Retrieve Test Results: After the tests are completed, Tricentis can send results back to AutoRABIT.&#x20;

[Please use the steps in this article to setup the Callout URL in ARM.](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/automation-and-ci/configure-callout-url) Here are a few Tricentis Specific things to keep in mind. &#x20;

1. Define the URL Callout:&#x20;
2. Enter the endpoint URL provided by Tricentis, which is typically a REST API URL where AutoRABIT will send the HTTP requests.&#x20;
3. Configure Parameters:&#x20;
4. Configure any necessary headers or authentication tokens required for Tricentis to authorize the request from AutoRABIT.&#x20;
5. Map Data and Payload:&#x20;
6. Define the payload, which will include the relevant metadata such as build numbers, specific test suites, or other identifiers that Tricentis needs to &#x20;

Once Tricentis completes the testing, it can send back the test results using a callback URL or a direct API response, which AutoRABIT can capture. The following steps summarize how AutoRABIT handles the test results:&#x20;

* Notification and Reporting: AutoRABIT can be set up to notify teams (via email or other communication channels) with the results of the test execution. These results can also be logged for auditing and future reference.&#x20;

Benefits of AutoRABIT-Tricentis Integration&#x20;

* Increased Automation: The seamless integration reduces the manual effort required for testing, enabling continuous delivery pipelines with high automation.&#x20;
* Improved Testing Efficiency: By automatically triggering relevant test cases in Tricentis based on build metadata, you ensure that testing is timely and targeted.&#x20;
* Faster Feedback Loops: Developers get real-time feedback on the quality of their code, helping to reduce the time spent on finding and fixing bugs late in the release cycle.&#x20;
* Enhanced Compliance and Reporting: All testing activities are tracked and logged in AutoRABIT, supporting compliance efforts and providing a clear audit trail.&#x20;

Conclusion&#x20;

AutoRABIT’s integration with Tricentis via URL callouts ensures that testing becomes an integrated, automated part of the release process. This approach allows organizations to leverage the full power of Tricentis’s testing suite while benefiting from the release management and automation capabilities of AutoRABIT.&#x20;

For more detailed information on setting up this integration, refer to the AutoRABIT and Tricentis documentation or consult with your AutoRABIT customer success manager.&#x20;

&#x20;
