# Vault Connect

### Introduction

This document provides complete information about the new feature Vault Connect, which will enhance the user’s capability to better utilize Vault in viewing archived Salesforce data from an external data source.

### Feature Overview

1. OData protocol is an open and platform-independent protocol that can be integrated with the system of the user’s choice (along with Salesforce) as it exposes REST APIs for consuming and querying data from the underlying archives.
2. External objects support most of the capabilities that standard and custom objects have in Salesforce.
3. No need to install any managed packages or write custom scripts in Salesforce.

### Step-by-Step Guide

**Create Connect Config**

1. Log in to the **Vault** application.

<figure><img src="../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the setup module of the Vault application. Click on the required Org.

<figure><img src="../../../.gitbook/assets/image (351).png" alt="" width="563"><figcaption></figcaption></figure>

3. Click on the **Connect (Beta)** module of the Vault application.
4. &#x20;On landing on the Connect (Beta) tab of the Vault setup, the user will see the following message on the screen:

<figure><img src="../../../.gitbook/assets/image (352).png" alt="" width="563"><figcaption></figcaption></figure>

5. Once the customer reaches out to AutoRABIT support team as specified on the above screen, our technical team will perform due diligence to enable Vault Connect for the customer(s).
6. When Vault Connect is enabled on the application, the user will see the following screen on the Connect (Beta) tab of the Vault Setup module.

<figure><img src="../../../.gitbook/assets/image (353).png" alt="" width="563"><figcaption></figcaption></figure>

7. Click on the **Add Connect Config** button on the application.

<figure><img src="../../../.gitbook/assets/image (354).png" alt="" width="563"><figcaption></figcaption></figure>

8.  A pop-up will be displayed with the following information:

    * &#x20;How/where to config the external data source;
    * OData URL for configuring the external data source; and
    * What to select when creating Auth. Providers.

    <figure><img src="../../../.gitbook/assets/image (355).png" alt="" width="563"><figcaption></figcaption></figure>
9. Copy the URL from the pop-up shown.&#x20;

{% hint style="info" %}
**Note:** The same URL can be copied from the pop-up and opened by clicking on the information icon available beside the **Add Connect Config** button.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (356).png" alt="" width="563"><figcaption></figcaption></figure>

10. Select the required config from the Archive Config section and click on the **Next** button.

<figure><img src="../../../.gitbook/assets/image (357).png" alt="" width="563"><figcaption></figcaption></figure>

11. On clicking **Next,** you will be redirected to the **Jobs** section.

<figure><img src="../../../.gitbook/assets/image (358).png" alt="" width="563"><figcaption></figcaption></figure>

12. Select the required **Job** and click on Next.
13. On clicking Next, you will be redirected to the **Objects** section.

<figure><img src="../../../.gitbook/assets/image (359).png" alt="" width="563"><figcaption></figcaption></figure>

14. The following operations can be performed:

    * Include/exclude the required objects from the list of objects available.

    <figure><img src="../../../.gitbook/assets/image (360).png" alt="" width="563"><figcaption></figcaption></figure>

    * &#x20;Include/exclude the fields as required from the list of Fields available. Click on the **File** icon from the **Fields** column.

    <figure><img src="../../../.gitbook/assets/image (361).png" alt="" width="563"><figcaption></figcaption></figure>
15. The following pop-up will be displayed, where the user can exclude the fields as required and click on **Apply** field.

<figure><img src="../../../.gitbook/assets/image (362).png" alt="" width="545"><figcaption></figcaption></figure>

16. On clicking Save, you will be prompted to enter the **Name** and **Description** for the config being created.

<figure><img src="../../../.gitbook/assets/image (363).png" alt="" width="563"><figcaption></figcaption></figure>

17. On entering the required details, click on **Save.**
18. On clicking Save, you will be shown a pop-up that says, **“Config has been created/updated successfully,”** and you will be redirected to the **Connect Config Summary**.

