# Release Notes 4.2

### CodeScan 4.2 <a href="#codescan-42" id="codescan-42"></a>

#### New Features <a href="#new-features" id="new-features"></a>

**New Apex Rules**

* **Avoid Insecure Digest Algorithms**: MD5 and SHA-1 algorithms are no longer considered secure because it's too easy to create a hash collision between two message contents.
* **Avoid Salesforce System Class Names**: Classes with names that already exist as internal classes will take precedence due to namespacing.
* **Avoid Nested Switch Statements**: Avoid creating nested 'switch' statements since they are error-prone, harder to read, and harder to maintain.
* **Avoid Reversed Operators**: Reversing operators may be a bug, or at the very least make it hard to read.
* **Avoid Using HTTP Referer Headers**: HTTP Referer headers can be modified by attackers. Making a decision based on the value of the referer can be dangerous.
* **Catch Block Should Do More Than Rethrow**: Catch blocks that do nothing but rethrow an exception should either be changed or removed.
* **Field Level Security Vulnerabilities**: This rule makes sure that the code checks for access permissions before running a SOQL, SOSL, or DML operation.\
  **Single Method Singleton**: Avoid using overloaded getInstance methods.\
  Statements Should Be On Separate Lines\
  Statements should be on separate lines to increase readability and maintainability.
* **Suspicious For Loop Incrementer**: Incrementers that do not match the body of the for loop could be a bug.
* **Ternary operators that can be simplified with || or &&**: Ternary operators with the form `condition ? literalBoolean : foo` or `condition ? foo : literalBoolean` can be simplified.
* **Unexpected Casting of Types**: When arithmetic is performed on a type, the type remains the same even if the result is a different type. This can return an unexpected result.

**Updated Apex Rules**

* **Division By Zero**: Division by zero exception may occur when zero could be the denominator to a division or modulo operation.
* **Apex Classes should use Random IV/Key**: Now checks for EncodingUtil.base64Decode(key);

**New Visualforce Rules**

* **Avoid using GETSESSIONID() and $API.Session\_Id**: Lightning Experience does not have access to the API session token. Visualforce pages that access the session ID should be tested within Lightning Experience.
* **External Script and Style Resources Should Be Avoided**: Including content from untrusted sources can lead to various security issues including include injection of malware.
* **Remove OnClick Javascript**: Javascript in "onclick", "onmouseover" and similar actions within components are ignored.
* **Require CSRF Protection On GET Requests**: Require CSRF protection on GET requests must be enabled from the Visual Force Page settings.
* **Unencoded Formulas In Style Tags XSS**: Makes sure that all values obtained from URL parameters are properly escaped / sanitized to avoid XSS attacks.
* **Unescaped Value Could Cause XSS**: Reflected Cross-site Scripting (XSS) occurs when an attacker injects browser executable code within a single HTTP response. Using unescaped parameters can be a security risk.
* **Avoid Apex Tags Within Script**: Avoid using \<apex:\*> tags within \<script> tags for readability and security.

#### &#x20;Enhancements <a href="#enhancements" id="enhancements"></a>

* Improved documentation on vulnerabilities including links to OWASP and CERT explanations.
* Support for Inherited Sharing Keywords in Apex - [Salesforce Documentation](https://help.salesforce.com/s/articleView?id=release-notes.rn\_apex\_inherited\_sharing.htm\&type=5\&release=216)

\


#### Bug Fixes <a href="#bug-fixes" id="bug-fixes"></a>

* Code coverage that does not match the current state of the codebase no longer causes unrecoverable errors (**v4.2.0**)
* Fixed bug that caused component files to not scan correctly (**v4.2.2**)
* Fixed issue that caused certain tags starting with "\\" in comments to not parse (**v4.2.3**)
* Fixed issue that caused code coverage to not be applied. (**v4.2.3**)
* Fixed bug in Long Javascript rule that causes the length to be improperly calculated (**v4.2.3**)
* Fixed issue that caused files to not highlight correctly **(v4.2.3**)
* Fixed bug that caused Class Without Test Class rule to ignore certain files (**v4.2.3**)
* Fixed bug that caused errors to appear and disappear (**v4.2.3**)
* Fixed bug that caused certain code coverage data to be displayed incorrectly (**v4.2.5**)
* Fixed bug in the Class Without Test Class rule (**v4.2.6**)

\


#### Other Changes <a href="#other-changes" id="other-changes"></a>

* The rule "Class with only Private Constructors should be Final" has been deprecated and removed completely.  Classes are final by default therefore this rule is unnecessary.
* The rule "Remove OnClick Javascript" has been removed from the default Visualforce and Lightning Quality Profile.
* SonarQube™ 7.6 Support
* A selection of new rules has been added to the default Quality Profiles (**4.2.1**).
