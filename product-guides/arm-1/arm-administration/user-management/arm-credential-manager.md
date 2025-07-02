# Credential Manager

{% hint style="info" %}
**Important Note:** The actions described here are visible only to **Org Administrators**. General users cannot access Credential Manager.
{% endhint %}

***

## Credential Manager: Overview <a href="#credential-manager-overview" id="credential-manager-overview"></a>

**Credential Manager (CM)** is your encrypted “digital locker” inside AutoRABIT.\
Store usernames, passwords, SSH keys, tokens, and certificates once, then reuse them across repositories and integrations without re-entering secrets each time.

Key benefits:

* Centralized, encrypted storage managed by ARM.
* Role-based sharing (global vs. private).
* Eliminates hard-coding credentials in jobs or scripts.

***

## Create a New Credential <a href="#create-a-new-credential" id="create-a-new-credential"></a>

1.  Hover over **`Admin`** and click **`Credentials`**.

    <figure><img src="../../../../.gitbook/assets/image (630).png" alt="Admin menu with Credentials option highlighted" width="326"><figcaption></figcaption></figure>
2.  Click **Create Credential**.

    <figure><img src="../../../../.gitbook/assets/image (631).png" alt="Create Credential button"><figcaption></figcaption></figure>
3. In the pop-up, enter a **Credential name** and choose a **Credential Type**:
   * **Username with Password**
   * **SSH**
   * **HashiCorp Vault**
   * **SSH Certificate**
   * **Application Token** (Enterprise only)

***

### Username with Password <a href="#username-with-password" id="username-with-password"></a>

Provide the service **username** and **password**. Choose a **Credential Scope**:

* **Global** – share with the team.
* **Private** – visible only to you.

<figure><img src="../../../../.gitbook/assets/image (632).png" alt="Username with Password credential form" width="563"><figcaption></figcaption></figure>

***

### SSH <a href="#ssh" id="ssh"></a>

Upload or paste your **private key** (optionally protected by a passphrase). ARM stores the key and uses it for Git operations over SSH.

<figure><img src="../../../../.gitbook/assets/image (633).png" alt="SSH credential form with key upload" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
* **Recommended** – SSH keys are more secure than user/password.
* Choose **Global** or **Private** scope.
* Paste or upload the private key file; ARM never exposes it in plain text.
{% endhint %}

***

### HashiCorp Vault <a href="#hashicorp-vault" id="hashicorp-vault"></a>

Add HashiCorp Vault credentials once; ARM can now generate a new **Vault Token** automatically via **AWS authentication** whenever the old token expires.

<figure><img src="../../../../.gitbook/assets/image (635).png" alt="HashiCorp Vault credential form with AWS Auth option" width="563"><figcaption></figcaption></figure>

_For details, see the dedicated_ [_HashiCorp Vault guide_](arm-credential-manager.md#hashicorp-vault)_._

***

### Authentication Using SSH Certificates <a href="#authentication-using-ssh-certificates" id="authentication-using-ssh-certificates"></a>

**SSH certificates** pair a public key with a signature from a trusted Certificate Authority (CA). A Git server that trusts the CA accepts any certificate signed by it.

* Upload the **certificate-signed key** while creating the credential.
* Supported for **GitHub Enterprise Cloud** orgs.

<figure><img src="../../../../.gitbook/assets/image (636).png" alt="SSH Certificate credential form" width="563"><figcaption></figcaption></figure>

> **Limitation:** Available only for GitHub Enterprise Cloud.

***

### Application Token (Enterprise Only) <a href="#application-token-for-enterprise-users-only" id="application-token-for-enterprise-users-only"></a>

Connect ARM to Jira via **Personal Access Token (PAT)** to meet enterprise compliance.

1. Select **Application Token** as **Credential Type**.
2. Paste the **PAT** generated in Jira.
3. Click **Save**.

<figure><img src="../../../../.gitbook/assets/image (637).png" alt="Application Token credential form for Jira integration"><figcaption></figcaption></figure>

Need PAT access? Email **support@autorabit.com**.\
How to create a PAT in Jira: [Atlassian docs](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

***
