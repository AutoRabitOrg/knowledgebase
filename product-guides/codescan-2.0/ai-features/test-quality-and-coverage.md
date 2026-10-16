---
description: Score how good your tests are, and see estimated and measured code coverage.
---

# Test Quality and Coverage

Coverage percentages are easy to game. A test that calls a method and asserts nothing still counts as coverage. CodeScan gives you three separate views of your tests, so you can see both whether code is tested and whether the tests would catch a bug. CodeScan never runs your tests: it reads them.

| View               | Question it answers                    | Uses AI |
| ------------------ | -------------------------------------- | ------- |
| Test quality       | Would this test notice a bug?          | Yes     |
| Estimated coverage | Can any test reach this code?          | No      |
| Measured coverage  | Did your tests actually run this code? | No      |

## Test Quality

### Switching It On

Turn on **`AI test quality review`** in [Project Settings](/broken/pages/9130a1cc74fd1ebef58d3563d5a1d2d908986c76), or pass `--check-tests` to `codescan review`. The scan then includes an **Analyzing tests** step.

### What You See

The scan page gets a **Test Quality** section, separate from findings and not counted in the finding total. For each test file and test, you see:

* a score from 0 to 100
* a coverage potential of Low, Medium or High: how much code the test could exercise, judged from its structure
* the reasoning, a breakdown against the scoring criteria, issues such as a weak or missing assertion, and suggestions

The scan also shows the average score and how many tests were scored. Test quality is reviewed for Apex, Java, TypeScript and Angular.

### What the Score Looks For

* **Meaningful assertions.** A test with no assertions, or assertions on irrelevant values, scores poorly.
* **The logic it claims to cover.** Calling a method is not the same as testing it.
* **Bulk behaviour.** An Apex test that inserts one record misses governor-limit problems.
* **Negative and error cases.** A suite that only tests the happy path is fragile.
* **Platform discipline.** For example `@IsTest`, DML isolation and readiness for parallel tests.

A test that cannot fail is worse than no test, because it hides the gap. Use the lowest-scoring tests as your list to strengthen.

{% hint style="info" %}
**Note:** Separately from the scores, more than 70 deterministic test rules run on every scan, such as a test with no assertion. Those appear as ordinary findings in the **Tests** category and count toward the quality gate.
{% endhint %}

## Estimated and Measured Coverage

|                 | Estimated coverage                                                                                                      | Measured coverage                        |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Source          | CodeScan, by following imports and calls from test code. No AI.                                                         | A coverage report from your own test run |
| Detail          | Method level for Apex, Java and Kotlin. File level for TypeScript, JavaScript, Python, Go, Rust, C#, C++, Scala and F#. | Lines your tests actually executed       |
| How to trust it | A guide. "Reached" is not "executed", so treat it as an upper limit.                                                    | The number to trust                      |
| To switch it on | Turn on **`Test coverage estimate (no AI)`** in project settings, then run a full scan.                                 | Upload a report for the reference branch |

Measured coverage replaces the estimate once a report matches the latest full scan of the reference branch, normally `main`.

### Uploading Measured Coverage

Supported formats: JaCoCo XML, LCOV, Cobertura XML, Istanbul JSON, OpenCover XML and Clover XML. Only line coverage is imported. Binary reports, HTML reports and Go's native cover profile are not supported, so export one of the formats above.

* A full `codescan review` on the reference branch finds coverage reports in the workspace and uploads them automatically.
* `codescan coverage upload` uploads reports without scanning. It fails if you are not on the reference branch.
* `--pr` and `--local` scans do not upload coverage.

A problem with a coverage report never fails the scan.

{% hint style="info" %}
**Note:** Salesforce Apex test-run coverage is not an imported format. The estimate still works for Apex, because it follows the call graph.
{% endhint %}

### The Coverage Tab

The **Coverage** tab shows the headline percentage, covered and executable lines, the report formats, the matching scan, and a file tree. Estimated files are labelled, for example **Imported by tests**, **Called by tests** or **Unreached**. You can filter by language or show uncovered files only.&#x20;

**`Analysis Findings`** ⇒ **`Project`** ⇒ **`Coverage`**

## Using the Three Views Together

* Take the changed files from the [Blast Radius](../findings/blast-radius-for-pull-requests.md) tab and look them up on the Coverage tab. A changed file with no coverage is new behaviour with no test: the highest priority.
* A finding whose **Impact** says _No test reaches this code_ needs a test with the fix.
* A file with good coverage but a low test-quality score has hollow coverage.

The Projects Dashboard tracks test quality over time. Use it in sprint reviews, not as a target for individuals.

## Related Articles

* [Exclusions and Test Folders](/broken/pages/95ed15983a60b2d580273c248279f34856ea1698)
* [Dashboards](/broken/pages/557aa5e6daa90989e7ec2a27f4272fe60b75b956)
