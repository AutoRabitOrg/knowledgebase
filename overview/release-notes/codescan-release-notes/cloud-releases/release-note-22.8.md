# Release Notes 22.8

**December 2022 - New Updates, Improvements**

> Date of release: 18 December 2022\
> Article last updated: 24 April 2023

### New Updates <a href="#new-updates" id="new-updates"></a>

#### 1. User Registration Flow Enhanced for CodeScan Cloud <a href="#1-user-registration-flow-enhanced-for-codescan-cloud" id="1-user-registration-flow-enhanced-for-codescan-cloud"></a>

The user registration flow is now _enhanced_ for improved user experience in the CodeScan cloud by updating several options and removing others that no longer apply.

* **Validate Email address-** The CodeScan team to allow users to register for a new CodeScan account using corporate email addresses only.
* The users who attempt to sign up using an email domain not registered with us require approval from the CodeScan team. To simplify the approval process, it is recommended that you only invite persons whose email domains already exist with us.

#### 2. SOQL/DML Rule Upgrade <a href="#2-soqldml-rule-upgrade" id="2-soqldml-rule-upgrade"></a>

The existing CodeScan rule is now enhanced to verify if SOQL queries are in the loop. With this release, if a SOQL query is called in a loop in another method or class, the rule will now alert the users with information like _class name_, _method name_, and the _line number_ of the violation.

#### 3. CodeScan IntelliJ plugin Upgrade <a href="#3-codescan-intellij-plugin-upgrade" id="3-codescan-intellij-plugin-upgrade"></a>

The CodeScan IntelliJ plugin has been upgraded to the stable **6.1.4** version. This update improves the connection process with your server.

### Improvements <a href="#improvements" id="improvements"></a>

This release includes minor stability fixes and improvements for the CodeScan platform.

***

### Changelogs <a href="#changelogs" id="changelogs"></a>

#### 19 April 2023 <a href="#19-april-2023" id="19-april-2023"></a>

**(CodeScan v23.0.6)**

This is a maintenance release. The following items were fixed and/or added:

* Fixed the following issues with the static code analysis (SCA) report observed in ARM where,
  * SCA report shows only _ApexClass_ and _AuraDefinitionBundle_ results in ARM, whereas the CodeScan app displays the accurate issues count.
  * Log file displays the error: `Only first 10000 issues can be shown` (#[48644](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000082753293)).

***

#### 22 March 2023 <a href="#22-march-2023" id="22-march-2023"></a>

**(CodeScan v23.0.5)**

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue with the **`Custom Metadata components must have a description field`** rule. The user added the description field to their quality profile's metadata and implemented the aforementioned rule, yet the problem still persists (#[65227](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000104349078)).
* Fixed an issue where the master scan was failing in the CodeScan application. The multiple scan running for the same environment caused the issue. (#[61134](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098014584)).
* Fixed an issue where the rule was missing the below case when permissions are checked through a local variable instance:\
  **`{noformat}SObject objAcc;`**\
  **`if (objAcc != null && objAcc.getSObjectType().getDescribe().isUpdateable()) {{noformat}`**\
  This case is now added to the rule.(#[58534](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000095397001)).

***

#### 15 March 2023 <a href="#15-march-2023" id="15-march-2023"></a>

**(CodeScan v23.0.4)**

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **`Avoid running Soql and DML inside loops`** rules were not evaluating properly and throws wrong issue (#[62432](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000100116773)).
* Fixed an issue with the integration of VS Code and CodeScan where, when a user clicked on the quality profile in the project information page, they were sent to a screen that read, **`The requested Quality Profile was not found`** (#[63569](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000101941939)).

***

#### 28 Feb 2023 <a href="#28-feb-2023" id="28-feb-2023"></a>

**(CodeScan v23.0.3)**

This is a maintenance release. The following items were fixed and/or added:

* Fixed an issue where the **`\triggers`** and **`\aura`** folders were not scanned for full code coverage. (#[62178](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000099818356)).
* Added a new column **Rull Name** to the CSV export report for better issue/rule identification (#[53040](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000087182005)).
* Fixed an issue where the users were not receieving notification for _My issues/My new issues/Issues_ with false positive although the notifications feature was enabled (#[61309](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000098509229)).
* Fixed an issue where the user when initiated a manual analysis inside CodeScan, the application throws the **`classes/WSRS_DistributionPartnerDAEventHandler.cls`** error (#[59746](https://support.autorabit.com/support/autorabit/ShowHomePage.do#Cases/dv/241415000096706361)).
* Fixed an issue whehre the unit test did not include the System.Assert() Update.
* Update the input text on the **SSO Login** screen from **"Your company email"** to **“Company SSO Domain”**.
