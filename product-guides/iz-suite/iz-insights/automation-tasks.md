# Automation Tasks

The following section describes the steps to create AI-driven automated tasks for AI Action Ops using IZ Insights.

### Creating an Automation Task

* Navigate to **`IZ Insights`** -> **`Generate Automation`**.
* Enter the name of the automation task and select the appropriate category:
  * Dev
  * Ops
  * Manager
* Select the task type:
  * utility - Mainly used as a utility which will be invoked by the **`Main`** task type
  * main - Main task
* Configure the following options:
  * **`Include in MCP Server`** – Indicates whether the task should be available as a tool in the MCP server.
  * **`Requires Manual Intervention`** – Indicates whether the task requires human approval or interaction during execution.
* Enter the task parameters in JSON format. Example -

```json
{
  "type": "object",
  "required": [
    "keyword"
  ],
  "properties": {
    "keyword": {
      "type": "string",
      "description": "Keyword to search Organizations. To search for all Organizations assign an empty string to this parameter. Also display a message saying only top 10 search results are being shown if the result size is equal to 10."
    }
  }
}
```

* Upload the required Postman collection that will be executed by the automation task.

### Run Automation Task

* Navigate to **IZ Insights** and choose **Run Automation Task** from the action menu corresponding to the automation task.
* Automation tasks can be executed in two modes:
  * **`Basic`** – Provide task parameters through a simple form.
  * **`Advanced`** – Provide the full parameter definition in JSON format.
* After submission, the execution logs can be viewed under **`Automation Task Logs`**.

### Including the Task in MCP Server

* Navigate to **IZ Insights** and choose **Task Settings** from the action menu corresponding to the automation task.
* Select the appropriate option to either include or exclude the task in MCP Server and **`Submit`**

### Enabling Manual Intervention

* Navigate to **IZ Insights** and choose **Task Settings** from the action menu corresponding to the automation task.
* Select the appropriate option to either enable or disable manual intervention and **`Submit`**

### See Also

* Code With AI
* Automation Task Logs
