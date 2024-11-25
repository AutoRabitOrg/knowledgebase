# SonarQube

### SonarQube: Overview <a href="#sonarqube-overview" id="sonarqube-overview"></a>

SonarQube is an automatic code review tool to detect bugs, vulnerabilities, and code smells in your code. It can integrate with your existing workflow to enable continuous code inspection project branches and pull requests.

### SonarQube: Concepts

#### Architecture <a href="#architecture" id="architecture"></a>

<table data-header-hidden><thead><tr><th width="200"></th><th></th></tr></thead><tbody><tr><td><strong>Concept</strong> </td><td><strong>Definition</strong> </td></tr><tr><td>Analyzer </td><td>A client application that analyzes the source code to compute snapshots. </td></tr><tr><td>Database </td><td>Stores configuration and snapshots. </td></tr><tr><td>Server </td><td>Web interface that is used to browse snapshot data and make configuration changes. </td></tr></tbody></table>

#### Quality <a href="#quality" id="quality"></a>

Issue types (bug, vulnerability, and code smell) are deprecated. Issues are now tied to Clean Code attributes and software qualities impacted. See [Clean Code](https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/) for more details.

<table data-header-hidden><thead><tr><th width="198"></th><th></th></tr></thead><tbody><tr><td><strong>Concept</strong></td><td><strong>Definition</strong></td></tr><tr><td>Clean Code</td><td>Code whose attributes make your software reliable, secure, and maintainable. See <a href="https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/">Clean Code</a> for more details.</td></tr><tr><td>Bug</td><td>An issue that represents something wrong in the code. If this has not broken yet, it will, and will probably break at the worst possible moment. This needs to be fixed as soon as possible.</td></tr><tr><td>Code smell</td><td>A maintainability-related issue in the code. Leaving it as-is means that at best, developers maintaining the code will have a harder time than they should when making changes. At worst, they'll be so confused by the state of the code that they'll introduce additional errors as they make changes.</td></tr><tr><td>Cost</td><td>See Remediation cost.</td></tr><tr><td>Debt</td><td>See Technical debt.</td></tr><tr><td>Issue</td><td>When a piece of code does not comply with a rule, an issue is logged on the snapshot. An issue can be logged on a source file or a unit test file. </td></tr><tr><td>Measure</td><td>The value of a metric for a given file or project at a given time. For example, 125 lines of code on class MyClass or, the density of duplicated lines = 30.5% on project myProject, can be considered a measure.</td></tr><tr><td>Metric</td><td><p>A type of measurement. Metrics can have varying values, or measures, over time. Examples: number of lines of code, complexity, etc. </p><p>A metric may be either <em>qualitative</em> (for example, the density of duplicated lines, line coverage by tests, etc.) or <em>quantitative</em> (for example, the number of lines of code, the complexity, etc.)</p></td></tr><tr><td>New code definition</td><td>A changeset or period that you're keeping a close watch on for the introduction of new problems in the code. Ideally, this is since the <code>previous_version</code>, but if you don't use a Maven-like versioning scheme, you may need to set a time period such as <em>21 days since a specific analysis</em> or use a reference branch. See <a href="https://docs.sonarsource.com/sonarqube/latest/project-administration/clean-as-you-code-settings/defining-new-code/">Defining new code</a> for more details.</td></tr><tr><td>Quality profile </td><td>A set of rules. Each snapshot is based on a single quality profile. See also <a href="https://docs.sonarsource.com/sonarqube/latest/instance-administration/quality-profiles/">Quality profiles</a>.</td></tr><tr><td>Rule</td><td>A coding standard or practice that should be followed. Not complying with coding rules can lead to issues and hotspots. Adherence to rules can be used to measure the quality of code files or unit tests.</td></tr><tr><td>Remediation cost</td><td>The estimated time required to fix vulnerability and reliability Issues.</td></tr><tr><td>Snapshot</td><td>A set of <strong>measures</strong> and <strong>issues</strong> on a given project at a given time. A snapshot is generated for each analysis.</td></tr><tr><td>Security hotspot</td><td>Security-sensitive pieces of code that need to be manually reviewed. Upon review, you'll either find that there is no threat or that there is vulnerable code that needs to be fixed.</td></tr><tr><td>Technical debt</td><td>The estimated time required to fix all maintainability issues and code smells.</td></tr><tr><td>Vulnerability</td><td>A security-related issue that represents a backdoor for attackers. See also <a href="https://docs.sonarsource.com/sonarqube/latest/user-guide/rules/security-related-rules/">Security-related rules.</a></td></tr></tbody></table>

