# Release Notes 22.1

### CodeScan 22.1 <a href="#codescan-221" id="codescan-221"></a>

**Released Date: 29 Dec 2021**

#### New Features <a href="#new-features" id="new-features"></a>

* **Integrated ZOHO as a ticketing tool for CodeScan support**: We've now integrated ZOHO as a way to submit a ticket for any CodeScan-related support. The AutoRABIT Support Portal allows users to submit a support request.
* **New Compliance rules for Salesforce Metadata**: We made our Salesforce Metadata Ruleset more powerful with the addition of two new rules that helps minimize and prevent the Salesforce users from being provided with unnecessary privileges.
  * **Limit number of page layouts per object**: In the Salesforce Metadata ruleset, we added a new rule "Limit number of page layouts per object" which helps to restrict the maximum number of page layouts that can be accommodated under a single object.
  * **Limit number of custom fields per object**: In the Salesforce Metadata ruleset, we added a new rule "Limit number of custom fields per object" which helps to limit the number of custom fields set for a salesforce object. The rule also allows users to specify object-specific custom field limits.

#### Enhancement <a href="#enhancement" id="enhancement"></a>

* **Log4j2 core and API versions are upgraded to 2.17.0**: To address the Apache Log4j Security Vulnerabilities thread, we updated the Apache Log4j version dependencies to 2.17.0.

#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* The user was unable to delete multiple projects from the Manage Projects page due to a bug, which has now been resolved.
* After deleting and adding a new repository into the CodeScan, we were getting an '**Unknown erro**r'. It has been fixed now.
* There was an issue in CodeScan Cloud where you couldn't create a branching, but it's now fixed and working properly.
* When a user attempts to analyze a project by clicking 'Re-run the analysis,' it fails. This problem has now been resolved.
* There was an issue with the links from GitHub fork PR and it is not linking to the correct branch. This issue has been fixed now.
