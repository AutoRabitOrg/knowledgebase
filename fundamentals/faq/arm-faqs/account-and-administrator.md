# Account & Administrator

{% hint style="info" %}
Use the AI search feature to find answers to your AutoRABIT questions. In the future, FAQs will no longer be updated on these pages; instead, they will be integrated into the Product Guide pages by associated topic.
{% endhint %}

## How can I view my organization-related support tickets in AutoRABIT? <a href="#how-can-i-view-my-organizationrelated-support-tickets-in-autorabit" id="how-can-i-view-my-organizationrelated-support-tickets-in-autorabit"></a>

To view your support ticket and its status, follow the steps below:

1. Log in to your ARM instance.
2. At the top of the page, navigate to **Quick Links > Help Center**. You'll be redirected to the ARM Support Dashboard page.
3.  Navigate to **Teams Queue** under **Tickets**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-VT7TJLCO.png" alt=""><figcaption></figcaption></figure>

Now you will be able to view your org-related tickets here.

### Why am I unable to log in to my ARM account? <a href="#unable-to-login-into-my-arm-account" id="unable-to-login-into-my-arm-account"></a>

If you're having trouble logging into your AutoRABIT account, here are some things you can try.

1. **The account is not created**: Please check with AutoRABIT admin for creating a new account
2. **The User ID and Password supplied to access the AutoRABIT account were incorrect or invalid**: Try resetting the password by following the instructions [here](https://knowledgebase.autorabit.com/product-guides/arm/arm-administration/user-management/reset-account-password).
3. **Check if your account subscription has expired or your account is disabled**: If your AutoRABIT account has been disabled, you'll see a message saying your account is disabled when you try to log in.
4. If you get the following error **“getAttribute: Session already invalidated"**, try clearing your browser cache.
5. **Restriction of your IP address**: Verify with your network team internally and verify if there are any issues or restrictions for your IP address from the network side.
6. If nothing works out, please reach out to us by raising a [Support Ticket](https://support.autorabit.com/portal/en/home)

### Why did I not receive the email to reset my account password? <a href="#not-receiving-email-to-reset-your-account-password" id="not-receiving-email-to-reset-your-account-password"></a>

If you requested a new password but didn't receive your password reset email, then:

1. Check the **spam** or **junk** email folder in your email accounts linked to your AutoRABIT account.
2. Try to **reset your password** again.

### What factors should I consider when modifying or resetting my account password? <a href="#what-are-the-factors-i-should-consider-when-modifying-or-resetting-my-account-password" id="what-are-the-factors-i-should-consider-when-modifying-or-resetting-my-account-password"></a>

#### **Password Requirements:**

1. MUST contain at least **10 characters** (12+ recommended)
2. MUST contain at least **one uppercase** letter (A-Z)
3. MUST contain at least **one lowercase** letter (a-z)
4. MUST contain at least **one number** (0-9)
5. MUST contain at least **one special** character (such as !, %, @, <, >, # and so on)
6. MUST NOT contain an email address, first, middle or last name, or commonly used passwords
7. MUST NOT be one of the **5 previously used** passwords

### How often do I have to change my password for the ARM application? <a href="#how-often-do-i-have-to-change-my-password-for-the-arm-application" id="how-often-do-i-have-to-change-my-password-for-the-arm-application"></a>

ARM has a 90-day rotational policy that requires you to change your password every 90 days. Follow the instructions [here](../../../product-guides/arm/arm-administration/user-management/reset-account-password.md) to reset your ARM password.

### \*\*Why am I unable to register my Salesforce Org using an OAuth connection? <a href="#why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection" id="why-am-i-unable-to-register-my-salesforce-org-using-an-oauth-connection"></a>

1. Verify in the user Salesforce Org if the AutoRABIT Connected App is **“Blocked”** and unblock it.
2. Verify in user Salesforce Org if there are any specific permissions set for the Connected App.
3. Verify whether the redirect URL, client ID, and the secret key in **oauth.properties** file (path: .rabit/org/oauth.properties) are valid.

If the user is on a proxy-enabled server and receives an error such as **"Username may not be null"**, the proxy credentials must be validated. If the proxy username is set to **"null"**, the above error will occur.

### How will I track all the support tickets that I have created in ARM? <a href="#how-will-i-track-all-the-support-tickets-that-i-have-created-in-arm" id="how-will-i-track-all-the-support-tickets-that-i-have-created-in-arm"></a>

View all your support tickets via **Quick Links > Help Center** from the ARM application which redirects to the Support portal page where you can see the list of open cases created by you or by your team.

### \*\*Which version of TLS does ARM run? <a href="#which-version-of-tls-does-arm-run" id="which-version-of-tls-does-arm-run"></a>

ARM runs on **TLS 1.2**, therefore when Salesforce disables TLS 1.0, it has no effect on ARM.

### \*\*What rules do I need to obey when naming identifiers for all of the labels in the ARM application?

There are some rules you have to follow for naming identifiers:

* Must contain at least 3 characters (5+ recommended)
* Uppercase letter (A-Z) is allowed
* Lowercase letter (a-z) is allowed
* Number (0-9) is allowed
* Special characters (- and ,) are allowed.

### \*\*What is the primary reason for restricting special characters when naming identifiers? <a href="#what-is-the-primary-reason-for-restricting-special-characters-when-naming-identifiers" id="what-is-the-primary-reason-for-restricting-special-characters-when-naming-identifiers"></a>

It is done to restrict XML injections and prevent XML file corruption.

### Where is the API token key used in the ARM application? <a href="#where-is-the-api-token-key-used-in-the-arm-application" id="where-is-the-api-token-key-used-in-the-arm-application"></a>

1. The API Token generated via ARM will be used to authenticate within the application and provide access to get details of CI Job configured & its build details.
2. To use the AutoRABIT capability, each user has their own API token, which should not be shared with anyone. If you come across something phishing, deactivate your current API token and create a new one.

### Who is authorized to access the API token? <a href="#who-all-are-authorized-to-access-the-api-token" id="who-all-are-authorized-to-access-the-api-token"></a>

Super Admins, Org Admins, and the users with admin level permissions are authorized to access the API token.

### What browsers does ARM support? <a href="#what-browsers-does-arm-support" id="what-browsers-does-arm-support"></a>

ARM works best in the two most recent versions of these browsers:

* Chrome
* Edge
* Firefox
* Safari

### Why am I unable to log in to ARM using the Chrome browser? <a href="#not-able-to-login-to-arm-using-chrome-browser" id="not-able-to-login-to-arm-using-chrome-browser"></a>

1. Try logging in to your account using Chrome incognito mode.
2. Clear the Chrome browser cache.
3. If cleaning the cache does not help, try a different browser (Firefox) and see if the problem persists.
4. If the problem is solely with Chrome, reinstall it.

### \*\*Given the shift in IP ranges, is it possible to migrate from one AutoRABIT instance to another? <a href="#given-the-shift-in-ip-ranges-is-it-possible-to-migrate-from-one-autoabit-instance-to-another" id="given-the-shift-in-ip-ranges-is-it-possible-to-migrate-from-one-autoabit-instance-to-another"></a>

Yes, this is achievable; however, your [Salesforce Orgs](../../../product-guides/arm/arm-administration/registration/salesforce-org/) must be re-registered in AutoRABIT, and permissions provided to the relevant AutoRABIT users must be re-granted.

### Why am I able to see some users who are deleted in AutoRABIT? <a href="#why-am-i-able-to-see-some-of-the-users-that-are-deleted-in-autorabit" id="why-am-i-able-to-see-some-of-the-users-that-are-deleted-in-autorabit"></a>

1. **The deleted user's credential exists in AutoRABIT**: Go to _**Admin > Credential Manager**_ and type in the username that exists. You should find a record if it is still there.
2. [**Version Control**](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) **repository is registered with the existing user's credentials**: Get your existing user credentials updated with the new user details with the help of your admin. To do so, go to **Credential Manager** section and search for the existing user credential and get it updated with the new user details. Or create a user credential for the new user and re-register the existing version control repository with it.

### Why do my users not have access to all the features available in ARM? <a href="#why-my-users-do-not-have-access-to-all-of-features-available-in-arm" id="why-my-users-do-not-have-access-to-all-of-features-available-in-arm"></a>

1. Your users may not have the authority to access the modules that they are looking for; nevertheless, users with administrator privileges only will have access to certain features. To see the user's available roles in AutoRABIT, go to the **Admin > Roles** section.
2. For the necessary permissions, contact your **Org Admin**.

### Is it feasible to update the repository URL without having to re-register the repository in ARM? <a href="#is-it-feasible-to-update-the-repository-url-without-having-to-reregister-the-repository-in-arm" id="is-it-feasible-to-update-the-repository-url-without-having-to-reregister-the-repository-in-arm"></a>

The repository URL cannot be changed; you must use the new repository URL and re-register it with ARM. To register a new repository, click this [link](../../../product-guides/arm/arm-features/version-control/introduction-to-version-control/version-control-repositories-summary.md).

### Why am I getting a Credential Name error while trying to Save Mappings? <a href="#why-am-i-getting-a-credential-name-error-while-trying-to-save-mappings" id="why-am-i-getting-a-credential-name-error-while-trying-to-save-mappings"></a>

If you're a sub-user and get an error message `Credential with name: "qa private token cred" for this UserEmail does not have permission to save mapping` while saving **Org Mapping**, then the admin must **re-register** the repository **credentials** and make the credentials **Public**. The sub-user must then use the newly registered credentials.

### Why am I unable to create branching baselines for UAT and new SIT and getting an error while trying to create a new branch from VC Repo's? <a href="#why-am-i-unable-to-create-branching-baselines-for-uat-and-new-sit-and-getting-an-error-while-trying" id="why-am-i-unable-to-create-branching-baselines-for-uat-and-new-sit-and-getting-an-error-while-trying"></a>

Depending on the error, the credentials may have expired. Check the repository credentials and then **Test Connection** in ARM. Then retrigger the branching baseline. Please contact our support team if the problem continues.

### Why is my Test Connection in ARM failing even after re-authenticating the credentials? <a href="#why-is-test-connection-in-arm-failing-even-after-reauthenticating-the-credentials" id="why-is-test-connection-in-arm-failing-even-after-reauthenticating-the-credentials"></a>

If you have already re-authenticated, but the issue is still unresolved, it may not be a credential issue. Please contact our support team so we can **whitelist the domain** from our end with the SRO team. Once this is whitelisted on our end, you must also whitelist the **Instance IPs** on your network side.

### How can I remove the previous Super Admin from ARM and assign access to myself? <a href="#how-can-i-remove-the-previous-super-admin-from-arm-and-assign-access-to-myself" id="how-can-i-remove-the-previous-super-admin-from-arm-and-assign-access-to-myself"></a>

Please follow the guidance published [here](https://knowledgebase.autorabit.com/product-guides/arm/arm-administration/user-management/changing-super-admin-in-arm). Once you have that access, you can log in to ARM with your credentials and delete users without access.

### How many Super Admins are allowed? Can I assign a backup Super Admin? <a href="#i-have-refreshed-one-of-our-branches-by-using-the-branching-baseline-option-the-process-was-successf" id="i-have-refreshed-one-of-our-branches-by-using-the-branching-baseline-option-the-process-was-successf"></a>

There can only be one Super Admin, but you can temporarily change the Super Admin. Refer to the documentation published [here](https://knowledgebase.autorabit.com/product-guides/arm/arm-administration/user-management/changing-super-admin-in-arm).

### I have refreshed one of our branches by using the Branching Baseline option. The process was successful, but why is there no Revision Number created? <a href="#i-have-refreshed-one-of-our-branches-by-using-the-branching-baseline-option-the-process-was-successf" id="i-have-refreshed-one-of-our-branches-by-using-the-branching-baseline-option-the-process-was-successf"></a>

Before proceeding with the Branching Baseline operation, please ensure you have Write permissions for the selected branch. Please refer to the knowledge base article below for more information: [Branching Baseline](../../../product-guides/arm/getting-started/registration/branching-baseline.md)

### How can I get access to the AutoRABIT LearningHub? <a href="#how-can-i-get-access-to-the-autorabit-academy" id="how-can-i-get-access-to-the-autorabit-academy"></a>

To register for the AutoRABIT LearningHub, go to [https://learninghub.autorabit.com](https://learninghub.autorabit.com/).

### Is there a way to change an existing user’s email address without deleting the user? <a href="#is-there-a-way-to-change-an-existing-users-email-address-without-deleting-the-user" id="is-there-a-way-to-change-an-existing-users-email-address-without-deleting-the-user"></a>

As of now, you cannot simply change the email address of an existing user, either active or inactive. Your Admin must delete the user, then the user can create a new account with the desired email address.

### Why is my On-Prem ARM Test Server not working even after I have restarted the server and also restarted the processes? <a href="#why-is-my-onprem-arm-test-server-not-working-even-after-i-have-restarted-the-server-and-also-restart" id="why-is-my-onprem-arm-test-server-not-working-even-after-i-have-restarted-the-server-and-also-restart"></a>

If there is a problem with the **Test Server** instance, we do suggest you restart it. However, please restart the services first and then restart the server. This should resolve the issue.

### AutoRABIT displays unwanted changes and removes picklist options from branches when deploying changes to RecordTypes picklistValues. <a href="#autorabit-displays-unwanted-changes-and-removes-picklist-options-from-branches-when-deploying-change" id="autorabit-displays-unwanted-changes-and-removes-picklist-options-from-branches-when-deploying-change"></a>

If you have selected the below configuration for recordTypes picklistValues under **Admin > Salesforce settings > Configuration for recordTypes picklistValues**, then it will replace all picklist values with new picklist values.

_**replaceall**_

**Solution:** Select the **Append** button so that instead of overriding the entire record type picklist values, it adds to the existing picklist values.

### Why can’t my colleague with Deployment Manager, Developer, and Pull Request Reviewer roles Approve/Reject Merge and EZ-Commits? <a href="#why-cant-my-colleague-with-deployment-manager-developer-and-pull-request-reviewer-roles-approverejec" id="why-cant-my-colleague-with-deployment-manager-developer-and-pull-request-reviewer-roles-approverejec"></a>

Please edit the role assigned to the user and ensure that the below-mentioned special permissions are enabled for that role:

1. Gated check-ins approver
2. EZ-Merge approver.

### We’re switching from an on-premises GitHub account to the Cloud version of GitHub. I created the GitHub cloud account and tried setting up the cloud connection in ARM, but the system gave me an error. <a href="#were-switching-from-an-onpremises-github-account-to-the-cloud-version-of-github-i-created-the-github" id="were-switching-from-an-onpremises-github-account-to-the-cloud-version-of-github-i-created-the-github"></a>

Once the GitHub cloud account is created, you should be able to set it up with ARM as well. If you’re facing any issues, it is possible that the repository might still be migrating. If so, you are unable to register the repository during that time. But after migration is complete, you should be able to register the repository in ARM.

### Why can't we see the Diff when a Commit is created, but we can see a Diff during the process of Commit? <a href="#we-can-see-the-diff-when-a-commit-is-created-but-can-we-see-a-diff-during-the-process-of-commit" id="we-can-see-the-diff-when-a-commit-is-created-but-can-we-see-a-diff-during-the-process-of-commit"></a>

Using the **Compare Changes** option, you can file the **Diff** before performing a Commit.

### Why is the Branching Baseline job status in ARM showing as hanged for more than 24 hours? <a href="#i-am-trying-to-run-the-branching-baseline-job-in-arm-why-is-the-job-status-showing-as-hanged-for-mor" id="i-am-trying-to-run-the-branching-baseline-job-in-arm-why-is-the-job-status-showing-as-hanged-for-mor"></a>

Usually, the metadata retrieval would fail due to timeout. Please rerun the baseline and reduce the batch size. If this doesn’t resolve the issue, contact the AutoRABIT support team, and we should be able to assist further after inspecting the logs.

### Why can’t I see the Pull Request Plugins dropdown and the Enable Pull Request Support checkbox in the Admin VC Repo page when the repository is registered with SSH? <a href="#why-cant-i-see-the-pull-request-plugins-dropdown-and-the-enable-pull-request-support-checkbox-in-the" id="why-cant-i-see-the-pull-request-plugins-dropdown-and-the-enable-pull-request-support-checkbox-in-the"></a>

**Pull requests** are currently not supported for repositories authenticated via **SSH** protocol. However, an **HTTPS-based** connection via username and personal access token is supported.

### ()Why can’t I see the User Management section anymore to add a user like I could before? <a href="#i-want-to-add-a-user-like-i-could-before-why-cant-i-see-the-user-management-section-anymore" id="i-want-to-add-a-user-like-i-could-before-why-cant-i-see-the-user-management-section-anymore"></a>

The **User Permissions** and **Roles** in your organization may have been rearranged. Please contact your Admin and they should be able to grant you the necessary permissions again.

### Why am I getting an error when trying to register a Bitbucket repo? <a href="#why-am-i-getting-an-error-when-trying-to-register-a-bitbucket-repo" id="why-am-i-getting-an-error-when-trying-to-register-a-bitbucket-repo"></a>

Please check your credentials because your Bitbucket account username is different than your email address. Once you have confirmed your username, try to register the repository, and then test to see whether branch creation was successful.

\
