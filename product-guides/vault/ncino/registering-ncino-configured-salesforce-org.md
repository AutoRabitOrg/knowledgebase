# Registering nCino configured Salesforce Org

Registering the nCino-installed Salesforce organization enables you to perform nCino data operations inside Vault. When you register your Salesforce Organization, Vault is connected to your Salesforce org with required permissions that enable you to back up your data and metadata information.

By default, [Vault](https://www.autorabit.com/products/vault-data-backup-recovery/) connects to orgs using the secure 'OAuth' method (our recommended approach). You can also connect to orgs using username/password connections if required.

To register a Salesforce org configured with nCino objects, follow the steps below in order:

1. Log in to **Vault** using your credentials.
2. Visit **Setup > Register New Org** from the Vault homepage.

<figure><img src="../../../.gitbook/assets/image (266).png" alt=""><figcaption></figcaption></figure>

3. Select [**nCino**](https://www.autorabit.com/industry-solution/banking-financial-services-ncino/) as **Environment**.
4. Select your [**Salesforce Org**](https://knowledgebase.autorabit.com/vault/docs/backup-configuration-for-your-salesforce-org) **type,** e.g., Production Org, Sandbox, QA Org, etc. You can add your custom org by adding your custom URL.
5.  Next, choose an Authentication Type to register the org. Usually, there are two ways to authenticate your Salesforce Org: **OAuth** or **Standard** (username/password).

    * **OAuth Authentication**: In OAuth authentication, enter the desired name for the Org in the **Org Title** field and the **Salesforce username**. On clicking **‘Authenticate,’** the page will redirect you to the Salesforce login screen, where you can enter your authentication details. Upon successful authentication, you will be redirected back to the Vault page.

    <figure><img src="../../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

    * **Standard Authentication**: In Standard authentication, the desired Salesforce Cloud environment, your username, password, and security token of the Salesforce are entered, and Vault authenticates the connection. To verify that Vault can connect to the target Salesforce organization when using the credentials of the target Salesforce user, click on **Test Connection**.

    <figure><img src="../../../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>
6. Finally, click on **Save** to complete the authentication process.

### What's Next? <a href="#whats-next" id="whats-next"></a>

Upon successful authentication, you must create a new configuration for your nCino-configured Salesforce org. There are two ways to add configuration for your Salesforce org:

* [Backup Configuration](https://knowledgebase.autorabit.com/vault/docs/backup-configuration-for-your-salesforce-org)
* [Archival Configuration](https://knowledgebase.autorabit.com/vault/docs/archival-configuration-for-your-salesforce-org)