### SonarQube: Metric definitions

#### Complexity <a href="#complexity" id="complexity"></a>

**Complexity** (`complexity`): _Complexity_ refers to _Cyclomatic complexity_, a quantitative metric used to calculate the number of paths through the code. Whenever the control flow of a function splits, the complexity counter gets incremented by one. Each function has a minimum complexity of 1. This calculation varies slightly by language because keywords and functionalities.

<details>

<summary>Language-specific details</summary>

*
[ ] 
    <table data-header-hidden><thead><tr><th width="194"></th><th></th></tr></thead><tbody><tr><td><strong>Language</strong> </td><td><strong>Notes</strong> </td></tr><tr><td>ABAP </td><td>The following keywords increase the complexity by one: AND, CATCH, CONTINUE, DO, ELSEIF, IF, LOOP, LOOPAT, OR, PROVIDE, SELECT…ENDSELECT, TRY, WHEN, WHILE. </td></tr><tr><td>C/C++/Objective-C </td><td>The complexity gets incremented by one for: each control statement such as: if, while, do while, for; switch statement keywords such as: case, default; the &#x26;&#x26; and || operators; the ? ternary operator and lambda expression definitions. </td></tr><tr><td>C# </td><td><p>The complexity gets incremented by one for each of these function declarations: method, constructor, destructor, property, accessor, operator, or local function declaration. </p><p>In addition, the count is incremented one for each: conditional expression, conditional access, switch case and switch expression arm, each and / or pattern, and for each of the do, for, foreach, if,  while statements and for ??, ??=, ||, or &#x26;&#x26; expressions. </p></td></tr><tr><td>COBOL </td><td>The following commands increase the complexity by one (except when they are used in a copybook): ALSO, ALTER, AND, DEPENDING, END_OF_PAGE, ENTRY, EOP, EXCEPTION, EXIT, GOBACK, CONTINUE, IF, INVALID, OR, OVERFLOW, SIZE, STOP, TIMES, UNTIL, USE, VARYING, WHEN, EXEC CICS HANDLE, EXEC CICS LINK, EXEC CICS XCTL, EXEC CICS RETURN. </td></tr><tr><td>Java </td><td>Keywords incrementing the complexity: if, for, while, case, &#x26;&#x26;, ||, ?, ->. </td></tr><tr><td>JS/TS, PHP </td><td>Complexity is incremented by one for each: function (i.e non-abstract and non-anonymous constructors, functions, procedures or methods), if, short-circuit (AKA lazy) logical conjunction (&#x26;&#x26;), short-circuit (AKA lazy) logical disjunction (||), ternary conditional expressions, loop, case clause of a switch statement, throw and catch statement, go to statement (only for PHP). </td></tr><tr><td>PL/I </td><td><p>The following keywords increase the complexity by one: PROC, PROCEDURE, GOTO, GO TO, DO, IF, WHEN, |, !, |=, !=, &#x26;, &#x26;=. Type 1 DO statements are ignored; only DO statements with conditions will increment complexity. </p><p>For procedures having more than 1 return statement: each additional return statement except for the last one, will increment the complexity metric. </p></td></tr><tr><td>PL/SQL </td><td>The complexity gets incremented by one for: the main PL/SQL anonymous block (not inner ones), CREATE PROCEDURE, CREATE TRIGGER, basic LOOP statement, WHEN clause statement (the “WHEN” of simple CASE statement and searched CASE statement), CONTINUE statement, cursor FOR LOOP  statement, CONTINUE / EXIT WHENclause (The “WHEN” part of the CONTINUE and EXIT statements), exception handler (every individual “WHEN”), EXIT statement, FORLOOP statement, FORALL statement,IF  statement, ELSIF clause, RAISE statement, RETURN statement, WHILELOOP statement, ANDexpression (“AND” reserved word used within PL/SQL expressions), ORexpression (“OR” reserved word used within PL/SQL expressions), WHEN clause expression (the “WHEN” of simple CASE expression and searched CASE expression). </td></tr><tr><td>VB.NET </td><td>The complexity gets incremented by one for: method or constructor declaration (Sub, Function), AndAlso, Case, Continue, Do, End, Error, Exit, For, ForEach, GoTo, If, Loop, On Error, OrElse, Resume, Stop, Throw, Try, While. </td></tr></tbody></table>

