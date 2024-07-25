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

