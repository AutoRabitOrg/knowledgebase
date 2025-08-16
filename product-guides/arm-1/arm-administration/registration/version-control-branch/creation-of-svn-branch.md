# Creation of SVN Branch

Creating or registering a Subversion (SVN) branch in AutoRABIT (ARM) lets you isolate development work, manage parallel features, and automate deployments from that new branch. The steps below cover both **creating** a brand-new branch and **registering** an existing one so ARM can track commits, merges, and CI jobs against it.

***

## Creation of SVN Branch <a href="#creation-of-svn-branch" id="creation-of-svn-branch"></a>

1. Log in to **ARM**.
2. Open the **`VC Repo's`** tab.
3. Select the SVN repository where the new branch should live.
4.  Click **Create**.\


    <figure><img src="../../../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
5.  In the **Create Branch** dialog, enter a **Display Name**.

    {% hint style="info" %}
    **Allowed characters** – avoid **"//" \ , \* ? & ' " < > | \` \~ ( )** and **spaces** in the **Display Name**.
    {% endhint %}
6. Choose the appropriate **Credential** from the drop-down.
7. In **Branch URL**, append the new branch path to the parent branch (e.g., `branches/Development`).
8. **Parent URL** auto-populates from the repo; edit only if necessary.
9.  Click **Create** to finish.

    <figure><img src="../../../../../.gitbook/assets/image (693).png" alt="Create Branch form with Display Name, Branch URL, and Parent URL fields" width="563"><figcaption></figcaption></figure>

***

## Registration of an Existing SVN Branch <a href="#registration-of-an-existing-svn-branch" id="registration-of-an-existing-svn-branch"></a>

Already created a branch directly in SVN? Register it so ARM can use it in EZ-Commit and CI.

1.  In **`Repositories`**, select the SVN repository from the **List**.\


    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 9.00.25 PM (4).png" alt="" width="563"><figcaption></figcaption></figure>
2. Click **Register**.
3. Enter a **Display Name** for the branch.

{% hint style="info" %}
**Allowed characters** – avoid **"//" \ , \* ? & ' " < > | \` \~ ( )** and **spaces** in the **Display Name**.
{% endhint %}

4. The **Repository** root is pre-filled. In **Branch URL**, add the path to the existing branch (e.g., `branches/Integration`).
5. Set **Last Commit Date** – ARM will pull changes from Salesforce only after this timestamp in EZ-Commit.
6.  Click **Register**.

    <figure><img src="../../../../../.gitbook/assets/image (695).png" alt="Register Branch screen with Branch URL and Last Commit Date fields"><figcaption></figcaption></figure>
