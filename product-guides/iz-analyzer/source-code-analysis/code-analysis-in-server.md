# Code Analysis in Server

### Using Sonar Scanner:

{% hint style="info" %}
Before analyzing the source code using **`[SonarScanner™](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)`**, make sure you have

* Downloaded and installed **`[SonarScanner™](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)`** CLI plugin. Refer to [Installing Sonar Scanner](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner)
* Follow the instructions here to generate security token
* For on-premises instances, please use your organization-specific service URL instead of [https://analyzer.integralzone.com](https://analyzer.integralzone.com/)
{% endhint %}

There are 2 ways in which the projects can be analyzed.&#x20;

* By creating and adding required properties in sonar-project.properties file in the parent directory of the project.&#x20;
* By directly passing all the properties as command line arguments

Steps outlined below uses the command line approach

1. Go to the project root directory from command line/terminal
2. Run **`sonar-scanner`** command with following options
   1. -Dsonar.projectKey=xxx\
      &#xNAN;_&#x55;nique key for the project being uploaded_
   2. -Dsonar.projectName=xxx\
      &#xNAN;_&#x44;iplay name of the project being uploaded_
   3. -Dsonar.projectVersion=x.x\
      &#xNAN;_&#x56;ersion of the project being uploaded_
   4. -Dsonar.sources=.\
      &#xNAN;_&#x53;ource code directory_
   5. -Dsonar.login=xxx\
      &#xNAN;_&#x53;ecurity token generated from the server. This parameter is deprecated from SonarQube version > 10.x, use sonar.token instead_
   6. -Dsonar.token=xxx\
      &#xNAN;_&#x53;ecurity token generated from the server. This parameter is applicable from SonarQube version > 10.x, for versions < 10.x use sonar.login parameter_
   7. -Dsonar.organization=xxx + _Optional. Applicable only for cloud version_
   8. -Dsonar.branch.name=xxx + _Optional. SCM branch for which code is being analysed. Eg: -Dsonar.branch.name=master_
3. Complete example may look like
   1. Using IZ Analyzer cloud instance PROJECT\_ROOT\_DIR> sonar-scanner\
      -Dsonar.projectKey=xxx\
      -Dsonar.organization=\
      -Dsonar.sources=.\
      -Dsonar.exclusions=target\
      -Dsonar.host.url=https://analyzer.integralzone.com\
      -Dsonar.login= \\
   2. Using IZ Analyzer on-prem instance PROJECT\_ROOT\_DIR> sonar-scanner # -Dsonar.projectKey=xxx\
      -Dsonar.projectName=xxx\
      -Dsonar.sources=.\
      -Dsonar.host.url=\
      -Dsonar.login= \\

{% hint style="info" %}
* For complete reference of all the properties that can be used with sonar-scanner, refer to [Analysis Parameters](https://docs.sonarqube.org/latest/analysis/analysis-parameters/#AnalysisParameters-projectBaseDir)
{% endhint %}

### Using Maven Plugin

{% hint style="info" %}
Before analyzing the source code using **`Maven Plugin`**, make sure you have:

* Downloaded and installed **`Apache Maven`**. Refer to [Installing Apache Maven](https://maven.apache.org/)
* Follow the instructions here to generate security token
{% endhint %}

1. Go to the project root directory from command line/terminal
2. Run **`mvn sonar:sonar`** command with following options
   * -Dsonar.projectKey=xxx\
     &#xNAN;_&#x55;nique key for the project being uploaded_
   * -Dsonar.projectName=xxx\
     &#xNAN;_&#x44;iplay name of the project being uploaded_
   * -Dsonar.projectVersion=x.x\
     &#xNAN;_&#x56;ersion of the project being uploaded_
   * -Dsonar.sources=.\
     &#xNAN;_&#x53;ource code directory_
   * -Dsonar.login=xxx\
     &#xNAN;_&#x53;ecurity token generated from the server. This parameter is deprecated from SonarQube version > 10.x, use sonar.token instead_
   * -Dsonar.token=xxx\
     &#xNAN;_&#x53;ecurity token generated from the server. This parameter is applicable from SonarQube version > 10.x, for versions < 10.x use sonar.login parameter_
   * -Dsonar.organization=xxx + _Optional. Applicable only for cloud version_
   * -Dsonar.branch.name=xxx + _Optional. SCM branch for which code is being analysed. Eg: -Dsonar.branch.name=master_
3. Complete example may look like
   * Using IZ Analyzer cloud instance PROJECT\_ROOT\_DIR> mvn sonar:sonar\
     -Dsonar.projectKey=xxx\
     -Dsonar.organization=\
     -Dsonar.exclusions=target\
     -Dsonar.sources=.\
     -Dsonar.host.url=https://analyzer.integralzone.com\
     -Dsonar.login=
   * Using IZ Analyzer on-prem instance PROJECT\_ROOT\_DIR> mvn sonar:sonar\
     -Dsonar.projectKey=xxx\
     -Dsonar.projectName=xxx\
     -Dsonar.sources=.\
     -Dsonar.host.url=\
     -Dsonar.login= \\

{% hint style="info" %}
Follow the instructions from [Scanner for Maven](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner+for+Maven) for addition information about configuring the plugin
{% endhint %}

### Setting Proxy Details

If the system from which the projects are analyzed using **`sonar-scanner`** or **`maven`** is configured with proxy, then set the following environment variable with proxy server details before running the respective commands

* Windows > set SONAR\_SCANNER\_OPTS="-Dhttps.proxyHost=PROXY\_HOST -Dhttps.proxyPort=PROXY\_PORT -Dhttp.proxyHost=PROXY\_HOST -Dhttp.proxyPort=PROXY\_PORT -Djava.net.useSystemProxies=true"
* Linux > export SONAR\_SCANNER\_OPTS="-Dhttps.proxyHost=PROXY\_HOST -Dhttps.proxyPort=PROXY\_PORT -Dhttp.proxyHost=PROXY\_HOST -Dhttp.proxyPort=PROXY\_PORT -Djava.net.useSystemProxies=true"

{% hint style="info" %}
- Replace **`PROXY_HOST`** and **`PROXY_PORT`** with appropriate values for Proxy server host and port
- If **`https.proxyPort`** is not specified, default value will be 443
- If **`http.proxyPort`** is not specified, default value will be 80
{% endhint %}

### See Also

* [Code Analysis In Anypoint Studio](code-analysis-in-studio.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
