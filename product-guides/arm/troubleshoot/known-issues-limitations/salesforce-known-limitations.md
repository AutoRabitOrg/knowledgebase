# Salesforce Known Limitations

This article summarizes Salesforce's known issues and limitations that AutoRABIT users should consider:

## Deployment <a href="#deployment" id="deployment"></a>

1. For Salesforce API version **45.0**, Salesforce does not allow deployment or retrieval of the **"PlatformEventChannel"** component in any environment. Therefore, AutoRABIT will not be able to retrieve the **"PlatformEventChannel"** component into the destination org even though the deployment is successful.
2. The above case is also similar to the **"PermissionSetGroup"** component (for API version 45.0 only). However, Salesforce has provision for selected customers to deploy the **PermissionSetGroup** component through a pilot program that requires agreement to specific terms and conditions. To be nominated to participate in the program, do contact Salesforce.
3. I am receiving the following error messages while trying to deploy the standard Task object: **"Value too long for field: Name maximum length is: 40"**\
   **Ans:** This is a Salesforce limitation that creates duplicate list views while performing either Selective or Full Deployment. Salesforce's R\&D team is currently working on addressing this issue.
4. While deploying controlled picklist fields with altered picklist values, I am getting an error: **"control field "XXXXXXXX" is not found"**\
   **Ans:** This is a known limitation from Salesforce.\
   **Reference:** [https://trailblazer.salesforce.com/issues\_view?id=a1p3A0000003eAfQAI\&title=deploying-controlled-picklist-fields-with-altered-picklist-values-is-failing-with-error-control-field-xxxxxxxx-is-not-found](https://trailblazer.salesforce.com/issues\_view?id=a1p3A0000003eAfQAI\&title=deploying-controlled-picklist-fields-with-altered-picklist-values-is-failing-with-error-control-field-xxxxxxxx-is-not-found)
5. While deploying picklist fields with empty values in translations, the deployment is successful; but any blank values are ignored and not persisted in the destination org. This is a known issue from Salesforce, and the Salesforce team is working to resolve it.\
   **Reference:** [https://trailblazer.salesforce.com/issues\_view?id=a1p3A000000KRWiQAO\&title=unable-to-update-translation-record-with-blank-null-value-via-metadata-api](https://trailblazer.salesforce.com/issues\_view?id=a1p3A000000KRWiQAO\&title=unable-to-update-translation-record-with-blank-null-value-via-metadata-api)
6. A report with multiple subfolders was created by the user in Salesforce, and this report was subsequently added to **Skip Members** in ARM. Next, a job was created and the **Do Not Include Skip Members** check box was selected. After the job was finished, it was discovered that the report had not been skipped as anticipated. Analysis revealed that Salesforce is not displaying information about the parent folder. So, ARM cannot retrieve the right file path for the reports contained in the sub-folders.

{% hint style="info" %}
**Important Notes:**

* This issue exists both for **CI Jobs** as well as **Deployments**, in **DX Repo** and **Non-DX Repo.**
* Jobs with skipped reports without any subfolders are working as expected.
{% endhint %}

7. It is not possible to deploy the removal of **Field dependency** values from one org to another because **Field Dependencies** cannot be removed via **Metadata API**. This is expected behavior and a known limitation from Salesforce.\
   **Reference:** [https://developer.salesforce.com/docs/atlas.enus.api\_meta.meta/api\_meta/meta\_field\_types.htm#meta\_type\_valueset](https://developer.salesforce.com/docs/atlas.enus.api\_meta.meta/api\_meta/meta\_field\_types.htm#meta\_type\_valueset)
8. A deployment in ARM might fail with the following error: **\`UNKNOWN\_EXCEPTION: An unexpected error occurred. Please include this ErrorId if you contact support.\`** This API exception is thrown by Salesforce and not by AutoRABIT. We don't have any more information about these errors. Please get in touch with **Salesforce Customer Support** and provide them with the deployment **Async Request ID** and the error message for further assistance.
9. If the **Flow Entry** criteria formulas are failing to **Commit/Deploy**, we recommend updating the **Salesforce API** **version** to **55.0** or later in ARM, then re-perform the commit/deployment, because the entry-related attributes for the **Flow** metadata were introduced in the **API version 55.0**.\
   Here's a list of the entry attributes only present in **API 55.0** from Flow metadata documentation:

<figure><img src="../../../../.gitbook/assets/image (26) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

10. **Reference:** [https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_visual\_workflow.htm](https://developer.salesforce.com/docs/atlas.en-us.api\_meta.meta/api\_meta/meta\_visual\_workflow.htm)

    To update the Salesforce API version, go to **Admin** > **My Account** > **Salesforce Settings**.

<figure><img src="../../../../.gitbook/assets/image (27) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Version Control <a href="#version-control" id="version-control"></a>

1. While performing an **EZ-Commit**, Salesforce Org is unable to retrieve the complete information on whether some members of the **WaveDataflow** metadata type are available or not in the package.xml file; and if it is available then whether it is **Added, Modified,** and **Deleted.** If the metadata type is available in the package.xml file, it will be listed in both **Added/Modified** and **Deleted** tabs. Select the metadata type in the correct tab, and it will become unavailable in the other tab immediately.
2. For Salesforce API version **57.0**, **OmniSupervisorConfig** metadata type is not supported in **Unlocked Package** creation, but is working as expected in **Commits** and **Deployments**.

## SFDX <a href="#sfdx" id="sfdx"></a>

Listed below in the table are the [metadata types](https://www.autorabit.com/blog/the-role-of-metadata-in-devops-for-salesforce/) which are currently not supported in the DX format:

| AccountRelationshipShareRule | AnalyticSnapshot       | Audience                        |
| ---------------------------- | ---------------------- | ------------------------------- |
| ApexTestSuite                | AIApplicationConfig    | BlacklistedConsumer             |
| CMSConnectSource             | CustomIndex            | AIApplication                   |
| ForecastingType              | InboundCertificate     | MLDataDefinition                |
| MLPredictionDefinition       | ManagedContentType     | MutingPermissionSet             |
| UserAuthCertificate          | UserProvisioningConfig | DecisionMatrixDefinitionVersion |
| UserAccessPolicy             | ExternalAiModel        | <p><br></p>                     |

## Profiles & Permission Sets Limitations <a href="#profiles-permission-sets-limitations" id="profiles-permission-sets-limitations"></a>

1. Any profile permission (say Object’s FLS, User permission) which holds a Boolean value is changed from True to False, the change cannot be committed to a branch through AutoRABIT.
2. Any Object CRUD for the profile is only fetched if at least one value is chosen. For example, if I change an Object CRUD from Create, Read, Update to None, this change is not fetched for Commit. In order to fetch Object CRUD at least one of Create, Edit, Read, Delete, View All, Modify All options should be selected.
3. The same behavior is applicable for Permission Sets as well. Any permission that holds Boolean value is changed from True to False, the change cannot be committed to a branch through AutoRABIT.

## Why does Salesforce recommend moving from SFDX to SFCLI?

Salesforce strongly recommends moving from SFDX to SF CLI because SF CLI is the newer, more powerful, and more flexible tool. SFDX is based on the Force.com CLI, which was originally designed for command-line developers. &#x20;

SFCLI is based on the Salesforce CLI, which was designed for a wider range of developers, including those who prefer to use a graphical user interface (GUI).&#x20;

| Feature                         | SFDX                    | SF CLI                             |
| ------------------------------- | ----------------------- | ---------------------------------- |
| Command-line interface          | Yes                     | Yes                                |
| Graphical user interface        | No                      | Yes                                |
| Programming languages supported | JavaScript              | JavaScript, Python, Java, and more |
| Power                           | Less powerful           | More powerful                      |
| Flexibility                     | Less flexible           | More flexible                      |
| Ease of use                     | More difficult to learn | Easier to learn                    |

## Limitations of SF CLI

Salesforce is aware of the limitations in SF CLI and is working to address them. One of the limitations that Salesforce is working to address includes:

**Limitation 1**: ERROR running force:source:deploy: INVALID\_OPERATION: testLevel of NoTestRun cannot be used in production organizations" occurs although "RunLocalTests" is the default test level.

**Description**: When deploying to a production instance, 'force:source:deploy -m ApexClass,' you will receive an error:

'INVALID\_OPERATION: testLevel of NoTestRun cannot be used in production organizations'

It should have a default testLevel of 'runLocalTests' for being a production org, but that isn't getting set.

**Workaround:** Run the sfdx command through \[TESTLEVEL] option.

Sample command: sfdx force:source:deploy -m ApexClass -u xxx@xxx.xxx -l RunLocalTests

Use the following links for reference:

[https://issues.salesforce.com/issue/a028c00000gAzEZAA0/error-running-%20forcesourcedeploy-invalid\_operation-testlevel-of-notestrun-cannot-be-used-in-%20production-organizations-occurs](https://issues.salesforce.com/issue/a028c00000gAzEZAA0/error-running-%20forcesourcedeploy-invalid\_operation-testlevel-of-notestrun-cannot-be-used-in-%20production-organizations-occurs)

[https://github.com/forcedotcom/cli/issues/2105](https://github.com/forcedotcom/cli/issues/2105)

_**What is AutoRABIT doing to help customers?**_

AutoRABIT is committed to delivering an exceptional customer experience. We continue to work closely with Salesforce to overcome limitations where they exist. While we jointly pursue a more elegant solution, please use the workaround cited above and continue providing the much-needed feedback that makes AutoRABIT the best choice for Salesforce DevOps. Stay tuned for our weekly updates where new information will be communicated.

## Data Loader <a href="#dataloader" id="dataloader"></a>

1. Execution Governors Limitations handled by AutoRABIT's Data Loader Pro
   * A total number of records retrieved by SOQL queries if it is greater than 50,000 limits- Dataloader Pro uses the **"Querymore"** operator to retrieve all the records that are greater than 50,000 limits.
   * SOQL query runtime before Salesforce cancels the transaction is above 120 seconds- As per the Salesforce execution governors limitation, the maximum SOQL query runtime before Salesforce cancels the transaction is 120 seconds. If it is beyond 120 seconds, this cannot be handled by our Dataloader Pro.
   * SOQL characters length should be 20,000 characters- Dataloader Pro divides a single query into multiple queries and execute them. Getting proper estimation while saving a [Dataloader](https://www.autorabit.com/blog/10-benefits-of-salesforce-data-loader/) job, is very difficult as the queries are randomly generated. This normally occurs in two different scenarios:
     * When fetching parents and child records that are linked to the master objects and
     * When extracting data of a particular object with all the linked fields. Since there are millions of records, there are more chances of the query being timed out. Therefore, it is highly recommended to create two or more jobs rather than creating a single job; apply proper filters on the master objects and select a minimum multiple reference option during execution.
2. Salesforce does not retrieve Validation rules from destination org for a particular object if the same object is duplicated and is available in **Deleted objects** list.
3. Salesforce restricts access to create an **External Id** for the following objects in AutoRABIT. These listed objects are not supported in **Dataloader Pro **_**(**for more details, refer_ _to_ [_How to perform Dataloader Pro Operation_](../../arm-features/dataloader/dataloader-pro.md), step 6_**)**_ and **Test Environment Setup **_**(**for more details, refer to_ [_Create a New Test Environment Setup_](../../arm-features/dataloader/test-environment-setup.md)_, step 5**)**_.

| ActionLinkGroupTemplate | ActivityHistory       | AccountTeamMember      | AggregateResult      | EmailStatus              | DuplicateRecordItem             | DandBCompany             |
| ----------------------- | --------------------- | ---------------------- | -------------------- | ------------------------ | ------------------------------- | ------------------------ |
| ContentDistribution     | FeedLike              | FeedTrackedChange      | Name                 | OpenActivity             | ProcessInstanceHistory          | AccountFeed              |
| AccountHistory          | AccountPartner        | AccountTag             | ApexLog              | ApexTestResult           | AssetFeed                       | AssetTag                 |
| AssignmentRule          | AsyncApexJob          | CallCenter             | CampaignHistory      | CampaignFeed             | CampaignTag                     | CaseFeed                 |
| CaseHistory             | CaseSolution          | CaseStatus             | CaseTag              | CaseTeamTemplateRecord   | ChatterActivity                 | Community                |
| CollaborationGroupFeed  | NewsFeed              | NoteTag                | OpportunityFeed      | CollaborationInvitation  | CollaborationGroupRecord        | ContactShare             |
| ContactFeed             | ContentDocumentFeed   | ContractStatus         | DashboardFeed        | ContentDocumentHistory   | DashboardComponent              | EventAttendee            |
| ContactHistory          | ContractFeed          | CronTrigger            | DashboardTag         | ContentVersionHistory    | DashboardComponentFeed          | EventTag                 |
| ContactTag              | ContractTag           | Dashboard              | DocumentTag          | EntitySubscription       | EventRelation                   | FeedComment              |
| EventFeed               | LeadHistory           | LeadFeed               | GoogleDoc            | AttachedContentDocument  | FiscalYearSettings              | FeedItem                 |
| ForecastShare           | GroupMember           | LeadTag                | LoginHistory         | OpportunityFieldHistory  | CombinedAttachment              | ProcessInstanceStep      |
| LeadStatus              | OpportunityTag        | Partner                | OpportunityStage     | OpportunityHistory       | ProcessInstance                 | Report                   |
| Period                  | Pricebook2History     | PartnerRole            | Product2Feed         | OpportunityPartner       | PermissionSetAssignment         | ReportFeed               |
| SetupEntityAccess       | QueueSobject          | SolutionFeed           | SolutionHistory      | ContractHistory          | SiteHistory                     | ReportTag                |
| SiteDomain              | Site                  | TaskFeed               |                      | UserLicense              | UserPreference                  | SolutionStatus           |
| TaskPriority            | TaskStatus            | TaskTag                | UserFeed             | TopicAssignment          | SiteFeed                        | SolutionTag              |
| UserRecordAccess        | Vote                  | ContentDocumentLink    | AccountShare         | AccountContactRole       | ApexExecutionOverlayAction      | CaseShare                |
| Activity                | AdditionalNumber      | ApexComponent          | BusinessHours        | BusinessProcess          | CaseComment                     | CategoryData             |
| ApexTestQueueItem       | UserProfileFeed       | Approval               | BrandTemplate        | CampaignShare            | CaseContactRole                 | CategoryNode             |
| CaseTeamMember          | CaseTeamTemplate      | CaseTeamTemplateMember | Document             | CollaborationGroup       | CollaborationGroupMember        | PushTopic                |
| ContentVersion          | ContentDocument       | ContractContactRole    | Holiday              | EmailMessage             | CollaborationGroupMemberRequest | IDEWorkspace             |
| EmailServicesAddress    | EmailServicesFunction | LeadShare              | MailmergeTemplate    | Note                     | DocumentAttachmentMap           | ObjectPermissions        |
| EmailTemplate           | IDEPerspective        | LiveChatTranscript     | NoteAndAttachment    | OpportunityCompetitor    | OpportunityContactRole          | Group                    |
| ProcessInstanceWorkitem | OpportunityShare      | WebLink                | ApexPage             | Organization             | RecordType                      | StaticResource           |
| CaseTeamRole            | TagDefinition         | ApexTrigger            | Folder               | PermissionSet            | Scontrol                        | UserRole                 |
| SelfServiceUser         | ApexClass             | FieldPermissions       | OrgWideEmailAddress  | Profile                  | SlaProcess                      | AssetTokenEvent          |
| TraceFlag               | Territory             | ContentAsset           | LookedUpFromActivity | AttachedContentNote      | ObjectTerritory2Association     | NetworkDiscoverableLogin |
| User                    | EmailMessageRelation  | UserAppInfo            | FeedAttachment       | NetworkActivityAudit     | NetworkUserHistoryRecent        | RecordActionHistory      |
| TodayGoal               | TestSuiteMembership   | SecurityCustomBaseline | Territory2Type       | CampaignMemberStatus     | ListEmailIndividualRecipient    | EmbeddedServiceLabel     |
| TodayGoalShare          | EmbeddedServiceDetail | OutgoingEmail          | Territory2           | UserEmailPreferredPerson | UserEmailPreferredPersonShare   | Knowledge\_\_ka          |
| ApexTestRunResult       | Stamp                 | OutgoingEmailRelation  | BatchApexErrorEvent  | ApexTestResultLimits     | StampAssignment                 | Audience                 |

However, if the user wants to migrate data on the above objects, they can do so by using the Single Dataloader operation in AutoRABIT.
