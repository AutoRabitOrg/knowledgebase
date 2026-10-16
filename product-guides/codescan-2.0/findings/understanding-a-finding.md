# understanding a finding

**Who this is for:** everyone | **Uses AI credits:** no | **Availability:** <mark style="color:red;">**\[TO CONFIRM]**</mark>

A finding is one problem the scan reported. This article explains what each part of a finding tells you and how to treat each severity.

## Severities

| Severity | How to treat it                                                                                                   |
| -------- | ----------------------------------------------------------------------------------------------------------------- |
| Blocker  | A serious defect or vulnerability. Fix before merging. By default, the only severity that fails the quality gate. |
| Critical | High impact. Fix soon. A project can add it to the gate.                                                          |
| Major    | A significant weakness. Plan the fix. A project can add it to the gate.                                           |
| Minor    | A small problem. Fix it when you next touch the code.                                                             |
| Info     | A convention or suggestion.                                                                                       |

Some rules are marked **Dynamic**: they set the severity of each finding individually, based on what was found.

## Categories

Findings are grouped by category, including security, code quality, performance, structure, exceptions, tests, strings, naming and style. On the scan page they roll up into **Security**, **Structure** and **Code Analysis**.

## The Finding Details

Select a finding to open its details. Depending on the finding, you see:

| Section              | What it tells you                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rule and description | What the rule checks, and why it matters. **Show Rule Description** in VS Code opens the same text.                                                                                         |
| Location             | The file and line. Select it to open the code.                                                                                                                                              |
| Data flow            | For security findings: numbered steps from where untrusted input enters your code (Source), through how it travels (Propagation and Call), to where it could cause damage (Sink).           |
| Impact               | How exposed the code is: reachable entry points, callers, importers, and whether any test reaches it. **No test reaches this code** means the fix should come with a test.                  |
| Reachability         | For dependency findings: whether your code actually imports the vulnerable package.                                                                                                         |
| CWE, OWASP, CVSS     | Standard references, where they apply.                                                                                                                                                      |
| CISA KEV             | **Known Exploited**: attackers are exploiting this vulnerability now.                                                                                                                       |
| EPSS                 | The probability that this vulnerability will be exploited.                                                                                                                                  |
| Duplicate locations  | For copy-paste findings: every place the same code appears.                                                                                                                                 |
| Suggested fix        | A remediation explanation (**How to fix it**), and, when the AI wrote one, an exact code change. See [Suggested Fixes and Patches](/broken/pages/de955a8bba000807df59b20c80febbff6a601f52). |
| AI reason            | For a likely false positive: why the AI reviewer doubts it. For a security finding, this points to the line that defends against it.                                                        |

<mark style="color:red;">**\[SCREENSHOT: finding details with data-flow steps]**</mark>

## Findings You Don't Need to Act On Yet

| Finding                   | What it means                                                                                                 | Counts toward the gate                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Likely false positive     | The AI reviewer found evidence the code is safe. Read the reason, and accept the finding if you agree.        | No                                                |
| Accepted                  | Your team decided to live with it, or marked it as a false positive.                                          | No                                                |
| Suppressed by the scanner | For example, a vendor has stated that a vulnerability does not affect their package. This cannot be reversed. | No                                                |
| Unreachable dependency    | Your code does not import the vulnerable package. It is deprioritised, not deleted.                           | <mark style="color:red;">**\[TO CONFIRM]**</mark> |

## Related Articles

* [Reading Scan Results](/broken/pages/4fc8fc351860dfda476934f46278053a93d53797)
* [Accept a Finding](/broken/pages/dcc4edcb9f36d5c37b6ba9579a82481322290101)
* [Blast Radius](/broken/pages/99ac0dae68e6571d4a54bf98829c1372b3c0dc3f)
