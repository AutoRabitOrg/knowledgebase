# Improved Required Field Validation in Commit Templates (New UI)

**Product:** AutoRABIT ARM\
**Module:** Version Control – Commit Templates\
**Availability:** New UI

### Overview

AutoRABIT ARM has enhanced the **Commit Template workflow** with improved required-field validation, making it easier to identify and correct missing information when creating, editing, or cloning Commit Templates.

With this enhancement, the **Next** and **Save Template** buttons support click-based validation, displaying clear inline error messages when users attempt to proceed without completing required information.

### What's New?

#### 1. Improved Required Field Validation

* The **Next** button remains enabled even when required fields are incomplete or metadata has not been selected, except when an operation is temporarily unavailable.
* Clicking **Next** or **Save Template** validates the required information.
* Missing or invalid fields are highlighted with inline error messages displayed directly below them.
* ARM automatically scrolls to and focuses on the first missing required field.
* Validation messages disappear as users provide valid information.

#### 2. Validation Across Commit Template Steps

**Step 1 – Select Metadata**

ARM validates the following required information:

* **Template Name:** A valid template name must be provided.
* **Source Org:** A Salesforce org must be selected.
* **Metadata Selection:** At least one metadata component must be selected.

If required information is missing, ARM displays the corresponding validation messages and prevents users from proceeding until the fields are completed.

**Step 2 – Review and Save**

Clicking **Save Template** validates the required information before saving. If any required information is missing, ARM displays inline error messages instead of relying on general pop-up notifications.

#### 3. Informative Tooltips

When the **Next** or **Save Template** button is temporarily disabled, such as while metadata is loading or a save operation is in progress, a tooltip explains why the action is unavailable.

### How It Works

1. Navigate to **Version Control > Commit Templates** in the New UI.
2. Create a new Commit Template or select an existing template to edit or clone.
3. Enter the **Template Name**, select the **Source Org**, and choose the required metadata.
4. Click **Next** to proceed.
5. If required information is missing, ARM highlights the corresponding fields and displays inline validation messages.
6. Complete the missing information and proceed to **Review and Save**.
7. Click **Save Template** to save the configuration.

### Important Notes

* At least one metadata component must be selected before proceeding.
* The **Description** field remains optional.
* Validation messages automatically disappear once the required information is provided.
* Existing duplicate template name validation remains unchanged.
* Buttons may be temporarily disabled during loading or save operations, with tooltips explaining the reason.
* This enhancement applies to **creating, editing, and cloning Commit Templates**.
* This functionality is available only in the **ARM New UI**.

### Benefits

* **Clearer Validation:** Helps users quickly identify missing required information.
* **Improved Navigation:** Automatically scrolls to the first invalid field.
* **Reduced Manual Effort:** Eliminates the need to check individual fields to identify missing information.
* **Better User Experience:** Provides actionable inline messages and informative tooltips.
* **Consistent Workflow:** Improves validation across Commit Template creation, editing, and cloning.
