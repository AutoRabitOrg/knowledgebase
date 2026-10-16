---
description: >-
  Review, edit and turn AI-generated fixes into a pull request from the scan
  page.
---

# Create a PR Fix

A PR fix turns the AI-generated fixes from a scan into a pull request. CodeScan never raises the pull request on its own. You review every change, can edit it or leave files out, and then choose to create the pull request.

### Before You Start

* The scan must have suggested fixes, so **`Advanced AI Suggestions`** must be on for the repository.&#x20;
* The repository must be connected with an access token that allows CodeScan to push a branch and open a pull request. See Register a Repository.

### Starting a PR Fix

1. Open the scan.
2. Select **`Create PR`** at the top of the page.
3. Select **`New PR fix`**.

When the fixes are ready, the PR fix appears in the **`Create PR`** menu with its status, for example _Ready for review · 2/2 fixed_, and a **Review by** date. Select **`Review changes`** to open it.

### Reviewing the PR Fix

The **Review PR fix** page shows:

| Field               | Meaning                                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Status`**        | For example, **Ready for review**                                                                                                            |
| **`Target branch`** | The branch the pull request will merge into                                                                                                  |
| **`Fix branch`**    | The branch CodeScan creates for the fixes, named `codescan/fix-<scan>-<id>`                                                                  |
| **`Fixed`**         | How many of the selected findings have a fix, for example _2/2 findings_                                                                     |
| **`Files`**         | How many files the fixes change                                                                                                              |
| **`Billed`**        | How many fixed findings are charged                                                                                                          |
| **`Expires`**       | The date to review by. After it, the PR fix expires. <mark style="color:red;">**\[TO CONFIRM: expiry period. Seven days in testing]**</mark> |

To review the changes:

1. Edit the **`Pull request title`** if you want. It is filled in for you, for example _CodeScan: fix 2 findings_.
2. Add a **`Description`**, or leave it empty and CodeScan writes one from the fixed findings.
3. In the file list, clear the checkbox next to any file you don't want in the pull request.
4. Select a file to see its fix side by side with the current code. You can edit the fix directly. **`Reset to AI version`** undoes your edits to that file.

### Creating the Pull Request

When you're happy with the changes, select **`Create PR`**. CodeScan pushes the fix branch and opens a pull request against the target branch in your git host. Your team reviews and merges it like any other pull request, with your usual checks.

To abandon the PR fix, select **`Discard`**.

{% hint style="info" %}
**Note:** Treat a PR fix like any other change. Run your tests, and let your normal review and CI checks run on the pull request before merging.
{% endhint %}

### Related Articles

* Suggested Fixes and Patches
* Register a Repository
* AI Credits
