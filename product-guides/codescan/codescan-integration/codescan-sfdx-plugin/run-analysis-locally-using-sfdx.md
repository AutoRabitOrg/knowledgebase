# Run analysis locally using SFDX

This article will guide you through how to run the code analysis manually using our **CodeScan Plugin** and **Salesforce CLI**.

## Prerequisites

To run the code analysis manually using our CodeScan Plugin and Salesforce CLI, first make sure you have:

* **Salesforce CLI** installed. Click [HERE](https://developer.salesforce.com/docs/atlas.en-us.sfdx\_setup.meta/sfdx\_setup/sfdx\_setup\_install\_cli.htm) to download the **Salesforce CLI** and its dependencies.
* Java 17
* NodeJS 18

Note: If you would want to stay on the lower version of the Java, then you will have to use the previous version of our plugin(1.0.8). It can be done by updating the script with a specific version (e.g. sfdx-codescan-plugin@1.0.8).

1. To install the **CodeScan SFDX plugin, follow these steps**:
   * Use **`sfdx plugins:install sfdx-codescan-plugin`**.
   * You'll be prompted that Salesforce does not sign this plugin; type **Y** to continue.
   * Check the installation using sfdx plugins.
2. You're ready to run a scan once the installation is completed. To run this scan, follow these steps:
   * Open **Bash CLI** like **Git Bash**, etc.
   *   Now, go to the folder with the project sources you want to run a scan on and enter the command as shown below:

       {% code overflow="wrap" fullWidth="false" %}
       ```
       sfdx codescan:run --token <token> --projectkey <project key>> --organization <organization key>
       ```
       {% endcode %}

       Note:To find your **Project Key** and the **Organization Key**, click on the respective links below:

       * [Project Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)
       * [Organization Key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)

       Project keys differ from project to project as the **organization** and **project keys** are unique.
3. This will start the analysis directly on the [CodeScan cloud](https://www.codescan.io/products/cloud/).
4. To learn how to generate a **Security Token**, click [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).
5. If you want to run the analysis in the [CodeScan Self-Hosted](https://www.codescan.io/products/self-hosted/), then make the following changes in the command:
   * Add _**--server <**Server Name**>**_&#x20;
   * Replace **Project key**
   * Replace **Organization key**
   * Replace **Token**
   *   Replace your **server name** (if applicable).

       {% code overflow="wrap" fullWidth="true" %}
       ```
       sfdx codescan:run --token <token> --projectkey <project key>> --organization <organization key>
       ```
       {% endcode %}
6.  To view a list of **parameters** and **flags** which you can use, run the following command: **`sfdx help codescan:run`**

    {% code fullWidth="false" %}
    ```actionscript
    USAGE:

    $ sfdx codescan:run [name=value...] [-s <string>] [-o <string>] [-k <string>] [-t <string>] [-u <string>] [-p
      <string>] [--noqualitygate] [--javahome <string>] [--nofail] [--qgtimeout <integer>] [--json] [--loglevel
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
    ```
    {% endcode %}
