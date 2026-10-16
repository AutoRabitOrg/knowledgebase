# create a pr fix

**Who this is for:** developers | **Uses AI credits:** yes | **Availability:** <mark style="color:red;">**\[TO CONFIRM]**</mark> <mark style="color:red;">**\[TO CONFIRM: how PR fixes are billed. The review page shows "Billed: n fixed findings"]**</mark>

A PR fix turns the AI-generated fixes from a scan into a pull request. CodeScan never raises the pull request on its own. You review every change, can edit it or leave files out, and then choose to create the pull request.

## Before You Start

* The scan must have suggested fixes, so **`Advanced AI Suggestions`** must be on for the repository. <mark style="color:red;">**\[TO CONFIRM: any other requirements]**</mark>
* The repository must be connected with an access token that allows CodeScan to push a branch and open a pull request. See [Register a Repository](/broken/pages/252a201d6a6737cbb7c285cb00a100a07e78ce4f).

## Starting a PR Fix

{% stepper %}
{% step %}
### Open the scan
{% endstep %}

{% step %}
### Select **`Create PR`** at the top of the page
{% endstep %}

{% step %}
### Select **`New PR fix`**

When the fixes are ready, the PR fix appears in the **`Create PR`** menu with its status, for example _Ready for review · 2/2 fixed_, and a **Review by** date. Select **`Review changes`** to open it.

<mark style="color:red;">**\[SCREENSHOT: Create PR menu (project file PR\_fix\_01\_scan\_page\_Create\_PR.png)]**</mark>
{% endstep %}
{% endstepper %}

## Reviewing the PR Fix

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

{% stepper %}
{% step %}
### Edit the **`Pull request title`** if you want

It is filled in for you, for example _CodeScan: fix 2 findings_.
{% endstep %}

{% step %}
### Add a **`Description`**

Leave it empty and CodeScan writes one from the fixed findings.
{% endstep %}

{% step %}
### Choose the files to include

In the file list, clear the checkbox next to any file you don't want in the pull request.
{% endstep %}

{% step %}
### Review and edit each fix

Select a file to see its fix side by side with the current code. You can edit the fix directly. **`Reset to AI version`** undoes your edits to that file.
{% endstep %}
{% endstepper %}

<mark style="color:red;">**\[SCREENSHOT: Review PR fix page (project file PR\_fix\_02\_Review\_PR\_fix\_page.png)]**</mark>

## Creating the Pull Request

When you're happy with the changes, select **`Create PR`**. CodeScan pushes the fix branch and opens a pull request against the target branch in your git host. Your team reviews and merges it like any other pull request, with your usual checks.

To abandon the PR fix, select **`Discard`**.

{% hint style="info" %}
**Note:** Treat a PR fix like any other change. Run your tests, and let your normal review and CI checks run on the pull request before merging.
{% endhint %}

## Related Articles

* [Suggested Fixes and Patches](/broken/pages/de955a8bba000807df59b20c80febbff6a601f52)
* [Register a Repository](/broken/pages/252a201d6a6737cbb7c285cb00a100a07e78ce4f)
* [AI Credits](/broken/pages/dcabf38942457e4fb002b4dea23979ce1ff57b1b)
