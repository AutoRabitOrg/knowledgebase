# Using IZ Scan CLI

## CI/CD Integration - Using IZ Scan CLI

{% hint style="warning" %}
Before scanning applications using IZ Scan, make sure you have:

* Purchased a valid license for IZ Scan.
* Downloaded and installed **`IZ Scan CLI`** plugin. Download the latest version of **`IZ Scan CLI`** from [latest](../../releases/iz-scan-cli/latest.md)
* Downloaded and installed JDK 11
* Follow the instructions on [Generating Security Token](generate-security-token.md) to generate a security token
{% endhint %}

### CICD Integration

1. Once the appropriate version of **`IZ Scan CLI`** is downloaded, unzip the binary unzip iz-scan-cli-\[VERSION]-\[OS].zip
2. Navigate to the **`bin`** directory within iz-scan-cli-\[VERSION]-\[OS]
3. Run **`iz-scan-cli`** command with the following options
   1. -serviceHost=xxx\
      &#xNAN;_&#x49;Z Scan service URL_
   2. -authToken=xxx\
      &#xNAN;_&#x53;ecurity token generated from the server_
   3. -applicationKey=x.x\
      &#xNAN;_&#x55;nique ID of the application / project being scanned_
   4. -applicationName=.\
      &#xNAN;_&#x4E;ame of the application being scanned_
   5. -source=xxx\
      &#xNAN;_&#x4F;ptional. Location of the project source directory. If ignored, the current directory will be used as the project source directory_
   6. -scmBranchName=xxx + _Optional. SCM branch for which code is being analyzed. If ignored, the default value will be **`master`**_
   7. -pullRequestId=xxx + \_Optional.SCM Pull request name for which code is being analyzed
   8. -organization=xxx + _Optional. Organization under which the project should be categorized. If ignored, the default organization will be used. Value can be any of Organization Name / Id / Ext Id_
   9. -sarifReport=xxx + \_Optional. Used to generate issues in SARIF format. The output report file path must be specified using this parameter.
4.  The complete example may look like&#x20;

    ```
    FALCON_SCAN_BIN_DIRECTORY> ./falcon-scan-cli -serviceHost -authToken -applicationKey orders-eapi -source <PROJECT_ROOT_DIRECTORY> -applicationName="Orders EAPI"
    ```

### Setting Proxy Details

If the system from which the projects are analyzed is configured with a proxy, then set the following environment variable with the proxy server details -

1.  Windows&#x20;

    ```
    set JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=PROXY_HOST -Dhttps.proxyPort=PROXY_PORT -Dhttp.proxyHost=PROXY_HOST -Dhttp.proxyPort=PROXY_PORT -Djava.net.useSystemProxies=true"
    ```
2.  Linux&#x20;

    ```
    export JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=PROXY_HOST -Dhttps.proxyPort=PROXY_PORT -Dhttp.proxyHost=PROXY_HOST -Dhttp.proxyPort=PROXY_PORT -Djava.net.useSystemProxies=true"
    ```

{% hint style="info" %}
* Replace **`PROXY_HOST`** and **`PROXY_PORT`** with appropriate values for Porxy server host and port
* If **`https.proxyPort`** is not specified default value will be 443
* If **`http.proxyPort`** is not specified default value will be 80
{% endhint %}

### See Also

* [Mule Code Coverage](page-2.md)
* [Install IZ Scan for Cloud](../vs-code-extension/install-vs-code-extension-cloud.md)
* [Install IZ Scan for Desktop](../vs-code-extension/install-vs-code-extension-desktop.md)
* [Aborting Builds](terminate-build.md)
