# Vlocity Configuration Settings

Vlocity integration with ARM allows you to retrieve and deploy Vlocity metadata in the same way as for the Salesforce metadata and commit the changes either to the repository or to a version control branch.

**Vlocity Version Supported:**\
**v. 1.17.1**

#### **Integrate Vlocity as a plugin in ARM**

1. In the **Vlocity Configuration Settings** section, select the **Enable Vlocity** checkbox.
2.  Next, select the various parameters required to integrate Vlocity with ARM:

    * **Compile on Build:** When selected or set to true, the _compileonbuild_ code is modified in the YAML file, and the same gets committed to your Version Control branch during the EZ-Commit process. When you're trying to deploy to a Salesforce org using the above-configured branch, the compilation will take place before the deployment begins. **However, ARM recommends that you keep this checkbox unselected.** This is because the Vlocity tool throws compilation errors when you're trying to deploy data that doesn't have dependent components when **Compile on Build** is checked.
    * **Auto Update Settings:** This option ensures you have the latest Data Pack settings before each export and deployment. This check is quick, and we recommend that you allow it.
    * **Separate Matrix Versions:** Add the ability to export matrix versions separately.
    * **Local Compilation:** To perform a local compilation of **FlexCard** and **OmniScript** metadata types, select this checkbox and enter the **Access Key** of Vlocity's private NPM repository to load the OmniStudio LWC compiler and deploy the compiled objects.

    **`Note:`**`If you do not have the NPM repository Access Key, you can request one from your Vlocity customer representative at`[ ](https://repo.vlocity/)[`https://repo.vlocity.com/repository/vlocity-public/`](https://repo.vlocity.com/repository/vlocity-public/) `by filing a support case with the subject Request for Access Key to Vlocity's Private NPM Repository.`

    * **MaxDepth:** MaxDepth decides the level of dependencies that will be executed while fetching and committing Vlocity components. By default, MaxDepth is set to **-1**.
      1. When MaxDepth Values is set to **-1 means**, it will execute all-level dependencies of the selected data pack record.
      2. When MaxDepth Values is set to **0 means,** it will execute only the selected data pack record.
      3. When MaxDepth Values is set to **1 means**, it will execute only first-level 1 dependencies of the selected data pack record.
    * **Local Compilation:** To perform a local compilation of **FlexCard** and **OmniScript** metadata types, select this checkbox and enter the **Access Key** of Vlocity's private NPM repository to load the OmniStudio LWC compiler and deploy the compiled objects.
    * **Data Pack Types:** This gives you the option to choose the specific Vlocity components to be committed to your destination org/branch.

    <figure><img src="../../../../.gitbook/assets/image (60) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3\. Click **Save.**
