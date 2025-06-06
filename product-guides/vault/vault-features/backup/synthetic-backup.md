# Synthetic Backup

Synthetic backup accelerates the process by capturing only the delta since the last full backup. These delta changes are merged with the existing full backup, eliminating the need to recreate a full backup from scratch. When the “Enable Synthetic Backup (Faster Backup)” option is selected, it ensures faster full backups by reusing prior backup data efficiently.

### Process Flow – Backup Configuration:

1. Only if the “Full Backup” option is selected for any job being created.
2.  &#x20;The “Enable Synthetic Backup (Faster Backup)” is available for selection, and, the option comes auto-enabled for the above said selections.

    <figure><img src="../../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>
3. If a synthetic backup need not be run on a full backup, the “Enable Synthetic Backup (Faster Backup)” option has to be explicitly disabled.&#x20;
4.  Observe the “Enable Synthetic Backup (Faster Backup)” option, and the info icon which provides information about the same.

    <figure><img src="../../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

### Process Flow – Start Backup:

On triggering a backup, if a configuration for which the “Enable Synthetic Backup (Faster Backup)” is enabled. The option comes auto enabled on the “Start Backup” pop-up.

<figure><img src="../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

&#x20;

&#x20;

&#x20;
