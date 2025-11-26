# Deployment

### Deployment Known Limitations <a href="#deployment-known-limitations" id="deployment-known-limitations"></a>

This section summarizes the deployment limits that ARM users should consider:

1. **Unable to remove Field Level Security (FLS) in Profiles while performing destructive changes on fields**- As of now, ARM does not support the deletion of references from Profile on a branch level. But, it is on our roadmap, and the development team is already working on it.
2. While performing deployment from one sandbox to sandbox, there are certain metadata types such as Email Template, Reports, Dashboards, Documents, etc. for which the selected folder path metadata will not get retrieved in the **Compare Metadata and Deploy** screen.
3. The **Compare Metadata & Deploy** functionality for **Profile** metadata will not show the correct difference since the source side displayed delta changes while the destination side retrieved the entire profile from the destination org.
4. **AccelQ** applies only to the deployment of [Salesforce Org](/broken/pages/9pLgfInGvztETx4cXCc2) and not Vlocity.
5. Rollback initiated for a successful deployment shows **No Changes** status in the build.
6. **Pre-destructive changes and deployment changes run in separate threads in ARM, but the status of the deployment changes is only seen:** Pre-destructive changes and deployment will be sent to Salesforce as part of the same request, and Salesforce will treat them as separate actions. To check the status of pre-destructive changes in ARM, click on your **Deployment Label** then go to **Deleted Components** tab.
7. **Is it possible that my code deployment will continue if my pre-destructive changes fail for some reason?** No, because pre-destructive changes and deployment will be sent to Salesforce as part of the same request in ARM, and if one of your deployments fails, the entire process fails in ARM.
8. Due to current ARM behavior, an **object file** is considered as a **destructive change** in deployment if the object file does not exist in the branch, you commit only a field (child), and then the newly committed field is deleted from the branch. This is the case only for **Metadata API** code, not for **SFDX**.
9. In case of **Vlocity Custom Deployment**, if the **Access Key** for **Local Compilation** is incorrect, ARM is unable to capture it in the logs.
10. In **Compare Org and Deploy functionality**, a file diff will not be generated between the source and the target for **Bot Version files**.
11. If a user uses the **SFDX extension** in a **non-SFDX repository** for any metadata type, then it will not be displayed in UI as a **metadata change** and won't be picked up for deployment in **package.XML**, but the file contents will stay in the promotional **ZIP** file.&#x20;
12. When dealing with the limitations of integrating Salesforce DX (SFDX) with Vlocity components, several key considerations must be taken into account to ensure effective management and deployment of these components. Below are the **compatibility issues** that must be considered for this feature:
    * **Metadata Types**: Understand the differences in metadata types between SFDX and Vlocity. SFDX does not natively support Vlocity-specific metadata, which requires using specialized tools like the Vlocity Build Tool.
    * **Deployment Methods**: SFDX deployment methods (e.g., packages, change sets) are not fully compatible with Vlocity DataPacks, necessitating alternative deployment strategies.
    * **Hybrid Approach**:&#x20;
      * Maintain separate repositories for SFDX and Vlocity components.&#x20;
      * Use SFDX for Salesforce metadata and development, while managing Vlocity components through their own repository and tools.&#x20;
      * Follow the specific guidelines and best practices provided by Vlocity and Salesforce DX for managing and deploying each type of component.
13. For **Release Label Deployments**, ARM generates **delta metadata only** for the components listed below:&#x20;

    * For **DX Repo Release Labels**, the supported components are:
      * autoResponseRules
      * bot
      * escalationRules
      * matchingRule
      * labels
      * object
      * sharingRules
      * workflow
    * For **Non-DX Repo Release Labels**, the supported components are:
      * autoResponseRules
      * bot
      * matchingRule
      * labels
      * object
      * translation
      * sharingRules
      * workflow

    At this time, delta generation is limited to these components, and no other metadata is supported when utilizing Release Label Deployments.&#x20;
14. **Translations**: The API can’t perform **destructive changes** with the translation value. The API can **add** existing `<translation>` to custom object translation but not **delete** them.
