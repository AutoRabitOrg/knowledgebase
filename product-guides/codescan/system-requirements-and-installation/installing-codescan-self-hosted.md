# Installing CodeScan Self-Hosted

### CodeScan On-Premise Implementation <a href="#codescan-onpremise-implementation" id="codescan-onpremise-implementation"></a>

What's New:

CodeScan Self-Hosted version **23.1.3** _(now compatible with **SonarQube™ version 10.0 or earlier)**_ is the latest CodeScan release. We strongly recommend all CodeScan users upgrade to this iteration.

[**Download**](https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-23.1.3.zip)

[**Release Note**](../../../overview/release-notes/codescan-release-notes/on-prem-releases/release-note-23.1.3.md)

***

### Overview <a href="#overview" id="overview"></a>

This section describes installing the CodeScan self-hosted server, allowing you to experience a _fully functional evaluation version_ of enterprise CodeScan on your server.

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

#### Step 1: Request a CodeScan License Key <a href="#step-1-request-a-codescan-license-key" id="step-1-request-a-codescan-license-key"></a>

<mark style="background-color:blue;">**Note:**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">If you already have a</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**License Key**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">or</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**Subscription Code**</mark><mark style="background-color:blue;">, proceed to step 2.</mark>

**AutoRABIT Access/License Key:** Before downloading the necessary files, email AutoRABIT’s support team at [support@codescan.io](https://support@codescan.io/) to request a **CodeScan License Key.**

Provide the following information in the email:\
• Client Name (first and last – typically the admin)\
• Client Company\
• Email\
• Duration of License (e.g., varies, 30 days)

#### Step 2: Download and Install SonarQube™ & CodeScan Zip Files <a href="#step-2-download-and-install-sonarqube-tm-codescan-zip-files" id="step-2-download-and-install-sonarqube-tm-codescan-zip-files"></a>

#### SonarQube™ Download <a href="#sonarqube-tm-download" id="sonarqube-tm-download"></a>

You must have a SonarQube™ server currently running in your environment. If not, please visit [SonarQube.org](https://www.sonarqube.org/) to download the latest Community version.

At [SonarSource.com](https://www.sonarsource.com/), scroll down to this graphic:\
![\[CS Self-Hosted pic1.png\] https://www.sonarsource.com/products/sonarqube/downloads/lts/9-9-lts/){target="\_blank"}](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Self-Hosted%20pic1\(1\).png)

<mark style="background-color:blue;">Note: This</mark> [<mark style="background-color:blue;">link</mark>](https://www.sonarsource.com/products/sonarqube/) <mark style="background-color:blue;">will take you to the</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**SonarQube™ 9.9 LTS**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">download.</mark> <mark style="background-color:blue;"></mark>_<mark style="background-color:blue;">**SonarQube™ 10.0 is now supported as well.**</mark>_

#### CodeScan Zip File Download <a href="#codescan-zip-file-download" id="codescan-zip-file-download"></a>

1. Download the latest compatible CodeScan version (currently **23.1.3**) from [here](https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-23.1.3.zip).

<mark style="background-color:blue;">Note: Keep in mind you need to download a version compatible with your</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**SonarJS plugin**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">version. Refer to the</mark> [<mark style="background-color:blue;">requirements</mark>](https://knowledgebase.autorabit.com/codescan/docs/codescan-self-hosted) <mark style="background-color:blue;">section for more information.</mark>

2. You will need to enter your **`License Key`** (to be provided by our Support Team) or a **`Subscription Code`**. For more information on Subscription Codes, click [here](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-subscription-code).

![CS Self-Hosted pic2.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Self-Hosted%20pic2.png)

3. Accept our [Terms of Service](https://www.codescan.io/tos/self-hosted/) and click on the **`Request Download`** button.
4. Extract the ZIP file. It contains the **SonarQube™** plugin and an **ant-based tool** enabling you to run an analysis.

#### Download links for previously supported CodeScan versions <a href="#download-links-for-previously-supported-codescan-versions" id="download-links-for-previously-supported-codescan-versions"></a>

<table data-full-width="true"><thead><tr><th>CodeScan Version</th><th>Platform Compatible</th><th>Date of Release</th><th>Support End Date</th><th>Download Link</th><th>Release Note</th></tr></thead><tbody><tr><td><strong>23.1.3 (Current version</strong>)</td><td><strong>SonarQube™ 10.0 or earlier</strong></td><td><strong>13 September 2023</strong></td><td><strong>30</strong> <strong>June 2024</strong></td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-23.1.3.zip"><strong>Download</strong></a></td><td><a href="../../../overview/release-notes/codescan-release-notes/on-prem-releases/release-note-23.1.3.md">https://app.gitbook.com/o/vIHQCTOOUDcNoPic3AQi/s/9vAxMuDrkUkB4OXlH9CL/overview/release-notes/codescan-release-notes/release-note-23.1.3</a></td></tr><tr><td>23.1.1</td><td>SonarQube™ 9.9 or earlier</td><td>12 May 2023</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-23.1.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/release-note-2310#12-may-2023">Release Note</a></td></tr><tr><td>22.8</td><td>SonarQube™ 8.9+ and SonarQube™ 9.9</td><td>25 December 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.8.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/release-note-228">Release Note</a></td></tr><tr><td>22.7</td><td>SonarQube™ 8.9+</td><td>01 November 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.7.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-227">Release Note</a></td></tr><tr><td>22.6.2</td><td>SonarQube™ 8.9+</td><td>12 July 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.6.2.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-224#codescan-v2262">Release Note</a></td></tr><tr><td>22.6.1</td><td>SonarQube™ 8.9+</td><td>23 June 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.6.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-224#codescan-v2261">Release Note</a></td></tr><tr><td>22.6</td><td>SonarQube™ 8.9+</td><td>13 June 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.6.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-224#codescan-v226">Release Note</a></td></tr><tr><td>22.5</td><td>SonarQube™ 8.9+</td><td>30 May 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.5.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-224#codescan-v225">Release Note</a></td></tr><tr><td>22.4</td><td>SonarQube™ 8.9+</td><td>16 May 2022</td><td>30 June 2024</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.4.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-224">Release Note</a></td></tr><tr><td>22.3</td><td>SonarQube™ 8.9+<br>(<em>From SonarQube™ 8.9 onwards, the vulnerability in Log4J has been fixed</em>)</td><td>24 April 2022</td><td>30 June 2023</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.3.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-223">Release Note</a></td></tr><tr><td>22.2.1</td><td>SonarQube™ 7.9 to 8.9, SonarJS 6.2+</td><td>02 February 2022</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.2.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-222">Release Note</a></td></tr><tr><td>22.2</td><td>SonarQube™ 7.9+, SonarJS 6.2+</td><td>26 January 2022</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.2.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-222">Release Note</a></td></tr><tr><td>22.1.1</td><td>SonarQube™ 7.9 to 8.5+, SonarJS 6.2+</td><td>31 December 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.1.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-221">Release Note</a></td></tr><tr><td>22.1</td><td>SonarQube™ 7.9 to 8.4, SonarJS 6.2+</td><td>29 December 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-221">Release Note</a></td></tr><tr><td>21.5.1</td><td>SonarQube™ 7.9 to 8.5+, SonarJS 6.2+</td><td>06 November 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-21.5.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-215">Release Note</a></td></tr><tr><td>21.5</td><td>SonarQube™ 7.9 to 8.4, SonarJS 6.2+</td><td>01 November 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-21.5.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-215">Release Note</a></td></tr><tr><td>4.5.7.1</td><td>SonarQube™ 7.9 to 8.5+, SonarJS 6.2+</td><td>16 April 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-4.5.7.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-45">Release Note</a></td></tr><tr><td>4.5.7</td><td>SonarQube™ 7.9 to 8.4, SonarJS 6.2+</td><td>08 April 2021</td><td>31 December 2022</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-4.5.7.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-release-notes-45">Release Note</a></td></tr></tbody></table>

### Plugin Installation <a href="#plugin-installation" id="plugin-installation"></a>

#### Step 1: Download CodeScan file <a href="#step-1-download-codescan-file" id="step-1-download-codescan-file"></a>

1. Delete any existing Salesforce plugins from your installation.
2. Ensure your **SonarJS plugin** is compatible with the current CodeScan for Lightning version. Currently the supported release requires **version 6.2+** of the **SonarJS plugin**. Click [here](https://www.codescan.io/products/cloud/#self-hosted) to see alternatives.

#### Step 2: CodeScan JAR file <a href="#step-2-codescan-jar-file" id="step-2-codescan-jar-file"></a>

3. Copy CodeScan downloads JAR files, **`sonar-salesforce-plugin-XXX.jar`** and **`sonar-codescanlang-plugin-XXX.jar`** into your SonarQube™ installation at **/extensions/plugins/**.
4. Place JAR files into your **SonarQube™** file installation at **/extensions/plugins/**.
5. Keep the **SonarQube™** file open for the next steps.

#### Step 3: Start Web Server <a href="#step-3-start-web-server" id="step-3-start-web-server"></a>

6. In your **SonarQube™** installation file, open **sonar.properties**, located in the **config** folder (\<SONARQUBE\_HOME>/conf/sonar.properties).
7. **Starting at lines 108-111**, add/replace these to the appropriate web server section and save your changes:

* _sonar.web.host=192.168.0.1_
* _sonar.web.port=80_
* _sonar.web.context=/sonarqube_

8. Lastly, you need to **RUNsonar** to execute the script to **start the server**. In your **SonarQube™ installation file, open, '/bin' folder**, choose **server type**, and **select ‘StartSonar’**. Once rendering is finished, the plugin installation is complete.

### Standard SonarQube™ Setup <a href="#standard-sonarqube-tm-setup" id="standard-sonarqube-tm-setup"></a>

**Step 1: Log in to the SonarQube™ self-hosted instance at** [**http://localhost:9000/**](https://localhost:9000/).\
The default System Admin credentials are _**admin/admin**_:\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-TNEKH28M.png)

**Step 2. Once you've gained access, go to** **`Administrator > Configuration > General Settings`**.

1. Select the **CodeScan tab**.
2. Enter your **CodeScan License Key** in the designated field.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-27R74NM5.png)
3. Click **Save**.
4. You have successfully completed the **CodeScan on-premise integration**. See the instructions below on how to integrate this to ARM.

### CodeScan On-Premise + ARM Integration <a href="#codescan-onpremise-arm-integration" id="codescan-onpremise-arm-integration"></a>

#### Overview <a href="#overview1" id="overview1"></a>

This guide will show you how to integrate the CodeScan self-hosted instance to ARM.

#### CodeScan On-Premise ARM Integration <a href="#codescan-onpremise-arm-integration1" id="codescan-onpremise-arm-integration1"></a>

**Step 1: Generate a SonarQube™ Token**

1. Log in to your SonarQube™ instance.
2. Go to **User > My Account > Security**. Your existing tokens are listed here, each with a **Revoke** button.
3. The form at the bottom of the page allows you to generate new tokens. Once you click the **Generate** button, you will see the token value. **Be sure to copy it immediately; once you dismiss the notification, you will not be able to retrieve it.**
4. This token is used when storing your credentials, such as your username and password, with AutoRABIT.

**Step 2: Store Your SonarQube™ Credentials in ARM**

This initial step is when your **SonarQube™ credentials**, such as your **username** and **password**, are stored in **AutoRABIT.**

1. Log in to your **AutoRABIT account.**
2. Hover your mouse over the **Admin module** and click on the **Credentials tab**.
3. Next, click on **Create Credential** from the right navigation bar.
4. On the next pop-up screen, enter the **Credential Name**.
5. Choose the Credential Type as **Username with Password**.
6. Choose your **Credential Scope**:\
   **Global**: Credentials accessible within the team.\
   **Private**: Credentials for private use.
7. Enter your **SonarQube™ account username**. For password, use the **copied token** mentioned in **Step 1**.
8. Verify you are using your **SonarQube™ username** instead of the **email address** you use to log in to **SonarQube™**.

![CS Self-Hosted pic3.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Self-Hosted%20pic3.png)

9. Click **Save**.

![CS Self-Hosted pic4.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/CS%20Self-Hosted%20pic4.png)

### Setting up Your Quality Profiles <a href="#setting-up-your-quality-profiles" id="setting-up-your-quality-profiles"></a>

1. In the **SonarQube™** self-hosted instance, click on the **`Quality Profiles`** menu.
2. Make sure you have selected the **`Salesforce Lightning profile`** as the default for both the JavaScript and Visualforce and Lightning languages. This can be done with the settings cog to the right of the profile name.

### Running a Scan <a href="#running-a-scan" id="running-a-scan"></a>

There are a few ways to run your scan. The first is using our **SFDX plugin** (this requires that the [Salesforce CLI](https://developer.salesforce.com/tools/sfdxcli) and the [SFDX CodeScan Plugin](https://www.npmjs.com/package/sfdx-codescan-plugin) be installed).

1. Generate a **token** from the **`My Account > Security`** menu in SonarQube™.
2.  Open the command prompt and navigate to:

    ```
    /runner/my-project
    ```
3.  Run the following command:

    {% code overflow="wrap" %}
    ```
    sfdx codescan:run --token <token> --projectkey my-project-key --organization default-organization --server https://your.server.url
    ```
    {% endcode %}

The [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys) above will work for the Community edition of SonarQube™ but may need to be edited depending on your setup using a paid edition.

You can also use **Ant** (this requires **Ant version 1.9+**).

<mark style="background-color:blue;">Note: You will need to edit</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`antbuild.properties`**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">if your SonarQube™ installation is different than usual, or if you have a proxy. You can also edit</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`/runner/antbuild.xml`**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">to customize your workflows.</mark>

**Running SFDX plugin behind a proxy**

To run the SFDX plugin behind a proxy, you will need to pass all the related information in the parameters of the analysis command.

**Example:**

{% code overflow="wrap" %}
```
sfdx codescan:run --server {instanceurl} --token {TKN} --projectkey {PRJ} --organization {ORG} -J-Dhttp.proxyHost=## -J-Dhttp.proxyPort=## -J-Dhttp.proxyUser=## -J-Dhttp.proxyPassword=## -J-Dhttps.proxyHost=## -J-Dhttps.proxyPort=## -J-Dhttps.proxyUser=## -J-Dhttps.proxyPassword=##
```
{% endcode %}

where,

<table data-full-width="true"><thead><tr><th width="192">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>instanceurl</strong></td><td>Enter your CodeScan <em>instance url</em><br><em>example-</em><br><a href="https://app.codescan.io/"><em>https://app.codescan.io</em></a> <em>for US region</em><br><a href="https://app-eu.codescan.io/"><em>https://app-eu.codescan.io</em></a> <em>for EU region</em><br><a href="https://app-aus.codescan.io/"><em>https://app-aus.codescan.io</em></a> <em>for AUS region.</em></td></tr><tr><td><strong>TKN</strong></td><td>Enter your CodeScan <em>security token</em> (For more information on how to generate a security token, see <a href="https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token">Security Token</a>)</td></tr><tr><td><strong>PRJ</strong></td><td>Enter your CodeScan <em>project key</em> (to find your project key, refer to the article <a href="https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key">Project Key</a>)</td></tr><tr><td><strong>ORG</strong></td><td>Enter your <em>CodeScan organization</em> (for more information, see <a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-organizations">Create a new CodeScan Organization</a>)</td></tr></tbody></table>

#### SonarQube™ ant plugin <a href="#sonarqube-tm-ant-plugin" id="sonarqube-tm-ant-plugin"></a>

For more instructions on setting up the **SonarQube™ ant plugin**, see [https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-ant/](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-ant/). You should verify that the ant script's steps are appropriate for your requirements.

1. Create a copy of the **`sonar-project-template`** folder in the runner directory of this folder and put it in the same project. Call **`it /runner/my-project`**. Add the following to the **`sonar-project.properties`** file in the **`my-project`** folder.
2. Set **sonar.login=** to a token available from the **`My Account > Security menu`** in SonarQube™.
3. Set **sonar.projectKey=myproject**
4. Set **sonar.projectName=My Project**
5.  Set **salesforce.username**, **salesforce.password** and **salesforce.url** to your Salesforce **username/password**. Your Salesforce token must also be appended to the end of your **salesforce.password** parameter.\
    **For example:** `salesforce.password=passwordtoken`.\


    > Setting your _Salesforce username_, _password_, and _URL_ is unnecessary if you want to analyze static content. Please use a system administrator user profile for this otherwise you may experience strange errors when downloading the code or executing tests.
6. Open a command prompt and navigate into _**`/runner/my-project`**_
7.  Run the following command:

    {% code overflow="wrap" %}
    ```
    ant -f ../antbuild.xml analyse
    ```
    {% endcode %}

<mark style="background-color:blue;">Note: If the Anyone group is not granted</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**Execute Analysis**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">permission, or if the SonarQube™ instance is secured (</mark><mark style="background-color:blue;">**`sonar.forceAuthentication property`**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">is set to</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`true`**</mark><mark style="background-color:blue;">), a user whose credentials have</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`Execute Analysis`**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">permission has to be provided through the</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`sonar.login`**</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">and</mark> <mark style="background-color:blue;"></mark><mark style="background-color:blue;">**`sonar.password properties`**</mark><mark style="background-color:blue;">.</mark>

### Proxies <a href="#proxies" id="proxies"></a>

* If your network has a proxy, you must pass some more parameters to avoid license errors.
* A guide for this is available [HERE](https://knowledgebase.autorabit.com/codescan/docs/setting-up-codescan-for-use-with-a-proxy).

### Having trouble? <a href="#having-trouble" id="having-trouble"></a>

* Read the tutorials
* Check the troubleshooting section
* Contact [Support](https://www.codescan.io/contact/)

***

\
