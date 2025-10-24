# Tip of your current branch is behind

## Error message: Tip of your current branch is behind

This error usually occurs when you try to push a commit to a target branch, but the `HEAD` has been updated by someone else after you started your merge. You need to fetch the latest changes from the remote repository using **git fetch** and then merge them into your local branch using **git merge** before attempting to push again. You **can’t re-push** because:

* Your merge commit references an **older state** of the target branch.
* Re-pushing would **skip** newer commits, which could cause lost work or conflicts.

You need to **re-perform the merge** using the latest version of the target branch.
