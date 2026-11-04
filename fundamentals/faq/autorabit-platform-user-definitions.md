# General User Definitions

{% hint style="info" %}
**ARM-Specific User Definitions**: The information below is generalized across the entire AutoRABIT suite of products. For information specific to ARM, please refer to the ARM User Definitions page [here](https://knowledgebase.autorabit.com/~/revisions/r1tfuUId2G5l58MjsNr3/product-guides/arm/arm-administration/user-management/arm-user-definitions).&#x20;
{% endhint %}

**Standard User**

A Standard User is an individual authorized by the Customer to log in to and fully utilize AutoRABIT’s subscribed products. Standard Users have access to all product functionalities, including the Web UI, IDE plugins, APIs, and other interfaces.&#x20;

Platform Owners/Admins are included in the Standard User class, ensuring administrative rights without affecting licensing terms.&#x20;

**Platform Integration User**&#x20;

A Platform Integration User is an individual authorized by the Customer to perform actions that trigger the execution of AutoRABIT products (directly or indirectly). &#x20;

This includes, but is not limited to:&#x20;

* Analyzing reports or data from AutoRABIT to identify and resolve code quality, security, compliance, or system performance issues.&#x20;
* Agents, bots, or systems executing actions via AutoRABIT to automate testing, deployments, or compliance checks.&#x20;
* Using AutoRABIT IDE plugins&#x20;
* Triggering AutoRABIT APIs&#x20;
* Directly changing Salesforce org configurations&#x20;
* Committing changes to a source code repository&#x20;

**Key Points:**&#x20;

* Automation (e.g., bots, agents) utilizing AutoRABIT for testing, deployment, or monitoring must be licensed appropriately.&#x20;
* Any person who commits code to a Source Code Management (SCM) system, where the commit directly or indirectly triggers a job in AutoRABIT, requires a Platform Integration License.&#x20;
* If a service account is used to trigger automation or integrate with AutoRABIT, the person or team responsible for the actual code commit must still hold a Platform Integration License. This ensures that each individual whose actions contribute to triggering AutoRABIT processes is appropriately licensed.&#x20;
* Any code commits triggering AutoRABIT jobs, directly or indirectly, manual or automate&#x64;**,** count toward Platform Integration Licenses.&#x20;

Example: In Git, multiple commits pushed simultaneously are counted individually toward user licensing.&#x20;

Platform Integration Users are included in licensing with view-only permissions.&#x20;

**Additional Notes:**&#x20;

* The number of licensed users represents the total unique users of the products throughout the Subscription Term.
