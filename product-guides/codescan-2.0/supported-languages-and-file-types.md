# Supported Languages and File Types

CodeScan runs more than 5,100 built-in rules across 49 languages and file types. Custom rules your team writes are added on top.

| Area                      | Languages and file types                                                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Salesforce and MuleSoft   | Apex, Salesforce metadata (including Visualforce), Lightning Web Components (HTML, JavaScript and XML configuration), Aura, MuleSoft                                                     |
| General-purpose languages | Java, JavaScript, TypeScript (including Angular and Vue), C#, VB.NET, F#, Python, Go, Rust, Kotlin, Scala, Groovy, PHP, Ruby, Swift, Objective-C, C, C++, Dart, Elixir, Lua, R, Solidity |
| Scripting                 | Shell scripts, PowerShell                                                                                                                                                                |
| Web and markup            | HTML, CSS, XML                                                                                                                                                                           |
| Databases                 | SQL, PL/SQL                                                                                                                                                                              |
| Infrastructure as code    | Terraform, AWS CloudFormation, Azure Resource Manager (ARM) templates, Bicep, Kubernetes and Helm, Ansible, Puppet, Chef                                                                 |
| Containers                | Dockerfile, Docker Compose                                                                                                                                                               |
| CI pipelines              | GitHub Actions, GitLab CI                                                                                                                                                                |
| APIs                      | OpenAPI                                                                                                                                                                                  |
| Across all code           | Secret detection, third-party dependencies                                                                                                                                               |

{% hint style="info" %}
**Note:** How deep the analysis goes depends on the language. Cross-file data flow and call graphs are deepest for Apex, Java, JavaScript, TypeScript, Python, C#, Kotlin, Scala, PHP, Go and Rust.
{% endhint %}

{% hint style="info" %}
**Note:** Helm charts are scanned only if `helm` is installed where the scan runs. Otherwise they are reported as not scanned, not as clean.
{% endhint %}

### Related Articles

* How a Scan Works
* [What Is CodeScan](./)
