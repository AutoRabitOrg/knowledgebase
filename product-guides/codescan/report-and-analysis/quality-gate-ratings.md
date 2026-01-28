# Quality Gate Ratings

The Security, Reliability, and Maintainability ratings in the Quality Gate affect the amount of blocked Vulnerabilities, Bugs, and Code Smells respectively.  They are displayed as a rating from A to E.

### Security Rating

The Security Rating is based on the highest severity Vulnerability that is present in your project.

**A** = No Vulnerabilities\
**B** = At least one Minor Vulnerability\
**C** = At least one Major Vulnerability\
**D** = At least one Critical Vulnerability\
**E** = At least one Blocker Vulnerability

### Reliability Rating

The Reliability Rating is based on the highest severity Bug that is present in your project.

**A** = No Bugs\
**B** = At least one Minor Bug\
**C** = At least one Major Bug\
**D** = At least one Critical Bug\
**E** = At least one Blocker Bug

### Maintainability Rating

The Maintainability Rating is based on the Technical Debt Ratio.  in CodeScan, each issue is given an issue remediation effort which represents the estimated time to fix that issue.

<figure><img src="../../../.gitbook/assets/image (1) (1) (3).png" alt=""><figcaption></figcaption></figure>

The Technical Debt Ratio is the ratio between the cost of developing code and the cost of fixing it. This is calculated with the following formula (where the cost to develop one line is 30 minutes:

Technical Debt Ratio = Technical Debt /(cost to develop one line of code \* number of lines of code)

**Example**:

* Technical debt: 408 Hours
* Number of lines of code: 8,222
* Cost to develop one line of code: 30 minutes
* Technical debt ratio: 10%

Based on that metric, the scale for Maintainability is as follows:

**A** = 0% to <5%\
**B** = ≥ 5% to <10%\
**C** = ≥ 10% to <20%\
**D** = ≥ 20% to <50%\
**E** = ≥ 50%&#x20;
