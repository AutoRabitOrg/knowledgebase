# Salesforce Summer ’27 Update: Retirement of SOAP API login() Authentication

### Overview

Salesforce has announced the retirement of the **SOAP API `login()` authentication method** by **Summer ’27**. This method allows integrations to authenticate using **Username + Password + Security Token**.

AutoRABIT currently provides a legacy authentication option that uses this mechanism to connect to Salesforce organizations. Since Salesforce is deprecating this method, it may impact integrations that rely on this authentication approach.

### Impact

If your AutoRABIT connection to Salesforce uses the following authentication method:

* Username
* Password
* Security Token

then it relies on the **SOAP API `login()` method**.

Once Salesforce retires this functionality, this authentication method will no longer be supported by Salesforce, and integrations using it may fail to authenticate.

### Where to Find the Setting

You can locate this setting in **Salesforce Setup**.

**Navigation:**\
`Setup → Quick Find → User Interface → Enable SOAP API login()`

If this option is enabled, external systems can authenticate using the **SOAP API `login()` call**.

### Important Note

Salesforce has announced that **SOAP API `login()` will be retired in Summer ’27**. For new Salesforce orgs, this option is **disabled by default**.

Even if you see a message about the retirement when hovering over the setting, it simply indicates the future deprecation notice and does **not affect the current configuration**.

### Recommendation

Salesforce is moving toward a modern integration model using **External Client Apps**.

External Client Apps are designed for **secure API-based integrations** and provide stronger authentication and governance controls for external systems.

AutoRABIT recommends using authentication based on **OAuth authentication via External Client Apps**.

This approach aligns with Salesforce’s long-term **security and integration strategy**.

### References

**Salesforce Documentation – SOAP API `login()`**\
[https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce\_api\_calls\_login.htm](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_login.htm)

**Salesforce Knowledge Article**\
[https://help.salesforce.com/s/articleView?id=005132110\&type=1](https://help.salesforce.com/s/articleView?id=005132110\&type=1)

{% hint style="info" %}
**Note:** Customers are encouraged to review their current authentication configurations and update them before the **Summer ’27 Salesforce release** to avoid potential service disruptions.
{% endhint %}
