# Create a Module

### Introduction <a href="#introduction" id="introduction"></a>

Modularization is all about segmenting your org and your customization into unlocked packages. The package will become the ultimate source of truth for whatever it contains, and you’ll bring different environments up to speed by installing your package(s) into those orgs. Those environments can be scratch orgs, sandboxes, and, of course, production.&#x20;

As you make updates to the [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) in your unlocked package, you create a new version of your package. Then you can install the new version in whatever environments you want to update.

### Creating a Module <a href="#creating-a-module" id="creating-a-module"></a>

To create a module in AutoRABIT, you need to perform the steps as mentioned below:

1. Hover your mouse over the [**SFDX**](salesforce-dx-metadata-format.md) tile and choose the option: **Modularization.**

<figure><img src="../../.gitbook/assets/image (1437).png" alt="" width="209"><figcaption></figcaption></figure>

2. Click on **Create Module**.

<figure><img src="../../.gitbook/assets/image (1438).png" alt=""><figcaption></figcaption></figure>

3. On the next screen, you need to assign a **Name** for the module. Also, select the **Source Org** on which the module will be created. Click **Next**.

<figure><img src="../../.gitbook/assets/image (1439).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, select the **Metadata Types** (along with their respective members ) that will be a part of the module being created. Even, you can use the **Search Filter** to find any specific metadata members quickly.

<figure><img src="../../.gitbook/assets/image (1440).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: The user should ensure not to select/ include such metadata types in a module of a branch if the same metadata types are already available for another module for the same branch.
{% endhint %}

5. Click on the **Selected Members** button to view the summary list of metadata types and their members that are selected. Click **OK**.

<figure><img src="../../.gitbook/assets/image (1441).png" alt="" width="563"><figcaption></figcaption></figure>

6. Click **Next** to proceed to the **Validate and Push** screen.

<figure><img src="../../.gitbook/assets/image (1442).png" alt=""><figcaption></figcaption></figure>

7. The first step is to validate the selected source org with another [Salesforce org](arm-administration/registration/salesforce-org/) to ensure the dependent metadata components are not skipped from the module.

<figure><img src="../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

8. **Additional option:**
   * **Ignore Missing Visibility Settings, If Package Contains Profiles Or PermissionSets:** This option will be visible only if the Source org contains Profile/ PermissionSets metadata types and such metadata types are to be included in the newly created module. This option will only deploy delta changes to the target environment.
   * **Ignore installed components:** When selected, AutoRABIT will scan for the components that are deployed, and if there are any managed package components located in the target org, these components will be excluded from the metadata.zip files while the remaining components are deployed.

{% hint style="info" %}
**Important Note**: **Standard fields** are not supported for **Ignore Missing Visible Settings**.
{% endhint %}

9.  Under the **Publish To** section, do the following:

    * Select the **Repository** and the **Branch** to which the data will get committed. Use the '+' icon to create a new branch where you like to commit the metadata types.
    * Select the **Development Hub (Dev Hub)** for which the unlocked package will be associated.
    * Enter the **Email Address** of the user who will be notified via email for the current operation being performed.
    * **Include metadata dependencies:** Related dependent members of the selected metadata types will be included while creating the module.

    <figure><img src="../../.gitbook/assets/image (1444).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: In order to include the dependent members for your source org metadata types, dependency API should be enabled. For more information about dependency API, click [HERE](https://developer.salesforce.com/docs/atlas.en-us.api\_tooling.meta/api\_tooling/tooling\_api\_objects\_metadatacomponentdependency.htm).&#x20;
{% endhint %}

10. The Dev Hub org can own multiple packages that are created in AutoRABIT. Such dependent packages will get displayed under the **Package Dependencies** section.

{% hint style="info" %}
**Important Note**: Conditions for dependent packages to get fetched:

* The package should be successfully created in AutoRABIT and&#x20;
* The package should contain at least one (1) successful version. &#x20;
{% endhint %}

11. From the **Available Packages** list, select the dependent packages that will be associated with the current module. Use the ![](<../../.gitbook/assets/image (1445).png>)/![](<../../.gitbook/assets/image (1446).png>) button to add/remove the dependent packages to the module and using the![](<../../.gitbook/assets/image (1447).png>)/![](<../../.gitbook/assets/image (1448).png>) button, move the package list up and down. Based on the selection, the top package will be deployed in the beginning and the process continues for the remaining dependent packages.

<figure><img src="../../.gitbook/assets/image (1449).png" alt=""><figcaption></figcaption></figure>

12. Click on **Create Module**. You will be redirected to the **Modularization** homepage which will show you the progress of the module recently created.
13. For each module created, the following information is displayed:

    * **Module Name:** Name of the Module
    * **Source Org:** Source org where the module is created
    * **Repository/Branch:** Version control repository and branch where the metadata and data will be committed
    * **Package URL (auto-generated):** Based on the generated URL and a valid login to a Salesforce org, the user can install the package. Refer to Deployment via Unlocked Packages for more information.
    * **Validation Status:** Pre-validate deployment status i.e., validation is successful or failed along with the pre-validation log report.
    * **Status:** Module status i.e., whether the module is successfully created or failed or is in progress.

    <figure><img src="../../.gitbook/assets/image (1450).png" alt=""><figcaption></figcaption></figure>

**Sample email notification**

<figure><img src="../../.gitbook/assets/image (1451).png" alt="" width="483"><figcaption></figcaption></figure>

### Additional Features <a href="#additional-features" id="additional-features"></a>

<figure><img src="../../.gitbook/assets/image (1452).png" alt=""><figcaption></figcaption></figure>

1. **Actions**:
   * **Edit Module:** Modify or update the detailed feed during the module creation
   * **Log Details:** View the execution log of the current module
   * **Delete a Module:** If you wish to delete a module, you can do so by clicking on the Delete icon. This process cannot be undone!!
2. **Info:**
   * **Module Summary Info:** View the dependencies for the selected members in the Source Org
   * **Module Info:** View the module information such as module created/modified date and time stamp, etc.
