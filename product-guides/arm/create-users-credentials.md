# Create Users' Credentials

{% hint style="info" %}
**Important Note:** This article is for **Org Administrators** in particular. The actions discussed in the article are not available to general users.&#x20;
{% endhint %}

### Credential Manager: Overview <a href="#credential-manager-overview" id="credential-manager-overview"></a>

Credential Manager (CM) is the "digital locker" where ARM stores log-in credentials like usernames and passwords. It securely stores your credentials, so you only need to enter them once for each remote repository you access. Storing login information in the ARM CM saves you time when you frequently access a file shared on another machine.&#x20;

### Create a New Credential <a href="#create-a-new-credential" id="create-a-new-credential"></a>

Log into ARM with username _xyz@autorabit.com_, for example, then do the following:&#x20;

1.  Hover your mouse over the **`Admin`** tile and select the option for **`Credentials`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682400604799.png" alt="" width="188"><figcaption></figcaption></figure>
2.  Click **`Create Credential`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682400659117.png" alt=""><figcaption></figcaption></figure>
3. On the next pop-up screen, enter a **`Credential name`**.
4. Choose a **`Credential Type`** from the drop-down field.&#x20;
   * Username with Password&#x20;
   * SSH
   * HashiCorp Vault
   * SSH Certificate

#### Username with Password  <a href="#username-with-password" id="username-with-password"></a>

Password-based authentication requires the user to enter their username and password to create a credential.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682400914282.png" alt="" width="563"><figcaption></figcaption></figure>

Credential Scope lets you specify exactly what type of access you need.&#x20;

* **`Global:`** Credential to be accessed by the team
* **`Private:`** Credential for private usage

#### SSH <a href="#ssh" id="ssh"></a>

**`SSH`** is an encrypted protocol used to administer and communicate with servers. SSH is a secure way to access a site’s server remotely. The user must generate a public/private key pair on the client machine to identify them on the servers. You can choose to protect it with a password. Entering it with no password means anyone with access to the key files has the same level of access as the user, and no password is required when the client connects to the servers. Protecting the keys with a password means that whenever the user connects to a server using those keys, the password for decrypting it is required.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682499869449.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. We recommend using SSH-type credentials rather than password-type credentials for increased security.
2. Credential Scope lets you specify exactly what type of access you need.
   * **`Global:`** Credential to be accessed by the team
   * **`Private:`** Credential for private usage
3. Upload the Private key, if available on your local machine, or paste it into the clipboard provided.
{% endhint %}

#### HashiCorp Vault <a href="#hashicorp-vault" id="hashicorp-vault"></a>

You can now choose the **`AWS Authentication`** method while adding HashiCorp credentials to ARM to generate the **`Vault Token`** automatically whenever the existing token expires. Now the user does not have to update the token manually from the application when it expires. Click [here](https://knowledgebase.autorabit.com/docs/hashicorp-vault#5-adding-hashicorp-credential-into-autorabit) for a more detailed article on this topic.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682499945028.png" alt="" width="563"><figcaption></figcaption></figure>

#### Authentication using SSH Certificates <a href="#authentication-using-ssh-certificates" id="authentication-using-ssh-certificates"></a>

**About SSH Certificates**

**`SSH certificates`** allow one SSH key to sign another SSH key, resulting in an SSH certificate. A server that trusts the Certificate Authority (CA) can verify the certificate’s signature and trust the certificate and its associated metadata.

Learn more information about SSH certificate authorities at [https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-git-access-to-your-organizations-repositories/about-ssh-certificate-authorities](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-git-access-to-your-organizations-repositories/about-ssh-certificate-authorities)

**How is an SSH certificate different than an SSH key?**

SSH uses key-based authentication with public key cryptography, while an SSH certificate-based authentication and attaches a signed certificate to each key to verify their identities. By using a certificate signed by a trusted CA, users can do away with passwords, which are not secure, given that passwords can either be stolen or cracked via brute force, and leverage a partially automated, trust-based certificate authentication process to gain access to systems.

**How to add SSH certificates?**

To give organizations more control over how their members access their repositories in GitHub, ARM now supports credentials of the **`SSH Certificate`** type. The user must upload the key for the SSH certificate while creating a credential. Then the user can later authenticate the repositories and add them inside ARM using the credential.

SSH certificates only allow access to repositories that belong to their organization.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1682500281739.png)

Limitation:

Adding SSH certificates is currently limited to organizations using GitHub Enterprise Cloud.
