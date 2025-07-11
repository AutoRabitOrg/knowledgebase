# User Sessions

Vault provides administrators with visibility into all currently active user sessions within the organization.

> **Info:** Vault admins can view all user sessions for their org, whereas non-admins can only see their own session details.

---

## Viewing Active Sessions

Administrators can view and manage user sessions from the **Profile > Session Information** screen.

![Session Info](../../../.gitbook/assets/image%20(69)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png)
![Session List](../../../.gitbook/assets/image%20(70)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png)

To log out a user:
- Select the session from the list.
- Click **Logout** to immediately terminate the session. The user will be logged out and must re-authenticate to regain access.

### Session Fields

| FIELD                | DESCRIPTION                                                                    |
|----------------------|--------------------------------------------------------------------------------|
| **Public IP**        | IP address of the user's session                                               |
| **User**             | Username associated with the session                                           |
| **City**             | Geolocated city based on IP address                                            |
| **Location**         | Approximate geographic location of the IP address                              |
| **Device Details**   | Device type (e.g., Desktop, Mobile)                                            |
| **OS Details**       | Operating system used during the session                                       |
| **Browser Details**  | Web browser used during the session                                            |
| **Last Access Time** | Timestamp of last activity from the user in that session                       |

---

## Search for Activities of a Specific User <a href="#search-for-activities-of-a-specific-user" id="search-for-activities-of-a-specific-user"></a>

To monitor user activity:

1. Go to the **Session Information** page and click **Activity Log**.
2. Choose a **Time Period** (e.g., 1 month, 6 months, 1 year).
3. Select a **User** from the dropdown.
4. Enter a specific **Activity** keyword (e.g., backup, compare, replicate).
5. Click **Get Details**.

![Activity Log](../../../.gitbook/assets/image%20(71)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png)

---

## Export the Activity Log <a href="#export-the-activity-log" id="export-the-activity-log"></a>

1. On the **Activity Logs** page, click **Download**.
2. The activity log will be saved as a **CSV** file on your device.

![Export Logs](../../../.gitbook/assets/image%20(72)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).png)
