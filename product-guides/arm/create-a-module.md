# Create a Module

### Introduction <a href="#introduction" id="introduction"></a>

Modularization lets you break your org’s customizations into **unlocked packages**.  
Each package becomes the single source of truth for the metadata it contains, and you can update any environment—scratch org, sandbox, or production—by installing the latest version.

Whenever you change the package’s [metadata](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/), you simply create a **new package version** and install it wherever it’s needed.

---

### Creating a Module <a href="#creating-a-module" id="creating-a-module"></a>

Follow these steps to create a module in AutoRABIT:

1. **Open Modularization**  
   Hover over the [**SFDX**](salesforce-dx-metadata-format.md) tile and click **Modularization**.

   <figure><img src="../../.gitbook/assets/image (1437).png" alt="SFDX → Modularization" width="209"><figcaption></figcaption></figure>

2. **Start a new module**  
   Click **Create Module**.

   <figure><img src="../../.gitbook/assets/image (1438).png" alt="Create Module button"><figcaption></figcaption></figure>

3. **Name and source**  
   * Enter a **Module Name**.  
   * Choose the **Source Org** that contains the metadata.  
   Click **Next**.

   <figure><img src="../../.gitbook/assets/image (1439).png" alt="Name and source org"><figcaption></figcaption></figure>

4. **Select metadata**  
   Choose the **Metadata Types** (and their members) to include. Use the **Search Filter** to locate items quickly.

   <figure><img src="../../.gitbook/assets/image (1440).png" alt="Select metadata"><figcaption></figcaption></figure>

   {% hint style="info" %}
   **Important:** Avoid adding metadata types that already belong to another module in the same branch.
   {% endhint %}

5. **Review selection**  
   Click **Selected Members** to view a summary of chosen metadata, then click **OK**.

   <figure><img src="../../.gitbook/assets/image (1441).png" alt="Selected members summary" width="563"><figcaption></figcaption></figure>

6. Click **Next** to open the **Validate and Push** screen.

   <figure><img src="../../.gitbook/assets/image (1442).png" alt="Validate and Push"><figcaption></figcaption></figure>

7. **Validate dependencies**  
   Compare the Source Org with another [Salesforce Org](arm-administration/registration/salesforce-org/) to ensure no dependent components are omitted.

   <figure><img src="../../.gitbook/assets/image (1443).png" alt="Validation options"><figcaption></figcaption></figure>

8. **Additional options**

   * **Ignore Missing Visibility Settings, If Package Contains Profiles Or PermissionSets** – visible only when Profiles/PermissionSets are included; deploys delta changes.  
   * **Ignore Installed Components** – skips managed-package components already present in the target org.

   {% hint style="info" %}
   **Note:** *Standard fields* are **not** supported for **Ignore Missing Visibility Settings**.
   {% endhint %}

9. **Publish To** – configure commit and package settings.

   * **Repository / Branch** – pick where to commit the metadata (use **+** to create a branch).  
   * **Development Hub (Dev Hub)** – select the Dev Hub that will own the unlocked package.  
   * **Email Address** – recipient of the module-creation email.  
   * **Include metadata dependencies** – automatically pull in required dependent members.

   <figure><img src="../../.gitbook/assets/image (1444).png" alt="Publish To settings"><figcaption></figcaption></figure>

   {% hint style="info" %}
   **Tip:** To fetch dependency data, the Dependency API must be enabled. See Salesforce docs [here](https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_metadatacomponentdependency.htm).
   {% endhint %}

10. **Package Dependencies**  
    If the Dev Hub already owns related packages with at least one successful version, they appear here.

    {% hint style="info" %}
    **Conditions:**  
    * The dependent package was created in AutoRABIT **and**  
    * It has at least one successful version.
    {% endhint %}

11. **Add / arrange dependencies**

    * Select packages in **Available Packages** and use the ![](<../../.gitbook/assets/image (1445).png>) / ![](<../../.gitbook/assets/image (1446).png>) icons to add or remove them.  
    * Use ![](<../../.gitbook/assets/image (1447).png>) / ![](<../../.gitbook/assets/image (1448).png>) to reorder; the top package deploys first.

    <figure><img src="../../.gitbook/assets/image (1449).png" alt="Package dependencies"><figcaption></figcaption></figure>

12. **Create the module**  
    Click **Create Module**. You’ll return to the **Modularization** home page, where you can monitor progress.

13. **Module list columns**

    * **Module Name** – name you assigned  
    * **Source Org** – org where the module originated  
    * **Repository / Branch** – VCS location for commits  
    * **Package URL** – link for package installation (see *Deployment via Unlocked Packages*)  
    * **Validation Status** – pre-validation result plus log  
    * **Status** – creation progress (Success, Failed, or In Progress)

    <figure><img src="../../.gitbook/assets/image (1450).png" alt="Module list"><figcaption></figcaption></figure>

**Sample email notification**

<figure><img src="../../.gitbook/assets/image (1451).png" alt="Email example" width="483"><figcaption></figcaption></figure>

---

### Additional Features <a href="#additional-features" id="additional-features"></a>

<figure><img src="../../.gitbook/assets/image (1452).png" alt="Additional features"><figcaption></figcaption></figure>

1. **Actions**  
   * **Edit Module** – update module details  
   * **Log Details** – view execution logs  
   * **Delete Module** – permanently remove a module *(irreversible)*

2. **Info**  
   * **Module Summary Info** – see dependency details for selected metadata  
   * **Module Info** – view timestamps and other metadata about the module
