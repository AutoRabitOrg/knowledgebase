# Active Directory

### Active Directory: Overview

Active Directory integration provides log-in to [Automated Release Management (ARM)](https://www.autorabit.com/products/automated-release-management/) using credentials stored in the Server.  The administrator can easily import users from the active directory into the AutoRABIT instance and keep both synchronized through these features.

### Setting Up Active Directory (AD) in ARM

1. Log in to your ARM account.
2. Hover your mouse over the **Admin** module and click on the **My Account** section.&#x20;
3. On the **My Account** page, go to the **Plugins** section.
4. Select the **AD** checkbox available under the **Identity Management** section.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5.  Provide the information below to integrate the AD with ARM:

    * **IP Address or FQDN (Fully Qualified Domain Name):** Paste here the IP address copied from the Active Directory server or enter the domain name (FQDN). The FQDN is required if the AD is configured over the SSL type.
    * **Port:** Enter the port here. By default, Port 389 will be taken. However, if the AD is configured over SSL, enter the port as 636.
    * **Domain Name:** Paste the domain name exactly as configured in the AD server.
    * **Group name:** Enter the group detail for which you would like to fetch the detail from the AD.
    * **Host Type**: Select the host type i.e., cloud or on-premise.
    * **Select Credential:** Choose the correct credentials from the drop-down field or, to create a new credential, click on the **+** icon.

    <figure><img src="../../../.gitbook/assets/image (21) (1) (1) (1) (1).png" alt="" width="385"><figcaption></figcaption></figure>
6. Next, click **Test Connection** to check for the connection authentication. Upon successful confirmation, click **OK** to register the AD with AutoRABIT.

### Importing Users from AD to ARM

1. Log in to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and click on **Users.**
3. On the **Users** screen, click on **Import Users From AD** in the top right corner.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1) (1) (1).png" alt="" width="470"><figcaption></figcaption></figure>

4. Select the users to import into AutoRABIT. Once the import is done, the users will be part of AutoRABIT and they can easily log in to AutoRABIT with their **Accountname@domainName**.
5. Also, whenever a user is created, modified, or deleted in the Active Directory, ARM will detect the change and perform the corresponding create, modify or delete action within the user database.
