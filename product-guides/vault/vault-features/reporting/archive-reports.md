# Archive Reports

## AutoRABIT Vault Reporting

### Introduction

AutoRABIT Vault's Archive Reporting feature allows users to generate data-driven insights on actions performed on archived data. These reports help in auditing, compliance, and operational analysis.

***

### Report Creation Workflow

1.  Click **Generate Report**.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 0.png" alt=""><figcaption></figcaption></figure>
2.  In the **Search By** dropdown, select the appropriate option.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 2.png" alt=""><figcaption></figcaption></figure>
3.  A pop-up will appear, prompting for input parameters.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 3.png" alt=""><figcaption></figcaption></figure>
4.  Fill in the required fields:

    * **Salesforce Org**: Select the target Org for which the report is generated.
    * **Report Label**: Enter a custom label (no special characters).
    *   **Report Date Range**: Choose a date range (maximum of 6 months).

        > ⚠️ **Note:** Only a 6-month date range is allowed.
    * **Object**: Select the Salesforce object to report on.
    * **Fields**: Choose the relevant fields from the selected object.
    * **Query**: A query will be auto-generated based on selected fields. You can also define a custom SOQL query.
    *   Click **Generate** to initiate the report creation.

        > ⚠️ **Note:** Reports expire 7 days after creation.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 4.png" alt=""><figcaption></figcaption></figure>
5. Reports may take time to process depending on data volume. A maximum of 5 reports run simultaneously; additional reports are queued.
6.  Once ready, reports are listed under **Archive Reports**.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 6.0.png" alt=""><figcaption></figcaption></figure>
7.  Click on the **Report Label** to view the report.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 7.png" alt=""><figcaption></figcaption></figure>
8.  Use the search bar to find records (default is case-insensitive). Enable case-sensitivity if needed.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 8.png" alt=""><figcaption></figcaption></figure>

***

### Additional Features

*   **Export to CSV**: Export report data using this feature.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 9.png" alt=""><figcaption></figcaption></figure>
*   **Consolidated Report**: View a combined report across related data sets.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 10.png" alt=""><figcaption></figcaption></figure>
*   **Change View**: Customize visible columns by selecting from the available list.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 11.png" alt=""><figcaption></figcaption></figure>
*   **Column Search**: Locate specific fields using the column search.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 12.png" alt=""><figcaption></figcaption></figure>
*   **Dynamic Operators**: Based on selected columns, applicable operators (e.g., equals, contains) are shown.

    <figure><img src="../../../../.gitbook/assets/KONE Reporting Screenshots 13.png" alt=""><figcaption></figcaption></figure>
