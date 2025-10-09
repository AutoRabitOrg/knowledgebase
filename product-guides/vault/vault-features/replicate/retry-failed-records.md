---
hidden: true
---

# Retry Failed Records

## Overview

The retry failed records feature provides a streamlined way to reprocess only the failed records from Replicate jobs. Instead of rerunning the entire job, Vault allows retrying failed records exclusively, saving time and improving efficiency.

## Step-by-Step Guide

1.  After a job completes, the retry option becomes available to reprocess failed records.

    <figure><img src="../../../../.gitbook/assets/image (2065).png" alt=""><figcaption></figcaption></figure>
2.  Click the Circular play icon to initiate the retry process.

    <figure><img src="../../../../.gitbook/assets/image (2066).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../.gitbook/assets/image (2068).png" alt=""><figcaption></figcaption></figure>
3. In “Retry Replicate Summary”, selecting 'Restore Now' will only attempt to restore failed records.
4. The retry option remains available for 30 days from the time the job is initiated.
5.  After the retention period elapses, the retry button is disabled (grayed out).

    <figure><img src="../../../../.gitbook/assets/image (2069).png" alt=""><figcaption></figcaption></figure>

