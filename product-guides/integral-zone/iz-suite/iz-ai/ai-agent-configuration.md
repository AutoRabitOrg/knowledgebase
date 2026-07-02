# AI Agent Configuration

The following section outlines the steps required to configure the AI agent.

### Agent Settings

* Navigate to **`Global Settings`** -> Search for **`AI Agent Settings`** and click on **`Configure Settings`** action item.
* Update the following settings based on the requirement -

| Settings key                         | Description                                                                                                                                                                                                                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`AI_AGENT_API_KEY`**               | The authentication key issued by the AI agent provider.                                                                                                                                                                                                                                                 |
| **`AI_PROVIDER`**                    | The name of the AI provider (e.g., **`ANTHROPIC`**, **`OPENAI`**).                                                                                                                                                                                                                                      |
| **`AI_MODEL`**                       | The specific model of the configured **`AI PROVIDER`** that will be used for code generation.                                                                                                                                                                                                           |
| **`VECTOR_DB_URL`**                  | The endpoint URL of the vector database service.                                                                                                                                                                                                                                                        |
| **`VECTOR_DB_TOKEN`**                | The authentication token used to access the vector database.                                                                                                                                                                                                                                            |
| **`VECTOR_DB_SEARCH_TOKEN`**         | The token used specifically for search/query operations in the vector database.                                                                                                                                                                                                                         |
| **`MULE_VECTOR_DB_COLLECTION_NAME`** | The name of the vector database collection containing MuleSoft related embeddings.                                                                                                                                                                                                                      |
| **`API_VECTOR_DB_COLLECTION_NAME`**  | The name of the vector database collection containing API related embeddings..                                                                                                                                                                                                                          |
| **`MULE_AGENT_VALIDATOR_CMD`**       | The maven command to be executed for validating the project.                                                                                                                                                                                                                                            |
| **`MAVEN_SETTINGS_XML`**             | The Maven settings.xml configuration used for dependency resolution and repository authentication.                                                                                                                                                                                                      |
| **`MULE_SPECIFICATIONS`**            | Organization specific guidelines and standards that the AI agent must follow while generating the mule project.                                                                                                                                                                                         |
| **`API_SPECIFICATIONS`**             | Organization specific guidelines and standards that the AI agent must follow while generating the API specification.                                                                                                                                                                                    |
| **`DOC_SPECIFICATIONS`**             | Organization specific guidelines and standards that the AI agent must follow while generating the documentation.                                                                                                                                                                                        |
| **`<LANGUAGE>_TEMPLATE_URL`**        | Location of the initial template to be used for generating the project. For Example - **`MULE_API_PROJECT_TEMPLATE_URL`** represents the template to be used for generating the mule project. This setting is application only while generating new projects and not while editing an existing project. |

* Save the configuration.

### See Also

* [Automation Tasks](automation-tasks.md)
* [Automation Task Logs](automation-task-logs.md)
