# AutoRABIT Platform User Definitions

**Standard User:**

An individual authorized by the Customer to log in to and use the AutoRABIT subscribed Products directly. The licensed User quantity is the total number of unique Users of the Products calculated over the course of the entire Subscription Term.

**Platform Integration User:**

An individual authorized by the customer to perform actions that trigger the execution of AutoRABIT products (e.g., using AutoRABIT IDE plugins, triggering AutoRABIT APIs, directly changing Salesforce org configuration, or committing changes to a source code repository).

A Platform Integration User includes any person who commits code to a Source Code Management (SCM) system where that commit directly or indirectly results in triggering a job in AutoRABIT software.

Even if the SCM repository uses a service account to trigger automation, the person who is responsible for the actual code commit must have a Platform Integration License.

For instance, in Git, the most popular SCM system, a collection of commits can be submitted (pushed) to the SCM at one time. Each commit is counted separately.

A Platform Integration User does not need to ever log in to the AutoRABIT Web UI to be counted as a user.

However, they will have view-only permissions to the AutoRABIT Web UI included in their license.

**Other Notes:**

Platform Owner/Admin is part of the standard user class. This allows customers to grant and revoke admin rights without any implications on licensing.

**How to Count Users:**

Count the number of users with commit permissions in any Source Code Management system that you intend to integrate with AutoRABIT, specifically those source code repositories that will have builds triggered from those commits. Also, count users who will access AutoRABIT via an IDE such as the VS Code plugin, or via API.

Count the number of users who will exclusively log in directly to AutoRABIT via the UI. These users may include administrators, end users, or those users logging in to view build results or other reports. Do not include users already counted as commit users.

Estimate your rate of attrition for the proposed term year and the number of new hires that will backfill those employees. A user is a named person, and new hires will require their own license.

Estimate the expected growth of your login and commit users for the proposed term year. Ensure enough headroom in your user count to accommodate onboarding new teams onto AutoRABIT as well as any additional new hires.

The total of the above is the estimated user count.

**User Count Framework**

Framework – To identify and understand the customer's current practices, pain points, and determine the roles involved in deployment, development, and integration processes.

By asking the below questions, we should be able to understand how many users get value from our Products or Services.

Broadly these questions aim to capture how many resources are involved in managing the code and configuration of Salesforce.

This would help us map the ARM Standard User and ARM Platform users.

**Salesforce Questions**

* What do you use Salesforce for – core use cases?
* How many end users do you have on Salesforce?
* What Salesforce editions and features are you currently utilizing?
* How many of your Salesforce end users are considered Standard users?
* What is the volume of data processed and stored in Salesforce?
* How many custom objects and fields are currently in use in your Salesforce environment?
* How many Salesforce integrations with external systems do you currently maintain?

**Regular Course of Business Questions**

* What is the size of your development team? Do all of them use source control?
* How many team members are involved in code integration processes?
* Who is responsible for managing deployments within your team?
* How many Business Analysts are directly involved in making changes to the code or configurations?
* How do you track and manage the work done by BAs in the development or configuration process?
* Are there specific integrations or tools you rely on? (Jira, Selenium, etc.)
* How frequently do you release updates to your Salesforce environment?
* How many Repos do you use for managing Salesforce code?
* What is the average number of code commits per week per source code user?
* How do you foresee your deployment and development processes evolving?

**Security and Compliance Questions**

* How do you manage Salesforce user permissions and security settings?
* Do you have a dedicated team for managing Salesforce deployments?
* Are there any compliance requirements you are aware of?
