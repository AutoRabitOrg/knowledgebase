# About Issue Status

**About Issues Status:**

An issue can have the following statuses:

* **Open**: The initial status after the first analysis. A user can reopen an issue that has been marked as Accepted or False positive. 
* **Confirmed**: Set by an authorized user to confirm they have reviewed it and decided to address the issue.

CodeScan ignores confirmed issues in the code ratings but displays the number of confirmed issues in various analysis snapshots in the UI.

* **Resolve as False Positive:** Set by an authorized user if the analysis is mistaken. (This issue can be suppressed if it was not raised accurately.). CodeScan ignores False Positive issues in the quality reports and code ratings.
* **Resolve as Fixed**: Set by an authorized user if the confirmed issue has been resolved in the code (i.e., it is no longer detected) and is waiting for the subsequence analysis to close it—or reopen it if it was not actually fixed.
* **Resolve as Won’t Fix**: Select if the user decides not to fix the issue and thinks the rule is irrelevant in this context.

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

If users tend to mark many issues as False Positives, it means that some coding rules are not appropriate for the project. In that case, rules can be deactivated in the quality profile, or the project's analysis scope can be adjusted to exclude files.

The following diagram shows the Issue lifecycle:

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption><p>Issue Lifecycle</p></figcaption></figure>
