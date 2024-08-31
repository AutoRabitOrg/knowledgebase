---
description: CodeScan Release 23.1
---

# Release Notes 23.1

### Major Updates <a href="#key-updates" id="key-updates"></a>

**23 April 2023 Release Date**

**(CodeScan v 23.1.0)**

#### 1. New policy rules added for Salesforce Metadata <a href="#id-1-new-policy-rules-added-for-salesforce-metadata" id="id-1-new-policy-rules-added-for-salesforce-metadata"></a>

<table data-full-width="true"><thead><tr><th width="120">Serial No.</th><th width="194">Rule Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Profile - Developer Policy</td><td><strong>Profile - Developer Policy</strong> gives visibility on access permissions related to Author APEX, Import Custom Objects. This violation means that this Profile conflicts with your policy for these settings.</td></tr><tr><td>2</td><td>Profile - Password Policy</td><td><strong>Profile - Password Policy</strong> gives visibility on access permissions related to Passwords Expiry, Enforce password History, Minimum Password Length, Password Complexity Requirement, Password Question Requirement, Maximum Invalid Login Attempts, Lockout Effective period, Obscure answer for password resets, Require minimum One Day password lifetime, Don't Immediately expire links in forgot password emails.</td></tr><tr><td>3</td><td>PermissionSet - Security Settings Policy</td><td><strong>PermissionSet - Security Settings Policy</strong> gives visibility on access permissions related to Manage Certificates,Manage IP Addresses,Manage Encryption Keys,View Threat Detection Events,Profile allows Manage Security Center.</td></tr><tr><td>4</td><td>PermissionSet - Flows Policy</td><td><strong>PermissionSet - Flows Policy</strong> gives visibility on access permissions related to Run Flows, Flows Policy, Manage Flow. This violation means that this Permission Set conflicts with your policy for these settings.</td></tr><tr><td>5</td><td>Profile - API Admin Policy</td><td><strong>Profile - API Admin Policy</strong> gives visibility on API Admin permissions.</td></tr><tr><td>6</td><td>Profile - Security Settings Policy</td><td><strong>Profile - Security Settings Policy</strong> gives visibility on access permissions related to IP Restrict Requests,Manage Certificates,Manage IP Addresses,Manage Encryption Keys,View Threat Detection Events,Profile allows Manage Security Center.</td></tr><tr><td>7</td><td>PermissionSet - Packages Admin Policy</td><td><strong>PermissionSet - Packages Admin Policy</strong> gives visibility on access permissions related to Create and Update Second-Generation Packages, Delete Second-Generation Packages, Manage Package Licenses, Download AppExchange Packages, Create AppExchange Packages, Upload AppExchange Packages.</td></tr><tr><td>8</td><td>PermissionSet - Platform Admin Policy</td><td><strong>PermissionSet - Platform Admin Policy</strong> gives visibility on Platform Admin permissions.</td></tr><tr><td>9</td><td>PermissionSet - User Management Policy</td><td><strong>PermissionSet - User Management Policy</strong> gives visibility on access permissions related to Manage Users, Manage Roles, Assign Permission Sets, Reset Passwords and Manage Internal Users.</td></tr><tr><td>10</td><td>Profile - Packages Admin Policy</td><td><strong>Profile - Packages Admin Policy</strong> gives visibility on access permissions related to Packaging2, Packaging2Delete, ManagePackageLicenses, InstallPackaging, CreatePackaging, PublishPackaging.</td></tr><tr><td>11</td><td>PermissionSet - Data Admin Policy</td><td><strong>PermissionSet - Data Admin Policy</strong> gives visibility on access permissions related to Manage Data Categories, View All Data, Manage Data Integrations, ModifyAllData , View Encrypted Data, Weekly Data Export, Edit Read Only Fields.</td></tr><tr><td>12</td><td>PermissionSet - Developer Policy</td><td><strong>PermissionSet - Developer Policy</strong> gives visibility on access permissions related to Author APEX, Import Custom Objects.</td></tr><tr><td>13</td><td>Profile - Data Admin Policy</td><td><strong>Profile - Data Admin Policy</strong> gives visibility on access permissions related to Manage Data Categories, View All Data, Manage Data Integrations, ModifyAllData , View Encrypted Data, Weekly Data Export, Edit Read Only Fields.</td></tr><tr><td>14</td><td>PermissionSet - Files and Content Policy</td><td><strong>PermissionSet - Files and Content Policy</strong> gives visibility on access permissions related to Files Connect Cloud.</td></tr><tr><td>15</td><td>Profile - Platform Admin Policy</td><td><strong>Profile - Platform Admin Policy</strong> gives visibility on Platform Admin permissions.</td></tr><tr><td>16</td><td>Profile - Reports and Dashboards Admin Policy</td><td><strong>Profile - Reports and Dashboards Admin Policy</strong> gives visibility on access permissions related to Create Report Folders, Manage All Private Reports and Dashboards, Create and Customize Reports, Manage Reports in Public Folders, Manage Dashboards in Public Folders, Manage Custom Report Types, Report Builder, Report Builder (Lightning Experience), Run Reports, Create and Customize Dashboards, Manage Dynamic Dashboards, Export Reports.</td></tr><tr><td>17</td><td>PermissionSet - Permissions Admin Policy</td><td><strong>PermissionSet - Permissions Admin Policy</strong> gives visibility on access permissions related to Manage Profiles and Permission Sets, Manage Sharing, Multi-Factor Authentication for User Interface Logins, Manage Auth. Providers, Manage Custom Permissions, Manage Login Access Policies, Manage Password Policies, Allow Password Never Expires, Manage Session Permission Set Activations, Exempt from Transaction Security, Waive Multi-Factor Authentication for Exempt Users.</td></tr><tr><td>18</td><td>PermissionSet - Reports And Dashboards Admin Policy</td><td><strong>PermissionSet - Reports And Dashboards Admin Policy</strong> gives visibility on access permissions related to Manage All Private Reports and Dashboards, Create and Customize Reports, Manage Reports in Public Folders, Manage Dashboards in Public Folders, Manage Custom Report Types, Report Builder, Report Builder (Lightning Experience), Run Reports, Create and Customize Dashboards, Manage Dynamic Dashboards, Export Reports.</td></tr><tr><td>19</td><td>Organization - Session Policy</td><td><strong>Organization - Session Policy</strong> gives visibility on access permissions related to Session Timeout, Enforce login IP ranges on every request.</td></tr><tr><td>20</td><td>Profile - Flows Policy</td><td><strong>Profile - Flows Policy</strong> gives visibility on access permissions related to Run Flows, Flows Policy, Manage Flow.</td></tr><tr><td>21</td><td>Organization - Password Policy</td><td><strong>Organization - Password Policy</strong> gives visibility on access permissions related to Passwords Expiry, Enforce password History, Minimum Password Length, Password Complexity Requirement, Password Question Requirement, Maximum Invalid Login Attempts, Lockout Effective period, Obscure answer for password resets, Require minimum One Day password lifetime.</td></tr><tr><td>22</td><td>Profile - Session Policy</td><td><strong>Profile - Session Policy</strong> gives visibility on access permissions related to Required Session Level and Session Timeout Limit.</td></tr><tr><td>23</td><td>Profile - Files and Content Policy</td><td><strong>Profile - Files and Content Policy</strong> gives visibility on access permissions related to Query All Files, Files Connect Cloud, Manage Salesforce CRM Content, Manage Content Permissions, Manage Content Properties.</td></tr><tr><td>24</td><td>Profile - Permissions Admin Policy</td><td><strong>Profile - Permissions Admin Policy</strong> gives visibility on access permissions related to Manage Profiles and Permission Sets, Manage Sharing, Multi-Factor Authentication for User Interface Logins, Manage Auth. Providers, Manage Custom Permissions, Manage Login Access Policies, Manage Password Policies, Allow Password Never Expires, Manage Session Permission Set Activations, Exempt from Transaction Security, Waive Multi-Factor Authentication for Exempt Users.</td></tr><tr><td>25</td><td>PermissionSet - API Admin Policy</td><td><strong>PermissionSet - API Admin Policy</strong> gives visibility on access permissions related to Modify Metadata Through Metadata API Functions, Bulk API Hard Delete, API Enabled, Multi-Factor Authentication for API Logins, Manage Multifactor Auth - API, Apex REST Services, Access Customer Asset Lifecycle Management APIs, Update Consent Preferences Using REST API.</td></tr><tr><td>26</td><td>Profile - User Management Policy</td><td><strong>Profile - User Management Policy</strong> gives visibility on access permissions related to Manage Users, Manage Roles, Assign Permission Sets, Reset Passwords and Manage Internal Users.</td></tr></tbody></table>

