# ARM Known Issues

These are the known issues in **ARM® 22.2**.

#### Salesforce DX known issues <a href="#salesforce-dx-known-issues" id="salesforce-dx-known-issues"></a>

These are the known issues for [Salesforce DX](../../salesforce-dx.md) in this release.

**Failed to initiate deployment**\
If a process is added to Salesforce's queue for more than 30 minutes during the deployment of CI Jobs with SFDX Repo as the source, the error **"Failed to initiate deployment"** is returned.

#### Vlocity known issues <a href="#vlocity-known-issues" id="vlocity-known-issues"></a>

These are the known issues for vlocity in this release.

**"Autodraft" or "Select Manaully" feature in EZ-Commit screen timed out**\
For massive retrieval of [Vlocity](https://www.autorabit.com/industry-solution/healthcare-vlocity/) data packs, Auto-draft or Select Manually functionality has more chances to get timed out.

**Logs contain "undefined message" for vlocity commits**\
This known issue can be considered from the vlocity build tool rather than from ARM because for the log report that contains 'undefined message', such log error messages are being returned from the vlocity build tool only. Currently, [ARM](https://www.autorabit.com/products/automated-release-management/) is working with the vlocity tool to fix the issue as soon as possible. Stay tuned for more updates.

#### EZ-Merge known issues <a href="#ezmerge-known-issues" id="ezmerge-known-issues"></a>

**Issue:** The following error causes **EZ-Merge** to fail: `Cannot delete <metadata_type>; <metadata_components> must be deleted invidually`

**Reason:** ARM is unable to identify the deleted components from the `<metadata_type>`.

**Explanation:**\
Let's assume **Branch 1** has workflow components, _workflow 1_ and _workflow 2_; **Branch 2** is a child of **Branch 1** and has same components as **Branch 1** i.e., _workflow 1_ and _workflow 2_.\
If _workflow 1_ and _workflow 2_ are deleted from **Branch 2**, and merge is done from **Branch 2** to **Branch 1** with **Run Destructive Changes** checkbox selected, EZ-Merge prevalidation will fail with error: `Cannot delete <metadata_type>; <metadata_components> must be deleted individually.`\
This happens because the deleted workflow details are not retained in the application for validation.

**Sample image attached:**

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Workaround:** If you see the aforementioned issue, please avoid selecting the **Run Destructive Changes** checkbox under the **Prevalidate Merge** section.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>
