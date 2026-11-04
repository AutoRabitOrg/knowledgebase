# Languages

IZ Scan detects the language of every project it scans and applies that language's quality profile, metric profile and quality gate. A repository can match more than one language. For example, a Spark project is also a Python project, so it is analysed by both, and the results appear under both menus.

Languages and their rule packs are delivered as seed data. A new language becomes available after the release seed data has been loaded and the language has been enabled on your licence.

#### Supported Languages <a href="#supported-languages" id="supported-languages"></a>

Under **`IZ Scan`**, applications are grouped by platform. Each language has its own menu item:

| Platform submenu        | Menu item                  | Language                               |
| ----------------------- | -------------------------- | -------------------------------------- |
| **`Anypoint Platform`** | **`Mule Projects`**        | Mule 3 and Mule 4 applications         |
| **`Anypoint Platform`** | **`APIs`**                 | RAML and OAS API specifications        |
| **`Azure`**             | **`Azure API Management`** | Azure API Management                   |
| **`Azure`**             | **`Azure Logic Apps`**     | Azure Logic Apps                       |
| **`Azure`**             | **`Azure Function Apps`**  | Azure Function Apps                    |
| **`AWS`**               | **`AWS CloudFormation`**   | CloudFormation and SAM templates       |
| **`AWS`**               | **`AWS Lambda`**           | AWS Lambda function definitions        |
| **`Others`**            | **`Python Apps`**          | Python                                 |
| **`Others`**            | **`PySpark Apps`**         | PySpark                                |
| **`Others`**            | **`Java Apps`**            | Java, including Spring and Spring Boot |
| **`Others`**            | **`CSharp Apps`**          | C#                                     |
| **`Others`**            | **`Kubernetes`**           | Kubernetes manifests                   |
| **`Others`**            | **`Apex Apps`**            | Salesforce Apex                        |

A menu item appears only when the language is enabled on your licence and your role has permission to view it. Licence modules are shown as **`IZ Scan <menu item>`**, for example **`IZ Scan Java Apps`**.

#### How a Project's Language Is Detected <a href="#how-a-projects-language-is-detected" id="how-a-projects-language-is-detected"></a>

Detection is controlled by the per-language scripts in [Language Identifier Settings](language-identifier-settings.md). The same scripts are used by repository scans, the [IZ Scan CLI](../releases/iz-scan-cli/) and the [VS Code Extension](vs-code-extension/).<br>

