# Generating Decorated SARIF Reports

**What is a SARIF Report?**

SARIF (Static Analysis Results Interchange Format) is a standardized file format used to represent the results of static code analysis. SARIF reports help developers and security teams:

* Track issues such as bugs, code smells, or vulnerabilities for your branch and PR requests.
* Understand issue metadata (e.g., severity, category/type)
* Integrate results with tools like GitHub Advanced Security, Azure DevOps, or custom dashboards

***

#### ⚙️ How SARIF File Generation Works in the Workflow <a href="#how-sarif-file-generation-works-in-the-workflow" id="how-sarif-file-generation-works-in-the-workflow"></a>

&#x20;

* You cannot enable both `generateSarifFile` and `generateReportFile` as `true` within a single configuration.\
  \

* The `generateSarifFile` flag controls the generation of reports on both the server and client sides:
  * When `generateSarifFile` is set to `true`, server-side reports are generated.
  * When `generateSarifFile` is set to `false`, client-side reports are generated. In this case, it is not necessary to explicitly set `generateReportFile: true`, as it is enabled by default in the configuration.

\
There are **two types of report generation** in the system:

1. **Server-Side SARIF File** – Controlled by `generateSarifFile`
2. **Client-Side Report File** – Controlled by `generateReportFile` ( SARIF, SAST )

Each has its own use case and default behavior.\
\
\


<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>



***

#### 🧩 Configurations and Their Defaults <a href="#configurations-and-their-defaults" id="configurations-and-their-defaults"></a>

| Input Key            | Default Value | Description                                                                                                                                                                                          |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generateSarifFile`  | `false`       | <p>If <code>true</code> SARIF file is generated on the <strong>server side</strong>.<br><br>If you don't mention this parameter in GitHub action .yml file by default it will <code>false</code></p> |
| `generateReportFile` | `true`        | If **true** (default), a SARIF report file is generated on the **client side**, useful for local or immediate analysis.                                                                              |

***

**Why we have two different repo generations in CodeScan:**\
Functional Differences

| Aspect                | **CodeScanReports**                                                   | **CodeScanSarif**                                                            |
| --------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Purpose**           | General-purpose reporting plugin (multi-format support: SARIF, SAST). | Specialized in SARIF report generation.                                      |
| **Supported Formats** | SARIF, SAST                                                           | SARIF only                                                                   |
| **Primary Use Case**  | Teams needing multiple report types across different use cases.       | Workflows needing SARIF as the output (e.g., CI/CD pipelines, integrations). |
| **Implementation**    | Multipurpose logic for handling various report types.                 | Focused implementation optimized for SARIF report generation.                |

&#x20;

***

#### 🧠 Why These Two Options?   <a href="#why-these-two-options" id="why-these-two-options"></a>

* **Server-side SARIF (**`generateSarifFile: true`**)**\
  This option produces a comprehensive SARIF report, including **all issues** (open + resolved), **Security Hotspots** and full metadata such as **Type** and **Severity**.\
  This is crucial for:
  * Security auditing
  * Historical tracking
  * Full integration with enterprise-grade systems

We can also generate codescan reports using sfdx and sonarcanner cli by passing the correct parameters in the command\
`-Dsonar.analysis.report.enabled=true` `-Dsonar.analysis.report.type=sarif`

&#x20;

* **Client-side SARIF (**`generateReportFile: true or generateSarifFile: false`**)**\
  This is useful for developers during early analysis or CI runs where only open issues are needed. It creates a basic report with just open issues, but with **metadata** like **Type** and **Severity** for rules and results. Ideal for quick checks.\
  \
  \


We can also generate codescan reports using sfdx and sonarcanner cli by passing the correct parameters in the command\
`-Dcodescan.reports.enabled=true` `-Dcodescan.reports.type=sarif or sast`

***

#### ✅ Summary of Behavior <a href="#summary-of-behavior" id="summary-of-behavior"></a>

| Configuration                                                                          | Report Includes                                  | Metadata (Type, Severity) | Use Case                          |
| -------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------- | --------------------------------- |
| `generateSarifFile: true`                                                              | All issues + security hotspots (open + resolved) | ✅ Included                | Audits, dashboards, policy checks |
| <p><code>generateSarifFile: false</code>,<br><code>generateReportFile: true</code></p> | Only open issues                                 | ✅ Included                | Lightweight local scans           |

***

**Example:**\
**Rules sample format:**

```
"rules": [
{
"id": "sf:LeftBracesLinePositions",
"name": "Left Braces Positioning Should Be Consistent",
"shortDescription": {
"text": "Left Braces Positioning Should Be Consistent"
},
"fullDescription": {
"text": "Left Braces Positioning Should Be Consistent"
},
"defaultConfiguration": {
"enabled": true,
"level": "warning"
},
"help": {
"text": "Left Braces Positioning Should Be Consistent [Type: Code Smell, Severity: Minor]"
},
"properties": {
"tags": [
"dummy",
"convention",
"hello"
]
}
}
]
```

\
**Results sample format:**

```
"rules": [
{
"id": "sf:LeftBracesLinePositions",
"name": "Left Braces Positioning Should Be Consistent",
"shortDescription": {
"text": "Left Braces Positioning Should Be Consistent"
},
"fullDescription": {
"text": "Left Braces Positioning Should Be Consistent"
},
"defaultConfiguration": {
"enabled": true,
"level": "warning"
},
"help": {
"text": "Left Braces Positioning Should Be Consistent [Type: Code Smell, Severity: Minor]"
},
"properties": {
"tags": [
"dummy",
"convention",
"hello"
]
}
}
]
```
