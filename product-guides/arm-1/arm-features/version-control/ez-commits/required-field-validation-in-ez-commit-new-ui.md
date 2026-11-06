# Required Field Validation in EZ-Commit (New UI)

**Product:** AutoRABIT ARM\
**Module:** Version Control – EZ-Commit\
**Availability:** New UI

### Overview

AutoRABIT ARM has enhanced the **Create EZ-Commit workflow** with improved required-field validation, making it easier to identify and correct missing information before proceeding.

With this enhancement, the **Next** and **Submit** buttons remain enabled, and ARM displays clear inline validation messages when users attempt to proceed without completing required fields.

### What's New?

#### 1. Improved Required Field Validation

* The **Next** and **Submit** buttons remain enabled even when required fields are incomplete.
* Clicking these buttons highlights all missing required fields and displays error messages directly below them.
* ARM automatically scrolls to and focuses on the first missing required field.
* Validation messages disappear as users provide valid information.
* Users can proceed to the next step only after completing the required fields.

#### 2. Validation Across EZ-Commit Steps

<figure><img src="../../../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

**Step 1 – New Commit**

ARM validates required fields such as:

* Salesforce Org and Salesforce Org Author
* Repository and Branch
* Components and Manageable States
* Additional fields such as Package Directory, Package Manifest, Commit Template, Labels, and ALM details when applicable

**Step 2 – Metadata Selection**

If users click **Next** without selecting any metadata, ARM displays a validation message and automatically scrolls to the metadata selection area.

**Step 4 – Submit for Validation / Commit / PR**

Clicking **Submit** validates the required fields based on the selected operation, including Commit Comments, Commit Labels, Reviewer Emails, Validation Options, and other applicable settings.

#### 3. Improved Navigation Feedback

When users attempt to access a step that is unavailable because required information is missing, a tooltip explains what needs to be completed before proceeding.

### How It Works

1. Navigate to **Version Control > EZ-Commit** in the New UI.
2. Start a new EZ-Commit operation.
3. Click **Next** to proceed.
4. If required information is missing, ARM highlights the fields and displays inline error messages.
5. Complete the highlighted fields. The corresponding validation messages disappear automatically.
6. Continue through the workflow and click **Submit** to complete the operation.

### Important Notes

* Validation messages appear directly below the relevant fields instead of displaying a general notification.
* ARM automatically scrolls to the first missing required field, including fields outside the visible screen area.
* Required fields may vary depending on the selected component type, fetch method, and operation.
* Existing validation behavior for fields that already validate during user interaction remains unchanged.
* The existing behavior for large metadata selections (more than 50 files) in the optional Review Artifact step remains unchanged.
* This enhancement is available only in the **ARM New UI**.

### Benefits

* Quickly identifies missing required information.
* Reduces confusion caused by disabled navigation buttons.
* Simplifies navigation through multi-step EZ-Commit workflows.
* Provides a smoother and more intuitive commit experience.
