# Analysis Scope on CodeScan Cloud

An analysis scope helps you narrow your results to only the relevant issues. This reduces the noise and issues from rules that may not be relevant to certain files.

The key features of an Analysis Scope are:

* Helps you exclude certain files from detecting specific issues.
* Helps you completely ignore some files.
* Helps you exclude files from duplication detection and coverage calculations.

Follow the steps below to use the **Analysis Scope** feature on [CodeScan cloud](https://www.codescan.io/products/cloud/).

{% hint style="info" %}
Codescan can scan 3rd party libraries only when the code is present in the file, and not when it's referenced.
{% endhint %}

1. Open the Project under the Organization for which you need to run the analysis and navigate to **Project Settings > General Settings > Analysis Scope**.

<figure><img src="../../../.gitbook/assets/image (416).png" alt=""><figcaption></figcaption></figure>

2.  You will now be able to view the tab, under which you can select your required specification to enable this feature during the analysis.

    * **Wildcards:** If you scroll the tab farther to the end, you can see a portion that says “wildcards,” under which there are rules and examples, which help you understand how to enter the specifications or part of the file name to enable this feature.&#x20;

    <figure><img src="../../../.gitbook/assets/image (417).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>
3.  If we go under **files**, you will be able to view two options as follows:



    <figure><img src="../../../.gitbook/assets/image (421).png" alt=""><figcaption></figcaption></figure>

    * **Source File Exclusions**: to exclude source code files. Specifying an exclusion means that everything under your directory will be included in analysis except the files with paths that match your exclusion pattern.
    * **Source File Inclusions**: Helps include only the specific source code files in the analysis. In a few corner cases, it is necessary to be explicit about what's included in analysis and leave out everything else, but that is not the normal case, and setting inclusions should not be the first thing you try when configuring a new project.
4. Once the analysis is completed, go to the **Code** tab to view the files as per your specified settings.

<figure><img src="../../../.gitbook/assets/image (422).png" alt=""><figcaption></figcaption></figure>

Here are a couple of implementation examples:

* **For Source File Exclusions**:

<figure><img src="../../../.gitbook/assets/image (423).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (424).png" alt=""><figcaption></figcaption></figure>

* **For Source File Inclusions**:

<figure><img src="../../../.gitbook/assets/image (425).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (426).png" alt=""><figcaption></figcaption></figure>

You can accomplish this by utilizing the "**Ignore Issues on Multiple Criteria**" feature in Project Settings under General Settings > Analysis Scope.

To do this, simply provide the rule key and file path name.

**Example:**

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
**Note** that only parameters set through the UI are stored in the database. For example, if you override the sonar.exclusions parameter via the command line for a specific project, it will not be stored in the database. Subsequent analyses, or analyses in SonarLint with connected mode, would still be executed with the exclusions defined in the UI and, therefore stored in the DB.
{% endhint %}
