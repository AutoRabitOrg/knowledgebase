# Understanding Quality Gates

## **What Is a Quality Gate?**

A quality gate is an indicator that determines whether your code meets the minimum quality standards for your project. It consists of a set of conditions applied to the results of each analysis. If the results meet or exceed these conditions, the status is "Passed"; otherwise, it is marked as "Failed."

A Quality Gate consists of measure-based, Boolean conditions that allow you to quickly assess whether your projects are production-ready. Ideally, all projects should utilize the same quality gate, with each project's quality gate status clearly visible on its homepage.

CodeScan will provide standard values for each metric in the default (built-in) quality gate (sonar way). However, the quality gate can be customized to align with your organization’s standards.

<figure><img src="../../../.gitbook/assets/Q gate 9.7.png" alt=""><figcaption></figcaption></figure>

**Important Note:** Built-in quality gates are standard and cannot be edited.

See more information on [Sonar Way](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates/), the recommended quality gate. We consider these conditions for our default quality gate.
