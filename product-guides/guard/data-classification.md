# Data Classification

## Overview

AutoRABIT Guard’s Data Classification enhances your organization's ability to identify and manage sensitive data within Salesforce environments. By automatically classifying and categorizing data based on sensitivity and compliance requirements, AutoRABIT supports your data governance and security strategies.

### Key Capabilities

* **Automated Data Classification**\
  Instantly scans your Salesforce org—including all custom fields across all objects—and classifies them against key regulations:
  * **PCI**
  * **HIPAA**
  * **GDPR**
  * **COPPA**
  * **CCPA**
  * **PersonalInfo**
  * **PII**
* **Regulation-Based Filtering**\
  Use the **Relevant Regulations** filter to quickly identify which fields align with specific compliance standards.
* **Object-Based Filtering**\
  Select to review fields based on specific Objects.
* **Field Insights: Know What's Really Happening**\
  For each classified field, Guard provides detailed context on how it matches a specific regulation—going beyond static definitions.\
  \
  Why It Matters? It's not enough to know a field is sensitive—you need to know how widely it's used and in what contexts. Guard tells you:&#x20;
  * **Where the field lives**: See where the field appears across your org in Page Layouts, Apex Classes, Flows, Validation Rules, etc.&#x20;

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Field Usage</p></figcaption></figure></div>

* **How often it's populated**: Understand if the field is frequently used, rarely touched, or unused—critical for prioritizing cleanup or lockdowns.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Records by Type</p></figcaption></figure>

*   **Access Visibility: See Who Has Keys**\
    Even well-protected data becomes a risk if too many people have access to it. With Guard, you can instantly view which Profiles, Permission Sets, and Permission Set Groups have access to a sensitive field.\


    <figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Access Visibility</p></figcaption></figure>

### Getting Started

To use Data Classification in Guard:

1. **Navigate** to the Data Classification module within the Compliance section.
2. **Salesforce Org**: Select one of your orgs registered in Guard
3. **Run Data Scans**: Your organization is scanned automatically, but you can also Refresh data manually as needed
4. **Review and Act**: Use filters to analyze classification results and implement necessary security controls or policy adjustments.

### Benefits

* **Increased Visibility**: Ensures sensitive data is appropriately classified and ready to be analyzed.
* **Regulatory Compliance**: Facilitates adherence to data protection laws by providing clear visibility into data types and their associated handling requirements.
* **Operational Efficiency**: Reduces manual efforts in data identification and classification, allowing teams to focus on strategic initiatives.
* **Risk Mitigation**: Identifies potential data exposure risks, enabling proactive measures to prevent data breaches.

### Conclusion

AutoRABIT's Data Classification feature empowers organizations to gain deeper insights into their data landscape, ensuring sensitive information is managed appropriately and in compliance with relevant regulations.
