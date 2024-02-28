# Release Notes 24.0.1

## CodeScan Self-Hosted

### Release Notes 24.0.1

This update introduces several new rules and bug fixes for current rules and the CodeScan analysis. This includes:

**Flow Rules**

There are 19 new rules for Salesforce flows:

* **Inactive flows should be removed:** Inactive flows may cause clutter in the Salesforce org. In extreme cases, they can begin to hit the organization’s limits. These should be removed if not being used.
* **Avoid Large Flows**: Too many nodes can cause your Flow to become complex and unmanageable. Consider using Subflows to make your Flow logic reusable and scalable.
* **DML statements should not be included in the loops:** SOQL and DML in Salesforce is bound by “Governor Limits.” If a large number of SOQL and or DML calls are made in a short amount of time, you can run into a Governor Limit Exception. This rule minimizes the chances of this by letting the user know when they are calling these in a loop.
* **Avoid creating nested loops in flows:** Nested loops within your Flows can cause them to become unreadable, inefficient, and complex. Consider using Invoked Actions to clean up complex Flows.
* **Document Flows and the flow components:** Flows should have adequate documentation. Any flow elements without a description should have a violation thrown independently.
* **Avoid Hard-Coded Values in Flows:** Hard-coded values in flows can lead to unexpected output and make maintenance difficult. Instead, Get Records can be used for the respective object using the DeveloperName. If you’re creating criteria in an entry condition, you can reference DeveloperName (API Name) fields with a formula.
* **Flows Should Include Fault Paths:** Fault paths are a way to handle errors that may occur in your Flow. Depending on the Flow and its purpose, errors can be logged, show an error screen, or send an email of the failure to a group of users. Flows should include Fault paths to ensure that all errors are handled appropriately.
* **Flow Naming:** Standardized naming conventions allow an organization's Flows to be clean, maintainable, and readable. This rule enforces standard naming conventions for Flows and Domains.
* **Flow Variables & Resources Naming:** This rule enforces standard naming conventions for Variables, Formulas, and Choices.
* **Flow Interaction Naming:** This rule enforces standard naming conventions for Screens, Actions, and Emails.
* **Flow Logic Naming**: This rule enforces standard naming conventions for Decisions, Assignments, and Loops.
* **Flow DML Naming:** This rule enforces standard naming conventions for DML operations (Query, Update, Create, Delete).
* **Migrate Workflows and Processes to Flows:** Process Builders and Workflows are being phased out over the coming year. In Winter '23 the ability to create new Workflows is being turned off, in Summer '23 the ability to create new Processes with Process Builder was turned off. It is recommended that these Processes and Workflows be migrated to Flows.
* **Use Fast Field Updates:** If a Flow is only updating the record that triggered it, it should be using the Fast Field Updates option. This can be up to 10 times faster than the more flexible Actions and Related Records Flow.
* **Get Records Should Be Filtered:** This rule mandates the usage of at least one filter in the Data element "Get Records" within Salesforce Flows. Enforcing this rule will encourage flow designers to think critically about their data retrieval needs and apply relevant filters, reducing the risk of performance bottlenecks and unoptimized queries.
* **Unused Flow Variables:** Consider removing unused Flow variables to increase performance and readability.
* **Missing Null Handler After Get Records in Flow:** By implementing a decision element to validate the result of the Get Records operation, you can proactively identify and handle cases where no data is retrieved. This allows you to avoid potential null reference errors and prevent unexpected crashes or data processing issues.
* **Duplicate DML operations in Flows:** This rule aims to avoid potential issues caused by duplicate database operations that might occur if users go back and forth between screens, triggering the same actions multiple times.
* **Flows API Version Is Too Old:** This rule identifies flows that are using older API versions. Consider updating the API versions of any flows found.

**Bug Fixes:**

* Rule Misfire fixed: Corrected Apex code incorrectly detecting TODOs.
* Fix provided for the rule “Avoid Using Hard Coded Credentials for Authentication”: Regex updated.
* Xpath added for the rule "SOQL Injection possible" to cover the public and class-level variables.
* License Key Update: The license has been updated and will now be associated with specified projects.
* Parser issue fixed on the rule: “Avoid Untrusted/Unescaped Variables in DML Query."
* A new rule parameter, allowList, added to the rule “Track Usage of @SuppressWarnings.”
* Fix provided for an error running a scan of the Salesforce-VA org.
* Apex Parser Update for Null Coalescing Operator: There will be no parsing error when ?? is present in Apex code.
