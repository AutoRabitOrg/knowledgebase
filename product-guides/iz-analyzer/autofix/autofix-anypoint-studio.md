# Autofix - Anypoint Studio

Autofix is a feature where static code analysis issues can be fixed automatically with the click of a button.

{% hint style="warning" %}
Make sure you have:

* Installed the latest version of Anypoint Studio / WSO2 Integration Studio Plugin
* Configured the Business Group/Organization associated with the issued license.
* Valid license with Auto Fix module enabled
{% endhint %}

### Enable Autofix

1. Go to **`Window`** -> **`Preferences`** -> **`IZ Preferences`**, and **`Sync Metadata`** if not done already
2. Click on **`Enable Auto Fix`**

### Auto Fix Issues

1. Go to **`Window`** -> **`Show View`** -> **`other`** -> **`IZ Analyzer`** -> select **`On the Fly Results`**
2. **`Preview`** and **`Fix`** options will be available in **`On the Fly Results`** table against applicable rules
3. Use the **`Preview`** option to view the list of changes that the **`Fix`** would perform. No files will be updated in preview mode&#x20;
4.  Use the **`Fix`** option to apply the fix to applicable files\
    &#x20;

    <figure><img src="../../../.gitbook/assets/auto_fix_apply (1).gif" alt=""><figcaption></figcaption></figure>

### Auto Fix - Logs

1. Go to **`Window`** -> **`Show View`** -> **`other`** -> **`IZ Analyzer`** -> select **`Auto Fix Logs`**
2. An audit log of the applied fix will be generated in the **`target/izanalyzer/autofix-log.csv`** directory
3.  HTML report of the same will be displayed in **`Auto Fix Logs`** view\
    &#x20;

    <figure><img src="../../../.gitbook/assets/auto-fix-logs (1).png" alt=""><figcaption></figcaption></figure>

#### Details

* Manage Anypoint Studio Plugin
* Manage Server Plugin

***

[SonarQube™](https://www.sonarqube.org) is a trademark belonging to SonarSource SA. For further information, please visit [www.sonarqube.org](https://www.sonarqube.org).
