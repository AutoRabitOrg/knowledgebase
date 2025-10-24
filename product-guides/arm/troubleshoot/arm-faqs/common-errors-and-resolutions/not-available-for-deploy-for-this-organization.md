# Not Available for deploy for this organization

## Error message: Not Available for deploy for this organization

Getting the ''Not Available for deploy for this organization'' error message while deploying the Apex class to the target org can occur when your Salesforce user has an Integration license assigned.

<figure><img src="../../../../../.gitbook/assets/image (1750).png" alt=""><figcaption></figcaption></figure>

While this license generally allows users to validate and deploy standard or custom objects and fields, it is usually insufficient for deploying most other metadata types. For example, if you are trying to deploy new or updated permissions or custom items like Flows or Apex, the Integration license is likely to result in one of the following two errors:

* &#x20;"_Insufficient access rights on cross-reference id"_
* &#x20;_"not available for deploy for this organization_''

**Troubleshooting Steps**

1. Ensure your Salesforce deployment user has all the necessary permissions to deploy the metadata item to the target organization.
2. If you're unsure about which user permission(s) are required for the deployment, we recommend consulting with the administrators who manage the organization’s permissions. They are the best resources to assist you.
3. Check whether both environments being compared are using the same API version. Differences in metadata API versions between the source and target organizations may lead to validation errors.

{% hint style="info" %}
**Note**: _Please note that this error originates from Salesforce rather than AutoRABIT. Nevertheless, we are committed to offering support based on our collective experience with the Metadata API. Our goal is to assist you in navigating this issue and, when possible, help you find a solution. If a resolution is not achievable, we may recommend reaching out to Salesforce support for additional assistance. Thank you for your understanding._
{% endhint %}
