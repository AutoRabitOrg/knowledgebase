# Installing CodeScan for VS Code

### Learning Objectives: <a href="#learning-objectives" id="learning-objectives"></a>

After completing this unit, you'll be able to:

* [Install the 'CodeScan for Visual Studio (VS) Code' extension](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#installing-the-codescan-for-vs-code-extension)
* [Integrate VS Code with CodeScan](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#integrate-vs-code-with-codescan-extension)
* [Run VS Code behind a proxy](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#visual-studio-code-behind-a-proxy)
* [Compatibility with Agentforce](installing-codescan-for-vs-code.md#compatibility-with-agentforce)
* [Troubleshooting steps if you experienced VS Code issues](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#vs-code-troubleshooting)

### Getting Started with VS Code <a href="#get-started-with-vs-code" id="get-started-with-vs-code"></a>

The **CodeScan VS Code** extension provides immediate feedback to developers on bugs and quality issues; it is a fully integrated user experience in Visual Studio Code (we'll refer to it as VS Code).

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Make sure you:

1. Install the latest VS Code version.
2. Have a CodeScan **cloud** account:
   * Have a valid enterprise license (or a **cloud** trial version—trial **not** available with self-hosted)
3. For CodeScan **Self Hosted**:
   * Have a working **SonarQube™ 9.9+ LTA** server
   * Have a licensed version (no trial available) of the latest **CodeScan** plugin to get started ([more info](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key)).
4. In the **CodeScan UI**, ensure the user has permissions to execute the analysis; otherwise, a 'license not set' error will occur.
5. Download the **CodeScan** extension from the marketplace
6. Download the **Salesforce Extension pack** from the marketplace if you are working with Salesforce code or, at a minimum, the **Visualforce plugins**.
7. Install **JDK version 17** or above.
8. Install **Java Runtime (JRE) 17** version or later.
9. Install the **Node.js 20 LTS** version.
10. Uninstall the **Apex PMD** and **SonarLint™** plugins. The CodeScan and VS Code plugin will not work with SonarLint™ or Apex PMD installed.

{% hint style="warning" %}
Version 2.0.0 requires Java Runtime (JRE) / JDK versions 17 or later. Prior CS versions will still work with older JRE / JDK versions 11.
{% endhint %}

{% hint style="info" %}
**Note:** CodeScan plugin is designed to work with a single VS Code window at a time. Using the CodeScan plugin while having multiple VS Code windows open may give unexpected results.
{% endhint %}

### Installing the 'CodeScan for VS Code' extension <a href="#installing-the-codescan-for-vs-code-extension" id="installing-the-codescan-for-vs-code-extension"></a>

Follow the installation instructions for the CodeScan extension and bind the extension to your CodeScan server.

**Step 1: Install CodeScan for VS Code Extension**

1. Open **Visual Studio Code** and go to the **Activity Bar** on your left. The last button on the Activity Bar is the **Extensions** button.

{% hint style="info" %}
**Note:** You can also press the Shortcut Key combination **`Ctrl + Shift + X`** to launch the Extensions side panel.
{% endhint %}

2. Search for **CodeScan** and click on **Install** to install the latest CodeScan extension.
3. Once installed, restart or reload VS Code to ensure it's taken effect.

**Step 2: Java Runtime (JRE) 17 Installation**

CodeScan should automatically find the JRE installed on your computer. Or you can specify the JRE path on your VS Code's **Settings** page by navigating to **VS Code Settings > Settings > Extensions > CodeScan**.

1. Under **CodeScan > Ls: Java Home** _(Not synced)_, enter the JRE path.

<figure><img src="../../../../.gitbook/assets/image (481).png" alt=""><figcaption></figcaption></figure>

2. Next, confirm the **JAVA\_HOME** variable is set properly on your system. Enter the command echo **%JAVA\_HOME%**. This should output the path to your Java installation folder. Reach out to your IT department if the **JAVA\_HOME** variable is not set.

**Step 3: Create the Connection**

1. Click the CodeScan icon on the left panel.

<figure><img src="../../../../.gitbook/assets/image (477).png" alt="" width="375"><figcaption></figcaption></figure>

2. Click on ‘Add CodeScan Connection.’

<figure><img src="../../../../.gitbook/assets/image (478).png" alt="" width="563"><figcaption></figcaption></figure>

3. Add your CodeScan URL.
4. Click on 'Generate Token.' This will open CodeScan in a browser.
5. Click 'Allow Connection' to send the newly generated token back to your IDE.
6. Add your organization key.
7. You can always find your **organization key** at the top right of your \*\***organization**\*\* home page.<br>
8. Enter a Unique Connection Name.
9. Click on 'Save Connection.' You will see your connection appear in your connected mode window.

<figure><img src="../../../../.gitbook/assets/image (479).png" alt="" width="293"><figcaption></figcaption></figure>

9. Click on your connection (CodeScan Cloud in the example.)

<figure><img src="../../../../.gitbook/assets/image (480).png" alt="" width="563"><figcaption></figcaption></figure>

10. Click the + symbol to the right. This will show you a list of projects from the Command palette.
11. Select the project you would like to connect to.
12. The project you connect to determines the rules for scanning your open files.

{% hint style="info" %}
**Note:** If the project you have open in VS Code matches the project you connect to in CodeScan Cloud, your IDE scans will ignore any Won’t Fix or False Positive issues.
{% endhint %}

### Visual Studio Code Behind a Proxy <a href="#visual-studio-code-behind-a-proxy" id="visual-studio-code-behind-a-proxy"></a>

VS Code extensions can be difficult to use behind a proxy. To point CodeScan at the correct proxy, all it takes is a single environment variable for your system.

Follow these steps to set your environment variables:

#### Windows GUI:

1. Press Windows + R to open the Windows Run prompt.
2. Type in `sysdm.cpl` and click OK.\
   ![](<../../../../.gitbook/assets/1 Run.png>)
3. Open the Advanced tab and click on the Environment Variables button in the System Properties window.\
   ![](<../../../../.gitbook/assets/2 System_properties.png>)
4. The Environment Variables window is divided into two sections. Click the New… button on the top section.\
   ![](<../../../../.gitbook/assets/3 Variables.png>)
5. In the New User Variable prompt, enter the Variable Name as JAVA\_TOOL\_OPTIONS, enter the following Variable Value, and click OK.\
   ![](<../../../../.gitbook/assets/4 New_variable.png>)\
   \
   ![](<../../../../.gitbook/assets/5 Output.png>)

#### Linux or macOS:

**Temporary Setup (for current session):**

In your terminal, type the following line:\
`export JAVA_TOOL_OPTIONS="-Dhttp.proxyHost= [YOUR_PROXY_HOST] -`\
`Dhttp.proxyPort=[YOUR_PROXY_PORT] ..."`\
\
All options for these variables are listed below.

PLEASE NOTE: This setting only lasts until the terminal session is closed.

**Permanent Setup (for all future sessions):**

Open your shell configuration file from your terminal:

For Bash:\
`nano ~/.bashrc`

For Zsh (default for mac since macOS Catalina):\
`nano ~/.zshrc`

1. Add the following line:\
   `export JAVA_TOOL_OPTIONS="-Dhttp.proxyHost= [YOUR_PROXY_HOST] -`\
   `Dhttp.proxyPort=[YOUR_PROXY_PORT] ..."`\
   \
   All options for these variables are listed below.
2. Save the file and apply the changes:\
   `source ~/.bashrc` or `source ~/.zshrc`

The environment variable is: **`JAVA_TOOL_OPTIONS`**

Follow the steps to set environment variables using the Windows GUI:

1. Press **`Windows + R`** to open the Windows Run prompt.
2. Type in **`sysdm.cpl`** and click **OK**.
3. Open the **Advanced** tab and click on the **`Environment Variables`** button in the **System Properties** window.
4. The **Environment Variables** window is divided into two sections. Click the **New…** button on the top section.
5. In the **New User Variable** prompt, enter the Variable Name as **`JAVA_TOOL_OPTIONS,`** enter the following Variable Values, and click **OK**.

#### **Variable Values:**

```
-Dhttp.proxyHost=[YOUR_PROXY_HOST] 
-Dhttp.proxyPort=[YOUR_PROXY_PORT]

-Dhttps.proxyHost=[YOUR_PROXY_HOST] 
-Dhttps.proxyPort=[YOUR_PROXY_PORT]

-Dhttp.nonProxyHosts="localhost|127.0.0.1"
```

If the proxy has a _username_ and _password_, you can add/update the following parameters and add them at the end of the variable value field.

```
-Dhttps.proxyUser=your_username
-Dhttps.proxyPassword=your_password
```

### Self-Signed Certificates <a href="#self-signed-certificates" id="self-signed-certificates"></a>

If you are connecting to a server with self-signed certificates, you will need to specify them for your **Java** and **Node** installations.

For your **Java** installation, you can find the documentation [here](https://docs.oracle.com/en/java/javase/11/security/java-security-overview1.html#GUID-054AD71D-D449-47FF-B6F7-F416DA821D46).

For **Node** installation, add the environment variable _**`NODEEXTRACA_CERTS`**_ with the path to your certificate file as a value, e.g., **`/usr/local/share/ca-certificates/YOUR_CERT.crt.`**

### Compatibility with Agentforce

This plugin is compatible with **Agentforce version 2.2.0 and up**.

To allow CodeScan to run correctly there are 2 steps:

1.  Turn off **Retrieval Augmented Generation** in the settings for Agentforce<br>

    <figure><img src="../../../../.gitbook/assets/image (1636).png" alt=""><figcaption></figcaption></figure>
2. Add the following lines to your settings.json file:

```
  "salesforce.einsteinForDevelopers.advanced": {
    "workspaceStatistics": false
  }
```

After these changes have been made, restart Visual Studio Code.

### VS Code Troubleshooting <a href="#vs-code-troubleshooting" id="vs-code-troubleshooting"></a>

#### PKIX Certificate error <a href="#pkix-certificate-error" id="pkix-certificate-error"></a>

**Error Code:**

```
javax.net.ssl.SSLHandshakeException: 
sun.security.validator.ValidatorException: 
PKIX path building failed: 
sun.security.provider.certpath.SunCertPathBuilderException: 
unable to find valid certification path to requested target.
```

**Reason:** This error occurs when the Java environment does not trust the certificate of the server running your SonarQube instance.

**Solution:** Install the server certificate to the Java key.

**Steps:**

1. In your browser, to the left of the URL, there is a lock icon (![](<../../../../.gitbook/assets/image (437).png>)).
2. Click on this icon and a window will pop up. From the window, select **Connection is secure**.

<figure><img src="../../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

3. Select the second option, i.e., **`Certificate is valid`**.

<figure><img src="../../../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

4. Go to the **Details** tab and click on **Export**.

<figure><img src="../../../../.gitbook/assets/image (435).png" alt="" width="452"><figcaption></figcaption></figure>

5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.

<figure><img src="../../../../.gitbook/assets/image (436).png" alt="" width="540"><figcaption></figcaption></figure>

6. The next process is to install the certificate in the **cacerts** file of the jdk installed in the system using the command line.

**Command:**

> keytool -import **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_ **-file** _{path where we have save the certificate}_

**Example:**

> keytool -import **-alias** _codescan-certificate_ **-keystore** _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ **-file** _c:/tmp/codescan-certificate.crt_

When adding the certificate, password is required. The password is **`changeit`.**

{% hint style="info" %}
**Point to Note:**

If adding the certificate as a trusted certificate to the Java Keystore still results in the **PKIX path building failed** error, we suggest you delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.
{% endhint %}

**Command to list all of the certificates from the Java Keystore:**\
keytool -list -v **-keystore** _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt

**Command to delete the certificate:**\
keytool -delete -noprompt **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt **-alias** _codescan-certificate_ **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_

#### CodeScan Update Binding Failed <a href="#codescan-update-binding-failed" id="codescan-update-binding-failed"></a>

If the CodeScan update binding is getting failed, try disabling the VPN and antivirus, then try updating the binding again.

**If the binding successfully updates,** the error occurred due to antivirus blocking CodeScan. Add CodeScan to the list of allowed sites for the antivirus in use.

**If the binding still fails**, check the HTTP client protocol version. Enter the Apache HTTP client protocol version (FORCE\_HTP\_1, FORCE\_HTTP\_2, or NEGOTIATE). Save and Update Bindings. Further documentation is available [here in the 'Parameters' section](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code?highlight=http%20client#integrate-vs-code-with-codescan-extension).

<figure><img src="../../../../.gitbook/assets/image (499).png" alt=""><figcaption></figcaption></figure>

**If the binding still fails**, raise a [Support Ticket](https://support.autorabit.com/portal/en/home), including the **analyzer logs** and **verbose logs** in the attachment.

#### Issue when ApexPMD plugin installed along with the CodeScan plugin <a href="#issue-when-apexpmd-plugin-installed-along-with-the-codescan-plugin" id="issue-when-apexpmd-plugin-installed-along-with-the-codescan-plugin"></a>

If Apex PMD plugin is installed alongside the CodeScan plugin, one or more of the following issues may occur:

* CodeScan is not listed in the dropdown in **`Output Tab`** of VS Code terminal.
* Inconsistency in the number of issues for a file on saving the file.
* Problems for a specific file are displayed even when the file is closed.

All these issues can be resolved by uninstalling Apex PMD plugin and restarting IDE, then updating the Binding to CodeScan Cloud.

#### CodeScan and Java Runtime Environment (JRE) sync issue <a href="#codescan-and-java-runtime-environment-jre-sync-issue" id="codescan-and-java-runtime-environment-jre-sync-issue"></a>

CodeScan should automatically find the JRE installed on your computer. If you have trouble, then you can specify the JRE path on your VS Code's **Settings** page.

**Navigation:&#x20;**_**VS Code Settings > Settings > Extensions > CodeScan.**_

Under **CodeScan > Ls: Java Home** _(Not synced)_, enter the JRE path.

<figure><img src="../../../../.gitbook/assets/image (500).png" alt="" width="563"><figcaption></figcaption></figure>

#### How do I see warnings and errors in VS Code? <a href="#how-do-i-see-warnings-and-errors-in-vs-code" id="how-do-i-see-warnings-and-errors-in-vs-code"></a>

You can click on the summary or press **`Ctrl+Shift+M`** to display the **`PROBLEMS`** panel with a list of all current errors. If you open a file that has errors or warnings, they will be rendered inline with the text and in the overview ruler.

{% hint style="info" %}
**Note:** The VS Code displays the code issues related to bugs, vulnerabilities, and code smells inside the **`PROBLEMS`** tab. No code duplications are shown in the IDE.
{% endhint %}

#### Other useful debugging information <a href="#other-useful-debugging-information" id="other-useful-debugging-information"></a>

* Some useful debugging information is available under the **`Output`** window under the ‘**`CodeScan`**’ tab.
* Also, you can check for any serious errors by going to **`Help > Toggle Developer Tools`** to bring up the console.

***

### Changelogs

#### 27 June 2024

**v. 2.0.3**

Changes were required to support fixes and enhancements of the **VS Code CodeScan Plugin (v2.0.3)** to VS Code Extension Marketplace; specifically, we fixed a plugin issue that caused non-recognition of CodeScan-specific JS and VF rules.

**13 June 2024**

**v. 2.0.2**

New CodeScan Issue Filter: Quickly sort and filter issues by type and severity for efficient code review. You can click on the specific _Type_ or _Severity_ to only see issues of that type.

<figure><img src="../../../../.gitbook/assets/image (567).png" alt=""><figcaption></figcaption></figure>

The released plugin can be updated directly from VSCode and also can be found in this link: [https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode](https://marketplace.visualstudio.com/items?itemName=codescansf.codescan-vscode)

***

### Raising a support ticket <a href="#raising-a-support-ticket" id="raising-a-support-ticket"></a>

Before raising a support ticket, perform the following checks in VS Code:

* **Is the Sonarlint or ApexPMD plugin installed alongside CodeScan?** _If so, uninstall it._
* **Is the Salesforce extension pack installed in VS Code?** _If not, install, as this is mandatory._
* **What version of Java is installed?** Version 2.0.0 onward requires Java Runtime (JRE) / JDK versions 17 or later. Prior CS versions will still work with older JRE / JDK versions 11.
* **Is the Java path passed to CodeScan (codescan.ls.javaHome)?** Verify by going to **`VS Code Settings > Settings > Extensions > CodeScan`** and under **`Codescan › Ls: Java Home (Not synced),`** you should see the **`JAVA_HOME`** path mentioned. If not present, please enter the **`JAVA_HOME`** path.
* You can also add the **`JAVA_HOME`** path in the **settings.json** file inside the **`codescan.ls.javaHome`** property.

<figure><img src="../../../../.gitbook/assets/image (501).png" alt="" width="563"><figcaption></figcaption></figure>

* Perform the **CodeScan Update Binding** and check if the issue is resolved.

{% hint style="info" %}
NOTE: Duplicate lines of code and Security Hotspot issues do not show up in IDE.
{% endhint %}

***

**What's Next?**\
If you're still having an issue with VS Code, raise a support ticket on the [CodeScan Support Page](https://support.autorabit.com/portal/en/home) and share with us the following information:

*   In **settings.json** file, please add the below properties inside the curly braces ({ }) to get debug level logs:

    ```
    "codescan.output.showVerboseLogs": true, 
    "codescan.output.showAnalyzerLogs": true,
    ```
* Update the CodeScan binding and share the logs with us.
