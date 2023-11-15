# Release Note 23.2

**September 2023 - Version 23.2**

This update introduces several significant improvements that will enhance your ability to maintain high-quality code and improve your security posture. This includes:

* Greater flexibility and easier maintenance of Quality Profiles
* Enhanced Token Generation
* Improved editing control over Quality Gates
* MuleSoft rules library with scanning XML configuration files
* UI/UX updates and improvements

**1. Maintenance of Quality Profiles**\
A new update was made to the screen where Quality Profiles are maintained. With this release, users can:

* **Extend an existing Quality Profile**: When you extend a profile, you create a child profile that inherits all the _activated_ rules in the parent profile. You can then activate additional rules in the child beyond those inherited.
* **Copy an existing Quality Profile**: When you copy a profile, you clone all activated rules of the original. From here, you independently activate or deactivate rules to fit your needs; your new profile will not inherit changes made to the original profile.
* **Create a blank Quality Profile**: Create a new custom profile and activate rules per your organization’s needs.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-V9S4EKAH.png)

Additionally, you can see your profile's inheritance hierarchy and change the parent profile by selecting the **Change Parent** option. Selecting the parent profile is now mandatory.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YGGDXDLP.png)

**2. Enhanced Token Generation**\
You can generate new tokens at **User > My Account > Security**.

You can now create two types of tokens: _**project analysis tokens**_ and _**user tokens**_. A _project analysis token_ allows you to run analyses on the project it was generated for. A _user token_ gives you all the permissions of the user who issued it. For example, a global Admin's user token gives you full rights to the instance.

You can select an expiration for your token or choose ‘**no expiration**.’ If you select an expiration date, you will receive an email seven days before your token's expiry date to remind you to rotate your token.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-LQG458EU.png)

**3. Improved editing control of Quality Gates**

_**Quality Gates permissions**_

The Quality Gates page now includes a section called '**Permissions**.' By default, users with the global '**Administer quality gates**' permission can edit quality gates.

Furthermore, CodeScan enables users with the global '**Administer quality gates**' permission to grant specific permissions to individuals or user groups for managing a particular quality gate. These permissions apply only to the specific quality gate and not all quality gates.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-BA7E5GYX.png)

_**Editing Quality Gates**_

Each quality gate condition comprises a _measure_, a _comparison operator_, and an _error value_.

In the latest update, users with the global '**Administer quality gates**' permission must use the **Unlock** editing feature for adding or modifying existing conditions for quality gates.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-RJCDWCCV.png)

**4. Scanning MuleSoft XML configuration files**\
CodeScan’s new MuleSoft scanner tool analyzes the security settings of sensitive configuration files to ensure vulnerabilities aren’t introduced to the system. For example, this tool can check if the credentials for a third-party database access are properly encrypted.

**Setup:**

**1. Navigating to Your MuleSoft Project from Git**\
Once you've created your MuleSoft project from Git, understanding the project's navigation and configuration becomes essential.

**2. Accessing the MuleSoft Project Dashboard**

* Click on the name of your MuleSoft project.
* This action will redirect you to the dashboard, where you can view the quantity of each type of issue present in your project.

**3. Viewing & Filtering Issues**\
On the dashboard, the numbers indicate different issue types. Clicking on any of the numbers will present a filtered list based on the issue type.

Alternatively, to see all issues:

* Click on the **Issues** tab at the top of the screen.
* Here, you can manually filter issues using the menu on the left.
* Filter options include **Type**, **Severity**, and the specific **Rule** causing the issue.

**4. Configuring a Quality Profile for Mule Language**\
A quality profile determines the issues that appear on your dashboard.

* Go to the organization screen.
* Click on **Quality Profiles**.
* Filter your profiles by selecting **Mule**.
* Here, you'll see the built-in profiles available for Mule versions 3 and 4.

**Creating a New Quality Profile**\
You can create a new profile in two ways:

1. Copy an existing built-in profile and start editing it.
2. Create a new profile from scratch.

For an in-depth look at this process, refer to the upcoming **Quality Profiles** video.

**5. Understanding Mule Quality Profile Rules**

* Inside your mule quality profile, you'll find rules that govern the profile's behavior.
* Click on the number of rules to view a filtered list of active rules within that profile.

For details on a rule:

* Click on any rule name. This provides a description of the rule and any parameters it contains.

**6. Analyzing Your MuleSoft Project**

* Click on the name of your MuleSoft project.
* Navigate to the **More** tab at the top of the screen.
* Choose **Project Analysis** from the dropdown menu.

**Manual Analysis**

* Click on the **Run Manual Analysis** button positioned at the top right corner.
* Then select **Analyze Now**.

**Automated Analysis**\
An analysis will automatically start on your MuleSoft project under the following conditions:

1. Any changes are pushed to your specified branch in your Git project.
2. A pull request is made against your selected branch.



**5. UI/UX Updates and Improvements**

_**Enabling key shortcuts**_

Various actions in CodeScan can be performed using keyboard shortcuts. Use the question mark shortcut (hit **?** on your keyboard) for a list of available keyboard shortcuts while working with CodeScan.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-FO6P60GB.png)

_**Additional UI/UX Updates**_

1. The **Projects** tab is newly added to CodeScan in this release. See **My Account > Projects** for a list of projects you are administering. You can select a project from there for full access.
2. The link "**Why is this an issue?**" on the **Issues** home screen has been relocated within each individual issue. Now when you click on an issue, a new page opens with two sections on the right side: **Where is the issue?** and **Why is this an issue?**

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XX287W89.png)

Original screen

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-5P9RYS7V.png)

New screen

3. A new addition to the **My Projects** section is the inclusion of the **My Favorites | All** tab. Under the **My Favorites** tab, you will find a collection of projects you marked as favorites. Selecting the **All** tab will display all the projects currently added in your organization.

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0MYSLQL9.png)

#### Other Improvements

Minor performance enhancements, bug fixes, and security improvements can also be observed in the CodeScan portal.
