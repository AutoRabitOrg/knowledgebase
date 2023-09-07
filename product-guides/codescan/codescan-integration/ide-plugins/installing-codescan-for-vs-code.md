# Installing CodeScan for VS Code

### Learning Objectives: <a href="#learning-objectives" id="learning-objectives"></a>

After completing this unit, you'll be able to:

* [Install the 'CodeScan for Visual Studio (VS) Code' extension](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#installing-the-codescan-for-vs-code-extension)
* [Integrate VS Code with CodeScan](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#integrate-vs-code-with-codescan-extension)
* [Run VS Code behind a proxy](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#visual-studio-code-behind-a-proxy)
* [Troubleshooting steps if you ran with VS Code issues](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#vs-code-troubleshooting)

***

### Get Started with VS Code <a href="#get-started-with-vs-code" id="get-started-with-vs-code"></a>

The **CodeScan VS Code** extension provides immediate feedback to developers on bugs and quality issues; it is a fully integrated user experience in Visual Studio Code (we'll refer to it as VS Code).\


#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Make sure you:

* Install the latest VS Code version.
* Have a CodeScan cloud account (with valid enterprise or trial license).
* For CodeScan **Self Hosted**:
  * Have a working **SonarQube™ (9.9+)** server
  * Have a licensed, latest version of **CodeScan** plugin to get started ([more info](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key)).
* Download the **CodeScan** extension from the marketplace
* Download the **Salesforce Extension pack** from the marketplace if you are working with Salesforce code or, at a minimum, the **Visualforce plugins**.
* Install the **JDK version 11** or above.
* Install the **Java Runtime (JRE) 11** version or later.
* Install the latest available **Node.js LTS** version.
* Uninstall the **Apex PMD** and **SonarLint™** plugins. The CodeScan and VS Code plugin will not work with SonarLint™ or Apex PMD installed.

Note:

CodeScan plugin is designed to work with a single VS Code window at a time. Using CodeScan plugin with multiple VS Code windows open may give unexpected results.

***

### Installing the 'CodeScan for VS Code' extension <a href="#installing-the-codescan-for-vs-code-extension" id="installing-the-codescan-for-vs-code-extension"></a>

Follow the installation instructions for the CodeScan extension and bind the extension to your CodeScan server.

**Step 1: Install CodeScan for VS Code Extension**

1. Open **Visual Studio Code** and go to the **Activity Bar** on your left. The last button on the Activity Bar is the **Extensions** button.

You can also press the Shortcut Key combination **`Ctrl + Shift + X`** to launch the Extensions side panel.

2. Search for **CodeScan** and click on **Install** to install the CodeScan latest extension, preferably **version 1.6.8** or above.
3. Once installed, restart or reload VS Code to ensure it's taken effect.

**Step 2: Java Runtime (JRE) 11 Installation**

CodeScan should automatically find the JRE installed on your computer. Or you can specify the JRE path on your VS Code's **Settings** page by navigating to **VS Code Settings > Settings > Extensions > CodeScan**.

1. Under **CodeScan > Ls: Java Home** _(Not synced)_, enter the JRE path.\
   ![CS Installing CS for VS Code 1.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%201.png)
2. Next, confirm the **JAVA\_HOME** variable is set properly on your system. Enter the command echo **%JAVA\_HOME%**. This should output the path to your Java installation folder. Reach out to your IT department if the **JAVA\_HOME** variable is not set.

**Step 3: Generate CodeScan token**

You can generate new tokens at **User > My Account > Security** or use an existing token if you have one saved. Copy the generated token and add it to the **settings.json** file (discussed later).

**Step 4: Obtain the Project Key**

Log in to CodeScan, click on the **Projects** tab, and find the project you need to configure. Click on the **Project Information** tab to find your project key at the bottom right of your screen.

**Step 5: Obtain the Organization Key**\
You can always find your **organization key** at the top right of your \*\*organization \*\*home page.\
![CS Installing CS for VS Code 2.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%202\(1\).png)

**Step 6: Add CodeScan Configuration**

1. Press **Ctrl + Shift + P** in the VS Code, and search for **Settings** and select **Open User Settings (JSON)**.\
   ![CS Installing CS for VS Code 3.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%203.png)
2. On the **settings.json** tab, inside the curly braces ({ }), copy and paste the following text, and add the parameters shown in the table below:\
   ![CS Installing CS for VS Code 4.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%204.png)

_**Example:**_\
![CS Installing CS for VS Code 5.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%205.png)

| PARAMETER                                                                                           | DESCRIPTION                                                                                                                |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| serverID                                                                                            | Add _serverId_ with a value you will remember. You will need to enter the same value in both of the _serverId_ parameters. |
| [organizationKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys) | Add your CodeScan organization key. If you are using CodeScan Self-Hosted, enter your default-organization.                |
| serverUrl                                                                                           | For CodeScan Cloud, enter:                                                                                                 |
| https://app.codescan.io/for U.S. region,                                                            |                                                                                                                            |
| https://app-eu.codescan.io/ for EU, and                                                             |                                                                                                                            |
| https://app-aus.codescan.io/for AUS.                                                                |                                                                                                                            |

For Self-Hosted CodeScan, add _serverUrl_ as your SonarQube™ _server URL_ (default is _**http://localhost:9000**_). |\
\| [token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token) | Add your security token. For **Self-Hosted CodeScan**, add token generated in SonarQube™. |\
\| [cell](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key) | Add your CodeScan project key.|\
\| codescan.httpclient.version\
(applicable for VS Code v1.6.10 or later)\
\| Enter the Apache HTTP client protocol version (**FORCE\_HTTP\_1**, **FORCE\_HTTP\_2**, or **NEGOTIATE**).\
Note: If no protocol version is set, the default protocol is **NEGOTIATE**. |

3. Save the **settings.json** file.

**Step 7: Configure the Project Binding**

Next, you will need to update the CodeScan bindings for the workspace to ensure the rules are in sync.

Select **-**\
**Shift+Command+P** or **-**\
**Shift+Command+P** (Mac) to open the Command Palette. Type in CodeScan to bring up the CodeScan commands and run **Update CodeScan binding to SonarQube/CodeScan Cloud**.

An **All CodeScan bindings successfully updated** notification appears once the binding is successfully completed.

**Step 8: Verifying**

You can verify this by opening a file that has problems. They will now be highlighted within your code:

* An underline shows a pop-up of the issue when hovering\
  ![CS Installing CS for VS Code 6.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%206.png)
* Within the VS Code problems panel\
  ![CS Installing CS for VS Code 7.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Installing%20CS%20for%20VS%20Code%207.png)

***

### Integrate VS Code with CodeScan extension <a href="#integrate-vs-code-with-codescan-extension" id="integrate-vs-code-with-codescan-extension"></a>

Once you're done installing the CodeScan extension from the marketplace,

1. Restart the Visual Studio Code.
2. Press **`Ctrl + Shift + P`** and search for **`Settings`** and select **`Open User Settings (JSON)`**\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-YY3YEG0M.png)
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

Plain textCopy

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-6ZJCVEMX.png)

| Parameters                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| serverId                                                                                                  | Add _serverId_ with a value you will remember. You will need to enter the same value in both of the _serverId_ parameters.                                                                                                                                                                                                                                                                             |
| [organizationKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)       | Add your CodeScan organization key. If you are using CodeScan Self Hosted, please enter your _default-organization_.                                                                                                                                                                                                                                                                                   |
| serverUrl                                                                                                 | <p>For <em>CodeScan cloud</em>, please enter:<br><code>https://app.codescan.io/</code>for US region,<br><code>https://app-eu.codescan.io/</code> for EU, and<br><code>https://app-aus.codescan.io/</code>for AUS.<br><br>For <strong>Self-Hosted CodeScan</strong>, add <em>serverUrl</em> as your <em>SonarQube™ server URL</em> (default is <strong><code>http://localhost:9000</code></strong>)</p> |
| [token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)                      | Add your security token. For _Self-Hosted CodeScan_, add token generated in SonarQube™.                                                                                                                                                                                                                                                                                                                |
| [projectKey](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)                  | Add your CodeScan project key.                                                                                                                                                                                                                                                                                                                                                                         |
| <p>codescan.httpclient.version<br><em>(applicable for VS Code <strong>v1.6.10</strong> or later)</em></p> | <p>Enter the Apache HTTP client protocol version (<strong><code>FORCE_HTTP_1</code></strong>, <strong><code>FORCE_HTTP_2</code></strong> or <strong><code>NEGOTIATE</code></strong>).<br><strong>Note:</strong> If no protocol version is set, the default protocol <strong><code>NEGOTIATE</code></strong> is used.</p>                                                                               |

6. Save the **settings.json** file.
7. Now select **`Ctrl+Shift+P (Windows/Linux)`** or **`Shift+Command+P(Mac)`** to open the **Command Palette**.
8. Type in **`CodeScan`** to bring up the CodeScan commands and run **`Update CodeScan binding to SonarQube/CodeScan Cloud`**.
9.  Go to **View > Output** to view the logs details. If a problem does occur, you are able to trace it via logs.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-MIL7HT7Q.png)

    Select **`Terminal > New Terminal`** or press **Ctrl+Shift +\`**, if you are not able to view the **Output** section at the bottom of the screen.
10. An **`All CodeScan bindings successfully updated`** notification appears if the binding is successfully completed.
11. If any changes are made on the SonarQube™ server, then repeat this step.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-T1SYRHUO.png)
12. Open a file, and you should see the issues in your code underlined.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-NA9LYN17.png)

\


***

### Visual Studio Code behind a proxy <a href="#visual-studio-code-behind-a-proxy" id="visual-studio-code-behind-a-proxy"></a>

VS Code extensions can be difficult to use behind a proxy. To point CodeScan at the correct proxy, all it takes is a single environment variable for your system.

The environment variable is: **`JAVA_TOOL_OPTIONS`**

Follow the steps to set environment variables using the Windows GUI:

1. Press **`Windows + R`** to open the Windows Run prompt.
2. Type in **`sysdm.cpl`** and click **`OK`**.
3. Open the **`Advanced`** tab and click on the **`Environment Variables`** button in the **System Properties** window.
4. The **Environment Variables** window is divided into two sections. Click the **`New…`** button on the top section.
5.  In the **New User Variable** prompt, enter the **`Variable Name`** as **`JAVA_TOOL_OPTIONS,`** enter the following **`Variable Value`**, and click **`OK`**.

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

***

### Self Signed Certificates <a href="#self-signed-certificates" id="self-signed-certificates"></a>

If you are connecting to a server with a self-signed certificates, you will need to specify them for your **Java** and **Node** installations.

For your **Java** installation, you can find the documentation [here](https://docs.oracle.com/en/java/javase/11/security/java-security-overview1.html#GUID-054AD71D-D449-47FF-B6F7-F416DA821D46).

For **Node** installation, add the environment variable _**`NODEEXTRACA_CERTS`**_ with the path to your certificate file as a value, e.g., **`/usr/local/share/ca-certificates/YOUR_CERT.crt.`**

***

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

**Reason:**\
This error occurs when the Java environment does not trust the certificate of the server running your SonarQube instance.

**Solution:**\
Install the server certificate to the Java key.

**Steps:**

1. In your browser, to the left of the URL, there is a lock icon (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ICO24JDZ.png)).
2. Click on this icon and a window will pop up. From the window, select **Connection is secure**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-5THK9CAG.png)
3. Select the second option, i.e., **`Certificate is valid`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XKDJCMFI.png)
4. Go to the **Details** tab and click on **Export**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CZDQLKG3.png)
5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-IBFUK217.png)
6.  The next process is to install the certificate in the **cacerts** file of the jdk installed in the system using the command line.

    **Command:**

    > keytool -import **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_ **-file** _{path where we have save the certificate}_

    \
    **Example:**

    > keytool -import **-alias** _codescan-certificate_ **-keystore** _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ **-file** _c:/tmp/codescan-certificate.crt_

>

When adding the certificate, password is required. The password is **`changeit`.**

Point to Note:

If adding the certificate as a trusted certificate to the Java Keystore still results in the **PKIX path building failed** error, we suggest you delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.

**Command to list all of the certificates from the Java Keystore:**\
keytool -list -v **-keystore** _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt\
\
\
**Command to delete the certificate:**\
keytool -delete -noprompt **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt **-alias** _codescan-certificate_ **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_

***

#### CodeScan Update Binding Failed <a href="#codescan-update-binding-failed" id="codescan-update-binding-failed"></a>

If the CodeScan update binding is getting failed, try disabling the VPN and antivirus, then try updating the binding again.

**If the binding successfully updates,** the error occurred due to antivirus blocking CodeScan. Add CodeScan to the list of allowed sites for the antivirus in use.

**If the binding still fails**, check the HTTP client protocol version. Enter the Apache HTTP client protocol version (FORCE\_HTP\_1, FORCE\_HTTP\_2, or NEGOTIATE). Save and Update Bindings. Further documentation is available [here in the 'Parameters' section](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code?highlight=http%20client#integrate-vs-code-with-codescan-extension).

<figure><img src="../../../../.gitbook/assets/CS VS Integration Binding Failed.png" alt=""><figcaption></figcaption></figure>

**If the binding still fails**, raise a [Support Ticket](https://support.autorabit.com/portal/en/home), including the **analyzer logs** and **verbose logs** in the attachment.

***

#### Issue when ApexPMD plugin installed along with the CodeScan plugin <a href="#issue-when-apexpmd-plugin-installed-along-with-the-codescan-plugin" id="issue-when-apexpmd-plugin-installed-along-with-the-codescan-plugin"></a>

If Apex PMD plugin is installed alongside the Codescan plugin, one or more of the following issues may occur:

* Codescan is not listed in the dropdown in **`Output Tab`** of VS Code terminal.
* Inconsistency in the number of issues for a file on saving the file.
* Problems for a specific file are displayed even when the file is closed.

All these issues can be resolved by uninstalling Apex PMD plugin and restarting IDE, then updating the Binding to Codescan Cloud.

***

#### CodeScan and Java Runtime Environment (JRE) sync issue <a href="#codescan-and-java-runtime-environment-jre-sync-issue" id="codescan-and-java-runtime-environment-jre-sync-issue"></a>

CodeScan should automatically find the JRE installed on your computer. If you have trouble, then you can specify the JRE path on your VS Code's **Settings** page.

**Navigation: **_**VS Code Settings > Settings > Extensions > CodeScan.**_

Under **Codescan > Ls: Java Home** _(Not synced)_, enter the JRE path.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-PBF1AMDG.png)

***

#### How do I see warnings and errors in VS Code? <a href="#how-do-i-see-warnings-and-errors-in-vs-code" id="how-do-i-see-warnings-and-errors-in-vs-code"></a>

You can click on the summary or press **`Ctrl+Shift+M`** to display the **`PROBLEMS`** panel with a list of all current errors. If you open a file that has errors or warnings, they will be rendered inline with the text and in the overview ruler.

Note:

The VS Code displays the code issues related to bugs, vulnerabilities and code smells inside the **`PROBLEMS`** tab. No code-duplications are shown in the IDE.

#### Other useful debugging information <a href="#other-useful-debugging-information" id="other-useful-debugging-information"></a>

* Some useful debugging information is available under the **`Output`** window under the ‘**`CodeScan`**’ tab.
* Also, you can check for any serious errors by going to **`Help > Toggle Developer Tools`** to bring up the console.

***

### Raising a support ticket <a href="#raising-a-support-ticket" id="raising-a-support-ticket"></a>

Before raising a support ticket, perform the following checks in VS Code:

* **Are Sonarlint or ApexPmd plugin installed alongside CodeScan?-** _If so, uninstall it._
* **Is the Salesforce extension pack installed in VS Code ?-** _If not, install as this is mandatory._
* **What version of Java is installed?**_- Java 11 version is required_
*   **Is the Java path passed to CodeScan (codescan.ls.javaHome)?**- Verify by going to **`VS Code Settings > Settings > Extensions > CodeScan`** and under **`Codescan › Ls: Java Home (Not synced),`** you should see the **`JAVA_HOME`** path mentioned. If not present, please enter the **`JAVA_HOME`** path.

    You can also add the **`JAVA_HOME`** path in the **settings.json** file inside **`codescan.ls.javaHome`** property.\
    ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GOHQE10H.png)

Perform the **CodeScan Update Binding** and check if the issue is resolved.

**What's Next?**\
If you're still having issue with VS Code, raise a support ticket on the [CodeScan Support Page](https://support.autorabit.com/portal/en/home) and share with us the following informations:

*   In **settings.json** file, please add the below properties inside the curly braces ({ }) to get debug level logs:

    ```
    "codescan.output.showVerboseLogs": true, 
    "codescan.output.showAnalyzerLogs": true,
    ```
* Update the CodeScan binding and share the logs with us.
