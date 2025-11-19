# Audit Report

### Introduction <a href="#introduction" id="introduction"></a>

The ARM **Audit Report** provides a searchable, exportable record of activity across your Salesforce orgs. Download the report as a CSV to review every change, verify compliance, and surface potential risks.

To generate a report:

1.  **Select a Salesforce Org.**\
    In the drop-down, choose the target [**Salesforce Org**](broken-reference).\
    \


    <figure><img src="../../../../.gitbook/assets/image (2152).png" alt=""><figcaption></figcaption></figure>
2. **Set a date range.**\
   Specify the **From** and **To** dates for the period you want to analyze.
3.  **Run the search.**\
    Click **SEARCH** to generate the report. When the results appear, click **Download** to save the CSV locally.\
    \


    <figure><img src="../../../../.gitbook/assets/image (2153).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Time-zone note:** ARM stores audit timestamps in GMT. Salesforce displays times in the user’s own time zone, so the two can differ. This is expected and does not indicate an error.
{% endhint %}

### Job Audit Report <a href="#job-audit-report" id="job-audit-report"></a>

On the **CI Job Results** page you’ll see a **Job Audit Report** button. Click it to download a PDF that captures the full deployment history for that job—ideal for internal or external audits.\
\
You can narrow the report to a specific time window—up to **120 days**—using either preset ranges or custom **From / To** dates.\


<figure><img src="../../../../.gitbook/assets/image (2154).png" alt=""><figcaption></figcaption></figure>

The PDF contains:

#### Build list

* Every deployment build for the job, in reverse-chronological order, showing:
  * Build number
  * Timestamp
  * Commit comments
  * Author and approver

#### Individual build summary

For each build the report includes:

* Commit IDs (with Git-hash links)
* Commit summaries and reviewer details
* Review dates
* ALM IDs (if provided)
* Differential revision details

