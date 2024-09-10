# 'Inactive users' error is thrown while accessing CodeScan projects

Sometimes, an "**Inactive user**" error may appear upon analysis start:

![](../../../../.gitbook/assets/image.png)

It could be caused by the following scenarios, in which the user who created the project and provided credentials for it:

* is no longer a member of the team and was removed
* had their permissions changed in CodeScan
* had their permissions changed in repo/environment which is scanned

To resolve the “**Inactive user**“ issue, you would need to reattach the project (without deleting its history).

Please follow these steps:

1. Delete project analysis:

![](<../../../../.gitbook/assets/image (1).png>)

**Important!** Don’t select '**Delete Project also?'** if you want to keep the current project and its history:

![](<../../../../.gitbook/assets/image (2).png>)

2. Reattach analysis:

![](<../../../../.gitbook/assets/image (3).png>)

3. Provide repo/ environment credentials:

![](<../../../../.gitbook/assets/image (4).png>)

4. Rerun SCA, it should succeed

If all the steps above were completed, but issue persists, please reach out to [support@autorabit.com](mailto:support@autorabit.com)
