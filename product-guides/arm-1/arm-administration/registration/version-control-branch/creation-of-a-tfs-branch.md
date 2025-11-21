# Creation of a TFS Branch

### Creation of a TFS Branch <a href="#creation-of-a-tfs-branch" id="creation-of-a-tfs-branch"></a>

1. Log in to your ARM account.
2. Go to the **`Repositories`**`tab.`
3. Select the TFS repository for which the branch needs to be created.
4.  Click on **`Create`** button.<br>

    <figure><img src="../../../../../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>
5. In the **`Create Branch`** screen, enter a branch name in the **`Display Name`**&#x66;ield.

{% hint style="info" %}
**Point to Note:** The characters **"//" \ , \* ? & ' " < > | \` \~ ( )** and **space** are not allowed in the **`Display Name`** field.
{% endhint %}

6. Select your **`Credential`** from the drop-down field.
7. Under the **`Target URL`** field, do the following:
   * The **`Repository`** field is auto-filled.
   * Enter your **`Project Name`**.
   * Enter your **`Branch`** name.
8. Under the **`Parent URL`** field, do the following:
   * The **`Repository`** field is auto-filled.
   * Enter the **`Project Name`** from which data is to be fetched.
   * Enter your **`Branch`** name.
9. Click **`Create`**.

<figure><img src="../../../../../.gitbook/assets/image (689).png" alt="" width="563"><figcaption></figcaption></figure>

### Registration of an existing TFS branch <a href="#registration-of-an-existing-tfs-branch" id="registration-of-an-existing-tfs-branch"></a>

1. On the **`Repositories`** page, select a TFS repository from the list.
2.  Click on **`Register`**.<br>

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 9.00.25 PM (3).png" alt="" width="563"><figcaption></figcaption></figure>
3. On the next screen, enter the **`Display Name`** of the branch that you want to register in ARM.

{% hint style="info" %}
**Point to Note:** The characters **"//" \ , \* ? & ' " < > | \` \~ ( )** and **space** are not allowed in the **`Display Name`** field.
{% endhint %}

4. The **`Repository`** field is auto-filled with the URL entered when registering the repository.
5. Select the **`Last Commit Date`**. The last commit date fetches changes from Salesforce org in EZ-Commit based on the specified date.
6. Click **`Register`** to complete the registration of the branch.

<figure><img src="../../../../../.gitbook/assets/image (691).png" alt=""><figcaption></figcaption></figure>
