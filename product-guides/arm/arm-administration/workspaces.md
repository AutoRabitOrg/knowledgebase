# Workspaces

A **workspace** is your isolated “build room” inside AutoRABIT (ARM).\
Whenever you run an operation that needs local disk—such as **EZ-Commit**, a **merge** or a **CI job**—ARM spins up (or re-uses) a workspace linked to the repo/branch in question. That keeps files, temporary build artifacts, and logs separated per operation, so one task never overwrites another.

***

## What Is a Workspace? <a href="#what-is-workspace" id="what-is-workspace"></a>

Think of a workspace as a **containerized file system**:

* It’s created (or re-attached) automatically when you start a commit, merge, or CI task.
* Multiple workspaces can exist side-by-side—one per concurrent job.
* If a matching workspace already exists, the new job re-uses it to save spin-up time.

***

## Workspace Storage <a href="#workspace-storage" id="workspace-storage"></a>

* Every tenant receives **500 GB** of workspace capacity.
* ARM emails admins when usage approaches the limit.
* Once the cap is hit, no new jobs can start until you **increase the limit** or **delete idle workspaces**.

***

## Managing a Workspace <a href="#managing-workspace" id="managing-workspace"></a>

Only **Org Administrators** can view, reset, or delete workspaces.

### Viewing the Workspace List <a href="#viewing-the-workspace" id="viewing-the-workspace"></a>

1. Log in to ARM.
2.  Go to **Admin › Workspaces**.

    <figure><img src="../../../.gitbook/assets/image (721).png" alt="Admin menu highlighting Workspaces option" width="170"><figcaption></figcaption></figure>
3.  The list shows every workspace ever created:

    <figure><img src="../../../.gitbook/assets/image (722).png" alt="Workspace list with labels, authors, sizes"><figcaption></figcaption></figure>

    | Field                | Description                                           |
    | -------------------- | ----------------------------------------------------- |
    | **Label**            | Workspace name (auto-generated)                       |
    | **Created On**       | Timestamp of first creation                           |
    | **Author**           | User who owns the workspace                           |
    | **Repo / Branch**    | Git location tied to the workspace                    |
    | **Status**           | _Running_ or _Idle_                                   |
    | **Module**           | ARM feature that created it (EZ-Commit, CI Job, etc.) |
    | **Last Used / Size** | Date of last activity and storage consumed            |

***

### Resetting a Workspace <a href="#reset-a-workspace" id="reset-a-workspace"></a>

Reset wipes the folder contents but keeps the workspace record.

1. Find the workspace and click **Reset**.
2.  Confirm to restore default state.

    <figure><img src="../../../.gitbook/assets/image (723).png" alt="Reset confirmation dialog"><figcaption></figcaption></figure>

***

### Deleting a Workspace <a href="#deleting-a-workspace" id="deleting-a-workspace"></a>

Delete removes the workspace permanently (repositories remain intact).

1. Click the trash-can icon next to the workspace.
2.  Confirm twice—you cannot undo this.

    <figure><img src="../../../.gitbook/assets/image (724).png" alt="Delete workspace button"><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (725).png" alt="Final delete confirmation modal"><figcaption></figcaption></figure>

{% hint style="info" %}
If the **Delete** button is missing, your role lacks the required permission.
{% endhint %}

{% hint style="info" %}
If the **Delete** button is grayed out, see the FAQ [below](workspaces.md#why-am-i-unable-to-delete-certain-workspaces).&#x20;
{% endhint %}

***

### Bulk-Deleting Inactive Workspaces <a href="#deleting-inactive-workspaces" id="deleting-inactive-workspaces"></a>

Free up space by purging all workspaces idle since a given date.

1.  Click **Settings**.

    <figure><img src="../../../.gitbook/assets/image (726).png" alt="Workspace Settings gear icon"><figcaption></figcaption></figure>
2.  Choose the cutoff date and confirm.

    <figure><img src="../../../.gitbook/assets/image (727).png" alt="Delete inactive workspaces dialog" width="418"><figcaption></figcaption></figure>

***

## Workspace Configurations <a href="#workspace-configurations" id="workspace-configurations"></a>

Need more space? An Org Admin can request an increase.

* Super Admin logs in and opens **Workspace Mgmt**.
* Raise the tenant limit—maximum **1 TB** (1000 GB)—based on subscription.

<figure><img src="../../../.gitbook/assets/image (728).png" alt="Super Admin screen showing workspace size adjustment"><figcaption></figcaption></figure>

Once approved, the new cap takes effect instantly and users can resume jobs without deleting old workspaces.

***

## Best Practices

* **Clean up idle workspaces weekly** to avoid hitting the limit.
* **Reset** instead of **Delete** if you just want a fresh working directory.
* Monitor the **Last Used / Size** column to spot abandoned, space-hogging workspaces early.

***

## FAQ

#### Why am I unable to delete certain workspaces?

Despite having admin privileges in your instance, you are unable to delete certain workspaces, as the Delete button appears grayed out, as shown in the screenshot below.

<figure><img src="../../../.gitbook/assets/image (1751).png" alt=""><figcaption><p>Base Workspaces</p></figcaption></figure>

The reason the Delete button is grayed out is that these workspaces are classified as Base Workspaces. Base workspaces are directly linked to a branch in your instance, and they cannot be deleted unless the associated branch is unregistered from AutoRABIT. When you register a new branch, a workspace is created, and they are tightly connected.

If you still wish to remove any workspace where the delete option is grayed out, please ensure that the related branch is no longer needed, and proceed to unregister the branch. Once the branch is unregistered, you will be able to delete the associated workspace.
