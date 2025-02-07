# Cloud Errors and Solutions

## CodeScan Cloud

## Common Errors and Solutions

### Can the status of issues marked as False Positives in the lower environment be transferred when the scan is triggered in the higher environment?

Issues in standalone branches are treated separately. The status can only be transferred if the Develop branch is a comparison or pull request branch using ProductionReady as the target.

### Why am I getting the error 'Background tasks failing'?&#x20;

This error either occurs if it’s out of memory or when multiple analyses have been triggered at the same time. The analysis triggered last gets completed first.

CodeScan is based on SonarQube™, an open-source reporting platform for coding languages. The Background Tasks that occur when an analysis report is run have been added by SonarQube™ to allow administrators to view technical details about why the processes fail.

To learn more about background tasks, please see the [SonarQube Documentation - Background Tasks](https://docs.sonarqube.org/latest/analysis/background-tasks/).

### Why am I getting an 'Expired Token' error on my project analysis?

Errors such as **Expired Token** on your **Project Analysis** page can sometimes be fixed by resetting the link to your code repository. CodeScan Cloud allows you to do this _without erasing_ the historical data present in your project.

To fix the above errors, follow the steps below to delete the **Analysis Project:**

1. Go to your **Project** and navigate to the **Project Settings > Project Analysis** page.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FjlDAU3lF0sY4VQsT4Amc%252Fimage.png%3Falt%3Dmedia%26token%3Da83ff6b8-3921-4780-a600-73a0528c8939&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=d695dae8&#x26;sv=2" alt=""><figcaption></figcaption></figure>

2. Click on **Delete Analysis**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FPtvecOs4DvxVfhklOlef%252Fimage.png%3Falt%3Dmedia%26token%3Df4d35269-1eb4-49f7-8007-af7e0fa941a9&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f45c5862&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. Make sure you do not have the "**Delete this project also?**" box checked. This will delete your history and is not reversible. Click **Delete Analysis**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FJQlratKw4gNSM78oJO9Q%252Fimage.png%3Falt%3Dmedia%26token%3D31789e6a-a83f-4f4c-b574-98780d28369a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=7cba9d7&#x26;sv=2" alt=""><figcaption></figcaption></figure>

4. Now, use the **Attach Analysis Project** button at the top right of the screen to add the link.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F9XV4FEd05jMN8noFpwM5%252Fimage.png%3Falt%3Dmedia%26token%3D8b92e06d-42f3-4bb4-b3cd-19d8229ff517&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2629d7d2&#x26;sv=2" alt=""><figcaption></figcaption></figure>

5. You will now see a new popup window. Select the required option from the options given.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F6g1URPxNdZlPF25SLpqv%252Fimage.png%3Falt%3Dmedia%26token%3D263b9688-7e35-42d3-ba2d-5ea8690e30ed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6a62fae2&#x26;sv=2" alt=""><figcaption></figcaption></figure>

6. Rerun the request.

### Why am I getting an 'inactive user' error message?

Sometimes, an "**Inactive user**" error may appear at the start of an analysis:

![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FUlxMqF9eZjJVggBcOMjb%252Fimage.png%3Falt%3Dmedia%26token%3Dad01ad32-cb59-4bbf-9fba-eca99ed41eb2\&width=768\&dpr=4\&quality=100\&sign=b0b3b0ba\&sv=2)

This could be caused because the user who created the project and provided credentials for it:

* Is no longer a member of the team and was removed.
* Had their permissions changed in CodeScan.
* Had their permissions changed in the repo/environment that is scanned.

To resolve the “**Inactive user**“ issue, you need to reattach the project—without deleting its history.

Follow these steps:

1. Delete the project analysis:

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FVHZkjz1ZwMnN2M1yKWH1%252Fimage.png%3Falt%3Dmedia%26token%3D9bd14e0f-f243-497f-8278-addd4a5332fe&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=1f0315a4&#x26;sv=2" alt=""><figcaption></figcaption></figure>

**Important!** Do **not** select the checkbox to '**Delete Project also?'** if you want to keep the current project and its history:

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FT9x5wKokEeJl9EVROsWp%252Fimage.png%3Falt%3Dmedia%26token%3Dc8c35fc2-a285-4928-be5e-b53d9bb2516f&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=61a3418c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

2. Reattach analysis:

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FkMD8jvNvSntFehn4CTKF%252Fimage.png%3Falt%3Dmedia%26token%3D3f6418d3-dcd8-4d6d-8db0-096689ec6dad&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a7be57d8&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. Provide repo/environment credentials:

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FecrzFoDeeZxtKyFmhdGs%252Fimage.png%3Falt%3Dmedia%26token%3Dadf6ffb3-ce85-4685-bd26-44cc4a88e69a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=3d7c071f&#x26;sv=2" alt=""><figcaption></figcaption></figure>

4. Rerun the SCA; it should succeed.

If the steps above were completed but the issue persists, contact [support@autorabit.com](mailto:support@autorabit.com).

### Why am I getting an 'ip restricted' message?

![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FfstI2XxSk8CuRCJWmCAc%252Fimage.png%3Falt%3Dmedia%26token%3D956a5ef0-a01d-467c-82ec-32716edcc55b\&width=768\&dpr=4\&quality=100\&sign=542c3c22\&sv=2)

The **IP restricted** issue can be solved by relaxing the IP restrictions for the CodeScan connected app in the org you are trying to scan.

To do this follow the below steps:

1. Log in to the org you are trying to scan.
2. Go to **Setup** and search for **Connected Apps OAuth Usage**.
3. Install the app that is making the scan (_CodeScan Cloud_ or _CodeScan Quick Reports_).
4. Click **Manage App Policies** and then **Edit Policies**.
5. Under **IP Relaxation** select **Relax IP Restrictions**.
6. Rerun the scan.

### Why is my Commit and Merge failing with the following SonarScanner error but still allowing submission: 'Language of file force-app/main/default/permissionsets/abc\_filename.permissionset-metaxml' can not be decided as the file matches patterns of both sonar.lang.patterns.mule: \*\*/\*abcd,\*\*/\*xml and sonar.lanq.patterns.sfmeta: \*\*/\*profile-meta.xml.\*\*/\*permissionset-meta.xml.\*\*/\*settings-meta.xml.\*\*/\*abject-metaxml.z\*/\*field-meta.xmll\*s/\*fiow-meta.xml.\*\*/\*sharingrules-meta.xml.\*\*/\*workflow-meta.xml\*\*/\*profilesessionsetting-meta.xml \*\*/\*profilepasswordpolicy-meta.xml.\*\*/\*.profile，\*\*/\*.permissionset，\*\*/\*.settings.\*\*/\*.object.\*\*/\*.flow，\*\*/\*.sharingrules，\*\*/\*warkflow\*\*/\*.profilesessionsetting，\*\*/\*.profilepassvordpolicy'?

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FgBRBEhfLgCocTQGUbyJT%252Fimage.png%3Falt%3Dmedia%26token%3D43e5fbe8-4e8d-4201-a4ea-a43a944d77c6&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=394d5661&#x26;sv=2" alt=""><figcaption></figcaption></figure>

**Environment configuration checklist**

Configure the Mule setting (Key: sonar.mule.file.suffixes) with values ".abcd" and ".xml," which are causing errors. Navigate to the project where this error occurs in CodeScan. Go to **Project Settings > General Settings**, and search for "mule" in the search box. Remove ".xml".

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FuE01vFHzeO7wnUDt0FF2%252Fimage.png%3Falt%3Dmedia%26token%3Df91eb0c2-fa66-448b-92f8-f5eb97908453&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=e9105416&#x26;sv=2" alt=""><figcaption></figcaption></figure>

By adjusting these settings in CodeScan, the SCA will not fail.

### Why am I getting a 'Packfile is truncated' error?

While analyzing the project, you may encounter a “Packfile is truncated” error. Initially, access to CodeScan was denied on GitHub.&#x20;

1. **Check Access:** Verify if you have the necessary access to CodeScan in GitHub.
2. **Grant Access:** If access is denied, request and obtain the required permissions for CodeScan.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FtBr5qh68WOHLi6xxUuMk%252Fimage.png%3Falt%3Dmedia%26token%3D5c13835b-da26-4a57-9e5b-f2811adfab2b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a4c1dec5&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. **Retry Analysis:** After granting access to CodeScan in GitHub and integrating it with CodeScan, start the connection, then reattempt the project analysis. The error should no longer appear. The repositories should be synced. CodeScan should indicate the analysis was triggered, and the user should see the issues.

### Why am I getting the error: 'Project reports are not available for branches created outside the CodeScan Cloud'?

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FjmxYnLe4X2u5Mjuk1mP6%252Fimage.png%3Falt%3Dmedia%26token%3Dcbbc4a69-1f13-4096-97e1-bf38a8c3ddd8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2c9917e1&#x26;sv=2" alt=""><figcaption><p>Error Message</p></figcaption></figure>

For branches created outside the CodeScan Cloud, such as ARM, Flosum, or Copado, project reports are not yet accessible. Only the branch chosen during the initial integration setup with CodeScan Cloud can have reports fetched in CodeScan.

In the **Edit Project** section, select **“Attach Analysis Project,”** and choose the project type as **“Webhook.”**

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FXfgm8cx3eZXsXWEo8LR5%252Fimage.png%3Falt%3Dmedia%26token%3Dd55cec61-a520-440d-af9c-4a9be4e5277a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b8774736&#x26;sv=2" alt=""><figcaption><p>Project Analysis page</p></figcaption></figure>

After this step, project reports will be accessible.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FMO1JR4tsfUSL7qumqUkH%252Fimage.png%3Falt%3Dmedia%26token%3Da564a6d6-3879-4873-b4d7-39817d99a064&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=83274c30&#x26;sv=2" alt=""><figcaption><p>Project Report page</p></figcaption></figure>

### Why am I getting the error: 'Salesforce returned an unexpected result'?

The Salesforce Enhanced Domains feature was rolled out to Sandboxes on August 26, 2022, and available on September 9 for all environments.

If your CodeScan Cloud Salesforce project was linked to a Sandbox or Org that this feature is enabled in, you will need to reattach your project analysis.

[CodeScan Cloud](https://www.codescan.io/products/cloud/) allows you to do this _without erasing_ the historical data present in your project.

To fix the above errors, first you need to delete the **Analysis Project**, to delete follow the steps below:

1. Go to your **Project** and navigate to the **Project Settings > Project Analysis** page.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F9z5szRXVzz06mcunqfeo%252Fimage.png%3Falt%3Dmedia%26token%3Da96e3cb7-af1d-4ae9-a843-c94482c67474&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=9a71d326&#x26;sv=2" alt=""><figcaption><p>CodeScan screenshot</p></figcaption></figure>

2. Click on **Delete Analysis**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FOYA7k37lrCMTNJrbDriH%252Fimage.png%3Falt%3Dmedia%26token%3D6fc4ce1b-d7e2-460a-8745-3879f26ca7cd&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5c016941&#x26;sv=2" alt=""><figcaption><p>Delete Analysis screenshot</p></figcaption></figure>

3. Make sure you do not have the "**Delete this project also?**" box checked. This will delete your history and is not reversible. Click **Delete Analysis**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F5xNukWwAWVbeaJfIH0uC%252Fimage.png%3Falt%3Dmedia%26token%3Dde98d291-38d7-4b45-872d-c9e9d1a3bc33&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6ece50ef&#x26;sv=2" alt=""><figcaption><p>Delete Analysis project checkbox</p></figcaption></figure>

4. Now use the **Attach Analysis Project** button at the top right of the screen to re-add the link.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FzjE3ULDdSHCl6RdnnkJq%252Fimage.png%3Falt%3Dmedia%26token%3D0092887f-780d-4796-b68e-2d10f2ac1b81&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=8263b3d7&#x26;sv=2" alt=""><figcaption><p>Attach Analysis Project</p></figcaption></figure>

5. &#x20;Configure the project and run the analysis.

### Why am I getting a unit test timeout?&#x20;

In CodeScan Cloud, the default setting for unit test timeouts is 1 hour (3,600 seconds). For Orgs and Sandboxes with a large number of tests, this can be insufficient. To increase the timeout, click on your project and then navigate to **Overview > Project Settings > General settings**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252Fv3LJPVcqQJHgdwGWRCHj%252Fimage.png%3Falt%3Dmedia%26token%3D997da7b2-9f1f-4dd3-afe1-d733748d84e7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b04741e1&#x26;sv=2" alt=""><figcaption></figcaption></figure>

In General Settings, click on the **CodeScan** tab on the left and edit the timeout under the **Unit Test timeout**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F8udG8vy8Ymz3W6eHO9iR%252Fimage.png%3Falt%3Dmedia%26token%3Dd1f6976f-f328-4fb2-a847-c3c908a5eb8a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=35d822ee&#x26;sv=2" alt=""><figcaption></figcaption></figure>
