# How to Include Network Settings in Commit or Deployment

## **Overview**

This guide provides the steps to include network settings when performing a commit or deployment. Follow the instructions carefully to ensure that network access is properly configured.

### **Steps to Include Network Settings**

1. **Metadata Retrieval in EZ-Commit / Deployment:**
   * During the **metadata retrieval stage** in EZ-Commit or Deployment, you need to include the **"security"** metadata under the "settings" section.
   * This ensures that network settings, including security configurations, are taken into account for the commit or deployment process.
2. **Compare Changes Stage:**
   * In the **"compare changes"** stage, you will be able to review all the **Network Access** configurations that were part of the commit. This is applicable in the case of an **existing commit** (ex commit).
   * Use this stage to verify that network-related changes are included and match expectations.

***

{% hint style="info" %}
#### **Important Note:** For optimal deployment, it is **preferable to grant IP access according to** the profile. This ensures that only the necessary IP addresses are granted access based on the specific requirements of the deployment profile, helping to maintain security and compliance.&#x20;
{% endhint %}
