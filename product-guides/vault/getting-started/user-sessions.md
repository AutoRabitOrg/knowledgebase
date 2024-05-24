# User Sessions

A new feature released by [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) allows the administrator to view a list of all the currently active users in the Vault.

{% hint style="info" %}
Vault admins can view all user sessions for an org; non-admins see only their own sessions.&#x20;
{% endhint %}

In addition to viewing all active sessions, the administrator can terminate any active session. This will automatically log the user out of the Vault. To do this, the administrator has to navigate to the **Profile > Session Information**.

<figure><img src="../../../.gitbook/assets/image (69) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (70) (1) (1).png" alt=""><figcaption></figcaption></figure>

Here the administrator can select any required user session and click on **Logout** to terminate that user’s session. The user will be automatically logged out from the organization as soon as the administrator clicks **Logout**.

When the admin manually ends a user’s session, the user must log in again to the Vault.&#x20;

The following table contains information about the fields you can view on this page. Due to the nature of geolocation technology, the accuracy of geolocation fields may vary.&#x20;

| FIELD                | DESCRIPTION                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| **Public IP**        | The IP address associated with the session                                     |
| **User**             | The username used when logged in to the session.                               |
| **City**             | The city where the user’s IP address is physically located.                    |
| **Location**         | The approximate location of the IP address from where the user logged in.      |
| **Device Details**   | The device on which the user is logged in.  For example, Desktop, Mobile, etc. |
| **OS Details**       | The operating system details for the session.                                  |
| **Browser Details**  | The browser details for the session.                                           |
| **Last Access Time** | The date and time stamp of the last session update due to activity.            |

### Search for activities of a specific user <a href="#search-for-activities-of-a-specific-user" id="search-for-activities-of-a-specific-user"></a>

1. On the **Session Information** page, click on **Activity Log**. The activity log page can display the user activity list up to 100 records per page. The default sort order is **Date/Time**.
2. Next, in the **Time Period** field, select the date range from the list. For example, 1 month, 6 months, or 1 year.
3. In the **Users** field, select a username.
4. Under **Activity Search**, mention the Vault activity to fetch the result. For ex- backup, compare, replicate, etc.&#x20;
5. Click on **Get Details.**

<figure><img src="../../../.gitbook/assets/image (71) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Export the Activity Log <a href="#export-the-activity-log" id="export-the-activity-log"></a>

1. Click the **Download** button on the Activity Logs page.
2. The file will be downloaded to your device in **CSV** file format.

<figure><img src="../../../.gitbook/assets/image (72) (1) (1).png" alt="" width="407"><figcaption></figcaption></figure>
