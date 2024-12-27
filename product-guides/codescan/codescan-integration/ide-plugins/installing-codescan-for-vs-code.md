# Installing CodeScan for VS Code

### Learning Objectives: <a href="#learning-objectives" id="learning-objectives"></a>

After completing this unit, you'll be able to:

* [Install the 'CodeScan for Visual Studio (VS) Code' extension](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#installing-the-codescan-for-vs-code-extension)
* [Integrate VS Code with CodeScan](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#integrate-vs-code-with-codescan-extension)
* [Run VS Code behind a proxy](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#visual-studio-code-behind-a-proxy)
* [Troubleshooting steps if you experienced VS Code issues](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#vs-code-troubleshooting)

### Installing the CodeScan IDE Plugin version 2.0.0

These step-by-step instructions will show you how to install the CodeScan plugin.&#x20;

1. Click the CodeScan icon on the left panel.&#x20;

<figure><img src="../../../../.gitbook/assets/image (477).png" alt="" width="375"><figcaption></figcaption></figure>

2. Click on ‘Add CodeScan Connection.’

<figure><img src="../../../../.gitbook/assets/image (478).png" alt="" width="563"><figcaption></figcaption></figure>

3. Add your CodeScan URL.
4. Click on 'Generate Token.' This will open CodeScan in a browser.
5. Click 'Allow Connection' to send the newly generated token back to your IDE.
6. Add your organization key.
7. Enter a Unique Connection Name.
8. Click on 'Save Connection.' You will see your connection appear in your connected mode window.

<figure><img src="../../../../.gitbook/assets/image (479).png" alt="" width="293"><figcaption></figcaption></figure>

9. Click on your connection (CodeScan Cloud in the example.)

<figure><img src="../../../../.gitbook/assets/image (480).png" alt="" width="563"><figcaption></figcaption></figure>

10. Click the + symbol to the right. This will show you a list of projects from the Command palette.
11. Select the project you would like to connect to.
12. The project you connect to determines the rules for scanning your open files.

{% hint style="info" %}
**Note:** If the project you have open in VS Code matches the project you connect to in CodeScan Cloud, your IDE scans will ignore any Won’t Fix or False Positive issues.
{% endhint %}

### Get Started with VS Code <a href="#get-started-with-vs-code" id="get-started-with-vs-code"></a>

The **CodeScan VS Code** extension provides immediate feedback to developers on bugs and quality issues; it is a fully integrated user experience in Visual Studio Code (we'll refer to it as VS Code).

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Make sure you:

1. Install the latest VS Code version.
2. Have a CodeScan **cloud** account:&#x20;
   * Have a valid enterprise license (or a **cloud** trial version—trial **not** available with self-hosted)
3. For CodeScan **Self Hosted**:
   * Have a working **SonarQube™ 9.9+ LTA** server
   * Have a licensed version (no trial available) of the latest **CodeScan** plugin to get started ([more info](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key)).
4. Download the **CodeScan** extension from the marketplace
5. Download the **Salesforce Extension pack** from the marketplace if you are working with Salesforce code or, at a minimum, the **Visualforce plugins**.
6. Install **JDK version 17** or above.
7. Install **Java Runtime (JRE) 17** version or later.
8. Install the latest available **Node.js LTS** version.
9. Uninstall the **Apex PMD** and **SonarLint™** plugins. The CodeScan and VS Code plugin will not work with SonarLint™ or Apex PMD installed.

{% hint style="warning" %}
Version 2.0.0 requires Java Runtime (JRE) / JDK versions 17 or later. Prior CS versions will still work with older JRE / JDK versions 11.
{% endhint %}

{% hint style="info" %}
**Note:** CodeScan plugin is designed to work with a single VS Code window at a time. Using the CodeScan plugin while having multiple VS Code windows open may give unexpected results.
{% endhint %}

### Installing the 'CodeScan for VS Code' extension <a href="#installing-the-codescan-for-vs-code-extension" id="installing-the-codescan-for-vs-code-extension"></a>

Follow the installation instructions for the CodeScan extension and bind the extension to your CodeScan server.

**Step 1: Install CodeScan for VS Code Extension**

1. Open **Visual Studio Code** and go to the **Activity Bar** on your left. The last button on the Activity Bar is the **Extensions** button.&#x20;

{% hint style="info" %}
**Note:** You can also press the Shortcut Key combination **`Ctrl + Shift + X`** to launch the Extensions side panel.
{% endhint %}

2. Search for **CodeScan** and click on **Install** to install the CodeScan latest extension, preferably **version 1.6.8** or above.
3. Once installed, restart or reload VS Code to ensure it's taken effect.

**Step 2: Java Runtime (JRE) 11 Installation**

CodeScan should automatically find the JRE installed on your computer. Or you can specify the JRE path on your VS Code's **Settings** page by navigating to **VS Code Settings > Settings > Extensions > CodeScan**.

1. Under **CodeScan > Ls: Java Home** _(Not synced)_, enter the JRE path.

<figure><img src="../../../../.gitbook/assets/image (481).png" alt=""><figcaption></figcaption></figure>

2. Next, confirm the **JAVA\_HOME** variable is set properly on your system. Enter the command echo **%JAVA\_HOME%**. This should output the path to your Java installation folder. Reach out to your IT department if the **JAVA\_HOME** variable is not set.

**Step 3: Generate CodeScan token**

You can generate new tokens at **User > My Account > Security** or use an existing token if you have one saved. Copy the generated token and add it to the **settings.json** file (discussed later).

**Step 4: Obtain the Project Key**

Log in to CodeScan, click on the **Projects** tab, and find the project you need to configure. Click on the **Project Information** tab to find your project key at the bottom right of your screen.

**Step 5: Obtain the Organization Key**

You can always find your **organization key** at the top right of your \*\*organization \*\*home page.

<figure><img src="../../../../.gitbook/assets/image (482).png" alt=""><figcaption></figcaption></figure>

**Step 6: Add CodeScan Configuration**

1. Press **Ctrl + Shift + P** in the VS Code, and search for **Settings** and select **Open User Settings (JSON)**.

<figure><img src="../../../../.gitbook/assets/image (483).png" alt=""><figcaption></figcaption></figure>

2. On the **settings.json** tab, inside the curly braces ({ }), copy and paste the following text, and add the parameters shown in the table below:

<figure><img src="../../../../.gitbook/assets/image (484).png" alt="" width="563"><figcaption></figcaption></figure>

_**Example:**_

<figure><img src="../../../../.gitbook/assets/image (485).png" alt=""><figcaption></figcaption></figure>

| PARAMETER                                                                                           | DESCRIPTION                                                                                                                                                |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| serverID                                                                                            | Add _serverId_ with a value you will remember. You will need to enter the same value in both of the _serverId_ parameters.                                 |
| [organizationKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys) | Add your CodeScan organization key. If you are using CodeScan Self-Hosted, enter your default-organization.                                                |
| serverUrl                                                                                           | <p>For CodeScan Cloud, enter:<br>https://app.codescan.io/for U.S. region, https://app-eu.codescan.io/ for EU, and https://app-aus.codescan.io/for AUS.</p> |

For Self-Hosted CodeScan, add _serverUrl_ as your SonarQube™ _server URL_ (default is _**http://localhost:9000**_). |\
\| [token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token) | Add your security token. For **Self-Hosted CodeScan**, add token generated in SonarQube™. |\
\| [cell](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key) | Add your CodeScan project key.|\
\| codescan.httpclient.version | (applicable for VS Code v1.6.10 or later)\
\| Enter the Apache HTTP client protocol version (**FORCE\_HTTP\_1**, **FORCE\_HTTP\_2**, or **NEGOTIATE**). |

{% hint style="info" %}
**Note:** If no protocol version is set, the default protocol is **NEGOTIATE**.
{% endhint %}

3. Save the **settings.json** file.

**Step 7: Configure the Project Binding**

Next, you will need to update the CodeScan bindings for the workspace to ensure the rules are in sync.

Select **-**\
**Shift+Command+P** or **-**\
**Shift+Command+P** (Mac) to open the Command Palette. Type in CodeScan to bring up the CodeScan commands and run **Update CodeScan binding to SonarQube/CodeScan Cloud**.

An **All CodeScan bindings successfully updated** notification appears once the binding is completed successfully.

**Step 8: Verifying**

You can verify this by opening a file that has problems. They will now be highlighted within your code:

* An underline shows a pop-up of the issue when hovering

<figure><img src="../../../../.gitbook/assets/image (486).png" alt=""><figcaption></figcaption></figure>

* Within the VS Code problems panel

<figure><img src="../../../../.gitbook/assets/image (487).png" alt=""><figcaption></figcaption></figure>

### Integrate VS Code with CodeScan extension <a href="#integrate-vs-code-with-codescan-extension" id="integrate-vs-code-with-codescan-extension"></a>

Once you're done installing the CodeScan extension from the marketplace,

1. Restart the Visual Studio Code.
2. Press **`Ctrl + Shift + P`** and search for **`Settings`** and select **`Open User Settings (JSON).`**

<figure><img src="../../../../.gitbook/assets/image (488).png" alt=""><figcaption></figcaption></figure>

3. On the **settings.json** tab, inside the curly braces ({ }), copy and paste the following text:

```none
"codescan.servers": [
       {
            "serverId": "**************",
            "organizationKey": "**************",
            "serverUrl": "**************",
            "token": "**************"
        },
    ],

    "codescan.project": {
        "serverId": "**************",
        "projectKey": "**************"
    }
    "codescan.httpclient.version": "***********",
```

Plain text Copy

<figure><img src="../../../../.gitbook/assets/image (489).png" alt="" width="464"><figcaption></figcaption></figure>

| Parameters                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| serverId                                                                                                  | Add _serverId_ with a value you will remember. You will need to enter the same value in both of the _serverId_ parameters.                                                                                                                                                                                                                                                                             |
| [organizationKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)       | Add your CodeScan organization key. If you are using CodeScan Self Hosted, please enter your _default-organization_.                                                                                                                                                                                                                                                                                   |
| serverUrl                                                                                                 | <p>For <em>CodeScan cloud</em>, please enter:<br><code>https://app.codescan.io/</code>for US region,<br><code>https://app-eu.codescan.io/</code> for EU, and<br><code>https://app-aus.codescan.io/</code>for AUS.<br><br>For <strong>Self-Hosted CodeScan</strong>, add <em>serverUrl</em> as your <em>SonarQube™ server URL</em> (default is <strong><code>http://localhost:9000</code></strong>)</p> |
| [token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)                      | Add your security token. For _Self-Hosted CodeScan_, add token generated in SonarQube™.                                                                                                                                                                                                                                                                                                                |
| [projectKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)                  | Add your CodeScan project key.                                                                                                                                                                                                                                                                                                                                                                         |
| <p>codescan.httpclient.version<br><em>(applicable for VS Code <strong>v1.6.10</strong> or later)</em></p> | <p>Enter the Apache HTTP client protocol version (<strong><code>FORCE_HTTP_1</code></strong>, <strong><code>FORCE_HTTP_2</code></strong> or <strong><code>NEGOTIATE</code></strong>).<br><strong>Note:</strong> If no protocol version is set, the default protocol <strong><code>NEGOTIATE</code></strong> is used.</p>                                                                               |

4. Save the **settings.json** file.
5. Now select **`Ctrl+Shift+P (Windows/Linux)`** or **`Shift+Command+P(Mac)`** to open the **Command Palette**.
6. Type in **`CodeScan`** to bring up the CodeScan commands and run **`Update CodeScan binding to SonarQube/CodeScan Cloud`**.
7. Go to **View > Output** to view the logs details. If a problem does occur, you are able to trace it via logs.

<figure><img src="../../../../.gitbook/assets/image (491).png" alt=""><figcaption></figcaption></figure>

8. Select **`Terminal > New Terminal`** or press **Ctrl+Shift +\`**, if you are not able to view the **Output** section at the bottom of the screen.
9. An **`All CodeScan bindings successfully updated`** notification appears if the binding is successfully completed.
10. If any changes are made on the SonarQube™ server, then repeat this step.

<figure><img src="../../../../.gitbook/assets/image (492).png" alt=""><figcaption></figcaption></figure>

11. Open a file, and you should see the issues in your code underlined.

<figure><img src="../../../../.gitbook/assets/image (493).png" alt=""><figcaption></figcaption></figure>

### Visual Studio Code behind a proxy <a href="#visual-studio-code-behind-a-proxy" id="visual-studio-code-behind-a-proxy"></a>

VS Code extensions can be difficult to use behind a proxy. To point CodeScan at the correct proxy, all it takes is a single environment variable for your system.

The environment variable is: **`JAVA_TOOL_OPTIONS`**

Follow the steps to set environment variables using the Windows GUI:

1. Press **`Windows + R`** to open the Windows Run prompt.
2. Type in **`sysdm.cpl`** and click **`OK`**.
3. Open the **`Advanced`** tab and click on the **`Environment Variables`** button in the **System Properties** window.
4. The **Environment Variables** window is divided into two sections. Click the **`New…`** button on the top section.
5. In the **New User Variable** prompt, enter the **`Variable Name`** as **`JAVA_TOOL_OPTIONS,`** enter the following **`Variable Value`**, and click **`OK`**.

**Variable Value:**

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

1. In your browser, to the left of the URL, there is a lock icon (![](<../../../../.gitbook/assets/image (494).png>)).
2. Click on this icon and a window will pop up. From the window, select **Connection is secure**.

<figure><img src="../../../../.gitbook/assets/image (495).png" alt=""><figcaption></figcaption></figure>

3. Select the second option, i.e., **`Certificate is valid`**.

<figure><img src="../../../../.gitbook/assets/image (496).png" alt=""><figcaption></figcaption></figure>

4. Go to the **Details** tab and click on **Export**.

<figure><img src="../../../../.gitbook/assets/image (497).png" alt="" width="452"><figcaption></figcaption></figure>

5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.

<figure><img src="../../../../.gitbook/assets/image (498).png" alt="" width="540"><figcaption></figcaption></figure>

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

### CodeScan Update Binding Failed <a href="#codescan-update-binding-failed" id="codescan-update-binding-failed"></a>

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

### CodeScan and Java Runtime Environment (JRE) sync issue <a href="#codescan-and-java-runtime-environment-jre-sync-issue" id="codescan-and-java-runtime-environment-jre-sync-issue"></a>

CodeScan should automatically find the JRE installed on your computer. If you have trouble, then you can specify the JRE path on your VS Code's **Settings** page.

**Navigation:&#x20;**_**VS Code Settings > Settings > Extensions > CodeScan.**_

Under **CodeScan > Ls: Java Home** _(Not synced)_, enter the JRE path.

<figure><img src="../../../../.gitbook/assets/image (500).png" alt="" width="563"><figcaption></figcaption></figure>

### How do I see warnings and errors in VS Code? <a href="#how-do-i-see-warnings-and-errors-in-vs-code" id="how-do-i-see-warnings-and-errors-in-vs-code"></a>

You can click on the summary or press **`Ctrl+Shift+M`** to display the **`PROBLEMS`** panel with a list of all current errors. If you open a file that has errors or warnings, they will be rendered inline with the text and in the overview ruler.

{% hint style="info" %}
**Note:** The VS Code displays the code issues related to bugs, vulnerabilities and code smells inside the **`PROBLEMS`** tab. No code-duplications are shown in the IDE.
{% endhint %}

#### Other useful debugging information <a href="#other-useful-debugging-information" id="other-useful-debugging-information"></a>

* Some useful debugging information is available under the **`Output`** window under the ‘**`CodeScan`**’ tab.
* Also, you can check for any serious errors by going to **`Help > Toggle Developer Tools`** to bring up the console.



***

### Changelogs

#### 27 June 2024

**v. 2.0.3**

Changes were required to support fixes and enhancements of the **VS Code CodeScan Plugin (v2.0.3)** to VS Code Extension Marketplace; specifically, we fixed a plugin issue that caused non-recognition of CodeScan-specific JS and VF rules.&#x20;



**13 June 2024**

**v. 2.0.2** &#x20;

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
