# Workspaces

## What is a Workspace?  <a href="#what-is-workspace" id="what-is-workspace"></a>

A workspace is a container in which you code. For example, say you're trying to commit the code changes through EZ-Commit to a version control repository branch. In such case, a workspace gets created dynamically and it gets assigned to your repository/branch. Multiple workspaces get created for each commit/merge operation in ARM. If the workspace is already available, then the operation will get invoked in the existing one.

## Workspace Storage  <a href="#workspace-storage" id="workspace-storage"></a>

Each workspace has a total storage limit of **500 GB** allocated per tenant. An email notification will be sent to users once the workspace limit is about to be reached. On the limit being reached, users will not be able to run any further operations in ARM unless the workspace size is either increased or idle workspaces are deleted.&#x20;

## Managing a Workspace <a href="#managing-workspace" id="managing-workspace"></a>

This section describes how Org Administrators can manage existing workspaces within an ARM instance.

### Viewing the Workspace <a href="#viewing-the-workspace" id="viewing-the-workspace"></a>

To view the workspace:

1. Log in to your ARM account.
2. Hover your mouse over the **Admin** tab and click on **Workspaces**.

<figure><img src="../../../.gitbook/assets/image (721).png" alt="" width="170"><figcaption></figcaption></figure>

3. The list of workspaces created/available to date will be listed on this page.

<figure><img src="../../../.gitbook/assets/image (722).png" alt=""><figcaption></figcaption></figure>

4. Each workspace will have:
   * Workspace label
   * Date/time stamp for workspace created
   * Workspace allocated author detail
   * Repo and Branch details
   * Workspace status, i.e., running or in idle state
   * The module on which the workspace has been allotted
   * Last used on along with the size consumed

### Resetting a Workspace <a href="#reset-a-workspace" id="reset-a-workspace"></a>

You can reset your workspace to revert to the default workspace settings for your user account.

1. In the **Workspaces** tab, check for your workspace label and click on **Reset**.
2. Upon confirmation, the workspace is reset to the default workspace for your user account.

<figure><img src="../../../.gitbook/assets/image (723).png" alt=""><figcaption></figcaption></figure>

### Deleting a Workspace <a href="#deleting-a-workspace" id="deleting-a-workspace"></a>

You can delete a workspace if it is no longer required. Deleting a workspace is permanent and unrecoverable, and it may have an impact on the jobs running on the workspace. However, deleting a workspace will not delete the repository or branches within it. Repositories/branches that belong to other workspaces will not be affected.

An **Org Administrative** user can delete the workspaces of another user.

{% hint style="info" %}
**Important Note**: If you are unable to delete a workspace, it is because you lack the required permissions. The **Delete** option will not be available.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (724).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (725).png" alt=""><figcaption></figcaption></figure>

Once confirmed, the workspace gets deleted.

### Deleting Inactive Workspaces <a href="#deleting-inactive-workspaces" id="deleting-inactive-workspaces"></a>

Deleting inactive workspaces can free up resources for other users. Workspace **Settings** allow you to delete multiple workspaces at one time that are in an idle state for a longer period of time.

Click on the **Settings** button and specify the final date when all workspaces are cleared.

<figure><img src="../../../.gitbook/assets/image (726).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (727).png" alt="" width="418"><figcaption></figcaption></figure>

## Workspace Configurations <a href="#workspace-configurations" id="workspace-configurations"></a>

If the workspace limit is reached, the user may submit a request to increase the size of their workspace. Our super administrator will confirm the same with the user, and the workspace limit is extended based on the user subscriptions.&#x20;

The Super Admin needs to log in to ARM with super admin credentials and then navigate to **Workspace Mgmt.** page.

Based on the user's org requirement/subscription, the super admin will add additional workspace to the current org limit. The max size limit which can be increased is **1,000 GB**.

<figure><img src="../../../.gitbook/assets/image (728).png" alt=""><figcaption></figcaption></figure>

