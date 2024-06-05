# Analysis Scope on Codescan Cloud

Analysis scope is something that helps you narrow down results to only the relevant issues. This in turn reduces the noise and the issues from the rules which may not be relevant for certain files.

The key features of Analysis Scope include:

* helps exclude certain files from detecting specific issues.
* helps you completely ignore some files.
* excludes files from duplication detection and coverage calculations.

Follow the steps below to use the **Analysis Scope** feature on [CodeScan cloud](https://www.codescan.io/products/cloud/).

1. Open the Project under the Organization for which you need to run the analysis and navigate to **Project Settings > General Settings > Analysis Scope**.

<figure><img src="../../../.gitbook/assets/image (416).png" alt=""><figcaption></figcaption></figure>

2.  You will now be able to view the tab, under which you can select your required specification to enable this feature during the analysis.

    * **Wildcards:** If you scroll the tab farther to the end, you can see a portion that says “wildcards,” under which there are rules and examples, which help you understand how to enter the specifications or part of the file name to enable this feature. To know more about wildcards, click on [Learn More](https://app.codescan.io/documentation/project-administration/narrowing-the-focus/).

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
