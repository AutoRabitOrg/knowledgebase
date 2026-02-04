# Release Pipeline Run Details

**Overview**\
The Release Run Details page is a drill-down view for a specific release pipeline run. It provides a complete, stage-by-stage view of how an artifact moved through the pipeline, along with execution status, logs, and deployment reports.

This page is typically accessed from the **Release history** view when deeper investigation or validation of a specific run is required.

How to access Release Run Details

1. Navigate to Pipelines → Releases
2. From the Most recent runs view, locate the required pipeline
3. Click View details
4.  From the pipeline run history, click View Details for the specific run you want to analyze\
    <br>

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2026-02-04 at 11.25.38 AM.png" alt=""><figcaption></figcaption></figure>

You will be redirected to the Release Run Details page.

What you see on this page

Step 1: Pipeline execution flow\
At the top of the page, the pipeline is displayed as a visual flow starting from the artifact and progressing through each configured stage in sequence.

This view helps you quickly understand how the artifact moved across environments during this run.\
<br>

<figure><img src="../../../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Step 2: Stage cards and execution status\
Each stage is represented as a card in the flow and displays:

* stage name
* execution status (completed, failed, in progress, pending)
* execution timestamp

This makes it easy to identify where a run succeeded, paused, or failed.

Step 3: Viewing stage logs\
For each stage, you can:

* hover over or click Logs to open the execution logs for that stage

Logs provide detailed information about deployment steps, validations, and any errors or warnings encountered during execution.\
\
![](<../../../../../../.gitbook/assets/image (5).png>)

Step 4: Stage-level deployment details\
Clicking on a stage opens detailed information specific to that stage, including:

* Jobs
* Deployment report
* Deployment logs
*   Post Activities Report (If applicable)<br>

    <figure><img src="../../../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

\
<br>

<figure><img src="../../../../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

These details are useful for troubleshooting failures, validating successful deployments, and supporting audits or reviews.\
<br>
