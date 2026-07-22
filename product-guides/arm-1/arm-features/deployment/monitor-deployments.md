# Track Deployment History

{% hint style="info" %}
The **Deployment History** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

### Overview <a href="#overview" id="overview"></a>

You can monitor deployments in progress, check which deployments are validated successfully/failed, check which deployments are in a queue, and view the results of completed deployments on the **`Deployment History`** screen.

This page lists all deployments that you have triggered in ARM. Use the **Filter** option to pare down the list of deployments based on the deployment label name, date range, or deployment status.

When running a deployment, the **`Deployment History`** page shows you the real-time progress of your current deployment. This page contains charts that visually represent the overall deployment progress. If the current deployment has errors, you can view these errors before the deployment finishes by clicking on the **Deployment Log** button.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

You’ll need the **`Deployment History`** access permission.

### List of fields available on the Deployment History screen <a href="#list-of-fields-available-on-the-deployment-history-screen" id="list-of-fields-available-on-the-deployment-history-screen"></a>

<figure><img src="../../../../.gitbook/assets/image (2141).png" alt=""><figcaption></figcaption></figure>

1. **`Deployment Label:`** Deployment label along with the name of the user performing the deployment, the date and time when the deployment started, and the deployment status.
2. **`Destination Sandbox:`** Filter the deployments based on the destination sandbox chosen.
3.  **`Last Created Date Range:`** By using this filter, you may narrow down the jobs based on when they were created. By default, the last 7 days' jobs are displayed. The jobs created within the previous 14 days, 30 days, or 24 hours can be filtered. Use the custom range filter to specify more criteria. Then, choose the date and time range for when you want to view the jobs.<br>

    <figure><img src="../../../../.gitbook/assets/image (2142).png" alt="" width="563"><figcaption></figcaption></figure>
4.  **`Last Iteration Status:`** Filter the jobs based on the status of the most recent deployment.\
    <br>

    <figure><img src="../../../../.gitbook/assets/image (2144).png" alt=""><figcaption></figcaption></figure>
5. **`Deployment Iterations:`**&#x45;ach new deployment updates the revision of the Deployment. Such revision details can be seen here (revision number, date, and time of the deployment). Also, view the deployment log for each iteration, which gives you information about the entire deployment process run for the selected deployment label.

{% hint style="info" %}
**Important Notes:**

1. For Salesforce DX custom deployments, multiple deployments can be rendered at one time, and the results are shown separately. Suppose you have invoked several deployment requests, but you have chosen to abort the deployment phase for one of the deployments; in such case, the deployment will be aborted, but the other deployment will continue to operate in parallel.
2. Detailed information on which deployment was triggered and canceled will appear in the **Log** report.
{% endhint %}

