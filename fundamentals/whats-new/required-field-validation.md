# Required Field Validation

### **Overview**

ARM has enhanced required field validation across multiple workflows in the **New UI** to provide a more intuitive and user-friendly experience.

These enhancements help users easily identify missing or invalid information, understand validation errors, and complete their configurations before proceeding with an action.

### **Enhanced Validation Behavior**

The following improvements apply across supported workflows:

* **Required Field Highlighting:** Highlights missing or invalid mandatory fields when users attempt to proceed.
* **Inline Error Messages:** Displays clear and meaningful validation messages alongside the affected fields.
* **Automatic Navigation:** Automatically scrolls to the first field requiring attention.
* **Informative Tooltips:** Explains why an action button is unavailable, helping users understand and resolve validation errors.

### **Supported Workflows**

#### **1. External Pull Request Creation**

When users click **Create Pull Request** without providing the required information, ARM highlights the missing or invalid fields, displays inline error messages, and automatically navigates to the first field requiring attention.

Tooltips provide additional guidance when the **Create Pull Request** button is unavailable.

![](<../../.gitbook/assets/image (650).png>)

#### **2. Get Org Differences**

When users click **Save** or **Save and Run** without completing the required fields or run configurations, ARM highlights the affected fields and displays relevant validation messages.

Tooltips explain why an action is unavailable, helping users resolve validation errors before saving or running Org Differences.

![](<../../.gitbook/assets/image (652).png>)

#### **3. Release Label Creation and Editing**

When users click **Save** without completing the required information, ARM highlights the affected fields and displays inline validation messages.

Additionally, ARM provides validation feedback when fewer than **two revisions** are selected. Tooltips explain why the **Save** button is unavailable.

<figure><img src="../../.gitbook/assets/image (670).png" alt=""><figcaption></figcaption></figure>

### **Benefits**

* Consistent validation experience across ARM workflows.
* Clear and actionable error messages.
* Easier identification of missing or invalid information.
* Reduced configuration errors and improved usability.

**Note:** These enhancements are available exclusively in the New UI.
