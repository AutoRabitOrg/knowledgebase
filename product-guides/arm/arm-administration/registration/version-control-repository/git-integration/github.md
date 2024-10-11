GitHub is a popular Git host. General instructions on connecting GitHub to ARM can be found in the section on [connecting to a version control repository](./README.md)

To connect securely from GitHub to ARM you may need a personal access token.

#### Creating a Personal Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

This section guides you through creating your personal access token directly on GitHub.

1. Log in to your GitHub account.
2. In the upper-right corner of any page, click your profile photo, then click **`Settings`**.

<figure><img src="../../../../../../.gitbook/assets/image (653).png" alt="" width="205"><figcaption></figcaption></figure>

3. In the left sidebar, click **`Developer settings`**.

<figure><img src="../../../../../../.gitbook/assets/image (654).png" alt="" width="225"><figcaption></figcaption></figure>

4. In the left sidebar, click **`Personal access tokens`**.

<figure><img src="../../../../../../.gitbook/assets/image (655).png" alt="" width="331"><figcaption></figcaption></figure>

5. Click **`Generate new token`**.

<figure><img src="../../../../../../.gitbook/assets/image (656).png" alt=""><figcaption></figcaption></figure>

6. Give your token a descriptive name.

<figure><img src="../../../../../../.gitbook/assets/image (657).png" alt=""><figcaption></figcaption></figure>

7. Select the scopes or permissions you want to grant this token. Select **`repo`** to use your token to access repositories from the command line.

<figure><img src="../../../../../../.gitbook/assets/image (658).png" alt="" width="563"><figcaption></figcaption></figure>

8. Click **`Generate token`**.

<figure><img src="../../../../../../.gitbook/assets/image (659).png" alt="" width="563"><figcaption></figcaption></figure>

9. Click![](<../../../../../../.gitbook/assets/image (660).png>)to copy the token to your clipboard. You cannot see the token again after navigating off the page for security reasons.

<figure><img src="../../../../../../.gitbook/assets/image (661).png" alt="" width="563"><figcaption></figcaption></figure>

10. Use the copied token as a password for creating/updating the credential in ARM.
11. Once updated, please use the same credential to authenticate the Git.

{% hint style="info" %}
**Important Note:** Treat your tokens like passwords and keep them secret. When working with the API, use tokens as environment variables instead of hardcoding them into your programs.
{% endhint %}