6. **`Async ID:`** A unique identifier ID assigned to each deployment that helps track the deployment process.
7. **`Deployment Status:`** A visual representation of the overall deployment progress. The first chart shows how many components have already been deployed and includes the number of components with errors. After all components have been deployed without errors, Apex tests start executing, if required or enabled. A second chart shows how many Apex tests have run out of the total number of tests and the number of errors returned. In addition, the chart shows the name of the currently running test.
8.  List of Options available under the Deployment History screen.

    1. As a User:
       1.  The user who initiated the deployment can see the history screen and the deployment with details, like who the approvers are and the status of the deployment. Also, they can see the list of components' part of the deployment with any comments from the approvers. If it is a Salesforce deployment, they are able to view the SCA report as well.

           Users can also add any comments if required, e.g., "Deployment is waiting for approval."\
           \
           <br>

           <figure><img src="../../../../.gitbook/assets/image (1698).png" alt=""><figcaption><p>Iterations</p></figcaption></figure>

           <figure><img src="../../../../.gitbook/assets/image (1698).png" alt=""><figcaption><p>SCA Report</p></figcaption></figure>

           <figure><img src="../../../../.gitbook/assets/image (2145).png" alt=""><figcaption></figcaption></figure>
    2.  #### As an Approver <a href="#as-an-approver" id="as-an-approver"></a>

        As soon as the approver comes to the Deployment history screen, the approver clicks on the Deployment that is pending approval.

        1. What do we show the approver?
           1. Basic information on the deployment.
           2. Metadata selected for deployment, which has been changed or added
           3. Level 1 and Level 2 Approvers list.
           4. Comment history of Approvers & Users.
           5. If the user enables SCA (Only available for Salesforce not for Vlocity Deployments),\
              SCA will run before it goes to the Approver. If it fails, the deployment gets automatically rejected.
           6. If SCA passes, the deployment will go for approval. An email will be sent to the Approver.
        2.  Once the Approver clicks on Approve → It is Auto-deployed. Users and approvers are notified via email.\
            Pending L1 Approval<br>

            <figure><img src="../../../../.gitbook/assets/image (2548).png" alt=""><figcaption></figcaption></figure>

            Email to Approver\
            ![](<../../../../.gitbook/assets/image (2552).png>)<br>

        Pending L2 Approval

        <figure><img src="../../../../.gitbook/assets/image (2551).png" alt=""><figcaption></figcaption></figure>

        \
        Approver can drop a comment, either Approve or Reject, so the user can review the comments in the comments screen.

    <figure><img src="../../../../.gitbook/assets/image (2550).png" alt=""><figcaption></figcaption></figure>

    1. Once the Approver clicks on Reject, the → Approver should reject with comments. Users and approvers are notified via email.
    2. The user can go to the rejected deployment and see the approver’s comments.
    3. The user will only have the option to select/reselect from the redeploy/promote screen, not the metadata changes.
    4. Once that is done, the User can reinitiate the deployment.
    5.  Deployment would again follow the L1 and L2 approval process.

        \
        **Assumptions/Conditions**

        * The approval process for the deployment feature is activated based on a feature flag.
        * This process applies only to custom deployments. For Salesforce deployments, the user and the approver can view the SCA report and access the **Redeploy** option. However, these options are unavailable for Vlocity deployments, as Vlocity does not support them.
        * Approvers must have access to both the Deployments and CI Jobs modules to approve any deployment.
        * If a deployment is awaiting approval and the Admin deletes the Salesforce Org associated with the approval setup, any pending deployment approvals will be automatically rejected.
        * Additionally, if a deployment remains in a pending approval state for more than three days, it will be automatically rejected.
        * Self-approval won't be possible even if you are an admin.
9. **Deployment Add-ons:**
   * **`Promotion:`** Downloads the metadata components in your local system. The file is in ZIP format.
   * **`Redeploy/Promote:`** This option allows you to redeploy the components into the same destination environment with the changes made or promote the same label into a different destination environment. This feature enables users to either redeploy the components to the same destination environment with the applied changes or promote the same label to a different destination environment. Notably, users now have visibility into all previously selected checkboxes and dropdowns from the previous iteration. This enhancement aims to streamline the process by eliminating the need for users to reselect options, enabling them to directly click on the redeploy option. Additionally, users have the flexibility to edit the checkboxes as needed.
   * **`Rollback:`** Rollbacks revert a deployment to a previous revision.
   * **`Abort:`** Cancels a running or stuck deployment process.
   * **`View Graph:`** View Graph gives the graphical representation of the metadata members included in the deployment package.
   * **`SCA Report:`**&#x53;tatic Code Analysis is usually performed as part of a Code Review and is carried out at the Implementation phase of a Security Development Lifecycle (SDL). Static Analysis tools such as PMD and Checkmarx continuously detect and report on dataflow problems, software defects, language implementation errors, inconsistencies, dangerous usage, coding standard violations, and security vulnerabilities.
   * **`Test Results:`** View the Apex test result that you have configured during the deployment.
   * **`Deployed Issues:`** Any issues found during deployment can be seen here.
   * **`Quick Deploy:`** With Quick Deploy, the components validated successfully for the target environment within the last **96 hours** can be deployed quickly.

