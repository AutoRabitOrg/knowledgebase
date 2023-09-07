# Release Notes 4.5

### CodeScan 4.5 <a href="#codescan-45" id="codescan-45"></a>

#### New Features <a href="#new-features" id="new-features"></a>

**New Cloud Features**

* **Native GitLab Integration**: Your GitLab cloud repo's are now just one click away from our new GUI integration.
* **Verbose Billing Warnings**: Billing warnings will now be more verbose.

**New Apex Rules**

* **Avoid using null conditions in SOQL WHERE clause:** by default, index tables do not include null records. WHERE clauses that include nulls will therefore require a full scan, which can be very slow for large data volumes. The developer must determine if a fix is needed.
* **Page Action with a simple redirection**: avoid creating a page action that makes a simple client side redirect.
* **Sending outbound emails using Messaging.sendEmail**: emails sent with Messaging.sendEmail count against daily limits which can cause rejection. The developer must determine if a fix is needed.
* **Using Batch Apex from a trigger is dangerous**: ensure that jobs created by the trigger do not exceed job limit.
* **Using Database.AllowCallouts interface in Batch Apex**: it is not recommended to make HTTP calls as part of Batch Apex logic.
* **Source files should have a sufficient density of comment lines (v4.5.3)**: this version of the rule is able to be used in the IDE. An issue is created on a file as soon as the density of comment lines on this file is less than the required threshold.

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* DMLWithoutSharingEnabled now takes Inheritance into account (**v4.5.2**).
* FieldLevelSecurity now has a parameter to check classes that extend system level classes ie. Database.Batchable, Queueable, and Install Handler (**v4.5.3**).
* CommentRequired now checks for private methods via parameter (**v4.5.3**).

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* Parsing issues for the Safe Navigation Operator fixed (**v4.5.1**).
* False positive fixed in SOQLInjection (**v4.5.1**).
* False positive fixed in AuraEnabledWithoutCatchBlock (**v4.5.1**).
* Parsing fixes for Javascript annotations (**v4.5.2**).
* EsLint configuration files are no longer picked up with analysis (**v4.5.3**).
* False positive fixed in BadCrypto (**v4.5.3**).
* False positive fixed in UseSingleton (**v4.5.5**).
* IDE Plugin no longer creates files in the base directory (**v4.5.5**).
* False positive fixed in FieldLevelSecurity (**v4.5.6**).
