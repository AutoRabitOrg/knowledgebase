# Exporting User Details

With **Admin** permissions you can download a CSV containing every user in your ARM tenant—handy for audits, license reviews, or compliance reports.

The export includes the following columns:

| Field                   | Description                                   |
| ----------------------- | --------------------------------------------- |
| **First Name**          | User’s first name                             |
| **Last Name**           | User’s last name                              |
| **Status**              | _Active_ or _Deactivated_                     |
| **Email**               | Email address                                 |
| **Login Name**          | Username used to sign in                      |
| **Role**                | Highest-privilege role assigned               |
| **Job Title**           | Title from the user profile                   |
| **Last Login Date**     | Timestamp of the most recent login            |
| **Created Date**        | Date the account was created                  |
| **Created By**          | User who created the account                  |
| **Last Modified Date**  | Date the account was last changed             |
| **Last Modified By**    | User who made the last change                 |
| **Login Type**          | _Standard_ (username/password) or _SSO_       |
| **Last Login IP**       | IP address recorded at last login             |
| **Last Login Lat/Long** | Latitude/longitude obtained at last login     |
| **Last Login Location** | City, state, and country resolved from the IP |
| **Last Login Browser**  | Browser string at last login                  |
| **Deactivated Date**    | Date the account was deactivated (if any)     |
| **Deactivated By**      | User who deactivated the account              |

{% hint style="info" %}
When a user signs in, ARM requests browser permission to access location services.

* **Allow** – latitude/longitude recorded via the browser.
* **Deny** – location inferred from the IP address.
{% endhint %}

***

## Export All Users to CSV

1.  In **Settings** **› Manage Users**, click **Export All Users** in the upper-right corner.<br>

    <figure><img src="../../../../../.gitbook/assets/image (1904).png" alt=""><figcaption></figcaption></figure>
2.  In the pop-up, choose which fields to include, then click **Export**.\
    <br>

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 2.59.36 PM.png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
Core identity fields—**First Name, Last Name, Status, Email, Login Name**—are preselected.\
Clear the checkboxes if you wish to omit them.
{% endhint %}

3. ARM generates the CSV and downloads it to your computer.

{% hint style="info" %}
#### Export Data Limitations

For users created **more than 60 days ago**, some values default:

* **Created Date** = Org creation date
* **Created By** = First registered user
* **Last Modified Date / By**, **Deactivated Date / By** = _null_

Recent users (≤ 60 days) include full, up-to-date metadata.
{% endhint %}
