# About Issue Status

## **Issue Status**

An issue can have the following statuses:

* **Open**: This is the initial status assigned by CodeScan when a new issue is detected during an analysis. (**Reopened:** A user can reopen a False positive, Accept Issues. If a fixed issue still exists after the next analysis, CodeScan automatically reopens it, indicating that the fix was unsuccessful.)
* **Accept (Won’t Fix)**: Select if the user decides not to fix the issue and thinks the rule is irrelevant in this context.
* **False Positive (Analysis is mistaken):** Set by an authorized user if the analysis is mistaken. (This issue can be suppressed if it was not raised accurately.). CodeScan ignores false-positive issues in the quality reports and code ratings.
* **Confirmed (deprecated)**: An issue is moved to Confirmed when a user manually validates it as a valid issue that needs to be addressed.

Note: CodeScan ignores confirmed issues in the code ratings but displays the number of confirmed issues in various analysis snapshots in the UI.

*   **Fixed (deprecated)**: Set by an authorized user if the confirmed issue has been resolved in the code (i.e., it is no longer detected) and is waiting for the subsequent analysis to close it, or reopen it if it was not actually fixed.<br>

    <figure><img src="../../../.gitbook/assets/image (1719).png" alt=""><figcaption><p>Fixed</p></figcaption></figure>

If users mark many issues as False Positives, it means that some coding rules are inappropriate for the project. In that case, rules can be deactivated in the quality profile, or the project's analysis scope can be adjusted to exclude files.

The following diagram shows the Issue life cycle:

<figure><img src="../../../.gitbook/assets/image (1720).png" alt=""><figcaption><p>Issue Life Cycle</p></figcaption></figure>

### &#x20;**Tracking Issue History**

1. Under the **Issues** tab, select the violation for which you want to check the history of changes.
2.  You should be able to see when the Issue was introduced in the upper corner of the issue page.<br>

    <figure><img src="../../../.gitbook/assets/image (1721).png" alt=""><figcaption><p>Issue Activity</p></figcaption></figure>
3.  In the Activity tab, you should see the history and every activity on the Issue, such as the creation date, member assignment, severity, comments, etc.<br>

    <figure><img src="../../../.gitbook/assets/image (1722).png" alt=""><figcaption><p>Activity Tab</p></figcaption></figure>
