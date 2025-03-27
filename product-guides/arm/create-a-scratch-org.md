# Create a Scratch Org

### What is Scratch Org? <a href="#what-is-scratch-org" id="what-is-scratch-org"></a>

Salesforce DX can be enabled for any Salesforce instance known as Developer Hub. One Developer Hub can have multiple Scratch Orgs. Scratch Orgs are temporary Salesforce org which can be created quickly and metadata can be deployed from source code management (SCM). This kind of Orgs can be used by developers to perform quick proof of concept or build and test packages. A developer can create as many numbers as Scratch Orgs and delete them for each specific Salesforce DX project.

### Requirements <a href="#requirements" id="requirements"></a>

Module registered in AutoRABIT ([LEARN MORE](create-a-module.md))

### Creating a new Scratch Org <a href="#creating-a-new-scratch-org" id="creating-a-new-scratch-org"></a>

To create a new Scratch Org, perform the below steps:

1. Hover your mouse over the [Salesforce DX](https://www.autorabit.com/blog/the-basics-of-salesforce-dx/) module and select the option: **Scratch Org Management.**

<figure><img src="../../.gitbook/assets/image (1417).png" alt="" width="203"><figcaption></figcaption></figure>

2. Click on **Create Scratch Org**.

<figure><img src="../../.gitbook/assets/image (1418).png" alt=""><figcaption></figcaption></figure>

#### Scratch Org Details <a href="#scratch-org-details" id="scratch-org-details"></a>

In this section, you would be filling your scratch org details.

{% hint style="info" %}
**Note:** When configuring your Scratch Org, be aware that certain objects may require associated profiles and dependency data. This requirement isn't always explicit, so it's important to review your objects and their dependencies thoroughly to ensure a seamless setup.
{% endhint %}

Select the **Dev HUB** name. This is the main [Salesforce org](getting-started/salesforce-org-management.md) that you and your team use to create and manage your scratch org. Also, give a name to the **Scratch Org**.

<figure><img src="../../.gitbook/assets/image (1419).png" alt=""><figcaption></figcaption></figure>

There are three ways of filling in the details for your scratch org:

1. **Download the ScratchOrg DefinitionTemplate** into your local machine, fill it, and upload them. The template will be created based on the information available in the file chosen

<figure><img src="../../.gitbook/assets/image (1420).png" alt=""><figcaption></figcaption></figure>

2. **Let AutoRABIT create the Scratch Org with Default Values**. This is done when you do not upload any definition file or fill in the scratch org fields manually. On navigating to the next section, a popup notification appears which asks for your confirmation to proceed further.

<figure><img src="../../.gitbook/assets/image (1421).png" alt=""><figcaption></figcaption></figure>

3.  Fill in the Scratch Org fields **Manually**. For manually, you need to fill in the below details:

    * Select the **Input Details** section.
    * On the pop-up screen, enter a **username** to the scratch org. If the field is left blank, the username gets auto-generated. Kindly note that the username entered should be in the email address format.
    * Give a small description of the scratch org in the **Description** field.&#x20;
    * Enter the **Duration Days** till the scratch org will be in the active state.
    * Fill in the **Organization** for which the scratch org will be used.
    * Select the **Features** and **Preferences Enable/Disable** associated with its Scratch Org. For multiple selections, hold down the **CTRL** key and click on it.
    * Fill in the **Admin Email**, **Country**, and the **Language** as desired.
    * Select the **Edition** i.e., Developer, Group, Enterprise, etc., from the drop-down box. This field is also optional.
    * Enter the **Wait Time (Minutes)** to create the scratch org. The default wait time is 6 minutes, but you can set this value from 1 minute to a maximum of 15 minutes.
    * Click **NEXT**.

    <figure><img src="../../.gitbook/assets/image (1422).png" alt=""><figcaption></figcaption></figure>

#### Select Module and Load Data <a href="#select-module-and-load-data" id="select-module-and-load-data"></a>

This section is all about choosing the right deployment source; it can be from your Salesforce Org, Version Control, or from an existing module that you have created in AutoRABIT. To create a new module, please follow the steps mentioned [HERE](create-a-module.md).

<figure><img src="../../.gitbook/assets/image (1423).png" alt=""><figcaption></figcaption></figure>

**Deployment via Salesforce Org**

1. Choose **Deployment From** as **Salesforce Org**.
2. The **Metadata Types** field allows you to deploy either the entire Salesforce Org or Full Profiles or Permission Sets.
   * **Full Profiles** will fetch all the profiles available in the selected Salesforce Org
   * **Full Permission Sets** will fetch all the permission sets from your selected Salesforce Org
   * **All** will fetch all the metadata types available in your Salesforce org
3. Select your **Source Org**.
4. Choose the **Deployment Method**:
   * **Selective Deployment**: Selective deployment will allow you to choose and deploy the selected metadata types from your Salesforce org
   * **Full Deployment:** All the metadata types will be deployed
5. Click **Retrieve Metadata**. This retrieves a list of all metadata types from your selected source org, allowing you to choose which members to be included in the deployment. If necessary, you can use the **search** filter to find your metadata types faster.

<figure><img src="../../.gitbook/assets/image (1424).png" alt=""><figcaption></figcaption></figure>

6. Click **Proceed > Proceed** to take you to the next screen where you can apply filters for your deployment being initiated.

<figure><img src="../../.gitbook/assets/image (1425).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1426).png" alt=""><figcaption></figcaption></figure>

7. Different **Deployment Filters**:
   * **Ignore warnings:** When this filter is checked, metadata types that trigger warnings during the retrieval process will not cause the deployment to fail, and AutoRABIT will deploy all other metadata types as possible.
   * **Validate only:** Checking this option will validate and save the deployment label without actually executing the deployment. The label can then be used later for a Quick Deploy if the target org is a production environment against which the validation was done.
   * **Take backup:** This option creates a backup of the original state of the metadata to which you can revert if the deployment fails or has other functional issues.
   * **Ignore missing visibility settings (profiles):** With this option, differences in visibility settings between the source and destination orgs will not cause the deployment to fail. AutoRABIT will compare the source and destination orgs and keep only the settings that are common between both orgs.
   * **Remove Login IP Ranges:** This option will remove IP ranges from your profile while deploying.
   * **Remove System and User Permissions:** Remove the user's permission from your profile while deploying.
   * **Do not include Destructive members:** Select this checkbox if you have configured certain metadata types to skip while deploying. You can configure such metadata types under the **Admin > Salesforce Org Management** page.
   * **Do not include Skip members:** Select this checkbox if you have configured certain metadata types to skip while deploying under the [My Account](arm-administration/user-management/manage-users-account-settings.md) page.
   * **Ignore installed components:** When selected, AutoRABIT will scan for the components that are deployed, and if there are any managed package components located in the target org, these components will be excluded from the metadata.zip files while the remaining components will get deployed.
   * **Fetch Wavexmd components (applicable only if WaveDashboard's metadata type is chosen for deployment):** Upon selection, this checkbox will allow you to select the respective wavexmd files belonging to the wave dashboard metadata type and deploy them via selective deployment to another Salesforce Org. This checkbox will be hidden if the 'WaveDashboard' metadata type or its corresponding members are not picked.

{% hint style="info" %}
**Important Note**: **Standard fields** are not supported for **Ignore Missing Visible Settings**.
{% endhint %}

8. Choose the **Static Code Analysis** tool to detect bugs, code smells, and security vulnerabilities before the deployment begins.
9. If you have created the **SEARCH** and **SUBSTITUTE** rules to define custom find and substitute rules that AutoRABIT applies whenever you commit and deploy files from one Sandbox to another Sandbox, one Sandbox to Version Control, or vice-versa, such rule can be found here.
10. Under **Deployment Notes**, specify the reason for the deployment and what has changed across your Salesforce Org.
11. Click **Next**. The user will be redirected to the **Deployment Summary** page where he can view the components one final time before getting deployed.&#x20;

<figure><img src="../../.gitbook/assets/image (1427).png" alt=""><figcaption></figcaption></figure>

**Deployment via Version Control**&#x20;

1. Choose **Deployment From** as Version Control.
2. In the **Version Control**, **Repository**, and **Branch** fields, choose the appropriate sources.
3. Select the **Metadata Types**.
4. Choose the **Deployment Method** and click on the **Retrieve Metadata** button. The remaining steps are already discussed in the previous section (**Steps 5-11**).

<figure><img src="../../.gitbook/assets/image (1428).png" alt=""><figcaption></figcaption></figure>

**Deployment via Module**

This section is all about deployment using the module available in your AutoRABIT application.

Different options get auto-populated based on the Module selected:

1. **Load Dataset from \<Module Name> for the Scratch org:** This option will reflect only if the user has selected **Create Data set from \<Source Org> for the module** under the **Publish** section at the time of creating a module. This option upon selection will add the dataset available in the selected module to the scratch org
2. **Include all the dependent packages:** All the dependent packages associated with the selected Module will get fetched. The user can either include all the dependency packages to the scratch org by selecting the checkbox as shown below or not include it.

<figure><img src="../../.gitbook/assets/image (1429).png" alt=""><figcaption></figcaption></figure>

Click **Show Members** to view the list of metadata types available in the selected module.

<figure><img src="../../.gitbook/assets/image (1430).png" alt=""><figcaption></figcaption></figure>

Click **Next** to go to the next section i.e., **Assign Branch and ALM**.

#### Assign Branch and ALM <a href="#assign-branch-and-alm" id="assign-branch-and-alm"></a>

**Assign Branch**

1. Select the **Version Control** type, **Repository**, and its respective **Branch**.
2. **Create Branch** callout button is useful in creating a fresh branch assigning to the Scratch Org being created.

<figure><img src="../../.gitbook/assets/image (1431).png" alt=""><figcaption></figcaption></figure>

**Assign User Story**

Select the ALM work item to update the ALM work item status. Once the changes are committed to the version control system, the status of the ALM work item is updated and reflected in your ALM system.

1. Select the **ALM Type**. Currently, AutoRABIT supports ALM types like JIRA, IBMRTC, Version One, CA Rally, and Azure DevOps.
2. Select the **ALM Label**.
3. Select the **Project** and the **Sprint** for which the commit is planned.
4. Select the **Work Item**.
5. Click **Next**.

<figure><img src="../../.gitbook/assets/image (1432).png" alt=""><figcaption></figcaption></figure>

#### Manage Permissions <a href="#manage-permissions" id="manage-permissions"></a>

In this section assign the module permission to your users. An email notification gets triggered to each user with scratch org details.

<figure><img src="../../.gitbook/assets/image (1433).png" alt=""><figcaption></figcaption></figure>

You will be redirected to the **Scratch Org Management** homepage which will show you the progress of the scratch org recently created.

<figure><img src="../../.gitbook/assets/image (1434).png" alt=""><figcaption></figcaption></figure>

### Additional Options on 'Scratch Org Management' screen <a href="#additional-options-on-scratch-org-management-screen" id="additional-options-on-scratch-org-management-screen"></a>

<figure><img src="../../.gitbook/assets/image (1435).png" alt=""><figcaption></figcaption></figure>

1. **Scratch Org Summary:** Click on the Scratch Org link to view the detailed summary of your Scratch Org

<figure><img src="../../.gitbook/assets/image (1436).png" alt="" width="563"><figcaption></figcaption></figure>

2. **View Log**: View the log information of the Scratch Org
3. **Deployment Status and Report:** Status of the deployment i.e., success, failure, succeeded partial,  or is timed-out along with the Deployment report
4. **Load Data:** This section gives info about sample data added to the scratch org or not.
5. **Scratch Org Status:** Scratch org status i.e., inactive or inactive state.
6. **Manage:**
   * **Launch Scratch Org:** Launch the Scratch Org in the new tab based on the URL instance. Make sure the pop-up is enabled in your browser which may sometimes strict the opening of another tab while using our application.
   * **Manage Scratch org permissions:** Manage the module permission that is assigned to the users. An email notification gets triggered to each user with scratch org details when modified.
7. **Actions:**
   * **Delete a Scratch Org:** Deletes a Scratch Org. This process cannot be undone!!
   * **Edit ALM and Branch:** Modify or update the ALM and Version Control Repository, Branch details.
