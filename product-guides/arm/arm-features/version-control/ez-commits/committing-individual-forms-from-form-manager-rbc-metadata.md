# Committing Individual Forms from Form Manager (RBC Metadata)

### Scenario

A user has 10 Record-Based Configuration (RBC) records (e.g., forms in Form Manager) in a Salesforce org. They want to **deploy only one form** to the Git repository using ARM. However, after committing that one form, the repo only contains that record, and the other 9 forms are **missing**—effectively overwritten.

### Expected Behavior

#### Should pulling and committing a single form merge it into the existing set of forms or replace the full folder?

By default, **ARM will replace** the contents of the RBC directory (e.g., `FormManager`) in the Git repo with whatever records are present in the commit—**even if it’s just one record**. So if only one form is committed, the other nine forms will be removed, unless specifically preserved in the workflow.

### Best Practice: Avoid Overwriting the Full Set

To safely commit a single form **without losing the others**, follow these guidelines:

#### 1. Use Merge or Append Mode (When Supported)

* When committing changes from an org to Git using ARM, configure the commit mode to **merge** or **append**, not replace.
* This ensures new records are being **added to** the existing set in Git rather than **replacing** the folder contents.
* **Source:** [AutoRABIT Docs – Commit Changes from Org to Version Control](https://docs.autorabit.com/docs/commit-changes-from-org-to-version-control)

#### 2. Avoid Committing a Partial Folder

* If ARM pulls and prepares a folder (like `FormManager`) with only one record, it treats that as the _entire_ state.
* **Workaround:** Use the **EZ-Merge** or **file-level commit view** to cherry-pick the new or modified record and keep the others intact.
* **Source:** [AutoRABIT Docs – EZ-Merge](https://docs.autorabit.com/docs/ez-merge)

#### 3. Use Full Pulls + Selective Commits When Possible

* Pull the full set of RBC records from the org.
* Use version control diffs to **selectively commit** the record you want to update.
* This ensures the rest of the records stay untouched in Git.
* **Source:** [AutoRABIT Docs – Managing Commits](https://docs.autorabit.com/docs/manage-commits)

### Important Notes

* This behavior applies to other RBC metadata types as well (e.g., Custom Metadata, Custom Labels).
* Review the **pre-commit diff view in ARM** before committing to ensure no unintended deletions occur.

### Summary

| Goal                                       | Recommended Action                                           |
| ------------------------------------------ | ------------------------------------------------------------ |
| Commit a single form without losing others | Use append/merge mode or EZ-Merge to cherry-pick the record  |
| Avoid overwriting the RBC folder           | Never commit a partial folder unless overwriting is intended |
| Preserve metadata consistency              | Validate the commit diff and consider pulling the full set   |
