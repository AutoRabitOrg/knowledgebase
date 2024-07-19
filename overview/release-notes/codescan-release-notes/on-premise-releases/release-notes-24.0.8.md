# Release Notes 24.0.8

## CodeScan On-Premises&#x20;

### Release 24.0.8

**19 July 2024**

1. **Rule enhancement for Misuse of Assert Class**\
   Included the ability to configure parameters for the "Misuse of Assert Class" rule, specifically for the Assert methods Assert.isFalse, Assert.isNotNull, hard-coded values, and Assert.areEqual, so that user can customize the rule to better fit the coding standards and practices of their project.
2. **Rule Enhancement for “Avoid Using Test.isRunningTest()” {APEX Rule}**: Previously, this rule was flagging violations when finding methods written as Test.isRunningTest(). This rule has been enhanced to also flag violations when finding methods written as System.Test.isRunningTest().
3. **Decrease False Positives reported for Rule “sf:FixDuplicateMethods” Summary**: CodeScan recognizes that methods should not share the same implementations. As such, the scope of the rule will be limited to methods with actual implementations, rather than including interface method declarations. This means the rule will now focus solely on detecting and addressing duplicate implementations within concrete classes, ensuring that only methods containing executable code are evaluated. Violations reported by this rule will now include details of all duplicate methods affected. This means each violation will list every instance of a method that shares the same implementation, making it easier to identify and resolve duplicated code. These updates will make the rule more precise, and its violation reports more comprehensive, enhancing its effectiveness.
4. **Enhancement to Rule "Field-Level Security" (FLS)**: CodeScan’s FLS rule did not detect DML methods called when syntax is insert (record), update (record), etc. Instead, FLS was only detecting when “insert record;” syntax was used. We made a parser update within CodeScan and an enhancement to the rule was applied, which corrected the syntax detection.
5. **Enhancement to Rule "Cyclomatic Complexity" Summary:** Several enhancements were applied to the rule cyclomatic complexity, including adding the decision points '?', '&&', '||', and 'catch'.
6. **New Rules:** CodeScan Polyfill Protection \
   We are excited to announce that CodeScan has been updated with crucial enhancements to address recent security concerns related to polyfills. Recent advisories have highlighted significant threats stemming from polyfills, particularly those distributed via the CDN polyfill.io, which are linked to malware. This update introduces advanced protection mechanisms to ensure your Salesforce environment remains secure.

Here’s how CodeScan is advancing your security:

1. **Configuration Scanning:** Our enhanced system now scans the configuration settings of Salesforce components, including Salesforce Sites, Salesforce CORS (Cross-Origin Resource Sharing), and Salesforce CSP (Content Security Policy), to detect any unauthorized calls to polyfill.io domains.
2. **Component Scanning**: We are scanning the core Salesforce components that enable developers to build sophisticated, custom user interfaces including Visualforce, Aura, Lightning, and other web components
3. **Package Scanning**: Our updated scanning mechanism checks downloaded packages from Salesforce AppExchange to ensure they do not contain insecure calls to polyfill.io domains

Activate the Polyfill rules, Avoid Script References to Polyfill.io, and Avoid Configuration References to [Polyfill.io](http://polyfill.io/) to your custom quality profile to begin using them.

### Rule Updates

1. The 'Hard-Coded Credentials' rule name has been changed to 'Use Named Credentials' for clarity.
2. 'Use Named Credentials' and 'Field-Level Security' rules have updated descriptions highlighting Salesforce best practices and better paths to resolution.

### Bug Fixes

Fixed a false positive in the rule 'Avoid using methods getDescribe and getMap inside Loops' when using custom methods with similar names.
