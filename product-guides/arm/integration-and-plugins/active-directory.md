# Active Directory

### Active Directory: Overview

Active Directory integration provides log-in to [Automated Release Management (ARM)](https://www.autorabit.com/products/automated-release-management/) using credentials stored in the Server.  The administrator can easily import users from the active directory into the AutoRABIT instance and keep both synchronized through these features.

### Setting Up Active Directory (AD) in ARM

1. Log in to your ARM account.
2. Hover your mouse over the **Admin** module and click on the **My Account** section.&#x20;
3. On the **My Account** page, go to the **Plugins** section.
4.  Select the **AD** checkbox available under the **Identity Management** section.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664446441984.png" alt=""><figcaption></figcaption></figure>
5. Provide the information below to integrate the AD with ARM:
   1. **IP Address or FQDN (Fully Qualified Domain Name):** Paste here the IP address copied from the Active Directory server or enter the domain name (FQDN). The FQDN is required if the AD is configured over the SSL type.
   2. **Port:** Enter the port here. By default, Port 389 will be taken. However, if the AD is configured over SSL, enter the port as 636.
   3. **Domain Name:** Paste the domain name exactly as configured in the AD server.
   4. **Group name:** Enter the group detail for which you would like to fetch the detail from the AD.
   5. **Host Type**: Select the host type i.e., cloud or on-premise.
   6.  **Select Credential:** Choose the correct credentials from the drop-down field or, to create a new credential, click on the **+** icon.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664446520555.png" alt="" width="375"><figcaption></figcaption></figure>
6. Next, click **Test Connection** to check for the connection authentication. Upon successful confirmation, click **OK** to register the AD with AutoRABIT.

### Importing Users from AD to ARM

1. Log in to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and click on **Users.**
3.  On the **Users** screen, click on **Import Users From AD** in the top right corner.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664446651647.png" alt="" width="563"><figcaption></figcaption></figure>
4. Select the users to import into AutoRABIT. Once the import is done, the users will be part of AutoRABIT and they can easily log in to AutoRABIT with their **Accountname@domainName**.
5. Also, whenever a user is created, modified, or deleted in the Active Directory, ARM will detect the change and perform the corresponding create, modify or delete action within the user database.
