# MCP Tools

## MCP Server Tools

List of tools available in the IZ MCP server along with the permissions required to run each tool:

### Tools available in both STDIO and HTTP MCP Servers:



| Tool Name                               | Available Version | Description                                                                                                                                           | Permission                                               |
| --------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **`searchFalconApplications`**          | 26.4.1            | Finds IZ Scan and IZ Eye applications by name or application key and returns their id, organization, environment, module and last scan time.          | Access to the application's organization and environment |
| **`getFalconIssues`**                   | 26.4.1            | Lists issues with rule, severity, category, message, file and line, filtered by application, organization, product, severity, category, rule or text. | Access to the application's organization and environment |
| **`getFalconIssuesGrouped`**            | 26.4.1            | Counts issues and sums remediation effort, grouped by one or more fields such as organization, rule, file or severity, largest groups first.          | Access to the application's organization and environment |
| **`getFalconRuleDetails`**              | 26.4.1            | Full definition of a rule: description with compliant and non-compliant examples, remediation, severity, category and tags.                           | Signed-in user                                           |
| **`getFalconRules`**                    | 1.0.0             | Searches rules by name.                                                                                                                               | **`View Quality Rules`**                                 |
| **`getFalconRuleProfiles`**             | 26.4.1            | Searches rule (quality) profiles with their language, default flag and rule counts.                                                                   | **`View Quality Profiles`**                              |
| **`getFalconOrganizationRuleProfiles`** | 26.4.1            | The rule profile active in an organization for each language.                                                                                         | Signed-in user                                           |
| **`getFalconRuleProfileRules`**         | 26.4.1            | Lists the rules of a rule profile and whether each is active.                                                                                         | **`View Quality Rules`**                                 |
| **`getFalconOrganizations`**            | 1.0.0             | Lists the organizations the user has access to.                                                                                                       | **`View Organizations`**                                 |
| **`getFalconAutomationTaskStatus`**     | 1.0.0             | Status, diagnostics and response of an automation task run.                                                                                           | **`View Insights`** or **`Run Insights`**                |

### Pagination

List tools (**`searchFalconApplications`**, **`getFalconIssues`**, **`getFalconIssuesGrouped`**, **`getFalconRules`**, **`getFalconRuleProfiles`**, **`getFalconRuleProfileRules`**, **`getFalconOrganizations`**) are paginated. They accept **`offset`** (default `0`) and **`limit`** (default `50`, maximum `200`) and return **`total`**, **`returned`**, **`hasMore`** and **`nextOffset`**. To read the next page, call the tool again with **`offset`** set to **`nextOffset`**.

### Tools available only in STDIO Servers:

| Tool Name          | Available Version | Description                                   | Permission                 |
| ------------------ | ----------------- | --------------------------------------------- | -------------------------- |
| **`iz-code-scan`** | >1.0.0            | Execute IZ Scan Code Analysis for the project | Add role **`IZ Scan CLI`** |

From 26.4.1 **`falcon-code-scan`** returns a compact summary of the scan it has just run: issue counts by severity, the most violated rules and files, a sample of the most severe issues and the application id. Use **`getFalconIssues`** with that application id for the full list. Results of an earlier scan are never reported as the result of the current one. While the scan runs, the tool sends a progress notification every 15 seconds so that MCP clients that support progress do not time out.

### Tools available as part of automation tasks:

1. Navigate to **`IZ AI`** -> **`Automation Tasks`**
2. Click on any of the listed **`Automation Tasks`** and toggle **`Include in MCP Server`**
3. If selected value is **`Yes`**, the automation task will be available as part of MCP Server tool list.

### See Also

* [Create Agent](../../../integral-zone/iz-suite/iz-core/agent/create-agent.md)
* [Update Agent](../../../integral-zone/iz-suite/iz-core/agent/update-agent.md)
