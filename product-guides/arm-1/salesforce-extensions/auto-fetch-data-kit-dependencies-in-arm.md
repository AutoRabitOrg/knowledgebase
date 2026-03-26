# Auto-Fetch Data Kit Dependencies

#### Overview

ARM now enables automatic retrieval of all dependent metadata for a selected Salesforce Data Cloud Data Kit using the connected org credentials. This eliminates the need to manually download the Data Kit package manifest (`package.xml`) from Salesforce and upload it during Commit workflows.

This enhancement reduces manual effort, saves time, and minimizes errors caused by missing or outdated manifest files.

***

#### Use Case

Previously, users had to manually perform the following steps:

* Log in to the source Salesforce org
* Download the package manifest for the Data Kit
* Save the `package.xml` file locally
* Upload it into ARM during Commit

With this enhancement, ARM automatically fetches all dependent members of the selected Data Kit directly from Salesforce, removing the need for manual download and upload.

***

#### Feature Summary

When you select a Data Kit in ARM:

* ARM connects to the Salesforce org using the configured credentials
* ARM fetches all dependent members related to the selected Data Kit
* ARM automatically prepares the manifest within the workflow
* You can proceed with the Commit process without manually uploading `package.xml`

***

### Step-by-Step User Guide

#### Commit a Data Cloud Data Kit Without Manual Manifest Upload

**Step 1: Log in to ARM**\
Sign in to your ARM account using valid credentials.

**Step 2: Open the Commit Workflow**\
Navigate to version control and select where you want to perform the commit.

**Step 3: Select the Source Salesforce Org**\
Choose the connected Salesforce org that contains the required Data Kit.

**Step 4: Select the Retrieval Option**\
In the commit workflow, choose the appropriate option for Data Cloud metadata retrieval, such as:

* Manual
* Auto Draft
* Package Manifest

Select the option that supports Data Kit-based retrieval.

**Step 5: Select the Required Data Kit**\
From the list of available Data Kits, select the Data Kit you want to commit.

**Step 6: Fetch Dependencies Automatically**\
Once the Data Kit is selected, ARM automatically connects to Salesforce and retrieves all dependent metadata associated with that Data Kit.

No manual manifest upload is required.

**Step 7: Review Retrieved Components**\
Review the list of fetched metadata members displayed in the workflow.

**Step 8: Proceed with Commit**\
Continue the commit process as usual.

**Step 9: Confirm Commit Completion**\
After the process finishes, verify that the commit completed successfully and includes the expected Data Cloud metadata.

**Step 10: Use the Commit Revision for Deployment**\
You can use the same commit revision in:

* CI Job Deployment
* Selective Deployment (single revision or revision range)

***

#### Important Notes

* Data Kits can be created as **Standard** or **DevOps** in Salesforce Data Cloud
* ARM supports **only DevOps Data Kits** for automatic dependency retrieval
* This feature is supported only for **DX format workflows**
* **Org-to-Org Deployment is not supported**, as it does not use DX format
