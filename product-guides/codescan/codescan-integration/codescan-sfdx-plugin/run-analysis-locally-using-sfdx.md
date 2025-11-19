# Run analysis locally using SFDX

This article will guide you through how to run the code analysis manually using our **CodeScan Plugin** and **Salesforce CLI**.

## Prerequisites

To run the code analysis manually using our CodeScan Plugin and Salesforce CLI, first make sure you have:

* **Salesforce CLI** installed. Click [HERE](https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm) to download the **Salesforce CLI** and its dependencies.
* **Java 17**
* **Node.js 20**

1. To install the **CodeScan SFDX plugin, follow these steps**:
   * Use **`sfdx plugins:install sfdx-codescan-plugin`**.
   * You'll be prompted that Salesforce does not sign this plugin; type **Y** to continue.
   * Check the installation using sfdx plugins.
2. You're ready to run a scan once the installation is completed. To run this scan, follow these steps:
   * Open **Bash CLI** like **Git Bash**, etc.
   *   Now, go to the folder with the project sources you want to run a scan on and enter the command as shown below:

       <pre data-overflow="wrap" data-full-width="false"><code>sfdx codescan:run --token &#x3C;token> --projectkey &#x3C;project key>> --organization &#x3C;organization key>
       </code></pre>

{% hint style="info" %}
**Note:** To find your **Project Key** and the **Organization Key**, click on the respective links below:

* [Project Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)
* [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)

Project keys differ from project to project as the **organization** and **project keys** are unique.
{% endhint %}

3. This will start the analysis directly on the [CodeScan cloud](https://www.codescan.io/products/cloud/).
4. To learn how to generate a **Security Token**, click [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).
5. If you want to run the analysis in [CodeScan Self-Hosted](https://www.codescan.io/products/self-hosted/), [CodeScan Cloud EU](https://app-eu.codescan.io/), or [CodeScan Cloud AUS](https://app-aus.codescan.io/), then make the following changes in the command:
   * Add _**--server <**&#x53;erver Nam&#x65;**>**_&#x20;
   * Replace **Project key**
   * Replace **Organization key**
   * Replace **Token**
   *   Replace your **server name** (if applicable).

       <pre data-overflow="wrap" data-full-width="true"><code>sfdx codescan:run --token &#x3C;token> --projectkey &#x3C;project key>> --organization &#x3C;organization key> --server &#x3C;Server Name>
       </code></pre>
6.  To view a list of **parameters** and **flags** which you can use, run the following command: **`sfdx help codescan:run`**

    <pre class="language-javascript" data-overflow="wrap" data-full-width="false"><code class="lang-javascript">USAGE:

    $ sfdx codescan:run [name=value...] [-s &#x3C;string>] [-o &#x3C;string>] [-k &#x3C;string>] [-t &#x3C;string>] [-u &#x3C;string>] [-p
      &#x3C;string>] [--noqualitygate] [--javahome &#x3C;string>] [--nofail] [--qgtimeout &#x3C;integer>] [--json] [--loglevel
      trace|debug|info|warn|error|fatal|TRACE|DEBUG|INFO|WARN|ERROR|FATAL]

    OPTIONS
    -k, --projectkey=projectkey        sonar.projectKey - the project key
                                       to create.
                                       
    -o, --organization=organization    CodeScan Organization Id. Only
                                       required when connecting to CodeScan Cloud

    -p, --password=password            SonarQube password (token is preferred)

    -s, --server=server                SonarQube server. Defaults to CodeScan Cloud
                                       (https://app.codescan.io)

    -t, --token=token                  SonarQube token (preferred)

    -u, --username=username            SonarQube username (token is preferred)

    --javahome=javahome                JAVA_HOME to use

    --json                             format output as json

    --loglevel=(trace|debug|info|warn|error|fatal|TRACE|DEBUG|INFO|WARN|ERROR|FATAL) 
                                       [default: warn] logging level for this
                                       command invocation
                                         
    --nofail                           Don't fail if sonar-scanner fails

    --noqualitygate                    Don't wait until the SonarQube background
                                       task is finished and return the build
                                       Quality Gate

    --qgtimeout=qgtimeout              Timeout in seconds to wait for
                                       Quality Gate to complete (default 300)
    </code></pre>
