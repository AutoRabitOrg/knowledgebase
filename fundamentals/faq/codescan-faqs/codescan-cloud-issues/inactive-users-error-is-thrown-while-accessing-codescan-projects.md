# Inactive user error

## Error Description

Sometimes, an "**Inactive user**" error may appear at the start of an analysis:

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Cause

It could be caused by the following scenarios, in which the user who created the project and provided credentials for it:

* Is no longer a member of the team and was removed.
* Had their permissions changed in CodeScan.
* Had their permissions changed in repo/environment that is scanned.

## Solution

To resolve the “**Inactive user**“ issue, you need to reattach the project—without deleting its history.

Follow these steps:

1. Delete the project analysis:

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Important!** Do **not** select the checkbox to '**Delete Project also?'** if you want to keep the current project and its history:

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Reattach analysis:

<figure><img src="../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

3. Provide repo/environment credentials:

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

4. Rerun the SCA; it should succeed.

If the steps above were completed, but the issue persists, contact [support@autorabit.com](mailto:support@autorabit.com).
