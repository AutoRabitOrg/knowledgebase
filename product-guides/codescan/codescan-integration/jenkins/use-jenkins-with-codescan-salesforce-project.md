# Use Jenkins with CodeScan Salesforce project

The following is a guide to setting up Jenkins for use with CodeScan. It assumes that:

* You have **Jenkins** installed.
* You have the **Ant** and **Git plugins** for Jenkins installed.

### Creating a Jenkins Project to use with [CodeScan](https://www.codescan.io/) <a href="#creating-a-jenkins-project-to-use-with-codescan" id="creating-a-jenkins-project-to-use-with-codescan"></a>

1. Create a **new Freestyle project**.
2. Add a **String parameter**:
   * Name it _**sonar.projectVersion**_
   * Make the default value _**1**_
3. Add another **string parameter**:
   * Name it _**salesforce.username**_
   * Make the default value your Saleforce username eg. **will@example.com**
4. Add a **password parameter**:
   * Name it _**salesforce.password**_
   * Make the default value your Salesforce password + your Salesforce token eg. **passwordtoken**
5. Add another **string parameter**:
   * Name it _**salesforce.url**_
   * Make the default value [https://login.salesforce.com](https://login.salesforce.com/) to pull from your production instance or [https://test.salesforce.com/](https://test.salesforce.com/) to pull from your sandbox instance
6. Add another **string parameter**:
   * Name it _**sonar.projectKey**_
   * Make the default value _**project1**_
7. Add another **string parameter**:
   * Name it _**sonar.projectName**_
   * Make the default value whatever you like. This will be the name displayed in SonarQube™.
8. Add another **string parameter**:
   * Name it _**sonar.host.url**_
   * Make the default value the url of your SonarQube™ instance. The default for SonarQube™ running locally would be **http://localhost:9000**
9. In the build section of the configuration click **Add Build Step > Invoke Ant**.
   * In the targets section write _**deletesrc download**_.
   * In the Build File section, fill in the path to the _**antbuild.xml**_ file in the runner folder of your CodeScan installation. eg. _**C:/great-tools/sonar-salesforce-plugin3.x/runner/antbuild.xml**_
   * In the Properties section, type _**user.dir=${WORKSPACE}**_
   * Leave the Java options blank.
10. Add another **Invoke Ant step**:
    * In the targets section write _**sonar**_.
    * In the Build File section, fill in the path to the _**antbuild.xml**_ file in the runner folder of your CodeScan installation. eg. _**C:/great-tools/sonar-salesforce-plugin3.x/runner/antbuild.xml**_
    * In the Properties section, type _**user.dir=${WORKSPACE}**_
    * In the java options add the path to your temp directory. eg. **-Djava.io.tmpdir=C:\Users\some-guy\AppData\Local\Temp**\\
    * You can also add _**-Xmx1024m**_ to the end of the Java options field to assign memory.

Save the **project** and click **Build with Parameters**. The results will be available in SonarQube™.
