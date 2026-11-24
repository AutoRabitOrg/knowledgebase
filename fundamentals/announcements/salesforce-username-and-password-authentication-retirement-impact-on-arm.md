# Salesforce Username and Password Authentication Retirement – Impact on ARM

### **Overview**

Salesforce is retiring username and password-based authentication through the SOAP API `login()` method in a phased approach, with complete retirement scheduled for the Salesforce Summer ’27 release.

This change impacts Salesforce organizations registered in AutoRABIT Release Management (ARM) using the **Standard** access type.

To ensure uninterrupted connectivity and continued execution of ARM operations, customers are advised to migrate their existing Salesforce organizations from Standard authentication to **OAuth authentication using External Client Apps (ECA)**.

### **Salesforce Retirement Timeline**

Salesforce is introducing the following changes in phases:

| Effective Date                | Salesforce Change                                                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| December 1, 2026              | Users authenticating through SOAP API `login()` must have the **Use Any API Auth** permission.                                                                                              |
| December 15, 2026 – Sandbox   | Security tokens will be required for authentication from broad login IP ranges. SOAP API `login()` will be disabled in organizations where it has not been used in the previous six months. |
| January 31, 2027 – Production | The same security token requirements and inactivity-based restrictions will apply to production organizations.                                                                              |
| Summer ’27 Release            | SOAP API `login()` will be retired for API versions 31.0 through 64.0.                                                                                                                      |

### **Impact on ARM Customers**

Customers who have registered Salesforce organizations in ARM using the **Standard (Username and Password)** access type may experience authentication failures as Salesforce introduces these restrictions.

Authentication failures may impact the following ARM operations:

* EZ-Commit and EZ-Merge
* CI Jobs
* Deployments and Deployment Validations
* Org Synchronization
* Environment Provisioning
* Other operations that require Salesforce organization connectivity

Customers already using OAuth authentication are not directly impacted by the retirement of SOAP API `login()`.

### **Changes in ARM**

To align with Salesforce's authentication retirement timeline, AutoRABIT is introducing the following changes in phases:

| Change                             | Description                                                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Authentication Warning             | ARM displays a warning for Salesforce organizations registered using Standard authentication. Available from ARM 26.3.13. |
| Standard Registration Restriction  | ARM will prevent new Salesforce organization registrations using the Standard access type.                                |
| Improved Error Messages            | ARM will provide clearer authentication error messages to help users identify and resolve Salesforce login restrictions.  |
| Standard Authentication Retirement | ARM plans to remove Standard authentication in alignment with the Salesforce Summer ’27 retirement timeline.              |

### **Recommended Action for Customers**

AutoRABIT strongly recommends migrating all existing Salesforce organizations registered using Standard authentication to OAuth authentication using External Client Apps (ECA).

#### **Step 1: Identify Salesforce Organizations Using Standard Authentication**

1. Log in to ARM.
2. Navigate to **Salesforce Org Management**.
3. Review the registered Salesforce organizations.
4. Identify organizations configured with the **Standard** access type.

#### **Step 2: Migrate to OAuth Authentication Using ECA**

1. Configure an External Client App in Salesforce.
2. Ensure the Salesforce integration user has the required permissions.
3. Configure the Salesforce organization in ARM using OAuth authentication through ECA.
4. Authorize the Salesforce connection.
5. Verify connectivity and validate the associated ARM workflows.

### **Temporary Measures for Existing Standard Connections**

If immediate migration to OAuth is not possible, customers should ensure the following Salesforce configurations are in place, where applicable:

* Assign the **Use Any API Auth** permission to the Salesforce integration user.
* Ensure **Enable SOAP API login()** is enabled in Salesforce.
* Provide a valid security token where required by Salesforce login IP restrictions.
* Verify that the configured username and password are valid.

**Important:** These measures are temporary and will not prevent authentication failures once Salesforce permanently retires SOAP API `login()`. Migration to OAuth authentication is the recommended long-term solution.

### **Frequently Asked Questions**

#### **Are existing OAuth connections impacted?**

No. Salesforce organizations already configured with supported OAuth authentication methods are not directly impacted by this SOAP API `login()` retirement.

#### **Can I continue using Standard authentication until Summer ’27?**

Existing Standard connections may continue to work, provided they meet Salesforce's authentication requirements during each phase. However, AutoRABIT recommends completing the migration as early as possible to avoid service disruptions.

#### **Can I register new Salesforce organizations using Standard authentication?**

ARM plans to restrict new Salesforce organization registrations using Standard authentication. Customers should use OAuth authentication through ECA for new registrations.

#### **What happens if I do not migrate before Summer ’27?**

Salesforce organizations using Standard authentication will no longer be able to authenticate through the retired SOAP API `login()` method, resulting in failures for dependent ARM operations.

### **References**

* [Salesforce Knowledge Article – SOAP API login() Retirement (KA 005132110)](https://help.salesforce.com/s/articleView?id=005132110\&type=1)

For further assistance with migrating Salesforce organizations to OAuth authentication using ECA, please contact our **Support Team**

**Note:** AutoRABIT recommends completing the migration before the Salesforce authentication restrictions take effect to ensure uninterrupted connectivity and business continuity.
