# Export Users Details

If you have **`Admin`** permissions, you can export a CSV file of all the users currently in your account. The CSV export will contain the following user information:

| Fields                | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `First Name`          | First Name                                                         |
| `Last Name`           | Last Name                                                          |
| `Status`              | User status - active or deactivated                                |
| `Email`               | Email address                                                      |
| `Login Name`          | Login Username                                                     |
| `Role`                | Assigned role                                                      |
| `Job Title`           | Job title                                                          |
| `Last Login Date`     | Last login date and time                                           |
| `Created Date`        | Date when the account was created                                  |
| `Created By`          | The user who created the account                                   |
| `Last Modified Date`  | Date when the account was last modified                            |
| `Last Modified By`    | The user who modified the account most recently                    |
| `Login Type`          | Login type: Standard or SSO                                        |
| `Last Login IP`       | The IP address of the user at the time of the last login           |
| `Last Login Lat/Long` | Geographical coordinates of the user at the time of the last login |
| `Last Login Location` | City, state, and country of the user at the time of the last login |
| `Last Login Browser`  | The user's browser at the time of the last login                   |
| `Deactivated Date`    | Date when the account was deactivated (if applicable)              |
| `Deactivated By`      | The user who deactivated the user account                          |

{% hint style="info" %}
**Important Note**: When a user logs in to ARM, the browser pop-up message will ask permission to access the location details. If you **allow** permission, the location details will be retrieved through your browser, but if you **deny** permission, the location details will be retrieved through your IP Address.
{% endhint %}

**To export all user's details in CSV:**

1. On the **`Users`** screen, in the upper right, click **`Export All Users`**.

<figure><img src="../../../../.gitbook/assets/image (577).png" alt=""><figcaption></figcaption></figure>

2. The fields you can export will be displayed on the next screen. Click the **`Export`** button after choosing the fields you want to export as CSV.

<figure><img src="../../../../.gitbook/assets/image (578).png" alt="" width="511"><figcaption></figcaption></figure>

{% hint style="info" %}
Fields like _`First Name, Last Name, Status, Email, and Login Name`_ are automatically selected by default when a CSV file is exported. If necessary, you can exclude them from being exported.
{% endhint %}

3. Your export will begin processing, and the CSV file will be downloaded on your local machine.

{% hint style="info" %}
**Export Data Limitations**: The parameters in the CSV for previously registered users (older than 60 days) will be slightly different:

* CreatedDate = OrgCreatedDate
* CreatedByName = registered user of the org
* LastModifiedDate, LastModifiedByName, Deactivated Date, and Deactivate by fields will be null

As expected, the exported CSV file will contain the newest parameter data and changes for newly registered users.
{% endhint %}
