# Issues

While running an analysis, CodeScan raises an issue every time a piece of code breaks a coding rule. The set of coding rules are defined by the associated quality profile for each language in the project.

Note: Each project in CodeScan is treated independently. Issues cannot be compared or Synced between two separate projects (even if they contain the same files and issues).

### Issue types <a href="#issue-types" id="issue-types"></a>

There are three types of issues:

* Bug: A coding mistake that can lead to an error or unexpected behavior at runtime.
* Vulnerability: A point in your code that's open to attack.
* Code Smell: A maintainability issue that makes your code confusing and difficult to maintain.

#### Issue severity <a href="#issue-severity" id="issue-severity"></a>

Each issue has one of five severities:

1. BLOCKER: Bug with a high probability to impact the behavior of the application in production. For example, a memory leak, or an unclosed JDBC connection are BLOCKERs that must be fixed immediately.
2. CRITICAL: Either a bug with a low probability to impact the behavior of the application in production or an issue that represents a security flaw. An empty catch block or SQL injection would be a CRITICAL issue. The code must be reviewed immediately.
3. MAJOR: A quality flaw that can highly impact the developer's productivity. An uncovered piece of code, duplicated blocks, or unused parameters are examples of MAJOR issues.
4. MINOR: A quality flaw that can slightly impact the developer's productivity. For example, lines should not be too long, and "switch" statements should have at least 3 cases, are both be considered MINOR issues.
5. INFO: Neither a bug nor a quality flaw, just a finding.
