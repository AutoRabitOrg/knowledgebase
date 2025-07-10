# Unique Identifier (UID)

## What is a Unique Identifier (UID) in Vault? <a href="#what-is-a-unique-identifier-uid-in-vault" id="what-is-a-unique-identifier-uid-in-vault"></a>

A Unique Identifier (UID) is a field that distinguishes one record from all others in Vault. It enables Vault to accurately reference, map, and synchronize individual records between Salesforce Orgs—preventing confusion or accidental duplication during operations.

## Why UID is Necessary for Each Record <a href="#why-uid-is-necessary-for-each-record" id="why-uid-is-necessary-for-each-record"></a>

Vault cannot inherently track records between source and destination orgs—especially post-sandbox refresh—since the internal record mapping is not preserved. A UID allows Vault to identify and match records between environments, ensuring continuity and preventing record duplication during replication or restoration.

## What Problem Are We Solving? <a href="#what-problem-we-are-solving-here" id="what-problem-we-are-solving-here"></a>

This feature enables configuration of unique identifiers per object in Salesforce, facilitating:

- Accurate data replication across Orgs.
- Avoidance of duplicate record creation.
- Preservation of object relationships across environments.

## Configuring Unique Identifier <a href="#configuring-unique-identifier" id="configuring-unique-identifier"></a>

### Mapping Unique ID for a Specific Object <a href="#mapping-unique-id-for-a-specific-object" id="mapping-unique-id-for-a-specific-object"></a>

1. In **Vault**, navigate to **Setup**, then select your **Salesforce Org**.
2. Go to the **Unique Identifiers** tab to view all objects and existing UID mappings.
3. Click **Map** next to the desired object. This will display all fields available in that object, including field types and UID eligibility.
4. Select the appropriate field(s) as the unique identifier(s).
5. Click **Save**. The screen will update with your selection mapped next to the corresponding object.

### Auto-Mapping Unique IDs for Specific Objects <a href="#automapping-unique-ids-for-a-specific-object" id="automapping-unique-ids-for-a-specific-object"></a>

1. From the **Unique Identifiers** tab, click **Auto-Map**.
2. Vault will scan and auto-select non-auto-increment unique fields across all objects.
3. This may take some time; Vault notifies the user upon completion.

### Cloning the Same UID Config to Multiple Orgs <a href="#cloning-same-config-to-multiple-orgs" id="cloning-same-config-to-multiple-orgs"></a>

1. In the **Unique Identifiers** tab, click **Clone to Another Org**.
2. A dropdown will display all Salesforce Orgs registered in Vault that have at least one UID mapping configured.
3. Select the destination Org and click **Clone**.
4. Vault will check for the presence of identical objects and fields in the target Org and replicate the UID mappings.
