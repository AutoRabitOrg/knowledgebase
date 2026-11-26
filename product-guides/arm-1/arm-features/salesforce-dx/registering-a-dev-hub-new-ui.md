# Registering a Dev Hub (New UI)

### **Introduction**

A Dev Hub is a Salesforce Org used to create and manage Scratch Orgs for Salesforce development, testing, and package development.

ARM allows users to register Dev Hubs through Salesforce Org Manager and manage them through the Hub Management module.

### **Prerequisites**

* Enable Dev Hub in your Salesforce Org.
* Ensure the Salesforce user has the required permissions to access and manage the Dev Hub.

### **Enable Dev Hub in Salesforce**

1. Log in to your Salesforce Org.
2. Navigate to **Setup**.
3. Search for **Dev Hub** in the Quick Find box.
4. Enable **Dev Hub**.
5. Enable **Unlocked Packages and Second-Generation Managed Packages**, if required.

<figure><img src="../../../../.gitbook/assets/image (717).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (718).png" alt=""><figcaption></figcaption></figure>

### **Register a Dev Hub**

Dev Hub registration is no longer available directly from the **SFDX → Hub Management** screen.

A notification is displayed directing users to Salesforce Org Manager to register a new Dev Hub.

<figure><img src="../../../../.gitbook/assets/image (720).png" alt=""><figcaption></figcaption></figure>

#### **Registration through Salesforce Org Manager**

1. Navigate to **Salesforce Org Manager**.
2. Click the Salesforce Org registration option.
3. In the **Register Salesforce Org** screen, provide the following details:

| Field                   | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **Name**                | Enter a name for the Salesforce Org.                                 |
| **Type**                | Select the appropriate Org type. Development is selected by default. |
| **Environment**         | Select Production or Development Edition.                            |
| **URL**                 | Verify the Salesforce login URL.                                     |
| **Access Type**         | Select **OAuth**.                                                    |
| **Is nCino Installed**  | Enable this option if nCino is installed in the Salesforce Org.      |
| **Register as Dev Hub** | Enable this checkbox to register the Salesforce Org as a Dev Hub.    |

4. Select the **Register as Dev Hub** checkbox.
5. Click **Validate & Save**.
6. Complete Salesforce authentication and authorize ARM to access the Salesforce Org.
7. Upon successful registration, navigate to **SFDX → Hub Management** to access the registered Dev Hub.

<figure><img src="../../../../.gitbook/assets/image (736).png" alt=""><figcaption></figcaption></figure>

**Note:** The **Register as Dev Hub** option is available only when OAuth is selected. This option is not available when OAuth via ECA is selected.

<figure><img src="../../../../.gitbook/assets/image (737).png" alt=""><figcaption></figcaption></figure>

### **Manage Registered Dev Hubs**

Navigate to **SFDX → Hub Management** and select the registered Dev Hub from the list.

The following tabs are available:

| Tab                       | Description                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| **Details**               | View the Dev Hub name, username, environment, and Salesforce URL. |
| **Scratch orgs**          | View Scratch Orgs associated with the selected Dev Hub.           |
| **Hub level permissions** | Manage user access to the Dev Hub.                                |
| **Org's API limits**      | View Salesforce API limits.                                       |
| **Packages**              | View packages associated with the Dev Hub.                        |

<figure><img src="../../../../.gitbook/assets/image (738).png" alt=""><figcaption></figcaption></figure>

### **Re-Authenticate a Dev Hub**

1. Navigate to **SFDX → Hub Management**.
2. Select the required Dev Hub.
3. Navigate to the **Details** tab.
4. Click **Re-Authenticate**.
5. Complete the Salesforce authentication process.

### **Test Connection**

1. Select the registered Dev Hub.
2. Navigate to the **Details** tab.
3. Click **Test connection** to verify Salesforce connectivity.

### **Hub Level Permissions**

1. Select the registered Dev Hub.
2. Navigate to the **Hub level permissions** tab.
3. Configure the required user permissions and save the changes.

<figure><img src="../../../../.gitbook/assets/image (739).png" alt=""><figcaption></figcaption></figure>

### **View Org's API Limits**

1. Select the registered Dev Hub.
2. Navigate to the **Org's API limits** tab.
3. Review the available Salesforce API limits.

<figure><img src="../../../../.gitbook/assets/image (740).png" alt=""><figcaption></figcaption></figure>

### **View Packages**

1. Select the registered Dev Hub.
2. Navigate to the **Packages** tab.
3. Review the packages and associated package versions.

<figure><img src="../../../../.gitbook/assets/image (741).png" alt=""><figcaption></figcaption></figure>

### **Important Considerations**

* New Dev Hubs must be registered through Salesforce Org Manager.
* Direct Dev Hub registration from Hub Management is no longer supported.
* Only **OAuth** authentication supports new Dev Hub registration.
* The **Register as Dev Hub** checkbox is not available with OAuth via ECA.
* Registered Dev Hubs can continue to be managed through **SFDX → Hub Management**.

### **What's Next?**

After successfully registering a Dev Hub, users can proceed with creating and managing Scratch Orgs in ARM.
