# Update Commit Templates

### **Overview**

ARM enhances **EZ-Commit** to allow users to update existing Commit Templates with newly selected metadata components during the commit process.

When a commit is initiated using an existing Commit Template, users can choose to update the existing template or create a new one.

This enhancement simplifies Commit Template management and eliminates the need to create duplicate templates when additional metadata components are introduced.

### **How to Update an Existing Commit Template**

1. Navigate to **EZ-Commit**.
2. Initiate a commit using an existing Commit Template.
3. ARM loads the metadata components associated with the selected template.
4. Select the additional metadata components you want to include.
5. Proceed to the **Submit for Validation** step.
6. Choose one of the following options:

| Option                           | Description                                                                 |
| -------------------------------- | --------------------------------------------------------------------------- |
| **Update the existing template** | Updates the existing Commit Template with the selected metadata components. |
| **Create a new template**        | Creates a new Commit Template using the selected metadata components.       |

<figure><img src="../../.gitbook/assets/image (683).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (685).png" alt=""><figcaption></figcaption></figure>

7. Select **Update the existing template** and proceed with the submission.
8. ARM saves the newly selected metadata components to the existing Commit Template without creating duplicate entries.

### **Functional Behavior**

* Newly selected metadata components are saved to the existing Commit Template.
* Duplicate metadata component entries are prevented.
* The existing Commit Template name is retained unless explicitly changed by the user.
* ARM records the user who modified the template and the modification date.
* Existing Commit Template permissions are respected.

### **Important Considerations**

* The **Update the existing template** option is available only when EZ-Commit is initiated using an existing Commit Template.
* Only users with appropriate permissions can update an existing Commit Template.
* When EZ-Commit is initiated without an existing Commit Template, only the **Create a new template** option is available.
* The existing functionality for creating new Commit Templates remains unchanged.

### **Benefits**

* Simplifies Commit Template management.
* Reduces manual effort and duplicate template creation.
* Keeps existing Commit Templates up to date.
* Improves consistency across repeatable commit operations.
