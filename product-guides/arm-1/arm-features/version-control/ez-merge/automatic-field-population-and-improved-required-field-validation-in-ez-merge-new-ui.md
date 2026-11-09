# Automatic Field Population and Improved Required Field Validation in EZ-Merge (New UI)

**Product:** AutoRABIT ARM\
**Module:** Version Control – EZ-Merge\
**Availability:** New UI

### Overview

AutoRABIT ARM has enhanced the **EZ-Merge workflow** with automatic field population and improved required-field validation to simplify merge operations and reduce repetitive manual entry.

With this enhancement, ARM automatically populates known values based on the selected source branch and the organization's Merge Review Settings. Additionally, the **Dry Run** and **Merge** buttons remain enabled, allowing users to identify and correct missing required information through inline validation messages.

### What's New?

#### 1. Automatic Field Population

ARM automatically populates the following fields when the required information is available:

* **Target Branch:** Automatically selects the parent branch of the selected source branch.
* **Reviewer Emails:** Populates the logged-in user's email address along with reviewer emails configured in the organization's review settings.
* **Validate Deployment:** Automatically applies the organization's configured Merge Review Settings.
* **Static Code Analysis (SCA):** Automatically applies the SCA options configured in Merge Review Settings.

All automatically populated values remain editable, allowing users to review and modify them before proceeding.

#### 2. Improved Required Field Validation

<figure><img src="../../../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

The EZ-Merge workflow now provides clearer validation when required information is missing.

* The **Dry Run** and **Merge** buttons remain enabled even when required fields are incomplete.
* Clicking either button validates the required fields.
* Missing required fields are highlighted with a **red border** and an inline error message below the field.
* Users remain on the current screen until all required information is completed.
* Validation messages disappear once users enter valid information.

### How It Works

1. Navigate to **Version Control > EZ-Merge** in the New UI.
2. Select the required repository and source branch.
3. ARM automatically populates the **Target Branch** based on the selected source branch's parent.
4. Review the automatically populated **Reviewer Emails, Deployment Validation, and Static Code Analysis** settings.
5. Modify any values if required.
6. Click **Dry Run** or **Merge** to proceed.
7. If required information is missing, ARM highlights the corresponding fields and displays inline validation messages.
8. Complete the missing information and continue with the operation.

### Important Notes

* All automatically populated values remain **editable**.
* If the selected source branch does not have a configured parent branch, the Target Branch remains empty for manual selection.
* Automatic population of validation and SCA options depends on the organization's existing Merge Review Settings.
* Repository, Source Branch, Merge Type, and Conflict Resolution Strategy continue to require manual selection where applicable.
* Automatic suggestions for **Label Name** and **Description** are not included in this enhancement.
* Existing saved configurations and previously created merge operations are not affected.
* This enhancement is available only in the **ARM New UI**.

### Benefits

* **Reduced Manual Effort:** Automatically populates frequently used merge settings.
* **Improved Consistency:** Applies the organization's configured validation and SCA preferences.
* **Fewer Configuration Errors:** Helps users select the appropriate target branch.
* **Clearer Validation:** Highlights missing required fields with actionable inline messages.
* **Improved User Experience:** Simplifies merge configuration while allowing users to modify populated values.
