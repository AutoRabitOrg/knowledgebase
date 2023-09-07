# Unique Identifier (UID)

### What is a Unique Identifier (UID) in Vault? <a href="#what-is-a-unique-identifier-uid-in-vault" id="what-is-a-unique-identifier-uid-in-vault"></a>

A unique identifier (UID) is an identifier that marks that particular record as unique from every other record. It allows the record to be referenced in Vault without confusion or unintentional overwriting from other records.

### Why UID is necessary for each record? <a href="#why-uid-is-necessary-for-each-record" id="why-uid-is-necessary-for-each-record"></a>

With the current implementation of Vault, when records are already available in a sandbox after the refresh, Vault doesn't have a way to identify the records in the destination since the mapping between source and destination records won't be available with Vault to uniquely identify the records in the destination.

### What problem we are solving here? <a href="#what-problem-we-are-solving-here" id="what-problem-we-are-solving-here"></a>

With this feature, the user can configure a unique identifier for each object in the Salesforce org. We will be able to replicate the data between orgs by uniquely identifying similar records between the orgs, thereby avoiding the recreation of duplicate records in the destination.

### Configuring Unique Identifier <a href="#configuring-unique-identifier" id="configuring-unique-identifier"></a>

#### Mapping unique id for a specific object <a href="#mapping-unique-id-for-a-specific-object" id="mapping-unique-id-for-a-specific-object"></a>

1. In the **Vault** application, go to **Setup** and choose your Salesforce Org.
2. Go to the **Unique Identifiers** tab. This will show all the objects and their unique identifiers on the screen.
3. Click on the **Map** button beside the object to show all the fields of the object in your Salesforce Org along with their type, and the unique fields.
4. Select the fields required and click on **Save**. You will redirect to the previous screen to show the fields selected by the user mapped and populated beside the corresponding object.

#### Auto-Mapping unique ids for a specific object <a href="#automapping-unique-ids-for-a-specific-object" id="automapping-unique-ids-for-a-specific-object"></a>

1. In the **Unique Identifiers** screen, click on the **Auto-Map** button.
2. Vault will fetch the info of the fields that are unique in Salesforce but not auto-increment to map automatically with all the objects in the org.
3. This is time-taking process, the user will be notified once the auto-map process is done.

#### Cloning same config to multiple orgs <a href="#cloning-same-config-to-multiple-orgs" id="cloning-same-config-to-multiple-orgs"></a>

1. In the **Unique Identifiers** screen, click on the **Clone to another Org** button.
2. This will show a popup with the Salesforce Org registered in Vault in dropdown with at least one object mapped.
3. Click on **Clone**.
4. This will check for the availability of the same objects and fields in the new org and perform the same mappings as the source.

\
