# All Applications

* Available from IZ Suite Server **26.3.1** under **`IZ Eye`** → **`All Applications`** .
* The view shows the applications of every application type your roles give you access to, across all organizations and environments



**`All Applications`** is a single grid over every scanned application of a module, regardless of application type. In IZ Eye it combines Mule applications, Exchange APIs, API Manager instances, Azure Logic Apps, Azure API Management, Azure Function Apps and Salesforce Apex in one list; in IZ Scan it combines all scanned repositories and projects. Use it to find an application without knowing its type, to compare quality gate results across types, or to export a consolidated list.

1. Navigate to **`IZ Eye`** → **`All Applications`** .
2. Each row is one application version (IZ Eye) :

| Column                             | IZ Eye                                                                            | IZ Scan                                           |
| ---------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------- |
| **`Application`**                  | Name of the application                                                           | Name of the repository or project                 |
| **`Version`** / **`Branch / PR`**  | Deployed version                                                                  | Branch or pull request scanned                    |
| **`App Type`**                     | Mule, API, API Instance, Logic App, API Management, Function App, Apex, and so on | Mule, API, Python, C#, Kubernetes, and so on      |
| **`Total Issues`**                 | Issues found by the latest scan                                                   | Issues found by the latest scan                   |
| **`Quality Gate`**                 | Result of the latest scan against the active quality gate                         | Same                                              |
| **`Status`** / **`Code Coverage`** | Runtime status of the application                                                 | Code coverage reported with the scan              |
| **`Created`**                      | When the application was first seen                                               | When the branch or pull request was first scanned |
| **`Last Scan`**                    | Time since the latest scan                                                        | Time since the latest scan                        |

3. Additional columns can be enabled from the column settings in the toolbar: **`Source`**, **`Organization`**, **`Environment`**, **`Scan Scheduled?`**, **`Is Deleted?`**, **`Has Custom Setting?`**, **`Uses Custom Setting?`**, **`Report Default?`** and **`Can Scan?`**.

#### Filters <a href="#filters" id="filters"></a>



* **`Name / Version`** (IZ Eye) or **`Name / Branch / PR`** (IZ Scan) - Inline search on application name, version, branch or pull request.
* **`Organizations`** and, for IZ Eye, **`Environments`**
* **`App Type`**
* **`Quality Gate Status`** - Passed, Failed or Free
* **`Severity`** and **`Category`** - Show applications that have issues of the selected rule severity or category
* **`Rule`** - Show applications that violate the selected rules. Search rules by name, id or tag.
* **`Is Report Default`**



#### Actions <a href="#actions" id="actions"></a>

| Action                    | Description                                                                                                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`View Dashboard`**      | Opens the application dashboard for this application. See [Application Dashboard](https://file+.vscode-resource.vscode-cdn.net/product-guides/integral-zone/iz-suite/iz-eye/anypoint-platform/application-dashboard.md).                          |
| **`View Issues`**         | Opens the issues of the latest scan, grouped by file. Available once the application has been scanned. See [Application Issues](https://file+.vscode-resource.vscode-cdn.net/product-guides/integral-zone/iz-suite/iz-eye/application-issues.md). |
| **`View Previous Scans`** | Opens the scan history of the application.                                                                                                                                                                                                        |

Use **`Download`** in the toolbar to export the current view, and **`Reload`** to refresh it.

<br>
