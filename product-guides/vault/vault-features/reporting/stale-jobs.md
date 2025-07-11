# Stale Jobs

## Preventing Stale Jobs

### Overview

The **Stale Jobs** feature in Vault enables administrators to monitor and manage jobs that have stalled during execution. Any job that remains inactive—i.e., without backend file updates—for **four consecutive days** is flagged as a *Stale Job*.

---

### Introduction

Vault manages stale jobs using a two-pronged approach:

1. **Automated Cron Job**: Scheduled weekly to identify and terminate long-running inactive jobs.
2. **Stale Jobs Interface**: Allows admins to manually view, select, and terminate stale jobs.

Key behaviors:
- Admins can manually terminate one or more stale jobs.
- For a single job, a **termination notification** is sent to both the admin and the job creator.
- For multiple jobs, a **consolidated notification** is delivered.

---

### How to Access the Stale Jobs Module

1. **Select the target Org** from the list of available organizations.

   ![Select Org](../../../../.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(2).png)

2. A list of jobs from various modules (Backup, Restore, Replicate, Archive) will be displayed for the selected Org.
3. Navigate between module tabs to review stale jobs in each category:

   - **Backup Jobs**  
     ![Backup Tab](../../../../.gitbook/assets/image%20(1)%20(1)%20(1)%20(1)%20(2).png)

   - **Restore Jobs**  
     ![Restore Tab](../../../../.gitbook/assets/image%20(2)%20(1)%20(1)%20(1)%20(2)%20(1).png)

   - **Replicate Jobs**  
     ![Replicate Tab](../../../../.gitbook/assets/image%20(3)%20(1)%20(1)%20(2).png)

   - **Archive Jobs**  
     ![Archive Tab](../../../../.gitbook/assets/image%20(4)%20(1)%20(1)%20(2).png)

---

### Terminating Stale Jobs

4. Select the jobs you wish to terminate and click **Terminate**.

5. **Notifications:**
   - **Single Job Termination**:  
     - An email is sent from the relevant module.
     - The message includes a new field: `Terminate Reason`.
   - **Multiple Job Termination**:  
     - A consolidated email lists all terminated jobs.

   ![Termination Notification](../../../../.gitbook/assets/image%20(5)%20(5).png)

This feature ensures system hygiene and prevents inactive jobs from consuming unnecessary system resources.
