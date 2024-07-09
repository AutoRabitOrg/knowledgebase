# Enable SCA Apex PMD validation criteria.

The **org administrator** can define global validation criteria to enforce Static Code Analysis (SCA) tools such as Apex PMD across CI jobs, gated commits, and merge jobs. Based on the priority set, the build will be successful only if the criteria are met.

Before you set the SCA criteria, ensure the following:

* Apex PMD is integrated with ARM.
* You are an **org administrator** or have the privilege to access the **My Account** page.

## How to set the Apex PMD criteria? <a href="#how-to-set-the-apex-pmd-criteria" id="how-to-set-the-apex-pmd-criteria"></a>

1. Log into the ARM account.
2. Go to **Admin > My Account**.
3. Go to **Validation Criteria - Static Code Analysis** section and select the **Enable Validation Criteria - SCA** checkbox.
4. Select **ApexPMD** and now set the priorities for it.
5. In the screenshot below, the **Priority-3** is set to **greater** than **5**, which means if **Priority-3** related errors are more than **5**, it should **pass**, or else it will **fail**.\
   This means if **Priority-3** related errors are more than 5, it should pass, or&#x20;

<figure><img src="../../../../.gitbook/assets/image (32) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **Save** to save the changes.
7. Now, go to the **Commit Validation - Approval Settings** section. You can enforce the SCA criteria to run for all commits before being merged to the version control branch.
8. Select the **Enable criteria-based Review Process** checkbox.
9. Enable the second checkbox, i.e., **Should pass validation criteria for Static Code Analysis** checkbox.
10. Choose **ApexPMD**.
11. Select the **Auto reject commit process if the criteria are not met** checkbox to auto-reject the commit if the set standards are not met _(as mentioned in Step-2)_.

<figure><img src="../../../../.gitbook/assets/image (33) (1) (1) (1).png" alt="" width="486"><figcaption></figcaption></figure>

12. Click **Save**.

In the below screenshot, the SCA criteria were fulfilled _(Priority-3 should be greater than 5)_, and the validation commit was moved to the **Approved** state as expected.

<figure><img src="../../../../.gitbook/assets/image (34) (1) (1) (1).png" alt="" width="519"><figcaption></figcaption></figure>
