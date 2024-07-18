# Understanding branches for Salesforce project

When you create an analysis project from Salesforce, the org or sandbox you authorize, will become your main branch. You can add your sandboxes as analysis project branches by editing your project (from the **Project Analysis** page). This allows for easy comparison between the production orgs or sandboxes and is especially good for checking features before production.

1. Select your Salesforce project from the **My Projects** screen.
2. Go to the **More** tab and select **Project Analysis** from the dropdown.

<figure><img src="../../../../.gitbook/assets/image (52) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Click on **Edit Project**.

<figure><img src="../../../../.gitbook/assets/image (53) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Click on![](<../../../../.gitbook/assets/image (55) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)button to add a new branch.

<figure><img src="../../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="389"><figcaption></figcaption></figure>

5.  Assign a name to your branch and choose the branch type:

    * **Comparison Branch**- This branch determines only the recent issues in a project branch based on comparing with the standard branch in your project.
    * **Standard Branch**- This branch will have your project's entire history and dashboards.

    <figure><img src="../../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="482"><figcaption></figcaption></figure>
6. Select your Salesforce environment.
7. Once you click on **Authorize**, it will redirect you to the Salesforce login page to validate your credentials.
8. This triggers the project analysis and the project being added under your CodeScan organization.
9. You'll be redirected to the **Project Analysis** screen, where you can view the status of your triggered analysis.

<figure><img src="../../../../.gitbook/assets/image (51) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### Features of a comparison branch <a href="#features-of-a-comparison-branch" id="features-of-a-comparison-branch"></a>

When you create a comparison branch, the issues shown are only the new ones in that branch, not the general issues you see in the project's main branch.

The property below is responsible for changing the UI labels and texts from _Pull Requests_ to _Comparison Branches_.

```
codescan.comparison.branches
```

{% hint style="info" %}
**Note:** The `codescan.comparison.branches` property is in OFF state by default.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (56) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

The comparison branches feature is enabled automatically when you:

* create new comparison branch via CodeScan user interface inside project with Salesforce as the integration type or,
* run sonar-scanner or CodeScan SFDX utility with these two new scanner properties:

> \-Dsonar.comparison.branch=...\
> \-Dsonar.comparison.base=...

Another way is via _Autorabit-CodeScan_ integration.

The new properties `sonar.comparison.branch` and `sonar.comparison.base` are equivalents/aliases of these existing two: `sonar.pullrequest.branch` and `sonar.pullrequest.base`.

So, because they are equivalents - the logic will be the same. If you mark any issue as `False Positive` or `Resolve as Won't fix` in your Comparison Branch, then this issue will not re-appear in the project's main branch after changes are merged.\
Similarly, the new comparison branches reflect the changes on issues made by the user on the project’s main branch.

<figure><img src="../../../../.gitbook/assets/image (57) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

To test the new feature using sonar-scanner:

1. Execute the initial analysis on base branch using the below command:

```
sonar-scanner -Dsonar.host.url=https://app.codescan.io -Dsonar.organization=<org-id>
-Dsonar.projectKey=<project-key> -Dsonar.login=<security-token>
```

2. Execute analysis on a comparison branch:

```
sonar-scanner -Dsonar.host.url=https://app.codescan.io -Dsonar.comparison.branch=<comparison-branch-name>
-Dsonar.comparison.base=<base-branch-name> -Dsonar.organization=<org-id> -Dsonar.projectKey=<project-key>
-Dsonar.login=<security-token>
```

### Managing branches <a href="#managing-branches" id="managing-branches"></a>

On your **Project Analysis** page, go to **Project Setting > Branches**.

<figure><img src="../../../../.gitbook/assets/image (58) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="323"><figcaption></figcaption></figure>

On this page, you can:

* View the branches you have created and segregated into master branches (including standalone branches) and comparison branches in two different tabs.
* Delete all the branches except the main branch.
* Renaming of the branch applies only to the main branch.

#### Delete a branch <a href="#delete-a-branch" id="delete-a-branch"></a>

For example, to delete a comparison branch, navigate to the **Comparisons Branches** tab, click on ![](<../../../../.gitbook/assets/image (59) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon and click on **Delete Comparison Branch**. Note that this process cannot be undone.

<figure><img src="../../../../.gitbook/assets/image (61) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Rename the main branch <a href="#rename-the-main-branch" id="rename-the-main-branch"></a>

To update the name of the main branch, navigate to the **Branches** tab, and look for the main branch.\
Click on![](<../../../../.gitbook/assets/image (60) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)icon under the **Actions** tab and click on **Rename branch**.

<figure><img src="../../../../.gitbook/assets/image (62) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Give the main branch a new name and click on **Rename**.

#### Comparing Branches <a href="#comparing-branches" id="comparing-branches"></a>

<figure><img src="../../../../.gitbook/assets/image (63) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

1. Select your Salesforce project from the **My Projects** page.
2. When you click on the main branch dropdown for your project, you can see the list of all branches that you have created or added.
3. If there are any violations for your branch, such details will appear. If you click on a branch, the details of the violations can be seen on the **Quality Gate Status** screen.

{% hint style="info" %}
**Important Note:**&#x20;

All new branches added in this way will be deleted in **30 days** if they are not analyzed again. If you have any further questions about CodeScan Cloud, please [contact us](https://www.codescan.io/contact/).
{% endhint %}
