---
hidden: true
---

# nCino Compare

## nCino Compare

**Introduction**

The Compare and Selective Deployment functionality in nCino enables users to perform detailed comparisons between datasets and object records across Salesforce environments or between a Salesforce Org and a version control repository. This process helps identify changes and selectively promote only the required records to the intended target environment.

**Overview**

* **Flexible Comparison Options**\
  Perform comparisons between two Salesforce Orgs (_Org-to-Org_) or between a Salesforce Org and a version control repository (_Org-to-Version Control_).
* **Relational Comparison Support**\
  Execute relational comparisons that take into account object relationships, ensuring accuracy in identifying relevant data changes.
* **Granular Record Selection**\
  View and select individual records at any level of the comparison hierarchy, providing full control over what is promoted.
* **Save and Reuse Selections**\
  Save selected records during comparison to revisit or finalize at a later stage, supporting iterative workflows.
* **Deployment Execution**\
  Proceed with deployment using the **Save and Deploy** option, which finalizes the selection and initiates the deployment process.
* **Object Summary and RBC Integration**\
  Access a consolidated _Object Summary_ screen to review selected records before deployment. From here, initiate RBC-based deployments directly.

### Step-by-Step Guide - Initiating Compare Operation

#### Initiating Compare Operation

**Feature Deployment – Template & Version Control**

1.  Click on "Create Feature Dployment" to initate the featre deployment creatio

    <figure><img src="../../../../.gitbook/assets/image (2446).png" alt=""><figcaption></figcaption></figure>
2.  Select **“Template”** or **“Version Control”** to reveal the **Retrieve Dataset** option.

    <figure><img src="../../../../.gitbook/assets/Compare - 1.1.png" alt=""><figcaption></figcaption></figure>
3. Clicking it redirects to the **Deployment History** page.
4. On that page, use **View Dataset** to open the dataset.

**Feature Deployment – Using Salesforce Org**

1. Select **Template Using Salesforce Org** or **VC Using Salesforce Org** to see **Create Dataset**.
2.  Refer the "[Feature Deployment](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/ncino/feature-deployment)" section for the creation of a feature deployment.

    <figure><img src="../../../../.gitbook/assets/Compare - 1.2.png" alt=""><figcaption></figcaption></figure>
3. Click **Retrieve Dataset** to start a comparison.
4. This would redirect the flow to the Deployment History.

**Perform Compare**

1. **Access Compare Option**
   *   From the **Deployment Iterations** page, select the ellipsis (three dots) for a specific iteration.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.png" alt=""><figcaption></figcaption></figure>
   *   Choose **Compare** to analyze dataset differences between environments.

       <figure><img src="../../../../.gitbook/assets/Compare - 2.1.png" alt=""><figcaption></figcaption></figure>
   * This helps validate consistency of deployed records.
2. **Select Comparison Destination**
   * In the **Compare** window, select between the destination type:
     *   **Salesforce Org**: Compares records with another Salesforce environment.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.png" alt=""><figcaption></figcaption></figure>
     *   **Version Control**: Compares records with version-controlled data.

         <figure><img src="../../../../.gitbook/assets/Compare - 3.1.png" alt=""><figcaption></figcaption></figure>
     * Choose the destination org or repository to proceed.
3. **Configure Comparison Parameters**
   *   Provide details such as:

       * **Feature Name**
       * **Object**
       * **Unique Id** (used to uniquely identify records)

       <figure><img src="../../../../.gitbook/assets/Compare - 4.png" alt=""><figcaption></figcaption></figure>
   *   Optionally, select fields to **exclude from comparison** (e.g., system fields like CreatedDate).

       <figure><img src="../../../../.gitbook/assets/Compare - 4.1.png" alt=""><figcaption></figcaption></figure>
   * Excluding non-essential fields avoids unnecessary mismatches.
4.  **Run Comparison**

    *   After configuring all parameters, click **Compare**.

        <figure><img src="../../../../.gitbook/assets/Compare - 5.png" alt=""><figcaption></figcaption></figure>
    *

    ```
    [<br>](https://github.com/AutoRabitOrg/knowledgebase/blob/7b2fb680c2e173abe9167088ba9aadb8ee2e1012/.gitbook/assets/Compare%20-%205.png)
    ```

[<br>](https://github.com/AutoRabitOrg/knowledgebase/blob/7b2fb680c2e173abe9167088ba9aadb8ee2e1012/.gitbook/assets/Compare%20-%201.1%20\(1\).png)
