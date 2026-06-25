# About IZ-Suite

## Steps for migration&#x20;

* Take files from the folders in IZ Suite Docs that Chethan sent&#x20;
* Copy markdown in the same file structure that is present
* Add images that are linked to the file by searching for them in the file sent by Chethan, MUST CHECK when opening markdown, because it doesn't show up once pasted in Gitbook.&#x20;
* Add in references to other pages linked at bottom of each page.&#x20;

## Introduction

**IZ Eye** continuously monitors all environments, verifying that the deployed applications are identical. This gives organizations assurance that the code in promoted environments are consistent and the Dev Sec Ops process is working as expected without any exceptions.

### Continuous Runtime Monitoring

Runtime code analyzer tool like **IZ Eye** fills this gap by continuously scanning any changes to all the environments based on the configuration and can intelligently determine when new code or API has been deployed to any of the servers.

It can identify whether the same code in dev environment has been promoted to Staging and Production environments or whether its a modified/new code deployed to the environments. It analyzes the code deployed if new and alerts based on any new vulnerabilities introduced with the deployment, so that even if the static code analysis didn’t capture the issues or if the process is bypassed, it will capture and provide an up-to-date state of the organization clearly.

This helps make sure that the organization can have a reliable way to check the runtime state of the estate - rather than just assuming that process works or to miss checking for any unauthorized deployments or changes at all!

### Keep Compliance Current (KCC)

When we have deployed hundreds of APIs/Applications which utilized various java packages or modules, in built connectors, custom connectors and libraries, we encountered two main types of changes to the security profile:

1. Critical vulnerabilities like Log4j vulnerability are discovered very frequently - and as part of company policy, they want to make sure that such vulnerabilities are quickly identified and fixed both in standard components and custom components.
2. If a company guidelines change (for example - allowed authentication methods or connectivity methods to a specific API/system changed from earlier policy to a new one or API specification guidelines are changed) - one would like to identify the technical debt easily.

Whenever guidelines change like this and they had hundreds of applications and APIs, the usual way of scanning each and every application/API is a huge laborious process. How do we get around this issue?

With a tool like IZ Runtime Analyzer, whenever a company adds or modifies their policy guideline, this will trigger a complete re-analysis of the entire affected infrastructure applications/APIs, so that an organization readily obtains an updated report on the compliance of the organization. Any application which was compliant under the old guideline or rule set could be either compliant, partially compliant, or noncompliant according to the new set of guidelines. This reduces the huge overhead on the DevSecOps team to re-trigger analysis of the entire application code base to analyze things, as well as capture rogue/bypassed applications according to the new guidelines to always keep the compliance current. In summary, IZ Runtime Analyzer provides the ability to re-scan the entire application infrastructure so that compliance of the organization remains current no matter the frequency or type of guideline change.

### Coverage Analysis

In **IZ Eye**, not only component-level code/specification is scanned with issues and metrics captured, it provides a capability of linking the assets across the entire estate. This enables an easy way of analyzing the compliance data in one shot, whether you would like to understand it at component level, summary level, or based on custom tag level!

This enables a true compliance dashboard specific to whatever level of data that you desire and analyzes the risk associated with issues discovered by the tool.