**Note:** If the Quick Deploy button is grayed out after successful validation, the issue is that there are invalid characters in the metadata file. To fix this issue, please follow these steps:

* **Access Deployment Logs** by navigating to the Deployment History section. Select the specific deployment label where the Quick Deploy button is missing. Review the deployment logs for any errors or warnings related to special characters.
* **Check Deployment Metadata** to identify the files or metadata containing special characters. The common special characters include: +, &, <, >, ", ', etc. Note the specific characters and their locations in the metadata.
* **Re-run Deployment** after you make necessary adjustments to the deployment files to ensure special characters are correctly encoded. Re-run the deployment process with the modified files. The Quick Deploy button should not be grayed out.
* **Escalate if Unresolved**, if the issue persists, escalate to AutoRABIT support for further assistance and provide detailed logs and steps taken to resolve the issue.

9. **Metadata Components Details:**
   * **`Components:`** This report displays the components successfully deployed into the target sandbox. Here you can download the deployed/deployable components in XML format. To do so, click on the **`Download`** button.
   * **`Failed Components:`** This report displays the components that have not been deployed into the target sandbox.
   * **`Deleted Components:`** When pre-destructive or post-destructive changes are selected during deployment initiation, the deleted components are displayed here.
   * **`Apex Test Success:`** This report displays the Apex test components that have successfully passed unit testing.
   * **`Apex Test Failures:`** This report displays the Apex test components that have failed.
   * **`Code Coverage Warning:`** This report shows the components in which the minimum code coverage has not been achieved (Salesforce recommends 75% of code coverage).
   * **`Deployment Notes:`** Specify the reason for the deployment and what has changed across your Salesforce Org.
   * **`Audit Log`**: The **`Audit Log`** lists the user's changes made during the deployment timestamp (based on the start time and end time of Deployment). Refer to the **`Audit Log`** section.

#### Audit Log <a href="#audit-log" id="audit-log"></a>

A new section called the **`Audit Log`** has been added under the **`Deployment Information`** tab.

The audit log lists the user's changes made during the deployment timestamp (based on the start time and end time of deployment).

<figure><img src="/broken/files/zUSc5pEtFyEBIfOFjugq" alt=""><figcaption></figcaption></figure>

Here is the list of changes that Audit Trail tracks:

**Administration**

* Company information, default settings like language or locale, and company messages
* Multiple currencies
* Users, portal users, roles, permission sets, and profiles
* Email addresses for any user
* Deleting email attachments sent as links
* Email footers, including creating, editing, or deleting
* Email deliverability settings
* Divisions, including creating, editing, transferring, and changing users’ default division
* Certificates, adding or deleting
* Domain names
* Enabling or disabling Salesforce as an identity provider

**Profiles**

* Permission for a standard or custom profile changed
* General or admin permission changed
* FLS changed on the profile
* Entity permission for a standard or custom profile changed
* Profile Page Layout changed
* Tab set on a standard or custom profile changed
* User tab set override changed
* User tab set customization override changed for standard or custom profiles
* Tab set visibility changed for a standard or custom profile
* Tab set visibility modified
* Default tab set modified
* Custom App default changed on standard or custom profiles
* Profile renamed, cloned, or deleted
* Profile description changed
* Standard or custom profile cloned
* Console setting or layout changed
* View, or modify all data enabled for this profile
* Login hours for the profile modified
* Client settings for the profile modified
* Record type added to or removed from the profile
* Default record type modified
* Default person account record type modified
* Default business account record type modified
* Single sign-on enabled or disabled for this profile

**Permission Sets/Groups**

