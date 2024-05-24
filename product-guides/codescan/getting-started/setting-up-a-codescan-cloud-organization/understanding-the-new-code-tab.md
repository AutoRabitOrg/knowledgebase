# Understanding the New Code Tab

The CodeScan **New Code** tab is a great way to keep track of new issues in your project.

How the **New Code** is set determines what issues are displayed as new issues. There are several options for this. The **New Code** can be configured for the specific project by navigating to the **Project Settings > New Code** menu from the project dashboard.

<figure><img src="../../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

The **New Code** settings can be configured for the project or each branch by clicking on the settings wheel (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-P2L8U745.png)) at the bottom of this page.

<figure><img src="../../../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

#### Date <a href="#date" id="date"></a>

By entering a date in the format **yyyy-mm-dd**, SonarQube™ will show the issues that have arisen since that date.

#### Number of days <a href="#number-of-days" id="number-of-days"></a>

SonarQube™ can be set to show the issues that have arisen within a certain number of days by entering the desired number. Remember that the issues found in the last **5 days** will not be the same as a week from now.

#### Previous version <a href="#previous-version" id="previous-version"></a>

By using the _**previous\_version**_ setting, the New Code will be tracked from the previous version set with the _**sonar.projectVersion**_ parameter or from the Activity page.

For example, a scan is run on a project with the _**sonar.projectVersion**_ _**1.0**_ . After time, the project’s _**sonar.projectVersion**_ is set to _**1.1**_. The New Code Period set to _**previous\_version**_ would display all issues that have arisen since _**sonar.projectVersion**_ _**1.0**_.

#### Reference Branch <a href="#reference-branch" id="reference-branch"></a>

The reference branch option compares all issues in the current branch to those in the specified reference branch. The New Code Tab will display the delta of those issues.

For example, the main branch of your project is pointing to a production environment. A second branch in your project is pointing at a developer environment. By defining the main branch as the reference for the second branch, you will be able to track new issues created in that developer environment.

#### Specific version <a href="#specific-version" id="specific-version"></a>

By entering _**sonar.projectVersion**_ into your projects, the New Code Period will display any issues that have arisen since that specific version.

For example, a scan is run on a project with the _**sonar.projectVersion**_ _**BASELINE**_. The project’s _**sonar.projectVersion**_ is then set to _**DEVELOPMENT**_ and all necessary scans are run over time. The New Code Period set to _**BASELINE**_ would display all issues that have arisen since the original scan.

It is important to note that all violations, including when they were introduced and the version in which they were introduced, are tracked. The New Code Period only filters this information on the project’s Overview dashboard and the Issues screen.

### Abnormalities <a href="#abnormalities" id="abnormalities"></a>

#### Added Files <a href="#added-files" id="added-files"></a>

Problems can arise when users baseline projects with an entire code base and use the same project key to compare branches of code. It will count the files added as new files if the branch does not contain your full code base and you add files to your branch that were present in the initial baseline scan. This means all the violations in those files will register as new violations.

There are two options to avoid this:

1. Make sure your entire codebase is present in the branch, not just the files you are working on.
2. Baseline your project with the full code base before every scan.

#### Only One Version <a href="#only-one-version" id="only-one-version"></a>

If only one version is present in your project and the New Code Period is set to its default (_**previous version**_), it may not display properly. To display the New Code Period correctly, set the versions of your project scans with _**sonar.projectVersion**_ or set the New Code Period to a specific date or number of days as mentioned above.

#### More information: <a href="#more-information" id="more-information"></a>

Click here to explore more on SonarQube™, [SonarQube™: Clean As You Code](https://docs.sonarqube.org/latest/user-guide/clean-as-you-code/)
