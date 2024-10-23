# Stale Jobs

## Preventing Stale Jobs

### Overview

This feature empowers users in tracking and terminating stale jobs in Vault. A long-running job that does not have any updates in its respective files in the back end for a period of 4 days is considered a ‘Stale Job.’

### Introduction

Vault handles stale jobs through a combination of Cron Job and a Stale Jobs report.

1. A cron job is scheduled to run once every week to identify and kill long-running stale jobs.
2. The Admin can select the required jobs from among the list of jobs displayed under the stale jobs module.
3. Once the Admin selects the required jobs, the admin can continue to terminate the selected jobs using the “Terminate” button on the page.
4. If the Admin terminates a single job, then a notification email from the respective module will be triggered to the admin and the user who created the job.
5. If the Admin terminates a group of jobs, then a consolidated job termination email will be sent to the admin and the user who created the job.

### Detailed Instructions

Follow these step-by-step instructions to access the “Stale Jobs” module in the Vault application.

1\.      Select an Org from the available list of Orgs.

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

2. On selecting the ORG, the user will see displayed the list of jobs from the respective modules.&#x20;
3. The user can toggle between different tabs to view jobs from different modules.

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (2).png" alt=""><figcaption><p>Backup</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (2) (1).png" alt=""><figcaption><p>Restore</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (2).png" alt=""><figcaption><p>Replicate</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (2).png" alt=""><figcaption><p>Archive</p></figcaption></figure>

4. The admin can select the jobs and terminate the required long-running stale jobs from the respective modules.
5. Once the jobs are terminated, a notification will be sent to the admin and the respective user who created the jobs.
   * **Single Job Termination:**
     * The user will receive the standard notification related to that module with the addition of a new field, “Terminate Reason,” which was added to the email templates for Backup, Restore, Replicate, and Archive.
   * **Multiple Jobs for Termination:**
     * As the user terminates a list of jobs, the user will receive a consolidated email listing the jobs terminated.

<figure><img src="../../../../.gitbook/assets/image (5) (5).png" alt=""><figcaption></figcaption></figure>

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;
