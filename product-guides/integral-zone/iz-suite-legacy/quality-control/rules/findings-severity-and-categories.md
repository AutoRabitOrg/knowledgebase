# Findings: Severity and Categories

## How are findings categorised?

Every finding comes from one rule, and every rule carries two labels that the finding inherits:

* **Severity:** Blocker, Critical, Major, Minor or Info. This is how urgent it is.
* **Category:** Vulnerability, Security Hotspot, Bug or Code Smell. This is what kind of problem it is.

Severity isn't worked out per scan. A rule always reports at the same severity, so the same problem is rated the same way across every application and run. You can see each rule's severity and category under **Quality Control → Quality rules**.

### What each severity means

| Severity     | Meaning                                                                                                        | Examples                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Blocker**  | A definite, high-impact flaw that should stop a release, typically an exploitable security issue.              | SQL injection; insecure deserialization; credentials embedded in a connection URI                                  |
| **Critical** | A serious security or reliability risk to fix urgently, though it may need a specific condition to cause harm. | Insecure direct object reference; container running privileged; join without a join condition; end-of-life runtime |
| **Major**    | A real defect or risk with significant impact on reliability, security review or maintainability.              | Function not in a healthy state; assignment inside an expression; RAML types not externalised                      |
| **Minor**    | A low-impact issue or best-practice gap.                                                                       | Container logs kept only on the instance; unversioned inline shell in a pipeline                                   |
| **Info**     | Guidance, naming or documentation, or a coverage/inventory note. It is not a defect.                           | Missing meaningful display name; missing API documentation                                                         |

### What each category means

* **Vulnerability:** A definite, exploitable flaw.
* **Security Hotspot:** Security-sensitive code that needs a person to review it.
* **Bug:** Code or configuration that won't behave as intended.
* **Code Smell:** A maintainability or style issue.

### If you rate a rule differently

Built-in severities are our defaults, but your organisation's risk policy can differ:

1. **Change the severity:** Set your own severity or category on the rule based on the organization requirements.
2. **Turn a rule off:** Deactivate it in your quality profile (**Quality Profiles → activate / deactivate rules**).

### Acting on severity in the pipeline

Quality gates count findings per severity: Blocker, Critical, Major, Minor and Info issues, plus totals of Vulnerabilities, Security Hotspots and Bugs.

A common setup is to fail the gate on any Blocker or Critical issue, or any Vulnerability, and to track the others as a trend.

Combined with `-DabortOnQualityGateFailure=true`, the build stops whenever the gate fails.
