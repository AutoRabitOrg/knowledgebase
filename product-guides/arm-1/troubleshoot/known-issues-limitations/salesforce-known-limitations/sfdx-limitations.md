# SFDX Known Limitations

## Salesforce DX Known Issues <a href="#salesforce-dx-known-issues" id="salesforce-dx-known-issues"></a>

These are the known issues for [Salesforce DX](../../../../arm/salesforce-dx.md) in this release.

**Failed to initiate deployment**\
If a process is added to Salesforce's queue for more than 30 minutes during the deployment of CI Jobs with SFDX Repo as the source, the error **"Failed to initiate deployment"** is returned.

## Salesforce DX Known Limitations <a href="#salesforce-dx-known-limitations" id="salesforce-dx-known-limitations"></a>

Below are the limitations of ARM related to salesforce dx:

1. [Salesforce DX](https://www.autorabit.com/blog/the-basics-of-salesforce-dx/) functionality is currently applicable only for DX-enabled version control repositories.
2. Source commit from EZ-Commit process will be done only in DX-format for SFDX enabled repositories.
3. It is mandatory to select the **SFDX Package Directory** for DX-enabled repositories while carrying out the EZ-Commit operation.
4. Dependencies will be calculated using **Salesforce Dependency API**.
5. Adding dependencies are subject to the **API limitations**.
6. In **SFDX > Modularization**, the data will be extracted only if the **CustomObject** metadata either selected/identified as a dependency.
7. A new package version gets generated each time the packages get updated. However, if you would like to install the updated packages to the same Salesforce org, the packages will not get installed. To do so, uninstall the current package from the Salesforce org and install the latest one **(Custom Deployment)**.
8. For a module or an unlocked package creation request is in progress, make sure for the same repository and branch, another creation request is not submitted.
9. The user should not include such metadata members in a package directory of a branch if the same metadata members are already available for another package directory for the same branch.
10. Profiles will not be included in the **Unlocked Packages**.
11. Listed below in the table the metadata types which are currently not supported in the DX format:

| AccountRelationshipShareRule | AnalyticSnapshot           | Audience           |
| ---------------------------- | -------------------------- | ------------------ |
| AccountRelationshipShareRule | AnalyticSnapshot           | AssessmentQuestion |
| AssessmentQuestionSet        | Audience                   | ApexTestSuite      |
| AIApplicationConfig          | BlacklistedConsumer        | CMSConnectSource   |
| CustomIndex                  | AIApplication              | ForecastingType    |
| ForecastingFilter            | ForecastingFilterCondition | InboundCertificate |