* Permission set (or group) created, cloned, or deleted
* Permission set created or cloned without a license
* Developer name, label, or description of a permission set changed
* Session activation changed by admin
* Permission in a permission set enabled or disabled by the admin
* FLS for an object in the permission set changed by the admin
* Permission set from a user assigned or unassigned by the admin
* Tab settings in permission set changed by admin
* Permission set group assigned or removed for a user
* Permission set group re-calculated

**Customizations**

* User interface settings like collapsible sections, Quick Create, hover details, or related list hover links
* Page layout, action layout, and search layouts
* Compact layouts
* Salesforce app navigation menu
* Inline edits
* Custom fields and field-level security, including formulas, picklist values, and field attributes like the auto-number field format, field manageability, or masking of encrypted fields
* Lead settings, lead assignment rules, and lead queues
* Activity settings
* Support settings, business hours, case assignment and escalation rules, and case queues
* Requests to Salesforce Customer Support
* Tab names, including tabs that you reset to the original tab name
* Custom apps (including Salesforce console apps), custom objects, and custom tabs
* Contract settings
* Forecast settings
* Email-to-Case or On-Demand Email-to-Case, enabling or disabling
* Custom buttons, links, and s-controls, including standard button overrides
* Drag-and-drop scheduling, enabling or disabling
* Similar opportunities, enabling, disabling, or customizing
* Quotes, enabling or disabling
* Data category groups, data categories, and category-group assignments to objects
* Article types Category groups and categories
* Salesforce Knowledge settings
* Ideas settings
* Answers settings
* Field tracking in feeds
* Campaign influence settings
* Critical updates, activating or deactivating
* Chatter email notifications, enabling or disabling
* Chatter new user creation settings for invitations and email domains, enabling or disabling
* Validation rules

**Security and Sharing**

* Public groups, sharing rules, and org-wide sharing, including the Grant Access Using Hierarchies option
* Password policies
* Password resets
* Session settings, like session timeout (excluding Session time-out after and Session security level required at login profile settings)
* Delegated administration groups and the items delegated admins can manage (setup changes made by delegated administrators are also tracked)
* Lightning Login, enabling or disabling, enrollments, and cancellations
* How many records a user permanently delete from their recycle bin and from the org recycle bin
* SAML (Security Assertion Markup Language) configuration settings
* Salesforce certificates
* Identity providers, enabling or disabling
* Named credentials Service providers
* Shield Platform Encryption setup
* Event Manager
* Transaction Security
* Some connected app policy and setting updates

**Data Management**

* Using mass delete, including when a mass delete exceeds the user’s Recycle Bin limit on deleted records
* Data export requests
* Mass transfer use
* Reporting snapshots, including defining, deleting, or changing the source report or target object on a reporting snapshot
* Use of the Data Import Wizard
* Sandbox deletions

**Development**

* Apex classes and triggers
* Visualforce pages, custom components, and static resources
* Lightning pages
* Action link templates
* Custom settings
* Custom metadata types and records
* Remote access definitions
* Salesforce Sites settings

**Various Setups**

* API usage metering notification, creating
* Territories
* Process automation settings
* Approval processes
* Workflow actions, creating or deleting
* Flows
* Packages from Salesforce AppExchange that you installed or uninstalled
* Notification delivery settings for custom and standard notification types

**Using the Application**

* Account team and opportunity team selling settings
* Activating Google Apps services
* Mobile configuration settings, including data sets, mobile views, and excluded fields
* Users with the “Manage External Users” permission logging in to the partner portal as partner users
* Users with the “Manage Customer Users” permission logging into the Salesforce Customer Portal as Customer Portal users
* Partner portal accounts, enabling or disabling
* Salesforce Customer Portal accounts, disabling
* Salesforce Customer Portal, enabling or disabling
* Creating multiple Customer Portals
* Entitlement processes and entitlement templates, changing or creating
* Self-registration for a Salesforce Customer Portal, enabling or disabling
* Customer Portal or partner portal users, enabling or disabling
