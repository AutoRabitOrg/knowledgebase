# Audit Report

### Introduction <a href="#introduction" id="introduction"></a>

An audit report gives you a comprehensive view of your business operations by fostering a collaborative operational audit environment. Here, you can download the audit report (CSV format) to view and track all the changes that occurred to help analyze and assess risk for your organization.

1.  Select your [**Salesforce Org**](arm-administration/registration/salesforce-org.md) from the drop-down.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654510410480.png" alt="" width="563"><figcaption></figcaption></figure>
2.  Choose the period (from and to dates) to view on the audit report.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654510461152.png" alt="" width="563"><figcaption></figcaption></figure>
3.  Click **SEARCH**. This will produce the audit report for the selected dates. You can download the report for your reference in CSV format on your local machine.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654510600047.png" alt=""><figcaption></figcaption></figure>

### **Job Audit Report** <a href="#job-audit-report" id="job-audit-report"></a>

A new call-to-action button is added in ARM in the **CI Job Results** screen called **Job Audit Report.** This feature lets you download and see the status of deployment build operations and commits associated with a deployment in the **Audit Report (PDF)** file. This will also be helpful during internal auditing.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654510719147.png)

The **Audit Report** will have the information below:&#x20;

**Build List**

You will have the visibility of all deployment builds of a job, sorted by date. It will contain the information below:

* Build number
* Timestamp of each build
* Commit comments
* Name of the author and approver

**Individual Build Summary**

This will contain a list of all the commits associated with the build and will also contain the following information:&#x20;

* Set of commit numbers
* Summary of each commit, associated reviewers’ details
* Date of review
* ALM ID (if included)
* Differential revision details
* You'll see the Git commit hash as well as a link to it

#### **Date and time range filters** <a href="#date-and-time-range-filters" id="date-and-time-range-filters"></a>

Explicitly define the time range to filter the builds of a specific CI job. You can select the dates of the predefined filter or enter your custom dates (maximum of 120 days) to filter the results and generate audit reports for the selected builds.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654510916792.png)

\
