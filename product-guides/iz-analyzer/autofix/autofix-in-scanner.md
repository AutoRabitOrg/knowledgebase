# Autofix - In Scanner

Autofix in scanner is a feature where static code analysis issues can be fixed automatically by enabling a few properties while scanning the projects.

{% hint style="warning" %}
Make sure you have a:

* Valid license with Autofix module enabled for either Mule or API or both
{% endhint %}

### Enable Auto Fix

1. Autofix can be enabled by passing **`analyzer.<plugin>.auto.fix.all`** system property while running the sonarscanner/mvn command to analyze the project. For more information refer Code Analysis In Server
   1. Ex: -Danalyzer.mule.auto.fix.all=true\
      &#xNAN;_&#x54;o enable auto fix for Mule plugin_
   2. Ex: -Danalyzer.api.auto.fix.all=true\
      &#xNAN;_&#x54;o enable auto fix for API plugin_
2. Preview mode can be enabled to get the list of changes that would be performed by Auto Fix without updating any of the files.
   1. Can be enabled using **`-Danalyzer.<plugin>.auto.fix.preview`** system property
3. Default log location is **`target/autofix_log.csv`** relative to the project from which scanner is invoked. This property can be customized using **`analyzer.<plugin>.auto.fix.log.location`** system property.
4. Fix can also be applied only on certain issues by passing various filters. Every rule will be associated with a **`Type`**, **`Severity`** and **`Tag`**, any of these properties can be used to specify the filters
   1. Ex: -Danalyzer.\<plugin>.auto.fix.rule.severities can be set to MAJOR,MINOR to fix only major and minor issues
   2. Ex: -Danalyzer.\<plugin>.auto.fix.rule.types can be set to CODE\_SMELL to fix only Code Smells
   3. Ex: -Danalyzer.\<plugin>.auto.fix.rule.tags can be set to any custom tags attached to the rule. Only rules with specified tags will be auto fixed in this case.

### Mule Scanner Properties

Following parameters can be passed as system properties to Mule scanner.

| Property Name                                | Description                                                                                                                                                                   | Possible Values                                       | Default                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------- |
| **`analyzer.mule.auto.fix.all`**             | Enable auto fix for the Mule scanner                                                                                                                                          | true / false                                          | false                                   |
| **`analyzer.mule.auto.fix.log.location`**    | Location of the Auto Fix log. Logs will be generated in .csv format                                                                                                           | Any location where the .csv should be generated       | target/autofix\_log.csv                 |
| **`analyzer.mule.auto.fix.preview`**         | Enable or disable the Auto Fix preview mode                                                                                                                                   | true / false                                          | false                                   |
| **`analyzer.mule.auto.fix.rule.types`**      | Rule types to be auto fixed. Only those issues with specified rule types will be fixed. Multiple rule types can be specified by using comma(,) as a delimiter.                | BUG / VULNERABILITY / CODE\_SMELL / SECURITY\_HOTSPOT | By default all the issues will be fixed |
| **`analyzer.mule.auto.fix.rule.severities`** | Rule severities to be auto fixed. Only those issues with specified rule severities will be fixed. Multiple rule severities can be specified by using comma(,) as a delimiter. | BLOCKER / CRITICAL / MAJOR / MINOR / INFO             | By default all the issues will be fixed |
| **`analyzer.mule.auto.fix.rule.tags`**       | Rule tags to be auto fixed. Only those issues with specified rule tags will be fixed. Multiple rule tags can be specified by using comma(,) as a delimiter.                   | Any tags associated with rule                         | By default all the issues will be fixed |

### API Scanner Properties

Following parameters can be passed as system properties to API scanner.

| Property Name                               | Description                                                                                                                                                                   | Possible Values                                       | Default                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------- |
| **`analyzer.api.auto.fix.all`**             | Enable auto fix for the API scanner                                                                                                                                           | true / false                                          | false                                   |
| **`analyzer.api.auto.fix.log.location`**    | Location of the Auto Fix log. Logs will be generated in .csv format                                                                                                           | Any location where the .csv should be generated       | target/autofix\_log.csv                 |
| **`analyzer.api.auto.fix.preview`**         | Enable or disable the Auto Fix preview mode                                                                                                                                   | true / false                                          | false                                   |
| **`analyzer.api.auto.fix.rule.types`**      | Rule types to be auto fixed. Only those issues with specified rule types will be fixed. Multiple rule types can be specified by using comma(,) as a delimiter.                | BUG / VULNERABILITY / CODE\_SMELL / SECURITY\_HOTSPOT | By default all the issues will be fixed |
| **`analyzer.api.auto.fix.rule.severities`** | Rule severities to be auto fixed. Only those issues with specified rule severities will be fixed. Multiple rule severities can be specified by using comma(,) as a delimiter. | BLOCKER / CRITICAL / MAJOR / MINOR / INFO             | By default all the issues will be fixed |
| **`analyzer.api.auto.fix.rule.tags`**       | Rule tags to be auto fixed. Only those issues with specified rule tags will be fixed. Multiple rule tags can be specified by using comma(,) as a delimiter.                   | Any tags associated with rule                         | By default all the issues will be fixed |

### Multiple Plugins Scanning the Same Project

While scanning the Mule projects, by default Mule and API Analyzer plugins would report the static code analysis issues. If there are any other open source plugins scanning files in the same project, then the **`Background Task`** might fail in the server with an error \_ Source of file has less/more lines than expected\_ .

As a resolution the scanner command should be executed again without **`analyzer.<plugin>.auto.fix.all`** system property.

1. Scan 1 - To auto Fix issues \_sonar-scanner -Dsonar.projectKey=\<key> -Dsonar.sources=. -Dsonar.host.url=\<host> -Dsonar.login=\<token> -Dsonar.exclusions=target/\*\* -Danalyzer.api.auto.fix.all=true -Danalyzer.mule.auto.fix.all=true \_
2. Scan 2 - To upload results to the server \_sonar-scanner -Dsonar.projectKey=\<key> -Dsonar.sources=. -Dsonar.host.url=\<host> -Dsonar.login=\<token> -Dsonar.exclusions=target/\*\* \_

#### Details

* Manage Anypoint Studio Plugin
* Manage Server Plugin

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
