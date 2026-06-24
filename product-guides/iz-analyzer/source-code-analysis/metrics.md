# Metrics

## Metrics Calculated for Mule Projects

### Mule Metrics

Various metrics will be calculated by IZ Analyzer for the mule application on successful analysis. Below are the details of available metrics.

{% hint style="info" %}
* `Metric Key` in the below table will be useful for querying the data using [APIs](https://analyzer.integralzone.com/web_api/api/measures/component).
{% endhint %}

| **`Metric Name`**        | **`Metric Key`**           | **`Description`**                                                                                                                                                         |
| ------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flows                    | `iz_component_flows`       | Total Number of flows in the mule application                                                                                                                             |
| Database Connectors      | `iz_component_database`    | Total Number of database connectors used in the mule application                                                                                                          |
| Batch Jobs               | `iz_component_batch`       | Total Number of batch jobs used in the mule application                                                                                                                   |
| File Connectors          | `iz_component_file`        | Total Number of file connectors used in the mule application                                                                                                              |
| FTP Connectors           | `iz_component_ftp`         | Total Number of FTP connectors used in the mule application                                                                                                               |
| Loggers                  | `iz_component_loggers`     | Total Number of loggers used in the mule application                                                                                                                      |
| VM Connectors            | `iz_component_vm`          | Total Number of VM connectors used in the mule application                                                                                                                |
| Web Service Consumers    | `iz_component_ws`          | Total Number of Web Service consumers used in the mule application                                                                                                        |
| Dataweave Transformers   | `iz_component_dw`          | Total Number of Dataweave transformers used in the mule application                                                                                                       |
| Total APIs               | `iz_api_no_of_apis`        | Total Number of APIs exposed in the mule application                                                                                                                      |
| HTTP Listeners           | `iz_listener_http`         | Total Number of HTTP Listeners used in the mule application                                                                                                               |
| HTTPS Listeners          | `iz_listener_https`        | Total Number of HTTP Listeners used in the mule application                                                                                                               |
| Debug Loggers            | `iz_debug_loggers`         | Total Number of Debug Loggers used in the mule application                                                                                                                |
| Info Loggers             | `iz_info_loggers`          | Total Number of Info Loggers used in the mule application                                                                                                                 |
| Error Loggers            | `iz_error_loggers`         | Total Number of Error Loggers used in the mule application                                                                                                                |
| Trace Loggers            | `iz_trace_loggers`         | Total Number of Trace Loggers used in the mule application                                                                                                                |
| Warn Loggers             | `iz_warn_loggers`          | Total Number of Warn Loggers used in the mule application                                                                                                                 |
| Global Exception Handler | `iz_global_exception_conf` | Indicates if Global Exception handling is configured in the application                                                                                                   |
| Scripting Components     | `iz_scripting_components`  | Total Number of Scripting Components used in the mule application                                                                                                         |
| MUnit Exists ?           | `iz_muit_exists`           | Indicates if the Mule project has MUnit test cases                                                                                                                        |
| Mule Version             | `iz_mule_version`          | Indicates if the Mule project version                                                                                                                                     |
| Project Score            | `iz_project_score`         | Total score of the mule project based on number of Blocker, Major, Critical, Minor, Info issues. Details of how the project score will be calculated can be found below - |
| Project Grade            | `iz_project_score`         | Rating of the Mule project based on project score                                                                                                                         |

### Project Score Calculation

1. Why do we need project score ?
   1. Project analysis to show bugs, vulnerabilities and issues is NOT ENOUGH
   2. Static rules dictate ANY issues in the project - from minor/info issues to critical bugs
   3. Quality gate works mainly works based on number of issues of a particular type to determine whether the project passes the quality check or not (i.e., the quality gate could be set up to ignore all the errors too and hence not a reliable indicator!)
   4. There is no one metric that we can use to qualitatively analyze the QUALITY of the project!
2. What does generating project score provide?
   1. Single score used to find out how the project is doing at a summary level
   2. Provides an indicator to the overall quality of the project without hiding anything
   3. Can be used to aggregate the score at groups of projects/organization level
3. How is a project score calculated?
   1. Project score is calculated based on number of Blocker, Major, Critical, Minor, Info issues.
   2. Each of the above issue types will be given a default weightage (Organization can customize the default weightage)
   3. Each project in the organization has a calculated graded average calculated based on weightage set and individual metrics
   4. Project Score is also represented as a project grade as below:&#x20;

| **`Score Range`** | **`Grade`** |
| ----------------- | ----------- |
| >90               | `A`         |
| 70-90             | `B`         |
| 50-70             | `C`         |
| 30-50             | `D`         |
| <30               | `E`         |

### See Also

* [Code Analysis In Anypoint Studio](code-analysis-in-studio.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
