---
hidden: true
---

# \[DRAFT - Project - X] Deployment Using Feature Migration Template

This article will walk you through deploying nCino data using the Feature Migration template. This provides a step-by-step procedure for creating a fresh migration using the "Deploy from template configuration".

1.  Feature Deployment can be triggered in the following ways

    1. Click on the "Create" button to observe the options to select the "Feature Deployment" as option

    <figure><img src="../../../../../.gitbook/assets/1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

    1. Click on the "Deployment History" under the nCino tab to access the "Create feature deployment"

    <figure><img src="../../../../../.gitbook/assets/1.1 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>
2. Upon selecting **"Create Feature Deployment" or "Feature Deployment,"** a Source Type screen will appear—choose from the available options to proceed.

<figure><img src="../../../../../.gitbook/assets/2 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

3. On selecting the "Source Type", the "Source" screen will be displayed.&#x20;

<figure><img src="../../../../../.gitbook/assets/3 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

4. Continue to input the required fields on the screen:
   1. **Label Name:** Input the desired lable name
   2. **Description:** Input a matching description that best describes the deployment being done
   3. **Feature Type:** Select either one of the options from "Standard" or "Community"
   4. **Feature:** Select the required feature from the list available under this field
   5. **Version:** continue to select the required version from the versions available
5. On filing the required details, click on the next to continue to the Destination screen, where the needed destinations can be selected.

<figure><img src="../../../../../.gitbook/assets/4 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

4. The destinations can be "Salesforce ORG" and/or "Version Control" here.
5. To deploy into a Salesforce Org, enable the **Deploy To** slider and choose your **Destination Org**. To commit to a branch, enable the **Commit To** slider, select the **Repository/Branch** details, and **comment** (if any).
6. Once done with selecting the destination(s), continue to the "Job Settings" page to select the required settings.

<figure><img src="../../../../../.gitbook/assets/5 - Feature Deployment.png" alt=""><figcaption></figcaption></figure>

4.  Before deploying to the destination, review and select from the available deployment criteria to proceed.

    **Deployment Filters**

    1. **Disable Workflow Rules:** This option will deactivate the workflow rules associated with objects part of the deployment.
    2. **Use Bulk API (Batch API will be used if the option is not enabled):** You can transfer bulk records in one go from the source and destination org.
    3. **Use UTF-8 file encoding for file read and write operations:** Use UTF-8 as the internal representation of strings. Text is transcoded from the local encoding to UTF-8 when data is written to or read from a file. UTF-8 must be enabled if your data exclusively contains English alphabet. UTF-8 must be disabled if your data contains non-English alphabets. UTF-8 should be enabled by default in accordance with Salesforce.
    4. **Automap User/Owner Data:** To ensure user permissions differences between different environments will not affect the RBC deployments, users are provisioned to disable the auto-assignment of users as they trigger the RBC deployments.
    5. **Disable Validation Rules:** This option will deactivate the validation rules associated with objects part of the deployment.
    6. **Insert/update with Null Values:** This will either insert or update record field values with null in the destination org (if the value is null in the source org).
    7. **Enable Rollback:** Enabling this option makes sure that the done deployment can be rolled back to the desired previous state.
5. Continue to the "Preview" tab to review to go through the selection made and to either **"Retrieve Dataset"** or **"Retrieve Dataset, Deploy and Commit"**
6. on selecting either of the **"Retrieve Dataset"** or **"Retrieve Dataset, Deploy and Commit"** options, you would be redirected to the  "Deployment History" page.
