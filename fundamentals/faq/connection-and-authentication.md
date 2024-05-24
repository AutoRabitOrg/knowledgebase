# Connection & Authentication

#### Register GitHub repositories with two-factor authentication <a href="#register-github-repositories-with-twofactor-authentication" id="register-github-repositories-with-twofactor-authentication"></a>

To use two-factor authentication in GitHub, you need to create a personal access token first.

1. Create a personal access token, and use it in place of a password when performing Git operations over HTTPS with GIT on the command line or the API. For detailed information, refer to [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
2. Register GitHub Repository in ARM using the same token.

#### How to rectify the GOLDENDOODLE vulnerability? <a href="#how-to-rectify-the-goldendoodle-vulnerability" id="how-to-rectify-the-goldendoodle-vulnerability"></a>

1. **Short-term solution**: Disable support for CBC encryption ciphers. Follow the below procedure to disable weak ciphers:
   * Run the following command to list the ciphers: **- sshd -T | grep ciphers | perl -pe 's/,/\n/g' | sort -u**
   * Edit the file **- /etc/ssh/sshd\_config** and add what all strong ciphers you want to have or place in this file as shown in the example below- **Ciphers aes128-ctr,aes192-ctr,aes256-ctr**
   * Now, restart your sshd service using the command:  **service sshd restart**
2. **Long-term solution:** Enable the **TLS 1.3** protocol.

#### Why does AutoRABIT need to install GDM (Gnome Desktop Manager) on the virtual machine of the client? <a href="#why-does-autorabit-need-to-install-gdm-gnome-desktop-manager-on-the-virtual-machine-of-the-client" id="why-does-autorabit-need-to-install-gdm-gnome-desktop-manager-on-the-virtual-machine-of-the-client"></a>

1. To run selenium scripts in the TAF module of the ARM application, GDM is necessary.
2. It will not affect Version Control, however it may have an influence on the CI Job module.

#### Why am I not able to authenticate JIRA with my account? <a href="#why-am-i-not-able-to-authenticate-jira-with-my-account" id="why-am-i-not-able-to-authenticate-jira-with-my-account"></a>

Make sure you are entering the JIRA API token in the **Password** field while registering JIRA plugin for the first time in the ARM application.

#### Steps to generate API token for JIRA <a href="#steps-to-generate-api-token-for-jira" id="steps-to-generate-api-token-for-jira"></a>

Follow the below steps to generate a new API token for JIRA:

1. Go to the link: **https://id.atlassian.com/manage/api-tokens**
2. Click on **Create API Token** and provide the label name and click on **Create**.
3. Once the token got created, you will be able to see the **Your new API token** popup, click on the **Copy to Clipboard**.
4. Use the copied token as a password for creating/updating the credential in AutoRABIT.
5. Once updated please use the same credential to authenticate the JIRA.

#### How can I add a repository to AutoRABIT if one already exists? <a href="#how-can-i-add-a-repository-to-autorabit-if-one-already-exists" id="how-can-i-add-a-repository-to-autorabit-if-one-already-exists"></a>

Follow the below steps to register the repository:

* Login to your repository and click on **Clone**. It will give you a _https_ and a _ssh_ link.
* To register the repository, copy the https link and paste it into ARM.
* Make sure the repo clone you see before https isn't included in the link you paste into ARM.
* You will just need to input the URL that begins with https.

#### Unable to register GitHub repository using SSH keys and getting invalid private key error. <a href="#unable-to-register-github-repository-using-ssh-keys-and-getting-invalid-private-key-error" id="unable-to-register-github-repository-using-ssh-keys-and-getting-invalid-private-key-error"></a>

This is because you used invalid SSH keys to register your repository. Please use the correct SSH keys and try again.

#### How to validate the 'src' folder under branch setting? <a href="#how-to-validate-the-src-folder-under-branch-setting" id="how-to-validate-the-src-folder-under-branch-setting"></a>

When you try to create a new branch you must validate the master branch's **'src'** folder path, then select the parent branch as master, and the **'src'** folder path will be automatically set to the newly created branch.

#### How does SSH Key differ from SSH Certificate? <a href="#how-does-ssh-key-differ-from-ssh-certificate" id="how-does-ssh-key-differ-from-ssh-certificate"></a>

While SSH Key-based authentication uses public key cryptography, SSH Certificate-based authentication attaches a signed certificate to each key to verify their identities. By using a certificate signed by a trusted Certificate Authority, users can do away with the passwords (which are not secure, given that passwords can either be stolen or cracked via brute force) and leverage a partially automated trust-based certificate authentication process to gain access to systems.
