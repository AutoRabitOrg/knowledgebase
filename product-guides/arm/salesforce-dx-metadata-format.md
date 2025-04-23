# Salesforce DX Metadata Format

### Overview <a href="#overview" id="overview"></a>

For AutoRABIT to detect your repository as being in DX format, it looks for an **sfdx-project.json** file in your local directory.

<figure><img src="../../.gitbook/assets/image (1394).png" alt=""><figcaption></figcaption></figure>

AutoRABIT scans for the **sfdx-project.json** in your local directory which is the configuration file. Here you will find an array named '**packageDirectories'**; this setting is called the **Package Directory** which contains the default directory of the source code/metadata where source code is pushed and pulled to and from scratch org.&#x20;

<figure><img src="../../.gitbook/assets/image (1395).png" alt=""><figcaption></figcaption></figure>

For the SFDX repository created outside and registered later with AutoRABIT, the source folder has to be declared in an **sfdx-project.json** file under the array named **packageDirectories**. This will allow you to pick the source folder that you have declared in the **sfdx-project.json** during commit/ CI Job operation or while creating unlocked packages. If you are in trouble finding the declared source folder yet, press the **Refresh** button to re-scan the Package Directories for the new source folder path.

ARM does not currently support custom SFDX directory structures. As per the standard SFDX directory structure, we follow and accept only the `<force-app*>/main/default/*` structure. This is the default structure created when we run the project generate command, as follows:

<figure><img src="../../.gitbook/assets/image (1396).png" alt=""><figcaption></figcaption></figure>

There can be multiple package directories, and all of them should follow the same structure. The `sfdx-project.json` file is used to identify the list of package directories, and all ARM functionalities work with the `<package-directory>/main/default` structure.

### Places to find the Source SFDX Folder Path <a href="#places-to-find-the-source-sfdx-folder-path" id="places-to-find-the-source-sfdx-folder-path"></a>

#### EZ-Commit screen <a href="#ezcommit-screen" id="ezcommit-screen"></a>

While committing metadata components from a Salesforce org to an SFDX repository/branch, you need to select the source folder under Package Directory drop-down field.

<figure><img src="../../.gitbook/assets/image (1397).png" alt=""><figcaption></figcaption></figure>

#### During CI Job <a href="#during-ci-job" id="during-ci-job"></a>

While deploying the SFDX source from a [Version Control](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) branch to a [Salesforce Org](registration/salesforce-org/salesforce-org-management.md), you need to choose the source folder for your SFDX repository.

<figure><img src="../../.gitbook/assets/image (1398).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1399).png" alt=""><figcaption></figcaption></figure>

#### During Branching Baseline operation <a href="#during-branching-baseline-operation" id="during-branching-baseline-operation"></a>

While retrieving and committing all the metadata components from a [Salesforce org](arm-administration/registration/salesforce-org/) to SDFX Branch, you need to select the source folder under the **Package Directory** field.

<figure><img src="../../.gitbook/assets/image (1400).png" alt=""><figcaption></figcaption></figure>

#### While creating Unlocked/Managed Packages <a href="#while-creating-unlockedmanaged-packages" id="while-creating-unlockedmanaged-packages"></a>

In the process of creating unlocked packages via [AutoRABIT](https://www.autorabit.com/), you need to select the source folder under the **Package Directory** field.

<figure><img src="../../.gitbook/assets/image (1401).png" alt=""><figcaption></figcaption></figure>

#### While creating a new Commit Label <a href="#while-creating-a-new-commit-label" id="while-creating-a-new-commit-label"></a>

While creating commit labels for SFDX repositories, you need to select the source folder under the **Package Directory** field.

<figure><img src="../../.gitbook/assets/image (1402).png" alt=""><figcaption></figcaption></figure>

#### During Release Label creation <a href="#during-release-label-creation" id="during-release-label-creation"></a>

During release label creation for [SFDX](arm-features/automation-and-ci/create-a-new-ci-job/deploy-from-sfdx-branch-to-a-salesforce-org.md) repositories, you need to select the source folder under the **Package Directory** field.

<figure><img src="../../.gitbook/assets/image (1403).png" alt=""><figcaption></figcaption></figure>