<figure><img src="../../../.gitbook/assets/image (364).png" alt="" width="563"><figcaption></figcaption></figure>

19. On the Connect Config Summary, you can view all the configurations created.

#### **View the Archived Data In Salesforce**

1. &#x20;Log in to the Salesforce org for which you want to view the data.
2.  **Create Auth. Providers**

    * Go to → Auth. Providers under setup.
    * Click on the Auth. Providers under setup.

    <figure><img src="../../../.gitbook/assets/image (365).png" alt=""><figcaption></figcaption></figure>
3. Click on **New.**

<figure><img src="../../../.gitbook/assets/image (366).png" alt=""><figcaption></figcaption></figure>

&#x20;4\. Select the **Provider Type – Salesforce.**

<figure><img src="../../../.gitbook/assets/image (367).png" alt=""><figcaption></figcaption></figure>

5. Provide **Name** and **URL Suffix** and click on **Save.**

{% hint style="info" %}
**Note:** Do not change the remaining settings on the layout.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (368).png" alt=""><figcaption></figcaption></figure>

6. On completing the required selections, click on the Save button.&#x20;

#### Create External Data Sources

1. **Go to** → **External Data Sources** under setup.

<figure><img src="../../../.gitbook/assets/image (369).png" alt=""><figcaption></figcaption></figure>

2. Click on **New External Data Sources.**
3. Provide **External Data** source.
   * Provide Name.
   * Type → Salesforce Data: OData 4.0
   * **Identity type** → Named Principal
   * **Authentication Protocol** → OAuth 2.0
   * **Authentication Provider** → On clicking the **LookUp** glass, you can select the **“Auth. Provider”** created earlier.
   * Select the **Authentication Provider.**
   * Click on **Save on the External Data Sources screen.**
   * On **Save**, click the **Validate and Sync.**
   * You will be shown all the objects selected as part of the config creation.
   * On selecting the required objects, the Sync button on Salesforce will be enabled.
   * Select all the objects you want to sync or select which objects’ data you want to view in Salesforce.
   * Click on the **Sync** button.
   * On completion, you can see all the objects selected.
4. **Create Tabs:** Customers can view the archived data under these tabs.
   * **Go to → Tabs** under setup.
   * Click on the **New** button.
5. Under **Objects**, you can see the objects that are part of the Config created with the naming convention **“Object\_\_X”.**



### Sync with Salesforce

#### Installing CodeScan for VS Code

**Learning Objectives:**

After completing this unit, you'll be able to:

