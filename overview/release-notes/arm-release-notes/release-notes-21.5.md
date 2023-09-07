# Release Notes 21.5

**August 2021 - Version 21.5 - Enhancements, and Changelogs**

Date of Release: _29 August 2021_

\


**On this page:**

1. [Enhancements](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#enhancements)
2. [Changelogs](https://knowledgebase.autorabit.com/arm/docs/arm-release-notes-215#changelogs)

\


In keeping with our dedication to continual improvement, the **August-21 (AR 21.5)** release delivers a plethora of exciting upgrades and improvements to our AutoRABIT application.

#### Enhancements <a href="#enhancements" id="enhancements"></a>

* **UI/UX Improvements:** Focused on application performance and user experience. Try it out for yourself and let us know how to feel:
  * **Page Navigation:** When working with several records, breaking data into multiple pages is always a good idea. You can now view 25, 50, 75, or 100 records on a single page, and use the **Previous** and **Next** buttons to switch to the previous or next page. This feature is now only available in the Version Control module, but it will be expanded to other modules in future releases.
  * **Never miss a required field:** You will be prompted to fill in all the required fields before you proceed. Follow the UI highlights to minimize rework.
* **Customize CI jobs for desired Salesforce API versions:** To support different Salesforce API versions for distinct Salesforce orgs instead of a global setup, we've added a new checkbox named **Salesforce API version** across the CI Job module. This will offer a granular facility in a CI job to select the required Salesforce API version.
* **Improved Audit Trail Report:** Additional data was added to the reports to support improved report analysis.
* **Performance Improvement:** Waiting is always boring- we have reduced that wait for you.
* **Salesforce CLI Upgrade-** Salesforce CLI upgraded to the latest stable **7.112** version.

#### &#x20;<a href="#undefined" id="undefined"></a>

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 14 November 2021 <a href="#14-november-2021" id="14-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed deployment issues
  * Fixed an issue where no metadata was found while validating the components from the master branch to the production environment ([#38612](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064709627), [#38587](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064645657), [#38571](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639413), [#38537](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064517581), [#38552](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064584042), [#38549](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064544537))
  * Fixed revision based deployment issue ([#38386](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064283007))
  * Fixed an issue where the commit labels changes are not reflected in the release label ([#38569](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064646158))
  * Fixed an issue where the salesforce deployment from GIT to SFDC was not working ([#38558](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064639001))
  * Fixed deployment issue where no components were being retrieved via _Single Revision_ or _Revision Range_ ([#38550](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064581003), [#38546](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064558188))
* Fixed a bug where the deployment CI Job occurs multiple times ([#37454](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061960003)).
* Fixed the search and substitute deletion rule issue ([#38410](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064291165)).
* Fixed SFDX parent and child job triggered the issue.
* Fixed an issue where the review artifact with AutoDraft functionality was not working properly in the Ez-commit screen.

#### 07 November 2021 <a href="#07-november-2021" id="07-november-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141))
* Fixed SFDX deployment and rollback mismatches issue ([#35947](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000057045040)).
* Fixed a bug where when attempting to commit the deletion of 19 profiles, a Diff Report listing of 20 profiles was generated. ([#38303](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063932311)).
* Fixed code coverage report discrepancy issue ([#36282](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000058168335)).
* Fixed an issue where the wave template related dependent files were missing from the package \[CI, Deployment, VC].
* Fixed an issue where all existing credentials for version control mappings that were created using the **Profile** screen were reset.

#### 31 October 2021 <a href="#31-october-2021" id="31-october-2021"></a>

This is a maintenance release. The following items were fixed and/or added:

* The deleted sharing rules were not showing up in the EZ-Commit Deleted tab, which was fixed ([#37747](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062586019))
* Fixed a bug where the older commits were not accessible for merge ([#38242](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063785008)).
* Fixed an issue where when deploying a new custom object, an error _"Profile Search Layout: - System Administrator - not appropriate for object XXXXXX"_ was thrown ([#37897](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062972201)).
* Fixed a merge conflict issue([#37950](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063128003)).
* Fixed a commit label issue ([#38275](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063874030)).
* Fixed an issue with SSO where users had to log in twice before being able to use the AutoRABIT application ([#36634](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000059319963)).
* The issue with the SSO domain has been fixed ([#37232](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000061168477)).
* Fixed data loader audit logs issue ([#37688](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000062385762)).
* Fixed an issue where the users were unable to exclude _EmbeddedServiceLiveAgent_ from CI Job ([#38261](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063818321)).
* Fixed an issue where the user couldn't delete a job with special characters in its name ([#38332](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000064061141)).
* Fixed an issue where users were unable to compare profiles using the _Profile Manager_ feature in the _Deployment_ module ([#36978](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000060367023)).
* In CI Jobs, a bug with the _"Group By"_ filter was fixed ([#38132](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063522197)).
* Fixed an issue where the community site was not getting deployed ([#38226](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000063775199)).
* Fixed a bug that caused metadata retrieval to fail with a **Null** error during revision range deployment.
* \[Profile Manager] Fixed an issue where the org compare feature would not work when three orgs were configured, resulting in a "Empty screen" error.
* \[Profile manager] Fixed an issue where after comparison, duplicate metadata entries and empty popups were displayed.
* \[nCino CI Jobs] Fixed an issue where the unwanted objects are displayed on editing the cloned CI Job.
