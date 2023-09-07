# Analysis Scope on Codescan Cloud

Analysis scope is something that helps you narrow down results to only the relevant issues. This in turn reduces the noise and the issues from the rules which may not be relevant for certain files.\
The key features of Analysis Scope include:

* helps exclude certain files from detecting specific issues.
* helps you completely ignore some files.
* excludes files from duplication detection and coverage calculations\
  .

Follow the steps below to use the **Analysis Scope** feature on [CodeScan cloud](https://www.codescan.io/products/cloud/).

1. Open the Project under the Organization for which you need to run the analysis and navigate to **Project Settings > General Settings > Analysis Scope**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(285\).png)
2. You will now be able to view the tab, under which you can select your required specification to enable this feature during the analysis.
   * **Wildcards:** If you scroll the tab farther to the end, you can see a portion that says “wildcards,” under which there are rules and examples, which help you understand how to enter the specifications or part of the file name to enable this feature. To know more about wildcards, click on [Learn More](https://app.codescan.io/documentation/project-administration/narrowing-the-focus/).\
     ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-C0HJYQMZ.png)\
     ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-W476DWV1.png)
3. If we go under **files**, you will be able to view two options as follows:\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(287\).png)
   * **Source File Exclusions**: to exclude source code files\
     Specifying an exclusion means that everything under your directory will be included in analysis except the files with paths that match your exclusion pattern.
   * **Source File Inclusions**: Helps include only the specific source code files in the analysis\
     In a few corner cases, it is necessary to be explicit about what's included in analysis and leave out everything else, but that is not the normal case, and setting inclusions should not be the first thing you try when configuring a new project.
4. Once the analysis is completed, go to the **Code** tab to view the files as per your specified settings.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(288\).png)

Here are a couple of implementation examples:

* **For Source File Exclusion**:\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(289\).png)\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(290\).png)
* **For Source File Inclusion**:\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(291\).png)\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(292\).png)

\
