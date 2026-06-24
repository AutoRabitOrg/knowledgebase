# FAQs

### Does IZ Analyzer allow us to write Custom rules?

Yes, custom rules can be created in IZ Analyzer using simple groovy scripts. Rules can be created by using either of the following ways -

1. [Rules Playground in Studio](../iz-suite/iz-scan/anypoint-studio/rules-playground.md) - Rules playground is part of Anypoint Studio plug-in, where custom rules can be evaluated and published to server.
2. [Rules Template in Server](manage-rules/custom-rules.md) - Custom rules can also be created directly in server using the custom rule template.

### If we start using this product will our code remain secure? How much of access will Integral Zone have in viewing our code?

\<TBA>

### What are the different installation options?

IZ Analyzer is available in both Cloud and On premise installation options. With similar user experiences, each installation options provides benefits of its own. To view a more comprehensive document on the installations options for IZ Analyzer, please follow the link [On-Premises vs Cloud](on-prem-vs.-cloud.md).

### How frequently are the updates and the support provided?

\<TBA>

### Can we get a perpetual license for IZ Analyzer?

Due to the ever evolving nature of the MuleSoft landscape and also the exciting new features we provide every year as part of your user experience of IZ Analyzer, we do not provide a perpetual license option.

### How easy is it to fit IZ Analyzer in our CI/CD?

Its as easy as executing a simple maven command in any of your existing CI/CD pipelines. There are options available to use `sonar-scanner` if maven cannot be used in your pipelines. Follow the below references to know more about integrating IZ Analyzer within your CI/CD pipeline

