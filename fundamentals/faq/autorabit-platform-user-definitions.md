# AutoRABIT Platform User Definitions

**Standard User** A Standard User is an individual authorized by the Customer to log in to and directly use AutoRABIT’s subscribed products.

**Platform Integration User** A Platform Integration User is an individual authorized by the Customer to perform actions that trigger the execution of AutoRABIT products (directly or indirectly). This may include, but is not limited to:&#x20;

• Using AutoRABIT IDE plugins&#x20;

• Triggering AutoRABIT APIs&#x20;

• Directly changing Salesforce org configurations&#x20;

• Committing changes to a source code repository

**Key Points:**&#x20;

• Any person who commits code to a Source Code Management (SCM) system, where the commit directly or indirectly triggers a job in AutoRABIT, requires a Platform Integration License.&#x20;

• If a service account is used to trigger automation or integrate with AutoRABIT, the person or team responsible for the actual code commit must still hold a Platform Integration License. This ensures that each individual whose actions contribute to triggering AutoRABIT processes is appropriately licensed.

**Example:** In Git, a popular SCM system, multiple commits can be pushed simultaneously. Each commit is counted separately toward the user license. 

A Platform Integration User does not need to log in to the AutoRABIT Web UI to be counted as a user but will have view-only permissions included in their license.

**Additional Notes:**

• Platform Owners/Admins are included in the Standard User class, allowing customers to manage admin rights without affecting the licensing terms.&#x20;

• The number of licensed users represents the total unique users of the products, calculated throughout the entire course of the Subscription Term.
