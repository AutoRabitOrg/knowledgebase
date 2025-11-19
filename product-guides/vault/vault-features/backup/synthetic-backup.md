# Synthetic Backup

Synthetic backup accelerates the process by capturing only the delta since the last full backup. These delta changes are merged with the existing full backup, eliminating the need to recreate a full backup from scratch. When the “Enable Synthetic Backup (Faster Backup)” option is selected, it ensures faster full backups by reusing prior backup data efficiently.

### Process Flow – Backup Configuration

1. Only if the “Full Backup” option is selected for any job being created.
2.  &#x20;The “Enable Synthetic Backup (Faster Backup)” is available for selection, and, the option comes auto-enabled for the above said selections.

    <figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. If a synthetic backup need not be run on a full backup, the “Enable Synthetic Backup (Faster Backup)” option has to be explicitly disabled.&#x20;
4.  Observe the “Enable Synthetic Backup (Faster Backup)” option, and the info icon which provides information about the same.

    <figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Process Flow – Start Backup

On triggering a backup, if a configuration for which the “Enable Synthetic Backup (Faster Backup)” is enabled. The option comes auto enabled on the “Start Backup” pop-up.

<figure><img src="../../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Frequently Asked Questions (FAQs)

1. Restoration of Deleted Records (Scenario 1)

“In synthetic backup, if the previous backup had 200 records and the current only has 50, how do we manage or restore the deleted 150?”

Synthetic backup captures deltas (changes) from the last backup. If 150 records were deleted between backups, these deletions are recorded as part of the delta. The synthetic backup process preserves this change, and records deleted from Salesforce are still tracked and can be restored, assuming they haven’t been permanently removed (e.g., from the Recycle Bin).

* If “Exclude Deleted Records” is not enabled, the deleted records will be part of the backup.
* If excluded, the records may still be recoverable for a short period (e.g., 24 hours via API, if they exist in the Recycle Bin).
* Verification of deleted records should be done before the demo/restore process to confirm their availability.



2. Value Mismatch Between Backups (Scenario 2)

“How do I ensure the original field value (e.g., ‘gold’) is retained or identified during restoration?”

The restore process in synthetic backup retains the most recent valid value of the record:

* If a field’s previous value was “gold” and it changed to “silver,” synthetic backup retains both states through deltas.
* During restore, the process will use the original value from the selected backup version, ensuring consistency.
* You can identify the correct version by reviewing backup timestamps and performing a value audit if needed. This helps ensure data accuracy when restoring earlier field states.



3. Applicability to Metadata, Data Files, and Attachments

“Do changes apply to metadata, data files, and attachments as well?”

Yes, synthetic backup handles updates across:

* Metadata (e.g., changes in custom objects or fields)
* Data files (standard and custom object records)
* Attachments (including new or modified files)

The backup system ensures only new or changed attachments are included (no duplication), keeping the process efficient. For example, if 10 attachments exist and 2 new ones are added, the next backup captures only those 2 new additions.



4. Switching to Full Backups When Needed

“Can we switch back to using full backups if synthetic backups are not sufficient?”

Yes, you can switch back to full backups at any point based on your operational or compliance needs.

* The team has discussed and agreed that both backup types will remain available, and you can choose full backups if a scenario demands a more complete restore baseline or addresses automation-related deletion challenges.

\


&#x20;

&#x20;

&#x20;
