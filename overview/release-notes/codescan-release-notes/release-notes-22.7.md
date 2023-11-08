# Release Notes 22.7

**October 2022 - New Features, Enhancements, Improvements, and Bugs Fixed**

### New Features <a href="#new-features" id="new-features"></a>

#### 1. SAML-based SSO for login <a href="#1-samlbased-sso-for-login" id="1-samlbased-sso-for-login"></a>

You can easily log in to CodeScan Cloud by setting up a Single Sign-On (SSO) through SAML-based third-party identity providers such as Okta, PingOne, and Microsoft Azure.

For more information, see [Single Sign-On](https://knowledgebase.autorabit.com/codescan/docs/single-sign-on-sso).

#### 2. CSV Export tool for CodeScan Cloud <a href="#2-csv-export-tool-for-codescan-cloud" id="2-csv-export-tool-for-codescan-cloud"></a>

The ability to download a CSV file containing the issues has now been added. The CodeScan **CSV issue export** option can be found in the **More** menu. Prior to this release, this functionality was only accessible to CodeScan Self-Hosted users; however, we have now enabled support for Cloud users as well.

For more information, see [Exporting Issues in CodeScan Cloud](https://knowledgebase.autorabit.com/codescan/docs/exporting-issues-in-codescan-cloud)

#### 3. New CodeScan Rule <a href="#3-new-codescan-rule" id="3-new-codescan-rule"></a>

CodeScan now has a new rule added to their Quality Profile called `Do not use vulnerable packages,` which checks for deprecated and outdated dependencies in the project and highlights the vulnerabilities available.



### Enhancements <a href="#enhancements" id="enhancements"></a>

#### Scheduled Reports available for Project Branches <a href="#scheduled-reports-available-for-project-branches" id="scheduled-reports-available-for-project-branches"></a>

Previously, project reports were available for download for the main branches. With this update, we now support generating reports manually or by scheduling them for every project branch.

For more information, see [Scheduled Reports](https://knowledgebase.autorabit.com/codescan/docs/scheduled-reports)

#### UX Enhancement <a href="#ux-enhancement" id="ux-enhancement"></a>

1. The drop-down list for the entry of Rule Parameters has been introduced to the improved **Activate in Quality Profiles** page. You could only feed regular text into fields prior to this release.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Z50YWBQ7.png)

Fig 1: Old Screen\


![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GQ2NQX2R.png)

Fig 2: New Screen\


2. With this update, the **Add Member** button on the **Members** page for all CodeScan versions is deleted.



### Improvements <a href="#improvements" id="improvements"></a>

* This release includes significant security improvements. Updating is strongly recommended.
* The existing metadata rules in CodeScan have been tweaked for SFDX compatibility.
* Significant improvements in the ways GitHub is triggered within CodeScan.



### Bugs fixed <a href="#bugs-fixed" id="bugs-fixed"></a>

* Fixed a minor issue where the analysis would start for both branches when merging a feature branch into the master branch. This shouldn't happen as analysis should be initiated only on the master branch and not the feature branch.
* Fixed an issue where the target branch's newly added code was not being fetched when the analysis was running.
* Fixed an issue where users could view invalid grant type errors while running a pull request analysis.
* Fixed an issue where users received a CE job timeout error in SonarQube's CE job.
