# HashiCorp Vault

### What is HashiCorp Vault?&#x20;

HashiCorp Vault is a secrets management solution that brokers access for both humans and machines, through programmatic access, to systems. Secrets can be stored, dynamically generated, and in the case of encryption, keys can be consumed as a service without the need to expose the underlying key materials.

### What is the purpose of Hashicorp Vault?

1. Ease of use for developers to access/use confidential secrets, keys, and credentials
2. Confidentiality for secrets, keys, and credentials
3. Provide mechanisms for key rotation in case of compromise
4. Create an audit log to keep track of what systems and users access confidential data

## Set up a HashiCorp server

### Steps for Installing Vault on Linux Ubuntu

#### Prerequisites

1. Ubuntu 18.04
2. A user account with **sudo** privileges
3. Access to a terminal window/command-line (Ctrl-Alt-T)

#### Install Consul

Consul is a highly scalable and distributed service discovery and configuration system. You can coordinate Consul Storage as a backend to Vault to ensure the software is highly available and fault-tolerant.&#x20;

The first step is to install and configure Consul on Ubuntu 18.04.

1. Start by navigating to the [Consul webpage](https://www.consul.io/) and clicking on the **Download** icon.
2. The browser then takes you to the Download page with all the available packages. Search for the Linux section and right-click on the 32 or 64-bit version. Copy the link location, as you will need it in the next step.
3. Open the terminal (**Ctrl**+**Alt**+**T**) and use the **wget** command to download the Consul package: **wget** [https://releases.hashicorp.com/consul/1.6.1/consul\_1.6.1\_linux\_amd64.zip](https://releases.hashicorp.com/consul/1.6.1/consul\_1.6.1\_linux\_amd64.zip)
4. Next, unzip the package with the command: **unzip consul\_1.6.1\_linux\_amd64.zip**Note:To download unzip software, use the command: **sudo apt install unzip –y**.
5. Then, move the installation package by typing the following command: **sudo mv consul /usr/bin**
6. End by verifying the installation with the command: **consul**
7. The output should list all available consul commands, as in the image below:

<figure><img src="../../../.gitbook/assets/image (31) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configure Consul

1. Create and open a new file with **sudo nano /etc/system/system/consul.service**
2.  Add the following content to the **consul.service** file: ActionScript

    ```actionscript
    [Unit]

    Description=Consul

    Documentation=https://www.consul.io/

    [Service]

    ExecStart=/usr/bin/consul agent –server –ui –data-dir=/temp/consul –bootstrap-expect=1 –node=vault –bind=IP.ADDRESS.OF.SERVER –config-dir=/etc/consul.d/

    ExecReload=/bin/kill –HUP $MAINPID

    LimitNOFILE=65536

    [Install]

    WantedBy=multi-user.target
    ```



    <figure><img src="../../../.gitbook/assets/image (32) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3. **Save** and **exit** the file.
4.  Then, move on to creating a configuration directory and adding a new **.json** file in it: ActionScript

    ```actionscript
    sudo mkdir /etc/consul.d

    nano /etc/consul.d/ui.json
    ```
5.  To set up the UI to connect to anything, add the following content to the newly created file: ActionScript

    ```actionscript
    {

    “addresses”: {

    “http”: “0.0.0.0”

    }

    }
    ```
6. Make sure to save before exiting the file.
7. For the changes to occur, you must reload, start, and enable the consul service.
8. Reload the system with the command: **systemctl daemon-reload** &#x20;
9. Run the command for **starting** the service: **systemctl start consul**
10. Then, **enable** it by using: **systemctl enable consul**
11. Verify that the service is up and running with the command: **journalctl –f –u consul**
12. This followed by opening a web browser and navigating to the URL: **vault.admintome.lab:8500/ui/**
13. This opens HashiCorp’s online management platform and displays available services. If you see consul as a service, you have successfully set up the software.

#### Installing Vault on Ubuntu

With Consul in place, move on to installing Vault on your Ubuntu 18.04 system.

1. Go to [Vault’s official website](https://www.vaultproject.io/), click on **Download**, and find the available package for Linux distributions.
2. Right-click on the **Download** icon and copy the link location.

<figure><img src="../../../.gitbook/assets/image (34) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="534"><figcaption></figcaption></figure>

3. Using the wget command, download the package by pasting the link location copied in the previous step: **wget** [https://releases.hashicorp.com/vault/1.2.3/vault\_1.2.3\_linux\_amd64.zip](https://releases.hashicorp.com/vault/1.2.3/vault\_1.2.3\_linux\_amd64.zip)
4. Next, unzip the package using the following command: **unzip vault\_1.2.3\_linux\_amd64.zip**
5. Then, move the package to the **/usr/bin** directory: **mv vault /usr/bin**
6. Check the installation using the following command: **vault**

As a result, a list of all available vault commands should appear, as in the image below:

<figure><img src="../../../.gitbook/assets/image (35) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configure Vault

1. Start by creating a configuration directory and a file within it: **sudo nano /etc/vault/config.hcl**
2.  Then, type or paste the following content in the file: ActionScript

    ```actionscript
    storage “consul” {

    address = “127.0.0.1:8500”

    path = “vault/”

    }

    listener “tcp” {

    address = ”IP.ADDRESS.OF.SERVER” [or “0.0.0.0” to listen to everything]

    tls_disable = 1

    }

    ui = truestorage “consul” {

    address = “127.0.0.1:8500”

    path = “vault/”

    }

    listener “tcp” {

    address = ”IP.ADDRESS.OF.SERVER” [or “0.0.0.0” to listen to everything]

    tls_disable = 1

    }

    ui = true
    ```
3. Again, save and exit the file.
4. Next, you need to create a UNI (**.uni**) file, a commonly used extension for configuration files. The easiest way to do this is to copy Consul’s configuration file and modify the specifications to suit Vault.
5. Duplicate the existing service configuration file under a new name with the command: **cp /etc/system.system/consul.service /etc/system/system/vault.service**
6. Open the new **vault.service** file: **vim /etc/system/system/vault.service**
7.  Make sure the content of the file matches the one below. Essentially, you’ll need to change all Consul-specific values with the appropriate Vault ones. ActionScript

    ```actionscript
    [Unit]

    Description=Vault

    Documentation=https://www.vault.io/

    [Service]

    ExecStart=/usr/bin/vault server –config=/etc/vault/config.hcl

    ExecReload=/bin/kill –HUP $MAINPID

    LimitNOFILE=65536

    [Install]

    WantedBy=multi-user.target[Unit]

    Description=Vault

    Documentation=https://www.vault.io/

    [Service]

    ExecStart=/usr/bin/vault server –config=/etc/vault/config.hcl

    ExecReload=/bin/kill –HUP $MAINPID

    LimitNOFILE=65536

    [Install]

    WantedBy=multi-user.target
    ```
8.  After saving the file, exit back to the terminal shell and launch the service with the following commands: ActionScript

    ```actionscript
    systemctl daemon-reload

    systemctl start vault

    systemctl enable vault

    systemctl status vaultsystemctl daemon-reload

    systemctl start vault

    systemctl enable vault

    systemctl status vault
    ```
9. The status should show the service is **active (running)**.
10. Using a vault client, connect to the running service with the command: **export VAULT\_ADDR=http://IP.ADDRESS.OF.VAULT:CLIENT**

#### Initialize Vault

As you have already installed Consul to serve as the back-end storage, you’ll now need to initialize Vault manually for it to work correctly.

1. First, run the following command to see current Vault status: **vault status.**

<figure><img src="../../../.gitbook/assets/image (36) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. As in the image above, the output displays that Vault is **sealed** and **not initialized** yet.
3. To change its status, you need three (3) keys you can find by running the command: **vault operator init**
   * The terminal will return **five (5) Unseal Keys** as well as an **Initial Root Token**. Also, it explains that anytime the Vault package is re-sealed, restarted, or stopped, you will need to supply at least three (3) of these keys.
   * If you do not provide the specified keys, Vault will remain sealed. Therefore, copy all five keys and paste them into a separate file.
4. Once you have at least 3 unseal keys, run the command**: vault operator unseal**
5. Copy and paste the first key and hit **Enter**.
6. Repeat the same procedure for Unseal Key 2 and 3.
7. The last step to unseal Vault is to run the following command with the Initial Root Token (listed with the Unseal Keys): **vault login \[root\_token]**
8. Now, check the status again to verify that the software has been initialized: vault status

<figure><img src="../../../.gitbook/assets/image (37) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Steps for Installing Vault on Windows

1. Install **Chocolatey** (free and open-source package management system for Windows).
2. Open PowerShell with Admin privileges
3.  Enter the below command:ActionScript

    ```actionscript
    “Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))”“Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))”
    ```
4. Open PowerShell and enter the below command: **choco install vault**
5. After installing Vault, verify the installation worked by opening a new terminal session and checking that the vault binary is available. By executing vault, you should see help output similar to the following:

<figure><img src="../../../.gitbook/assets/image (38) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;**Vault Server**

Vault operates as a client/server application. The Vault server is the only piece of the Vault architecture that interacts with the data storage and backends. All operations are done via the Vault CLI interact with the server over a TLS connection.

**Starting the Dev Server**

1. Open **PowerShell.**
2. Enter the command: **1$ vault server -dev**![](<../../../.gitbook/assets/image (39) (1) (1) (1) (1) (1) (1) (1).png>)

<figure><img src="../../../.gitbook/assets/image (40) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (41) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3.  With the dev server started, perform the following:

    * Launch a new terminal session.
    * Copy and run the export **VAULT\_ADDR ...** command from the terminal output. This will configure the Vault client to talk to the dev server.
    * Vault CLI determines which Vault servers to send requests using the **VAULT\_ADDR** environment variable.
    * Save the unseal key somewhere. Don't worry about how to save this securely. For now, just save it anywhere.
    * Set the **VAULT\_TOKEN** environment variable value to the generated Root Token value displayed in the terminal output.
    * Verify the server is running.

    <figure><img src="../../../.gitbook/assets/image (42) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## HashiCorp Vault- Basic Commands

Once you start the server (as mentioned in the section: **Starting the Dev Server**), the server will be on sealed mode, by default. Therefore, it is required to initialize the server first.

{% hint style="info" %}
**Important Note:** Step to initialize the server is not required for dev mode server.
{% endhint %}

#### Initialize the server

The operator **init** command initializes a Vault server. Initialization is the process by which Vault's storage backend is prepared to receive data. Since Vault servers share the same storage backend in HA mode, you only need to initialize one Vault to initialize the storage backend.

During initialization, Vault generates an in-memory master key and applies Shamir's secret sharing algorithm to disassemble that master key into a configuration number of key shares such that a configurable subset of those key shares must come together to regenerate the master key. These keys are often called "unseal keys" in Vault's documentation.

This command cannot be run against an already-initialized Vault cluster: **vault operator init**

<figure><img src="../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Default it will generate 5 share keys and a master token.

#### Verify the Server is Running

Check for the server is running successfully by using the command: **vault status**

<figure><img src="../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Unsealing

The unseal process is done by running vault operator unseal or via the API. This process is stateful: each key can be entered via multiple mechanisms on multiple computers, and it will work. This allows each share of the master key to be on a distinct machine for better security.

**vault operator unseal \<code>**

<figure><img src="../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### &#x20;Log in to the Vault Server

Authenticate by using root key:

| <p><strong>vault login &#x3C;Initial_Root_Token></strong></p><p>or, </p><p><strong>set VAULT_TOKEN=&#x3C;Initial_Root_Token></strong></p> |
| ----------------------------------------------------------------------------------------------------------------------------------------- |

<figure><img src="../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Enable KV

Most secrets engines must be configured in advance before they can perform their functions. These steps are usually completed by an operator or configuration management tool.

A v2 kv secrets engine can be enabled by:

| <p><strong>vault secrets enable -version=2 kv</strong></p><p>or,</p><p><strong>vault secrets enable kv-v2</strong></p> |
| ---------------------------------------------------------------------------------------------------------------------- |

An existing version 1 kv can be upgraded to a version 2 KV store with the CLI command: **vault kv enable-versioning secret/**

<figure><img src="../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Above all steps are one-time setup only.&#x20;
{% endhint %}

#### Commands to add or get secrets from Vault

**kv put**

The **kv put** command writes the data to the given path in the K/V secrets engine.

| **Command:** _vault kv put secret/data key=value_ |
| ------------------------------------------------- |

<figure><img src="../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**kv get**

The **kv get** command retrieves the value from K/V secrets engine at the given key name. If no key exists with that name, an error is returned. If a key exists with the name but has no data, nothing is returned.

| **Command:** _vault kv get secret/creds_ |
| ---------------------------------------- |

<figure><img src="../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Adding HashiCorp Credential into AutoRABIT

Follow the below steps to integrate HashiCorp Vault with AutoRABIT:

1. Go to **Admin > Credentials** and click on **Create Credential**
2. On the next pop-up screen, give a **Credential Name**.
3. Choose the **Credential Type** as **HashiCorp Vault**
4. Choose the **Credential Scope**. The Credential Scope lets you specify exactly what type of access you need.
   * **Global:** Credential can be accessed within the team
   * **Private:** Credential to be used for private usage
5. Fill in the below details:
   * **Vault Server URL:** Enter the Vault server to configure with AutoRABIT. The Vault dev server defaults to running at **http://127.0.0.1:8200**. The server is initialized and unsealed.
   *   **Authentication Method AWS:** This checkbox will be selected by default. After you enter the remaining details, the Vault token will automatically be generated through the AWS login authentication method whenever the existing token expires.

       <figure><img src="../../../.gitbook/assets/image (54) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="293"><figcaption></figcaption></figure>

       * If you deselect the **Authentication Method AWS** checkbox, then the below **Vault Token** mandatory field will be displayed.

       <figure><img src="../../../.gitbook/assets/image (55) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="288"><figcaption></figcaption></figure>
   * **Vault Token:** Enter the Vault token that you generated earlier using unseal key. For more information, refer [HERE](https://learn.hashicorp.com/tutorials/vault/generate-root?in=vault/operations).
   * **Key Name**: Enter the **Key Name** that you have obtained in HashiCorp CLI.
   * **Secret Path**: Enter the Secret Path.
6. Click **Validate and Save**. This validates the credentials and if all the fields are correctly added, the credentials get saved in AutoRABIT.

## TLS Support for Hashicorp Vault Integration

Hashicorp Vault integration runs on **TLS 1.2** version.
