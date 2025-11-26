# ARM Known Limitations

These are the known limitations in **ARM® 22.3**.

### **List of Failure Cases / Limitations** <a href="#list-of-failure-cases-limitations" id="list-of-failure-cases-limitations"></a>

1. **Patch Can't Apply Commit Failing: If there are conflicts on the same line in modified files.** For example, when multiple users make changes to the same line and User-2 has committed to the remote branch. If User-1 then tries to perform the commit on a previously created prevalidation commit label, the commit will fail.
2. **Patch Can't Apply Commit Failing: If there are conflicts on added files.** Similar to the previous case, multiple users are making commits to the same new files. If User-2 has committed to the remote branch, and User-1 then tries to perform a commit already created using a prevalidation commit label, the commit will fail.
3. **Patch Can't Apply Commit Failing: If multiple users make changes in between 3–4 lines.** This scenario leads to conflicts; the patch and commit will fail.
4. **Patch Can't Apply Commit Failing: In some cases, specific metadata type components may have conflicts, while other metadata type components may not have conflicts.** This scenario leads to conflicts; the patch and commit will fail.
