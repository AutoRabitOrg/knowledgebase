# Clone Release Labels

### **Overview**

ARM introduces the **Clone Release Label** option, allowing users to create a new Release Label by copying an existing one along with all its configurations and associated revisions.

The cloned Release Label can be managed independently without affecting the original Release Label.

**Availability:** New UI only.

### **How to Clone a Release Label**

1. Navigate to **Version Control → Release Labels**.
2. Locate the Release Label you want to clone.
3. Click the **Clone** icon next to the **Edit** icon.

4\. In the **Clone Release Label** popup, review the following fields:

| Field                  | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| Existing Release Label | Displays the selected Release Label name in read-only mode.             |
| New Release Label Name | Enter a unique name for the new Release Label. This field is mandatory. |

5. Click **Clone**.
6. Upon successful cloning, the newly created Release Label appears in the Release Labels list.

<figure><img src="../../.gitbook/assets/image (672).png" alt=""><figcaption></figcaption></figure>

### **Configurations and Revisions**

ARM automatically copies the following information from the original Release Label:

* Repository
* Branch
* Label Type
* Time Range
* Package Directory
* Description
* All associated revisions
* Other applicable Release Label settings

### **Important Considerations**

* The new Release Label name must be unique within the applicable scope.
* All configurations and revisions are copied automatically.
* Users can add or remove revisions from the cloned Release Label after creation.
* Changes made to the cloned Release Label do not affect the original Release Label.

### **Benefits**

* Reduces manual effort when creating similar Release Labels.
* Eliminates the need to manually select existing revisions.
* Ensures consistency across Release Label configurations.
* Enables independent management of cloned Release Labels.
