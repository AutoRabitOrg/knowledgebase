# Scheduled Reports

### Overview <a href="#overview" id="overview"></a>

You can schedule to run the project reports daily, weekly or monthly using this option. On scheduling the report, the selected report gets generated automatically on the specified date and time and the generated report is sent to the respective user through e-mail. Thus by scheduling the reports you get the data in regular intervals without manually generating it.

#### What's New

Previously, the project reports were available for download for the main branches. With **CodeScan 22.7** update, we now support generating reports manually or by scheduling them for every project branch.

To configure scheduled reports,

1. Select the CodeScan organization and choose your project.
2.  Navigate to the **More** tab and choose **Project Reports** from the dropdown.\


    <figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption><p>Project Reports</p></figcaption></figure>
3. Choose **Scheduling** option as **Cron**, if not automatically selected.
4. The **Cron expression** is a string consisting five subexpressions (fields) that describe individual details of the schedule.

| Cron Value   | Allowed Values  | Allowed Special Characters |
| ------------ | --------------- | -------------------------- |
| Minutes      | 0-59            | , - \* /                   |
| Hours        | 0-23            | , - \* /                   |
| Day of month | 1-31            | , - \* /                   |
| Month        | 0-11 or JAN-DEC | , - \* /                   |
| Day of week  | 1-7 or SUN-SAT  | , - \* ? / L C #           |

5. Choose **Receive Scheduled Reports** as **Enabled**.
6.  Click **Run now**.\


    <figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="563"><figcaption><p>Run Now</p></figcaption></figure>
