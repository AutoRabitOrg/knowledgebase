# Registering a Dev Hub (Classic UI)

### **Introduction**

A Dev Hub is a Salesforce Org used to create and manage Scratch Orgs for Salesforce development and testing.

ARM allows users to register Dev Hubs and manage associated Scratch Orgs, user permissions, Salesforce API limits, and packages.

### **Prerequisites**

* Enable Dev Hub in your Salesforce Org.
* Ensure the Salesforce user has the required permissions to access and manage the Dev Hub.

### **Enable Dev Hub in Salesforce**

1. Log in to your Salesforce Org.
2. Navigate to **Setup**.
3. Search for **Dev Hub** in the Quick Find box.
4. Enable **Dev Hub**.
5. Enable **Unlocked Packages and Second-Generation Managed Packages**, if required.

<figure><img src="../../../../.gitbook/assets/image (742).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (743).png" alt=""><figcaption></figcaption></figure>

### **Register a Dev Hub**

New Dev Hub registrations must be performed through Salesforce Org registration using **OAuth** authentication.

1. Log in to the ARM Classic UI.
2. Navigate to Salesforce Org registration.
3. Enter the required Salesforce Org details.
4. Select **Production or Development Edition** as the environment.
5. Select **OAuth** as the Access Type.
6. Enable the **Register as Dev Hub** option.
7. Complete the registration and Salesforce authorization process.
8. Navigate to **SFDX → Hub Management** to access the registered Dev Hub.

<figure><img src="../../../../.gitbook/assets/image (744).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (745).png" alt=""><figcaption></figcaption></figure>

**Note:** Dev Hub registration is supported only through OAuth authentication. OAuth via ECA does not support Dev Hub registration.

### **Hub Level Permissions**

1. Navigate to **SFDX → Hub Management**.
2. Locate the registered Dev Hub.
3. Click **Hub Level Permissions**.
4. Configure the required user permissions.
5. Save the changes.

<figure><img src="../../../../.gitbook/assets/image (746).png" alt=""><figcaption></figcaption></figure>

### **View Org's API Limits**

1. Navigate to **SFDX → Hub Management**.
2. Locate the registered Dev Hub.
3. Click **View Org's API Limits**.
4. Review the maximum and remaining Salesforce API limits.

<figure><img src="../../../../.gitbook/assets/image (747).png" alt=""><figcaption></figcaption></figure>

### **View Packages**

1. Navigate to **SFDX → Hub Management**.
2. Locate the registered Dev Hub.
3. Click **View Packages**.
4. Review the available managed and unlocked packages, package versions, and applicable ancestor information.

<figure><img src="../../../../.gitbook/assets/image (768).png" alt=""><figcaption></figcaption></figure>

### **Important Considerations**

* Dev Hub registration requires OAuth authentication.
* OAuth via ECA does not support new Dev Hub registration.
* Registered Dev Hubs can be managed through Hub Management.
* Standard authentication is no longer supported for new Salesforce Org registrations.

### **What's Next?**

After successfully registering a Dev Hub, users can proceed with creating and managing Scratch Orgs in ARM.
