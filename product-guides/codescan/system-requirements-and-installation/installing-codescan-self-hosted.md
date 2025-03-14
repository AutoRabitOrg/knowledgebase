# Installing CodeScan Self-Hosted

As part of our commitment to providing the best possible products and services, we periodically discontinue support for older software versions. All **CodeScan self-hosted versions below 23.1.1** will reach their **End of Life (EOL)** on **December 31, 2024**.

## CodeScan Self-Hosted Installation <a href="#codescan-onpremise-implementation" id="codescan-onpremise-implementation"></a>

What's New:

CodeScan Self-Hosted now has two versions available to meet your operating system needs:

**CodeScan version 25.1.0 Eagle Edition v3.0** (now compatible with _**SonarQube™ versions 10.1 to 10.7)**_ is the latest CodeScan release. We strongly recommend all CodeScan users upgrade to this iteration.

**CodeScan version 25.0.1 Tiger Edition v3.0** _(_&#x6E;ow compatible with _**SonarQube™ version 10.3 or earlier)**_ is a newer version of the CodeScan release for users running older versions of SonarQube™.&#x20;

[**Downloads & Compatibility Chart**](https://knowledgebase.autorabit.com/product-guides/codescan/system-requirements-and-installation/installing-codescan-self-hosted#codescan-downloads-and-compatibility-chart)

[**Release Notes**](https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases)

***

### Overview <a href="#overview" id="overview"></a>

This section describes installing the CodeScan self-hosted server, allowing you to experience a _fully functional evaluation version_ of enterprise CodeScan on your server.

### Prerequisites <a href="#prerequisite" id="prerequisite"></a>

#### Step 1: Request a CodeScan License Key <a href="#step-1-request-a-codescan-license-key" id="step-1-request-a-codescan-license-key"></a>

{% hint style="info" %}
**Note:** If you already have a **License Key** or **Subscription Code**, proceed to step 2.
{% endhint %}

**AutoRABIT Access/License Key:** Before downloading the necessary files, email AutoRABIT’s support team at [support@autorabit.com](mailto:support@autorabit.com) to request a **CodeScan License Key.**

Provide the following information in the email:\
• Client Name (first and last – typically the admin)\
• Client Company\
• Email\
• Duration of License (e.g., varies, 30 days)

#### Step 2: Download and Install SonarQube™ & CodeScan Zip Files <a href="#step-2-download-and-install-sonarqube-tm-codescan-zip-files" id="step-2-download-and-install-sonarqube-tm-codescan-zip-files"></a>

#### SonarQube™ Download <a href="#sonarqube-tm-download" id="sonarqube-tm-download"></a>

You must have a SonarQube™ server currently running in your environment. If not, please visit [SonarQube.org](https://www.sonarqube.org/) to download the latest Community version.

The following matrix identifies the current versions of SonarQube™ supported for CodeScan Self-Hosted/On-Premises clients:

## SonarQube™ Compatibility Matrix <a href="#sonarqube-tm-download" id="sonarqube-tm-download"></a>

<table data-full-width="true"><thead><tr><th width="125">CodeScan On-Premises Plug-In</th><th width="119" align="center">SQ 9.9 LTA</th><th width="92">SQ 10.0</th><th width="84">SQ 10.1</th><th width="80">SQ 10.2</th><th width="79">SQ 10.3</th><th width="79">SQ 10.4</th><th width="95">SQ 10.5</th><th width="100">SQ 10.6</th><th>SQ 10.7</th><th>SQ 10.8</th><th>SQ 2025.1 LTA</th></tr></thead><tbody><tr><td>25.0.1 (Feb 2025) Tiger v3.0</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>25.1.0 (Feb 2025) Eagle v3.0</td><td align="center"><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td></tr><tr><td>24.0.13 Tiger v2.0 (Nov 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.1.1 Eagle v2.0 (Nov 2024)</td><td align="center"><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.0.9 Tiger (Sept 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.1.0 Eagle (Aug 2024)</td><td align="center"><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.0.8 (July 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.0.5 (June 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.0.4 (April 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>24.0.1 (Jan 2024)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr><tr><td>23.1.3 (Sept 2023)</td><td align="center"><mark style="color:green;">✓</mark></td><td><mark style="color:green;">✓</mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td><td><mark style="color:red;"><strong>⮾</strong></mark></td></tr></tbody></table>

At [SonarSource.com](https://www.sonarsource.com/), find the latest compatible version with the CodeScan version you are using.

{% hint style="info" %}
**Note:** This [link](https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.9.6.92038.zip?_gl=1*fhgchu*_gcl_au*MjA5Mjk3NjYzNi4xNzIyMjY5Nzg1*_ga*NjMyNjYxNTE5LjE3MjIyNjk3ODQ.*_ga_9JZ0GZ5TC6*MTcyMjI2OTc4My4xLjEuMTcyMjI3MDE3OS4xNC4wLjA.) will take you to the **SonarQube™ 9.9 LTA** download.&#x20;
{% endhint %}

#### CodeScan Zip File Download <a href="#codescan-zip-file-download" id="codescan-zip-file-download"></a>

1. Download the latest compatible CodeScan version from [here](https://license.code-scan.com/index.php/download/sonar-salesforce-plugin-24.0.8.zip).

{% hint style="info" %}
**Note:** Keep in mind you need to download a version compatible with your **SonarJS plugin** version. Refer to the [requirements](https://knowledgebase.autorabit.com/codescan/docs/codescan-self-hosted) section for more information.
{% endhint %}

2. You will need to enter your **`License Key`** (to be provided by our Support Team) or a **`Subscription Code`**. For more information on Subscription Codes, click [here](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-subscription-code).\
   ![](<../../../.gitbook/assets/image (1500).png>)
3. Accept our [Terms of Service](https://www.codescan.io/tos/self-hosted/) and click on the **`Request Download`** button.
4. Extract the ZIP file. It contains the **SonarQube™** plugin and an **ant-based tool** enabling you to run an analysis.

## CodeScan Downloads & Compatibility Chart



<table data-full-width="false"><thead><tr><th width="115">CodeScan Version</th><th width="125">Platform Compatible</th><th width="103">Release Date</th><th width="104">Support End Date</th><th width="107">Link</th><th width="126">Release Note</th></tr></thead><tbody><tr><td><strong>25.1.0 Eagle</strong> <strong>v.3.0</strong></td><td><strong>SonarQube™ 10.1 - 10.7</strong> </td><td><strong>February 2025</strong></td><td><strong>February 2026</strong></td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-25.1.0.zip"><strong>Download</strong></a></td><td><a href="https://knowledgebase.autorabit.com/release-notes/release-notes/codescan-release-notes/on-premise-releases/eagle-edition/release-notes-25.1.0-eagle-3.0"><strong>Release Note</strong></a></td></tr><tr><td><strong>25.0.1 Tiger v3.0</strong> </td><td><strong>SonarQube™ 10.0 - 10.3</strong><br><strong>9.9 LTA</strong></td><td><strong>February 2025</strong></td><td><strong>February 2026</strong></td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-25.0.1.zip"><strong>Download</strong></a></td><td><a href="https://knowledgebase.autorabit.com/release-notes/release-notes/codescan-release-notes/on-premise-releases/tiger-edition/release-notes-25.0.1-tiger-3.0"><strong>Release Note</strong></a></td></tr><tr><td>24.1.1 Eagle v2.0</td><td>SonarQube™ <br>10.1 - 10.6 </td><td>November 2024</td><td>November 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.1.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases/release-notes-24.1.1-eagle-2.0">Release Note</a></td></tr><tr><td>24.0.13 Tiger v2.0</td><td>SonarQube™ <br>10.0 - 10.3<br>9.9 LTA</td><td>November 2024</td><td>November 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.0.13.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases/release-notes-24.0.13-tiger-2.0">Release Note</a></td></tr><tr><td>24.1.0 Eagle</td><td>SonarQube™ <br>10.1 - 10.6 </td><td>August 2024</td><td>August 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.1.0.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases/release-notes-24.1.0-eagle#release-notes-self-hosted-on-prem-24.1.0-eagle-edition">Release Note</a></td></tr><tr><td>24.0.9 Tiger</td><td>SonarQube™ <br>10.0 - 10.3<br>9.9 LTA</td><td>September 2024</td><td>September 2025</td><td><a href="https://license.code-scan.com/index.php/download/sonar-salesforce-plugin-24.0.9.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases/release-notes-24.0.9-tiger#release-notes-self-hosted-on-prem-24.0.9-tiger-edition">Release Note</a></td></tr><tr><td>24.0.8</td><td>SonarQube™ <br>10.2<br>10.1 <br>9.9 LTA</td><td>July 2024</td><td>July 2025</td><td><a href="https://license.code-scan.com/index.php/download/sonar-salesforce-plugin-24.0.8.zip">Download</a></td><td><a href="../../../release-notes/release-notes/codescan-release-notes/on-premise-releases/prior-editions/release-notes-24/release-notes-24.0.8.md">Release Note</a></td></tr><tr><td>24.0.5</td><td>SonarQube™ <br>10.2<br>10.1 <br>9.9 LTA</td><td>June 2024</td><td>June 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.0.5.zip">Download</a></td><td><a href="../../../release-notes/release-notes/codescan-release-notes/on-premise-releases/prior-editions/release-notes-24/release-notes-24.0.5.md">Release Note</a></td></tr><tr><td>24.0.4</td><td><p>SonarQube™ <br>10.2</p><p>10.1<br>9.9 LTA</p></td><td>April 2024</td><td>April 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.0.4.zip">Download</a></td><td><a href="../../../release-notes/release-notes/codescan-release-notes/on-premise-releases/prior-editions/release-notes-24/release-notes-24.0.4.md#release-notes-24.0.4">Release Note</a></td></tr><tr><td>24.0.1</td><td><p>SonarQube™ <br>10.2</p><p>10.1 </p><p>9.9 LTA</p></td><td>January 2024</td><td>30 January 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-24.0.1.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/overview/release-notes/codescan-release-notes/on-premise-releases/release-notes-24.0.1">Release Note</a></td></tr><tr><td>22.8</td><td>SonarQube™<br>9.9 LTA<br>8.9 (Previous LTA)</td><td>25 December 2022</td><td>30 April 2025</td><td><a href="https://license.code-scan.com/index.php/download/login?path=sonar-salesforce-plugin-22.8.zip">Download</a></td><td><a href="https://knowledgebase.autorabit.com/codescan/docs/release-note-228">Release Note</a></td></tr></tbody></table>

### Plugin Installation <a href="#plugin-installation" id="plugin-installation"></a>

#### Step 1: Download CodeScan file <a href="#step-1-download-codescan-file" id="step-1-download-codescan-file"></a>

1. Delete any existing Salesforce plugins from your installation.
2. Ensure your **SonarJS plugin** is compatible with the current CodeScan for Lightning version. Currently the supported release requires **version 6.2+** of the **SonarJS plugin**. Click [here](https://www.codescan.io/products/cloud/#self-hosted) to see alternatives.

#### Step 2: CodeScan JAR file <a href="#step-2-codescan-jar-file" id="step-2-codescan-jar-file"></a>

3. Copy CodeScan downloads JAR files, **`sonar-salesforce-plugin-XXX.jar`** and **`sonar-codescanlang-plugin-XXX.jar`** into your SonarQube™ installation at **/extensions/plugins/**.
4. Place JAR files into your **SonarQube™** file installation at **/extensions/plugins/**.
5. Keep the **SonarQube™** file open for the next steps.

#### Step 3: Start Web Server  <a href="#step-3-start-web-server" id="step-3-start-web-server"></a>

6. Lastly, you need to **RUNsonar** to execute the script to **start the server**. In your **SonarQube™ installation file, open, '/bin' folder**, choose **server type**, and **select ‘StartSonar’**. Once rendering is finished, the plugin installation is complete.

### Standard SonarQube™ Setup <a href="#standard-sonarqube-tm-setup" id="standard-sonarqube-tm-setup"></a>

**Step 1: Log in to the SonarQube™ self-hosted instance at** [**http://localhost:9000/**](https://localhost:9000/).\
The default System Admin credentials are _**admin/admin**_:

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Step 2. Once you've gained access, go to** **`Administrator > Configuration > General Settings`**.

1. Select the **CodeScan tab**.
2. Enter your **CodeScan License Key** in the designated field.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Click **Save**.
4. You have successfully completed the **CodeScan on-premises integration**. See the instructions below on how to integrate this to ARM.

## CodeScan On-Premises + ARM Integration <a href="#codescan-onpremise-arm-integration" id="codescan-onpremise-arm-integration"></a>

### Overview <a href="#overview1" id="overview1"></a>

This guide will show you how to integrate the CodeScan self-hosted instance with ARM.

### CodeScan On-Premises ARM Integration <a href="#codescan-onpremise-arm-integration1" id="codescan-onpremise-arm-integration1"></a>

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

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Click **Save**.

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

{% hint style="info" %}
**Note:** You will need to edit **`antbuild.properties`** if your SonarQube™ installation is different than usual, or if you have a proxy. You can also edit **`/runner/antbuild.xml`** to customize your workflows.
{% endhint %}

### **Running SFDX plugin behind a proxy**

To run the SFDX plugin behind a proxy, you will need to pass all the related information in the parameters of the analysis command.

**Example:**

{% code overflow="wrap" %}
```
sfdx codescan:run --server {instanceurl} --token {TKN} --projectkey {PRJ} --organization {ORG} -J-Dhttp.proxyHost=## -J-Dhttp.proxyPort=## -J-Dhttp.proxyUser=## -J-Dhttp.proxyPassword=## -J-Dhttps.proxyHost=## -J-Dhttps.proxyPort=## -J-Dhttps.proxyUser=## -J-Dhttps.proxyPassword=##
```
{% endcode %}

where,

<table data-full-width="true"><thead><tr><th width="187">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>instanceurl</strong></td><td>Enter your CodeScan <em>instance url</em><br><em>example-</em><br><a href="https://app.codescan.io/"><em>https://app.codescan.io</em></a> <em>for US region</em><br><a href="https://app-eu.codescan.io/"><em>https://app-eu.codescan.io</em></a> <em>for EU region</em><br><a href="https://app-aus.codescan.io/"><em>https://app-aus.codescan.io</em></a> <em>for AUS region.</em></td></tr><tr><td><strong>TKN</strong></td><td>Enter your CodeScan <em>security token</em> (For more information on how to generate a security token, see <a href="https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token">Security Token</a>)</td></tr><tr><td><strong>PRJ</strong></td><td>Enter your CodeScan <em>project key</em> (to find your project key, refer to this article: <a href="https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key">Project Key</a>)</td></tr><tr><td><strong>ORG</strong></td><td>Enter your <em>CodeScan organization</em> (for more information, see <a href="https://knowledgebase.autorabit.com/codescan/docs/codescan-organizations">Create a new CodeScan Organization</a>)</td></tr></tbody></table>

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

{% hint style="info" %}
**Note:** If the Anyone group is not granted **Execute Analysis** permission, or if the SonarQube™ instance is secured (**`sonar.forceAuthentication property`** is set to **`true`**), a user whose credentials have **`Execute Analysis`** permission has to be provided through the **`sonar.login`** and **`sonar.password properties`**.
{% endhint %}

### Proxies <a href="#proxies" id="proxies"></a>

* If your network has a proxy, you must pass some more parameters to avoid license errors.
* A guide for this is available [HERE](https://knowledgebase.autorabit.com/codescan/docs/setting-up-codescan-for-use-with-a-proxy).

### Having trouble? <a href="#having-trouble" id="having-trouble"></a>

* Read the tutorials
* Check the troubleshooting section
* Contact [Support@autorabit.com](mailto:support@autorabit.com).
