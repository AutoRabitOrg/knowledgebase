# Error: "TF402455: Pushes to this branch are not permitted

### Description

Encountering an error while attempting to commit the changes for the production organization to the GitHub master branch. The error message states, **"TF402455: Pushes to this branch are not permitted; you must use a pull request to update this branch."**

### Cause

This is expected. When the branch is set with the branch policy, you cannot pushes it directly and need to create a pull request to update it.

### Resolution

Once you remove the branch policy, you should have the ability to push changes to the master branch. Please contact the GitHub Administrator to request push permissions.

\
