# Release Notes 22.2

### CodeScan 22.2 <a href="#codescan-222" id="codescan-222"></a>

**Released Date: 26 Jan 2022**

#### New Features <a href="#new-features" id="new-features"></a>

* **New compliance rules added for Apex Class**:
  * **Long Class Names**: In the Apex class ruleset, we have added a new rule “Long Class Name” You can now configure an Apex Class with a class name that is longer than 40 characters.
  * **Long Trigger Names**: In the Apex class ruleset, we have added a new rule “Long Trigger Name”. You can now configure an apex trigger with a trigger name that contains more characters than the set limit.
  * **Long Method Name**: In the Apex class ruleset, we have added a new rule “Long Method Name”. This rule helps to create an apex class rule with a method name that contains more characters than a set limit.
* **New compliance rules added for Salesforce Metadata**:
  * **Avoid Excess Workflow Rules in Org**: In the Salesforce metadata ruleset, we have added a new rule “Avoid Excess Workflow Rules in Org”. This rule helps to limit the number of workflow rules in your salesforce org.
* **Project Analysis Log Report**: We've added a new feature that allows users to view their project analysis report by clicking on a link from their VC project. As a result, the user can now view the detailed log report.

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* **Log4j Version**: Updated the latest version of log4j to 2.17.1 to address the Apache Log4j security vulnerabilities.
* **Scheduled project reports**: Users with Administrator permission either at the project level or organization level can configure the scheduled project reports. Earlier, this option was available only to the owners of the organization.
* **Analyze salesforce packages**: Users can now analyze the contents of salesforce packages. This will help to keep track of issues in files packages. This feature is especially helpful when the packages are developed and maintained by the user.

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* There was an issue with project reports not being triggered when they were scheduled; this has now been fixed.
