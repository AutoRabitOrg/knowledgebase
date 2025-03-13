# System Requirements and Installation Self-Hosted

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

You must have a SonarQube™ server currently running in your environment. If you do not, please visit [SonarQube.org](https://www.sonarqube.org/) to get set up.

### Hardware Requirements <a href="#hardware-requirements" id="hardware-requirements"></a>

1. At least **8GB of RAM** to run efficiently. If you are installing an instance for a large teams or Enterprise, do consider the additional recommendations of **16GB of RAM**.
2. **2 CPU cores** (equivalent to AWS t2.large)
3. **100GB** of disk space.
4. CodeScan must be installed on hard drives that have excellent read & write performance.

{% hint style="info" %}
**Note:** Depending on your use case, this may be way too much or too little. As SonarQube™ stores all snapshots for a long time, the data can build up for a large project. Additionally, heavy usage for users would cause more load.
{% endhint %}

### Supported Platforms <a href="#supported-platforms" id="supported-platforms"></a>

1. Java version 11
2. SonarQube™ Versions 9.9 LTA, 2025.1 LTA and SonarQube Versions 10.0 - 10.8 - Please refer to our [compatibility matrix](https://knowledgebase.autorabit.com/product-guides/codescan/system-requirements-and-installation/installing-codescan-self-hosted#sonarqube-tm-download-1) for more detailed information.
3. SonarJS 6.2+
4. **Operating System (OS)**: Windows, Mac, and Linux
5. Latest available **Node.js LTS** version (v16 as of today)
6. **CodeScan custom rule designer**: This is a designer tool to help build XPath Rules for self-hosted CodeScan. You can download the tool [here](https://license.code-scan.com/index.php/download/login?path=codescan-designer-22.3.jar).

### Web Browser <a href="#web-browser" id="web-browser"></a>

To get the full experience CodeScan has to offer, you must enable JavaScript in your browser.

| Browser        | Version |
| -------------- | ------- |
| Microsoft Edge | Latest  |
| Google Chrome  | Latest  |
| Safari         | Latest  |
