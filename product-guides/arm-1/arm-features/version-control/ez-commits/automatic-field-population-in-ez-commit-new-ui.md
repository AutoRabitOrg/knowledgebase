# Automatic Field Population in EZ-Commit (New UI)

**Product:** AutoRABIT ARM\
**Module:** Version Control – EZ-Commit\
**Availability:** New UI

### Overview

AutoRABIT ARM has enhanced the **EZ-Commit workflow** to automatically populate known values and suggest relevant information, reducing repetitive manual entry and simplifying commit creation.

With this enhancement, ARM automatically fills certain fields based on the logged-in user, selected Salesforce org, and repository configuration.

### What's New?

#### 1. Automatically Populated Fields

ARM automatically populates the following fields when the required information is available:

* **Reviewer Email:** Defaults to the logged-in user's email address.
* **Salesforce Org Author:** Automatically selects the logged-in user's mapped Salesforce org account, when available.
* **Parent Branch:** Defaults to the repository's configured default branch when creating a new branch.
* **Credentials:** Automatically selects the available credential when the user has only one credential.

#### 2. Suggested Values

ARM also suggests meaningful values for the following fields:

* **Commit Label:** Suggested based on the selected Salesforce org, branch, and date.
* **Commit Comment:** Suggested based on the selected metadata components.
* **Branch Display Name:** Suggested based on the linked work item or the user's name and date.

Users can accept these suggestions or modify them according to their requirements.

#### 3. Salesforce Org User Population

The **Salesforce Org User** field under **My Profile > Org Registration** is automatically populated using the username configured under **Org Settings > Details > Username**.

### How It Works

1. Navigate to **Version Control > EZ-Commit** in the New UI.
2. Start a new EZ-Commit operation and select the required Salesforce org.

<figure><img src="../../../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

3. Review the automatically populated author information and other available values.
4. When creating a new branch, review the default Parent Branch, Credentials, and suggested Branch Display Name.

<figure><img src="../../../../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

5. Review the suggested Commit Label, Commit Comment, and Reviewer Email.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2026-11-06 at 23.02.13.png" alt=""><figcaption></figcaption></figure>

6. Modify any values if needed and continue with the existing EZ-Commit workflow.

### Important Notes

* All automatically populated and suggested values remain **editable**.
* Fields are populated only when ARM can identify the appropriate information. Otherwise, they remain empty for manual selection.
* Existing saved configurations and previously created commits are not affected.
* Previously selected values for Salesforce org, repository, branch, components, and checkbox options are not automatically remembered.
* This enhancement is available in the **New UI**.

### Benefits

* Reduces repetitive manual entry during commit creation.
* Speeds up branch creation and commit configuration.
* Encourages consistent and meaningful commit labels and comments.
* Allows users to retain full control over automatically populated values.
