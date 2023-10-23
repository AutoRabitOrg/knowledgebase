# Workspaces

### What is Workspace?  <a href="#what-is-workspace" id="what-is-workspace"></a>

A workspace is a container where you code in. For example, you're trying to commit the code changes through EZ-Commit to a version control repository branch. In such case, a workspace gets created dynamically and it gets assigned to your repository/branch. Multiple workspaces get created for each commits/merge operation in ARM. If the workspace is already available, then the operation will get invoked in the existing one.

### Workspace Storage  <a href="#workspace-storage" id="workspace-storage"></a>

Each workspace has a total storage limit of **500 GB** allocated per tenant. An email notification will be sent to the users once the workspace limit is about to reach. On limit being reached, the users will not be able to run any further operation in ARM unless the workspace size is either increased or idle workspaces are deleted.&#x20;

### Managing Workspace <a href="#managing-workspace" id="managing-workspace"></a>

This section describes how Org Administrators can manage existing workspaces within an ARM instance.

#### Viewing the Workspace <a href="#viewing-the-workspace" id="viewing-the-workspace"></a>

To view the workspace:

1. Log into your ARM account.
2.  Hover your mouse over the **Admin** tab and click on **Workspaces**.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613542405387.png" alt="" width="188"><figcaption></figcaption></figure>
3.  The list of workspaces created/available to date will get listed on this page.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613542492393.png" alt=""><figcaption></figcaption></figure>
4. Each workspace will have:
   1. Workspace label
   2. Date/time stamp for workspace created
   3. Workspace allocated author detail
   4. Repo and Branch details
   5. Workspace status i.e., running or in idle state
   6. The module on which the workspace has been allotted
   7. Last used on along with the size consumed

#### Reset a Workspace <a href="#reset-a-workspace" id="reset-a-workspace"></a>

You reset your workspace to return back to the default workspace settings for your user account.

1. In the **Workspaces** tab, check for your workspace label and click on **Reset**.
2. Upon your confirmation, the workspace gets reset to the default workspace for your user account.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613543615991.png" alt=""><figcaption></figcaption></figure>

#### Deleting a Workspace <a href="#deleting-a-workspace" id="deleting-a-workspace"></a>

Delete a workspace if it is no longer required. Deleting a workspace is permanent and unrecoverable, and may have an impact on the jobs running on the workspace. However, deleting a workspace will not delete the repository or branches within it. Repository/branch that belongs to other workspaces will not be affected.

An **Org Administrative** user can delete the workspaces of another user.

{% hint style="info" %}
**Important Note**: If you are unable to delete a workspace, it is because you lack the required permissions. The **Delete** option will no longer be available.
{% endhint %}

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613543652658.png)

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618692124471.png)

Once confirmed, the workspace gets deleted.

#### Deleting Inactive Workspaces <a href="#deleting-inactive-workspaces" id="deleting-inactive-workspaces"></a>

Deleting inactive workspaces can free up resources for other users. Workspace **Settings** allow you to delete multiple workspaces at a single go that are in an idle state for a longer period.

Click on the **Settings** button and specify the last date until all workspaces are cleared.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613543692142.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1618692634020.png" alt="" width="375"><figcaption></figcaption></figure>

### Workspace Configurations <a href="#workspace-configurations" id="workspace-configurations"></a>

If the limit is reached, the user may raise a request to increase the size of their workspace. Our super administrator will confirm the same with the user, and the workspace limit is extended based on the user subscriptions.&#x20;

The Super Admin needs to log in to ARM with super admin credentials and then navigate to **Workspace Mgmt.** page.

Based on the user's org requirement/ subscription, the super admin will add additional workspace to the current org limit. The max size limit which can be increased is **1000 GB**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1613543905665.png" alt=""><figcaption></figcaption></figure>
