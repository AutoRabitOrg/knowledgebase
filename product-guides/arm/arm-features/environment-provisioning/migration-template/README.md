# Migration Template

### List of Migration Templates supported <a href="#list-of-migration-templates-supported" id="list-of-migration-templates-supported"></a>

1. Enable History Tracking on Objects
2. Disable History Tracking on Objects
3. Enable History Tracking on Custom Fields
4. Disable History Tracking on Custom Fields
5. Run Destructive Changes
6. Execute Anonymous Apex
7. Enable Validation Rules
8. Disable Validation Rules
9. Enable Workflow Rules
10. Disable Workflow Rules
11. Enable Flows
12. Disable Flows
13. Enable Apex Triggers
14. Disable Apex Triggers
15. Migrate Custom Setting Data from one org to another org

### How to create a migration template <a href="#how-to-create-a-migration-template" id="how-to-create-a-migration-template"></a>

To create a new migration template, please follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. The **Create Migration Template** tab will be auto-selected by default, if not, select it.
5. Give the template a **name** and a **short description** of it.
6. Select the checkboxes for the template types for which you want to create a template. You can create multiple templates at the same time.&#x20;
7. You must upload the **package manifest XML** file for each template type that you have selected. Failure to insert the correct XML file will result in the migration template being created unsuccessfully.
8. Click **Save**.
9. You can find your recently created template on the **Environment Provisioning History** page.
10. The next step is to run the template on your destination Salesforce org.
11. Look for your template on the **Environment Provisioning History** screen and click on **Run**.
12. Select your **destination org** from the dropdown and enter the email address(es) to receive an email notification whenever the operation is carried out.
13. Click **Run**.

### View History <a href="#view-history" id="view-history"></a>

The **View History** screen will display the detailed summary report of the template operation being carried out.

The left side screen will display the template name, the template creation date/time stamp, and the Salesforce org where the template was run.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616328277736.png" alt=""><figcaption></figcaption></figure>

Click on the **Log** icon to view the log report on the right side of the page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616328449188.png" alt=""><figcaption></figcaption></figure>

**Result** icon will display the status of the deployment for the template (success or failed), deployed components, deployed components path, and many more.&#x20;

**Re-Run** option allows you to run the template once again.&#x20;

**Info** option allows you to view the input file which you have uploaded in the initial stage for template creation.

#### More Information on Environment Provisioning Screen

The following information will be displayed for each template created on the Environment Provisioning History screen.

<figure><img src="../../../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

1. **Template Name:** Name of the template along with the template created date/time
2. **Template Type:** Template type, i.e., migration template or an unsupported metadata template
3. **Last Modified By:** User detail who last modified this template&#x20;
4. **Salesforce Org:** Destination org where the template was run
5. **Last Run:** The date/time stamp the template was last run
6. **Status:** Template status, i.e., successfully run or failed
7. **Run:** Run the template
8. **Delete:** Delete the template
9. **Edit:** Edit the template fields
10. **Share:** Click on the share button; if you want to share the template with others, users in the org will be able to access it.
11. **Revoke**: Click on the revoke button; if you don't want to share the template with others, users in the org will not be able to access it.
12. **View History:** Detailed info on the template, such as the last modified date/time of the template, log details, etc.

<figure><img src="../../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
