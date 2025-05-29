# Salesforce DX Metadata Format

Modern DevOps workflows rely on **Salesforce DX (SFDX)** to treat org configuration like code.  
Instead of a monolithic ZIP, your metadata lives in a **source-tracked directory structure** that maps cleanly to Git and CI/CD pipelines. AutoRABIT embraces this model and adds automation on top—but it needs to know which folder(s) contain your DX-formatted source.

---

### Overview <a href="#overview" id="overview"></a>

AutoRABIT identifies an SFDX repository by locating an **`sfdx-project.json`** file in the root:

<figure><img src="../../.gitbook/assets/image (1394).png" alt="Root containing sfdx-project.json"></figure>

This file includes a **`packageDirectories`** array. Each entry defines a **Package Directory**—the root of your metadata for pushes to and pulls from scratch orgs.

<figure><img src="../../.gitbook/assets/image (1395).png" alt="packageDirectories inside sfdx-project.json"></figure>

If you register an existing DX repo with AutoRABIT, ensure every source folder is listed under **`packageDirectories`**. Click **Refresh** in the UI if the directories don’t appear immediately.

> **Supported layout**  
> AutoRABIT currently supports the **standard** DX structure only:  
> `<package-directory>/main/default/*`  
> (Created automatically by `sfdx force:project:create`.)

<figure><img src="../../.gitbook/assets/image (1396).png" alt="Standard SFDX directory tree"></figure>

You may declare multiple package directories, but **each** must follow the same `/main/default` sub-tree.

---

### Places to Select the Source SFDX Folder <a href="#places-to-find-the-source-sfdx-folder-path" id="places-to-find-the-source-sfdx-folder-path"></a>

#### EZ-Commit Screen <a href="#ezcommit-screen" id="ezcommit-screen"></a>

Choose **Package Directory** when committing metadata from a Salesforce org to an SFDX branch.

<figure><img src="../../.gitbook/assets/image (1397).png" alt="Package Directory dropdown in EZ-Commit"></figure>

#### During a CI Job <a href="#during-ci-job" id="during-ci-job"></a>

Select the folder while deploying SFDX source from Version Control to a Salesforce org.

<figure><img src="../../.gitbook/assets/image (1398).png" alt="Package Directory dropdown in CI Job"></figure>

<figure><img src="../../.gitbook/assets/image (1399).png" alt="CI Job configuration with Package Directory"></figure>

#### Branching Baseline Operation <a href="#during-branching-baseline-operation" id="during-branching-baseline-operation"></a>

When committing all metadata from a Salesforce org into an SFDX branch, pick the directory here.

<figure><img src="../../.gitbook/assets/image (1400).png" alt="Package Directory during Branching Baseline"></figure>

#### Creating Unlocked/Managed Packages <a href="#while-creating-unlockedmanaged-packages" id="while-creating-unlockedmanaged-packages"></a>

Specify **Package Directory** while defining an unlocked or managed package.

<figure><img src="../../.gitbook/assets/image (1401).png" alt="Package Directory dropdown in package creation"></figure>

#### New Commit Labels <a href="#while-creating-a-new-commit-label" id="while-creating-a-new-commit-label"></a>

Commit labels for DX repos also require the source folder.

<figure><img src="../../.gitbook/assets/image (1402).png" alt="Package Directory selection for Commit Label"></figure>

#### Release Label Creation <a href="#during-release-label-creation" id="during-release-label-creation"></a>

Choose the directory again when generating a release label.

<figure><img src="../../.gitbook/assets/image (1403).png" alt="Package Directory selection for Release Label"></figure>
