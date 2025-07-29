# Connection & Authentication

## Azure Hosting Migration

To our valued Customer,&#x20;

AutoRABIT is working to modernize and standardize our infrastructure to provide a better experience for you, as we to innovate in our ARM product. &#x20;

As part of that effort, we are deprecating our Azure hosting option in September in favor of our standard AWS hosting offering, now that AWS provides service in the UAE, and will be migrating all the services (which will impact your tenant).&#x20;

This migration activity is planned for Sunday, September 28 (with a backup date of October 5), at 8:30AM (Dubai local time). The instance will be unavailable for up to 10 hours as we complete this activity.  &#x20;

We will also need your assistance to complete this migration. &#x20;

_**Your action (right away – if applicable) :**_&#x20;

Whitelist the following IP addresses for the new instance &#x20;

o        IP Addresses:&#x20;

_3.28.164.9_ \
&#xNAN;_&#x35;1.112.70.124_&#x20;

§     _Only needed if you have whitelisting in place for the current instance (for security purposes, or if required for your **Salesforce and GitHub, Gitlab, etc. related access)**_&#x20;

We will be providing a new login URL for the new instance; the following will need to be done in the new instance, closer to the migration date.:&#x20;

**Your Actions in the new instance**&#x20;

* Re-set up SSO if you are currently using it to access your account ([KB article](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/sso))&#x20;
* Re-set up your webhooks for the new URL ([KB Article](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/webhooks))&#x20;
* Re-Authenticate your Salesforce Org ([KB Article](https://knowledgebase.autorabit.com/product-guides/arm/registration/salesforce-org/salesforce-org-re-authentication))&#x20;
* Share the new instance URL with your team&#x20;

After the migration they will need to use the new link to access your account&#x20;

**What you need to know:**&#x20;

* There is no change to the application, nor will your data/configurations be impacted.
* During and post the migration activity, all data will stay in the UAE &#x20;
* We will set up a meeting, closer to the migration date, to review and coordinate the activities we identified.&#x20;
* If you need any help with preparing for this change: &#x20;
  * Technical assistance with completing any of the above activities -please submit a ticket via the support portal &#x20;
* Questions or concerns about the migration – please contact your Account Manager &#x20;

### How do I register GitHub repositories with two-factor authentication? <a href="#register-github-repositories-with-twofactor-authentication" id="register-github-repositories-with-twofactor-authentication"></a>

To use two-factor authentication in GitHub, create a personal access token first.

1. Create a personal access token and use it in place of a password when performing Git operations over HTTPS with GIT on the command line or the API. For detailed information, refer to [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2. Register your GitHub Repository in ARM using the same token.

### How do I rectify the GOLDENDOODLE vulnerability? <a href="#how-to-rectify-the-goldendoodle-vulnerability" id="how-to-rectify-the-goldendoodle-vulnerability"></a>

1. **Short-term solution**: Disable support for CBC encryption ciphers. Follow the procedures below to disable weak ciphers:
   * Run the following command to list the ciphers: \
     &#xNAN;**- sshd -T | grep ciphers | perl -pe 's/,/\n/g' | sort -u**
   * Edit the file **- /etc/ssh/sshd\_config** and add what strong ciphers you want to have or place in this file as shown in the example below- **Ciphers aes128-ctr,aes192-ctr,aes256-ctr**
   * Now, restart your sshd service using the command:  **service sshd restart**
2. **Long-term solution:** Enable the **TLS 1.3** protocol.

### Why am I not able to authenticate JIRA with my account? <a href="#why-am-i-not-able-to-authenticate-jira-with-my-account" id="why-am-i-not-able-to-authenticate-jira-with-my-account"></a>

Make sure you are entering the JIRA API token in the **Password** field while registering your JIRA plugin for the first time in the ARM application.

### How do I generate a new API token for JIRA? <a href="#steps-to-generate-api-token-for-jira" id="steps-to-generate-api-token-for-jira"></a>

Follow the steps below to generate a new API token for JIRA:

1. Go to the link: [https://id.atlassian.com/manage/api-tokens](https://id.atlassian.com/manage/api-tokens)**.**&#x20;
2. Click on **Create API Token** and provide the label name and click on **Create**.
3. Once the token is created, you will be able to see the **Your new API token** popup. Click on the **Copy to Clipboard**.
4. Use the copied token as a password for creating/updating the credential in AutoRABIT.
5. Once updated please use the same credential to authenticate the JIRA.

### How can I add a repository to AutoRABIT if one already exists? <a href="#how-can-i-add-a-repository-to-autorabit-if-one-already-exists" id="how-can-i-add-a-repository-to-autorabit-if-one-already-exists"></a>

Follow the below steps to register the repository:

* Log in to your repository and click on **Clone**. It will give you an _https_ and an _ssh_ link.
* To register the repository, copy the https link and paste it into ARM.
* Make sure the repo clone you see before https isn't included in the link you paste in ARM.
* Input the URL that begins with https.

### How does an SSH Key differ from an SSH Certificate? <a href="#how-does-ssh-key-differ-from-ssh-certificate" id="how-does-ssh-key-differ-from-ssh-certificate"></a>

While SSH Key-based authentication uses public key cryptography, SSH Certificate-based authentication attaches a signed certificate to each key to verify identity. By using a certificate signed by a trusted Certificate Authority, users can do away with the passwords (which are not secure, given that passwords can either be stolen or cracked via brute force) and leverage a partially automated trust-based certificate authentication process to gain access to systems.

### Why am I unable to register a GitHub repository using SSH keys and getting an 'invalid private key' error? <a href="#unable-to-register-github-repository-using-ssh-keys-and-getting-invalid-private-key-error" id="unable-to-register-github-repository-using-ssh-keys-and-getting-invalid-private-key-error"></a>

This is because you used invalid SSH keys to register your repository. Please use the correct SSH keys and try again.

### How do I validate the 'src' folder under branch settings? <a href="#how-to-validate-the-src-folder-under-branch-setting" id="how-to-validate-the-src-folder-under-branch-setting"></a>

When you try to create a new branch you must validate the master branch's **'src'** folder path, then select the parent branch as master, and the **'src'** folder path will be automatically set to the newly created branch.

