# Configure Merge Approval

You can enforce this workflow using merge approvals to ensure one or more people approve every merge. Merge approvals allow you to set the necessary approvals that will need to approve every merge in a project.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* Enforcing review of all code that gets merged into a repository.
* Specifying reviewers for a given proposed code change.

### Configuring Approvals <a href="#configuring-approvals" id="configuring-approvals"></a>

To configure the merge approvals:

1. Login to ARM with the admin credentials.
2. Navigate to **Admin > My Account** and expand the **Merge Settings**
3. Tick the **Enable criteria-based Review Process** checkbox.
4. Select the **Enable Merge Approver** checkbox.
5. Set the minimum number of required approvals under the **Approval Level** box. _The minimum **Approval Level** can be **1**._

<figure><img src="../../../../.gitbook/assets/image (28) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **Save**.
7.  The steps above are the minimum required to get approvals working in your merge, but there are a couple more options available that might be suitable to your workflow:

    * **Auto commits on Approval:** This option will allow developers to work on their feature branches, and after review (approved), it gets automatically committed to the trunk.
    * **Disable Merge Self Approval:** This option will allow you to prevent _EZ-Merge approvers_ that have committed to a merge from approving it. However, the Org admins can still view the _approve/reject_ option and proceed with all the merges.

    <figure><img src="../../../../.gitbook/assets/image (29) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Eligible Approvers <a href="#eligible-approvers" id="eligible-approvers"></a>

1. No criteria can restrict the **org admin** from approving any merge.
2. The org admin can approve their merges even if the **Disable Merge Self Approval** checkbox is selected.
3. The **EZ-Merge Approver** _(non-admin user)_ cannot approve their merges if the **Disable Merge Self Approval** checkbox is selected.
4. No more approval is needed if the approval level is set to 2 and the org admin approves the merge.
5. The L1 and L2 approver email ids cannot be the same when the approval level is set to 2.

### More Information <a href="#more-informations" id="more-informations"></a>

The following details pertain to the criteria for commit validation approval:

1. There are no restrictions on the **org admin's** ability to approve any prevalidation commits.
2. If the **Disable Commit Self Approval** checkbox is enabled in **Commit Validation - Approval Settings**, the gated check-ins approvers cannot approve their commit unless they are an **org admin**. The org admins can view the _approve/reject_ option and proceed with the prevalidation commits.
3. If the **Enable Commit Approver** checkbox is checked, the _admin_ and the gated check-ins approver added to the reviewer list will be allowed to approve the prevalidation commits.

<figure><img src="../../../../.gitbook/assets/image (30) (1) (1).png" alt=""><figcaption></figcaption></figure>
