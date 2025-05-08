---
description: CodeScan Cloud Release Notes
---

# Release Notes 25.1

## Integration Requirements for CodeScan v25.1.0

Please note that there are updated requirements for customers who are using one or more of the following to integrate with CodeScan:

* SFDX
* SonarScanner
* ADO
* VS Code
* IntelliJ&#x20;

### Overview

For customers who are using the SonarScanner in CI/CD pipelines and/or using the SFDX plugin, the latest CodeScan release (v25.1.0) now requires Java 17 and Node.js 20 for these integrations.  Further, IDE integrations (VS Code and IntelliJ) also require these upgrades.

While this change may not affect all users, any customer who is dependent upon automated builds and pipelines and/or running CodeScan plugins locally (via CLI or IDE) should review and update their Java and Node.js versions to ensure continued compatibility.&#x20;

### Affected Integrations, Required Updates, and Actions Required

1. **VS Code Plugin**&#x20;
   * **Requirement**: Java 17 and Node.js 20 LTS&#x20;
   * **Latest version**: VS Code CodeScan plugin v2.1.0&#x20;
   * **Action Required**: Upgrade to latest version of the plugin and restart VS Code after verifying installations.&#x20;
2. **IntelliJ IDE Plugin**&#x20;
   * **Requirement**: Java 17 and Node.js 20 LTS&#x20;
   * **Latest version**: IntelliJ CodeScan plugin v7.3.0&#x20;
   * **Actions Required**: Upgrade to the latest version of the plugin and restart the IDE to apply changes.&#x20;
3. **SonarScanner CLI**&#x20;
   1. Download SonarScanner v5.0.1.3006 (comes pre-bundled with Java 17).&#x20;
   2. Verify SonarScanner is a supported version using the command: _sonar-scanner –v_
   3. Run Scan: \
      sonar-scanner ^ \
      -Dsonar.host.url=https://app.codescan.io -Dsonar.organization={org} ^ \
      -Dsonar.projectKey={projectKey} -Dsonar.token={token}
4. **CodeScan SFDX Plugin**&#x20;
   * **Latest version**: CodeScan SFDX plugin v1.0.9&#x20;
   * **Action Required**: Ensure the latest version of SFDX plugin is being used.
5. **CodeScan Azure Plugin**&#x20;
   * **Latest version**: CodeScan Azure plugin v2.0.1
   * **Action Required**: At the "Run Code Analysis" step, select the correct JDK version source for analysis (use the built-in JAVA\_HOME\_17\_X64 on hosted agents or specify JAVA\_HOME as 17).

### Additional Notes

* The environment running your Salesforce CLI requires an upgrade to JDK 17 and NodeJS 20. Typically, organizations run the Salesforce CLI either in a docker container or on a CI/CD server.  Alternatively, the CLI could be run with a dev environment (either locally or in a shared environment \[like a cloud-based IDE]).
* Node.js v20 should be accessible via system PATH. Node is a mandatory requirement for analyzing JavaScript files.&#x20;
* A new version of CodeScan plugin for VS Code (v2.1.0) is available on the VS marketplace at [https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode.](https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode.) You can also install it directly from extensions within VS Code. Please note that users running their IDEs locally need to ensure that they are running JDK 17 and NodeJS 20.
* A new version of the CodeScan plugin for IntelliJ (v7.3.0) is available on the JetBrains marketplace at [https://plugins.jetbrains.com/plugin/16087-codescan](https://plugins.jetbrains.com/plugin/16087-codescan). You can also install directly from extensions within IntelliJ.  Please note that users running their IDEs locally need to ensure that they are running JDK 17 and NodeJS 20.

## Release Notes 25.1.0&#x20;

**Release Date: 20 April 2025**&#x20;

### Summary:&#x20;

CodeScan 25.1.0 is comprised of two main components / features:&#x20;

* [New User Interface ](release-notes-25.1.md#new-user-interface)
* [Technical Architecture Improvements ](release-notes-25.1.md#technical-architecture-improvements)

Component details are listed in their corresponding sections within this document.&#x20;

### New User Interface&#x20;

In this release, we have updated the CodeScan User Interface order to provide four key benefits:&#x20;

* Easier navigation, which provides both an improved, intuitive experience for more advanced users, while reducing the learning curve for new users
* Consistency in screen layout, providing a more cohesive experience throughout the application  &#x20;
* Enhanced performance and responsiveness within CodeScan&#x20;
* Brand modernization alignment with other AutoRABIT solutions&#x20;

<figure><img src="../../../../.gitbook/assets/image (1).png" alt=""><figcaption><p>UI Upgrades</p></figcaption></figure>

{% hint style="info" %}
Please note: CodeScan documentation pages will have new images to reflect the latest UI changes over the coming weeks. This should not affect the effectiveness of instruction steps in the meantime.&#x20;
{% endhint %}

### Technical Architecture Improvements&#x20;

* The CodeScan 25.1.0 contains various technical architecture improvements and upgrades to various libraries. We have also included several enhancements to CodeScan’s security architecture.

&#x20;&#x20;

&#x20;

&#x20;
