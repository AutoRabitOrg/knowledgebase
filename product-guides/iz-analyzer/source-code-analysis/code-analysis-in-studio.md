# Code Analysis in Studio

{% hint style="warning" %}
Before analyzing the source code in Studio, make sure you have either

* Installed and configured IZ Analyzer - [Anypoint Studio Plugin](../../iz-suite/iz-scan/anypoint-studio/install-iz-analyzer-studio.md).
* Installed and configured IZ Analyzer - [WSO2 Integration Studio Plugin](../releases/server-plugin/wso2/).
{% endhint %}

### On The Fly Results:

**`On The Fly Results`** table/view will display the issues related to the project that user is working on. Project is determined based on the current active file (i.e. the file that user is working on) in Anypoint Studio.

Issues will be detected and reported as and when the connectors are configured in the editor. With this, the issues can be fixed even before they exists.

Follow the below steps to explore **`On The Fly Results`** view.

1.  Go to **`Window`** -> **`Show View`** -> **`other`** -> **`IZ Analyzer`** -> select **`On the Fly Results`** <br>

    <figure><img src="../../../.gitbook/assets/studio_add_on_the_fly_results (1).png" alt=""><figcaption></figcaption></figure>
2.  Open any mule project xml, the issues will be automatically detected and the results can be seen in **`On the Fly Results`** panel. <br>

    * NOTE: **`On The Fly Results`** scans the whole project corresponding to current mule project xml and displays the results

    <figure><img src="../../../.gitbook/assets/studio_on_the_fly_results (1).png" alt=""><figcaption></figcaption></figure>

### On The Fly Results Tab Features

The Results tab provides options such as start or stop analysis, sync rules from the server, reload on the fly results and helps us to quickly sort through the results based on file type, component type and severity.

1.  Go to **`Window`** -> **`Show View`** -> **`other`** -> **`IZ Analyzer`** -> select **`On the Fly Results`**. The options are displayed at the top right corner. <br>

    <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options (1).png" alt=""><figcaption></figcaption></figure>
2.  By default the analysis is active and will immediately report any issues it sees fit. Clicking on the **`Stop Button`** will stop the analysis. You can start it at a later time once a part of your development is completed. <br>

    <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options-start-stop-analysis (1).png" alt=""><figcaption></figcaption></figure>
3.  Your organization might have added new rules or updated the rules in server. By clicking on the **`Sync Rules`** option, you will be importing these updated rules onto Anypoint studio. <br>

    <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options-sync-rules (1).png" alt=""><figcaption></figcaption></figure>
4.  By Clicking on **`Reload on the fly results`** option, your project will be validated against the rules to refresh the tab so as to display any new issues along with the previously displayed issues. <br>

    <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-reload-results (1).png" alt=""><figcaption></figcaption></figure>
5. The Issues seen in the On The Fly Results tab can be grouped based on file type, component type and severity.
   1.  Grouping based on **`File Type`**. <br>

       <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options-group-by-file (1).png" alt=""><figcaption></figcaption></figure>
   2.  Grouping based on **`Component Type`**. <br>

       <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options-group-by-component (1).png" alt=""><figcaption></figcaption></figure>
   3.  Grouping based on **`Severity`**. <br>

       <figure><img src="../../../.gitbook/assets/on-the-fly-results-tab-options-group-by-severity (1).png" alt=""><figcaption></figcaption></figure>

### Issue Fix Recommendation

**`On The Fly Results`** precisely point out the problem in each file with line number, but many users might not be aware of issue fix.\
Issue fix recommendation helps to deal with this scenario with detailed description and examples on how to fix the issue.

1.  Double click on any issue that need a fix to open up the **`Rule Description`** view. <br>

    <figure><img src="../../../.gitbook/assets/studio_rule_description_view (1).png" alt=""><figcaption></figcaption></figure>
2. **`Rule Description`** view provides information about:
   1. Type of Issue. E.g.: **`Code Smell`**, **`Bug`**
   2. Detailed description of the violated rule/issue
   3. Non Compliant Code Example
   4. Compliant Code Example, which guides developers on how to fix the issue
   5. Optionally, an external link to any official documentation for further information about the fix

### Upload to Server

After development is complete, users might want to upload the project to server and save the analysis results or for any other purposes.\
IZ Analyzer provides an easy option to upload project to server from Anypoint Studio.

{% hint style="info" %}
This step assumes that the server details are configured well in advance as mentioned in Installing Studio Plugin SonarQube version 9.x and above requires Java version 11 to scan the projects. It is recommended to use Anypoint Studio version greater than 7.9.0 to use this feature with latest versions of SonarQube.
{% endhint %}

1.  Right click on the project that needs to be uploaded to server, click on **`IZ Analyzer - Server Upload`** <br>

    <figure><img src="../../../.gitbook/assets/studio_upload_to_sonarqube (1).png" alt=""><figcaption></figcaption></figure>
2. Fill in the values required for server upload and click on **`Finish`**:
   1. Project Key - Unique key of the project
   2. Project Name - Display name of the project
   3. Project version - Version of the project
3.  Detailed logs of upload/scanner process will be displayed in **`console`** view\
    &#x20;

    <figure><img src="../../../.gitbook/assets/studio_upload_soanr_qube (1).png" alt=""><figcaption></figcaption></figure>
4.  Results of analysis can be further explored in https://analyzer.integralzone.com/IZ Analyzer] dashboard<br>

    <figure><img src="../../../.gitbook/assets/sonar_server_results (1).png" alt=""><figcaption></figcaption></figure>

### See Also

* Code Analysis In Server