</details>

**Cognitive Complexity** (`cognitive_complexity`): How hard it is to understand the code's control flow. See the [Cognitive Complexity white paper](https://www.sonarsource.com/resources/white-papers/cognitive-complexity/) for a complete description of the mathematical model applied to compute this measure.

#### Duplications <a href="#duplications" id="duplications"></a>

**Duplicated blocks** (`duplicated_blocks`): The number of duplicated blocks of lines.

<details>

<summary>Language-specific details</summary>

For a block of code to be considered as duplicated:

**Non-Java projects**:

* There should be at least 100 successive and duplicated tokens.
* Those tokens should be spread at least on:
* 30 lines of code for COBOL
* 20 lines of code for ABAP
* 10 lines of code for other languages

**Java projects**:\
There should be at least 10 successive and duplicated statements whatever the number of tokens and lines. Differences in indentation and in string literals are ignored while detecting duplications.

</details>

**Duplicated files** (`duplicated_files`): The number of files involved in duplications.

**Duplicated lines** (`duplicated_lines`): The number of lines involved in duplications.

**Duplicated lines (%)** (`duplicated_lines_density`): `duplicated_lines` / (lines of code) \* 100

#### Issues <a href="#issues" id="issues"></a>

The old severity feature is deprecated. Issue severity is now tied to the impact on the software qualities and cannot be changed. See [Clean Code](https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/) for more details.

**New issues** (`new_violations`): The number of issues raised for the first time on new code.

**New xxx issues** (`new_xxx_violations`): The number of issues of the specified severity raised for the first time on new code, where xxx is one of: `blocker`, `critical`, `major`, `minor`, `info`.

**Issues** (`violations`): The total count of issues in all states.

**xxx issues** (`xxx_violations`): The total count of issues of the specified severity, where xxx is one of: `blocker`, `critical`, `major`, `minor`, `info`.

**False positive issues** (`false_positive_issues`): The total count of issues marked false positive.

**Open issues** (`open_issues`): The total count of issues in the Open state.

**Confirmed issues** (`confirmed_issues`): The total count of issues in the Confirmed state.

**Reopened issues** (`reopened_issues`): The total count of issues in the Reopened state.

#### Maintainability <a href="#maintainability" id="maintainability"></a>

Issue types (bug, vulnerability, and code smell) are deprecated. Issues are now tied to Clean Code attributes and software qualities impacted. See [Clean Code](https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/) for more details.

**Code smells** (`code_smells`): The total count of code smell issues.

**New code smells** (`new_code_smells`): The total count of Code Smell issues raised for the first time on New Code.

**Maintainability rating** (`sqale_rating`): (Formerly the SQALE rating.) The rating given to your project related to the value of your **Technical debt ratio**. The default Maintainability rating grid is:

A=0-0.05, B=0.06-0.1, C=0.11-0.20, D=0.21-0.5, E=0.51-1

The Maintainability rating scale can be alternately stated by saying that if the outstanding remediation cost is:

* <=5% of the time that has already gone into the application, the rating is A
* between 6 to 10% the rating is a B
* between 11 to 20% the rating is a C
* between 21 to 50% the rating is a D
* anything over 50% is an E

