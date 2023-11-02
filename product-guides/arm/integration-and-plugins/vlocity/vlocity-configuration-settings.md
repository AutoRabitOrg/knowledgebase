# Vlocity Configuration Settings

Vlocity integration with ARM allows you to retrieve and deploy Vlocity metadata in the same way as for the Salesforce metadata and commit the changes either to the repository or to a version control branch.

**Vlocity Version Supported:**\
**v. 1.17.1**\


#### **Integrate Vlocity as a plugin in ARM**

1. In the **Vlocity Configuration Settings** section, select the **Enable Vlocity** checkbox.
2. Next, select the various parameters required to integrate Vlocity with ARM:
   1. **Compile on Build:** When selected or set to true, the _compileonbuild_ code is modified in the YAML file, and the same gets committed to your Version Control branch during the EZ-Commit process. When you're trying to deploy to a Salesforce org using the above-configured branch, the compilation will take place before the deployment begins. **However, ARM recommends that you keep this checkbox unselected.** This is because the Vlocity tool throws compilation errors when you're trying to deploy data that doesn't have dependent components when **Compile on Build** is checked.
   2. **Auto Update Settings:** This option ensures you have the latest Data Pack settings before each export and deployment. This check is quick, and we recommend that you allow it.
   3. **Separate Matrix Versions:** Add the ability to export matrix versions separately.
   4. **Local Compilation:** To perform a local compilation of **FlexCard** and **OmniScript** metadata types, select this checkbox and enter the **Access Key** of Vlocity's private NPM repository to load the OmniStudio LWC compiler and deploy the compiled objects.

**Note:**

**If you do not have the NPM repository Access Key, you can request one from your Vlocity customer representative at**[ ](https://repo.vlocity/)[**https://repo.vlocity.com/repository/vlocity-public/**](https://repo.vlocity.com/repository/vlocity-public/) **by filing a support case with the subject Request for Access Key to Vlocity's Private NPM Repository.**

e.  **MaxDepth:** MaxDepth decides the level of dependencies that will be executed while fetching and committing Vlocity components. By default, MaxDepth is set to **-1**.

* When MaxDepth Values is set to **-1 means**, it will execute all-level dependencies of the selected data pack record.
* When MaxDepth Values is set to **0 means,** it will execute only the selected data pack record.
* When MaxDepth Values is set to **1 means**, it will execute only first-level 1 dependencies of the selected data pack record.

f. **Data Pack Types:** This gives you the option to choose the specific Vlocity components to be committed to your destination org/branch.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1695757390341.png)

3\. Click **Save.**