The complete CodeScan rules list can be accessed [HERE](https://knowledgebase.autorabit.com/codescan/docs/codescan-rule-list).

***

### Improvements <a href="#improvements" id="improvements"></a>

#### UI/UX Improvements <a href="#uiux-improvements" id="uiux-improvements"></a>

{% hint style="info" %}
Note: Self-Hosted 23.1 users will not have the same UI/UX changes as Cloud Release 23.1
{% endhint %}

* New interactive and appearance have been introduced to the CodeScan **Welcome screen**. Two new options, **`Application Security Testing`** and **`Policy Management`** are offered when you first log in to CodeScan. If you select **`Application Security Testing`**, you will be directed to the **Projects** page, which is now your default homepage. As a result, when you log in to CodeScan the next time, you will be immediately redirected to the **Projects** page. Similarly, if you choose **`Policy Management`**, you will be navigated to the **Policy Results** screen, now set as your default homepage.\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-SIOPTPTQ.png)
* The **Policy Results** page can now be accessed under the **More** tab in the CodeScan application.\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-NKBAXC3W.png)

#### Other improvements <a href="#other-improvements" id="other-improvements"></a>

* This release includes minor stability fixes and improvements for the CodeScan platform.

***

### Minor Releases / Changelogs <a href="#changelogs" id="changelogs"></a>

