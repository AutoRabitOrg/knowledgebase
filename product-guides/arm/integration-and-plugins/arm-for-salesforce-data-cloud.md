# ARM for Salesforce Data Cloud

## &#x20;<a href="#deploying-salesforce-data-cloud-metadata-using-autorabit-arm" id="deploying-salesforce-data-cloud-metadata-using-autorabit-arm"></a>

**Last Updated:** Oct 31st 2025\
**Applies to:** AutoRABIT ARM 25.4.5 and later<br>

### Overview <a href="#overview" id="overview"></a>

**Salesforce Data Cloud** (formerly Customer Data Platform) is not just another Salesforce cloud — it’s a **real-time customer data platform (CDP)** that unifies, harmonizes, and activates data across systems.\
ARM now supports full **Data Cloud metadata deployment** through **Data Kits**, enabling seamless movement of Data Cloud configurations between orgs.

This guide walks you through **end-to-end deployment** of Data Cloud metadata even if you’ve never used Data Cloud before.

### What is Data Cloud? <a href="#what-is-data-cloud" id="what-is-data-cloud"></a>

Data Cloud helps organizations achieve a **360° customer view** by combining and activating data from multiple internal and external systems.

| Capability            | Description                                                                    |
| --------------------- | ------------------------------------------------------------------------------ |
| **Data Unification**  | Merge CRM, transactional, web, and third-party data into one profile.          |
| **AI & Insights**     | Built-in Einstein AI generates predictive insights and segmentation.           |
| **Governance**        | Secure and compliant with GDPR, HIPAA, and encryption policies.                |
| **Activation**        | Push unified data to Sales, Marketing, and Service Clouds for personalization. |
| **Ecosystem Support** | Works with Stripe, Google Drive, Snowflake, and other external systems.        |

### Key Components of Data Cloud Metadata <a href="#key-components-of-data-cloud-metadata" id="key-components-of-data-cloud-metadata"></a>

Below are the main metadata types that define your Data Cloud configuration:

| Category                                    | Metadata Types                                                                               | Purpose                                                              |
| ------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Data Streams**                            | DataStreamDefinition, DataStreamTemplate                                                     | Define ingestion pipelines that bring external data into Salesforce. |
| **Data Lake / Model Objects (DLOs / DMOs)** | DataSourceObject, DataSourceBundleDefinition, DataPackageKitObject, DataPackageKitDefinition | Represent data structures and relationships used for unification.    |
| **Calculated Insights**                     | MktCalcInsightObjectDef                                                                      | Define metrics and aggregations.                                     |
| **Segments**                                | MarketSegmentDefinition                                                                      | Define target audiences or customer groups.                          |
| **Activation Targets**                      | ActivationPlatform\*, ActvPlatformField\*, ActvPlatformAdncIdentifier                        | Push data or segments to external systems.                           |
| **Identity Resolution**                     | IdentityResolutionRuleSet                                                                    | Define how profiles are matched and merged.                          |
| **Data Actions**                            | DataAction, DataTrigger                                                                      | Trigger workflows when data changes.                                 |
| **Search Indexes (Vector DB)**              | Vector Search Retrievers                                                                     | Power semantic and search-based use cases.                           |
| **Data Spaces**                             | DataSpace                                                                                    | Logical containers for Data Cloud deployments.                       |

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

Make sure you meet the following **prerequisites** before attempting a deployment.

#### Permissions <a href="#id-1.-permissions" id="id-1.-permissions"></a>

**System Permissions:**

* API Enabled — so the user can call the APIs needed for ingestion, metadata, streams, etc.
* Modify Metadata Through Metadata API Functions — to allow changes to metadata (objects, fields, permission sets) via Metadata API.
* View Setup and Configuration — required to access Setup, enabling features like Data Cloud Setup, Data Spaces, etc.

**Object and Field Access:**\
Ensure the deployment user has full access to all **Data Cloud objects and fields** referenced in Data Streams and Data Model Objects.

### Step 1: Create a DevOps Data Kit <a href="#step-1-create-a-devops-data-kit" id="step-1-create-a-devops-data-kit"></a>

1. Go to **Setup → Data Kit**.
2. Click **New DevOps Data Kit** _(ensure DevOps, not Standard, is selected)._
3. Provide a descriptive name, e.g., `Customer360_DevOpsKit_v1`.
4. Add components such as:
   * **Connections** (external data sources – credentials not migrated)
   * **Data Streams**
   * **Data Lake / Data Model Objects**
   * **Calculated Insights**
   * **Identity Resolution Rules**
   * **Segmentation Rules**
   * **Data Source Metadata**
5. Click **Download Manifest (package.xml)**.

_Note: Standard Data Kits (used in customer solutions) lock certain metadata post-installation._

### &#x20;Step 2: Commit in AutoRABIT ARM <a href="#step-2-commit-in-autorabit-arm" id="step-2-commit-in-autorabit-arm"></a>