* [Install the 'CodeScan for Visual Studio (VS) Code' extension](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#installing-the-codescan-for-vs-code-extension)&#x20;
* [Integrate VS Code with CodeScan](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#integrate-vs-code-with-codescan-extension)
* [Run VS Code behind a proxy](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#visual-studio-code-behind-a-proxy)
* [Troubleshooting steps if you ran with VS Code issues](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code#vs-code-troubleshooting)

## Installing the CodeScan IDE Plugin version 2.0.0

These step-by-step instructions will show you how to install the CodeScan plugin.

1.  Click the CodeScan icon on the left panel.\


    <figure><img src="../../../.gitbook/assets/image (537).png" alt="" width="293"><figcaption></figcaption></figure>
2.  Click on ‘Add CodeScan Connection.’\


    <figure><img src="../../../.gitbook/assets/image (538).png" alt="" width="375"><figcaption></figcaption></figure>
3. Add your CodeScan URL.
4. Click on 'Generate Token.' This will open CodeScan in a browser.
5. Click 'Allow Connection' to send the newly generated token back to your IDE.
6. Add your organization key.
7. Enter a Unique Connection Name.
8.  Click on 'Save Connection.' You will be able to see your connection appear in your connected mode window.\


    <figure><img src="../../../.gitbook/assets/image (539).png" alt="" width="229"><figcaption></figcaption></figure>
9.  Click on your connection (CodeScan Cloud in the example.)\


    <figure><img src="../../../.gitbook/assets/image (540).png" alt="" width="375"><figcaption></figcaption></figure>
10. Click the + symbol that appears to the right. This will show you a list of projects from the Command palette.
11. Select the project you would like to connect to.
12. The project you connect to determines the rules for scanning your open files.

{% hint style="info" %}
**Note**: If the project you have open in VS Code matches the project you connect to in CodeScan Cloud, your IDE scans will ignore any Won’t Fix or False Positive issues.
{% endhint %}



## Get Started with VS Code

The **CodeScan VS Code** extension provides immediate feedback to developers on bugs and quality issues; it is a fully integrated user experience in Visual Studio Code (we'll refer to it as VS Code).

#### Prerequisites

Make sure you:

1. Install the latest VS Code version.
2. Have a CodeScan cloud account (with valid enterprise or trial license).
3. For CodeScan Self Hosted:\
   Have a working SonarQube™ (9.9+) server\
   Have a licensed, latest version of CodeScan plugin to get started ([more](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key) [info](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key)).
4. Download the CodeScan extension from the marketplace
5. Download the Salesforce Extension pack from the marketplace if you are working with Salesforce code or, at a minimum, the Visualforce plugins.
6. Install the JDK version 17 or above.
7. Install the Java Runtime (JRE) 17 version or later.
8. Install the latest available Node.js LTS version.
9. Uninstall the Apex PMD and SonarLint™ plugins. The CodeScan and VS Code plugin will not work with SonarLint™ or Apex PMD installed.

{% hint style="warning" %}
**Version 2.0.0 requires Java Runtime (JRE) / JDK versions 17 or later. Prior CS versions will still work with older JRE / JDK versions 11.**
{% endhint %}

{% hint style="info" %}
**Note:** CodeScan plugin is designed to work with a single VS Code window at a time. Using CodeScan plugin with multiple VS Code windows open may give unexpected results.
{% endhint %}



## Installing the 'CodeScan for VS Code' extension

Follow the installation instructions for the CodeScan extension and bind the extension to your CodeScan server.

**Step 1: Install CodeScan for VS Code Extension**

1. Open Visual Studio Code and go to the Activity Bar on your left. The last button on the Activity Bar is the Extensions button.

{% hint style="info" %}
**Note:** You can also press the Shortcut Key combination Ctrl + Shift + X to launch the Extensions side panel.
{% endhint %}

2. Search for CodeScan and click on Install to install the CodeScan latest extension, preferably version 1.6.8 or above.
3. Once installed, restart or reload VS Code to ensure it's taken effect.

**Step 2: Java Runtime (JRE) 11 Installation**

CodeScan should automatically find the JRE installed on your computer. Or you can specify the JRE path on your VS Code's Settings page by navigating to VS Code Settings > Settings > Extensions > CodeScan.

1.  Under CodeScan > Ls: Java Home _(Not synced)_, enter the JRE path. \


    <figure><img src="../../../.gitbook/assets/image (541).png" alt=""><figcaption></figcaption></figure>
2. Next, confirm the JAVA\_HOME variable is set properly on your system. Enter the command echo %JAVA\_HOME%. This should output the path to your Java installation folder. Reach out to your IT department if the JAVA\_HOME variable is not set.

**Step 3: Generate CodeScan token**

You can generate new tokens at User > My Account > Security or use an existing token if you have one saved. Copy the generated token and add it to the settings.json file (discussed later).

**Step 4: Obtain the Project Key**

Log in to CodeScan, click on the Projects tab, and find the project you need to configure. Click on the Project Information tab to find your project key at the bottom right of your screen.

**Step 5: Obtain the Organization Key**

You can always find your organization key at the top right of your organization home page.

<figure><img src="../../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

**Step 6: Add CodeScan Configuration**

1.  Press Ctrl + Shift + P in the VS Code, and search for Settings and select Open User Settings (JSON).\


    <figure><img src="../../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>
2.  On the settings.json tab, inside the curly braces ({ }), copy and paste the following text, and add the parameters shown in the table below:\


    <figure><img src="../../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

**Example:**

<figure><img src="../../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="192">PARAMETER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>serverID</td><td>Add <em>serverId</em> with a value you will remember. You will need to enter the same value in both of the <em>serverId</em> parameters.</td></tr><tr><td><a href="https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys">organizationKe</a> <a href="https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys">y</a></td><td>Add your CodeScan organization key. If you are using CodeScan Self-Hosted, enter your default-organization.</td></tr><tr><td>serverUrl</td><td>For CodeScan Cloud, enter: https://app.codescan.io/for U.S. region, https://app-eu.codescan.io/ for EU, and https://app-aus.codescan.io/ for AUS.</td></tr></tbody></table>

For Self-Hosted CodeScan, add _serverUrl_ as your SonarQube™ _server URL_ (default is _http://localhost:9000_). |&#x20;

\|  [token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token) | Add your security token. For Self-Hosted CodeScan, add token generated in SonarQube™. |&#x20;

\|  [cell](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key) | Add your CodeScan project key.| | codescan.httpclient.version | (applicable for VS Code v1.6.10 or later)&#x20;

\| Enter the Apache HTTP client protocol version (FORCE\_HTTP\_1, FORCE\_HTTP\_2, or NEGOTIATE). |

{% hint style="info" %}
**Note:** If no protocol version is set, the default protocol is NEGOTIATE.
{% endhint %}

3. Save the settings.json file.

**Step 7: Configure the Project Binding**

Next, you will need to update the CodeScan bindings for the workspace to ensure the rules are in sync.

Select:

* Shift+Command+P or -
* Shift+Command+P (Mac) to open the Command Palette. Type in CodeScan to bring up the CodeScan commands and run Update CodeScan binding to SonarQube/CodeScan Cloud.

An All CodeScan bindings successfully updated notification appears once the binding is successfully completed.

**Step 8: Verifying**

You can verify this by opening a file that has problems. They will now be highlighted within your code:

An underline shows a pop-up of the issue when hovering:

<figure><img src="../../../.gitbook/assets/image (547).png" alt=""><figcaption></figcaption></figure>

Within the VS Code problems panel

<figure><img src="../../../.gitbook/assets/image (548).png" alt=""><figcaption></figcaption></figure>

## Integrate VS Code with CodeScan extension

Once you're done installing the CodeScan extension from the marketplace,

1. Restart the Visual Studio Code.
2. Press Ctrl + Shift + P and search for Settings and select 'Open User Settings (JSON).'

<figure><img src="../../../.gitbook/assets/image (549).png" alt=""><figcaption></figcaption></figure>

3.  On the settings.json tab, inside the curly braces ({ }), copy and paste the following text:\


    <figure><img src="../../../.gitbook/assets/image (550).png" alt=""><figcaption></figcaption></figure>

Plain text copy

<figure><img src="../../../.gitbook/assets/image (551).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="252">Parameters</th><th>Description</th></tr></thead><tbody><tr><td>serverId</td><td>Add <em>serverId</em> with a value you will remember. You will need to enter the same value in both of the <em>serverId</em> parameters.</td></tr><tr><td><a href="https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys">organizationKey</a></td><td><p>Add your CodeScan organization key. If you are using CodeScan Self Hosted,</p><p>please enter your <em>default-organization</em>.</p></td></tr><tr><td>serverUrl</td><td><p>For <em>CodeScan cloud</em>, please enter:</p><p>https://app.codescan.io/ for US region, https://app-eu.codescan.io for EU, and https://app-aus.codescan.io/ for AUS.</p></td></tr><tr><td>token</td><td>Add your security token. For self-hosted CodeScan, add token generated in SonarQube.</td></tr><tr><td>projectKey</td><td>Add your CodeScan project key.</td></tr><tr><td>codescan.httpclient.version (applicable for VS Code v1.6.10 or later)</td><td>Enter the Apache HTTP client protocol vesion (FORCE_HTTP_1, FORCE_HTTP_2 or NEGOTIATE). <br>Note: If no protocol is set, the default of NEGOTIATE is used.</td></tr></tbody></table>

4. Save the settings.json file.
5. Now select Ctrl+Shift+P (Windows/Linux) or Shift+Command+P (Mac) to open the Command Palette.
6. Type in  CodeScan to bring up the CodeScan commands and run Update CodeScan binding to SonarQube/CodeScan Cloud.
7.  Go to View > Output to view the logs details. If a problem does occur, you are able to trace it via logs.\


    <figure><img src="../../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>
8. Select Terminal>New Terminal or press Ctrl+Shift+\`, if you are not able to view the Output section at the bottom of the screen.
9. An 'All CodeScan bindings successfully updated' notification appears if the binding is successfully completed.
10. If any changes are made on the SonarQube™ server, then repeat this step.\


    <figure><img src="../../../.gitbook/assets/image (553).png" alt=""><figcaption></figcaption></figure>
11. Open a file, and you should see the issues in your code underlined.\


    <figure><img src="../../../.gitbook/assets/image (554).png" alt=""><figcaption></figcaption></figure>



## Visual Studio Code behind a proxy

VS Code extensions can be difficult to use behind a proxy. To point CodeScan at the correct proxy, all it takes is a single environment variable for your system.

The environment variable is: JAVA\_TOOL\_OPTIONS

Follow the steps to set environment variables using the Windows GUI:

1. Press Windows+R to open the Windows Run prompt.
2. Type in svsdm.cpl and click ok.
3. Open the 'Advanced' tab and click on the Environment Variables button in the System Properties window.
4. The Environment Variables window is divided into two sections. Click the button on the top section.
5. In the New User Variable prompt, enter the Variable Name as JAVA\_TOOL\_OPTIONS, enter the following Variable Value, and click OK.

Variable Value:

* \-Dhttp.proxyHost=\[YOUR\_PROXY\_HOST]
* \-Dhttp.proxyPort=\[YOUR\_PROXY\_PORT]
* \-Dhttps.proxyHost=\[YOUR\_PROXY\_HOST]
* \-Dhttps.roxyPort=\[YOUR\_PROXY\_PORT]
* Dhttp.nonProxyHosts="localhost | 127.0.0.1"

If the proxy has a _username_ and _password_, you can add/update the following parameters and add them at the end of the variable value field.

* \-Dhttps.proxyUser=your\_username
* \-Dhttps.proxyPassword=your\_password



## Self-Signed Certificates

If you are connecting to a server with self-signed certificates, you will need to specify them for your Java and Node installations.

For your Java installation, you can find the documentation [ here](https://docs.oracle.com/en/java/javase/11/security/java-security-overview1.html#GUID-054AD71D-D449-47FF-B6F7-F416DA821D46).

For Node installation, add the environment variable 'NONDEEXTRACA\_CERTS' with the path to your certificate file as a value, e.g., /usr/local/share/ca-certificates/YOUR\_CERT.crt.



## VS Code Troubleshooting

**PKIX Certificate error**

**Error Code:**

javax.net.ssl.SSLHandshakeException:&#x20;

sun.security.validator.ValidatorException:&#x20;

PKIX path building failed:&#x20;

sun.security.provider.certpath.SunCertPathBuilderException:&#x20;

unable to find valid certification path to requested target.\


**Reason:** This error occurs when the Java environment does not trust the certificate of the server running your SonarQube instance.

**Solution**: Install the server certificate to the Java key.

**Steps:**

1. In your browser, to the left of the URL, there is a lock icon (![](<../../../.gitbook/assets/image (557).png>)).
2. Click on this icon and a window will pop up. From the window, select Connection is secure.\
   ![](<../../../.gitbook/assets/image (558).png>)
3. Select the second option, i.e., Certificate is valid.\
   ![](<../../../.gitbook/assets/image (559).png>)
4. Go to the Details tab and click on Export.\
   ![](<../../../.gitbook/assets/image (560).png>)
5.  Rename the certificate (e.g., _codescan-certificate_), then choose a location and save the certificate.\


    <figure><img src="../../../.gitbook/assets/image (561).png" alt=""><figcaption></figcaption></figure>
6. The next process is to install the certificate in the cacerts file of the jdk installed in the system using the command line.

**Command:**

keytool -import -alias _{alias-name for the certificate}_ -keystore _“{path for the cacerts file}”_ -file _{path where we have save the certificate}_

**Example:**

keytool -import -alias _codescan-certificate_ -keystore _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ -file _c:/tmp/codescan- certificate.crt_

When adding the certificate, a password is required. The password is: changeit.

{% hint style="info" %}
**Note:** If adding the certificate as a trusted certificate to the Java Keystore still results in the PKIX path building failed error, we suggest you delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.
{% endhint %}

**Command to list all of the certificates from the Java Keystore:**

keytool -list -v -keystore _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v -keystore _“c:\Program Files\Java\jdk- 11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt

**Command to delete the certificate:**

keytool -delete -noprompt -alias _{alias-name for the certificate}_ -keystore

_“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt -alias _codescan-certificate_ -keystore _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_

**CodeScan Update Binding Failed**

If the CodeScan update binding is failing, try disabling the VPN and antivirus, then try updating the binding again.

**If the binding successfully updates**, the error occurred due to antivirus blocking CodeScan. Add CodeScan to the list of allowed sites for the antivirus in use.

**If the binding still fails**, check the HTTP client protocol version. Enter the Apache HTTP client protocol version (FORCE\_HTP\_1, FORCE\_HTTP\_2, or NEGOTIATE). Save and Update Bindings.  Further documentation is available [here in the](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code?highlight=http%20client\&integrate-vs-code-with-codescan-extension) '[Parameters' section](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-vs-code?highlight=http%20client\&integrate-vs-code-with-codescan-extension).

<figure><img src="../../../.gitbook/assets/image (562).png" alt=""><figcaption></figcaption></figure>

**If the binding still fails**, raise a [Support Ticket](https://support.autorabit.com/portal/en/home), including the analyzer logs and verbose logs in the attachment.

Issue when ApexPMD plugin installed along with the CodeScan plugin

If Apex PMD plugin is installed alongside the CodeScan plugin, one or more of the following issues may occur:

* CodeScan is not listed in the dropdown in Output Tab of VS Code terminal.
* Inconsistency in the number of issues for a file on saving the file.&#x20;
* Problems for a specific file are displayed even when the file is closed.

All these issues can be resolved by uninstalling Apex PMD plugin and restarting IDE, then updating the Binding to CodeScan Cloud.

**CodeScan and Java Runtime Environment (JRE) sync issue**

CodeScan should automatically find the JRE installed on your computer. If you have trouble, then you can specify the JRE path on your VS Code's Settings page.

**Navigation: VS Code Settings > Settings > Extensions > CodeScan.**

Under CodeScan > Ls: Java Home _(Not synced)_, enter the JRE path.

<figure><img src="../../../.gitbook/assets/image (565).png" alt=""><figcaption></figcaption></figure>

**How do I see warnings and errors in VS Code?**

You can click on the summary or press Ctrl+Shift+M to display the Problems panel with a list of all current errors. If you open a file that has errors or warnings, they will be rendered inline with the text and in the overview ruler.

{% hint style="info" %}
**Note:** The VS Code displays the code issues related to bugs, vulnerabilities and code smells inside the PROBLEMS tab. No code-duplications are shown in the IDE.
{% endhint %}

**Other useful debugging information**

&#x20;Some useful debugging information is available under the Output window under the CodeScan tab.

Also, you can check for any serious errors by going to Help>Toggle Developer Tools to bring up the console.

## Raising a support ticket

Before raising a support ticket, perform the following checks in VS Code:

* Are Sonarlint or ApexPmd plugin installed alongside CodeScan? _If so, uninstall it._
* Is the Salesforce extension pack installed in VS Code ? _If not, install as this is mandatory._
* What version of Java is installed? _Java 11 version is required_
* Is the Java path passed to CodeScan (codescan.ls.javaHome)? Verify by going to VS Code Settings>Settings?Extensions>CodeScan and under CodeScan>LS: Java Home (Not synced), you should see the JAVA\_HOME path metioned. If not present, please enter the JAVA\_HOME path.&#x20;
*   You can also add the JAVA\_HOME path in the settings.json file inside codescan.ls.javaHome property. \


    <figure><img src="../../../.gitbook/assets/image (566).png" alt=""><figcaption></figcaption></figure>
* Perform the CodeScan Update Binding and check if the issue is resolved.

#### What's Next?

If you're still having issue with VS Code, raise a support ticket on the [CodeScan](https://support.autorabit.com/portal/en/home) [Support Page](https://support.autorabit.com/portal/en/home) and share with us the following information:

In settings.json file, please add the below properties inside the curly braces ({ }) to get debug level logs:

"codescan.output.showVerboseLogs": true,\
"codescan.output.showAnalyzerLogs": true,

Update the CodeScan binding and share the logs with us.



### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Salesforce Connect OData 4.0 license subscription.

{% hint style="info" %}
**Note:** Not required for free developer edition org.
{% endhint %}

### Limitations <a href="#limitations" id="limitations"></a>

1. Files and attachments are not supported for viewing through external objects in Salesforce. This will be supported in the upcoming version of Vault Connect scheduled for the end of Q4’23.
2. Salesforce OData 4.0 adapter has a limitation on the number of callouts per hour. This will be addressed with the support for the Salesforce OData 4.01 adapter in subsequent versions of the capability.
3. Relationships between external objects and Salesforce objects need to be established manually (like if cases are archived and they are related to accounts that are not archived, the reference to accounts that are in the Salesforce object will be available in the external object but will not be reflected as a lookup relationship). The plan is to support the automated recreation of these references by the end of Q4 2023.
4. All the limitations of Salesforce external objects are applicable as mentioned in this article: [Help and Training Community](https://help.salesforce.com/s/articleView?language=en\_US\&id=sf.platform\_connect\_general\_limits.htm\&type=5)
5. The solution only supports customers configured with AWS S3 as a storage option in Vault.
6. There is a max limit of 5GB of archived data per customer supported for connecting to Salesforce external data source as part of the beta program. This can be extended to a higher limit by raising a request with [support@autorabit.com](mailto:support@autorabit.com).
7. Fields of type XmlObjectWrapper are not supported.
8.  Fields of the object that have soapType as double, values will be truncated according to the precision and scale, as defined in the metadata of the object’s field.

    **For example:** If a field holds decimal value information for that object, precision and scale values will be predefined.

    **Precision:** The maximum number of digits in a numeric value includes all numbers to the left and to the right of the decimal point (but excludes the decimal point character).

    **Scale:** The number of digits to the right of the decimal point in a numeric value must be less than the precision value.

**Example 1:**&#x20;

Define a custom number field, e.g., "Number." Give it length = 3 and decimal places = 1 (scale). It might seem that this is done to restrict the precision of the field to one decimal place. However, on the UI level (on a standard edit page), if you try to type in, for example, 237.631, it will round it off to 237.631. Here precision is 4 and scale is 1. When mapping it back to Salesforce as the external object’s field, the value will be truncated to 237.6.

**Example 2:**&#x20;

Say a field holds info on geo location latitude and longitude and their precision and scale are 5 and 2, respectively. Assign the value as 77.2090, then when mapping it back to Salesforce as the external object’s field, it will be truncated to 77.20.