**Technical debt** (`sqale_index`): A measure of effort to fix all code smells. The measure is stored in minutes in the database. An 8-hour day is assumed when values are shown in days.

**Technical debt on new code** (`new_technical_debt`): a measure of effort required to fix all code smells raised for the first time on new code.

**Technical debt ratio** (`sqale_debt_ratio`): The ratio between the cost to develop the software and the cost to fix it. The Technical Debt Ratio formula is: `Remediation cost / Development cost`\
Which can be restated as: `Remediation cost / (Cost to develop 1 line of code * Number of lines of code)`\
The value of the cost to develop a line of code is 0.06 days.

**Technical debt ratio on new code** (`new_sqale_debt_ratio`): The ratio between the cost to develop the code changed on new code and the cost of the issues linked to it.

#### Quality gates <a href="#quality-gates" id="quality-gates"></a>

**Quality gate status** (`alert_status`): The state of the quality gate associated with your project. Possible values are `ERROR` and `OK`. Note: the `WARN` value has been removed since SonarQube 7.6.

**Quality gate details** (`quality_gate_details`): For all the conditions of your quality gate, you know which condition is failing and which is not.

#### Reliability <a href="#reliability" id="reliability"></a>

Issue types (bug, vulnerability, and code smell) are deprecated. Issues are now tied to Clean Code attributes and software qualities impacted. See [Clean Code](https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/) for more details.

**Bugs** (`bugs`): The total number of bug issues.

**New Bugs** (`new_bugs`): The number of new bug issues.

**Reliability Rating** (`reliability_rating`)\
A = 0 Bugs\
B = at least 1 Minor Bug\
C = at least 1 Major Bug\
D = at least 1 Critical Bug\
E = at least 1 Blocker Bug

**Reliability remediation effort** (`reliability_remediation_effort`): The effort to fix all bug issues. The measure is stored in minutes in the DB. An 8-hour day is assumed when values are shown in days.

**Reliability remediation effort on new code** (`new_reliability_remediation_effort`): The same as _Reliability remediation effort_ but on the code changed on new code.

#### Security <a href="#security" id="security"></a>

