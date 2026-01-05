# Automation and CI Jobs

### What is Continuous Integration? <a href="#what-is-continuous-integration" id="what-is-continuous-integration"></a>

Continuous Integration (CI) is a software development best practice of automating your test suite, so all your integration and unit tests run on every merge or pull request automatically. This way you know before you merge if problems are going to be introduced. You use a CI tool with a [Version Control System](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) (VCS) and it is best practice to require a review via pull request and enforce passing tests before the pull request can be merged. Early fixes save your company money and keep your team and users happy.

### How does CI work in practice? <a href="#how-does-ci-work-in-practice" id="how-does-ci-work-in-practice"></a>

Continuous integration allows for extremely fast and flexible development and release of code. It is also applicable to the migration of metadata. It involves short-term development, meaning that Salesforce product requirements can be adjusted without the developers having to start from scratch. In [continuous integration](https://www.autorabit.com/blog/8-advantages-of-using-salesforce-ci-tools/), developers pull the latest code from a central code repository and work on completely separate sections of code at the same time — committing and building regularly. This constant committing and automated building is the key to continuous integration as it prevents disastrous integration late in the cycle between developers working on the same project. This automation is key to making continuous integration easier and faster than the normal development cycle. Continuous and automatic testing for inconsistencies occurs throughout the process, alerting developers immediately when an inconsistency or error is found within their code. This allows for constant small adjustments to prevent code inconsistencies rather than the major time-consuming reworking of code at a later stage.

For a robust quality assurance process, use a continuous integration system, such as AutoRABIT, to run test deployments for each addition of customization to the source control repository. You can perform these deployments in a dedicated sandbox for continuous integrations. Apex tests are executed as part of each deployment.

You can use a continuous integration system to automate deployments. For example, using AutoRABIT to automate deployments to the user acceptance testing (UAT) sandbox.

## Frequently Asked Questions

### **Why does the CI job deploy all files in a Static Resource folder instead of just the changed ones?**

When deploying Static Resources using a CI job, the system deploys the **entire folder**, not just the delta (changed) files. This is **expected behavior**.

For example, even if only a `.csv` file is committed, the CI job includes all files from the Static Resource folder in the branch. This can cause deployment failures if outdated or unintended files are present.

> **Note:** EZ-Commit appends retrieved metadata to the repository and does **not remove** stale files. Removing unwanted metadata requires a **destructive commit**, which operates at the metadata level—not on individual files within Static Resources.

**Recommended Approach:**\
Before committing changes, **manually clean the Static Resource folder** in the branch to ensure only intended files are present. Use **destructive changes** if you need to remove obsolete metadata components.



For the answer to many other CI Job FAQs, visit the [FAQ page](../../../arm/troubleshoot/arm-faqs/ci-jobs.md).&#x20;

