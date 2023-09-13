# Release Note 23.2

### CodeScan 23.2.0 Release Notes

**Sep 2023 Update**

**September 2023 - Version 23.2.0**

This update introduces several significant improvements that will enhance your ability to maintain high-quality code and improve your security posture. This includes:

* Greater flexibility and easier maintenance of Quality Profiles
* Enhanced Token Generation
* Improved editing control over Quality Gates
* Mulesoft rules library with scanning XML configuration files
* UI/UX updates and improvements

**1. Maintenance of Quality Profiles**\
A new update was made to the screen where Quality Profiles are maintained. With this release, users can:

* **Extend an existing Quality Profile**: When you extend a profile, you create a child profile that inherits all the activated rules in the parent profile. You can then activate additional rules in the child beyond those inherited.
* **Copy an existing Quality Profile**: When you copy a profile, you clone all activated rules of the original. From here, you independently activate or deactivate rules to fit your needs; your new profile will not inherit changes made to the original profile.
* **Create a blank Quality Profile**: Create a new custom profile and activate rules per your organization’s needs.\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-V9S4EKAH.png)

Additionally, you can see your profile's inheritance hierarchy and change the parent profile by selecting the **Change Parent** option. Selecting the parent profile is now mandatory.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YGGDXDLP.png)

**2. Enhanced Token Generation**\
You can generate new tokens at **User > My Account > Security**.

You can now create two types of tokens: _**project analysis tokens**_ and _**user tokens**_. A _project analysis token_ allows you to run analyses on the project it was generated for. A _user token_ gives you all the permissions of the user who issued it. For example, a global admin's user token gives you full rights to the instance.

You can select an expiration for your token or choose ‘**no expiration**.’ If you select an expiration date, you will receive an email seven days before your token's expiry date to remind you to rotate your token.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-LQG458EU.png)

**3. Improved editing control of Quality Gates**\
_**Quality Gates permissions**_\
The Quality Gates page now includes a section called '**Permissions**.' By default, users with the global '**Administer quality gates**' permission can edit quality gates.

Furthermore, CodeScan enables users with the global '**Administer quality gates**' permission to grant specific permissions to individuals or user groups for managing a particular quality gate. These permissions apply only to the specific quality gate and not all quality gates.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-BA7E5GYX.png)

_**Editing Quality Gates**_\
Each quality gate condition comprises a _measure_, a _comparison operator_, and an _error value_.

In the latest update, users with the global 'Administer quality gates' permission must use the Unlock editing feature for adding or modifying existing conditions for quality gates.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RJCDWCCV.png)

**4. Scanning MuleSoft XML configuration files**\
CodeScan’s new MuleSoft scanner tool analyzes the security settings of sensitive configuration files to ensure vulnerabilities aren’t introduced to the system. For example, this tool can check if the credentials for a third-party database access are properly encrypted.

**5. UI/UX Updates and Improvements**\
_**Enabling key shortcuts**_\
Various actions in CodeScan can be performed using keyboard shortcuts. Use the question mark shortcut (hit **?** on your keyboard) for a list of available keyboard shortcuts while working with CodeScan.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-FO6P60GB.png)

_**Additional UI/UX Updates**_

1. The **Projects** tab is newly added to CodeScan in this release. See M**y Account > Projects** for a list of projects you are administering. You can select a project from there for full access.
2. The link "**Why is this an issue?**" on the\*\* Issues\*\* home screen has been relocated within each individual issue. Now when you click on an issue, a new page opens with two sections on the right side: "**Where is the issue?**" and "**Why is this an issue?**"\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XX287W89.png){height="" width=""}\
   Original screen

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-5P9RYS7V.png){height="" width=""}\
New screen

3. A new addition to the **My Projects** section is the inclusion of the **My Favorites | All** tab. Under the **My Favorites** tab, you will find a collection of projects you marked as favorites. Selecting the **All** tab will display all the projects currently added in your organization.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0MYSLQL9.png)

#### Other Improvements <a href="#other-improvements" id="other-improvements"></a>

Minor performance enhancements, bug fixes, and security improvements can also be observed in the CodeScan portal.
