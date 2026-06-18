# MCP Tools

## MCP Server Tools

List of tools available in the IZ MCP server along with the permissions required to run each tool:

### Tools available in both STDIO and HTTP MCP Servers:

| Tool Name                    | Available Version | Description                                                             | Permission                                  |
| ---------------------------- | ----------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| **`getIZApplicationIssues`** | 1.0.0             | Returns the number of issues for a given application                    | **`View Report`**, **`View Organizations`** |
| **`getIZIssuesSummary`**     | 1.0.0             | Returns the total number of issues across all the organizations         | **`View Report`**, **`View Organizations`** |
| **`getIZOrganizations`**     | 1.0.0             | Get all the organizations in IZ Suite                                   | **`View Organization`**                     |
| **`getIZRuleSeverities`**    | 1.0.0             | Get all IZ rule severities in IZ Suite                                  | **`View Quality Rules`**                    |
| **`getIZRuleCategories`**    | 1.0.0             | Get the rule categories in IZ Suite                                     | **`View Quality Rules`**                    |
| **`getIZIssuesDetails`**     | 1.0.0             | Returns all the issues by line number and file across all organizations | **`View Report`**                           |
| **`getIZRules`**             | 1.0.0             | Returns the IZ rules matching the search criteria                       | **`View Quality Rules`**                    |

### Tools available only in STDIO Servers:

| Tool Name          | Available Version | Description                                   | Permission                 |
| ------------------ | ----------------- | --------------------------------------------- | -------------------------- |
| **`iz-code-scan`** | 1.0.0             | Execute IZ Scan Code Analysis for the project | Add role **`IZ Scan CLI`** |

### Tools available as part of automation tasks:

1. Navigate to **`IZ AI`** -> **`Automation Tasks`**
2. Click on any of the listed **`Automation Tasks`** and toggle **`Include in MCP Server`**
3. If selected value is **`Yes`**, the automation task will be available as part of MCP Server tool list.

### See Also

* [Create Agent](../../agent/create-agent.md)
* [Update Agent](../../agent/update-agent.md)
