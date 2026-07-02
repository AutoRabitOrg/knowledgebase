# About IZ Analyzer

## Introduction

**IZ Analyzer** covers basic concept of continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs, code smells, and security vulnerabilities. Well integrated with [SonarQube™](https://www.sonarqube.org) offerings like reports on duplicated code, coding standards, unit tests, code coverage, code complexity, comments, bugs, and security vulnerabilities.

### Motivation

1. Unavailability of Mule code review tool
2. Unavailability of (RAML/OAS) code review tool
3. Unavailability of WSO2 code review tool
4. Unavailability of a issue auto fix functionality
5. Code quality checks
6. Non-centralized continuous inspection

### User Journey Illustrated

* Flow below illustrates overall user journey to achieve continuous inspection via IZ Analyzer:
  * User Install IZ Analyzer to start with.
  * Opt one of the installation path Studio Plugin/Server Plugin
  * Developers code in their Anypoint Studio / WSO2 Integration Studio and use _IZ Analyzer Plugin_ to run local analysis and _Auto Fix_ issues.
  * _Template rule_ is a new **feature** added, this enables user to define their custom rule and respective code.
  * _Anypoint Studio Plugin_ supports scanning and uploading results to server.
  * _Analyzer Server_ processes and stores the analysis report results in Database, and displays the results in UI.
  * Developers review, comment, challenge their Issues to manage and reduce their Technical Debt.

#### Details

* [Manage Studio Plugin](../integral-zone/iz-suite/iz-scan/anypoint-studio/installation/install-iz-analyzer-studio.md)
* [Manage Server Plugin](../integral-zone/iz-analyzer/manage-server-plugin/install-server-plugin.md)

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
