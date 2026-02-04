# Configuring Metadata Folder Paths

## Overview

When working with non-SFDX repositories in your version control setup, it's important to correctly configure the metadata folder path for each branch to ensure successful deployments and CI job executions.

### Metadata Folder Path Configuration

**When Using a Custom src Folder**

If your non-SFDX repository is structured using a folder named src (or any other custom folder name), it is mandatory to configure the Metadata Folder Path for each branch.

**Navigate to:**

Admin > VC Repos > Branches > Branch Settings\
Update the Metadata Folder Path with the appropriate folder name (e.g., src)\
This step must be completed immediately after branch creation or registration.

### Why It Matters

If the metadata folder path is not correctly set up for non-default folder structures, metadata changes will not be detected when triggering CI jobs, which can lead to failed or incomplete deployments.

**When Using the Default SFDX Structure**

For non-SFDX repositories that follow the default SFDX folder structure (i.e., force-app/main/default)\
The system automatically detects the metadata folder. There is no need to manually configure the Metadata Folder Path under Branch Settings.

{% hint style="warning" %}
Important: Manually adding the Metadata Folder Path in this case can interfere with automatic detection, resulting in CI job builds not picking up changes correctly and gives build status as “No Modifications.”
{% endhint %}

**If Metadata Folder Path Was Incorrectly Configured**

If the Metadata Folder Path was incorrectly configured whether for a custom folder (SFDX or non-SFDX) or the default folder structure, the change will not immediately reflect after the path is corrected. Specifically, if a CI Job has already been created, simply removing the incorrect folder path from the Branch Settings will not automatically update the CI job configuration.

**To Correct This:**

Remove the incorrect metadata folder path under:\
Admin > VC Repos > Branches > Branch Settings

Then, go to the associated CI Job:

* Edit the CI Job
* Re-save it without making any changes

This refreshes the backend CI job configuration and ensures the correct package directory is applied in future CI job runs.