Issue types (bug, vulnerability, and code smell) are deprecated. Issues are now tied to Clean Code attributes and software qualities impacted. See [Clean Code](https://docs.sonarsource.com/sonarqube/latest/user-guide/clean-code/) for more details.

**Vulnerabilities** (`vulnerabilities`): The number of vulnerability issues.

**Vulnerabilities on new code** (`new_vulnerabilities`): The number of new vulnerability issues.

**Security Rating** (`security_rating`)\
A = 0 Vulnerabilities\
B = at least 1 Minor Vulnerability\
C = at least 1 Major Vulnerability\
D = at least 1 Critical Vulnerability\
E = at least 1 Blocker Vulnerability

**Security remediation effort** (`security_remediation_effort`): The effort to fix all vulnerability issues. The measure is stored in minutes in the DB. An 8-hour day is assumed when values are shown in days.

**Security remediation effort on new code** (`new_security_remediation_effort`): The same as _Security remediation effort_ but on the code changed on New Code.

**Security hotspots** (`security_hotspots`): The number of Security Hotspots

**Security hotspots on new code** (`new_security_hotspots`): The number of new Security Hotspots on New Code.

**Security review rating** (`security_review_rating`): The security review rating is a letter grade based on the percentage of Reviewed Security Hotspots. Note that security hotspots are considered _reviewed_ if they are marked as _Acknowledged_, _Fixed_ or _Safe_.

A = >= 80%\
B = >= 70% and <80%\
C = >= 50% and <70%\
D = >= 30% and <50%\
E = < 30%

**Security review rating on new code** (`new_security_review_rating`): The security review rating for new code.

**Security hotspots reviewed** (`security_hotspots_reviewed`): The percentage of reviewed security hotspots. Ratio formula: `Number of Reviewed Hotspots x 100 / (To_Review Hotspots + Reviewed Hotspots)`

**New Security Hotspots Reviewed**: The percentage of reviewed security hotspots on new code.

#### Size <a href="#size" id="size"></a>

**Classes** (`classes`): The number of classes (including nested classes, interfaces, enums, and annotations).

**Comment lines** (`comment_lines`): The number of lines containing either comment or commented-out code.

Non-significant comment lines (empty comment lines, comment lines containing only special characters, etc.) do not increase the number of comment lines.

The following piece of code contains 9 comment lines:

```cobol
/**                                            +0 => empty comment line
 *                                             +0 => empty comment line
 * This is my documentation                    +1 => significant comment
 * although I don't                            +1 => significant comment
 * have much                                   +1 => significant comment
 * to say                                      +1 => significant comment
 *                                             +0 => empty comment line
 ***************************                   +0 => non-significant comment
 *                                             +0 => empty comment line
 * blabla...                                   +1 => significant comment
 */                                            +0 => empty comment line

/**                                            +0 => empty comment line
 * public String foo() {                       +1 => commented-out code
 *   System.out.println(message);              +1 => commented-out code
 *   return message;                           +1 => commented-out code
 * }                                           +1 => commented-out code
 */                                            +0 => empty comment line
```

<details>

<summary>Language-specific details</summary>

*
[ ] 
    <table data-header-hidden><thead><tr><th width="139"></th><th></th></tr></thead><tbody><tr><td><strong>Language</strong></td><td><strong>Note</strong></td></tr><tr><td>COBOL</td><td>Generated lines of code and pre-processing instructions (<code>SKIP1</code>, <code>SKIP2</code>, <code>SKIP3</code>, <code>COPY</code>, <code>EJECT</code>, <code>REPLACE</code>) are not counted as lines of code.</td></tr><tr><td>Java</td><td>File headers are not counted as comment lines (because they usually define the license).</td></tr></tbody></table>

</details>

**Comments (%)** (`comment_lines_density`): The comment lines density = comment lines / (lines of code + comment lines) \* 100

With such a formula:

* 50% means that the number of lines of code equals the number of comment lines
* 100% means that the file only contains comment lines

**Directories** (`directories`): The number of directories.

**Files** (`files`): The number of files.

**Lines** (`lines`): The number of physical lines (number of carriage returns).

**Lines of code** (`ncloc`): The number of physical lines that contain at least one character which is neither a whitespace nor a tabulation nor part of a comment.

**Lines of code per language** (`ncloc_language_distribution`): The _non-commented lines of code_ distributed by language.

**Functions** (`functions`): The number of functions. Depending on the language, a function is defined as either a _function_, a _method_, or a _paragraph_.

<details>

<summary>Language-specific details</summary>

*
[ ] 
    <table data-header-hidden><thead><tr><th width="139"></th><th></th></tr></thead><tbody><tr><td><strong>Language</strong> </td><td><strong>Note</strong> </td></tr><tr><td>COBOL </td><td>It is the number of paragraphs. </td></tr><tr><td>Java </td><td>Methods in anonymous classes are ignored. </td></tr><tr><td>VB.NET </td><td>Accessors are not considered to be methods. </td></tr></tbody></table>

</details>

**Projects** (`projects`): The number of projects in a Portfolio.

**Statements** (`statements`): The number of statements.

#### Tests <a href="#tests" id="tests"></a>

**Condition coverage** (`branch_coverage`): On each line of code containing some boolean expressions, the condition coverage answers the following question: 'Has each boolean expression been evaluated both to `true` and to `false`?'. This is the density of possible conditions in flow control structures that have been followed during unit tests execution.

Condition coverage = (CT + CF) / (2\*B)\
where:

* CT = conditions that have been evaluated to 'true' at least once
* CF = conditions that have been evaluated to 'false' at least once
* B = total number of conditions

**Condition coverage on new code** (`new_branch_coverage`): This definition is identical to **Condition coverage** but is restricted to new/updated source code.

**Condition coverage hits** (`branch_coverage_hits_data`): A list of covered conditions.

**Conditions by line** (`conditions_by_line`): The number of conditions by line.

**Covered conditions by line** (`covered_conditions_by_line`): The number of covered conditions by line.

**Coverage** (`coverage`): A mix of **Line coverage** and **Condition coverage**. It's goal is to provide an even more accurate answer the question  'How much of the source code has been covered by the unit tests?'.

Coverage = (CT + CF + LC)/(2\*B + EL)\
where:

* CT = conditions that have been evaluated to 'true' at least once
* CF = conditions that have been evaluated to 'false' at least once
* LC = covered lines = line&#x73;_&#x74;&#x6F;_&#x63;over - uncovered\_lines
* B = total number of conditions
* EL = total number of executable lines (`lines_to_cover`)

**Coverage on new code** (`new_coverage`): This definition is identical to **Coverage** but is restricted to new/updated source code.

**Line coverage** (`line_coverage`): On a given line of code, Line coverage simply answers the question 'Has this line of code been executed during the execution of the unit tests?'. It is the density of covered lines by unit tests:

Line coverage = LC / EL\
where:

* LC = covered lines (`lines_to_cover` - `uncovered_lines`)
* EL = total number of executable lines (`lines_to_cover`)

**Line coverage on new code** (`new_line_coverage`): This definition is identical to **Line coverage** but restricted to new/updated source code.

**Line coverage hits** (`coverage_line_hits_data`): A list of covered lines.

**Lines to cover** (`lines_to_cover`): The number of lines of code that could be covered by unit tests (for example, blank lines or full comments lines are not considered as lines to cover).

**Lines to cover on new code** (`new_lines_to_cover`): This definition is Identical to **Lines to cover** but restricted to new/updated source code.

**Skipped unit tests** (`skipped_tests`): The number of skipped unit tests.

**Uncovered conditions** (`uncovered_conditions`): The number of conditions that are not covered by unit tests.

**Uncovered conditions on new code** (`new_uncovered_conditions`): This definition is identical to **Uncovered conditions** but restricted to new/updated source code.

**Uncovered lines** (`uncovered_lines`): The number of lines of code that are not covered by unit tests.

**Uncovered lines on new code** (`new_uncovered_lines`): This definition is identical to **Uncovered lines** but restricted to new/updated source code.

**Unit tests** (`tests`): The number of unit tests.

**Unit tests duration** (`test_execution_time`): The time required to execute all the unit tests.

**Unit test errors** (`test_errors`): The number of unit tests that have failed.

**Unit test failures** (`test_failures`): The number of unit tests that have failed with an unexpected exception.

**Unit test success density (%)** (`test_success_density`): Test success density = (Unit tests - (Unit test errors + Unit test failures)) / (Unit tests) \* 100

### Setting Up SonarQube in AutoRABIT <a href="#setting-up-sonarqube-in-autorabit" id="setting-up-sonarqube-in-autorabit"></a>

If you want to integrate all the functionality included in your **SonarQube** license with AutoRABIT, you need to integrate SonarQube as a plugin with your AutoRABIT account. However, it does require some steps in SonarQube as well as in your AutoRABIT account to get it configured.

#### Step 1: Generate a SonarQube Token <a href="#step-1-generate-a-sonarqube-token" id="step-1-generate-a-sonarqube-token"></a>

1. Log in to your SonarQube instance.
2. Go to **User > My Account > Security**. Your existing tokens are listed here, each with a **Revoke** button.
3. The form at the bottom of the page allows you to generate new tokens. Once you click the **Generate** button, you will see the token value. Copy it immediately; once you dismiss the notification you will not be able to retrieve it.
4. This token will be used while storing your credential with AutoRABIT.&#x20;

#### Step 2: Store your SonarQube's credential in AutoRABIT <a href="#step-2-store-your-sonarqubes-credential-in-autorabit" id="step-2-store-your-sonarqubes-credential-in-autorabit"></a>

This is an initial step where your SonarQube credential such as username and password is stored in AutoRABIT.

1. Log in to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and click on the **Credentials** tab.
3. Next, click on **Create Credential** from the right navigation bar.
4. On the next pop-up screen, give a **Credential name**.
5. Choose the Credential Type as '**User name with Password'.**
6. Choose your **Credential Scope**
   * **Global**: Credential can be accessed within the team
   * &#x20;**Private**: Credential for private usage&#x20;
7. Enter your SonarQube account's username. For **password**, use the copied token as mentioned in _**Step 1: Create a SonarQube Token**_
8. Please double-check that you use your SonarQube username instead of the email address that you use to log in to SonarQube.
9. Click **Save**.

<figure><img src="../../../.gitbook/assets/image (873).png" alt="" width="393"><figcaption></figcaption></figure>

#### Step 3: Integrate SonarQube with AutoRABIT <a href="#step-3-integrate-sonarqube-with-autorabit" id="step-3-integrate-sonarqube-with-autorabit"></a>

If you're logged out from your account, log in again into AutoRABIT with your credentials.

1. Go to **Admin > My Account** section.
2. Go to the **Plugins** section.
3. Check the **SonarQube** checkbox under **Static Code Analysis**.

<figure><img src="../../../.gitbook/assets/image (874).png" alt=""><figcaption></figcaption></figure>

4.  Fill in the below details:

    * Enter the SonarQube **hosted URL**. For the SonarQube cloud version use **https://sonarcloud.io**
    * Choose the **Host Type** i.e., _Cloud_ or _On-premise_. For SonarQube hosted on Cloud, you need to add the **Organization Key.**&#x20;
    * Select your **Credential** from the drop-down.
    * Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
    * Click **Save**.

    <figure><img src="../../../.gitbook/assets/image (875).png" alt="" width="383"><figcaption></figcaption></figure>
5. Click on **Save** once again and you are all set with SonarQube integration.

#### Step 4: Setting SonarQube Global Criteria Settings <a href="#step-4-setting-sonarqube-global-criteria-settings" id="step-4-setting-sonarqube-global-criteria-settings"></a>

You can now set the global Quality Gate criteria to enforce SonarQube Static code analysis tool across CI Jobs, Deployment, and gated Commits. The Quality Gate gives you a Pass or Fail rating for your project in the SonarQube tool depending on the metrics you have provided. Based on the criteria configured in AutoRABIT and if it matches in your SonarQube account, the process gets aborted.

1. Go to **Admin > My Account** section.
2. Next, navigate to the **Validation Criteria-Static Code Analysis** section.
3. Select the **Enable** checkbox.
4. Enable the **SonarQube** checkbox and assign the Quality Gate status for all your projects. By default, it is set to **ERROR**, however, you can choose the criteria of your own. If the Quality Gate matches with the status assigned to the projects on your SonarQube tool, the validation process gets failed and the build aborts.

<figure><img src="../../../.gitbook/assets/image (876).png" alt="" width="511"><figcaption></figcaption></figure>

5. Click **Save**.
6. Next, go to the next section i.e., **Commit Validation - Approval Settings**. In this section, you can allow the SonarQube tool to identifying potential software quality issues before the code moves to production and abort the commit process if the Quality Gate set earlier matches with the status in the SonarQube application.&#x20;
7. Select the checkbox: **Enable criteria based Review Process**&#x20;
8.  Enable the **Should pass validation criteria for Static Code Analysis** checkbox, select the below checkboxes:

    * **SonarQube**
    * **Auto reject commit process if the criteria are not met**

    <figure><img src="../../../.gitbook/assets/image (877).png" alt=""><figcaption></figcaption></figure>
9. Click **Save**.
10. Similar to SonarQube criteria globally configured in AutoRABIT for Commit operation, you can even set the same for Merge Process. Go to the next section: **Merge Settings**
11. Select the **Enable criteria-based Review Process** checkbox.
12. Under **Should pass validation criteria for Static Code Analysis**, select the **SonarQube** checkbox.
13. Finally, click on **Save**.