1. [mvn](https://docs.integralzone.com/iz-analyzer/1.0.0/source-code-analysis/in-sonarqube-server.html#_using_maven_plugin) - Using maven in your CI/CD pipeline
2. [sonar-scanner](https://docs.integralzone.com/iz-analyzer/1.0.0/source-code-analysis/in-sonarqube-server.html#_using_sonar_scanner) - Using sonar scanner plugin in your CI/CD pipeline

### How can a quality gate be setup so that after matching a certain criteria, the build can be failed or progressed accordingly?

Quality Gates can be setup to as per the organization standards and can be integrated with CICD pipelines to check the status. The builds can be failed or progressed based on the Quality Gate status.

Here is a reference example to validate Quality Gate status in Jenkins pipeline - [SonarQube Scanner for Jenkins](https://www.jenkins.io/doc/pipeline/steps/sonar/)

### Does IZ Analyzer Studio plug-in work offline too?

There are 2 instances where Studio plug-in will work offline:

1. Without Service URL - When a service URL is not configured, Studio plug-in will make use of the default rules available as part of the plug-in release.
2. With Service URL - When a service URL is configured, Studio plug-in will download the rules configured in the server to local Studio instance (when online, if not the default rules as mentioned above will be used). Once the rules are downloaded to local, `On The Fly Results` will be evaluated offline.

### How heavy is the IZ Analyzer Studio Plugin? Would it make the computer slow?

IZ Analyzer Studio plug-in is very lightweight and all the scans will be done in a background thread, which does not impact the performance.

### How are your current customers using it? Any stories you could share?

\<TBA>

### Is it a real-time analyzer?

Yes, IZ Analyzer Studio plugin scans the project in real time as the developer starts working on the project. So, developers would get a real-time feedback as and when they start adding new components, connectors, properties, etc. into the project.

### How do we feed org-specific standards for RAML and Mule flows?

Custom rules can be created in IZ Analyzer using simple groovy scripts. Rules can be created by using either of the following ways -

1. [Rules Playground in Studio](https://docs.integralzone.com/iz-analyzer/1.0.0/manage-rules/rules-playground.html) - Rules playground is part of Anypoint Studio plug-in, where custom rules can be evaluated and published to server.
2. [Rules Template in Server](https://docs.integralzone.com/iz-analyzer/1.0.0/manage-rules/custom-rules.html) - Custom rules can also be created directly in server using the custom rule template.

### What are the different versions of Mule supported by IZ Analyzer?

IZ Analyzer supports all versions of Mule from 3.x to 4.x.

| Language | Version                       |
| -------- | ----------------------------- |
| Mule     | 3.x to 4.x                    |
| RAML     | 0.8 & 1.0                     |
| Swagger  | 2.0 both .json & .yaml format |
| OAS      | 3.0                           |

### Does IZ Analyzer have a trial version?

IZ Analyzer has a free open source version available for every interested Muley to try. Called the Community Edition, it is completely free. For Enterprise inquiries, you can request a trial and also an exclusive free demo by following the link [Book Online Demo](https://integralzone.com/book-online-demo).

### Can IZ Analyzer functionality be scripted and/or invoked from command-line or via web APIs?

Yes, IZ Analyzer REST API’s can be utilized to invoke any of the functionality from scripts. List of supported REST APIs can be found [here](https://analyzer.integralzone.com/web_api/api/authentication).

### Are Issues generated based on the rules defined in the IZ Analyzer?

Yes, all the issues generated for Mule applications are based on the rules defined in IZ Analyzer. Rules will be applied based on the Quality Profile selected. A Quality Profile may consist of 180+ built-in rules as well as custom rule definitions.

### Can IZ Analyzer be run part of maven build and report created?

Yes, IZ Analyzer can be invoked to scan your Mule projects by invoking a simple maven command without making any changes in your pom.xml or settings.xml. More information on using maven scanner can be found [here](https://docs.integralzone.com/iz-analyzer/1.0.0/source-code-analysis/in-sonarqube-server.html#_using_maven_plugin).

### Can the users of IZ Analyzer create their own dashboards?

Creating custom dashboards is not supported by IZ Analyzer yet. This feature is in our future roadmap.

### How does IZ Analyzer define private project and public project?

Public and private projects are applicable only for the Cloud version of [IZ Analyzer](https://analyzer.integralzone.com).

1. `Public Projects` - Public projects will be accessible to any user. Any user will be able to access the project’s analysis report, issues, dashboard etc.
2. `Private Projects` - Private projects will only be visible to members of the organization. All the project analysis report, issues, dashboard will be accessible only to the members of the organization.

### Can I use the IZ Analyzer Anypoint Studio plug-in during my trial?

For any Enterprise inquiry, we provide access to a limited trial of all features of IZ Analyzer, including the Anypoint Studio plug-in.

### Is Coverage through-book a part of the report provided by IZ Analyzer?

Current version of IZ Analyzer does not support scanning MUnit coverage reports. This feature is in our future roadmap.

### Where is IZ Analyzer being hosted?

IZ Analyzer is hosted on Google Cloud Platform (GCP) in the European region.

### How does IZ Analyzer compare to its closest alternatives in the market?

IZ Analyzer stands alone as the enterprise ready option for code quality, analysis and review in the MuleSoft ecosystem.

### How are threats and security vulnerabilities handled? In terms of patches, updates, notifications, ETA, service availability?

1. For cloud edition, based on critical security issues, patches will be rolled out as they become available on SonarQube software - since our cloud edition is based on SonarQube system.
2. For on-premises edition, you would need to patch and install updates manually by working with SonarQube server. Notification and availability of patches will be communicated as part of the Knowledge Base Article in our support portal.

### How is Disaster Management, Backups and security handled for the tool both on cloud and on-premise

1. Both Hard Disks and Databases are backed up. Hard Disks are backed up using the GCP’s Disk Snapshot feature. All backups are stored in Google Cloud Platform (GCP).
2. \<TBA> More info required about security & Disaster Management

### Is IZ Analyzer a CI/CD tool or aligned more towards DevOps?

IZ Analyzer is a product designed to optimize your DevOps and increase productivity and drive cost effective operation. Given its strong presence as an automation tool in the CI/CD pipelining stages, IZ Analyzer plays an important role here too.

### How frequently does Anypoint studio sync rules from the server? Can we sync the rules manually if required?

Anypoint Studio plugin syncs the rules from server in an interval of 6 hours. Rules ca also be manually/force synced from server using the `Force Sync Rules` option in `On The Fly Results` pane.

### Can I deactivate a built-in rule if it’s not relevant to my organization?

Yes, built-in rules can be deactivated if it’s not relevant to the organization. Follow the link to know more about deactivating built-in rules:[ De-activate built-in rules](manage-rules/deactivate-rules.md).
