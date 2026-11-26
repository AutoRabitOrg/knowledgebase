# Salesforce Authentication Changes

### **Overview**

Salesforce is retiring SOAP API username and password authentication (`login()`) as part of its security enhancements.

To prepare for this change, ARM has enhanced its Salesforce authentication workflows by restricting new Standard authentication registrations and providing improved authentication error messages.

Customers using **Standard authentication** are encouraged to migrate to **OAuth via External Client Applications (ECA)** before Salesforce retires SOAP API login in Summer '27.

**Availability:** Classic and New UI, including API-based registrations.

### **Salesforce Retirement Timeline**

| Effective Date                | Salesforce Changes                                                                                                                                       |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| December 1, 2026              | The **Use Any API Auth** permission is required for SOAP API login.                                                                                      |
| December 15, 2026 – Sandbox   | Security token requirements for broad login IP ranges and SOAP API login restrictions for orgs that have not used SOAP login in the previous six months. |
| January 31, 2027 – Production | The above security restrictions apply to production orgs.                                                                                                |
| Summer '27                    | Retirement of SOAP API `login()` for API versions 31.0–64.0.                                                                                             |

For more information, refer to [Salesforce SOAP API Login Retirement](https://help.salesforce.com/s/articleView?id=005132110\&type=1\&utm_source=chatgpt.com).

### **Changes in ARM**

#### **1. New Salesforce Org Registrations**

The **Standard** authentication option is no longer available when registering new Salesforce Orgs or Dev Hubs.

Users are encouraged to register Salesforce Orgs using **OAuth via ECA**.

This restriction applies to both Classic and New UI, including API-based registrations.

<figure><img src="../../.gitbook/assets/image (673).png" alt="" width="188"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (674).png" alt="" width="188"><figcaption></figcaption></figure>

#### **2. Existing Salesforce Org Registrations**

Existing Salesforce Orgs registered using Standard authentication can continue to operate, subject to Salesforce's authentication requirements.

Users can:

* Update existing passwords and security tokens.
* Test existing Salesforce Org connections.
* Migrate existing Standard authentication configurations to OAuth via ECA.

![](<../../.gitbook/assets/image (682).png>)

#### **3. Improved Authentication Error Messages**

ARM now provides more specific and actionable error messages when Salesforce authentication fails.

| Authentication Issue                    | Recommended Action                                                                                   |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Missing **Use Any API Auth** permission | Assign the required permission to the Salesforce integration user or migrate to OAuth via ECA.       |
| Security token required                 | Update the security token in ARM, review the Salesforce login IP range, or migrate to OAuth via ECA. |
| SOAP API login disabled or retired      | Migrate the Salesforce Org to OAuth via ECA.                                                         |

These improvements help users identify authentication failures through relevant UI notifications, execution logs, and job failure emails.

### **Migrating to OAuth via ECA**

Customers using Standard authentication are encouraged to migrate their existing Salesforce Org connections to OAuth via ECA.

1. Configure an External Client Application in Salesforce with the required OAuth settings.
2. Log in to ARM as an authorized administrator.
3. Navigate to Salesforce Org Management.
4. Edit the existing Salesforce Org registered with Standard authentication.
5. Change the authentication type to **OAuth via ECA**.
6. Provide the required ECA configuration details and complete OAuth authorization.
7. Save the configuration and verify the connection using **Test Connection**.

### **Important Considerations**

* Existing OAuth and OAuth via ECA connections remain unaffected by this SOAP API login retirement.
* New Standard authentication registrations are no longer supported.
* Existing Standard authentication connections remain subject to Salesforce's phased security restrictions.
* Customers should complete their migration before Summer '27 to avoid interruptions to ARM operations.
* ARM plans to remove Standard authentication entirely in alignment with Salesforce's SOAP API login retirement.

**Recommendation:** Migrate all existing Salesforce Orgs and Dev Hubs using Standard authentication to OAuth via ECA as early as possible to ensure uninterrupted Salesforce connectivity.
