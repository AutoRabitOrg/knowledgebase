# Release Notes 22.4

**May 2022 - New Features, Enhancements, and Improvements**

### New Features <a href="#new-features" id="new-features"></a>

#### [Added new nCino rules](https://knowledgebase.autorabit.com/codescan/docs/codescan-rule-list) <a href="#added-new-ncino-rules" id="added-new-ncino-rules"></a>

The following are the **"ncino-goldstandard"** nCino-related rules that have been added to the current _Apex/Salesforce Metadata rule sets_.

| Rule                                      | Description                                                                                                                                               |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avoid Excess Workflow Rules per Object    | This rule is required as the objects which contain too many decisions, are complex and difficult to maintain                                              |
| Flow Decision Limits                      | Flows which contain too many decisions are complex and difficult to maintain. This rule will consider reducing the number of decisions or utilizing Apex. |
| Potential Overuse - Cross-Object Formulas | This rule is required as Salesforce does not allow more than 15 cross-object formulas per object                                                          |
| Potential Overuse - Object Lookups        | This rule is required as Salesforce does not allow more than 25 lookup relationships on a single custom object                                            |
| Potential Overuse - Relationship Objects  | This rule is required as Salesforce does not allow more than 40 relationships per object                                                                  |
| Potential Overuse - External IDs          | This rule is required as Salesforce does not allow more than 5 External IDs per object                                                                    |
| Test Class Names Should Include 'Test'    | This rule is required as Test classes should include the word 'Test' in their class names                                                                 |
| Hard Coded Email Address                  | This rule is required as to avoid hardcoded email addresses                                                                                               |

#### SonarQube compatible <a href="#sonarqube-compatible" id="sonarqube-compatible"></a>

CodeScan self-hosted is compatible with **SonarQube™ 8.9** and **SonarJS 6.2+**. For more information, see [Installing CodeScan Self-Hosted](https://knowledgebase.autorabit.com/codescan/docs/codescan-self-hosted)

### Enhancements <a href="#enhancements" id="enhancements"></a>

#### Updated existing nCino rules <a href="#updated-existing-ncino-rules" id="updated-existing-ncino-rules"></a>

Below are the exisitng CodeScan rules key that are tagged as **“ncino-goldstandard.”**

<table data-full-width="false"><thead><tr><th>Rule Key</th></tr></thead><tbody><tr><td>sf:AvoidUsingHardCodedId</td></tr><tr><td>sf:MultipleTriggersOnObject</td></tr><tr><td>sf:LongMethodName</td></tr><tr><td>sf:LongClassName</td></tr><tr><td>sf:LongTriggerName</td></tr><tr><td>sf:VariableNamingConventions</td></tr><tr><td>vf:HeaderCheck</td></tr><tr><td>sf:UncommentedEmptyMethod</td></tr><tr><td>sf:UncommentedEmptyConstructor</td></tr><tr><td>sf:CommentRequired</td></tr><tr><td>sf:UnitTestContainsTooManyAsserts</td></tr><tr><td>sf:AvoidUsingTestIsRunningTest</td></tr><tr><td>sf:OnlyOneReturn</td></tr><tr><td>sf:UnusedLocalVariable</td></tr><tr><td>sf:EmptyTryBlock</td></tr><tr><td>sf:EmptyFinallyBlock</td></tr><tr><td>sf:AvoidSoqlInLoops</td></tr><tr><td>sfmeta:ExcessiveWorkflowsOrgWide</td></tr><tr><td>sfmeta:RequireDescriptionComponent</td></tr><tr><td>sfmeta:LimitCustomFields</td></tr></tbody></table>

### Improvements <a href="#improvements" id="improvements"></a>

1. Updated all third-party libraries to the most recent versions to address security, stability, and reliability issues.
2. The CodeScan portal has been updated to include minor speed, bug fixes, and security enhancements.

### Changelog <a href="#changelog" id="changelog"></a>

#### CodeScan v22.6.2 <a href="#codescan-v2262" id="codescan-v2262"></a>

**(12 July 2022)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where Codescan and Visual Studio Code's rule and file-type issue counts were out of sync. We have updated Codescan Visual Studio Code extension to version 1.6.9, which fixes the issue with analysing metadata files ([46480](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078573029))
* Writing XPath rules based on filename on SFMeta is now supported ([44685](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000075295124)).
* There was an issue that prevented users from editing the settings for **Branches** and caused an error message that said, `Cannot read properties of undefined (reading "config")` ([46575](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078733001)).
* Resolved an issue where the **Project Analysis** jobs were stuck in the queue and were not triggered at the scheduled time ([46552](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000078677885)).
* Fixed an issue where the CodeScan-Visual Studio Code plugin failed to detect javascript errors even though SonarQube have identified it at the Salesforce Lightning web component ([46104](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000077797001)).

#### CodeScan v22.6.1 <a href="#codescan-v2261" id="codescan-v2261"></a>

**(23 June 2022)**\
This is a maintenance release. The following items were fixed and/or added:

* The `sf:UnusedFormalParameter` rule's false positive issue has been resolved ([45282](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000076355001))
* Fixed an issue that prevented `SonarQube 9.4.0` from functioning properly with `Java 11` version.
* The `sonar-java-plugin` has been updated to version `7.6.0.28201`.
* Fixed an issue for all child rule violations that happen when files are crossed (rule violation location in two different files).. This was fixed by setting the correct file location for child rule violations.
* Fixed an issue where users were experiencing an expired token error that appeared on the master branch every time a comparison branch was analysed before it ([44492](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000074950299)).

#### CodeScan v22.6 <a href="#codescan-v226" id="codescan-v226"></a>

**(13 June 2022)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue that prevented the CodeScan and Azure DevOps integration from functioning as expected. The `Azure DevOps plugin` was updated to version `1.6.8` to overcome these issues.
* Fixed an issue where the **Field Level Security Rule** displayed a false negative for the code below:\
  `update Security.stripInaccessible(AccessType.UPDATABLE, new List<vlocity_ins__ContactEmployment__c> { ceLst.get(0) }).getRecords();`

#### CodeScan v22.5 <a href="#codescan-v225" id="codescan-v225"></a>

**(30 May 2022)**\
This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue that prevented the user from logging into the CodeScan instance.
* Fixed an issue that prevented the user from creating the Salesforce project in their CodeScan instance.
* The issue where the user were not able to create a CodeScan project using the Gitlab plugin has been resolved.
* Fixed an issue where the codeScan rules which were not a part of active Quality Profiles were getting applied.
* Fixed a bug where, after logging out from the CodeScan application, the user was directed to the CodeScan's Project screen rather than being asked for their login information (username and password) when they selected the **Login with AuthO** button.
* Fixed an issue where the **Field Level Security Rule** shows false negative for the below cases:

> 1. Vulnerability detection in For-each loop. for eg., for(Contact c : \[SELECT Name FROM Contact])
> 2. Vulnerability detection in Database method calls. for eg., Database.insert(\[SELECT Name FROM Contact]);

* Migrated `IntelliJPluginErrorAction` web servlet to Spring MVC.