#### **7 November 2023** <a href="#id-12-may-2023" id="id-12-may-2023"></a>

**(CodeScan  v.23.1.6)**

This update included minor improvements.&#x20;

***

#### **1 November 2023**

**(CodeScan  v.23.1.5)**

The following was updated:

<table><thead><tr><th width="282">Rule Key</th><th>Rule Title</th></tr></thead><tbody><tr><td>sf:AvoidPublicFields</td><td>Class Variable Fields should not have Public Accessibility</td></tr><tr><td>sf:AvoidUsingHardCodedId</td><td>Avoid Using Hard Coded Salesforce Id</td></tr></tbody></table>

***

#### **October 2023**

**(CodeScan  v23.1.4)**

The following rules were updated for release 23.1:

<table><thead><tr><th width="225">Rule Key</th><th>Rule Title</th></tr></thead><tbody><tr><td>sf:InsecureEndpoint<br></td><td>Avoid Cleartext Transmission of Sensitive Information<br></td></tr><tr><td>sf:SOQLInjection<br></td><td>Avoid Untrusted/Unescaped Variables in DML Query<br></td></tr></tbody></table>

***

#### **September 2023**

**(CodeScan  v23.1.3)**

What's New:

CodeScan Self-Hosted version **23.1.3** _(now compatible with **SonarQube™ version 10**_).

***

#### 31 May 2023 <a href="#id-31-may-2023" id="id-31-may-2023"></a>

**(CodeScan v23.1.2)**

This is a maintenance release. The following items were fixed and/or added:

* Starting from version **23.1.2**, CodeScan supports integration to GIT with **SSH Keys** and supports **ssh://** protocol. Connecting to GIT repository using the Secure Shell Protocol (SSH) provides a secure channel over an unsecured network. [(Learn More](https://knowledgebase.autorabit.com/codescan/docs/add-a-project-to-codescan-from-git))
* **Salesforce Spring '23 (API version 57.0) Support:** To keep our product up to current with the most recent Salesforce upgrades, CodeScan supports the most recent **API 57.0** version in this release.
* This release also includes insecure dependent libraries upgrade and other significant security improvements.

***

#### 12 May 2023 <a href="#id-12-may-2023" id="id-12-may-2023"></a>

**(CodeScan v23.1.1)**

* CodeScan self-hosted has been upgraded from _**22.8**_ to _**23.1.1**_ version.
* This release includes Apex-pmd dependency upgrade and significant security improvements. Updating is strongly recommended.

