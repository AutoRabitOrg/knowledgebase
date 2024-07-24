# Understanding branches in CodeScan Cloud

Branches allow you to keep track of changes that may affect the branch to which your project is linked. There are two types of branches:

1. **Long lived branches** allow you to see the entire dashboard and history of your project.
2. **Short lived branches** allow you to see the delta in issues between your branch and your master/production/target.

#### GitHub and Bitbucket <a href="#github-and-bitbucket" id="github-and-bitbucket"></a>

When creating an analysis project from GitHub or Bitbucket repository in [CodeScanCloud](https://www.codescan.io/products/cloud/), you will be asked to choose the branch to which the project is linked. This branch will become your main branch. If you also select **Check Pull requests**, any changes that affect this main branch will be reflected in the project with the branch functionality.

#### Pull Requests <a href="#pull-requests" id="pull-requests"></a>

If you have set your main branch to master, any relevant pull request will be analyzed when it is created and updated every time. The results will be displayed on the same page as your main branch analysis under the branches’ dropdown menu.

#### Salesforce <a href="#salesforce" id="salesforce"></a>

This topic is covered in a separate article. Click [here](https://knowledgebase.autorabit.com/codescan/docs/understanding-branches-for-salesforce-project) to go to the related article.

#### Visual Studio Team Services (VSTS) <a href="#visual-studio-team-services-vsts" id="visual-studio-team-services-vsts"></a>

When a pull request is created in a VSTS repository or a repository tracked by your VSTS Build Definition, a new branch will be created on your CodeScan Cloud project. Please note that any remote repositories must have _Continuous Integration_ and _Pull Request Validation_ checked for the appropriate branches in the **Build Definition’s Triggers** menu.

#### Managing branches <a href="#managing-branches" id="managing-branches"></a>

On your **Project Analysis** page, go to **Project Setting > Branches and Pull requests**. This page allows users to delete any new branches and also change the branch that the Analysis Project is checking.

<figure><img src="../../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="450"><figcaption></figcaption></figure>

* **Delete Branch**: To delete a branch, click the (![](<../../../../.gitbook/assets/image (64) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) button next to the branch and click **Delete Branch**.

<figure><img src="../../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Rename Branch**: To change the branch that the Analysis Project is tracking, click the (![](<../../../../.gitbook/assets/image (65) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon next to the main branch and click **Rename Branch**. Enter the name of the branch you would like to begin tracking. Changes will only be reflected on the project’s Overview page once the analysis has been performed.

<figure><img src="../../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Comparing Branches <a href="#comparing-branches" id="comparing-branches"></a>

<figure><img src="../../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Here you can see the branch has four new violations. If the branch is selected, the details of the violation(s) can be seen. All new branches added in this way will be deleted in **30 days** if they are not analyzed.

If you have any further questions about CodeScan Cloud, please [contact us](https://www.codescan.io/contact/).
