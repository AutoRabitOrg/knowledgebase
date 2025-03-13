# 🛠️ Getting Set Up

## What is AutoRABIT? <a href="#what-is-autorabit" id="what-is-autorabit"></a>

AutoRABIT is a cloud-based CI/CD and release automation suite specifically designed for Salesforce.com. AutoRABIT helps Salesforce developers, admins, analysts, and release managers automate version control, deployment, testing, data loading, and sandbox management across multiple Salesforce orgs.

## What does AutoRABIT do? <a href="#what-does-autorabit-do" id="what-does-autorabit-do"></a>

AutoRABIT delivers a unified CI/CD solution purpose-built for Salesforce. The ease of use provided by AutoRABIT makes it much easier for Salesforce administrators and developers to leverage an enterprise-class DevOps process to accelerate their journey from defining requirements to deploying code.

## What do I need to get started?

### Salesforce

Salesforce is a web-based Customer Relationship Management (CRM), which is an essential cloud application that the ARM tool works with to build a successful **CI/CD pipeline**. Therefore, whether you are in support, engineering, enterprise services, product, or customer success, it is essential to have a Salesforce environment to replicate bugs, train, or verify bug fixes.&#x20;

Salesforce provides a full copy of the **Lightning Platform** for free. This means you can get your own Developer Edition to integrate with ARM for free by signing up at: https://developer.salesforce.com/signup.&#x20;

### Version Control System&#x20;

In addition to Salesforce, it is critical to have a **Version Control System** to ensure that the version control is the source of truth. There are several Version Control Systems out there, including **GitHub**, **Bitbucket**, and **Azure DevOps Server** (formerly known as TFS \[Team Foundation Server]). Each client may utilize a different Version Control System, but ARM allows you to connect to the three most popular Version Control Systems: **GIT**, **SVN**, and **TFS**.

### Microsoft Visual Studio Code

In addition to Developer Edition orgs and a Version Control System, having **Microsoft Visual Studio** **Code** is beneficial. Microsoft VS Code is a powerful source code editor on your desktop. You can download Visual Studio Code, which integrates GIT for Windows, macOS, and Linux. Follow this link to download for your appropriate platform: [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

### Git Bash

In addition to the tools mentioned above, it is recommended to install **Git Bash**. The URL to download Git Bash for Mac OS X, Windows, Linux/Unix can be found here: [https://git-scm.com/downloads](https://git-scm.com/downloads). Git Bash is a command line through which users can use Git features, including standard Unix commands. One of the common Unix commands available through Git Bash is to add a file to your existing Git repository:

```actionscript
# create new file
$ touch README
```
