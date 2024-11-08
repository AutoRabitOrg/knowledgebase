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
2. Hover your mouse over the **Admin** tab and click on **Workspaces**.

<figure><img src="../../../.gitbook/assets/image (721).png" alt="" width="170"><figcaption></figcaption></figure>

3. The list of workspaces created/available to date will get listed on this page.

<figure><img src="../../../.gitbook/assets/image (722).png" alt=""><figcaption></figcaption></figure>

4. Each workspace will have:
   * Workspace label
   * Date/time stamp for workspace created
   * Workspace allocated author detail
   * Repo and Branch details
   * Workspace status, i.e., running or in idle state
   * The module on which the workspace has been allotted
   * Last used on along with the size consumed

#### Reset a Workspace <a href="#reset-a-workspace" id="reset-a-workspace"></a>

You reset your workspace to return back to the default workspace settings for your user account.

1. In the **Workspaces** tab, check for your workspace label and click on **Reset**.
2. Upon your confirmation, the workspace gets reset to the default workspace for your user account.

<figure><img src="../../../.gitbook/assets/image (723).png" alt=""><figcaption></figcaption></figure>

#### Deleting a Workspace <a href="#deleting-a-workspace" id="deleting-a-workspace"></a>

Delete a workspace if it is no longer required. Deleting a workspace is permanent and unrecoverable, and may have an impact on the jobs running on the workspace. However, deleting a workspace will not delete the repository or branches within it. Repository/branch that belongs to other workspaces will not be affected.

An **Org Administrative** user can delete the workspaces of another user.

{% hint style="info" %}
**Important Note**: If you are unable to delete a workspace, it is because you lack the required permissions. The **Delete** option will no longer be available.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (724).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (725).png" alt=""><figcaption></figcaption></figure>

Once confirmed, the workspace gets deleted.

#### Deleting Inactive Workspaces <a href="#deleting-inactive-workspaces" id="deleting-inactive-workspaces"></a>

Deleting inactive workspaces can free up resources for other users. Workspace **Settings** allow you to delete multiple workspaces at a single go that are in an idle state for a longer period.

Click on the **Settings** button and specify the last date until all workspaces are cleared.

<figure><img src="../../../.gitbook/assets/image (726).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (727).png" alt="" width="418"><figcaption></figcaption></figure>

### Workspace Configurations <a href="#workspace-configurations" id="workspace-configurations"></a>

If the limit is reached, the user may raise a request to increase the size of their workspace. Our super administrator will confirm the same with the user, and the workspace limit is extended based on the user subscriptions.&#x20;

The Super Admin needs to log in to ARM with super admin credentials and then navigate to **Workspace Mgmt.** page.

Based on the user's org requirement/ subscription, the super admin will add additional workspace to the current org limit. The max size limit which can be increased is **1000 GB**.

<figure><img src="../../../.gitbook/assets/image (728).png" alt=""><figcaption></figcaption></figure>

### **Workspace Storage Management**

* Once a feature flag is enabled, a new global workspace will be created for each repository in the "/workspaces/globalcheckouts" folder, and for commits/merges, new user workspaces will be created in "/workspaces/localcheckouts" and will be deleted after usage is completed. The existing user workspaces will remain unchanged for now; they will not be deleted immediately. Instead, they will be removed through scheduled jobs as previously done; no new migration has been added to delete workspaces. On the workspace sub-module, only the workspaces created after enabling the feature flag will be visible. Previous non-optimized workspaces will not be visible in the UI if the feature flag is active.

### **Rollback Plan**

* If the feature flag is turned off later, the existing non-optimized workspaces will be used since they were not removed. We will continue utilizing the previous workspaces stored in the base checkout and specific user directories **after sync with latest remote**. Even when the feature flag is enabled/disabled, the retention policy will remain unaffected and will continue to operate as usual.
