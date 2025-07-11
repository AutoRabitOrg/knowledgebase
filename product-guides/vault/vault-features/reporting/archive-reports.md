# Archive Reports

## Vault Reporting

### Introduction

Vault's Archive Reporting feature allows users to generate data-driven insights on actions performed on archived data. These reports help in auditing, compliance, and operational analysis.

---

### Report Creation Workflow

1. Click **Generate Report**.

![Generate Report Button](../../../../.gitbook/assets/image%20(244).png)

2. In the **Search By** dropdown, select the appropriate option.

![Search By Options](../../../../.gitbook/assets/image%20(245).png)

3. A popup will appear prompting for input parameters.

![Report Configuration Popup](../../../../.gitbook/assets/image%20(246).png)

4. Fill in the required fields:

   - **Salesforce Org**: Select the target Org for which the report is generated.
   - **Report Label**: Enter a custom label (no special characters).
   - **Report Date Range**: Choose a date range (maximum of 6 months).

     > ⚠️ **Note:** Only a 6-month date range is allowed.

   - **Object**: Select the Salesforce object to report on.
   - **Fields**: Choose the relevant fields from the selected object.
   - **Query**: A query will be auto-generated based on selected fields. You can also define a custom SOQL query.
   - Click **Generate** to initiate the report creation.

     > ⚠️ **Note:** Reports expire 7 days after creation.

![Form Example](../../../../.gitbook/assets/image%20(247).png)

5. Reports may take time to process depending on data volume. A maximum of 5 reports run simultaneously; additional reports are queued.

6. Once ready, reports are listed under **Archive Reports**.

![Reports List](../../../../.gitbook/assets/image%20(248).png)

7. Click on the **Report Label** to view the report.

![Report Preview](../../../../.gitbook/assets/image%20(250).png)

8. Use the search bar to find records (default is case-insensitive). Enable case-sensitivity if needed.

![Case Sensitivity Option](../../../../.gitbook/assets/image%20(251).png)

---

### Additional Features

- **Export to CSV**: Export report data using this feature.

  ![Export Options](../../../../.gitbook/assets/image%20(252).png)

- **Consolidated Report**: View a combined report across related data sets.

  ![Consolidated View](../../../../.gitbook/assets/image%20(253).png)

- **Change View**: Customize visible columns by selecting from the available list.

  ![Column Selection](../../../../.gitbook/assets/image%20(254).png)

- **Column Search**: Locate specific fields using the column search.

  ![Search Columns](../../../../.gitbook/assets/image%20(255).png)

- **Dynamic Operators**: Based on selected columns, applicable operators (e.g., equals, contains) are shown.

  ![Operator Selection](../../../../.gitbook/assets/image%20(256).png)
