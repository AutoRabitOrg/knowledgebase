# Analysis Scope on CodeScan Cloud

An analysis scope helps you narrow your results to only the relevant issues. This reduces the noise and issues from rules that may not be relevant to certain files.

The key features of an Analysis Scope are:

* Helps you exclude certain files from detecting specific issues.
* Helps you completely ignore some files.
* Helps you exclude files from duplication detection and coverage calculations.

Follow the steps below to use the **Analysis Scope** feature on [CodeScan cloud](https://www.codescan.io/products/cloud/).

{% hint style="info" %}
CodeScan can scan 3rd party libraries only when the code is present in the file, and not when it's referenced.
{% endhint %}

1.  Open the Project under the Organization for which you need to run the analysis and navigate to **Project Settings > General Settings > Analysis Scope**.<br>

    <figure><img src="../../../.gitbook/assets/image (3) (1) (1) (3) (1) (1).png" alt=""><figcaption><p>Project Settings</p></figcaption></figure>
2.  You will now be able to view the tab, under which you can select your required specification to enable this feature during the analysis.

    *   **Wildcards:** If you scroll the tab farther to the end, you can see a portion that says “wildcards,” under which there are rules and examples, which help you understand how to enter the specifications or part of the file name to enable this feature. <br>

        <figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (3) (1) (1) (1).png" alt=""><figcaption><p>Wildcards</p></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>
3.  If we go under **files**, you will be able to view two options as follows:<br>

    <figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (3) (1) (1) (1).png" alt=""><figcaption><p>File Exclusions</p></figcaption></figure>

    * **Source File Exclusions**: to exclude source code files. Specifying an exclusion means that everything under your directory will be included in analysis except the files with paths that match your exclusion pattern.

### **Use Case: Excluding Standard Salesforce Files from Analysis**

In some Salesforce projects, standard files such as SiteLoginController.cls and SiteRegister.page are present across multiple Salesforce organizations. These files may generate issues during analysis, even though they may not be relevant to the customer’s use case. At the same time, customers may want to keep all CodeScan rules active in the Quality Profile.

#### Solution Approach

&#x20;In this scenario, use Source File Exclusions under Analysis Scope. This allows you to completely exclude specific files from analysis while keeping all rules active for the rest of the codebase.

#### Configuration Steps

1. Open the required project.
2. Navigate to Project Settings.
3. Click on General Settings.
4. Select Analysis Scope.
5. Under File Exclusions, locate Source File Exclusions.
6. Enter the file path pattern using the actual component name.
7. Save the configuration.
8. Run the analysis again.

#### Example

To exclude specific Salesforce components, use the actual component name in the file path pattern.

For example:

{% code lineNumbers="true" %}
```
**/SiteLoginController.cls
**/SiteRegister.page
```
{% endcode %}

You can also use a generic format:

{% code lineNumbers="true" %}
```
**/componentname.cls
**/componentname.page
```
{% endcode %}

These patterns ensure that the specified files are excluded from analysis wherever they exist in the project structure.

#### Note

Analysis Scope is configured at the project level. If you need to exclude the same files across multiple projects, you must add the same Source File Exclusion patterns in each project.

#### Expected Outcome

After applying the configuration, the specified files are excluded from analysis.  CodeScan rules remain active in the Quality Profile and continue to run on all other relevant files, helping reduce unnecessary noise in the analysis results.



* **Source File Inclusions**: Helps include only the specific source code files in the analysis. In a few corner cases, it is necessary to be explicit about what's included in analysis and leave out everything else, but that is not the normal case, and setting inclusions should not be the first thing you try when configuring a new project.

1.  Once the analysis is completed, go to the **Code** tab to view the files as per your specified settings.<br>

    <figure><img src="../../../.gitbook/assets/image (3) (1) (1) (3) (1) (1) (1).png" alt=""><figcaption><p>Code Tab</p></figcaption></figure>

Here are a couple of implementation examples:

*   **For Source File Exclusions**:<br>

    <figure><img src="../../../.gitbook/assets/image (4) (1) (3) (1).png" alt=""><figcaption><p>Source File Exclusions</p></figcaption></figure>



In the example above, replace generic patterns (such as \*\*/apex.cls) with the actual component name (for example, \*\*/SiteLoginController.cls).



<figure><img src="../../../.gitbook/assets/image (5) (1) (3) (1).png" alt=""><figcaption><p>Classes</p></figcaption></figure>

*   **For Source File Inclusions**:<br>

    <figure><img src="../../../.gitbook/assets/image (6) (1) (3) (1).png" alt=""><figcaption><p>Source File Inclusions</p></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (7) (1) (3) (1).png" alt=""><figcaption><p>Classes</p></figcaption></figure>

You can accomplish this by utilizing the "**Ignore Issues on Multiple Criteria**" feature in Project Settings under General Settings > Analysis Scope.

To do this, simply provide the rule key and file path name.

**Example:**<br>

<figure><img src="../../../.gitbook/assets/image (8) (6).png" alt=""><figcaption><p>Field-Level Security Vulnerabilities</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)   (1).png" alt=""><figcaption><p>Ignore Issues on Multiple Criteria</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Rule Key Pattern</p></figcaption></figure>



{% hint style="info" %}
**Note** that only parameters set through the UI are stored in the database. For example, if you override the sonar.exclusions parameter via the command line for a specific project, it will not be stored in the database. Subsequent analyses, or analyses in SonarLint with connected mode, would still be executed with the exclusions defined in the UI and, therefore stored in the DB.
{% endhint %}
