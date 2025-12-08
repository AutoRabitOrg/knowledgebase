# Generating SSH Keys and Configuring Git Repo Access

### Feature Overview

This guide walks you through the steps to generate SSH keys, configure GitHub access, and set up your credentials in AutoRABIT ARM for secure repository integration.

### Step-by-Step Guide

**Step 1: Retrieve Your GitHub Username**

1. Log in to your GitHub account.
2. Copy your exact GitHub username as it appears in your profile.
3. Save it in a text editor (e.g., Notepad) for later reference.



**Step 2: Verify Repository Access:** Ensure your GitHub account has access to the repository you'll be connecting to through AutoRABIT. If you're unsure, check with your GitHub administrator or repository owner.



**Step 3: Generate SSH Keys**

Run the following command to generate a new SSH key pair:

`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

**When prompted:**

* Press Enter to accept the default file location.
* When asked for a passphrase, you can leave it blank (press Enter twice).

**Note:** The command is the same for both Windows and macOS users.

&#x20;

**Step 4: Locate the Generated SSH Files:** After running the command, two files will be created in your .ssh directory:

1. **id\_rsa:** Private key — used for authentication in AutoRABIT
2. **id\_rsa.pub:** Public key — added to your GitHub account

**Default file location:**

* Windows: C:\Users\\\<YourUsername>\\.ssh\\
* macOS/Linux: /Users/\<YourUsername>/.ssh/

&#x20;

**Important:**

* The public key (id\_rsa.pub) will be uploaded to GitHub.
* The private key (id\_rsa) will be uploaded securely to AutoRABIT.
* Do not share your private key with anyone.

**Troubleshooting Tip:** If you've generated SSH keys previously using the same folder, clear out the old files or specify a different filename during key creation to avoid conflicts.

&#x20;

**Step 5: Add the SSH Credential in AutoRABIT**

1. Log in to AutoRABIT.
2. Navigate to Admin Console → Credentials.
3. Click New Credential.
   * Use a meaningful name, for example: FirstNameSSH2025.
4. Set Credential Type to SSH.
5. Upload your private key file (id\_rsa).
6. Enter your GitHub username.
7. Leave the Token/Password field empty.
8. Click Upload Private Key, select the file, and then click Save.



**Step 6: Add the Public Key to GitHub**

1. Log in to GitHub and go to your profile settings.
2. From the left sidebar, select SSH and GPG keys.
3. Click New SSH key.
   * Enter a descriptive title (e.g., FirstNameARSSH2025)
4. Open your id\_rsa.pub file in a text editor, copy the full content, and paste it into the Key field.
5. Click Add SSH key to save.



**Step 7: Authorize the SSH Key with GitHub SSO**

1. Under SSH and GPG keys, find the key you just added.
2. Click the Configure SSO option next to it.
3. Click Authorize to complete the authentication process.
4. This step links your SSH key with your organization's GitHub SSO setup.



**Step 8: Test the SSH Connection in AutoRABIT**

1. Return to AutoRABIT.
2. Navigate to Profile → My Version Control Mappings.
3. You can use the search bar (Ctrl+F) to find your repository mapping.
4. Select your newly created SSH credential.
5. Click "Test Connection" to verify a successful setup.



**Important:**

* Ensure you have the required roles and permissions assigned by your AutoRABIT administrator.
* If you do not see the correct branches or mappings:
  * Confirm access with a team member who can view them.
  * Ask your admin to assign the necessary permissions or group access.



**You're All Set!** Once your SSH connection is validated, your repository will be securely linked to AutoRABIT, allowing you to perform CI/CD operations seamlessly. If you need further assistance, please contact the AutoRABIT Support Team ([support@autorabbit.com](mailto:support@autorabbit.com)).&#x20;