1. Navigate to **Create New → New EZ-Commit**.
2. Select the **Data Cloud Source Org** and **DX repository** (recommended).
3. Choose **Fetch Changes from Package Manifest** and upload your `package.xml`.
4. **Do not select “Apply Auto Draft.”**
5. After retrieval, **select all components** and review for missing/deleted files.
6. Click **Commit**.
7. Once commit is complete, note the **revision number**.\
   \
   **Note:** When committing a Permission Set that includes Data Cloud Objects, you don’t need to select “**Commit Options for PermissionSet.**” ARM automatically identifies and includes the related Object and Field permissions during the commit. This is because Data Cloud metadata is already handled as part of the core Permission Set logic, so manual selection isn’t required for successful deployment.

### Step 3: Deploy in ARM <a href="#step-3-deploy-in-arm" id="step-3-deploy-in-arm"></a>

1. Go to **Create New → New Deployment**.
2. Choose **Single Revision** and pick the revision created in Step 2.
3. Select the **Target Org**.
4. Retrieve and **select all components**.
5. Click **Deploy**.

After the deployment succeeds:

* In your **target org**, navigate to\
  **Data Cloud Setup → Data Kits → \[Your Kit] → Deploy**,\
  to activate the components in the **default Data Space**.

### Step 4: Post-Deployment Tasks <a href="#step-4-post-deployment-tasks" id="step-4-post-deployment-tasks"></a>

* **Reauthorize connectors** (for ingestion/streaming) — credentials don’t migrate.
* **Verify deployment** under Deployment History.
* **Check Data Spaces** and object/field permissions.
* **Activate** Data Cloud components if required.Best Practices

### Metadata Support Matrix <a href="#metadata-support-matrix" id="metadata-support-matrix"></a>

| API Name                     | Support in ARM          | Dependent via Package.xml | Independent |
| ---------------------------- | ----------------------- | ------------------------- | ----------- |
| DataPackageKitDefinition     | Yes                     | Yes                       | -           |
| DataPackageKitObject         | Yes                     | Yes                       | -           |
| DataSource                   | Yes                     | Yes                       | -           |
| DataSourceBundleDefinition   | Yes                     | Yes                       | -           |
| DataSourceObject             | Yes                     | Yes                       | -           |
| DataSrcDataModelFieldMap     | Yes                     | Yes                       | -           |
| DataStreamTemplate           | Yes                     | Yes                       | -           |
| FieldSrcTrgtRelationship     | Yes                     | Yes                       | -           |
| DataKitObjectDependency      | Yes                     | Yes                       | -           |
| DataKitObjectTemplate        | Yes                     | Yes                       | -           |
| ActivationPlatform           | Yes                     |  -                        | Yes         |
| ActvPlatformAdncIdentifier   | Yes                     |  -                        | Yes         |
| CustomerDataPlatformSettings | Yes                     |  -                        | Yes         |
| DataConnectorIngestApi       | Yes                     |  -                        | Yes         |
| DataSourceTenant             | Yes                     |  -                        | Yes         |
| DataStreamDefinition         | Yes                     |  -                        | Yes         |
| ExternalDataConnector        | Yes                     |  -                        | Yes         |
| ExternalDataSource           | Yes                     |  -                        | Yes         |
| ExtDataTranFieldTemplate     | Yes                     |  -                        | Yes         |
| ExtDataTranObjectTemplate    | Yes                     |  -                        | Yes         |
| InternalDataConnector        | Yes                     |  -                        | Yes         |
| MarketSegmentDefinition      | Yes                     |  -                        | Yes         |
| MktCalcInsightObjectDef      | Yes                     |  -                        | Yes         |
| MktDataTranObject            | Yes                     |  -                        | Yes         |
| ObjectSourceTargetMap        | Yes                     |  -                        | Yes         |
| ActivationPlatformActvAttr   | Yes                     |  -                        | Yes         |
| StreamingAppDataConnector    | Yes                     |  -                        | Yes         |
| ActivationPlatformField      | Yes                     |  -                        |  No         |
| ActvPfrmDataConnectorS3      | Yes (Excluded for SFDX) |  -                        |             |
| ActvPlatformFieldValue       | Yes (Excluded for SFDX) |  -                        |  No         |
| AIPlugInUtteranceDef         | Yes                     |  -                        |             |
| DataConnector                | Yes                     |  -                        |             |
| DataConnectorS3              | Yes                     |  -                        |             |
| DataSourceField              | Yes                     |  -                        |             |
| ExternalDataTranObject       | Yes                     |  -                        |  No         |

\
**Testing Conclusions** -

1. The metadata types which have **Package.xml - Yes** should follow the above mentioned steps for Commit, Deployments & CI Jobs.
2. The metadata types which have **Package.xml - No** can follow the regular steps \[any type] for Commit, Deployments & CI Jobs. (Deployments might fail for the components \[Details are mentioned in the table]).
3. Merge, Release Label, Branching Baseline is working for all the metadata types with both DX & NON DX repositories.

\*\* All the above implies for both Constructive and Destructive changes.

### Quick Summary for New Users <a href="#quick-summary-for-new-users" id="quick-summary-for-new-users"></a>

* Create a **DevOps Data Kit** with all your Data Cloud metadata.
* Use **EZ-Commit** with `package.xml` (DX repo only).
* Deploy via **Single Revision** and activate from **Data Cloud Setup**.
* Always reauthorize connectors and verify Data Space configurations.
* Do **not** mix standard Salesforce metadata with Data Cloud types.
