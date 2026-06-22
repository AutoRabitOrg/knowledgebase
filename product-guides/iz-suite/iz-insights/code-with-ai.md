# Code with AI

The following section outlines the steps to generate code using IZ AI.

### New Code Generation

* Navigate to **`Code With AI`** -> **`Generate Code`**.
* Choose an **`Implementation Type`** based on your requirement:

| Implementation Type               | Description                                                                                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`Generate Mule Application`**   | Generates a MuleSoft application based on the provided requirements, including flows, configurations, and integrations.                                            |
| **`Generate API Specification`**  | Automatically creates an API specification (RAML/OAS) with endpoints, request/response models, and sample payloads based on user input.                            |
| **`Implement API Specification`** | Generates backend logic and connectors for an existing API specification, with optional support for generating dependent APIs.                                     |
| **`IZ Eye Insights`**             | Provides insights and recommendations for application design, including generation of HLDs, LLDs, and related artifacts for applications on the Anypoint Platform. |
| **`IZ Scan Insights`**            | Offers insights and recommendations for applications scanned via SCM or local sources, including generation of HLDs and LLDs.                                      |

* Enter a name for the project and select the destination where it should be stored.
* Choose the Organization and provide the prompt required for code generation.
* After submission, you can view the code-generation progress and details under the **`Log Overview`** and **`Diagnostics`** tabs.

### Code Generation using Chat Bot

* Navigate to **`Code With AI`** -> **`AI Operations`**. All the tasks available in **`Automation Tasks`** will be available as part of the Chat Bot
* Enter the required prompt to perform appropriate actions. A an example is described below -
  * Prompt **`All Tasks`** -&#x20;
  * Choose the required task from the list of available **`Automation Tasks`**. Appropriate questions will be prompted based on the task selected. Platform where the generated code should be stored.&#x20;
  * Choose the organization&#x20;
  * Enter the prompt for the AI to generated the code&#x20;

### See Also

* [Automation Tasks](automation-tasks.md)
* [Automation Task Logs](automation-task-logs.md)
