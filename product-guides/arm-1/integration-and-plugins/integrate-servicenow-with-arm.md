# Integrate ServiceNow with ARM

## Step 1: Store Your ServiceNow Credentials in ARM

1. Log in to your ARM account.
2.  Navigate to the **Admin** module and click the **Credentials** tab.

    ![Credential Tab](<../../../.gitbook/assets/image (900).png>)
3.  Click **Create Credential** from the right navigation.

    ![Create Credential](<../../../.gitbook/assets/image (901).png>)
4. In the popup:
   * Enter a **Credential Name**
   * Set **Credential Type** to _User name with Password_
   * Input your **ServiceNow username** and **password**
   * Ensure you're using your **username**, not your login email
5.  Click **Save**

    ![Credential Entry](<../../../.gitbook/assets/image (902).png>)

***

## Step 2: Integrate ServiceNow with ARM

1. Log in to ARM (if not already logged in).
2. Go to **Admin > My Account**
3.  Click **New ALM System** under the **ALM Management** section

    ![New ALM System](<../../../.gitbook/assets/image (903).png>)
4.  Set **ALM Type** as _SERVICENOW_

    ![ALM Type](<../../../.gitbook/assets/image (904).png>)
5. Enter:
   * A **Label Name**
   * Your ServiceNow **subdomain URL** (e.g., `https://[subdomain].service-now.com`)
   * The **credentials** stored in Step 1
6. Click **Test Connection** to validate
7. Click **Save** to complete the integration

> Once integrated, you can log bugs/issues to ServiceNow directly from ARM.

{% hint style="danger" %}
**Note:** ServiceNow OAuth integration is supported only for **Cloud versions**. Contact **support@autorabit.com** to enable this feature.
{% endhint %}

***

## Configuring ServiceNow Work Items in ARM

### EZ-Commit Integration

1.  In the **EZ-Commit** screen under **Post Commit**:

    * Check **Update ALM Workitem Status**
    * Select:
      * **ALM Type:** SERVICENOW
      * **ALM Label, Project, Sprint,** and **Work Item**
      * **Status** to be updated

    ![EZ Commit Config](<../../../.gitbook/assets/image (905).png>)
2. Upon commit, work item status will be reflected in ServiceNow.

***

### CI Job Integration

#### Applicable to:

* Package from Version Control
* Deploy from Version Control
* Deploy from SFDX branch to Salesforce Org
* Install Unlocked Package from VCS

1.  In **Build** section of CI Job creation:

    * Check **Map ALM Project (Ex: ServiceNow)**

    ![CI Job Build](<../../../.gitbook/assets/image (906).png>)
2.  Go to **ALM** section:

    * Set:
      * **ALM Type:** SERVICENOW
      * **Label** and **Projects**

    ![ALM Projects](<../../../.gitbook/assets/image (907).png>)
3.  Choose:

    * One or all **Active Sprints**

    ![Sprint Selection](<../../../.gitbook/assets/image (908).png>)
4.  Select:

    * **Work Item Type** (or all)

    ![Work Item Type](<../../../.gitbook/assets/image (909).png>)
5.  Update the **Status** for selected work item types

    ![Status Update](<../../../.gitbook/assets/image (910).png>)
